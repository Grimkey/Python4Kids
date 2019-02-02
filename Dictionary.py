colors = {
    "red": "Red looks great on race cars",
    "yellow": "Yellow is the color of a school bus",
    "blue": "Blue is the color of the sky",
    "black": "At night it is very black"
}

color = input("What is your favorite color? ")
testcolor = color.lower()

if testcolor in colors:
    output = colors[testcolor]
    print(output)
else:
    print("Intersting. I haven't thought about that color.")