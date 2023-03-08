class Item:
    def __init__(self, name, place):
        self.name = name
        self.place = place

class Place:
    def __init__(self, name, desc, exits):
        self.name = name
        self.desc = desc
        self.exits=exits
    def look(self):
        print(self.desc)
        if len(self.exits) == 0:
            print("There is no way out!")
        else:
            for e in self.exits:
                print("There is an exit "+e.direction+".")
    def isExit(self, strExit):
        for e in self.exits:
            print(e.direction)
        return strExit in self.exits

class Exit:
    def __init__(self, direction, place):
        self.direction=direction
        self.place=place



print("Welcome to the adventure game")

#p = Place("", "", e)
p = Place("green",
          "You are in a large, green room.",
          {}
    )
e = {} #empty set of exits
p.exits={Exit("north", p), Exit("south", p)}
p.look()

while True:
    print()
    print("What would you like to do?")
    strcmd=input()
    o=strcmd.split()
    if len(o)==0:
        print("What?")
        continue
    if len(o)>2:
        print("I can only understand two words at a time!")
        continue
    strverb=o[0]
    if len(o)>1:
        strnoun=o[1]
    else:
        strnoun=""
    if strverb=="go":
        if not p.isExit(strnoun):
            print("I can't go that way")
            continue
        
    print("I don't know how to '"+strverb+"'.")
    print("I don't know what a '"+strnoun+"' is.")
