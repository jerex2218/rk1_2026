from PIL import Image

def line(img, x0, y0, x1, y1): 
    steep = abs(y1 - y0) > abs(x1 - x0)
    if steep:
        x0, y0 = y0, x0
        x1, y1 = y1, x1

    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    dx = x1 - x0
    dy = abs(y1 - y0)
    ystep = 1 if y1 > y0 else -1

    delta = 0
    y = y0
    for x in range(x0, x1 + 1):
        if steep:
            img.putpixel((y, x), (255, 255, 255))
        else:
            img.putpixel((x, y), (255, 255, 255))

        delta += 2 * dy
        if delta >= dx:
            delta -= 2 * dx
            y += ystep


img = Image.new("RGB", (100, 100))

line(img, 20, 20, 35, 55)   
#line(img, 10, 50, 70, 70)   
#line(img, 90, 20, 10, 40) 

img.save("imagname.png")