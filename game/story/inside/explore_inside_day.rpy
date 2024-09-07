label explore_inside_day:

    if not meet_lord:
        jump meet_lord

    scene bg interior entrance day with dissolve

    menu:
        "Where do you want to go?"

        "Bedroom":
            jump bedroom

        "Kitchen":
            jump kitchen

        "Outside":
            jump explore_outside_day
