def printBoard(xState,zState):
    zero = 'X' if xState[0] else ('O' if zState[0] else ' ')
    one = 'X' if xState[1] else ('O' if zState[1] else ' ')
    two = 'X' if xState[2] else ('O' if zState[2] else ' ')
    three = 'X' if xState[3] else ('O' if zState[3] else ' ')
    four = 'X' if xState[4] else ('O' if zState[4] else ' ')
    five = 'X' if xState[5] else ('O' if zState[5] else ' ')
    six = 'X' if xState[6] else ('O' if zState[6] else ' ')
    seven = 'X' if xState[7] else ('O' if zState[7] else ' ')
    eight = 'X' if xState[8] else ('O' if zState[8] else ' ')
    print(f" {zero} | {one} | {two} ")
    print(f"---|---|---")
    print(f" {three} | {four} | {five} ")
    print(f"---|---|---")
    print(f" {six} | {seven} | {eight} ")
def sum(a,b,c):
    return a+b+c
def checkwin(xState,zState):
    wins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if(sum(xState[win[0]],xState[win[1]],xState[win[2]])==3):
            printBoard(xState, zState)
            print("X won the match")
            return 1
        if (sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3):
            printBoard(xState, zState)
            print("O won the match")
            return 0
    return -1
if __name__ == '__main__':
    xState=[0,0,0,0,0,0,0,0,0]
    zState=[0,0,0,0,0,0,0,0,0]
    turn=1 # 1 for x 0 for o
    print("Welcome to Tic Tac Toe game")
    x=0
    while x < 9:
        printBoard(xState,zState)
        if turn==1 :
           print("X's chance")
           value=int(input("Enter the position: "))
           xState[value]=1
        else:
            print("O's chance")
            value = int(input("Enter the position: "))
            zState[value] = 1

        cwin=checkwin(xState,zState)
        if cwin!=-1:
            print("Match over")
            break
        turn = 1 - turn
        x=x+1
        if x==9:
            print("Match drawn")


