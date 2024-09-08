label basement:

    jump basement_door

label basement_door:

    if basement_locked:
        scene bg door closed with dissolve

        player "The door is locked."

        menu:
            "What do you want to do?"

            "Unlock door with key" if basement_key:
                $ basement_locked = False

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

    player "What a creepy looking basement."

    "{i}Crash."

    player "What was that?"

    scene bg basement dark with dissolve

    player "..."

    show penguin
    with moveinbottom
    with vpunch

    pause 1

    jump end
