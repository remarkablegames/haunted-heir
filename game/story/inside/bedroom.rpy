label bedroom:

    if night:
        scene bg bedroom night with dissolve
    else:
        scene bg bedroom day with dissolve

    menu:
        "What do you want to do?"

        "Rest":
            $ dialogue = renpy.random.choice(["Time to get some rest.", "I’m feeling pretty tired.", "Can’t wait to fall asleep.", "Time to count sheep."])
            player "[dialogue]"

            scene black with fade
            pause 0.5

            $ night = not night

            jump bedroom

        "Look around":
            call screen explore_bedroom

        "Leave the bedroom":
            jump explore_inside_day

screen explore_bedroom():
    use back("bedroom")

    vbox:
        for i in range(8):
            textbutton "{alpha=0}{noalt}PLANTS":
                action Jump("bedroom_plant")
                hover_sound None
                xpos 130
                ypos 335

    textbutton "{alpha=0}{noalt}P\nL\nA":
        action Jump("bedroom_plant")
        hover_sound None
        xpos 420
        ypos 400

    vbox:
        for i in range(7):
            textbutton "{alpha=0}{noalt}BEDBEDBEDBEDBEDBEDBEDBED":
                action Jump("bedroom_bed")
                hover_sound None
                xpos 820
                ypos 455

label bedroom_plant:
    player "Someone needs to take care of this plant."
    call screen explore_bedroom

label bedroom_bed:
    player "The bed is soft."
    call screen explore_bedroom
