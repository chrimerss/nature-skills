#!/usr/bin/env python3
"""Run deterministic structural checks on patent claims."""

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path


CLAIM_START = re.compile(r"(?m)^\s*(\d+)\s*\.\s*")
REFERENCE = re.compile(
    r"claim\s*(\d+)(?:\s*(?:to|-|through)\s*(\d+))?"
    r"|claim\s*(\d+)\s*(?:or|,|and)\s*(\d+)",
    re.IGNORECASE,
)
TERM_INTRO = re.compile(r"(?:said|the)\s+([a-zA-Z][a-zA-Z0-9_-]{1,30})", re.IGNORECASE)
PLACEHOLDER = re.compile(r"\[TO CONFIRM[^\]]*\]", re.IGNORECASE)


@dataclass
class Finding:
    level: str
    claim: int | None
    code: str
    message: str


def split_claims(text: str) -> list[tuple[int, str]]:
    matches = list(CLAIM_START.finditer(text))
    claims = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        claims.append((int(match.group(1)), text[match.end() : end].strip()))
    return claims


def references(body: str) -> list[int]:
    result = []
    for match in REFERENCE.finditer(body):
        if match.group(1):
            start = int(match.group(1))
            finish = int(match.group(2) or start)
            result.extend(range(start, finish + 1))
        else:
            result.extend((int(match.group(3)), int(match.group(4))))
    return sorted(set(result))


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def audit(text: str) -> list[Finding]:
    claims = split_claims(text)
    findings = []
    if not claims:
        return [Finding("ERROR", None, "NO_CLAIMS", "No claims starting with '1.' detected.")]

    numbers = [number for number, _ in claims]
    expected = list(range(1, len(claims) + 1))
    if numbers != expected:
        findings.append(
            Finding("ERROR", None, "NUMBER_SEQUENCE", f"Claim numbers should be consecutive {expected}, found {numbers}.")
        )

    previous_text = ""
    claim_map = {}
    for number, body in claims:
        compact = normalize(body)
        claim_map[number] = compact
        refs = references(body)

        if not body:
            findings.append(Finding("ERROR", number, "EMPTY", "Claim body is empty."))
            continue
        if PLACEHOLDER.search(body):
            findings.append(
                Finding("ERROR", number, "PLACEHOLDER", "Formal claims still contain confirmation placeholders.")
            )
        if number == 1 and refs:
            findings.append(
                Finding("ERROR", number, "INDEPENDENT_REFERENCE", "Claim 1 should not reference other claims.")
            )
        if number > 1 and not refs:
            findings.append(
                Finding("WARNING", number, "NO_REFERENCE", "No dependency reference detected; verify if this is intended as an independent claim.")
            )
        for ref in refs:
            if ref >= number:
                findings.append(
                    Finding("ERROR", number, "FORWARD_REFERENCE", f"References a subsequent claim {ref}.")
                )
            if ref not in claim_map:
                findings.append(
                    Finding("ERROR", number, "MISSING_REFERENCE", f"Referenced claim {ref} does not exist.")
                )

        if not re.search(r"(comprising|characterized in that|comprises|including|consisting of)", compact, re.IGNORECASE):
            findings.append(
                Finding("WARNING", number, "TRANSITION", "No standard transition phrase ('comprising', 'characterized in that', etc.) detected.")
            )
        if len(compact) < 25:
            findings.append(
                Finding("WARNING", number, "TOO_SHORT", "Claim is relatively short; verify that it completely defines the technical solution.")
            )
        if re.search(r"\b(better|superior|significantly improved|greatly improved|best|optimal)\b", compact, re.IGNORECASE):
            findings.append(
                Finding("WARNING", number, "RESULT_LANGUAGE", "Contains promotional or result-only language; verify whether technical limitations should be used instead.")
            )

        searchable_basis = previous_text + " ".join(
            claim_map.get(ref, "") for ref in refs
        )
        for match in TERM_INTRO.finditer(body):
            term = match.group(1).lower()
            if term in {"method", "apparatus", "device", "system", "step", "program", "medium", "process", "invention"}:
                continue
            if term not in searchable_basis.lower() and compact.lower().find(term) <= 15:
                findings.append(
                    Finding(
                        "WARNING",
                        number,
                        "ANTECEDENT_BASIS",
                        f"Term '{term}' introduced with 'said/the' may lack clear antecedent basis.",
                    )
                )
        previous_text += " " + compact

    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("claims", type=Path, help="UTF-8 claims text file")
    parser.add_argument("--json", action="store_true", help="Output findings as JSON")
    args = parser.parse_args()

    text = args.claims.read_text(encoding="utf-8")
    findings = audit(text)
    if args.json:
        print(json.dumps([finding.__dict__ for finding in findings], ensure_ascii=False, indent=2))
    elif not findings:
        print("PASS: No claim structural issues detected.")
    else:
        for finding in findings:
            location = f"Claim {finding.claim}" if finding.claim else "Overall"
            print(f"{finding.level}\t{location}\t{finding.code}\t{finding.message}")
        errors = sum(finding.level == "ERROR" for finding in findings)
        warnings = sum(finding.level == "WARNING" for finding in findings)
        print(f"\nSummary: {errors} error(s), {warnings} warning(s)")

    return 1 if any(finding.level == "ERROR" for finding in findings) else 0


if __name__ == "__main__":
    raise SystemExit(main())
