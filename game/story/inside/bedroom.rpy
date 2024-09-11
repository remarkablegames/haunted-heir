label bedroom:

    if night:
        scene bg bedroom night with dissolve
    else:
        scene bg bedroom day with dissolve

    menu:
        "What do you want to do?"

        "Explore the bedroom":
            player "The bed looks pretty comfy."

            jump bedroom

        "Leave the bedroom":
            jump explore_inside_day
