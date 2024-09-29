label night3_kitchen_ghost:

    scene bg kitchen night with dissolve

    show ghost smile with dissolve

   
    if empathy_kitchen < 0:
        kitchen_ghost "Oh. It is you again. Come back to be a brute?"
        jump kitchen_blunt_35
    else:
        kitchen_ghost "Hello. I have been thinking about when last we spoke."
        jump kitchen_empathy_35

label kitchen_blunt_35:

    menu:
        "Maybe I was a little too direct, but I’ve never had to deal with anything like this before. I don’t know what I'm doing.":
            $ empathy_kitchen -= 1
            jump kitchen_blunt_4
        "I can’t imagine it was an easy time. Are you okay?":
            $ empathy_kitchen += 1
            jump kitchen_empathy_4
label kitchen_empathy_35:

    menu:
        "I am sorry if I was too direct, but I’ve never had to deal with something like this before. I don’t have a guide.":
            $ empathy_kitchen -= 1
            jump kitchen_blunt_4
        "I appologize for being too blunt. Are you okay?":
            $ empathy_kitchen += 1
            jump kitchen_empathy_4



label kitchen_blunt_4:

    kitchen_ghost "Yes, well, I am sure you at least understand basic etiquette. It is far from polite to just throw such a revelation at someone."
    jump kitchen_neutral_2

label kitchen_empathy_4:

    kitchen_ghost "No, I am not. Memories of my later years have come back to roost. I see now why I am so reticent."
    jump kitchen_neutral_2

label kitchen_neutral_2:
   
    player  "What exactly have you come to learn?"

    kitchen_ghost "I recall my illness. The staff feared it was contagious. So few stayed. I suppose I succumbed to it."

    menu:
        "I’m glad you’ve come around. Now we need to get you with the other shards of yourself. Then you can recombine and we can get this over with.":
            $ empathy_kitchen -= 1
            jump kitchen_blunt_5
        "I’m so sorry you had such a terrible experience. I’ll have to reunite you with the other parts of yourself for you to move on. When you’re ready of course.":
            $ empathy_kitchen += 1
            jump kitchen_empathy_5

label kitchen_blunt_5:

    kitchen_ghost "I feel the fever even now. I recognize this for what it is. This hunger is not something I can fix. This is no existence. I cannot accept this. I am done with you for now. You will let me come to terms with this at my own speed."
    jump end_night3

label kitchen_empathy_5:

    kitchen_ghost "I feel the fever even now. I recognize this for what it is. This hunger is not something I can fix. This is no existence. I cannot accept this. I cannot face them. Not yet. I fear the trauma I may recall. I need time. Please, let me have time."
    jump end_night_3

label end_night_3:
    player "I understand."


    jump kitchen
