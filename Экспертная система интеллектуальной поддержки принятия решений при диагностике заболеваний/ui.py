import tkinter as tk
from inference_engine import InferenceEngine
from knowledge_base import KnowledgeBase

class DiagnosisApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Экспертная система диагностики заболевания")

        self.knowledgeBase = KnowledgeBase()
        self.knowledgeBase.load_data()
        self.inferenceEngine = InferenceEngine(self.knowledgeBase)

        self.initUi()

    def initUi(self):
        self.simptomLabel = tk.Label(self.root, text="Введите симптомы (через запятую): ")
        self.simptomLabel.pack(pady=10)

        self.simptomEntry = tk.Entry(self.root, width=50)
        self.simptomEntry.pack(pady=5)

        self.diagnoseButton = tk.Button(self.root, text="Диагностировать", command=self.diagnose)
        self.diagnoseButton.pack(pady=10)

        self.resultLabel = tk.Label(self.root, text="")
        self.resultLabel.pack(pady=10)

    def diagnose(self):
        symptoms = self.simptomEntry.get().split(',')
        symptoms = [simptom.strip() for simptom in symptoms]
        diseases = self.inferenceEngine.diagnose(symptoms)
        resultText = "Возможные заболевания: \n"
        if diseases:
            for  diasease, score in diseases:
                resultText += f"{diasease} (Совпадений: {score})\n"
        else:
            resultText = "Нет совпадений для введенных симптомов."
        self.resultLabel.config(text=resultText)

if __name__ == "__main__":
    root = tk.Tk()
    app = DiagnosisApp(root)
    root.mainloop()