import random 

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

    


black_data = list(filter(lambda each: each["color"]=="black", deck_data))
red_data = list(filter(lambda each: each["color"] == "red" , deck_data))



player_1 = []
player_2 = []
player_3 = []




list_range = []
for i in range(0,52):
    list_range.append(i)

random_cards = random.sample(list_range,15)


print("before loop lenghth of deck is :",len(deck_data))


player1_list = [random_cards[0],random_cards[1],random_cards[2],random_cards[3],random_cards[4]]
player2_list = [random_cards[5],random_cards[6],random_cards[7],random_cards[8],random_cards[9]]
player3_list = [random_cards[10],random_cards[11],random_cards[12],random_cards[13],random_cards[14]]


print(player1_list)
print(player2_list)
print(player3_list)


player1_cards = []

for numb1 in player1_list:
    player1_cards.append(deck_data[numb1])
    print(numb1)
    

print("**************  Player 1 cards ***************")
print(player1_cards)



player2_cards = []

for numb2 in player2_list:
    player2_cards.append(deck_data[numb2])
    print(numb2)
   
    
print("**************  Player 2 cards ***************")
print(player2_cards)




player3_cards = []

for numb3 in player3_list:
    player3_cards.append(deck_data[numb3])
    print(numb2)
    
    
print("**************  Player 3 cards ***************")
print(player3_cards)





combine_list = player1_cards + player2_cards + player3_cards
print("combine list is --------------------",combine_list)

deck_after_distribution = []
num_ = 0

while num_ < 51:

    if deck_data[num_] not in combine_list:
        num_ += 1
        
        deck_after_distribution.append(deck_data[num_])
        

    else :
        
        num_ += 1
        

print("after distribution of cards :",len(deck_after_distribution))






