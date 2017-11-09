

def get_card(used_card):
    temp = randint(52)
    while temp in used_card:
        temp = randint(52)
    return temp

def score(PC_card, cards):
    card_sum = 0
    Acount = 0
    for card in PC_card:
        if type(cards[card]) == type(0):
            card_sum += cards[card]
        elif cards[card] != 'A':
            card_sum += 10
        else:
            Acount += 1
    
    if Acount == 0:
        return [card_sum]
    
    score_list = []
    for sr in range(1,10*Acount+2,10):
        score_list.append(sr+card_sum)
    return score_list

card = (["A"]+list(range(2,11))+list("JQK"))*4
while True:
    used = []
    computer = []
    player = []
    print("遊戲開始~\n現在發下各自的兩張牌~覆蓋的那張不能看")
    for i in range(2):
        used.append(get_card(used))
        computer.append(used[-1])
        used.append(get_card(used))
        player.append(used[-1])
    print("player  : ?, {}".format(card[player[1]]))
    print("computer: ?, -")
    Padd = True
    Cadd = True
    win = 0
    for i in range(1,4):
        print("第{}輪：".format(i))
        choice = '0'
        if Padd:
            while choice[0].upper()!='Y' and choice[0].upper()!='N':
                print("請問玩家是否加牌?(Y/N)")
                choice = input(":")
            if choice[0].upper()=='Y':
                print("玩家選擇加牌")
                used.append(get_card(used))
                player.append(used[-1])
            else:
                print("玩家不再加牌")
                Padd = False
        if Cadd:
            if min(score(computer[1:],card))<=10:
                print("電腦選擇加牌")
                used.append(get_card(used))
                computer.append(used[-1])
            else:
                print("電腦不再加牌")
                Cadd = False
        if Padd or Cadd:
            print("目前狀況：")
            print("player  : ?",end="")
            for j in player[1:]:
                print(",",card[j],end="")
            print("")
            print("computer: ?",end="")
            for j in computer[1:]:
                print(", -",end="")
            print("")
            
            if min(score(computer[1:],card))>21 and min(score(player[1:],card))>21:
                win = 3
                print("雙方手牌皆炸，和局")
                break
            elif min(score(computer[1:],card))>21:
                win = 1
                print("由於電腦的手牌已炸，玩家獲勝!!")
                break
            elif min(score(player[1:],card))>21:
                win = 2
                print("由於玩家的手牌已炸，電腦獲勝!!")
                break
        else:
            break
    if win == 0:
        print("\n=============================")
        print("加牌結束公布結果：")
        print("player  :",end="")
        for j in player:
            print(" ",card[j],end="")
        print("")
        print("computer:",end="")
        for j in computer:
            print(" ",card[j],end="")
        print("")        
    if min(score(computer,card))>21 and min(score(player,card))>21:
        print("雙方分數皆炸，和局")
    elif min(score(computer,card))>21:
        print("由於電腦的分數已炸，玩家獲勝!!")
    elif min(score(player,card))>21:
        print("由於玩家的分數已炸，電腦獲勝!!")  
    else:
        ps = max(filter(lambda x: x if x<=21 else None,score(player,card)))
        cs = max(filter(lambda x: x if x<=21 else None,score(computer,card)))
        print("玩家分數：{}\n電腦分數：{}".format(ps,cs))
        if ps==cs:
            print("和局")
        elif ps>cs:
            print("玩家獲勝")
        else:
            print("電腦獲勝")
    choice = '0'
    while choice[0].upper()!='Y' and choice[0].upper()!='N':
        print("是否繼續遊戲?(Y/N)")
        choice = input(":")
    if choice[0].upper()=='N':
        break
    print("\n=============================\n\n\n")