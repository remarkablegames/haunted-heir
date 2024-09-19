label day1_meet_lord:

    $ day1_meet_lord = True

    play music the_old_castle

    scene bg interior entrance day with dissolve

    show screen lord_book 

    show lord smirk with dissolve

    lord "Ah, you must be the new heir."
    lord "Please come in."

    menu:
        "Who are you?":
            lord "I’m the Lord of this mansion."

        "Take a seat.":
            pass

    player "Are you the one who sent the letter?"

    lord @ sigh "Indeed."
    lord "This mansion has been waiting for someone like you."
    lord "It’s been in our family for generations{w=0.3} and passed down through time."
    lord happy "And now,{w=0.3} it’s yours to claim."

    menu:
        "Why me?":
            lord @ sigh "There’s something special about you,{w=0.3} [player_name]."

        "How much is this mansion worth?":
            lord @ sigh "Although it’s a mansion with a long history,{w=0.3} I can assure you that it’s worth its weight in gold."

    lord "This mansion has treasure for you to find."

    menu:
        "What’s next?":
            lord neutral "Preparations are underway to transfer the deed to you."

        "When can I expect the deed?":
            pass

    lord neutral "I’ll need a few days before I can finalize the paperwork."
    lord "By the way,{w=0.3} could you pass me the book to your left?"

    call screen lord_book(blink=True)

screen lord_book(blink=False):
    imagebutton:
        xpos 100
        ypos 515
        idle "items/book.webp"
        action Jump("lord_book_found")
        at scale(0.17)
        if blink:
            at delayed_blink(0, 1)

label lord_book_found:

    $ item.find("book")
    hide screen lord_book

    player "Here you go."

    $ item.use("book")

    lord smirk "Much appreciated."
    lord "Please rest in our guest bedroom while you wait."

    player "Thanks."

    stop music fadeout 4

    scene bg bedroom day with fade

    player "Well,{w=0.2} here’s to becoming rich."
    player "It’s been a long journey,{w=0.2} so let me take a quick nap."
    player "At least the pillows are fluffy."

    menu:
        "Nap":
            pass

    $ night = True

    scene bg bedroom evening with dissolve
    pause 0.5

    scene black with fade
    pause 0.5

    scene bg bedroom night with dissolve

    player "{i}Yawn.{/i}{w=0.3} What a good nap."
    player "I’m feeling kind of hungry."
    player "Let me go downstairs to grab a bite to eat."

    jump bedroom
