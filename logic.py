import random
import settings as option
import configparser


def cards():
    cfgr = configparser.ConfigParser()
    cfgr.read('settings.cfg')
    return int(cfgr.get('Other', 'howManyCards'))

def interval():
    cfgr = configparser.ConfigParser()
    cfgr.read('settings.cfg')
    random.seed()
    m = random.randint(1, int(cfgr.get('Other', 'howManyReturns')))
    return m

def logic():
    tasks = [1, 2, 3, 4]

    random.seed()
    randomTask = random.randint(0, len(tasks)-1)
    taskToDo = tasks[randomTask]
    print(str(taskToDo))
    if taskToDo == tasks[0]:
        option.task1 = True
        option.task2 = False
        option.task3 = False
        option.task4 = False
    elif taskToDo == tasks[1]:
        option.task1 = False
        option.task2 = True
        option.task3 = False
        option.task4 = False
    elif taskToDo == tasks[2]:
        option.task1 = False
        option.task2 = False
        option.task3 = True
        option.task4 = False
    elif taskToDo == tasks[3]:
        option.task1 = False
        option.task2 = False
        option.task3 = False
        option.task4 = True
