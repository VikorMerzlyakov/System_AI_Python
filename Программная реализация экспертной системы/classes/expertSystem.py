from .knowledgeBase import KnowledgeBase


class ExpertSystem:
    def __init__(self, knowledgeBase):
        self.knowledgeBase = knowledgeBase

    def askQuestion(self, attribute, value):
        frames = self.knowledgeBase.findFramesByAttribute(attribute, value)
        if frames:
            return "\n".join(str(frame) for frame in frames)
        else:
            return "Нет информации по вашему запросу."

    def addNewFrame(self, frame):
        self.knowledgeBase.addFrame(frame)

    def updateFrame(self, name, attribute, newValue):
        frame = self.knowledgeBase.getFrame(name)
        if frame:
            frame.updateSlot(attribute, newValue)

    def removeFrame(self, name):
        self.knowledgeBase.removeFrame(name)