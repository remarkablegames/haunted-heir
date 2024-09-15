label backyard:

    if night:
        play music night_ambience fadein 1
        scene bg backyard night with dissolve
    else:
        scene bg backyard day with dissolve

    menu:
        "What do you want to do?"

        "Look around":
            $ dialogue = "It’s too dark to see anything." if night else "What lovely flowers."
            player "[dialogue]"

            jump backyard

        "Go elsewhere":
            stop music fadeout 1

            jump explore_outside_day
