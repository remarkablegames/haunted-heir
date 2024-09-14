label bedroom:

    if night:
        scene bg bedroom night with dissolve
    else:
        scene bg bedroom day with dissolve

    menu:
        "What do you want to do?"

        "Rest":
            player "Time to get some rest."

            scene black with fade
            pause 1

            if night:
                $ night = False
            else:
                $ night = True

            jump bedroom

        "Look around":
            player "The bed looks comfy."
            jump bedroom

        "Leave the bedroom":
            jump explore_inside_day
