# nature-downloader

<p align="center">
  <img src="assets/banner.jpg" alt="nature-downloader — Completing the missing PDF retrieval step in the Nature workflow" width="100%">
</p>

`nature-downloader` is an academic full-text/PDF download skill operating under legitimate institutional entitlements. It integrates two primary capabilities:

- **Initial Resource Portal Setup**: Records the electronic resource portal link actually used by the researcher, identifies the university, SSO/CARSI/EZproxy/WebVPN/resource aggregation platform information, and saves the configuration to `~/.config/lit-dl/school.json`.
- **Authentic Full-Text Retrieval**: Reuses the user's logged-in Chrome session via a web-access CDP proxy to download legally accessible PDFs into the project folder. If the library subscription only provides HTML full text, it saves the HTML/text and explicitly notes that no PDF is available.
- **Chinese Literature Defaulting to CNKI**: When downloading by Chinese title, it defaults to using the user's logged-in/authorized CNKI portal; a dedicated library CNKI portal can be specified via school configuration or `--cnki-url`.
- **Open Access Priority**: If an article is Open Access or published in an open journal, it retrieves the legal OA PDF directly. If the institutional library explicitly lacks entitlement, it informs the user directly.

It does NOT bypass paywalls, use mirror sites, break CAPTCHAs, or read/export cookies, passwords, localStorage, or session files. When encountering SSO/CARSI logins, CAPTCHAs, Cloudflare checks, SMS/OTP, or human verification, it pauses and prompts the user to complete the step in Chrome.

## Quick Start

Copy the following instruction to your agent to automatically guide you through initial setup:

```text
Please use the nature-downloader skill to help me complete initial library resource setup: ask me for my library's electronic resource/database portal link, identify the authorization path, and save the configuration; if login is needed, guide me to complete SSO/CARSI authentication in Chrome; finally, run configuration display and connectivity health check to confirm that the library resource can be reused for literature downloading.
```

### 1. Configure Resource Portal

For new users, prioritize providing the library electronic resource/database portal link rather than entering a university name:

```bash
python3 scripts/configure_school.py infer "https://whu.metaersp.cn/personalIndex"
python3 scripts/configure_school.py url "https://whu.metaersp.cn/personalIndex"
python3 scripts/configure_school.py show
```

`infer` only evaluates the authorization path without saving; `url` writes to the configuration. For example, Wuhan University's `whu.metaersp.cn` will be identified as a resource aggregation portal, redirecting to `cas.whu.edu.cn` when login is required.

If no resource portal link is available, use preset universities as a fallback:

```bash
python3 scripts/configure_school.py preset ShanghaiJiaoTongUniversity
python3 scripts/configure_school.py show
```

View available presets:

```bash
python3 scripts/configure_school.py list
```

Run connectivity health check:

```bash
python3 scripts/configure_school.py health --force
```

The default configuration path is `~/.config/lit-dl/school.json`. For testing or multi-profile scenarios, override it using `LIT_DL_CONFIG_DIR=/path/to/configdir`.

### 2. Prepare Browser Login State

1. Open your university library or academic resource aggregation portal in Chrome.
2. Complete SSO/CARSI login using your institutional credentials.
3. Confirm that Web of Science or target publisher pages display full-text links normally in Chrome.
4. Open `chrome://inspect/#remote-debugging` and allow remote debugging for the current browser instance.
5. Start the web-access CDP proxy.

### 3. Download Literature

Download by DOI:

```bash
node scripts/batch_download.mjs \
  --dois "10.1007/s00122-021-03957-1,10.1111/pbi.14066" \
  --out "./literature-automatic-download"
```

Download by Chinese title (defaults to CNKI):

```bash
node scripts/batch_download.mjs \
  --title "Digital Governance under Rural Revitalization" \
  --out "./literature-automatic-download"
```

