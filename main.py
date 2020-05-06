import random
from IPython.display import clear_output


def blackjack():
    class players_hand():

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
                if num > 1 and num < 10:
                    pass
                elif num > 9:
                    num = 10
                else:
                    num = 11
                self.myhand.append(num)

            self.cardwords = []
            for card in self.mycards:
                x = random.randint(1, 4)
                if x == 1:
                    cardtype = ' of diamonds'
                if x == 2:
                    cardtype = ' of clubs'
                if x == 3:
                    cardtype = ' of hearts'
                if x == 4:
                    cardtype = ' of spades'

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
            print('Your cards are ', end='')
            for card in self.cardwords:
                print(', ', end='')
                print(card, end='')

            print('\nSum=', self.process_sum())
        def hit(self):
            import random
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
            if num > 1 and num < 10:
                pass
            elif num > 9:
                num = 10
            else:
                num = 11
            self.myhand.append(num)
            x = random.randint(1, 4)
            if x == 1:
                cardtype = ' of diamonds'
            if x == 2:
                cardtype = ' of clubs'
            if x == 3:
                cardtype = ' of hearts'
            if x == 4:
                cardtype = ' of spades'

            mycard = num
            if mycard == 11:
                mycard = 'jack'

            elif mycard == 1:
                mycard = 'ace'

            elif mycard == 12:
                mycard = 'queen'

            elif mycard == 13:
                mycard = 'king'
            self.cardwords.append(str(mycard) + cardtype)

        def print1(self):
            print('Players cards are', end='')
            for card in self.cardwords:
                print(', ', end= '')
                print(card, end='')

    class dealers_hand(players_hand):

        def __init__(self):
            import random
            x = random.randint(1, 13)
            y = random.randint(1, 13)
            self.mycards = [x, y]
            self.myhand = []
            for num in self.mycards:
                if num > 1 and num < 10:
                    pass
                elif num > 9:
                    num = 10
                else:
                    num = 11
                self.myhand.append(num)

            self.cardwords = []
            for card in self.mycards:
                x = random.randint(1, 4)
                if x == 1:
                    cardtype = ' of diamonds'
                if x == 2:
                    cardtype = ' of clubs'
                if x == 3:
                    cardtype = ' of hearts'
                if x == 4:
                    cardtype = ' of spades'

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
            print('The dealers cards are', self.cardwords[0]+', hidden card')

        def print1(self):
            print('The dealers cards are ', self.cardwords[0], ', hidden card')

        def print_whole(self):
            print('Dealers cards are', end='')
            for card in self.cardwords:
                print(', ', end='')
                print(card, end='')

    class Player():

        def __init__(self, player_name, balance):
            self.player_name = player_name
            self.balance = balance

        def bet(self, bet_money):
            self.bet_money = bet_money
            self.balance -= self.bet_money

        def winning(self, winnings):
            self.winnings = winnings
            self.balance += self.winnings

    want = 'Y'
    print('Welcome to blackjack!')
    y = input('Are you ready(Y or N): ')

    while y == 'N':
        y = input('Are you ready(Yes or No): ')
    player_name = input('What is your name? ')
    money = int(input('how much do you want your balance to be? '))
    player1 = Player(player_name, money)

    while want == 'Y':
        bet_money = player1.balance + 1
        while bet_money > player1.balance or bet_money <= 0:
            bet_money = int(input(f'How much do you want to bet? (your current balance is {player1.balance}) '))
        player1.bet(bet_money)
        clear_output()
        print()
        player1_hand = players_hand()
        dealer_hand = dealers_hand()
        print()
        while True:
            sum_player = player1_hand.process_sum()

            if sum_player < 21:
                play = input('What do you want to do?(hit or stay) ')

                if play == 'hit':
                    player1_hand.hit()
                    sum_player = player1_hand.process_sum()
                    player1_hand.print1()
                    print(f'\nsum={sum_player}')
                    dealer_hand.print1()
                    print('')

                else:
                    player1_hand.print1()
                    print(f'\nsum={sum_player}')
                    dealer_hand.print_whole()
                    print(f'\nsum={dealer_hand.process_sum()}')
                    print('')
                    break

            if sum_player == 21:
                print('Hooray! You won!')
                player1.winning(bet_money * 2)
                print('your current bank balance=', player1.balance)
                break

            if sum_player > 21:
                print('Sorry! You lose!')
                print('your current bank balance=', player1.balance)
                break

        if sum_player < 21:
            sum_dealer = dealer_hand.process_sum()

            while sum_dealer < 21 and sum_dealer <= sum_player:
                dealer_hand.hit()
                sum_dealer = dealer_hand.process_sum()
                player1_hand.print1()
                print(f'\nsum={sum_player}')
                dealer_hand.print_whole()
                print(f'\nsum={sum_dealer}')
                print('')

            if sum_dealer > sum_player and sum_dealer <= 21:
                print('Sorry! You lost!')
                print('your current bank balance=', player1.balance)

            else:
                print('Hooray! You won!')
                player1.winning(bet_money * 2)
                print('your current bank balance=', player1.balance)
                player1.winning(bet_money * 2)

        want = input('do you want to play again?(Y or N)')
        clear_output()


blackjack()
