txtfile = open("input.txt","r").read()

def get_input_numbers(txtfile):
    return list(eval(txtfile.split("\n")[0]))

def get_boards(txtfile):

    tables_raw = txtfile.split("\n\n")
    tables_raw = tables_raw[1:]
    tables = []
    for table_raw in tables_raw :
        line = []
        for l in table_raw.split("\n"):
            
            line.append(list(filter(lambda a : a!="", l.split(" "))))
        tables.append(line)
    return tables

def mark_board(board,number,marked_board):
    table = []
    for x in range(len(board)):
        line = []
        for y in range(len(board[0])):
            line.append((board[x][y] == number) or marked_board[x][y])
        table.append(line)
    return table

def board_is_win(board):
    for line in board:
        if line == [True]*5 :
            return True
    for x in range(5):
        line = []
        for l in board:
            line.append(l[x])
        if line == [True]*5 : return True
        else : line = []
    return False

def sum_unmarked(board,marked_board):
    s = 0
    for x in range(len(board)):
        for y in range(len(board)):
            if not marked_board[x][y] : s += int(board[x][y])
    return s

numbers = get_input_numbers(txtfile)
boards = get_boards(txtfile)
marked_boards = [[[False]*5]*5]*len(boards)


win = False
i = 0
while i<len(numbers) and not win :
    num = numbers[i]
    for k in range(len(boards)) :
        marked_boards[k] = mark_board(boards[k],str(num),marked_boards[k])
    
    for k in range(len(boards)) :
        # print(marked_boards[k])
        if board_is_win(marked_boards[k]) :
            print(sum_unmarked(boards[k],marked_boards[k])*num)
            print(num)
            win = True

            for i in boards[k] :
                for j in i:
                    print(j, end=" ")
                print()
            break
    i += 1