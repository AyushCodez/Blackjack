from Classes import Player, Hand

print('Welcome to blackjack!')
y = input('Are you ready(y or n): ')

while y.upper() != 'Y':
    y = input('Are you ready(y or n): ')
money = 0
while money <= 0:
    try:
        money = int(input('How much do you want your balance to be? '))
    except ValueError:
        print('Enter valid amount')
        continue
    if money <= 0:
        print('Enter valid amount')
player1 = Player(money)

while y.upper() == 'Y':
    bet_money = player1.balance + 1
    count = 0
    while bet_money > player1.balance or bet_money <= 0:
        count += 1
        try:
            bet_money = int(input(f'How much do you want to bet? (your current balance is {player1.balance}) '))
        except ValueError:
            print('Enter integer')
        else:
            if count > 1:
                print('Please enter valid amount')
    player1.bet(bet_money)
    print()
    player1_hand = Hand()
    sum_player = player1_hand.process_sum()
    player1_hand.print1()
    print(f'sum={sum_player}')
    dealer_hand = Hand()
    dealer_hand.print1_dealer()
    while True:
        sum_player = player1_hand.process_sum()

        if sum_player < 21:
            play = input('Do you want to hit(h) or stay(s)? ').lower()

            if play == 'h':
                print()
                player1_hand.hit()
                sum_player = player1_hand.process_sum()
                player1_hand.print1()
                print(f'sum={sum_player}')
                dealer_hand.print1_dealer()

            elif play == 's':
                print()
                player1_hand.print1()
                print(f'sum={sum_player}')
                dealer_hand.print_whole()
                print(f'sum={dealer_hand.process_sum()}')
                break
            else:
                print('Enter valid option')
                continue

        if sum_player == 21:
            print('\nHooray! You won!')
            player1.winning(bet_money * 2)
            print('your current bank balance =', player1.balance)
            break

        if sum_player > 21:
            print('\nSorry! You lose!')
            print('your current bank balance=', player1.balance)
            break

    if sum_player < 21:
        sum_dealer = dealer_hand.process_sum()

        while sum_dealer < 21 and sum_dealer <= sum_player:
            dealer_hand.hit()
            sum_dealer = dealer_hand.process_sum()
            print('Dealer hits')
            player1_hand.print1()
            print(f'sum={sum_player}')
            dealer_hand.print_whole()
            print(f'sum={sum_dealer}')
            print('')

        if 21 >= sum_dealer > sum_player:
            print('Sorry! You lost!')
            print('your current bank balance=', player1.balance)

        else:
            print('Hooray! You won!')
            player1.winning(bet_money * 2)
            print('your current bank balance=', player1.balance)

    if player1.balance == 0:
        print('You went bankrupt!!\nGame Over')
        break
    y = input('Do you want to play again?(y or n) ')
