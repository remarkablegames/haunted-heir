label backyard:

    if night:
        play music night_ambience fadein 1
        scene bg backyard night with dissolve
    else:
        scene bg backyard day with dissolve

    menu:
        "What do you want to do?"

        "Look around":
            player "What pretty flowers."
            jump backyard

        "Go elsewhere":
            stop music fadeout 1
            jump explore_outside_day
