# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define g = Character("GUN")
define n = Character("Nora")
image bg barn = "Art/Backgrounds/Bg_Barn.png"
image gun neutral = "Art/Characters/EvilGun_neutral.png"
image nora neutral ="Art/Characters/Nora_neutral.png"



label start:

    scene bg barn

    show gun neutral at left

    show nora neutral at right

    g "Hello, we are testing"

    n "And I am super sexxyyyy"

    return
