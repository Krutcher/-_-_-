import os
import random

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4

def deal(deck):
    hand = []
    for i in range(2):
	    random.shuffle(deck)
	    card = deck.pop()
	    if card == 11:card = "J"
	    if card == 12:card = "Q"
	    if card == 13:card = "K"
	    if card == 14:card = "A"
	    hand.append(card)
    return hand

def play_again():
    again = input("Хотите сыграть ещё одну игру? (Д/Н) : ").lower()
    if again == "д":
	    dealer_hand = []
	    player_hand = []
	    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
	    game()
    else:
	    print("Пока!")
	    exit()

def total(hand):
    total = 0
    for card in hand:
	    if card == "J" or card == "Q" or card == "K":
	        total+= 10
	    elif card == "A":
	        if total >= 11: total+= 1
	        else: total+= 11
	    else: total += card
    return total

def hit(hand):
	card = deck.pop()
	if card == 11:card = "J"
	if card == 12:card = "Q"
	if card == 13:card = "K"
	if card == 14:card = "A"
	hand.append(card)
	return hand

def clear():
	if os.name == 'nt':
		os.system('CLS')
	if os.name == 'posix':
		os.system('clear')

def print_results(dealer_hand, player_hand):
	clear()
	print ("У дилера " + str(dealer_hand) + " в итоге " + str(total(dealer_hand)))
	print ("У тебя " + str(player_hand) + " в итоге " + str(total(player_hand)))

def blackjack(dealer_hand, player_hand):
	if total(player_hand) == 21:
		print_results(dealer_hand, player_hand)
		print ("Поздравляю! У вас Blackjack!\n")
		play_again()
	elif total(dealer_hand) == 21:
		print_results(dealer_hand, player_hand)		
		print ("Простите, вы проиграли. У дилера  Blackjack.\n")
		play_again()

def score(dealer_hand, player_hand):
	if total(player_hand) == 21:
		print_results(dealer_hand, player_hand)
		print ("Поздравляю! У вас Blackjack!\n")
	elif total(dealer_hand) == 21:
		print_results(dealer_hand, player_hand)		
		print ("Простите, вы проиграли. У дилера  Blackjack.\n")
	elif total(player_hand) > 21:
		print_results(dealer_hand, player_hand)
		print ("Прости. Ты попался и проиграл.\n")
	elif total(dealer_hand) > 21:
		print_results(dealer_hand, player_hand)			   
		print ("Дилер попался. Ты победил!\n")
	elif total(player_hand) < total(dealer_hand):
		print_results(dealer_hand, player_hand)
        #print ("Sorry. Your score isn't higher than the dealer. You lose.\n")
	elif total(player_hand) > total(dealer_hand):
		print_results(dealer_hand, player_hand)			   
		print ("Поздравляю! Твой счёт выше, чем у дилера. Ты победил\n")		

def game():
	choice = 0
	clear()
	print ("Добро пожаловать в игру Blackjack! !\n")
	dealer_hand = deal(deck)
	player_hand = deal(deck)
	while choice != "q":
		print ("Дилер показывает " + str(dealer_hand[0]))
		print ("У тебя " + str(player_hand) + " в итоге " + str(total(player_hand)))
		blackjack(dealer_hand, player_hand)
		choice = input("Вы хотите [П]однять или [У]йти: ").lower()
		clear()
		if choice == "п":
			hit(player_hand)
			while total(dealer_hand) < 17:
				hit(dealer_hand)
			score(dealer_hand, player_hand)
			play_again()
		elif choice == "у":
			print ("Пока!")
			exit()
	
if __name__ == "__main__":
    game()
