class KnowledgeBase:
    def __init__(self):
        self.symptoms = {}
        self.diseases = {}

    def addSympthom(self, symptom, disease):
        if symptom not in self.symptoms:
            self.symptoms[symptom] = []
        self.symptoms[symptom].append(disease)
        if disease not in self.diseases:
            self.diseases[disease] = []
        self.diseases[disease].append(symptom)

    def getDiasesBySymptomes(self, symptoms):
        diseaseScores = {}
        for symptom in symptoms:
            if symptom in self.symptoms:
                for disease in self.symptoms[symptom]:
                    if disease not in diseaseScores:
                        diseaseScores[disease] = 0
                    diseaseScores[disease] += 1
        return sorted(diseaseScores.items(), key=lambda x: x[1], reverse=True)

    def load_data(self):
        # Пример загрузки данных в базу знаний
        data = [
            ("жар", "Грипп"),
            ("кашель", "Грипп"),
            ("головная боль", "Грипп"),
            ("жар", "Пневмония"),
            ("кашель", "Пневмония"),
            ("головная боль", "Мигрень"),
            ("головная боль", "Травма"),
            ("бол живота", "Гастроэнтерит"),
            ("жидкий стул", "Гастроэнтерит"),
            ("жар", "Гастроэнтерит"),
        ]
        for symptom, disease in data:
            self.addSympthom(symptom, disease)