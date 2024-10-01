label day1_meet_lord:

    $ event_meet_lord1 = True

    play music the_old_castle

    scene bg interior entrance day with dissolve

    show screen lord_book 

    show lord smirk with dissolve

    voice "voice/lord/lord01.ogg"
    lord "Ah, you must be the new heir."

    voice "voice/lord/lord02.ogg"
    lord "Please come in."

    menu:
        "Who are you?":
            voice "voice/lord/lord03.ogg"
            lord "I’m the Lord of this mansion."

        "Take a seat.":
            pass

    player "Are you the one who sent the letter?"

    voice "voice/lord/lord04.ogg"
    lord @ sigh "Indeed."

    voice "voice/lord/lord05.ogg"
    lord neutral "This mansion has been waiting for someone like you."

    voice "voice/lord/lord06.ogg"
    lord "It’s been in our family for generations{w=0.5} and passed down through time."

    voice "voice/lord/lord07.ogg"
    lord happy "And now,{w=0.3} it’s yours to claim."

    menu:
        "Why me?":
            voice "voice/lord/lord08.ogg"
            lord sigh "There’s something special about you,{w=0.3} [player_name]."

        "How much is this mansion worth?":
            voice "voice/lord/lord09.ogg"
            lord sigh "Although it’s a mansion with a long history,{w=0.3} I can assure you that it’s worth its weight in gold."

    voice "voice/lord/lord10.ogg"
    lord happy "This mansion has treasure for you to find."

    menu:
        "What’s next?":
            voice "voice/lord/lord11.ogg"
            lord neutral "Preparations are underway to transfer the deed to you."

        "When can I expect the deed?":
            pass

    voice "voice/lord/lord12.ogg"
    lord neutral "I’ll need a few days before I can finalize the paperwork."

    voice "voice/lord/lord13.ogg"
    lord @ sigh "By the way,{w=0.3} could you pass me the book to your left?"

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

    voice "voice/lord/lord14.ogg"
    lord smirk "Much appreciated."

    voice "voice/lord/lord15.ogg"
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
