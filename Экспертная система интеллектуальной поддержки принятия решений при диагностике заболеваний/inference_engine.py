from knowledge_base import KnowledgeBase

class InferenceEngine:
    def __init__(self, knowlege_base):
        self.knowledgeBase = knowlege_base

    def diagnose(self, symptoms):
        return self.knowledgeBase.getDiasesBySymptomes(symptoms)