class Slot:
    def __init__(self, attribute, value):
        self.attribute = attribute
        self.value = value

    def __repr__(self):
        return f"Slot(attribute='{self.attribute}', value={self.value})"

class Frame:
    def __init__(self, name):
        self.name = name
        self.slots = {}

    def addSlot(self, slot):
        self.slots[slot.attribute] = slot

    def getSlot(self, attribute):
        return self.slots.get(attribute)

    def updateSlot(self, attribute, newValue):
        if attribute in self.slots:
            self.slots[attribute].value = newValue

    def removeSlot(self, attribute):
        if attribute in self.slots:
            del self.slots[attribute]

    def __repr__(self):
        return f"Frame(name='{self.name}', slots={list(self.slots.values())})"
