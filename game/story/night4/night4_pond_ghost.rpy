label night4_pond_ghost:

    scene bg pond night with dissolve

    show ghost smile with dissolve
    pond_ghost "Hello, caretaker. Gatherer. Here for the next steps?"

    menu:
        "I don’t know. Are you going to say anything helpful other than wait?":
            $ empathy_pond -= 1
            jump pond_blunt_6
        "Yes, I think I’m ready now.":
            $ empathy_pond += 1
            jump pond_empathy_6

label pond_blunt_6:

    pond_ghost "Oh, yes. Some tales are not mine to tell, but you are ready now."

    jump pond_neutral2

label pond_empathy_6:

    pond_ghost "Indeed, you are. I can feel it. It is time for tales and revelations. I too find myself ready for what comes. Though I am not as all-knowing as you seem to believe."

    jump pond_neutral2

label pond_neutral2:

    player "Tales? I’m listening."

    pond_ghost "I remember more of myself. Much more of the good. Smiling. Playing. You are bringing the pieces together. The picture is not whole, and the picture will not be pleasant. If this is to work, you must complete the image of our life."

    menu:
        "That’s the most direct you’ve been. I don’t know what to say.":
            $ empathy_pond -= 1
            jump pond_blunt_7
        "I’ll do my best to learn what I can and bring you three together.":
            $ empathy_pond += 1
            jump pond_empathy_7

label pond_blunt_7:

    pond_ghost "Say nothing. Continue listening. I choose my words carefully. You have my aid. When you are ready, we can make an attempt."

    jump pond

label pond_empathy_7:

    pond_ghost "I choose my words carefully. There is something you miss. When the time comes, I will be ready. We can make the attempt."

    jump pond




