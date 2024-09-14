label bedroom:

    if night:
        scene bg bedroom night with dissolve
    else:
        scene bg bedroom day with dissolve

    menu:
        "What do you want to do?"

        "Rest":
            $ dialogue = renpy.random.choice(["Time to get some rest.", "I’m feeling pretty tired.", "Can’t wait to fall asleep.", "Time to count sheep."])
            player "[dialogue]"

            scene black with fade
            pause 0.5

            $ night = not night

            jump bedroom

        "Look around":
            player "The bed looks comfy."
            jump bedroom

        "Leave the bedroom":
            jump explore_inside_day
