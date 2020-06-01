from IPython.display import clear_output
from Classes import Player, Hand

want = 'Y'
print('Welcome to blackjack!')
y = input('Are you ready(Y or N): ')

while y != 'Y':
    y = input('Are you ready(Yes or No): ')
money = int(input('How much do you want your balance to be? '))
player1 = Player(money)

while want == 'Y':
    bet_money = player1.balance + 1
    count = 1
    while bet_money > player1.balance or bet_money <= 0:
        if count > 1:
            print('Please enter valid amount')
        count += 1
        bet_money = int(input(f'How much do you want to bet? (your current balance is {player1.balance}) '))
    player1.bet(bet_money)
    clear_output()
    print()
    player1_hand = Hand()
    sum_player = player1_hand.process_sum()
    player1_hand.print1()
    print(f'\nsum={sum_player}')
    dealer_hand = Hand()
    dealer_hand.print1_dealer()
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
                dealer_hand.print1_dealer()
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
            print('Dealer hits')
            player1_hand.print1()
            print(f'\nsum={sum_player}')
            dealer_hand.print_whole()
            print(f'\nsum={sum_dealer}')
            print('')

        if 21 >= sum_dealer > sum_player:
            print('Sorry! You lost!')
            print('your current bank balance=', player1.balance)

        else:
            print('Hooray! You won!')
            player1.winning(bet_money * 2)
            print('your current bank balance=', player1.balance)

    want = input('Do you want to play again?(Y or N) ')
    clear_output()
