label day2_lord_intro:

    $ day2_meet_lord = True

    play music the_old_castle

    scene bg hallway day with dissolve

    show lord smirk with dissolve

    lord "Good morning, [player_name]."
    lord "Did you have a good night’s rest?"

    menu:
        "It was okay...":
            show lord laugh2
            lord "That’s good to hear."

        "This place creeps me out.":
            show lord laugh2
            lord "It’s a new environment,{w=0.3} you’ll get used to it."

    show lord smirk
    
    lord "Is there anything you’d like to know?"

    menu:
        "Is there really treasure in this mansion?":
            show lord neutral
            lord "It’s been said...{w=0.3} but I don’t know for sure."

        "What’s in the basement?":
            show lord disgust
            lord "There’s nothing important in the basement."
            show lord sigh
            lord "I suggest you stay away from it."

    show lord smirk 

    lord "Anyway,{w=0.3} I have some work to finish."
    lord "Feel free to grab a bite to eat in the kitchen."

    scene black with dissolve

    stop music fadeout 4

    jump explore_inside_day
