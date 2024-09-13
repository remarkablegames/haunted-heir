label basement:

    if basement_locked:
        scene bg door closed with dissolve

        play sound locked

        player "The door is locked."

        menu:
            "What do you want to do?"

            "Unlock the door with the key" if item.is_inventory("key"):
                play sound unlocked
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

            "Go downstairs":
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

        "Look around":
            player "The air feels chilly here..."

        "Go upstairs":
            jump explore_inside_day
