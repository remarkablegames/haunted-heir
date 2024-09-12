label day_2_lord_intro:

    $ meet_lord_day_2 = True

    scene bg hallway day with dissolve

    show lord with dissolve

    lord "Good morning, [player_name].{w=0.3} Did you have a good night's rest?"

    menu:
        "It was okay...":
            lord "Good to hear."

        "This place creeps me out.":
            lord "It's a new environment,{w=0.3} you'll grow to like it here."

    menu:
        "Is there treasure in this mansion?":
            lord "It's been said,{w=0.3} [player_name]...{w=0.3} but I don't know for sure."

        "What's in the basement?":
            lord "There's nothing important in the basement,{w=0.3} [player_name]."
            lord "I recommend you stay away from it."

    lord "I have work to get done.{w=0.3} Feel free to grab a bite to eat in the kitchen."
  
    jump explore_inside_day
