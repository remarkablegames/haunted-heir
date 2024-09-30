label basement:

    if locked_basement:
        scene bg door closed with dissolve

        if item.show("scroll"):
            show screen scroll_closed with dissolve

        play sound locked

        player "The door is locked."

    else:
        scene bg door open with dissolve

        if item.show("scroll"):
            show screen scroll_closed with dissolve

    jump basement_door
