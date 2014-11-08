import item

class container(item.item):
    def __init__(self, parent):
        item.item.__init__(self, parent)
        self.items = []

    def addItem(self, item):
        self.items.append(item)

    def removeItem(self, item):
        self.items.remove(item)

    def containsItemType(self, itemType):
        contains = False
        item = None
        for it in self.items:
            if isinstance(it, itemType):
                contains = True
                item = it
        return contains, item
