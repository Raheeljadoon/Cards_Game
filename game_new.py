import random
from random import sample
deck_data = []

shape_dic = {0:"CLUB",1:"SPADE",2:"HEART",3:"DIAMOND"}
color_counter = 0
color = ""
shape = ""
for count in range(1,5):

    if color_counter <= 1:
        shape = shape_dic[color_counter]
        color_counter += 1
        color = "black"
    else:
        shape = shape_dic[color_counter]
        color_counter += 1
        color = "red"
        
    for number_card in range(1,11):
        data = {'color':color, 'shape':shape, 'card':number_card}
        deck_data.append(data)
    for picture_card in ['j','k','q']:
        deck_data.append({"color":color, "shape":shape, "card":picture_card})

deck_data_dic = {}    
for count,each_card in enumerate(deck_data):
    deck_data_dic[count] = each_card

print(deck_data_dic)



number_of_players = 3
number_of_random_card = number_of_players*5
random_card = []

counter = 0
while counter < number_of_random_card:
    rand = random.randint(0,51)
    if rand not in random_card:
        counter +=1
        random_card.append(rand)

print(random_card)
print(len(random_card))

players_card = [random_card[i:i + 5] for i in range(0, len(random_card), 5)] 
print(players_card)
print(players_card[1])


# now remove the random card from deck of card and assign to players

dic = {}
for count ,player in enumerate(players_card):
    
    list_of_card = []
    for card_of_player in player:
        list_of_card.append(deck_data_dic.pop(card_of_player))

    dic["player_{}".format(count+1)] = list_of_card

print(dic)
        
# all cards are assign to the players and remove from the deck

print(len(deck_data_dic))

center_cards = []

print(deck_data_dic.keys())
center_cards.append(deck_data_dic.pop(sample(deck_data_dic.keys(),1)[0]))

print(center_cards[-1])
print(len(deck_data_dic))

# run all the cards of user

endgame = False
while endgame == False:
    for key, value in dic.items():
        
        for index ,each_player_cards in enumerate(value) :
            if center_cards[-1]["shape"] == each_player_cards['shape'] or center_cards[-1]["card"] == each_player_cards['card']:
                print("player :", key)

                center_cards.append(value.pop(index)) 
                print(center_cards)

    for key , value in dic.items():
        if len(value) == 0:
            print("Winnner !! ",key)
            endgame = True
                

# print(center_cards)


