label hallway:

    scene bg hallway day2 with dissolve

    menu:
        "What do you want to do?"

        "Explore the hallway.":
            player "The skies are clear today."

            jump hallway

        "Go somewhere else.":
            jump explore_inside_day
