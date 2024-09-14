label basement:

    if basement_locked:
        scene bg door closed with dissolve

        play sound locked

        player "The door is locked."

        menu:
            "What do you want to do?"

            "Unlock the door" if item.is_inventory("key"):
                play sound unlocked

                $ basement_locked = False
                $ item.use("key")

                player "The door is unlocked."

                play sound creak

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

    if night:
        if with_dissolve:
            scene bg basement dark with dissolve

            if handed_treasure != "ghost":
                show ghost angry at center, opacity(0.5), delayed_blink(0, 5)
                with dissolve
        else:
            scene bg basement dark

            if handed_treasure != "ghost":
                show ghost angry at center, opacity(0.5), delayed_blink(0, 5)

    else:
        if with_dissolve:
            scene bg basement light with dissolve
        else:
            scene bg basement light

        if basement_visit > 1:
            show screen basement_book

    menu:
        "What do you want to do?"

        "Talk to the Ghost" if night and handed_treasure != "ghost":
            jump basement_ghost

        "Look around":
            call screen explore_basement

        "Go upstairs":
            hide screen basement_book
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
            player "It’s best not to snoop through other people’s belongings."

    jump basement_room

label basement_ghost:
    show ghost angry talk
    menu:
        ghost "{sc}What do you have for me?"

        "Hand the treasure over" if item.is_inventory("necklace"):
            player "Is this what you’re looking for?"

            $ item.use("necklace")
            $ handed_treasure = "ghost"

            show ghost sad smile

            ghost "{sc}Yes,{w=0.3} this is my precious..."

            hide ghost with dissolve

            show miss blush at center, opacity(0.8), delayed_blink(0, 5) with dissolve

            ghost "...precious necklace."

            ghost "I can finally rest in peace...{w=0.3} and see my daughter again."

            show miss smile at center, opacity(0.8), delayed_blink(0, 5)

            ghost "Thank you... so much."

            ghost "Farewell, [player_name]."

            hide miss with dissolve

            call basement_room(False)

        "Nevermind":
            call basement_room(False)
