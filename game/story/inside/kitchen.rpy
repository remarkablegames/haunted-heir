label kitchen:

    if night:
        scene bg kitchen night with dissolve
    else:
        scene bg kitchen day with dissolve

    if item.show("key"):
        show screen basement_key

    call kitchen_dialogue

    menu:
        "What do you want to do?"

        "Look around":
            call screen explore_kitchen

        "Go elsewhere":
            hide screen basement_key
            jump explore_inside_day

label kitchen_dialogue:
    if day == 1 and night and not day1_whisper:
        $ day1_whisper = True

        player "Let’s see...{w=0.3} What’s in the fridge?"

        unknown "{sc}Find...{w=0.3} Treasure..."

        player "What...{w=0.3} was that?"
        player "Am I hearing things?"

        unknown "{sc}Go...{w=0.3} Basement..."

        player "Well,{w=0.2} there goes my appetite."
        player "I’ll just head back to bed."
        player "I feel spooked."

        $ sleep = True

    return

screen explore_kitchen():
    use back("kitchen")

    textbutton "{alpha=0}{noalt}PAINTING\nPAINTING\nPAINTING\nPAINTING":
        xpos 120
        ypos 280
        action Call("kitchen_painting")

    textbutton "{alpha=0}{noalt}CABINETCABIN\nCABINETCABIN\nCABINETCABIN\nCABINETCABIN":
        xpos 560
        ypos 215
        action Call("kitchen_cabinet")

    textbutton "{alpha=0}{noalt}BREAD\nBREAD":
        xpos 790
        ypos 410
        action Call("kitchen_bread")

    textbutton "{alpha=0}{noalt}FRIDGERATER\nFRIDGERATER\nFRIDGERATER\nFRIDGERATER\nFRIDGERATER\nFRIDGERATER\nFRIDGERATER\nFRIDGERATER\nFRIDGERATER\nFRIDGERATER":
        xpos 1430
        ypos 280
        action Call("kitchen_fridge")

label kitchen_painting:
    player "A painting of the outdoors.{w=0.3} How serene."
    call screen explore_kitchen

label kitchen_cabinet:
    player "I don’t see anything in the cabinets."
    call screen explore_kitchen

label kitchen_bread:
    player "Just took a bite of the bread,{w=0.3} it tastes stale."
    call screen explore_kitchen

label kitchen_fridge:
    player "There isn’t much in the fridge."
    call screen explore_kitchen

screen basement_key():
    imagebutton:
        xpos 1400
        ypos 440
        idle "items/key.png"
        action Jump("basement_key_found")
        at scale(0.2)

label basement_key_found:
    $ item.find("key")
    hide screen basement_key
    player "What’s this key doing here?"
    player "I wonder what it unlocks."
    call screen explore_kitchen
