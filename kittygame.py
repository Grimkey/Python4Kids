from collections import namedtuple
from enum import Enum

MyStruct = namedtuple("MyStruct", ("field1", "field2"))
m = MyStruct("foo", "bar")

class Room(Enum):
    Description = 1
    North = 2
    West = 3
    South = 4
    East = 5
    Up = 6
    Down = 7

def LydiaRoom(op):
    return {
        Room.Description: "You are in Lydia's room. Everything is picked up and looks like except for the candy wrapper on the floor.",
        Room.West: "You walk into the call. There is a scratching post. It is less interesting than the rug."
    }.get(op, "Can't go that way")


commands = {
    "R":"Description",
    "N":"North",
    "S":"South",
    "E":"East",
    "W":"West",
    "U":"Up",
    "D":"Down"
}

print("Allowed commands:")
print(commands)