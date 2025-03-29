'''Запрос даты'''
# from numpy.random.mtrand import choice


def get_date(untt):
    print(f'список доступных дат: - \n\t{str(untt)}')
    date_fild = input('Введите КОГДА СДЕЛАТЬ - ')
    return date_fild

def get_task():
    '''Запрос ввода поставленной задачи'''
    task_fild = input('Введите ЧТО СДЕЛАТЬ - ')
    return task_fild

def check_comand(unit):
    dates = ['сегодня', 'завтра', 'послезавтра']
    if unit in dates:
        return True
    else:
        return False


'''функция добавления задачи в список'''
def add_task(time, wish): # функция добавления задачи в список
    '''функция добавления задачи в список'''
    time.append(wish)
    pass

def show_tasks(variant):
    if variant == 1:
        print(HELP)
    elif variant == 2:
        print()
    pass

comand_list = ['show', 'add', 'help', 'exit']

dates = ['сегодня', 'завтра', 'послезавтра']

HELP = """
Список доступных команд:
* print/show  - напечать все задачи на заданную дату
* todo - добавить задачу
* help - Напечатать help
* exit - выход
    """

dates_tasks = {}

# for i in range(3):
#     date = get_date()
#     task = get_task()
#     dates_tasks[date] = task

# print('Список дел на 3 дня')
# for i in dates_tasks:
#     print(f'\t{i} - {dates_tasks[i]}')
# print(f'Список дел: {date_fild} - {task}')

wish_list = {
'today': [],
'tomorrow': [],
'enother': []
    }

choice_task = input('выбирите команду - ')


if choice_task == 'show':
    print(HELP)

elif choice_task == 'todo':
    # print('список доступных дат: \n\tСегодня, Завтра, Потом')
    if get_date(dates) == 'Сегодня':
        wish_list['today'].append(get_task())

    elif get_date(dates) == 'завтра':
        wish_list['tomorrow'].append(get_task())

    elif get_date(dates) == 'потом':
        wish_list['enother'].append(get_task())


print(today)




