label room:

    scene bg room day with dissolve

    menu:
        "What do you want to do?"

        "Explore the room":
            player "Nothing to see here."

            jump room

        "Go elsewhere":
            jump explore_inside_day
