label kitchen:

    $ visits_kitchen += 1

    if night:
        scene bg kitchen night with dissolve
    else:
        scene bg kitchen day with dissolve

    if item.show("key") and visits_kitchen > 1:
        show screen basement_key with dissolve

    if night and not event_whisper1:
        jump day1_whisper

    menu:
        "What do you want to do?"

        "Look around":
            call screen explore_kitchen

        "Go elsewhere":
            hide screen basement_key
            jump explore_inside_day

screen explore_kitchen():
    use back("kitchen")

    textbutton "{alpha=0}{noalt}PAINTING\nPAINTING\nPAINTING\nPAINTING":
        xpos 120
        ypos 280
        action Jump("kitchen_painting")

    textbutton "{alpha=0}{noalt}CABINETCABIN\nCABINETCABIN\nCABINETCABIN\nCABINETCABIN":
        xpos 560
        ypos 215
        action Jump("kitchen_cabinet")

    textbutton "{alpha=0}{noalt}BREAD\nBREAD":
        xpos 790
        ypos 410
        action Jump("kitchen_bread")

    textbutton "{alpha=0}{noalt}FRIDGERATER\nFRIDGERATER\nFRIDGERATER\nFRIDGERATER\nFRIDGERATER\nFRIDGERATER\nFRIDGERATER\nFRIDGERATER\nFRIDGERATER\nFRIDGERATER":
        xpos 1430
        ypos 280
        action Jump("kitchen_fridge")

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
        xpos 1384
        ypos 428
        idle "items/key.webp"
        action Jump("basement_key_found")
        at scale(0.3)
        if night:
            at scale(0.3), tint("#222")

label basement_key_found:
    $ item.find("key")
    hide screen basement_key
    player "What’s this key doing here?"
    player "I wonder what it unlocks."
    call screen explore_kitchen
