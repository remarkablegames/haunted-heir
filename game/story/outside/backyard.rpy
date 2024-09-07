label backyard:

    scene bg backyard day1 with dissolve

    menu:
        "What do you want to do?"

        "Explore the backyard":
            player "The flowers look pretty."

            jump backyard

        "Go somewhere else":
            jump explore_outside_day
