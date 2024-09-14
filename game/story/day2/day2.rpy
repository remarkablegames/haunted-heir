label day2:

    $ night = True

    scene bg hallway night with fade

    show lord worry with dissolve

    play music dusty_piano_keys1

    lord "[player_name]!{w=0.3} Are you okay?"
    lord "You look spooked."

    player "This place is haunted."
    player "I was nearly attacked!"

    lord "Some never left this place,{w=0.3} and they’re very angry."

    menu:
        "Who are “they”?":
            lord "Well,{w=0.3} I’d rather not say."
            lord "It’s best if you don’t ask."

        "Have you seen them before?":
            lord "Indeed,{w=0.3} I have."
            lord "Stay close to me,{w=0.3} I know how to navigate this place."

    player "Okay..."

    lord "Have a good night,{w=0.3} [player_name]."

    stop music fadeout 4

    jump bedroom
