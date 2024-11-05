from ToDoList import ToDoList


def run(to_do):
    while True:
        try:
            info = int(input("\nВведите число соответствующее действию:\n"
                             "1 - Добавить новую задачу в список задач\n"
                             "2 - Пометить задачу как выполненную\n"
                             "3 - Удалить задачу из списка\n"
                             "4 - Вывести список всех задач\n"
                             "0 - Завершить программу\n>> "))
            if info == 1:
                to_do.add_task()
            elif info == 2:
                to_do.complete_task()
            elif info == 3:
                to_do.remove_task()
            elif info == 4:
                to_do.get_list_tasks()
            elif info == 0:
                break
            else:
                print("Соответствие не найдено!")

        except:
            print("Ввод некорректного значения!")


to_do = ToDoList()
run(to_do)
