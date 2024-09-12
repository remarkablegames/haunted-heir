label backyard:

    if night:
        play music night_ambience fadein 1
        scene bg backyard night with dissolve
    else:
        scene bg backyard day with dissolve

    menu:
        "What do you want to do?"

        "Explore the backyard":
            player "The flowers look pretty."

            jump backyard

        "Go elsewhere":
            stop music fadeout 1
            jump explore_outside_day
