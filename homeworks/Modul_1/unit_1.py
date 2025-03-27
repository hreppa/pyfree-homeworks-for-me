'''Запрос даты'''
def get_date():
    date_fild = input('Введите КОГДА СДЕЛАТЬ - ')
    return date_fild
def get_task():
    task_fild = input('Введите ЧТО СДЕЛАТЬ - ')
    return task_fild


dates_tasks = {}

for i in range(3):
    date = get_date()
    task = get_task()
    dates_tasks[date] = task

print('Список дел на 3 дня')
for i in dates_tasks:
    print(f'\t{i} - {dates_tasks[i]}')
# print(f'Список дел: {date_fild} - {task}')
