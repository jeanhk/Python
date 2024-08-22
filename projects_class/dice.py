import random  # Import statement should be at the top of the file


#
#Dicee
#
def get_number():
  return random.randint(1, 6)
  
a = get_number()
b = get_number()

if (a + b) == 12:
  print("You rolled a double six!")
elif a == b:
  print("You rolled a double in your dice!.")
  print(f"You rolled {a} and {b}")
else:
  print(f"You rolled {a} and {b}")