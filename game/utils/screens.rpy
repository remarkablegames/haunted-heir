screen back(jump_to_label):
    $ back_button_xpos = 40 if renpy.variant("web") else 0

    frame:
        xpos back_button_xpos
        textbutton "Back":
            action Jump(jump_to_label)
