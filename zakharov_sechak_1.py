import os
import datetime
name = input('Введите имя файла:')
name +='.txt'
while not os.path.exists(name):
     name = input('Файла с таким именем не существует, введите другое имя:')
     name = name+'.txt'
if os.path.isfile(name):
        print('Файл найден')
        print('Размер: ~',os.path.getsize(name)//1024,'Кб')
        print('Дата создания:',\
              datetime.datetime.fromtimestamp(int(os.path.getctime(name))))
        print('Дата последнего открытия:',\
              datetime.datetime.fromtimestamp(int(os.path.getatime(name))))
        print('Дата последнего изменения:',\
              datetime.datetime.fromtimestamp(int(os.path.getmtime(name))))
f = open(name, "r");
f_new = open("out.txt", "w");
arr = f.readlines();
n = len(arr);
sep = "+" + 9*"-" + "+" + 9*"-" + "+" + 9*"-" + "+";
print(sep);
f_new.write(sep + "\n");
print("|  Число  | Квадрат |   Куб   |");
print(sep);
f_new.write("| Число | Квадрат | Куб    |"+ "\n");
for i in range (n):
     try:
       arr[i] = float(arr[i]);
       s = "|{0:9.3f}|{1:9.3f}|{2:9.3f}|".format(arr[i], arr[i]**2, arr[i]**3);
       print(s);
       f_new.write(sep + "\n");
       f_new.write(s + "\n");
     except ValueError:
        l = len(arr[i]);
        s = "|{0:>9}|".format(arr[i].replace('\n', '')) + "Не число |Не число |";
        print(s);
        f_new.write(sep + "\n");
        f_new.write(s + "\n");
     print(sep);
f_new.write(sep + "\n");
f.close();
f_new.close();
print('Таблицу так же можно посмотреть в файле "out.txt"');
a = input("Нажмите F13 для выхода");
