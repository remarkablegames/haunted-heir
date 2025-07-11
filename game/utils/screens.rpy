screen back(label_name):
    frame:
        xpos (40 if renpy.variant("web") else 0)
        textbutton "Back":
            action Jump(label_name)
