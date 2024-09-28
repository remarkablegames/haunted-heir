label night2_pond_ghost:

    scene bg pond night with dissolve

    show ghost smile with dissolve

    pond_ghost "New blood. But familiar, too."

    menu:
        "AH! I thought the first one was terrifying!":
            $ empathy_pond -= 1
            jump night2_pond_blunt1

        "OH! Okay. Hi. Hello.":
            $ empathy_pond += 1
            jump night2_pond_empathy1

label night2_pond_blunt1:

    pond_ghost "Panic. Yes, good. Leave me to linger and float. Eternal."

    menu:
        "Does this mean you know you’re dead? That saves time. How can I help you move on?":
            $ empathy_pond -= 1
            jump night2_pond_blunt2

        "I’m here to help you move on. What can I do for you?":
            $ empathy_pond += 1
            jump night2_pond_empathy2

label night2_pond_empathy1:

    pond_ghost "Panic. Yes, good. Leave me to linger and float. Eternal."

    menu:
        "Does this mean you know you’re dead? That saves time. How can I help you move on?":
            $ empathy_pond -= 1
            jump night2_pond_blunt2

        "I’m here to help you move on. What can I do for you?":
            $ empathy_pond += 1
            jump night2_pond_empathy2

label night2_pond_blunt2:

    pond_ghost "Ah, new owner. Need me out? No deal. Here is comfort. Here is happiness. No moving on. No moving."

    menu:
        "I won’t act like I know what the afterlife holds, but that doesn’t seem helpful for either of us.":
            $ empathy_pond -= 1
            jump night2_pond_blunt3

        "It’s scary, but I truly do want to help you if I can. Mansion or no mansion.":
            $ empathy_pond += 1
            jump night2_pond_empathy3

label night2_pond_empathy2:

    pond_ghost "Ah, but I must leave for you, no? Help me, or help you? I am comfortable here. No moving on. No moving."

    menu:
        "I won’t act like I know what the afterlife holds, but that doesn’t seem helpful for either of us.":
            $ empathy_pond -= 1
            jump night2_pond_blunt3

        "It’s scary, but I truly do want to help you if I can. Mansion or no mansion.":
            $ empathy_pond += 1
            jump night2_pond_empathy3

label night2_pond_blunt3:

    pond_ghost "Hrm. A point worth considering. Leave me to my pond. My stars. My rest."

    jump pond

label night2_pond_empathy3:

    pond_ghost "Help that comes with reward should be questioned. Leave me now to question and consider."

    jump pond
