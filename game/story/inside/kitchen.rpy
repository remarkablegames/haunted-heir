label kitchen:

    if night:
        scene bg kitchen night with dissolve
    else:
        scene bg kitchen day with dissolve

    if item.show("key"):
        show screen basement_key

    if day == 1 and night:
        player "Time to grab something to eat!"

        unknown "{sc}Find...{/sc}{w=0.3} {sc}Treasure...{/sc}{w=0.3} {sc}Go...{/sc}{w=0.3} {sc}Basement...{/sc}"

        player "What...{w=0.2} in the world{w=0.2} was that?"

    menu:
        "What do you want to do?"

        "Explore the kitchen":
            call screen explore_kitchen

        "Go elsewhere":
            hide screen basement_key

            jump explore_inside_day

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
    player "The cabinets are empty."
    call screen explore_kitchen

label kitchen_bread:
    player "The bread looks stale.{w=0.3} I probably shouldn’t eat it."
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
