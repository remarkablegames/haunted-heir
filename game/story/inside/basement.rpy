label basement:

    jump basement_door

label basement_door:

    if basement_locked:
        scene bg door closed with dissolve

        player "The door is locked."

        menu:
            "What do you want to do?"

            "Unlock the door with the key" if item.is_inventory("key"):
                $ basement_locked = False
                $ item.use("key")

                player "The door is unlocked."

                jump basement_door

            "Go upstairs":
                jump explore_inside_day

    else:
        scene bg door open with dissolve

        menu:
            "What do you want to do?"

            "Enter basement":
                jump basement_room

            "Go upstairs":
                jump explore_inside_day

label basement_room:

    $ basement_visit += 1

    if basement_visit == 1:
        jump basement_room_first_visit

    scene bg basement light with dissolve

    menu:
        "What do you want to do?"

        "Explore the basement":
            player "It feels chilly in the basement."

            jump basement_room

        "Go upstairs":
            jump explore_inside_day

label basement_room_first_visit:

    scene bg basement light with dissolve

    player "The air feels chilly here..."

    "{i}Crash."

    player "What was that?"

    scene bg basement dark with dissolve

    player "..."

    show ghost girl angry:
        xalign 0.5
        ease .5 zoom 1.5
    with moveinbottom
    with vpunch


    miss "You… finally.{w=0.3} I’ve waited…{w=0.3} so long…"

    player "Who...{w=0.3} who are you?"

    miss "Does it matter?{w=0.3} You’ll join me soon enough."

    menu:
        "Please, don't hurt me!":
            miss "Oh, I want to,{w=0.3} [player_name],{w=0.3} I really do."

        "You don't scare me. What do you want?":
            miss "To take revenge on someone."


    player "What can I do?"

    miss "I once had a daughter.{w=0.3} She was taken from me."

    miss "Before she died,{w=0.3} she gifted me a necklace she made.{w=0.3} It's been lost."

    miss "Maybe you can find it, [player_name].{w=0.3} Rather,{w=0.3} you better find it."

    player "What does it look like?"

    miss "It has a light blue diamond.{w=0.3} Now go find it, [player_name]."

    player "Your daughter gave it to you?{w=0.3} I'll find it, I promise."

    pause 1

    jump act_2
