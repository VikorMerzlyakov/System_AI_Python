from classes.knowledgeBase import KnowledgeBase
from classes.frameStruct import Frame, Slot
from classes.expertSystem import ExpertSystem

def main():
    knowledge_base = KnowledgeBase()

    # Создание фреймов
    frame1 = Frame("компьютер1")
    frame1.addSlot(Slot("тип", "ноутбук"))
    frame1.addSlot(Slot("производитель", "Dell"))
    frame1.addSlot(Slot("цена", 1000))
    frame1.addSlot(Slot("операционная_система", "Windows 10"))

    frame2 = Frame("монитор1")
    frame2.addSlot(Slot("диагональ", 15.6))
    frame2.addSlot(Slot("разрешение", "1920x1080"))
    frame2.addSlot(Slot("тип_подключения", "HDMI"))

    # Добавление фреймов в базу знаний
    knowledge_base.addFrame(frame1)
    knowledge_base.addFrame(frame2)

    # Создание экспертной системы
    expert_system = ExpertSystem(knowledge_base)


    print(expert_system.askQuestion("тип", "ноутбук"))

    # Добавление нового фрейма
    new_frame = Frame("компьютер2")
    new_frame.addSlot(Slot("тип", "десктоп"))
    new_frame.addSlot(Slot("производитель", "HP"))
    new_frame.addSlot(Slot("цена", 1500))
    new_frame.addSlot(Slot("операционная_система", "Linux"))
    expert_system.addNewFrame(new_frame)

    # Обновление фрейма
    expert_system.updateFrame("компьютер1", "цена", 1200)

    # Удаление фрейма
    expert_system.removeFrame("монитор1")

    # Вывод базы знаний
    print(knowledge_base)

if __name__ == "__main__":
    main()