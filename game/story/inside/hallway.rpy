label hallway(with_dissolve=True):

    if night:
        if with_dissolve:
            scene bg hallway night with dissolve
        else:
            scene bg hallway night

    else:
        if with_dissolve:
            scene bg hallway day with dissolve
            show lord with dissolve
        else:
            scene bg hallway day
            show lord

    menu:
        "What do you want to do?"

        "Talk to the Lord" if not night:
            jump hallway_lord

        "Look around":
            call screen explore_hallway

        "Go elsewhere":
            jump explore_inside_day

    return

label hallway_lord:

    menu:
        lord "How may I help you?"

        "Hand the treasure over" if item.is_inventory("necklace"):
            play sound treasure

            $ item.use("necklace")
            $ handed_treasure = "lord"

            player "I found a necklace."

            lord smirk "Thanks for giving it to me."
            lord "I’ll get it appraised today,{w=0.3} and I’ll make sure to reward you handsomely."

            $ night = True

            jump bedroom

        "Show the scroll" if item.is_inventory("scroll"):
            play sound paper

            $ item.use("scroll")

            player "I found a scroll near the basement."

            lord @ sigh "The [surname] family stores many artifacts there."

            player "Do you know what comes at night?"

            lord @ disgust "Some things are better not knowing..."

            call hallway(with_dissolve=False)

        "Nevermind":
            call hallway(with_dissolve=False)

screen explore_hallway():
    use back("hallway")

    vbox:
        for i in range(8):
            textbutton "{alpha=0}{noalt}WINDOW":
                xpos 90
                ypos 210
                action Jump("hallway_window")

    vbox:
        for i in range(8):
            textbutton "{alpha=0}{noalt}WINDOW":
                xpos 330
                ypos 210
                action Jump("hallway_window")

    vbox:
        for i in range(8):
            textbutton "{alpha=0}{noalt}WINDOW":
                xpos 1410
                ypos 210
                action Jump("hallway_window")

    vbox:
        for i in range(8):
            textbutton "{alpha=0}{noalt}WINDOW":
                xpos 1640
                ypos 210
                action Jump("hallway_window")

label hallway_window:
    $ dialogue = renpy.random.choice(["The skies are clear tonight.", "The moon shines brightly."]) if night else renpy.random.choice(["The skies are clear today.", "The sun shines brightly."])
    player "[dialogue]"
    call screen explore_hallway
