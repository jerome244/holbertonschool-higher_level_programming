import random

number = random.randint(-10, 10)  # This generates a random signed number

# Print the number followed by whether it is positive, zero, or negative
print(f"{number} is", end=" ")
if number > 0:
    print("positive")
elif number == 0:
    print("zero")
else:
    print("negative")
