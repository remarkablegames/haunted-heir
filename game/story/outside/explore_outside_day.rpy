label explore_outside_day:

    if night:
        scene bg mansion front night with dissolve
    else:
        scene bg mansion front day with dissolve

    menu:
        "Where do you want to go?"

        "Backyard":
            jump backyard

        "Pond":
            jump pond

        "Inside":
            jump explore_inside_day
