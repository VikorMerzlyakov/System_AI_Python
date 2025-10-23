from .frameStruct import Frame

class KnowledgeBase:
    def __init__(self):
        self.frames = {}

    def addFrame(self, frame):
        self.frames[frame.name] = frame

    def getFrame(self, name):
        return self.frames.get(name)

    def findFramesByAttribute(self, attribute, value):
        return [frame for frame in self.frames.values() if frame.getSlot(attribute) and frame.getSlot(attribute).value == value]

    def removeFrame(self, name):
        if name in self.frames:
            del self.frames[name]

    def __repr__(self):
        return f"KnowledgeBase(frames={list(self.frames.values())})"