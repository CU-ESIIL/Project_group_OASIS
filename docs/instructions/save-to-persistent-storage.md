---
layout: page
title: Save to persistent storage
permalink: /instructions/save/
---

# Save to Persistent Storage with GoCommands

### 0) One-time setup (install + login)
```bash
# Install GoCommands (Linux x86_64)
GOCMD_VER=$(curl -L -s https://raw.githubusercontent.com/cyverse/gocommands/main/VERSION.txt); \
curl -L -s https://github.com/cyverse/gocommands/releases/download/${GOCMD_VER}/gocmd-${GOCMD_VER}-linux-amd64.tar.gz | tar zxvf -

# Configure iRODS (accept defaults for Host/Port/Zone; use your CyVerse creds)
./gocmd init
./gocmd auth login  # follow prompts to authenticate with CyVerse
```

**Community folder root (read/write for teams):**
```
i:/iplant/home/shared/esiil/Innovation_summit/<GROUP_NAME>
```

Set environment variables:
```bash
# —— Edit these two lines ——
GROUP_NAME="Group_1"                  # <-- change to your group
USERNAME="<your_cyverse_username>"    # <-- no angle brackets

COMMUNITY="i:/iplant/home/shared/esiil/Innovation_summit/${GROUP_NAME}"
PERSONAL="i:/iplant/home/${USERNAME}"
```

> **Note:** GoCommands uses `i:` to denote paths on the CyVerse Data Store. Include this prefix for any remote path (for example, `i:/iplant/home/...`). Local filesystem paths should not have the `i:` prefix.

---

## A) Save data **to the community folder**
```bash
# Put (upload) a local folder into your group’s community space
LOCAL_SRC="outputs/run-YYYYMMDD"
REMOTE_DST="${COMMUNITY}/outputs/"

./gocmd put --icat --retry 3 -d -k -r "${LOCAL_SRC}" "${REMOTE_DST}"
```
- `put` uploads from local → CyVerse Data Store
- `-r` is recursive; `--diff` (optional) only sends changed files

Verify upload:
```bash
./gocmd ls "${REMOTE_DST}"
```

---

## B) **Pull** data **from the community folder**
```bash
# Get (download) a shared dataset from the community folder into ./data/
mkdir -p ./data
REMOTE_SRC="${COMMUNITY}/shared_data/"
LOCAL_DST="./data/"

./gocmd get --icat --retry 3 -d -k -r "${REMOTE_SRC}" "${LOCAL_DST}"
```
- `get` downloads from CyVerse → local machine
- Use for pulling common datasets your team prepared

---

## C) **Move** data from the community folder **to your personal space**
```bash
# Copy directly between two Data Store locations
REMOTE_SRC="i:/iplant/home/shared/esiil/Innovation_summit/${GROUP_NAME}/deliverables/"
REMOTE_PERSONAL_DST="i:/iplant/home/${USERNAME}/projects/innovation_summit_2025/deliverables/"

./gocmd cp --icat --retry 3 -d -k -r "${REMOTE_SRC}" "${REMOTE_PERSONAL_DST}"

# Verify contents
./gocmd ls "${REMOTE_PERSONAL_DST}"
```

---

## Notes & Best Practice
- Use **descriptive subfolders** in `${COMMUNITY}` (e.g., `shared_data/`, `outputs/`, `deliverables/`).
- Always add `--diff` when re-uploading to avoid resending unchanged files.
- Use `./gocmd ls <path>` to explore or confirm folder structure.
- To reorganize: safest workflow is **get locally → restructure → put back**.

**More info:** [CyVerse GoCommands Docs](https://learning.cyverse.org/ds/gocommands/)
