import random


class Hand:

    def process_sum(self):
        while True:
            self.sum = 0
            for x in self.hand:
                self.sum += x
            if self.sum <= 21:
                break
            else:
                if 11 in self.hand:
                    num = self.hand.index(11)
                    self.hand.remove(11)
                    self.hand.insert(num, 1)
                else:
                    break
        return self.sum

    def __init__(self):
        x = random.randint(1, 13)
        y = random.randint(1, 13)
        self.cards = [x, y]
        self.hand = []
        for num in self.cards:
            if 1 <= num < 10:
                pass
            elif num > 9:
                num = 10
            else:
                num = 11
            self.hand.append(num)

        self.card_words = []
        for card in self.cards:
            card = (['ace'] + list(range(2, 11)) + ['jack', 'queen', 'king'])[card - 1]
            types = [" of diamonds", " of spades", " of clubs", " of hearts"]
            while True:

                card_type = random.choice(types)

                if str(card) + card_type not in self.card_words:
                    break

            self.card_words.append(str(card) + card_type)

    def hit(self):
        num = random.randint(1, 13)
        while True:
            count = self.cards.count(num)
            if count >= 4:
                num = random.randint(1, 13)
            else:
                break
        self.cards.append(num)
        if 1 <= num <= 10:
            pass
        elif num > 9:
            num = 10
        else:
            num = 11
        self.hand.append(num)

        card = (['ace'] + list(range(2, 11)) + ['jack', 'queen', 'king'])[num - 1]

        types = [" of diamonds", " of spades", " of clubs", " of hearts"]
        while True:

            card_type = random.choice(types)

            if str(card) + card_type not in self.card_words:
                break

        self.card_words.append(str(card) + card_type)

    def print1(self):
        print('Players cards are ' + ', '.join(self.card_words))

    def print1_dealer(self):
        print('The dealers cards are ' + self.card_words[0] + ', hidden card')

    def print_whole(self):
        print('Dealers cards are ' + ', '.join(self.card_words))


class Player:

    def __init__(self, balance: int):
        self.balance = balance

    def bet(self, bet_money: int):
        self.bet_money = bet_money
        self.balance -= self.bet_money

    def winning(self, winnings: int):
        self.winnings = winnings
        self.balance += self.winnings
