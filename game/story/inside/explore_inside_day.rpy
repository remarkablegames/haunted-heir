label explore_inside_day:

    if not day1_meet_lord:
        jump day1_meet_lord

    elif not night and not day2_meet_lord:
        jump day2_lord_intro

    if night:
        scene bg interior entrance night with dissolve
    else:
        scene bg interior entrance day with dissolve

    if not day1_night:
        player "Why are the lights off?"
        player "Are they trying to save electricity?"
        $ day1_night = True

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
