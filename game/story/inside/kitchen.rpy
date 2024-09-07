label kitchen:

    scene bg kitchen day with dissolve

    menu:
        "What do you want to do?"

        "Explore the kitchen.":
            player "The bread is looking kind of stale."

            jump kitchen

        "Go somewhere else.":
            jump explore_inside_day
