label pond:

    if night:
        scene bg pond night with dissolve
    else:
        scene bg pond day with dissolve

    if item.show("necklace"):
        show screen necklace

    menu:
        "What do you want to do?"

        "Explore the pond":
            call screen explore_pond

        "Go elsewhere":
            hide screen necklace
            jump explore_outside_day

screen explore_pond():
    use back("pond")

    hbox:
        for y in [0, 0, 0, 50, 100]:
            textbutton "{alpha=0}{noalt}BRIDGE\nBRIDGE\nBRIDGE\nBRIDGE\nBRIDGE":
                xpos 1040
                ypos 600 + y
                action Call("pond_bridge")

    hbox:
        for i in range(16):
            textbutton "{alpha=0}{noalt}TREES\nTREES\nTREES\nTREES\nTREES\nTREES\nTREES\nTREES\nTREES\nTREES":
                xpos 30
                ypos 130
                action Call("pond_tree")

    textbutton "{alpha=0}{noalt}ROCK\nROCK":
        xpos 720
        ypos 505
        action Call("pond_rock")

    hbox:
        for i in range(7):
            textbutton "{alpha=0}{noalt}GRASS\nGRASS\nGRASS\nGRASS\nGRASS\nGRASS\nGRASS\nGRASS\nGRASS\nGRASS\nGRASS":
                xpos 0
                ypos 590
                action Call("pond_grass")

label pond_bridge:
    player "This bridge looks very old.{w=0.3} I need to be careful."
    call screen explore_pond

label pond_tree:
    player "I think those are pine trees."
    call screen explore_pond

label pond_rock:
    player "I guess they never bothered to move that rock."
    call screen explore_pond

label pond_grass:
    player "This grass definitely needs to be cut."
    call screen explore_pond

screen necklace():
    imagebutton:
        xpos 1817
        ypos 775
        idle "items/necklace.png"
        action Jump("necklace_found")
        at scale(0.1)

label necklace_found:
    $ item.find("necklace")
    hide screen necklace
    player "Wow, this is stunning necklace!"
    player "I wonder if someone lost this."
    call screen explore_pond
