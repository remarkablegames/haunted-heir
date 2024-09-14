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

    show ghost girl angry at center, opacity(0.5), zoom(1.5)
    with moveinbottom
    with vpunch

    ghost "{sc}You...{w=0.3} finally...{w=0.3} I’ve waited...{w=0.3} so long..."

    player "Who...{w=0.3} who are you?"

    ghost "Does it matter?{w=0.3} You’ll join me soon enough."

    menu:
        "Please, don’t hurt me!":
            ghost "Oh, I want to,{w=0.3} [player_name],{w=0.3} I really do."

        "You don’t scare me. What do you want?":
            ghost "To take revenge on someone."

        "I’m sorry! What do you want?":
            ghost "To take revenge on someone."

    player "What can I do?"

    ghost "I once had a daughter.{w=0.3} She was taken from me."

    ghost "Before she died,{w=0.3} she gave me a necklace she made.{w=0.3} It’s been lost."

    ghost "Maybe you can find it, [player_name].{w=0.3} Rather,{w=0.3} you better find it."

    player "What does it look like?"

    ghost "It has a light blue diamond.{w=0.3} Now go find it, [player_name]."

    player "Your daughter gave it to you?{w=0.3} I’ll find it, I promise."

    stop music fadeout 4

    jump day2
