import aMachine

class rock(aMachine.item):
    def __init__(self, parent):
        self.gotonce = False
        self.description = "This is just a rock..."
        aMachine.item.__init__(self, parent)
    def getName(self):
        return "rock"
    def getNameWithArticle(self):
        return "a " + self.getName()
    def getDescription(self):
        if self.gotonce:
            return "This is MORE than a rock NOW!"
        self.gotonce = True
        return self.description

class coat(aMachine.item):
    def __init__(self, parent):
        aMachine.item.__init__(self, parent)
    def getName(self):
        return "coat"
    def getNameWithArticle(self):
        return "a " + self.getName()
    def getDescription(self):
        return "It's just a coat."

class hook(aMachine.container):
    def __init__(self, parent):
        aMachine.container.__init__(self, parent)
    def getName(self):
        return "hook"
    def getNameWithArticle(self):
        return "a " + self.getName()
    def getDescription(self):
        hasCoat = False
        description = "It's just a small brass hook, "
        contains = self.containsItemType(coat)
        if contains[0]:
            contains[1].parent = self
            description += 'with a coat hanging on it.'
        else:
            description += 'screwed to the wall.'
        return description

class mainRoom(aMachine.room):
    def __init__(self):
        aMachine.room.__init__(self)
        self.rock = rock(self)
        self.addItem(self.rock)

    def getDescription(self):
        return "It's the main room. Not much"

    def getName(self):
        return "main room"

    def getNameWithArticle(self):
        return "the " + self.getName()

    def connectNorth(self, gate):
        self.north.linkTo(gate)

class topRoom(aMachine.room):
    def __init__(self):
        aMachine.room.__init__(self)
        self.hook = hook(None)
        self.coat = coat(None)
        self.addItem(self.hook)
        self.hook.addItem(self.coat)

    def getDescription(self):
        return "It's the top room. Not much"

    def getName(self):
        return "top room"

    def getNameWithArticle(self):
        return "the " + self.getName()

class ourGame(aMachine.aMachine):
    def __init__(self):
        aMachine.aMachine.__init__(self)
        self.mainRoom = mainRoom()
        self.topRoom = topRoom()

        self.mainRoom.connectNorth(self.topRoom.south)

        self.setInitialRoom(self.mainRoom)

if __name__ == "__main__":
    theGame = ourGame()
    ourActor = aMachine.actor(None)
    theGame.setActor(ourActor)
    theGame.setIntro("WELCOME TO THE TEST!\nThis game is a test of the basic shell of A-Machine.")
    theGame.run()
