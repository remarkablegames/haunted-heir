label explore_outside_day:

    if night:
        play music night_ambience fadein 1
        scene bg mansion front night with dissolve
    else:
        scene bg mansion front day with dissolve

    menu:
        "Where do you want to go?"

        "Backyard":
            stop music fadeout 1
            jump backyard

        "Pond":
            stop music fadeout 1
            jump pond

        "Inside":
            stop music fadeout 1
            jump explore_inside_day
