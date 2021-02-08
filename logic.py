import random
import settings as option
import inOut
import time

def cards():
    return option.howManyCards

def interval():
    m = random.randint(1, option.howManyReturns)
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

