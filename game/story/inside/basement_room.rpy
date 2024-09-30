label basement_room(with_dissolve=True):

    if visits_basement == 1:
        jump basement_room_first_visit

    if night:
        if with_dissolve:
            scene bg basement dark with dissolve

            if handed_treasure != "ghost":
                show ghost angry at center, opacity(0.5)
                with dissolve
        else:
            scene bg basement dark

            if handed_treasure != "ghost":
                show ghost angry at center, opacity(0.5)

    else:
        if with_dissolve:
            scene bg basement light with dissolve
        else:
            scene bg basement light

        if visits_basement > 1:
            show screen basement_book

    menu:
        "What do you want to do?"

        "Talk to the Ghost" if night and handed_treasure != "ghost":
            jump basement_ghost

        "Look around":
            call screen explore_basement_room

        "Go upstairs":
            hide screen basement_book
            jump explore_inside_day

    return

screen explore_basement_room():
    use back("basement_room")

screen basement_book():
    imagebutton:
        xpos 980
        ypos 387
        idle "items/book.webp"
        action Jump("basement_book")
        at scale(0.13), tint("#666")

label basement_book:

    player "It’s the Lord’s book."

    menu:
        "Should I take a peek?"

        "Yes":
            player "The last entry is dated November 11th."

            "“I can’t wait to surprise my beloved on her birthday today.{w}\nI’ll treasure this day forever.”"

            player "I wonder what that means..."

        "No":
            player "It’s best not to snoop through other people’s belongings."

    call screen explore_basement_room

label basement_ghost:
    show ghost angry talk at center, opacity(0.5)

    menu:
        ghost "{sc}What do you have for me?"

        "Hand the treasure over" if item.is_inventory("necklace"):
            player "Is this what you’re looking for?"

            $ item.use("necklace")
            $ handed_treasure = "ghost"

            ghost sad smile "{sc}Yes,{w=0.3} this is my precious..."

            hide ghost with dissolve

            show miss blush at center, opacity(0.8), scale(1.5)
            with dissolve

            ghost "... my precious necklace."
            ghost "I can finally rest in peace..."

            show miss smile at center, opacity(0.8), scale(1.5)

            ghost "Thank you..."
            ghost "Farewell, [player_name]."

            hide miss with dissolve

            call basement_room(with_dissolve=False)

        "Nevermind":
            call basement_room(with_dissolve=False)
