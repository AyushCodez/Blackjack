import random


class Hand:

    def process_sum(self):
        self.sum = 0
        while True:
            self.sum = 0
            for x in self.myhand:
                self.sum += x
            if self.sum <= 21:
                break
            else:
                if 11 in self.myhand:
                    num = self.myhand.index(11)
                    self.myhand.remove(11)
                    self.myhand.insert(num, 1)
                else:
                    break
        return self.sum

    def __init__(self):
        x = random.randint(1, 13)
        y = random.randint(1, 13)
        self.mycards = [x, y]
        self.myhand = []
        for num in self.mycards:
            if 1 <= num < 10:
                pass
            elif num > 9:
                num = 10
            else:
                num = 11
            self.myhand.append(num)

        self.cardwords = []
        for card in self.mycards:
            types = [" of diamonds", " of spades", " of clubs", " of hearts"]

            cardtype = random.choice(types)

            mycard = card
            if mycard == 11:
                mycard = 'jack'

            elif mycard == 1:
                mycard = 'ace'

            elif mycard == 12:
                mycard = 'queen'

            elif mycard == 13:
                mycard = 'king'
            self.cardwords.append(str(mycard) + cardtype)

    def hit(self):
        num = random.randint(1, 13)
        count = 1
        while True:
            for card in self.mycards:
                if card == num:
                    count += 1
            if count > 4:
                num = random.randint(1, 13)
            else:
                break
        self.mycards.append(num)
        if 1 <= num <= 10:
            pass
        elif num > 9:
            num = 10
        else:
            num = 11
        self.myhand.append(num)

        mycard = num
        if mycard == 11:
            mycard = 'jack'

        elif mycard == 1:
            mycard = 'ace'

        elif mycard == 12:
            mycard = 'queen'

        elif mycard == 13:
            mycard = 'king'

        while True:
            types = [" of diamonds", " of spades", " of clubs", " of hearts"]

            cardtype = random.choice(types)

            if str(mycard) + cardtype not in self.cardwords:
                break

        self.cardwords.append(str(mycard) + cardtype)

    def print1(self):
        print('Players cards are ' + ', '.join(self.cardwords))

    def print1_dealer(self):
        print('The dealers cards are ' + self.cardwords[0] + ', hidden card')

    def print_whole(self):
        print('Dealers cards are ' + ', '.join(self.cardwords))


class Player:

    def __init__(self, balance):
        self.balance = balance

    def bet(self, bet_money):
        self.bet_money = bet_money
        self.balance -= self.bet_money

    def winning(self, winnings):
        self.winnings = winnings
        self.balance += self.winnings
