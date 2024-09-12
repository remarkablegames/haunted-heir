label day_2:

    $ night = True
    scene bg hallway night with dissolve

    show lord worry at center
    with dissolve

    lord "[player_name]!{w=0.3} Are you okay?{w=0.3} You look spooked."

    player "This place is haunted.{w=0.3} I was nearly attacked!"

    lord "Some never left this place,{w=0.3} [player_name].{w=0.3} They're very angry."

    menu:
        "Who's 'they'?":
            lord "Well,{w=0.3} I'd rather not say.{w=0.3} It's best if you don't ask."

        "Have you seen them before?":
            lord "Indeed,{w=0.3} I have.{w=0.3} Stay close to me,{w=0.3} [player_name],{w=0.3} I know how to navigate this place."

    player "Well, okay then."

    lord "Have a good night,{w=0.3} [player_name]."

    jump bedroom
