label night2_kitchen_ghost:

    scene bg kitchen night with dissolve

    show ghost smile with dissolve

    kitchen_ghost "Oh, hello again. You certainly took off in a hurry last night."

    menu:
        "Well, you certainly are a startling spirit.":
            $ empathy_kitchen -= 1
            jump night2_kitchen_blunt1

        "Ah, apologies. I had to rush to my room.":
            $ empathy_kitchen += 1
            jump night2_kitchen_empathy1

label night2_kitchen_blunt1:

    kitchen_ghost "I know I may have snuck up on you, but that gives you no right to call a young lady startling."
    kitchen_ghost "All I was asking for was dinner if you were so inclined to assist. I feel like I haven’t eaten in days."

    menu:
        "You can’t eat. You’re a ghost.":
            $ empathy_kitchen -= 1
            jump night2_kitchen_blunt2

        "Is there a reason you haven’t made food for yourself?":
            $ empathy_kitchen += 1
            jump night2_kitchen_empathy2

label night2_kitchen_empathy1:

    kitchen_ghost "I'm sorry to hear that. Are you feeling well? I know I often feel quite warm. The  icebox is a nice refuge from such states. "
    kitchen_ghost "Speaking of, are you cooking? I feel as though I haven’t eaten in days."

    menu:
        "You can’t eat. You’re a ghost.":
            $ empathy_kitchen -= 1
            jump night2_kitchen_blunt2

        "Is there a reason you haven’t made food for yourself?":
            $ empathy_kitchen += 1
            jump night2_kitchen_empathy2

label night2_kitchen_blunt2:

    kitchen_ghost "I suppose there is no point in continuing conversation with such a boorish person. All I’ve done is be kind and ask a favor. There is no reason to be so rude."

    menu:
        "You’re dead. I have to help you move on. How can we get this moving?":
            $ empathy_kitchen -= 1
            jump night2_kitchen_final

        "I’m sorry to say, but you’ve passed on. I’m here to help you.":
            $ empathy_kitchen += 1
            jump night2_kitchen_final

label night2_kitchen_empathy2:

    kitchen_ghost "If you are implying I cannot cook, I will have you know our fine chefs taught--I was so young when… Where have they gone? Why have I not…?"

    menu:
        "You’re dead. I have to help you move on. How can we get this moving?":
            $ empathy_kitchen -= 1
            jump night2_kitchen_final

        "I’m sorry to say, but you’ve passed on. I’m here to help you.":
            $ empathy_kitchen += 1
            jump night2_kitchen_final

label night2_kitchen_final:

    if empathy_kitchen < 0:
        kitchen_ghost "ENOUGH! Enough. I must go. I need to think."
    else:
        kitchen_ghost "Yay"

    jump kitchen
