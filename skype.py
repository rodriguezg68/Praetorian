import random

prev_guess = []
while True:
  input = raw_input("Number of gladiatros: ")
  input2 = raw_input("Number of weapons: ")
  input3 = raw_input("Numebr of guesses: ")
  if int(input) > 0 and int(input2) > 0 and int(input3) > 0:
    break
  print "Error: inputs out of bounds"

gladiators = int(input)
weapons = int(input2)
weapon_numb = []
max_guess = int(input3)
guess = []

for count in range(weapons):
  weapon_numb.append(count)

def rand_assign():
  global weapons
  for preson in range(gladiators):
    while True:
      randnumb = random.choice(weapon_numb)
      if randnumb not in guess:
        guess.append(randnumb)
        break

def eliminate_numb():
  for number in list(weapon_numb):
    if number in prev_guess[-1][-3]:
      weapon_numb.remove(number)

def conjecture(number):
  global guess
  if number == 0:
    rand_assign()
  else: 
    if prev_guess[-1][-2] == 0 or prev_guess[-1][-2] < weapons / 2:
      if prev_guess[-1][-2] == 0:
        eliminate_numb()
      rand_assign()
    elif prev_guess[-1][-2] >= weapons / 2:
      if prev_guess[-1][-2] == weapons:
        eliminate_numb()

def main():
  global guess
  for number in range(max_guess):
    conjecture(number)
    print guess
    while True:
      input = raw_input("Number of correct weapons: ")
      input2 = raw_input ("Numebr of gladiators killed: ")
      if int(input) >= 0 and int(input2) >= 0:
        break
      print "Error: inputs out of bounds"
    if int(input) == gladiators and int(input2) == gladiators:
      print "You win!"
      break
    prev_guess.append([guess, int(input), int(input2)])
    guess = []

  print "You lost!"

main()
