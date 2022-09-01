class Terminal:
    def __init__(self, pin, num):
        self.pin = self.set_pin(pin)
        self.num = self.set_card_num(num)
        self.money = 0
        
    def set_card_num(self, num):
        try:
            num = int(num)
            if len(str(num).replace('',' ').split(' ')[1:-1]) == 16:
                return num
            else:
                print('card number must contain 16 digits')
        except:
            raise Exception('InvalidValue: card number code must contain only numbers ')

    def set_pin(self, pin):
        try:
            pin = int(pin)
            if len(str(pin).replace('',' ').split(' ')[1:-1]) == 4:
                return pin
            else:
                print('Pin code must contain 4 digits')
        except:
            raise Exception('InvalidValue: pin code must contain only numbers ')
    def put(self, pin, money):
        if self.set_pin(pin) == self.pin:
            try:
                money = int(money)
                self.money += money
            except:
                raise Exception('InvalidValue must be only a digits')
        else:
            print('wrong pin')

    def get_money(self, pin, money):
        if self.set_pin(pin) == self.pin:
            try:
                money = int(money)
                valid = [10,100,200,5000]
                if money in valid:
                    self.money -= money
                else:
                    print('токого нет')
            except:
                raise Exception('InvalidValue must be only a digits')
        else:
            print('неверный пин')
    def listing(self, pin):
        if self.set_pin(pin) == self.pin:
            print('Ваши денги состовляют: ', self.money, 'долларав')
        else:
            print('неверный пин')