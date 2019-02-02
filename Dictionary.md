# Dictionary lesson

## Upper and lower case

Notice the following, when you have this code:

```#Python
color = input("What is your favorite color? ")
if color == "blue":
    print("I like blue too.")
else:
    print("My favorite color is blue.")
```

If you run this problem and put in:

```#Bash
>caselesson.py
What is your favorite color? Blue

My favorite color is blue.
```

In the example, I use `Blue` with an uppercase `B`, but in the code, I check: `if color == 'blue':` which is a lowercase 'b'.

One practice to make sure that you can check your strings no matter the casing is to use: `.lower()`.

```#Python
color = input("What is your favorite color? ")
if color.toLower() == "blue":
    print("I like blue too.")
else:
    print("My favorite color is blue.")
```

## Introduction to Dictionaries

A dictionary in Python allows you to connect two pieces of data together. Look at this example:

```#Python
colors = {
    "red": "Red looks great on race cars",
    "yellow": "Yellow is the color of a school bus",
    "blue": "Blue is the color of the sky",
    "black": "At night it is very black"
}
```

The variable `color` above is a dictionary. This dictionary have 4 keys: 'red', 'yellow', 'blue', 'black'

Here is the code for `dictionary.py`:

```#Python
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
```

Notice in this code that we create a variable `testcolor` which is the lower case version of the variable `color`. This is so that if you want to print `color` back to the user exactly how they typed it, you can do that.

Look now at this line, `output = colors[testcolor]`. The square brackers `[testcolor]` tell Python which key you want to look for in the `colors` dictionary.

We know that `testcolor` is in the dictionary, because we tested it before hand by doing `if testcolor in colors:`.

## Exercise

Create a dictionary of your favorite super powers and your opinions on them.

Then prompt the user for their favorite super power and let them know your opinion from the dictionary. If the user puts in a power that you didn't expect, make sure that you tell them that too.