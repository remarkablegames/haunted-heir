label explore_inside_day:

    if night:
        scene bg interior entrance night with dissolve

        if not event_night1:
            player "Why are the lights off?"
            player "Are they trying to save electricity?"
            $ event_night1 = True

    else:
        if handed_treasure == "ghost":
            jump day3_good_ending

        if handed_treasure == "lord":
            jump day3_bad_ending

        if not event_meet_lord1:
            jump day1_meet_lord

        if not event_meet_lord2:
            jump day2_lord_intro

        scene bg interior entrance day with dissolve

    menu:
        "Where do you want to go?"

        "Bedroom":
            stop bleep
            jump bedroom

        "Hallway":
            stop bleep
            jump hallway

        "Kitchen":
            stop bleep
            jump kitchen

        "Room":
            stop bleep
            jump room

        "Basement":
            stop bleep
            jump basement

        "Outside":
            stop bleep
            jump explore_outside_day
