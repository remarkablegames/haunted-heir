label start:

    "You receive a letter in the mailbox."

    scene bg bedroom day with fade

    "To the child of yadda yadda..."
    "The home of the <Surname> has been <insert dramatic monologue here>."

    "And now it shall be inherited to you."

    "Go to the mansion in <random street/country>, claim the inheritance yadda yadda, and bring our lives to justice."

    "Sincerely,\nLeon <Surname>"

    "There is a return envelope."

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

                        "{sc}Stop it{/sc}":
                            scene black with fade

                            "{b}End{/b}."

                            return

label accept_letter_offer:

    "Insert name as signature..."

    $ player_name = renpy.input("My name is...", length=32).strip() or player_name

    "Welcome, [player_name]."

    jump end
