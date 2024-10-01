label basement_door:

    if locked_basement:
        scene bg door closed

        menu:
            "What do you want to do?"

            "Unlock the door" if item.is_inventory("key"):
                play sound unlocked

                $ locked_basement = False
                $ item.use("key")

                player "The door is unlocked."

                play sound creak

                hide screen scroll_closed

                jump basement

            "Go upstairs":
                hide screen scroll_closed

                jump explore_inside_day

            "Look around":
                call screen explore_basement_door

    else:
        scene bg door open

        menu:
            "What do you want to do?"

            "Go downstairs":
                $ visits_basement += 1
                jump basement_room

            "Go upstairs":
                jump explore_inside_day

screen scroll_closed():
    imagebutton:
        xpos 1300
        ypos 800
        idle "items/rolledscroll.webp"
        action Jump("scroll_found")
        at rotate(90), scale(0.11)

screen scroll_opened():
    imagebutton:
        xpos 600
        ypos 100
        idle "items/bewarescroll.webp"
        action Hide("scroll_opened")
        at scale(0.8)

label scroll_found:
    play sound paper

    hide screen scroll_closed
    show screen scroll_opened

    player "Umm...{w=0.3} what comes at night?"

    $ item.find("scroll")

    hide screen scroll_opened

    jump basement_door

screen explore_basement_door():
    use back("basement_door")
