label room:

    if night:
        scene bg room night with dissolve
    else:
        scene bg room day with dissolve

    show screen safe

    menu:
        "What do you want to do?"

        "Look around":
            call screen explore_room
            jump room

        "Go elsewhere":
            hide screen safe
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
            at scale(0.1)

    else:
        imagebutton:
            xpos 1170
            ypos 520
            idle "items/safe_open.png"
            at scale(0.1)

        if item.show("necklace"):
            use necklace

label safe:
    if renpy.input("Enter safe passcode:", length=4) == "1111":
        $ safe_locked = False
        play sound unlocked
        player "The safe opened."
    else:
        play sound locked
        player "Incorrect passcode."

    call screen explore_room

screen necklace():
    imagebutton:
        xpos 1227
        ypos 541
        idle "items/necklace.png"
        action Jump("necklace_found")
        at scale(0.08)

label necklace_found:
    $ item.find("necklace")
    hide screen necklace
    player "What a dazzling necklace."
    player "I wonder who it belongs to."
    call screen explore_room
