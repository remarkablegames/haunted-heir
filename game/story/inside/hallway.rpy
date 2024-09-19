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
            $ dialogue = renpy.random.choice(["The skies are clear tonight.", "The moon shines brightly."]) if night else renpy.random.choice(["The skies are clear today.", "The sun shines brightly."])
            player "[dialogue]"

            call hallway(with_dissolve=False)

        "Go elsewhere":
            jump explore_inside_day

    return

label hallway_lord:

    menu:
        lord "How may I help you?"

        "Hand the treasure over" if item.is_inventory("necklace"):
            player "I found this necklace."

            $ item.use("necklace")
            $ handed_treasure = "lord"

            lord smirk "Thanks for giving it to me."
            lord "I’ll get it appraised by tomorrow,{w=0.3} and I’ll make sure to reward you handsomely."

            $ night = True

            jump bedroom

        "Nevermind":
            call hallway(with_dissolve=False)
