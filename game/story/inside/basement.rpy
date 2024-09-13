label basement:

    if basement_locked:
        scene bg door closed with dissolve

        play sound locked

        player "The door is locked."

        menu:
            "What do you want to do?"

            "Unlock the door with the key" if item.is_inventory("key"):
                play sound unlocked
                $ basement_locked = False
                $ item.use("key")
                player "The door is unlocked."
                jump basement

            "Go upstairs":
                jump explore_inside_day

    else:
        scene bg door open with dissolve

        menu:
            "What do you want to do?"

            "Go downstairs":
                $ basement_visit += 1
                jump basement_room

            "Go upstairs":
                jump explore_inside_day

label basement_room:

    if basement_visit == 1:
        jump basement_room_first_visit

    scene bg basement light with dissolve

    if basement_visit > 2:
        show screen basement_book

    menu:
        "What do you want to do?"

        "Look around":
            call screen explore_basement

        "Go upstairs":
            jump explore_inside_day

screen explore_basement():
    use back("basement_room")

screen basement_book():
    imagebutton:
        xpos 980
        ypos 387
        idle "items/book.png"
        action Jump("basement_book")
        at scale(0.13), tint("#666")

label basement_book:

    player "It’s the Lord’s book."

    menu:
        "Should I take a peek?"

        "Yes":
            player "The last entry is dated November 11th."

            "“I can’t wait to surprise my beloved on her birthday today.{w}\nI’ll treasure this day forever.”"

        "No":
            player "I shouldn’t snoop around other people’s stuff."

    call screen explore_basement
