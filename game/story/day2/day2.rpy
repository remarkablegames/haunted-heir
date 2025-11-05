label day2:

    $ night = True

    scene bg hallway night with fade

    show lord disgust at center, tint("#666")
    with dissolve

    play music dusty_piano_keys1

    lord "Are you okay,{w=0.2} [player_name]?"
    lord "You look spooked."

    player "This place is haunted..."
    player "I was nearly attacked!"

    lord @ sigh "Some never left this place...{w=1} and they’re very angry."

    menu:
        "Who are “they”?":
            lord "Well...{w=1} I’d rather not say."
            lord @ sigh "It’s best if you don’t ask."

        "Have you seen them before?":
            lord @ sigh "Indeed...{w=1} I have."
            lord "Stay close to me!{w=1} I know how to navigate this place."

    player "Okay..."

    lord "Have a good night,{w=0.2} [player_name]."

    stop music fadeout 4

    jump bedroom
