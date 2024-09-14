label day3_bad_ending:

    play music the_cold_breeze_through_the_window1

    scene bg interior entrance day with dissolve

    show lord smirk with dissolve

    lord "Good morning,{w=0.3} [player_name]."
    lord "How was your night?"

    menu:
        "It was okay.":
            show lord laugh2
            lord "Great, I’m glad you’re here."

        "Creepy, as usual.":
            show lord laugh2
            lord "Don’t worry, it’ll grow on you."

    lord "I appreciate you giving me the treasure."
    show lord smirk 
    lord "Turns out,{w=0.3} it’s worth a pretty penny."

    player "Who left that there?"

    show lord

    lord "Who knows?{w=0.3} There are many mysteries here."

    player "I believe it.{w=0.3} When will I receive the payment?"

    show lord smirk

    lord "Right...{w=0.3} now."

    show lord laugh2

    lord "Well, I’m off.{w=0.3} Take care..."

    hide lord with dissolve

    stop music fadeout 1
    queue music seek_and_slaughter1
    queue music seek_and_slaughter2

    pause 0.5

    scene bg interior entrance evening with dissolve

    player "This place...{w=0.3} the air is getting heavier."

    scene bg interior entrance night with dissolve

    queue music [seek_and_slaughter2, seek_and_slaughter3]
    play sound crash

    player "What was that?"

    voice "voice/bad_end.ogg"
    unknown "{sc}You’re...{w=0.3} now...{w=0.3} mine..."

    player "Oh no...{w=0.3} I shouldn't have used the treasure for my own selfish purposes."
    player "Now it looks like I’ll be tormented...{w=0.3} for years to come."

    jump end
