# Tarot Arcana Visual Novel Skeleton

This repository provides a minimal Ren'Py project structure for a visual novel based on the Major Arcana of Tarot. It separates scripts and assets, follows snake_case naming, and includes a placeholder CI workflow.

## Project Structure
```
VNresearch/
├── game/
│   ├── script.rpy              # Main entry point
│   ├── options.rpy             # Basic configuration
│   ├── gui.rpy                 # GUI colors and fonts
│   ├── script/                 # Story scripts
│   │   └── ma00_fool/          # Example arcana folder
│   │       └── ma00_fool_demo.rpy
│   ├── images/
│   │   ├── bg/                 # Background images
│   │   └── characters/         # Character sprites
│   ├── gui/                    # Interface assets and fonts
│   └── audio/                  # Music and sound effects
├── docs/                       # Bibles, roadmap, marketing plans
├── .github/workflows/ci.yml    # Placeholder CI workflow
└── README.md
```

## Adding Content
- **Scripts:** create a new folder in `game/script/` named after the card (e.g., `ma01_magician/`) and add `.rpy` files inside it. Use snake_case names like `ma01_magician_scene.rpy`.
- **Images:** put background images in `game/images/bg/` and character sprites in `game/images/characters/`. The project uses solid-color placeholders in `script.rpy`; replace them with actual art files.
- **Audio:** place music and sound effects in `game/audio/`.
- **Documentation:** store narrative, art, tech, and marketing references in the corresponding subfolders under `docs/`.

## Building for Steam
1. Install the [Ren'Py SDK](https://www.renpy.org/).
2. Place this repository inside the `projects/` directory of the SDK.
3. Open the project in the Ren'Py launcher and use **Build Distributions** to create a Steam package.
4. Upload the generated build to Steam using the Steamworks tools. Refer to Ren'Py's [Steam deployment guide](https://www.renpy.org/doc/html/steam.html) for details.

## CI Placeholder
The repository includes a minimal GitHub Actions workflow file (`.github/workflows/ci.yml`) that can be expanded to lint scripts, run tests, or build releases.
