# GitHub release guide — Feirmeoir v0.1.0

This repository ZIP is designed to be unpacked into a new GitHub repository. **Do not upload the original mixed-source distribution ZIP as-is**; use the prepared repository and the separate offline download below.

## Suggested repository details

- **Name:** `Feirmeoir`
- **Description:** `A family, a farm, a future — a browser adaptation of Michael Robinson’s historical farming board game.`
- **Topics:** `board-game`, `browser-game`, `farming-game`, `turn-based`, `worker-placement`, `javascript`, `html5`, `offline-game`, `irish-history`, `pass-and-play`
- **Website:** set to your live GitHub Pages URL once deployed (do not enter a guessed address).
- **Social preview:** optionally upload `media/social-preview.png` under the repository’s social-preview settings.

## Create the release

1. Upload the contents of **Feirmeoir-v0.1.0-GitHub-Source.zip** into a repository (default branch `main`).
2. Confirm **CI / Verify Feirmeoir** passes.
3. In **Settings → Pages**, select **GitHub Actions** as the source. Confirm the Pages workflow passes.
4. Create a GitHub release with the tag **`v0.1.0`**, title **`Feirmeoir v0.1.0 — First Playable Release`**.
5. Attach **`Feirmeoir-v0.1.0-Offline.zip`** to that release. Optionally attach the single **`Feirmeoir.html`** file if you prefer a direct download too.
6. Copy the description below into the release, and publish. If the author chooses broader source reuse rights later, update `LICENSE.md` separately.

## Suggested release description

### Feirmeoir v0.1.0 — First Playable Release

**A family. A farm. A future.** Ireland, 1844. Grow a farmstead, manage food and fuel, and guide your family through twelve uncertain harvests in this digital adaptation of Michael Robinson's board game.

**Play immediately:** Download `Feirmeoir-v0.1.0-Offline.zip`, unzip it, and open `Feirmeoir.html` in a modern desktop browser. No installer, server, downloads, or account required after extracting the ZIP.

- Solo high scores and 2–4 player local pass-and-play.
- Farming, livestock, cards, worker placement, food, fuel, taxes, and final scoring.
- All supplied card art and the original rules PDF are included inside the offline HTML.
- Automatic local browser saving where supported.
- An online static-web edition is available through GitHub Pages when enabled by the repository owner.

**Note:** There is no online multiplayer or AI opponent. The game includes documented digital rulings for ambiguities in the original printed rules. Save persistence for locally opened HTML files depends on your browser.

Game, supplied artwork, and original rules © Michael Robinson. All rights reserved.
