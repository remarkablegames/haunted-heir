label start:

    jump night2_pond_ghost
    show screen inventory

    play music hide_and_seek1
    queue music [hide_and_seek2, hide_and_seek3]

    "You receive a letter in the mailbox."

    "To the child of Jasmine..."
    "The House of [surname] has fallen."
    "And now it shall be bequeathed to you."
    "Go to 11 Hollow Street, Glasgow and claim your inheritance."
    "Sincerely,\nLeon [surname]"

    menu:
        "Do you accept this offer?"

        "Yes":
            jump accept_letter_offer

        "No":
            menu:
                "Do you {b}ACCEPT{/b} this offer?"

                "Yes":
                    jump accept_letter_offer

                "{sc}No":
                    jump end

label accept_letter_offer:

    "Please sign your name below..."

    $ player_name = renpy.input("My name is...", length=32).strip() or player_name

    stop music fadeout 4

    scene bg mansion front day with fade

    player "Looks like I’ve arrived at my destination."
    player "What a large mansion."

    menu:
        "Where do you want to go?"

        "Go inside":
            jump explore_inside_day

        "Explore outside":
            jump explore_outside_day
