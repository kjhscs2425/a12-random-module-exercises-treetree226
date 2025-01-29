import random
def spin_twister_spinner():
  """
  Returns a list with a random color, side, and appendage
  
  colors: "red", "green", "yellow", or "blue"
  sides: "left" or "right"
  appendage: "hand" or "foot"
  """
  colors= random.choice(["red", "blue","yellow", "green"])
  sides= random.choice(["left","right"])
  appendage= random.choice(["hand", "foot"])
  return [colors, sides, appendage]

# Here's the function call. This should print a random assortment of twister commands
for i in range(10):
  print(spin_twister_spinner())