import argparse
import random

"""
    解析使用者的姓名，若未從命令列參數提供則提示使用者輸入。

    回傳值:
        str: 使用者的姓名，來自命令列參數或使用者輸入。
"""
def get_user_name()->str:
    parser = argparse.ArgumentParser(description="猜數字遊戲")
    parser.add_argument("-n","--name",type=str,help="姓名")
    parser.add_argument("-f","--frequency",type=int,help="玩的次數",default=1)
    args = parser.parse_args()

    if not args.name:
        name = input("請輸入您的姓名:")
    else:
        name = args.name

    return name


"""
    猜數字遊戲

    此函數實現一個互動式的猜數字遊戲，玩家需要在給定範圍內猜出目標數字。

    參數:
        name (str): 玩家名稱

    功能:
        - 隨機生成1-100之間的目標數字
        - 根據玩家的輸入給出大小提示
        - 統計玩家猜測次數
        - 確保輸入在有效範圍內
        - 顯示遊戲進度和結果

    返回:
        None

    使用方式:
        遊戲會持續進行直到玩家猜中目標數字為止
        每次猜測後會更新可猜測的數字範圍
        系統會顯示當前已猜測次數
"""

def play_game(name:str)->None:

    i = 0
    print(f"========猜數字遊戲第{i+1}次=========\n\n")
    min = 1
    max = 100
    count = 0
    target = random.randint(min,max)
    print(target)
    while(True):
        keyin = int(input(f"猜數字範圍{min}~{max}:"))
        count += 1
        if(keyin>=min and keyin<=max):
            if target == keyin:
                print(f"賓果!猜對了, 答案是:{target}")
                print(f"{name}共猜了{count}次\n")
                break
            elif(keyin > target):
                print(f"猜錯了!再小一點")
                max = keyin - 1
            else:
                print(f"猜錯了!再大一點")
                min = keyin + 1
            print(f"{name}已經猜{count}次\n")
        else:
            print("請輸入提示範圍內的數字\n")

def main():
    """
    主程式進入點

    主程式讓使用者輸入名字並控制遊戲的執行次數。
    透過get_user_name()取得使用者名稱，並呼叫play_game()執行指定次數的遊戲。
    最後顯示遊戲結束訊息及遊玩次數。

    變數說明:
    frequency -- 遊戲執行次數
    name -- 使用者名稱

    備註:
    需要先定義get_user_name()和play_game()函式才能執行
    """
    frequency = 1
    name = get_user_name()
    for i in range(frequency):
        play_game(name)
    print(f"遊戲結束,{name}共玩了{frequency}次")

if __name__ == '__main__':
    main()