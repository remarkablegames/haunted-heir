transform opacity(value):
    alpha value

transform flip:
    xzoom -1.0

transform unflip:
    xzoom 1.0

transform resize(x, y):
    size (x, y)

transform rotate(degrees):
    rotate degrees

transform scale(ratio):
    zoom ratio

transform tint(color):
    matrixcolor TintMatrix(color)

transform ypos(position):
    ypos position
