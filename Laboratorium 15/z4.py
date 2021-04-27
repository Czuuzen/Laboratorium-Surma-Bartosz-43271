import random
import sys

class Card:
    suits = ['\u2666', '\u2665', '\u2663', '\u2660']  # ["Trefl", "Karo", "Kier", "Pik"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '%s %s' % (Card.suits[self.suit], Card.ranks[self.rank])
        # return '%s %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])

    def __lt__(self, other):
        t1 = self.rank, self.suit
        t2 = other.rank, other.suit
        return t1 < t2


class Deck:
    def __init__(self):
        """Stworzenie talii."""
        self.cards = []
        for suit in range(4):
            for rank in range(13):
                card = Card(suit, rank)
                self.cards.append(card)
        self.shuffle()

    def __str__(self):
        """Informacja o talii w stringu."""
        res = []
        for card in self.cards:
            res.append(str(card))
        return ', '.join(res)

    def __len__(self):
        """Nadpisanie długości"""
        return len(self.cards)

    def add_card(self, card):
        """Dodanie karty do talli (dla oszukistów)."""
        self.cards.append(card)

    def pop_card(self, i=-1):
        """Usuwa i zwraca kartę z talii."""
        return self.cards.pop(i)

    def shuffle(self):
        """Przetasowanie kart w talii."""
        random.shuffle(self.cards)

    def sort(self):
        """Posortowanie talii."""
        self.cards.sort()

    def wincard(self, cards):
        """Wybór zwycięzcy wedle wagi karty"""
        winner = cards[0]
        for card in cards:
            if winner < card:
                winner = card
        return winner


class Hand(Deck):
    """Wypisanie ręki."""

    def __init__(self, label=''):
        self.cards = []
        self.label = label
        self.wincount = 0

    def getlabel(self):
        """ Zapisa nazwy gracza """
        return self.label

    def roundwinner(self):
        """ Zliczanie wygranych gracza """
        self.wincount += 1

    def getwincount(self):
        """ Całościowy wynik zwycięstw """
        return self.wincount

    def __str__(self):
        return "Ręką dla " + self.label + " jest " + Deck.__str__(self)


def play(argv):
    deck = Deck()
    hands = []
    for i in range(1, 5): # ilość graczy
        player = 'Gracz %d' % i
        if len(argv) > i:
            player = argv[i]
        hands.append(Hand(player))

    while len(deck) > 0:
        for hand in hands:
            hand.add_card(deck.pop_card())

    print("!!! Gra w najwyższą kartę !!!")
    input("Zacznijmy grę, naciśnij jakikolwiek przycisk aby kontynuować : ")

    for i in range(1, 11): # ilość rund
        cards = []
        floors = []
        for hand in hands:
            card = hand.pop_card()
            cards.append(card)
            floors.append(hand.getlabel() + " : " + str(card))

        winner_card = deck.wincard(cards)
        winner_hand = hands[cards.index(winner_card)]
        winner_hand.roundwinner()
        print("Runda", i, "|", ", ".join(floors))
        print("Zwycięzca rundy ", i,": ", winner_hand.getlabel(), ":", winner_card)
        input()

    for hand in hands:
        print("Wynik dla", hand.getlabel(), "to", hand.getwincount())


def main(argv=[]):
    answer = "Y"
    while answer.upper() == "Y":
        play(argv)
        answer = input("Czy chcesz zagrać ponownie (Y/N)? : ")
    print("Żegnam ozięble.")


if __name__ == '__main__':
    main(sys.argv)