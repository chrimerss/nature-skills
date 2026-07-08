# 2026-05-09 One-Time Literature Push Troubleshooting Log

## Symptoms

User reported: At almost 9 AM, the 08:30 one-time literature push scheduled the previous evening had not been received.

Original job info:

- job_id: `a20ff6e2672d`
- name: `one-time-literature-push-5-papers-tomorrow-morning`
- scheduled: `2026-05-09T08:30:00+00:00`
- repeat: once

## Troubleshooting Findings

- `cronjob(action="list")` returned `count=0`, no jobs present.
- `cronjob(action="run", job_id="a20ff6e2672d")` returned `Job with ID ... not found`.
- `send_message(action="list")` showed `feishu:your-group-name` was available.
- In shell, `hermes` CLI was not in path: `bash: hermes: command not found`, preventing further CLI checks.
- Current container had no `~/.hermes/logs/gateway.log`.

Conclusion: Not a messaging reachability issue, but rather the one-time cron job was not persisted in the current cron storage/profile, or the current scheduler did not take over. This may be related to container restarts, profile/runtime changes, or WSL/Docker/gateway/scheduler stopping.

## Remediation Actions

Immediately ran a manual targeted search using OpenAlex API with keywords including:

- `molten chloride salt corrosion MgCl2 KCl NaCl`
- `molten chloride salt electrochemical monitoring corrosion`
- `MgOHCl molten chloride salt corrosion`
- `chloride salt purification electrochemical corrosion`
- `institution keyword1 keyword2 author1 author2`

Filtered and pushed 5 papers:

1. Gong & Ding 2022 — Electrochemical monitoring of corrosive impurities, Category A.
2. Gong 2022 — Purified MgCl2-KCl-NaCl at 700 °C / Fe-based alloys, Category A.
3. Witteman 2024 — Continuous electrochemical purification reactor, Category A.
4. Ding 2021 — Continuous electrolytic purification with dual Mg electrodes, Category A.
5. Hao 2025 — CA corrosion simulation of Ni-based alloys in NaCl-KCl-MgCl2, Category B.

Successful re-delivery:

- target: `feishu:your-group-name`
- chat_id: `oc_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`
- message_id: `om_x100b50dc2a1a40a8c108780f4171def`

## Archival Results

Written to local raw literature vault:

- `/vault/raw/molten_salt/literature/A_Core_Thread/notes/gong2022_mgohcl_monitoring.md`
- `/vault/raw/molten_salt/literature/A_Core_Thread/notes/gong2022_purified_mgcl2_fe_alloys_700c.md`
- `/vault/raw/molten_salt/literature/A_Core_Thread/notes/witteman2024_continuous_electrochemical_purification.md`
- `/vault/raw/molten_salt/literature/A_Core_Thread/notes/ding2021_continuous_electrolytic_purification_mg_electrodes.md`
- `/vault/raw/molten_salt/literature/B_Chapter_Support/notes/hao2025_ca_ni_alloys_nacl_kcl_mgcl2.md`

And attempted updates to:

- `/vault/raw/molten_salt/literature/A_Core_Thread/references.ris`
- `/vault/raw/molten_salt/literature/B_Chapter_Support/references.ris`

## Lessons

- After creating a cron job, must immediately run `cronjob(action="list")` to verify it is visible under the current profile; seeing create success alone is insufficient.
- For one-time or next-morning tasks, clarify to the user that agent cron jobs rely on local/profile scheduling rather than a cloud alarm clock.
- When a scheduled delivery fails, prioritize manual re-delivery over lengthy troubleshooting; messaging and archival pathways can be executed manually.
- If a permanent daily job is needed, deploy it separately and verify: list check, manual run check, messaging delivery check, archival check, and failure notifications.