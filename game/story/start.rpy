label start:

    "Ugh..." with vpunch
    "You feel lightheaded as your consciousness fades in."

    scene bg bedroom day with fade

    butler "Are you alright, Sir?"
    butler "You had a nasty fall."
    butler "Do you remember your name?"

    $ player_name = renpy.input("Yes, my name is...", length=32).strip() or player_name

    butler "Glad to know you haven't forgotten your name, Master [player_name]."
    butler "What's the last thing you remember?"

    menu:
        "The last thing I remember is..."

        "Nothing":
            butler "Ah, that's not a good sign."

        "...":
            pass

    butler "You may have amnesia."
    butler "I suggest you rest up and your memories may come back."

    jump end
