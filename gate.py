import item

class gate(item.item):
    def __init__(self, parent):
        item.item.__init__(self, parent)
        self.linkedGate = None
        self.parent = parent

    def linkTo(self, otherGate):
        self.linkedGate = otherGate
        otherGate.linkedGate = self

    def isLinked(self):
        if otherGate == None:
            return False
        else:
            return True

    def goThrough(self):
        return self.linkedGate.parent
