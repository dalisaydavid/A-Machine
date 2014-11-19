from item       import item
from container  import container
from room       import room
from actor      import actor
from gate       import gate

class aMachine:
    def __init__(self):
        self.actor = None
        self.intro = None
        self.currentRoom = None

    def setInitialRoom(self, room):
        self.currentRoom = room

    def setActor(self, actor):
        self.actor = actor

    def setIntro(self, intro):
        self.intro = intro

    def run(self):
        print(self.intro)

        alive = True

        self.actor.parent = self.currentRoom
        print(self.currentRoom.getDescription())
        while alive:
            print(self.currentRoom.getDescription())
            print("You see:\n" + self.currentRoom.getHeldItemsStr())
            print(">", end=' ', flush=True)
            inString = input().split()
            print()

            if inString[0].lower() == 'go':
                if inString[1].lower() == 'north':
                    self.currentRoom = self.currentRoom.north.goThrough()
                elif inString[1].lower() == 'south':
                    self.currentRoom = self.currentRoom.south.goThrough()
                elif inString[1].lower() == 'east':
                    self.currentRoom = self.currentRoom.east.goThrough()
                elif inString[1].lower() == 'west':
                    self.currentRoom = self.currentRoom.west.goThrough()
            elif inString[0].lower() == 'look':
                if len(inString) == 1:
                    print(self.currentRoom.getDescription())
                    print("You see:\n" + self.currentRoom.getHeldItemsStr())
                else:
                    item = self.currentRoom.getItemFromString(inString[1])
                    print(item.getDescription())
            self.actor.parent = self.currentRoom
