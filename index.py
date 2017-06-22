def AreaPerimeter(height,width):
    height = int(height)
    width = int(width)
    area = height * width
    pre = (2*height) + (2*width)
    print "area:",height
    print "pre:",pre
    return

while True:
    h = raw_input("height: ")
    w = raw_input("width: ")
    AreaPerimeter(h,w)
