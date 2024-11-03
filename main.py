from ToDoList import ToDoList


def run(tdl):
    while True:
        try:
            info = int(input("\nВведите число соответствующее действию:\n"
                             "1 - Добавить новую задачу в список задач\n"
                             "2 - Пометить задачу как выполненную\n"
                             "3 - Удалить задачу из списка\n"
                             "4 - Вывести список всех задач\n"
                             "0 - Завершить программу\n>> "))
            if info == 1:
                tdl.add_task()
            elif info == 2:
                tdl.complete_task()
            elif info == 3:
                tdl.remove_task()
            elif info == 4:
                tdl.get_list_tasks()
            elif info == 0:
                break
            else:
                print("Соответствие не найдено!\n")

        except:
            print("Ввод некорректного значения!\n")


tdl = ToDoList()

run(tdl)
