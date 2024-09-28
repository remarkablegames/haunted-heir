label explore_inside_day:

    if night:
        scene bg interior entrance night with dissolve

        if not event_night1:
            player "Why are the lights off?"
            player "Are they trying to save electricity?"
            $ event_night1 = True

    else:
        if not event_meet_lord1:
            jump day1_meet_lord

        elif not event_meet_lord2:
            jump day2_lord_intro

        elif handed_treasure == "ghost":
            jump day3_good_ending

        elif handed_treasure == "lord":
            jump day3_bad_ending

        scene bg interior entrance day with dissolve

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
