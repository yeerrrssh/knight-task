# Задача "Про шахматного коня"
Задача, которую решает данный модуль:
Определение количества ходов, необходимых шахмотному коню, чтобы добраться из одной клетки в другую и определение минимального количества ходов, за которые могут встретиться два коня, расположенных на двух разных клетках.
# Использование 
## Ввод позиций
В файле main.py, в корневой папке проекта, вы можете указать две клетки. В первой расположен конь из первой задачи в начале своего пути, эта же клетка будет начальной позицией первого коня из второй задачи. Вторая клетка будет являться финишем для коня из первой задачи и начальной позицией коня из второй задачи.

___Учтите, что шахматная доска имеет размеры 8х8___

Строки для введения позиций, описанных выше:

![Здесь должен быть скрин](Снимок.PNG)

## Выбор задачи
Как только вы запустите программу, вам будет предложено ввести цифру от 1 до 3 (13 строка файла main.py):

'''
move = input('Введите номер желаемого действия (1 - от коня до клетки, 2 - встреча двух коней, 3 - обе задачи): ')
'''

При введении 1 - выведется минимальное количество ходов, за которое конь перейдет из одной клетки в другую;

При введении 2 - выведется минимальное количество ходов за которое два коня встретятся;

При введении 3 - выведется оба значения.
