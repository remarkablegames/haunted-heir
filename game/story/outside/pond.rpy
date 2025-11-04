label pond:

    play music running_water

    if night:
        scene bg pond night with dissolve
    else:
        scene bg pond day with dissolve

    menu:
        "What do you want to do?"

        "Look around":
            stop bleep
            call screen explore_pond

        "Go elsewhere":
            stop bleep
            stop music fadeout 1
            jump explore_outside_day


screen explore_pond():
    use back("pond")

    hbox:
        for y in [0, 0, 0, 50, 100]:
            textbutton "{alpha=0}{noalt}BRIDGE\nBRIDGE\nBRIDGE\nBRIDGE\nBRIDGE":
                action Jump("pond_bridge")
                hover_sound None
                xpos 1040
                ypos 600 + y

    hbox:
        for i in range(16):
            textbutton "{alpha=0}{noalt}TREES\nTREES\nTREES\nTREES\nTREES\nTREES\nTREES\nTREES\nTREES\nTREES":
                action Jump("pond_tree")
                hover_sound None
                xpos 30
                ypos 130

    textbutton "{alpha=0}{noalt}ROCK\nROCK":
        action Jump("pond_rock")
        hover_sound None
        xpos 720
        ypos 505

    hbox:
        for i in range(7):
            textbutton "{alpha=0}{noalt}GRASS\nGRASS\nGRASS\nGRASS\nGRASS\nGRASS\nGRASS\nGRASS\nGRASS\nGRASS\nGRASS":
                action Jump("pond_grass")
                hover_sound None
                xpos 0
                ypos 590


label pond_bridge:
    player "This bridge looks old.{w=0.3} I need to be careful when crossing."
    call screen explore_pond


label pond_tree:
    player "I think those are pine trees."
    call screen explore_pond


label pond_rock:
    player "I guess no one bothered to move that rock."
    call screen explore_pond


label pond_grass:
    player "Someone should cut the grass."
    call screen explore_pond
