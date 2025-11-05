label day3_bad_ending:

    play music the_cold_breeze_through_the_window1

    scene bg interior entrance day with dissolve

    show lord smirk with dissolve

    lord "Good morning,{w=0.3} [player_name]."
    lord "How was your night?"

    menu:
        "It was okay.":
            lord @ happy "Great...{w=1} I’m glad you’re here."

        "Creepy, as usual.":
            lord @ angry "Don’t worry...{w=0.6} it’ll grow on you."

    lord @ sigh "Ah...{w=1} I appreciate you giving me the treasure."
    lord "Turns out,{w=0.3} it’s worth a pretty penny."

    player "Who left that there?"

    lord @ sigh "Who knows?{w=0.3} There are many mysteries here."

    player "I believe it.{w=0.3} When will I receive the payment?"

    play sound ["<silence 2.5>", cash]

    lord smirk "Right about...{w=1.5} now."

    lord neutral "Well, I’m off.{w=0.3} Take care..."

    hide lord with Dissolve(1)

    stop music fadeout 0.5
    queue music seek_and_slaughter1
    queue music [seek_and_slaughter2, seek_and_slaughter3]

    pause 0.5

    scene bg interior entrance evening with Dissolve(1)

    player "This place...{w=0.3} the air is getting heavier."

    scene bg interior entrance night with Dissolve(1)

    play sound crash

    scene bg interior entrance night with hpunch

    player "What was that?"

    unknown "{sc}You’re...{w=0.3} now...{w=0.3} mine..."

    player "Oh no...{w=0.3} I shouldn’t have used the treasure for my own selfish purposes..."

    play sound ghost

    player "Now it looks like I’ll be tormented...{w=0.3} for years to come."

    jump end
