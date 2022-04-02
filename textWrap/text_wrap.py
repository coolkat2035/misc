MAP = """  ###    ###
 #####  #####
##############
##############
##############
##############
##############
 ############
  ##########
   ########
    ######
     ####
      ##
"""

text = input("Enter some text: ")
i = 0 #counter to keep track of what is selected

def place(char):#don't want to say end = '' everytime
  print(char, end = '')
  
for c in MAP:
  i %= len(text)
  if c == '#':
    place(text[i])
    i += 1
  else:
    place(c)

input("Press enter to exit!")
