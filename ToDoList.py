# 1. Класс должен называться `ToDoList`.
#
# 2. Конструктор класса не должен принимать никаких параметров,
# кроме обязательного параметра `self`.
#
# 3. У класса должен быть метод `add_task(self, task)`,
# который добавляет новую задачу в список задач.
#
# 4. У класса должен быть метод `complete_task(self, task)`,
# который помечает указанную задачу как выполненную.
# Если задача не найдена, метод должен выводить сообщение о том,
# что такая задача не существует.
#
# 5. У класса должен быть метод `remove_task(self, task)`,
# который удаляет указанную задачу из списка.
# Если задача не найдена, метод должен выводить сообщение о том,
# что такая задача не существует.
#
# 6. У класса должен быть метод `list_tasks(self)`,
# который выводит список всех задач.
# Выполненные задачи должны отмечаться специальным значком.


class ToDoList:
    def __init__(self):
        self.task_list = {}
        self.task_number = 0

    def add_task(self):  # добавляет новую задачу в список задач
        self.task_number += 1
        task = input("\nНовая задача:\n>> ")
        self.task_list[self.task_number] = {
            "ballot_box": "\N{BALLOT BOX}",
            "task": task
        }
        print(f"Задача добавлена в список задач под №{self.task_number}.")

    def complete_task(self):  # помечает указанную задачу как выполненную
        task_number = int(input("\nВведите номер задачи, "
                                "чтобы пометить как выполненную:\n>> "))
        self.task_list[task_number] = {
            "ballot_box": "\N{BALLOT BOX WITH CHECK}",
            "task": self.task_list[task_number].get("task")
        }
        print(f"Задача под №{task_number} помечена как выполненная.")

    def remove_task(self):  # удаляет указанную задачу из списка
        task_number = int(input("\nВведите номер задачи для удаления:\n>> "))
        del self.task_list[task_number]
        print(f"Задача под №{task_number} удалена.")

    def get_list_tasks(self):  # выводит список всех задач
        print("\nСписок задач:")
        for key, value in self.task_list.items():
            print(f"{value["ballot_box"]} Задача №{key}: {value["task"]}")
