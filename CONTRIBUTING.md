# Contributing to Feirmeoir

Thanks for helping improve the digital adaptation. Bug reports, documentation corrections, accessibility feedback, and suggestions are welcome through GitHub Issues.

## Before proposing a change

- Consult the game’s in-app **How to play**, including the section on digital rulings.
- Keep the original card images and rules intact; do not submit third-party artwork without explicit reuse rights.
- Describe proposed changes to board-game behavior in the issue before implementing them, since some choices resolve ambiguities in the physical rules.
- Be aware this project is **not** currently published under an open-source reuse license. Contact the rights holder for permission before contributing code intended for redistribution.

## Test locally

```bash
node tests/rules.test.cjs
python tools/verify_assets.py
python tools/build_offline.py --zip
```

When filing bugs, provide reproduction steps, a screenshot if useful, browser and OS, player count, and which distribution you used (hosted or single-file offline). Avoid sharing personal data from browser storage.
