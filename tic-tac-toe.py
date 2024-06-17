import re

board = [[" "," "," "],[" "," "," "],[" "," "," "]]
Tries = 0
print("""Play tic-tac-toe
---------------
|   ||   ||   |
---------------
|   ||   ||   |
---------------
|   ||   ||   |
---------------
""")
while Tries<9:
    user_input = input("Enter location in acronym-shape: ").lower()
    if matches:=re.search("(tr|t|tl|m|mr|ml|b|bl|br)-(x|o)",user_input):
        if matches.group(1) == "tl" and board[0][0]==" ":
            board[0][0] = matches.group(2)
        elif matches.group(1) == "t" and board[0][1]==" ":
            board[0][1] = matches.group(2)
        elif matches.group(1) == "tr" and board[0][2]==" ":
            board[0][2] = matches.group(2)
        elif matches.group(1) == "ml" and board[1][0]==" ":
            board[1][0] = matches.group(2)
        elif matches.group(1) == "m" and board[1][1]==" ":
            board[1][1] = matches.group(2)
        elif matches.group(1) == "mr" and board[1][2]==" ":
            board[1][2] = matches.group(2)
        elif matches.group(1) == "bl" and board[2][0]==" ":
            board[2][0] = matches.group(2)
        elif matches.group(1) == "b" and board[2][1]==" ":
            board[2][1] = matches.group(2)
        elif matches.group(1) == "br" and board[2][2]==" ":
            board[2][2] = matches.group(2)
        else:
            print("Oops!, someone is already there.")
            Tries -= 1
        print("---------------")
        for i in range(3):
            for j in range(3):
                print(f"| {board[i][j]}", end=" |")
            print("\n---------------")
        Tries += 1
        #Horizontal
        if (board[0][0]==board[0][1]==board[0][2]=="x") or (board[0][0]==board[0][1]==board[0][2]=="o"):
            print(f"Game Over!!!\nUser '{board[0][0]}' Won")
            break
        elif (board[1][0]==board[1][1]==board[1][2]=="x") or (board[1][0]==board[1][1]==board[1][2]=="o"):
            print(f"Game Over!!!\nUser '{board[1][0]}' Won")
            break
        elif (board[2][0]==board[2][1]==board[2][2]=="x") or (board[2][0]==board[2][1]==board[2][2]=="o"):
            print(f"Game Over!!!\nUser '{board[2][0]}' Won")
            break
        
        #Vertical
        elif (board[0][0]==board[1][0]==board[2][0]=="x") or (board[0][0]==board[1][0]==board[2][0]=="o"):
            print(f"Game Over!!!\nUser '{board[0][0]}' Won")
            break
        elif (board[0][1]==board[1][1]==board[2][1]=="x") or (board[0][1]==board[1][1]==board[2][1]=="o"):
            print(f"Game Over!!!\nUser '{board[0][1]}' Won")
            break
        elif (board[0][2]==board[1][2]==board[2][2]=="x") or (board[0][2]==board[1][2]==board[2][2]=="o"):
            print(f"Game Over!!!\nUser '{board[0][2]}' Won")
            break
        
        #Diagonal
        elif (board[0][0]==board[1][1]==board[2][2]=="x") or (board[0][0]==board[1][1]==board[2][2]=="o"):
            print(f"Game Over!!!\nUser '{board[0][0]}' Won")
            break
        elif (board[0][2]==board[1][1]==board[2][0]=="x") or (board[0][2]==board[1][1]==board[2][0]=="o"):
            print(f"Game Over!!!\nUser '{board[0][2]}' Won")
            break
    else:
        print("""      Type Error!!!
For example, for top right: tr
             for shape: o or x
             Like this: tr-o""")
        break
else:
    print("It's a DRAW!!!")