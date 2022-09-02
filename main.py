import os
import sys
from terminal import *

pin = input('pin: ')
num = input('card number: ')
st1 = Terminal(pin,num)
if st1._num == None or st1.check_pin() == None:
     os.execv(sys.executable, [sys.executable] + sys.argv)
re = input('Что вы хотите сделать(1 - положить денег, 2 - вывести деньги, 3 - проверить деньги, end - завершить): ')

while re.lower() != 'end':
    if re == '1':
        put_pin = input('pin: ')
        put_mon = input('money: ')
        st1.put(put_pin, put_mon)
    elif re == '2':
        get_pin = input('pin: ')
        get_mon = input('money(10,100,200,5000): ')
        st1.get_money(get_pin, get_mon)
    elif re == '3':
        _pin = input('pin: ')
        st1.listing(_pin)
    else:
        print()

    re = input('Что вы хотите сделать(1 - положить денег, 2 - вывести деньги, 3 - проверить деньги, end - завершить): ')