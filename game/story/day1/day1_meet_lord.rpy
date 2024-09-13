label day1_meet_lord:

    $ day1_meet_lord = True

    play music the_old_castle

    scene bg interior entrance day with dissolve

    show screen lord_book 

    show lord smile
    with dissolve

    lord "Ah, you must be the new heir."
    lord "Please come in."

    menu:
        "Who are you?":
            lord "I’m the Lord of this mansion."

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
    lord "Please rest in our guest bedroom while you wait."

    player "Thanks."

    stop music fadeout 4

    scene bg bedroom day with fade

    player "Well,{w=0.2} here’s to becoming rich."
    player "I’m feeling pretty tired,{w=0.2} so I should get some rest."
    player "At least the pillows are soft."

    menu:
        "Nap":
            pass

    $ night = True

    scene bg bedroom evening with dissolve

    pause 1

    scene bg bedroom night with fade

    player "{i}Yawn.{/i}{w=0.3} What a good nap."
    player "I’m feeling kind of hungry."
    player "Let me go downstairs to grab a bite to eat."

    jump bedroom
