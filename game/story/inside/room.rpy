label room:

    if night:
        scene bg room night with dissolve
    else:
        scene bg room day with dissolve

    show screen safe

    menu:
        "What do you want to do?"

        "Explore the room":
            call screen explore_room
            jump room

        "Go elsewhere":
            jump explore_inside_day

screen explore_room():
    use back("room")

screen safe():
    if safe_locked:
        imagebutton:
            xpos 1170
            ypos 520
            idle "items/safe_closed.png"
            action Jump("safe")
            at scale(0.10)

    else:
        imagebutton:
            xpos 1170
            ypos 520
            idle "items/safe_open.png"
            at scale(0.10)

label safe:
    if renpy.input("Enter safe passcode:", length=4) == "1111":
        $ safe_locked = False
        play sound door_unlock
        player "The safe opened."
    else:
        play sound door_open
        player "Incorrect passcode."

    call screen explore_room
