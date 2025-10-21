label backyard:

    if night:
        play music night_ambience fadein 1
        scene bg backyard night with dissolve
    else:
        play music birds_chirping
        scene bg backyard day with dissolve

    menu:
        "What do you want to do?"

        "Look around":
            call screen explore_backyard

        "Go elsewhere":
            stop music fadeout 1
            jump explore_outside_day

screen explore_backyard():
    use back("backyard")

    vbox:
        for i in range(8):
            textbutton "{alpha=0}{noalt}PLANTS":
                action Jump("backyard_plants")
                hover_sound None
                xpos 210
                ypos 500

    vbox:
        for i in range(5):
            textbutton "{alpha=0}{noalt}PLANTS":
                action Jump("backyard_plants")
                hover_sound None
                xpos 385
                ypos 700

    vbox:
        for i in range(7):
            textbutton "{alpha=0}{noalt}PLANTS":
                action Jump("backyard_plants")
                hover_sound None
                xpos 520
                ypos 460

    textbutton "{alpha=0}{noalt}DOOR\nDOOR":
        action Jump("backyard_door")
        hover_sound None
        xpos 975
        ypos 510

    vbox:
        for i in range(4):
            textbutton "{alpha=0}{noalt}FLOWER":
                action Jump("backyard_flowers")
                hover_sound None
                xpos 1560
                ypos 590

    textbutton "{alpha=0}{noalt}F\nL\nO":
        action Jump("backyard_flowers")
        hover_sound None
        xpos 1705
        ypos 725

label backyard_door:
    player "The door is bolt shut."
    call screen explore_backyard

label backyard_plants:
    $ dialogue = renpy.random.choice(["The plants are lovely.", "Whoever planted these has a green thumb.", "What luscious plants."])
    player "[dialogue]"
    call screen explore_backyard

label backyard_flowers:
    $ dialogue = renpy.random.choice(["The flowers smell nice.", "The flowers are in full bloom.", "These flowers look beautiful."])
    player "[dialogue]"
    call screen explore_backyard
