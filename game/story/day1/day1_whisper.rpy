label day1_whisper:

    $ event_whisper1 = True

    play music a_hollow_call1

    player "Let’s see...{w=0.3} What’s in the fridge?"

    voice "voice/whisper/whisper1.ogg"
    unknown "{sc}Find...{w=0.3} the...{w=0.3} treasure..."

    player "What...{w=0.3} in the world was that?"
    player "Am I hearing things?"

    voice "voice/whisper/whisper2.ogg"
    unknown "{sc}Go...{w=0.3} to...{w=0.3} basement..."

    player "Welp,{w=0.2} there goes my appetite."
    player "I’m going straight back to bed."

    stop music fadeout 4

    jump kitchen
