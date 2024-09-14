label day3_good_ending:

    play music hide_and_seek1
    queue music [hide_and_seek2, hide_and_seek3]

    scene bg interior entrance day with dissolve

    show lord smile with dissolve

    lord "Good morning,{w=0.3} [player_name]."
    lord "How was your night?"

    player "It was nice, actually."
    player "I feel like the air in this mansion suddenly became lighter."

    lord "Wait...{w=0.3} [player_name]...{w=0.3} did you?"

    player "Yes,{w=0.3} she’s finally at peace now."

    lord "I never told you who she was,{w=0.3} did I?"

    player "No,{w=0.1} you didn’t.{w=0.3} Do you know her?"

    lord "Yes,{w=0.3} she’s my daughter."

    lord "I couldn’t leave her here,{w=0.3} not while she was still so angry."

    player "I’m sorry to hear that."
    player "She’s in a much better place now."

    queue music hide_and_seek1

    lord "Indeed,{w=0.2} and thank you for that."
    lord "Also, the papers have been finalized."
    lord "Congratulations on inheriting this mansion."
    lord "I’m off on my own journey now."
    lord "Take care..."

    hide lord with dissolve

    pause 0.5

    scene bg interior entrance evening with dissolve

    player "Guess I won’t be as rich as I imagined."
    player "But even though I’ve given away the treasure,{w=0.2} at least I feel at peace."

    jump end
