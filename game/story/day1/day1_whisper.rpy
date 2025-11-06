label day1_whisper:

    $ event_whisper1 = True

    play music a_hollow_call1

    player "Let’s see...{w=0.3} What’s in the fridge?"

    unknown "{sc}Find...{w=1.2} the...{w=1.5} treasure..."

    player "{i}{cps=10}What...{/cps}{w=0.3} in the world was that?"
    player "{i}Am I hearing things?"

    unknown "{sc}Go...{w=1.8} to...{w=1.8} basement..."

    player "Welp,{w=0.2} there goes my appetite."
    player "I’m going straight back to bed."

    stop music fadeout 4

    jump kitchen
