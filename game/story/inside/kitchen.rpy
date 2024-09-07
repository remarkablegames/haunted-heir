label kitchen:

    scene bg kitchen day with dissolve

    if not basement_key:
        show screen basement_key

    menu:
        "What do you want to do?"

        "Explore the kitchen":
            call screen explore_kitchen

            jump kitchen

        "Go somewhere else":
            hide screen basement_key

            jump explore_inside_day

screen explore_kitchen():
    textbutton "Back" action Jump("kitchen")

    textbutton "{alpha=0}BREAD\nBREAD":
        xpos 790
        ypos 410
        action Call("kitchen_bread")

label kitchen_bread:

    player "The bread looks stale."

    call screen explore_kitchen

screen basement_key():
    imagebutton:
        xpos 1400
        ypos 440
        idle "items/key.png"
        hover "items/key.png"
        action Jump("basement_key_found")
        at scale(0.2)

label basement_key_found:

    $ basement_key = True

    hide screen basement_key

    player "I found a key."

    jump kitchen
