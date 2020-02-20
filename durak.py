import random

class Durak:
    def __init__(self, N):
        self.order_num = N
        self.order_cards_player_1_kozyr = []
        self.order_cards_player_2_kozyr = []

    def all_cards(self):
        self.deck = [(6, '♥'), (7, '♥'), (8, '♥'), (9, '♥'), (10, '♥'), (11, '♥'), (12, '♥'), (13, '♥'), (14, '♥'),
                     (6, '♦'), (7, '♦'), (8, '♦'), (9, '♦'), (10, '♦'), (11, '♦'), (12, '♦'), (13, '♦'), (14, '♦'),
                     (6, '♣'), (7, '♣'), (8, '♣'), (9, '♣'), (10, '♣'), (11, '♣'), (12, '♣'), (13, '♣'), (14, '♣'),
                     (6, '♠'), (7, '♠'), (8, '♠'), (9, '♠'), (10, '♠'), (11, '♠'), (12, '♠'), (13, '♠'), (14, '♠')]

        hand_player_1 = []
        hand_player_2 = []
        for i in range(6):
            player_1_card = random.choice(self.deck)
            hand_player_1.append(player_1_card)
            self.deck.remove(player_1_card)
            player_2_card = random.choice(self.deck)
            hand_player_2.append(player_2_card)
            self.deck.remove(player_2_card)
        self.player_1_cards = hand_player_1
        self.player_2_cards = hand_player_2
        self.player_1_cards.sort()
        self.player_2_cards.sort()
        kozyr_card = random.choice(self.deck)
        self.kozyr = kozyr_card[1]
        random.shuffle(self.deck)
        self.list_bito = []
        print('карты 1-го игрока:', len(self.player_1_cards), self.player_1_cards)
        print('карты 2-го игрока:', len(self.player_2_cards), self.player_2_cards)
        print('карт в колоде:', len(self.deck))
        print('козырь:', self.kozyr)

    def bito(self, x, y):
        self.list_bito.append(x)
        self.list_bito.append(y)
        self.list_bito.sort()

    def dobor(self):
        if len(self.deck) > 0 and len(self.player_1_cards) < 6:
            self.next_card = self.deck[0]
            self.deck.remove(self.next_card)
            self.player_1_cards.append(self.next_card)
            print('первый игрок взял карту из колоды {}, в колоде {} карт'.format(self.next_card, len(self.deck)))
        if len(self.deck) > 0 and len(self.player_2_cards) < 6:
            self.next_card = self.deck[0]
            self.deck.remove(self.next_card)
            self.player_2_cards.append(self.next_card)
            print('второй игрок взял карту из колоды {}, в колоде {} карт'.format(self.next_card, len(self.deck)))
        self.player_1_cards.sort()
        self.player_2_cards.sort()
        self.order_cards_player_1_not_kozyr = [x for x in self.player_1_cards if x[1]!=self.kozyr]
        self.order_cards_player_1_not_kozyr.sort()
        self.order_cards_player_1_kozyr = [x for x in self.player_1_cards if x[1]==self.kozyr]
        self.order_cards_player_1_kozyr.sort()
        self.order_cards_player_2_not_kozyr = [x for x in self.player_2_cards if x[1]!=self.kozyr]
        self.order_cards_player_2_not_kozyr.sort()
        self.order_cards_player_2_kozyr = [x for x in self.player_2_cards if x[1]==self.kozyr]
        self.order_cards_player_2_kozyr.sort()

    def order_cards(self):
        w = 0
        for i in range(1, self.order_num):
            if w==0:
                self.dobor()
                if len(self.order_cards_player_1_not_kozyr) > 0:
                    order_cards_player_1 = self.order_cards_player_1_not_kozyr[0]
                else:
                    order_cards_player_1 = self.order_cards_player_1_kozyr[0]
                order_cards_player_1_suit = order_cards_player_1[1]
                order_cards_player_1_digit = order_cards_player_1[0]
                print('ход первого игрока:', order_cards_player_1)
                hand_player_2_suit = [x for x in self.player_2_cards if x[1]==order_cards_player_1_suit]
                hand_player_2_suit_higher = [x for x in hand_player_2_suit if x[0] > order_cards_player_1_digit]
                if len(hand_player_2_suit_higher) + len(self.order_cards_player_2_kozyr)==0:
                    self.player_2_cards.append(order_cards_player_1)
                    print('второй игрок взял')
                    self.player_1_cards.remove(order_cards_player_1)
                    self.dobor()
                    w = 0
                elif order_cards_player_1_suit==self.kozyr and order_cards_player_1[0] > \
                        self.order_cards_player_2_kozyr[-1][0]:
                    self.player_2_cards.append(order_cards_player_1)
                    print('второй игрок взял')
                    self.player_1_cards.remove(order_cards_player_1)
                    self.dobor()
                    w = 0
                elif order_cards_player_1_suit==self.kozyr and order_cards_player_1[0] < \
                        self.order_cards_player_2_kozyr[-1][0]:
                    self.m = 3
                    if self.m <= (len(self.order_cards_player_2_kozyr) - 1):
                         order_cards_player_2 = self.order_cards_player_2_kozyr[self.m]
                    print('ход второго игрока:', order_cards_player_2)
                    self.bito(order_cards_player_1, order_cards_player_2)
                    print('бито')
                    self.dobor()
                    w = 1
                elif len(hand_player_2_suit_higher)==0 and len(self.order_cards_player_2_kozyr) > 0:
                    print('ход второго игрока:', self.order_cards_player_2_kozyr[0])
                    order_cards_player_2 = self.order_cards_player_2_kozyr[0]
                    self.player_1_cards.remove(order_cards_player_1)
                    self.player_2_cards.remove(order_cards_player_2)
                    self.bito(order_cards_player_1, order_cards_player_2)
                    print('бито')
                    self.dobor()
                    w = 1
                else:
                    print('ход второго игрока:', hand_player_2_suit_higher[0])
                    order_cards_player_2 = hand_player_2_suit_higher[0]
                    self.player_1_cards.remove(order_cards_player_1)
                    self.player_2_cards.remove(order_cards_player_2)
                    self.bito(order_cards_player_1, order_cards_player_2)
                    print('бито')
                    self.dobor()
                    w = 1
                print('карты 1-го игрока после {} хода:'.format(i), len(self.player_1_cards), self.player_1_cards)
                print('карты 2-го игрока после {} хода:'.format(i), len(self.player_2_cards), self.player_2_cards)
            if w==1:
                self.dobor()
                if len(self.order_cards_player_2_not_kozyr) > 0:
                    order_cards_player_2 = self.order_cards_player_2_not_kozyr[0]
                else:
                    order_cards_player_2 = self.order_cards_player_2_kozyr[0]
                order_cards_player_2_suit = order_cards_player_2[1]
                order_cards_player_2_digit = order_cards_player_2[0]
                print('ход второго игрока:', order_cards_player_2)
                hand_player_1_suit = [x for x in self.player_1_cards if x[1]==order_cards_player_2_suit]
                hand_player_1_suit_higher = [x for x in hand_player_1_suit if x[0] > order_cards_player_2_digit]
                if len(hand_player_1_suit_higher) + len(self.order_cards_player_1_kozyr)==0:
                    self.player_1_cards.append(order_cards_player_2)
                    self.player_2_cards.remove(order_cards_player_2)
                    print('первый игрок взял')
                    self.dobor()
                    w = 1
                elif order_cards_player_2_suit==self.kozyr and order_cards_player_2[0] > \
                        self.order_cards_player_1_kozyr[-1][0]:
                    self.player_1_cards.append(order_cards_player_2)
                    self.player_2_cards.remove(order_cards_player_2)
                    print('первый игрок взял')
                    self.dobor()
                    w = 1
                elif order_cards_player_2_suit==self.kozyr and order_cards_player_2[0] < \
                        self.order_cards_player_1_kozyr[-1][0]:
                    print('ход первого игрока:', self.order_cards_player_1_kozyr[-1])
                    order_cards_player_1 = self.order_cards_player_1_kozyr[-1]
                    self.player_1_cards.remove(order_cards_player_1)
                    self.player_2_cards.remove(order_cards_player_2)
                    self.bito(order_cards_player_1, order_cards_player_2)
                    print('бито')
                    self.dobor()
                    w = 0
                elif len(hand_player_1_suit_higher)==0 and len(self.order_cards_player_1_kozyr) > 0:
                    print('ход первого игрока:', self.order_cards_player_1_kozyr[0])
                    order_cards_player_1 = self.order_cards_player_1_kozyr[0]
                    self.player_1_cards.remove(order_cards_player_1)
                    self.player_2_cards.remove(order_cards_player_2)
                    self.bito(order_cards_player_1, order_cards_player_2)
                    print('бито')
                    self.dobor()
                    w = 0
                else:
                    print('ход первого игрока:', hand_player_1_suit_higher[0])
                    order_cards_player_1 = hand_player_1_suit_higher[0]
                    self.player_1_cards.remove(order_cards_player_1)
                    self.player_2_cards.remove(order_cards_player_2)
                    self.bito(order_cards_player_1, order_cards_player_2)
                    print('бито')
                    self.dobor()
                    w = 0
                print('карты 1-го игрока после {} хода:'.format(i), len(self.player_1_cards), self.player_1_cards)
                print('карты 2-го игрока после {} хода:'.format(i), len(self.player_2_cards), self.player_2_cards)
            if len(self.player_1_cards)==0 and len(self.player_2_cards)==0:
                print('ничья')
                break
            elif len(self.player_1_cards)==0:
                print('1-й игрок победил')
                break
            elif len(self.player_2_cards)==0:
                print('2-й игрок победил')
                break

if __name__=='__main__':
    cards_game = Durak(25)
    cards_game.all_cards()
    cards_game.order_cards()