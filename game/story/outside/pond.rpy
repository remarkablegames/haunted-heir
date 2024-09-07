label pond:

    scene bg pond day with dissolve

    menu:
        "What do you want to do?"

        "Explore the pond":
            player "It feels pretty tranquil here."

            jump pond

        "Go somewhere else":
            jump explore_outside_day
