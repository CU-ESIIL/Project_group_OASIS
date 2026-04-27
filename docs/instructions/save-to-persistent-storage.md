---
layout: page
title: Save Files to Persistent Storage
permalink: /instructions/save/
---

# Save Files to Persistent Storage

This page covers moving data and larger outputs between your JupyterLab instance and persistent storage using `gocmd`. Use GitHub for code, Markdown, notebooks, and small files. Use persistent storage for files that are too large for GitHub or need to survive after the container stops.

## The CRT cloud workflow

In the Cloud Triangle, this page covers **instance to/from persistent storage**.

!!! info "Cloud Triangle pages"
    1. [Connect instance to GitHub](link-to-github.md)
    2. [Instance to/from GitHub](push-to-github.md)
    3. **Instance to/from persistent storage:** this page

!!! tip "What goes where?"
    Code and text go to GitHub. Large data and outputs go to persistent storage. Active work happens in JupyterLab.

| Task | Best tool |
|---|---|
| Edit the website text | GitHub / Git widget |
| Save a notebook or script | GitHub / Git widget |
| Save a small figure used on the site | GitHub / Git widget |
| Save a large dataset | Persistent storage / `gocmd` |
| Save model outputs or large intermediate files | Persistent storage / `gocmd` |
| Work interactively during a session | JupyterLab |
| Share final public code | GitHub |
| Share final public data | Persistent storage or approved data archive |

Persistent storage is not a replacement for GitHub. It will keep your data safe, but it does not provide the same version history, issue tracking, pull requests, or website publishing workflow. For large files, save them here and commit a small note or metadata file to GitHub that explains where the data lives.

## 0) One-time setup

Open a JupyterLab terminal and install GoCommands:

```bash
# Install GoCommands (Linux x86_64)
GOCMD_VER=$(curl -L -s https://raw.githubusercontent.com/cyverse/gocommands/main/VERSION.txt); \
curl -L -s https://github.com/cyverse/gocommands/releases/download/${GOCMD_VER}/gocmd-${GOCMD_VER}-linux-amd64.tar.gz | tar zxvf -
```

Configure iRODS. Accept defaults for host, port, and zone. Use your CyVerse username when prompted.

```bash
./gocmd init
```

Check that you can list your CyVerse home folder:

```bash
./gocmd ls i:/iplant/home/YOUR_USER
```

The `i:` prefix means an iRODS remote path. Local paths, such as `outputs/run-YYYYMMDD`, do not use `i:`.

## 1) Set your group paths

The shared community folder root is:

```text
i:/iplant/home/shared/esiil/Innovation_summit/<GROUP_NAME>
```

Set these environment variables in your terminal. Change the group name and username first.

```bash
# Edit these two lines
GROUP_NAME="Group_1"
USERNAME="<your_cyverse_username>"

COMMUNITY="i:/iplant/home/shared/esiil/Innovation_summit/${GROUP_NAME}"
PERSONAL="i:/iplant/home/${USERNAME}"
```

Use descriptive folders inside `${COMMUNITY}`, such as:

- `shared_data/`
- `outputs/`
- `deliverables/`
- `scratch/`

## 2) Save files from the instance to persistent storage

Use `put` to upload local files from JupyterLab to the CyVerse Data Store.

```bash
# Put (upload) a local folder into your group's community space
LOCAL_SRC="outputs/run-YYYYMMDD"
REMOTE_DST="${COMMUNITY}/outputs/"

./gocmd put --progress -K --icat -r "${LOCAL_SRC}" "${REMOTE_DST}"
```

Use `--diff` when re-uploading so unchanged files are skipped:

```bash
./gocmd put --progress -K --icat --diff -r "${LOCAL_SRC}" "${REMOTE_DST}"
```

Verify the upload:

```bash
./gocmd ls "${REMOTE_DST}"
```

## 3) Bring files from persistent storage into the instance

Use `get` to download shared data or outputs from persistent storage into the running JupyterLab instance.

```bash
# Get (download) a shared dataset from the community folder into ./data/
mkdir -p ./data
REMOTE_SRC="${COMMUNITY}/shared_data/"
LOCAL_DST="./data/"

./gocmd get --progress -K --icat -r "${REMOTE_SRC}" "${LOCAL_DST}"
```

Use this when your team has prepared shared data in persistent storage and you need a local copy for analysis.

## 4) Copy files between community and personal storage

Use `cp` to copy directly between two Data Store locations.

```bash
REMOTE_SRC="${COMMUNITY}/deliverables/"
REMOTE_PERSONAL_DST="${PERSONAL}/projects/innovation_summit_2026/deliverables/"

./gocmd cp --progress -K --icat -r "${REMOTE_SRC}" "${REMOTE_PERSONAL_DST}"
```

Verify the copied files:

```bash
./gocmd ls "${REMOTE_PERSONAL_DST}"
```

## 5) Record where the data lives

After saving large data or outputs to persistent storage, add a small note to GitHub so teammates can find it later.

Good places for that note:

- `docs/index.md`, if the data supports a public figure or result
- `data.md`, if the project has dataset notes
- a small README next to the analysis code

Example note:

```markdown
Large model outputs are stored in:
`i:/iplant/home/shared/esiil/Innovation_summit/Group_1/outputs/fire-spread-run-01/`
```

## Troubleshooting

If a path is not found, list upward and then drill down to confirm exact folder names:

```bash
./gocmd ls i:/iplant/home/shared/esiil/Innovation_summit
./gocmd ls i:/iplant/home/shared/esiil/Innovation_summit/${GROUP_NAME}
```

If a collection exists but transfers fail, inspect its type and permissions:

```bash
./gocmd stat i:/iplant/home/shared/esiil/Innovation_summit/${GROUP_NAME}/<EXACT_NAME>
```

If a transfer is interrupted, rerun the command with `--diff` so GoCommands can skip files that already transferred.

More information: [CyVerse GoCommands Docs](https://learning.cyverse.org/ds/gocommands/)
