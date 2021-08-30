from PIL import Image
with Image.open("testimgSmall.png") as img:

    wpercent = 350/float(img.size[0])
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((350,hsize))


    img.show()
