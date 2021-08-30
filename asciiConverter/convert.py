from PIL import Image
import math, sys, os, time

MAXW = 150
args = sys.argv
lum_map = "@#$%&?/:,."#lightmode
img_name = "defaultNameYouShouldntSeeThis.png"#image name lmao should be updated
name_noext = "defaultNameYouShouldntSeeThis"

try:#if user typing in cmd or clicking on the file (no argvs)
    img_name = args[1]#cmd
    if "-d" in args:
        lum_map = lum_map[::-1]#switch to darkmode

except IndexError:#clicking
    img_name = input("Enter your input image path here (with extension!!!)> ")

    while True:
        is_flip = input("Do you want to flip the brightness? Default is light background dark text.(y/n)")
        if is_flip.startswith('y'):
            print("Alright, moving on.")
            lum_map = lum_map[::-1]#switch to dark mode
            break
        elif is_flip in ['n', "no", "nah", "nope"]:
            print("Got it, moving on")
            break
        else:
            print("I don't really understand...\n")#bruh stop playing its not funny
            continue

############################Stuff gets real now####################################

past = time.time()#timer cause why not

def convertToString(target:str):
    """
    Turns image to max width of 350, outputs a string of them.

    input: target(String of path name)
    output: final_str(String)
    """
    final_str = """"""#thing to be written in file
    global lum_map
    global MAXW

    try:
        with Image.open(target) as img:
            wpercent = MAXW/float(img.size[0])#how much width should shrink or grow
            hsize = int(img.size[1]* wpercent)
            img = img.resize((MAXW,hsize))

            img = img.convert("L")

            #img.show()#DEBUG

            for y in range(img.height):#row
                for x in range(img.width):#column
                    lum = img.getpixel((x,y))
                    final_str += lum_map[math.floor(lum / 256 *10)]#math mapping 8)

                final_str += "\n"
            return final_str

    except FileNotFoundError:
        print("This image does not exist...")
        return "did your finger slipped"
        
    

name_noext = os.path.splitext(img_name)[0]#getting rid of the ext
with open(f"{name_noext}_ascii.txt", 'w') as ascii:
    ascii.writelines(convertToString(img_name))

input(f"Done! Time used: {round(time.time() - past)} seconds.\nI made a text file for the ascii, go check it out in notepad! Press enter to exit...")

