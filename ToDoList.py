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
        self.task_storage = []

    def get_task_store(self):  # проверяет, пустой ли список задач
        if not self.task_storage:
            print("\nСписок задач пуст!")
        return self.task_storage

    def add_task(self):  # добавляет новую задачу в список задач
        task = input("\nНовая задача:\n>> ")
        self.task_storage.append({
            "\N{BALLOT BOX}": task
        })
        print(f"Задача добавлена в список задач "
              f"под №{len(self.task_storage)}.")

    def complete_task(self):  # помечает указанную задачу как выполненную
        if self.get_task_store():
            task_number = int(input("\nВведите номер задачи, "
                                    "чтобы пометить как выполненную:\n>> "))
            if task_number <= 0:
                raise
            else:
                self.task_storage[task_number - 1] = {
                    "\N{BALLOT BOX WITH CHECK}":
                        self.task_storage[task_number - 1].popitem()[1]
                }
                print(f"Задача под №{task_number} помечена как выполненная.")

    def remove_task(self):  # удаляет указанную задачу из списка
        if self.get_task_store():
            task_number = int(input(
                "\nВведите номер задачи для удаления:\n>> "
            ))
            if task_number <= 0:
                raise
            else:
                del self.task_storage[task_number - 1]
                print(f"Задача под №{task_number} удалена.")

    def get_list_tasks(self):  # выводит список всех задач
        if self.get_task_store():
            print("\nСписок задач:")
            sequence_number = 0
            for task in self.task_storage:
                sequence_number += 1
                for key, value in task.items():
                    print(f"{key} Задача №{sequence_number}: {value}")
