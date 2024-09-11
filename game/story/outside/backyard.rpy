label backyard:

    if night:
        scene bg backyard night with dissolve
    else:
        scene bg backyard day with dissolve

    menu:
        "What do you want to do?"

        "Explore the backyard":
            player "The flowers look pretty."

            jump backyard

        "Go elsewhere":
            jump explore_outside_day
