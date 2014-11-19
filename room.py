import container
import gate

class room(container.container):
    def __init__(self):
        container.container.__init__(self, None)
        self.north = gate.gate(self)
        self.south = gate.gate(self)
        self.east = gate.gate(self)
        self.west = gate.gate(self)
