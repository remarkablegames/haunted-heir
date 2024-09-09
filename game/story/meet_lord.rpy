label meet_lord:

    $ meet_lord = True

    scene bg interior entrance day with dissolve

    show screen lord_book 

    show lord smile at center
    with dissolve

    lord "Ah, you must be the new heir."
    lord "Please come in."

    menu:
        "Who are you?":
            lord "I’m the lord of this mansion."

        "Take a seat.":
            pass

    player "Are you the one who sent the letter?"

    lord "Correct."
    lord "This mansion has been waiting for someone like you."
    lord "It’s been in our family for generations and passed down through time."
    lord "And now, it’s yours to claim."

    menu:
        "Why me?":
            lord "There’s something special about you, [player_name]."

        "How much is this mansion worth?":
            lord "Although it’s a mansion with a long history,{w=0.3} I can assure you that it’s worth its weight in gold."

    lord "This mansion has treasure for you to find."

    menu:
        "What’s next?":
            lord "Preparations are underway to transfer the deed to you."

        "When can I expect the deed?":
            pass

    lord "I’ll need a few more days before I can finalize the paperwork."
    lord "By the way,{w=0.3} do you mind passing me the book to your left?"

    call screen lord_book(blink=True)

screen lord_book(blink=False):
    if blink:
        imagebutton:
            xpos 100
            ypos 515
            idle "items/book.png"
            action Jump("lord_book_found")
            at scale(0.17), delayed_blink(0, 1)

    else:
        imagebutton:
            xpos 100
            ypos 515
            idle "items/book.png"
            action Jump("lord_book_found")
            at scale(0.17)

label lord_book_found:

    $ item.find("book")
    hide screen lord_book

    player "Here you go."

    $ item.use("book")

    lord "Much appreciated."
    lord "While you wait, please rest in our guest bedroom."

    player "Alright."

    lord "See you later."

    jump explore_inside_day
