---
layout: page
title: Setting up SSH for GitHub in JupyterHub
permalink: /instructions/link/
---

# Setting up SSH for GitHub in JupyterHub

This page walks you through generating an SSH key inside JupyterHub and adding it to your GitHub account. This setup allows you to push and pull without typing a Personal Access Token each time.

> **Prereq:** Open a **Jupyter Notebook**, paste the code below into a cell, and click the **Run/Play ▶️** button to execute it.

[![Launch in CyVerse DE](https://img.shields.io/badge/Launch-CyVerse%20DE-0b6efd?style=flat-square)](https://de.cyverse.org/apps/de/faf1d268-44cc-11ed-9715-008cfa5ae621/launch?saved-launch-id=dc65718e-1964-4d11-99ad-bf901cddda99)

---

## 1) Run this one‑cell setup script in a Notebook

Paste the entire block into a new cell and run it. It will:

* prompt for your **GitHub username/email** (used for commit identity),
* create an **Ed25519 SSH keypair** at `~/.ssh/github` and a matching SSH config entry for `github.com`,
* start `ssh-agent`, add your key, and
* add `github.com` to `~/.ssh/known_hosts` to avoid first‑connect prompts.

```python
import os, subprocess, textwrap

def add_github_to_known_hosts():
    ssh_dir = os.path.expanduser("~/.ssh")
    known_hosts = os.path.join(ssh_dir, "known_hosts")
    os.makedirs(ssh_dir, exist_ok=True)
    out = subprocess.run(
        ["ssh-keyscan", "-t", "rsa,ed25519", "github.com"],
        capture_output=True, text=True, check=True
    ).stdout.strip()
    with open(known_hosts, "a") as fh:
        if out:
            fh.write(out + "\n")
    print("github.com added to known_hosts")


def configure():
    username = input("GitHub username: ")
    email = input("GitHub email: ")

    subprocess.run(["git", "config", "--global", "user.name", username], check=True)
    subprocess.run(["git", "config", "--global", "user.email", email], check=True)

    ssh_dir = os.path.expanduser("~/.ssh")
    os.makedirs(ssh_dir, exist_ok=True)
    key_path = os.path.join(ssh_dir, "github")  # ~/.ssh/github and github.pub

    # Create Ed25519 keypair (no passphrase for this ephemeral VM)
    subprocess.run(["ssh-keygen", "-t", "ed25519", "-f", key_path, "-N", ""], check=True)

    # Minimal SSH config entry
    cfg_path = os.path.join(ssh_dir, "config")
    block = textwrap.dedent(f"""\
    Host github.com
      HostName github.com
      User git
      IdentityFile {key_path}
    """)
    with open(cfg_path, "a") as fh:
        fh.write(block)

    # Start agent and add key
    subprocess.run(f'eval "$(ssh-agent -s)" && ssh-add {key_path}', shell=True, check=True)

    add_github_to_known_hosts()

    with open(key_path + ".pub") as fh:
        pub = fh.read().strip()
    print("\nPublic key — copy to GitHub → Settings → SSH keys:\n")
    print(pub, "\n")

configure()
```

When the cell finishes, the **last lines of output** show your **public key** (starts with `ssh-ed25519`). **Copy** that entire line.

---

## 2) Add the key to GitHub

1. In a new browser tab, go to **GitHub**.
2. Click your **profile picture (top‑right)** → **Settings**.
3. In the left menu, click **SSH and GPG keys** → **New SSH key**.
4. Title: *JupyterHub Key* (or similar).
5. Paste the **public key** you copied from the Notebook into the **Key** box.
6. Click **Add SSH key**.

---

## 3) Test the connection

Back in JupyterHub, open a **Terminal** and run:

```bash
ssh -T git@github.com
```

You should see:

```
Hi <your-username>! You've successfully authenticated, but GitHub does not provide shell access.
```

---

## 4) Ensure your repo uses SSH (not HTTPS)

When you clone or set your remote, **always copy the SSH link** from GitHub, not the HTTPS link.

### How to get the SSH link

1. Go to your repository page on GitHub.
2. Click the green **Code** button.
3. In the pop‑up, choose the **SSH** tab.
4. Copy the URL (looks like `git@github.com:ORG/REPO.git`).

   * ⚠️ Do **not** copy the HTTPS link (`https://github.com/...`), or GitHub will keep asking for a Personal Access Token.

Example:

```
git@github.com:CU-ESIIL/home.git
```

### Check your remote inside JupyterHub

Open a Terminal in JupyterHub and run:

```bash
git remote -v
```

If you see `https://...`, change it to SSH:

```bash
git remote set-url origin git@github.com:<org-or-user>/<repo>.git
```

---

## 5) Notes & troubleshooting

* The script adds an entry to `~/.ssh/config` so `github.com` will automatically use the new key at `~/.ssh/github`.
* Some Hubs reset the agent between sessions. If you later see `Permission denied (publickey)`, re‑run:

```bash
eval "$(ssh-agent -s)" && ssh-add ~/.ssh/github
```

* If `ssh -T git@github.com` hangs on first use, ensure `github.com` is in `known_hosts` (the script already does this) or run:

```bash
ssh-keyscan -t rsa,ed25519 github.com >> ~/.ssh/known_hosts
```

You’re now ready to use the **Git widget** page to **Pull → Stage → Commit → Push** without PAT prompts.
