import random

# center_card_val = ""

print(50*'-') 
print(20*'*', "Game Started",20*"*")
print(50*'-')
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
    for picture_card in ['J','K','Q']:
        deck_data.append({"color":color, "shape":shape, "card":picture_card})
 
black_data = list(filter(lambda each: each["color"]=="black", deck_data))
red_data = list(filter(lambda each: each["color"] == "red" , deck_data))

player_1 = []
player_2 = []
player_3 = []


list_range = []
for i in range(0,52):
    list_range.append(i)

random_cards = random.sample(list_range,52)

print(20*'*',"Total Cards in deck are  :",len(deck_data),20*'*')
print(50*'-') 
print(20*'-',"Cards Are Now Distributing",20*'-')

player1_list = [random_cards[0],random_cards[1],random_cards[2],random_cards[3],random_cards[4]]
player2_list = [random_cards[5],random_cards[6],random_cards[7],random_cards[8],random_cards[9]]
player3_list = [random_cards[10],random_cards[11],random_cards[12],random_cards[13],random_cards[14]]
center_card_list = [random_cards[15]]

player1_cards = []

for numb1 in player1_list:
    player1_cards.append(deck_data[numb1])
      
print(50*'-') 
print("**************  Player 1 cards ***************")
print(50*'-') 

for each_card_1 in player1_cards:
    print(" {} {} of {} ".format(each_card_1['color'],each_card_1['shape'],each_card_1["card"]))


player2_cards = []

for numb2 in player2_list:
    player2_cards.append(deck_data[numb2])
    
print(50*'-') 
print("**************  Player 2 cards ***************")
print(50*'-') 

for each_card_2 in player2_cards:
    print(" {} {} of {} ".format(each_card_2['color'],each_card_2['shape'],each_card_2["card"]))

player3_cards = []

for numb3 in player3_list:
    player3_cards.append(deck_data[numb3])
   
print(50*'-') 
print("**************  Player 3 cards ***************")
print(50*'-') 

for each_card_3 in player3_cards:
    print(" {} {} of {} ".format(each_card_3['color'],each_card_3['shape'],each_card_3["card"]))



combine_list = player1_cards + player2_cards + player3_cards


deck_after_distribution = []
num_ = 0


card_in_center = []
for centr_card in center_card_list:
    card_in_center.append(deck_data[centr_card])

for each_center_card in card_in_center:
    center_card_val = " {} {} of {} ".format(each_center_card['color'],each_center_card['shape'],each_center_card["card"])

    print(10*'-',"Card in center :" ,center_card_val)




#     if deck_data[num_] not in combine_list and deck_data[num_] not in card_in_center:
        
#         deck_after_distribution.append(deck_data[num_])
        
#         num_ += 1
#     else :
        
#         num_ += 1
        
# # print(50*'-') 
# # print(50*'-') 
# print(20*'*' ,"After distribution number of cards are :",len(deck_after_distribution),20*'*')
# # print(50*'-') 
# # # print(50*'-') 
# pop_num = 0
# while len(player1_cards) >= 1 :

# # randn = random.randint(16,36)

# # for each_center_card in card_in_center:
# #     print("center card" , each_center_card['shape'])

#     for each_card_1 in player1_cards:
#         print(" {} {} of {} ".format(each_card_1['color'],each_card_1['shape'],each_card_1["card"]))


#         # print("player 1 card" ,each_card_1['shape'],"and",each_card_1['card'])
#     for each_card_1 in player1_cards:
#         randn = random.randint(16,36)

#         print(each_card_1['shape'],each_card_1['card'])
#         if each_card_1['shape'] == card_in_center[-1]['shape'] or each_card_1['card'] == card_in_center[-1]['card'] :
            
#             print(pop_num)
#             append_num = player1_cards.pop(pop_num)
#             print("apend number ============================================",append_num)
#             # player1_cards.pop(pop_num)
#             card_in_center.append(append_num)
#             print("length of player 1 cards after pop",len(player1_cards))

#             print("yes")


#         else :
#             print("no")
#             # print(random_cards)
#             check = 0
#             while check != 1:
#                 randn = random.randint(16,36)
#                 print( "rnad ", randn)
#                 print(deck_data[random_cards[randn]])
#                 if deck_data[random_cards[randn]] not in player1_cards :
#                     player1_cards.append(deck_data[random_cards[15 + randn]])
#                     print("____")
#                     check = 1
                

                
#             print("length of player 1 cards",len(player1_cards))
