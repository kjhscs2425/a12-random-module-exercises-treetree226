# Make a random pet.
import random
# Choose:
# Type of animal (at least 3 choices, string)
animal = random.choice(["snake", "puppy", "dragon", "pig", "goat", "tiger"])
# Age (integer)
age = random.randint(1,100)
# Color (at least 3 choices, string)
color =random.choice(["red", "pink", "blue", "gold", "silver", "green"])
# Weight (float)
weight =random.uniform(1,100)

# Print a summary of your pet using an f-string
print(f"Your pet is a {age} year old, {color}, {weight} pounds, {animal}")