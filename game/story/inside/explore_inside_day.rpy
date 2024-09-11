label explore_inside_day:

    if not meet_lord:
        jump meet_lord

    if night:
        scene bg interior entrance night with dissolve
    else:
        scene bg interior entrance day with dissolve

    if day == 1 and night:
        player "Why are the lights off?"
        player "Are they trying to save electricity?"

    menu:
        "Where do you want to go?"

        "Bedroom":
            jump bedroom

        "Hallway":
            jump hallway

        "Kitchen":
            jump kitchen

        "Room":
            jump room

        "Basement":
            jump basement

        "Outside":
            jump explore_outside_day
