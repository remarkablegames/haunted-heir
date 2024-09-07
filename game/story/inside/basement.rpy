label basement:

    if not basement:
        jump basement_locked

    scene bg basement light with dissolve

    menu:
        "What do you want to do?"

        "Explore the basement":
            player "The basement is spooky."

            jump basement

        "Go upstairs":
            jump explore_inside_day

label basement_locked:

    scene bg door closed with dissolve

    player "The basement is locked."

    menu:
        "What do you want to do?"

        "Go upstairs":
            jump explore_inside_day
