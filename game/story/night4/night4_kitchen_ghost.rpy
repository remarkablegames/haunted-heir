label night4_kitchen_ghost:

    scene bg kitchen night with dissolve

    show ghost smile with dissolve

    label kitchen_ghost_night_4:

    kitchen_ghost "I am remembering unpleasant things. The fragmented joys of childhood are being filled in with the suffering of my final years."

    player "That was never my intention."

    kitchen_ghost "Yes, I know. Actions can have unforeseen consequences. You say I must meet with the other parts of myself. Have they been experiencing similar issues?"

    menu:
        "The only shard I’ve met so far has their own problems. Real big fan of the pond.":
            $ empathy_kitchen -= 1
            jump kitchen_blunt_6
        "Well, the only other part of you I’ve met was at the pond. They have been cryptic and pretty resistant to moving on.":
            $ empathy_kitchen += 1
            jump kitchen_empathy_6

label kitchen_blunt_6:

    kitchen_ghost "The pond? I loved swimming. In time, that was also one of the few places I could go as refuge from the pain. I see. I really am only a part of myself. If I agree to this… gathering, would it help you collect the other?"

    player "I’m just as new to this as you, but I can’t see how it would hurt."

    kitchen_ghost "Okay. I will do it. Let me know when. I do not know if I am ready for this, but I also do not know what I am missing until I try."
    jump neutral_3

label kitchen_empathy_6:

    kitchen_ghost "I did love that pond. Though it went from exercise to treatment. I can see why a part of me would linger there. I am also only a part of me. Memories of a full home. Delicious food. Family and friends. If I have these, do the other parts of me? Would gathering together help them?"
    jump neutral_3

label neutral_3:
    player "I’m just as new to this as you, but I can’t see how it would hurt."

    kitchen_ghost "Okay. I will do it. Let me know when. I do not know if I am ready for this, but I also do not know what I am missing until I try."

    menu:
        "Great. I’ll work on getting the rest of you ready, and then we can get this over with.":
            $ empathy_kitchen -= 1
            jump kitchen_blunt_7
        "I understand how hard this is. You’re brave for trying.":
            $ empathy_kitchen += 1
            jump kitchen_empathy_7

label kitchen_blunt_7:

    kitchen_ghost "Brusque as ever. I will wait for your word."

    return

label kitchen_empathy_7:

    kitchen_ghost "Thank you. I worry what memories they have that I do not. I will wait for your word."




    jump kitchen
