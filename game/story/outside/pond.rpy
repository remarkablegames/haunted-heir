label pond:

    scene bg pond day with dissolve

    if not necklace:
        show screen necklace

    menu:
        "What do you want to do?"

        "Explore the pond":
            player "Seems nobody has been here for a while."

            jump pond

        "Go somewhere else":
            jump explore_outside_day

screen explore_pond():
    textbutton "Back" action Jump("pond")

    textbutton "{alpha=0}BRIDGE\nBRIDGE\nBRIDGE\nBRIDGE":
        xpos 1293
        ypos 761
        action Call("bridge")

    textbutton "{alpha=0}TREE\nTREE\nTREE\nTREE":
        xpos 1565
        ypos 456
        action Call("tree")
    
    textbutton "{alpha=0}STONE\nSTONE\nSTONE\nSTONE":
        xpos 120
        ypos 280
        action Call("stone")
    
    textbutton "{alpha=0}GRASS\nGRASS\nGRASS\nGRASS":
        xpos 1085
        ypos 563
        action Call("grass")

label bridge:
    player "This bridge looks very old.{w=0.3} I need to be careful."
    call screen bridge

label tree:
    player "I think those are pine trees."
    call screen tree

label stone:
    player "I guess they never bothered to move that stone."
    call screen stone

label grass:
    player "This grass definitely needs to be cut."
    call screen grass

screen necklace():
    imagebutton:
        xpos 1817
        ypos 775
        idle "items/necklace.png"
        hover "items/necklace.png"
        action Jump("necklace_found")
        at scale(0.1)

label necklace_found:
    $ necklace = True
    hide screen necklace
    player "Wow, this is stunning! I wonder who lost this."
    jump pond