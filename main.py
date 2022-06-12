import matplotlib.pyplot as plt
from my_interface import *
import sys

fig, ax = plt.subplots()
ax.set_title('Оценка объемов продаж')
ax.grid()

listNames = []  # сюда записываем наименования шкал по порядку
listColors = ['red', 'green', 'black', 'yellow', 'purple', 'blue']
listA1 = []
listA2 = []
listA = []
listB = []
listX = [[]]  # список с координатами графика
listY = [[]]  # список с координатами графика
countSales = []  # список с нашими Х, которые будем проверять
listFunction = []  # список с результатами функций принадлежности i - это само значение j - результат функции
listResultFunction = [[]]  # список с результатами функций принадлежности i - это само значение j - результат функции


def function(a1, a2, a, b, x):
    if x <= a and x >= a1:
        return float(1 - ((a - x) / (a - a1)))
    elif x <= b and x >= a:
        return float(1)
    elif x <= a2 and x >= b:
        return float(1 - ((x - b) / (a2 - b)))
    else:
        return float(0)
    return float(0)


def checkFunction():
    if listFunction[0] > listFunction[1]:
        if listFunction[0] > listFunction[2]:
            return listFunction[0]
        else:
            return listFunction[2]
    else:
        if listFunction[1] > listFunction[2]:
            return listFunction[1]
        else:
            return listFunction[2]


def checkResult():
    for i in range(0, len(listFunction)):
        if checkFunction() == listFunction[i]:
            return i


def addInfo():  # Заполняем данными наши списки
    listNames.append(ui.TextLineName.toPlainText())
    ui.listNames.addItem(str(ui.TextLineName.toPlainText()))

    listA1.append(float(ui.TextLineA1.toPlainText()))
    listA2.append(float(ui.TextLineA2.toPlainText()))
    listA.append(float(ui.TextLineA.toPlainText()))
    listB.append(float(ui.TextLineB.toPlainText()))

    ui.TextLineA1.clear()
    ui.TextLineA2.clear()
    ui.TextLineA.clear()
    ui.TextLineB.clear()
    ui.TextLineName.clear()

def addPoints():  # заносим наши точки в Х и У
    countSales.append(float(ui.TextLineCountSales.toPlainText()))
    for i in range(0, len(listNames)):
        listX.insert(i, [listA1[i], listA[i], listB[i], listA2[i], listA1[i]])
        listY.insert(i, [0, 1, 1, 0, 0])

def functionForAllX():
    return 0

def addXToList():
    countSales.append(float(ui.TextLineCountSales.toPlainText()))
    ui.listForX.addItem(ui.TextLineCountSales.toPlainText())
    ui.TextLineCountSales.clear()


def create():
    addPoints()
    for i in range(0, len(listNames)):
        ax.plot(listX[i], listY[i], color=listColors[i], label=listNames[i])
    helpNumber = checkResult()
    plt.scatter(countSales[0], checkFunction(), color=listColors[helpNumber],
                label='Объем продаж (Х) соответсвует уровню -' + listNames[helpNumber])
    plt.legend(fontsize=14)
    plt.tight_layout()
    plt.show()


app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()

ui.buttonCreateGraf.clicked.connect(create)
ui.buttonAddX.clicked.connect(addXToList)
ui.buttonAddInfo.clicked.connect(addInfo)

sys.exit(app.exec_())
