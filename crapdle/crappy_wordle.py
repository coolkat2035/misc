import random, os

length = 5
solution = None
words = []

#load the thing into memory first so we don't have to do it every check
#https://svnweb.freebsd.org/csrg/share/dict/words
with open("words.txt", 'r') as file:
  words = [x.replace('\n', '') for x in file.readlines()]

words = [x for x in words if len(x) == length]
solution = random.choice(words)

def validate(ans):#Answer not accepted
  if len(ans) != 5:#Too short/long
    return 1
  if ans not in words:#Not an actual word
    return 2
  return 0

def check(ans):#check the whole thing char by chat
  pattern = ""
  for c in range(len(ans)):
    if ans[c] == solution[c]:#0 = correct place
      pattern = pattern + '0'
      
    elif ans[c] in solution:#1 = wrong place
      pattern = pattern + '1'

    else:#doesnt exist in the word
      pattern = pattern + '2'

  return pattern
########################################################################
hp = 6
if input("""Welcome to Crappy Wordle! Type enter to start the game,
or anything else to see the instructions.""") != '':
  input(
  """ This is a guessing game where you guess a word each turn. 

  You will then see a new line printed out with 4 possibilities:")
  1. An error message
  or your answer, with
  2. Two spaces surrounding a character (like this: e )
     means this character is not in the correct answer.
  3. A pair of round brackets around a character (like this: (e) )
     means this character is in the correct answer, but wrong place.
  4. A pair of square brackets around a character (like this: [e] )
     means this character is in the right place of the correct answer.

  You have 6 tries before the game is over.
  Good Luck!

  (Press enter to start the game.)""")

os.system("clear")
  
while True:
  if hp <= 0:
    print(f"Game over! The correct answer is '{solution}'")
    break
  else:
    print(hp,"attempts left.")

  answer = input("Guess a word(5 characters): ")
  print('\r')
  
  if validate(answer) == 1:
    print("Word is too short/long!")
    continue
  elif validate(answer) == 2:
    print("This doesn't exist!")
    continue
  
  for i in range(len(check(answer))):
    if check(answer)[i] == '0':
      print(f"[{answer[i]}]", end = '')
    elif check(answer)[i] == '1':
      print(f"({answer[i]})", end = '')
    else:
      print(f" {answer[i]} ", end = '')
  print()
  
  hp -= 1

  if check(answer) == "00000":
    print("You win!")
    break

  
  
  
