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
            player "The skies are clear today."
            call hallway(False)

        "Go elsewhere":
            jump explore_inside_day

label hallway_lord:

    menu:
        lord "How may I help you?"

        "Hand the treasure over" if item.is_inventory("necklace"):
            player "I found a treasure in the mansion."

            $ item.use("necklace")
            $ handed_treasure = "lord"

            lord "Thanks for giving it to me."
            lord "I’ll make sure to reward you handsomely."

            call hallway(False)

        "Nevermind":
            call hallway(False)
