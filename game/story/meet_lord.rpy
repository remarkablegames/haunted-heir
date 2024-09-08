label meet_lord:

    $ meet_lord = True

    scene bg interior entrance day with dissolve

    show lord smile at center
    with dissolve

    lord "Ah, you must be the new heir."
    lord "Please come in and have a seat."

    menu:
        "Who are you?":
            lord "I’m the lord of this mansion."

        "Take a seat.":
            pass

    player "Are you the one who sent for me?"

    lord "Indeed."
    lord "This mansion...{w=0.3} has been waiting for someone like you." 

    lord "It’s been in our family for generations, passed down through time. And now, it’s yours to claim."

    menu:
        "Why me?":
            lord "There’s something special about you, [player_name]."

    lord "You were meant to find it, and now it belongs to you."

    menu:
        "What does that mean?":
            lord "It means this mansion has history."

            player "I see..."

        "When can I expect the deed?":
            pass

    lord "I’ll need a few days before I can finish the paperwork."
    lord "Please rest in the guest bedroom in the meantime."

    player "Alright."

    jump explore_inside_day