If you only want PDF and not CAJ, add `--cnki-format pdf`. When CNKI has no explicit PDF download button, the script will report that no authorized PDF was found rather than saving `.caj`:

```bash
node scripts/batch_download.mjs \
  --title "Digital Governance under Rural Revitalization" \
  --cnki-format pdf \
  --out "./literature-automatic-download"
```

If the university library provides a dedicated CNKI portal, specify it explicitly:

```bash
node scripts/batch_download.mjs \
  --title "Digital Governance under Rural Revitalization" \
  --cnki-url "https://kns.cnki.net/kns8s/defaultresult/index" \
  --out "./literature-automatic-download"
```

Search by topic on Web of Science and download the top N papers:

```bash
node scripts/batch_download.mjs \
  --topic "rice blast resistance gene" \
  --count 10 \
  --out "./literature-automatic-download"
```

Download Open Access papers by exact title (suitable for arXiv papers or papers without DOIs):

```bash
node scripts/batch_download.mjs \
  --title "Attention Is All You Need" \
  --open-access \
  --out "./literature-automatic-download"
```

Download and verify directly when the PDF address is known:

```bash
node scripts/batch_download.mjs \
  --pdf-url "https://arxiv.org/pdf/1706.03762" \
  --title "Attention Is All You Need" \
  --out "./literature-automatic-download"
```

By default, only the main PDF is downloaded. Include supporting information only when explicitly requested:

```bash
node scripts/batch_download.mjs --dois "10.xxxx/example" --out "./literature-automatic-download" --si
```

Output directory:

```text
literature-automatic-download/
  PDFs/
  SupportingInformation/
```

The script outputs JSON status. Common statuses include `downloaded`, `open_access_downloaded`, `full_text_html_available`, `library_no_permission`, `carsi_waiting_user`, `publisher_verification_waiting_user`, `sciencedirect_robot_check`, `no_authorized_pdf_found`, and `failed_after_retry`. When the status is `full_text_html_available`, it indicates that readable HTML full text was retrieved but no valid PDF is available under the current entitlement; this must be clearly explained to the user. When the status is `library_no_permission`, it indicates that the institutional library lacks full-text entitlement for the reference, which must also be explicitly stated.

## Current Implementation Boundaries

- Implemented: School configuration, config file I/O, preset library, connectivity health checks, Web of Science portal config reading, PDF download under Chrome login state, PDF header verification, status code system.
- Implemented: Chinese title defaulting to CNKI routing, reusing Chrome library/CNKI login state to download authorized PDF/CAJ; `--cnki-format pdf` can be used to restrict downloads to PDF only.
- Verified Path: Shanghai Jiao Tong University (SJTU) + Web of Science + CARSI/Chrome session as the primary real-world download path.
- New User Setup Policy: Prioritizes identifying authorization chains from library resource portal links; school presets serve as a fallback.
- Verified Open Access Path: `--title "Attention Is All You Need" --open-access` accurately matches arXiv titles and downloads PDFs.
- Workflow Strategy: Open Access articles are downloaded directly; non-OA articles route through configured library resources; lack of institutional entitlement is explicitly communicated to the user.
- Extensible Paths: Other universities can be configured via `data/schools.yaml` for SSO/CARSI and `discovery.web_of_science_url`.
- Out of Scope: Downloading without login state, bypassing publisher restrictions, automated handling of CAPTCHA/OTP/Cloudflare, unlimited batch downloading.
- Note: `--topic` performs a Web of Science topic search and does not guarantee exact title matching; prioritize `--title` for exact titles.

## Dependencies

```bash
pip install -r requirements.txt
node --version  # Node.js 22+ recommended
```

## Verification

```bash
python3 -m unittest discover -s tests/python
node --test tests/unit/*.test.mjs
node --check scripts/batch_download.mjs
node --check scripts/browser_pdf_downloader.mjs
```

See `SKILL.md` for the complete workflow, security boundaries, status code system, and failure handling.
