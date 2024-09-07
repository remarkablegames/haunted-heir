label bedroom:

    scene bg bedroom day with dissolve

    menu:
        "What do you want to do?"

        "Take a nap.":
            jump end

        "Explore the bedroom.":
            player "The bed looks pretty comfy."

            jump bedroom

        "Go somewhere else.":
            jump explore_inside_day
