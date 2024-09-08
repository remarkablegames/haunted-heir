﻿label start:

    show screen inventory

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
                "Do you accept this offer?"

                "Yes":
                    jump accept_letter_offer

                "N̴o̸":
                    menu:
                        "Do you {b}ACCEPT{/b} this offer?"

                        "Yes":
                            jump accept_letter_offer

                        "{sc}No{/sc}":
                            jump restaurant

label accept_letter_offer:

    "Please sign your name on the dotted line..."

    $ player_name = renpy.input("My name is...", length=32).strip() or player_name

    scene bg mansion front day with fade

    player "Looks like I’ve arrived at my destination."

    menu:
        "Where do you want to go?"

        "Go inside":
            jump explore_inside_day

        "Explore outside":
            jump explore_outside_day
