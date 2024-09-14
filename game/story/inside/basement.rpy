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

label basement_room(with_dissolve=True):

    if basement_visit == 1:
        jump basement_room_first_visit

    if with_dissolve:
        scene bg basement light with dissolve
    else:
        scene bg basement light

    if night:
        if with_dissolve:
            show ghost girl talk at center, opacity(0.5)
            with dissolve
        else:
            show ghost girl talk at center, opacity(0.5)
    else:
        if basement_visit > 2:
            show screen basement_book

    menu:
        "What do you want to do?"

        "Talk to the Ghost" if night:
            jump basement_ghost

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
            player "It’s best not to snoop through other people’s things."

    call screen explore_basement

label basement_ghost:

    menu:
        ghost girl "{sc}What do you have for me?"

        "Hand the treasure over" if item.is_inventory("necklace"):
            player "Is this the treasure?"
            $ item.use("necklace")
            ghost girl "{sc}Yes,{w=0.3} this is what I’ve been looking for."
            ghost girl "{sc}I can finally rest in peace."
            ghost girl "{sc}Thank you..."
            call basement_room(False)

        "Nevermind":
            call basement_room(False)
