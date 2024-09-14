label day2:

    $ night = True

    scene bg hallway night with fade

    show lord worry at center, tint("#333")
    with dissolve

    play music dusty_piano_keys1

    lord "[player_name]!{w=0.3} Are you okay?"
    lord "You look spooked."

    show lord 

    player "This place is haunted."
    player "I was nearly attacked!"

    show lord sigh

    lord "Some never left this place,{w=0.3} and they’re very angry."

    show lord 

    menu:
        "Who are “they”?":
            show lord worry
            lord "Well,{w=0.3} I’d rather not say."
            show lord sigh 
            lord "It’s best if you don’t ask."

        "Have you seen them before?":
            show lord sigh
            lord "Indeed,{w=0.3} I have."
            show lord smirk
            lord "Stay close to me,{w=0.3} I know how to navigate this place."

    player "Okay..."

    show lord smirk 
    
    lord "Have a good night,{w=0.3} [player_name]."

    stop music fadeout 4

    jump bedroom
