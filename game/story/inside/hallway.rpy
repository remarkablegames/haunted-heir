label hallway(with_dissolve=True):

    if with_dissolve:
        if night:
            scene bg hallway night with dissolve
        else:
            scene bg hallway day with dissolve
    else:
        if night:
            scene bg hallway night
        else:
            scene bg hallway day

    if with_dissolve:
        show lord with dissolve
    else:
        show lord

    menu:
        "What do you want to do?"

        "Talk to the Lord":
            jump hallway_lord

        "Look around":
            player "The skies are clear today."
            call hallway(False)

        "Go elsewhere":
            jump explore_inside_day

label hallway_lord:

    menu:
        lord "How may I help you?"

        "Nevermind":
            call hallway(False)
