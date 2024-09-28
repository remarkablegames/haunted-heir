label night3_pond_ghost:

    scene bg pond night with dissolve

    show ghost smile with dissolve


    pond_ghost "The other has returned. There is much to discuss."

    menu:
        "I need to get you to the others. So you can recombine and cross over.":
            $ empathy_pond -= 1
            jump pond_blunt_4
        "What answers have you found?":
            $ empathy_pond  += 1
            jump pond_empathy_4

label pond_blunt_4:

    pond_ghost "Hah. You assume I accept your terms. No. Something is missing."
    jump pond_neutral

label pond_empathy_4:

    pond_ghost "Curious. Wonderful. Stay that way. You are missing much."
    jump pond_neutral

label pond_neutral:

    player "Missing?"

    pond_ghost "Some parts are not my place to say. I have lingered here for a very long time. Pieced together much of what was scattered. I stay here to ease the pain. Float. Another stays to ease the fever. The last stays to suffer. You are yet to see how we can help you."
    menu:
        "No, I think you heading to the afterlife would be very helpful for me, actually.":
            $ empathy_pond  -= 1
            jump pond_blunt_5
        "I'm not sure I understand. How am I involved? ":
            $ empathy_pond  += 1
            jump pond_empathy_5

label pond_blunt_5:

    pond_ghost "This is fact, but involves more than just the shards you know. You must be more curious. Your haste may cause you to miss things that are clear to others."

    player "Then what is my next step, if I’m rushing this?"

    pond_ghost "You are not ready to hear it. Just as we are not ready to face it. Leave me to my peace tonight."
    jump pond


label pond_empathy_5:

    pond_ghost "A vital piece. Light shiner. Truth bringer. Your focus on us comes from care or desperation? Move on quickly. For us or you? You bargain in subtlety."

    player "Then what is my next step, if I’m rushing this?"

    pond_ghost "You are not ready to hear it. Just as we are not ready to face it. Leave me to my peace tonight."
    jump pond



