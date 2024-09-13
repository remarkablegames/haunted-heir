label day2_lord_intro:

    $ day2_meet_lord = True

    play music the_old_castle

    scene bg hallway day with dissolve

    show lord with dissolve

    lord "Good morning, [player_name]."
    lord "Did you have a good night’s rest?"

    menu:
        "It was okay...":
            lord "That’s good to hear."

        "This place creeps me out.":
            lord "It’s a new environment,{w=0.3} you’ll get used to it."

    lord "Is there anything you’d like to know?"

    menu:
        "Is there really treasure in this mansion?":
            lord "It’s been said...{w=0.3} but I don’t know for sure."

        "What’s in the basement?":
            lord "There’s nothing important in the basement."
            lord "I suggest you stay away from it."

    lord "Anyway,{w=0.3} I have some work to finish."
    lord "Feel free to grab a bite to eat in the kitchen."

    scene black with dissolve

    stop music fadeout 4

    jump explore_inside_day
