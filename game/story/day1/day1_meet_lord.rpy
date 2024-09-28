label day1_meet_lord:

    $ events["meet_lord1"] = True

    play music the_old_castle

    scene bg interior entrance day with dissolve

    show screen lord_book 

    show lord smirk with dissolve

    lord "Welcome to the [surname] manor." 
    player "Are you the one who sent the letter?" 
    lord "Indeed I am."
    player "So this is mine now? Where’s the deed?"
    lord "Straight to the point I see. Yes, the house and the land will be yours. I can have the necessary paperwork complete in a few days."
    player "What’s the catch?"
    lord "How shrewd. There is a condition you will need to fulfill. We will discuss it in detail tomorrow."
    lord "For now, I can lead you to your room, and you can settle in for the evening. If you need anything, let me know."
    jump first_questions


label first_questions: 
    menu:
        "What’s the wifi?":
            lord "The what?" 
            player "The wifi. What’s the password? I want to connect to the internet."
            lord "I’m not sure I’m familiar. Is this net you refer to a type of physical object, or some manner of metaphysical framework?" 
            player "…What?"
            player  "So, does that mean you don’t have internet? How old even are you?" 
            lord "I once found novel and innovative many of the amenities that you find mundane, so I’d wager I’m rather ancient by comparison." 
            player "How old is ancient? Did you you have dinosaurs as pets?"
            lord "Something like that"
            player "How big were they?"
            lord "Let's just say that you would make an unsatisfactory meal."             
        "Is this place haunted?":
            lord "Every house is haunted."
            player "What do you mean? Like, metaphorically?"
            lord "If there’s nothing else, I will take my leave."
        "How much is this place worth?":
            lord "Quite the acquisitive individual, I see. Find a buyer and you need not work another day in this life."
            jump first_questions

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
