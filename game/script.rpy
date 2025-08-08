# script.rpy
# Main entry point for the visual novel. Defines core characters and placeholder assets.
# Replace Solid-based placeholders with actual image files in game/images/.

# Character definitions
define narrator = Character(None)
define f = Character("Шут", color="#c3e9f9")

# Placeholder image definitions using solid colors
image bg placeholder = Solid("#4a4a4a", xysize=(1920, 1080))
image placeholder char = Solid("#808080", xysize=(512, 1024))

# Start label
label start:
    scene bg placeholder
    show placeholder char at center
    narrator "Это базовый проект. Замените этот текст и изображения на свой сценарий и ассеты."
    jump ma00_fool_demo

