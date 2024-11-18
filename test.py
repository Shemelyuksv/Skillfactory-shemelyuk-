import random

students = ["Анна", "Саша", "Сережа", "Юля", "Даша"]
students.sort()
classes = ["Русский", "Математика", "Иностранный", "Физика"]
classes.sort()

students_marks = {}
for student in students:
    students_marks[student] = {}
    # print(f"{students_marks}")
    for class_ in classes:
        marks = [random.randint(1, 5) for i in range(2)]
        students_marks[student][class_] = marks


def is_add_mark(student, class_, mark):
    if student in students_marks.keys() and class_ in students_marks[student].keys():
        students_marks[student][class_].append(mark)
        print(f"Для {student} по предмету {class_} добавлена оценка {mark}")
    else:
        print("ОШИБКА: неверное имя ученика или название предмета")


def is_del_mark(student, class_, mark):
    if student in students_marks.keys() and class_ in students_marks[student].keys():
        students_marks[student][class_].remove(mark)
        print(f"Для {student} по предмету {class_} удалена оценка {mark}")
    else:
        print("ОШИБКА: неверное имя ученика или название предмета")


def is_rem_mark(student, class_, mark, mark_new):
    if (
        student in students_marks.keys()
        and class_ in students_marks[student].keys()
        and mark in students_marks[student][class_]
    ):
        students_marks[student][class_].remove(mark)
        students_marks[student][class_].append(mark_new)
        print(
            f"Для {student} по предмету {class_} изменена оценка {mark} на оценку {mark_new}"
        )
    else:
        print("ОШИБКА: неверное имя ученика, название предмета или оценка")

def is_add_student (student_new, classes):
    if student_new not in students_marks:
        students_marks[student_new] = {class_: [] for class_ in classes}
        students.append(student_new)
    else:
        print(f"Студент {student_new} уже есть в журнале.")


while True:
    print("""Список доступных команд:
    1. Добавить оценку ученика по предмету
    2. Вывести средний бал по всем предмету по каждому ученику
    3. Вывести все оценки по всем ученикам
    4. Удалить оценку по предмету для ученика
    5. Редактировать оценку по предмету для ученика
    6. Добавить, удалить или редактировать ученика
    ...
    99. Выход из программ
    """)
    command = int(input("Введите номер команды: "))
    if command == 1:
        print(students)
        student = input("Введите имя ученика: ")
        print(classes)
        class_ = input("Введите предмет: ")
        mark = int(input("Введите оценку (1-5): "))
        is_add_mark(student, class_, mark)
        print(students_marks)

    elif command == 2:
        for student in students:
            print(f"\b{student}")
        for class_ in classes:
            marks_summ = sum(students_marks[student][class_])
            marks_len = len(students_marks[student][class_])
            middle_marks = marks_summ / (marks_len + 1)
            print(f"{class_} - {middle_marks}")

    elif command == 3:
        print("3. Вывести все оценки по всем ученикам")
        for student in students:
            print(student)
            for class_ in classes:
                print(f"\t{class_} - {students_marks[student][class_]}")
            print()

    elif command == 4:
        print(students)
        student = input("Введите имя ученика: ")
        print(classes)
        class_ = input("Введите предмет: ")
        print(marks)
        mark = int(input("Введите оценку (1-5): "))
        is_del_mark(student, class_, mark)
        print(students_marks)

    elif command == 5:
        print(students)
        student = input("Введите имя ученика: ")
        print(classes)
        class_ = input("Введите предмет: ")
        print(marks)
        mark = int(input("Выберете оценку для замены: "))
        mark_new = int(input("Введите новую оценку (1-5): "))
        is_rem_mark(student, class_, mark, mark_new)
        print(students_marks)
        
    elif command == 6:
        command_students = int(input('''Выберете команду:
             1. Для добавления нового ученика
             2. Для редактирования ученика
             3. Для удаления ученика
        '''))
        if command_students == 1:
            student_new = input("Введите имя ученика: ")
            is_add_student (student_new, classes)
            print(f"Добавлен новый ученик {student_new}")
            print(students_marks)
                    
    elif command == 99:
        print("Завершение программы")
        break