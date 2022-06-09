def inputData(): #считавание данных из файда
    with open('input.txt', 'r', encoding = 'utf8') as file:
        p = list(file.readline().strip())
        t = list(file.readline().strip())
    return p, t

def checkLine(p, t): # количество вхождение подстроки в строку
    result = []
    for i in range(len(t)-len(p)+1): #цикл по основной строке (T)
        ok = True
        for j in range(len(p)): #цикл по искомой строке
            if t[i+j] != p[j]:
                ok = False
                break
        if ok:  #если три буквы искомой строки совпали с основной строкой подряд
            result.append(i+1) #запись результат
    return result

def writeData(result):
    count = len(result)
    with open('output.txt', 'w', encoding = 'utf8') as file:
        file.write(str(count) + '\n'+' '.join(map(str,result)))
    return

def main():
    p, t = inputData()
    result = checkLine(p, t)
    writeData(result)
    return

if __name__ == '__main__':
    main()