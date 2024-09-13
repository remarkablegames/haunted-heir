label hallway:

    if night:
        scene bg hallway night with dissolve
    else:
        scene bg hallway day with dissolve

    menu:
        "What do you want to do?"

        "Look around":
            player "The skies are clear today."
            jump hallway

        "Go elsewhere":
            jump explore_inside_day
