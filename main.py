import re
file = open("synonyms.txt", "r+")   #открытие файла для чтения
spisok = file.readlines()   #читает все строки и записывает в список
def synonyms():
    number = 0 #чтобы понимать, был ли найден синоним
    word = input(str("Введите слово: "))
    file.seek(0)    #в начало файла
    for i in file:  #для каждой строки файла
        if word in i:  #если есть это слово
            syn = re.split(r"[ ]", i) #делит строку по '-'  и возвращает список получившихся подстрок
            if word == syn[0]: #если первое слово из строки = введенному
                print(syn[2])   #то выводится 3й элемент строки
                if len(syn) == 4:   #если более одного синонима, то выводит и второй синоним
                    print(syn[3])
            else:
                print(syn[0])

            number = 1 #1 синоним был найден
            choice(word)   #передает введенное слово
    if number == 0:    #если синоним не найден:
        print("Синоним не найден")

def choice(word):
    new_sin = input("Добавить синоним? ")
    if new_sin == 'да':
        print("Введите новый синоним:")
        return new(word)
    else:
        return

def new(word):
    x = input("Введите новый синоним ")
    newwords = word.title() + " - " + x + "\n"
    file.write(newwords) #запись нового синонима в конец файла
    return
synonyms()
