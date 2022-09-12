print ("Welcome to our password rating application")
password = input("type your password here to get a strength score")
passwordscore = 0
for character in password:
    if character in "abcdefghijklmnopqrstuvwxyz":
      passwordscore = passwordscore + 1
      print (str(character)+ "= 1")
for character in password:
    if character in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
      passwordscore = passwordscore + 2
      print (str(character)+ "= 2")
for character in password:
    if character in "0123456789":
      passwordscore = passwordscore + 3
      print (str(character)+ "= 3")
for character in password:
    if character in ",./?;':[]-)(*&^%$#@!<>":
      passwordscore = passwordscore + 7
      print (str(character)+ "= 7")

length = len(password)
print ("this is your character score" + str(passwordscore))
print ("this is your length score" + str(length))
print ("this is your total score" + str(passwordscore + length))
