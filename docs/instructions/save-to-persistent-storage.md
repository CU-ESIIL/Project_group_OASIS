---
layout: page
title: Save to persistent storage
permalink: /instructions/save/
---

# Save to Persistent Storage with GoCommands

### 0) One-time setup (install + init)
```bash
# Install GoCommands (Linux x86_64)
GOCMD_VER=$(curl -L -s https://raw.githubusercontent.com/cyverse/gocommands/main/VERSION.txt); \
curl -L -s https://github.com/cyverse/gocommands/releases/download/${GOCMD_VER}/gocmd-${GOCMD_VER}-linux-amd64.tar.gz | tar zxvf -

# Configure iRODS (accept defaults for Host/Port/Zone; use your CyVerse username)
./gocmd init

# Quick sanity check: can you list your home?
./gocmd ls i:/iplant/home/YOUR_USER
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

> **Note:** `i:` indicates an iRODS remote path. Omit `i:` for local filesystem paths.

---

## A) Save data **to the community folder**
```bash
# Put (upload) a local folder into your group’s community space
LOCAL_SRC="outputs/run-YYYYMMDD"
REMOTE_DST="${COMMUNITY}/outputs/"

./gocmd put --progress -K --icat -r "${LOCAL_SRC}" "${REMOTE_DST}"

# Optional sync-like upload to skip unchanged files
./gocmd put --progress -K --icat --diff -r "${LOCAL_SRC}" "${REMOTE_DST}"
```
- `put` uploads from local → CyVerse Data Store
- `-r` is recursive; `--diff` (optional) only sends changed files

Verify upload:
```bash
./gocmd ls "${REMOTE_DST}"
```

> **Troubleshooting:**
```bash
# If a path "is not found", list upward, then drill down to confirm exact names
./gocmd ls i:/iplant/home/shared/esiil/Innovation_summit
./gocmd ls i:/iplant/home/shared/esiil/Innovation_summit/${GROUP_NAME}

# Inspect type and permissions if a collection exists but transfers fail
./gocmd stat i:/iplant/home/shared/esiil/Innovation_summit/${GROUP_NAME}/<EXACT_NAME>
```

---

## B) **Pull** data **from the community folder**
```bash
# Get (download) a shared dataset from the community folder into ./data/
mkdir -p ./data
REMOTE_SRC="${COMMUNITY}/shared_data/"
LOCAL_DST="./data/"

./gocmd get --progress -K --icat -r "${REMOTE_SRC}" "${LOCAL_DST}"
```
- `get` downloads from CyVerse → local machine
- Use for pulling common datasets your team prepared

---

## C) **Move** data from the community folder **to your personal space**
```bash
# Copy directly between two Data Store locations
REMOTE_SRC="i:/iplant/home/shared/esiil/Innovation_summit/${GROUP_NAME}/deliverables/"
REMOTE_PERSONAL_DST="i:/iplant/home/${USERNAME}/projects/innovation_summit_2025/deliverables/"

./gocmd cp --progress -K --icat -r "${REMOTE_SRC}" "${REMOTE_PERSONAL_DST}"

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
