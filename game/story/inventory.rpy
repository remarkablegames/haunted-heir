screen inventory():
    if len(item.inventory):
        frame:
            xalign 1.0

            hbox:
                for i in item.inventory:
                    image "items/[i].png" at resize(75, 75)
