import random
import settings as option
import configparser


def cards():
    cfgr = configparser.ConfigParser()
    cfgr.read('settings.cfg')
    return int(cfgr.get('Other', 'howManyReturns'))

def interval():
    cfgr = configparser.ConfigParser()
    cfgr.read('settings.cfg')
    m = random.randint(1, int(cfgr.get('Other', 'howManyReturns')))
    return m

def logic():
    tasks = []
    tasks.append(option.task1)
    tasks.append(option.task2)
    tasks.append(option.task3)
    tasks.append(option.task4)

    for i in range(cards()):
        randomTask = random.randint(0, len(tasks)-1)
        taskToDo = tasks[randomTask]
        return taskToDo
