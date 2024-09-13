label bedroom:

    if night:
        scene bg bedroom night with dissolve
    else:
        scene bg bedroom day with dissolve

    menu:
        "What do you want to do?"

        "Sleep" if sleep:
            $ day += 1
            $ night = False
            $ sleep = False
            player "It’s been a long day."
            scene black with fade
            jump bedroom

        "Look around":
            player "The bed looks comfy."
            jump bedroom

        "Leave the bedroom":
            jump explore_inside_day
