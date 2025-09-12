---
layout: page
title: RStudio Proxy Workaround
permalink: /instructions/open-rstudio/
---

# RStudio Proxy Workaround (JupyterHub)

I’m sorry it’s sometimes difficult to open RStudio, but here is the hack to make it work.

---

## The two links you need

When you click the RStudio button in JupyterLab, it will open a **blank tab**. Keep that tab open — it is the live connection to the proxy server. Into that blank tab, paste these two links one after the other:

1. **Login link (Link A)**

   ```
   https://<INSTANCE>.cyverse.run/rstudio/auth-sign-in
   ```
2. **RStudio link (Link B)**

   ```
   https://<INSTANCE>.cyverse.run/rstudio/
   ```

Replace `<INSTANCE>` with the instance number from your JupyterHub URL (the long ID string after `/user/`).

---

## How to use them

1. Paste **Link A** into the blank RStudio tab and press **Enter**.

   * Expected: It may fail or redirect you to a login page. Log in if prompted.
2. After login, paste **Link B** into the same blank tab and press **Enter**.

   * Expected: RStudio should now load in that tab.

You only need to do this **once per session**. After that, RStudio will keep working until you shut down your JupyterHub instance. Next time you start a new instance, repeat the process.

---

## Quick checks if it still fails

* Be sure you replaced `<INSTANCE>` with your actual instance number.
* Use the same blank tab that the RStudio button opened.
* Try a **hard refresh** (Cmd/Ctrl+Shift+R) if the second link doesn’t load.
* If you close your instance and start a new one, repeat the steps with the new instance number.

---

## Primer: Why this is needed

RStudio runs through a **proxy server** inside JupyterHub. The proxy makes sure only authenticated users can access their private RStudio sessions. Sometimes the automatic login handshake doesn’t complete, which is why you have to visit the **auth link** first, then the **RStudio link**. The first link is like showing your badge at the front desk, and the second link is like walking into your office.

