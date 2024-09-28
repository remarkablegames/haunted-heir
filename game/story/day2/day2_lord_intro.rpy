label day2_lord_intro:

    $ event_meet_lord2 = True

    play music the_old_castle

    scene bg hallway day with dissolve

    show lord smirk with dissolve

    lord "Good morning, [player_name]."
    lord "Did you have a good night’s rest?"

    menu:
        "It was okay...":
            lord @ smile "That’s good to hear."

        "This place creeps me out.":
            lord @ sigh "It’s a new environment,{w=0.3} you’ll get used to it."

    lord "Is there anything you’d like to know?"

    menu:
        "Is there really treasure in this mansion?":
            lord @ neutral "It’s been said...{w=0.3} but I don’t know for sure."

        "What’s in the basement?":
            lord @ angry "There’s nothing in the basement."
            lord @ sigh "I suggest you stay away from it."

    lord neutral "Anyway,{w=0.3} I have work to do."
    lord "Feel free to grab something to eat in the kitchen."

    scene black with dissolve

    stop music fadeout 4

    jump explore_inside_day
