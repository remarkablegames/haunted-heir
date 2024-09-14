label basement_room_first_visit:

    play music a_hollow_call1

    scene bg basement light with dissolve

    player "The air feels chilly here..."

    play sound crash

    pause 0.5

    player "What was that?"

    queue music a_hollow_call2

    scene bg basement dark with dissolve

    player "..."

    play sound crash

    show ghost angry talk at center, opacity(0.5), scale(1.5), ypos(1.4)
    with moveinbottom
    with vpunch

    ghost "{sc}I’ve waited...{w=0.3} so long..."

    show ghost angry

    player "Who...{w=0.3} who are you?"

    show ghost angry talk

    ghost "{sc}Does it matter?{w=0.3} You’ll join me soon enough."

    show ghost angry

    menu:
        "Please, don’t hurt me!":
            show ghost angry talk
            ghost "{sc}Oh, I want to,{w=0.3} [player_name],{w=0.3} I really do."

        "What do you want?":
            show ghost angry talk
            ghost "{sc}To attain what’s rightfully mine."

    show ghost sad talk
    ghost "{sc}I once had a treasure...{w=0.3} but it’s been taken away from me."
    show ghost angry talk
    ghost "{sc}I want you to find it for me,{w=0.3} [player_name]."
    show ghost angry
    menu:
        "I’ll see what I can do.":
            show ghost angry talk
            ghost "{sc}Now...{w=0.3}, LEAVE!"

        "Escape":
            pass

    stop music fadeout 4

    jump day2
