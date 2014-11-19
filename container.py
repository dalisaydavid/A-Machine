import item

class container(item.item):
    def __init__(self, parent):
        item.item.__init__(self, parent)
        self.items = []
        self.itemDict = {}

    def addItem(self, it):
        self.items.append(it)
        it.parent = self
        self.itemDict[it.getName().lower()] = it

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

    def getItemFromString(self, string):
        item = self.itemDict.get(string.lower())
        if item == None:
            for it in self.items:
                if isinstance(it, container):
                    return it.getItemFromString(string)
        return item

    def getHeldItemsStr(self):
        first = True
        itemStr = ""
        for it in self.items:
            if first:
                first = False
            else:
                itemStr += ", "
            itemStr += it.getNameWithArticle()
            if isinstance(it, container):
                itemStr += ", "
                itemStr += it.getHeldItemsStr()
        return itemStr
