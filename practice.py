
zahyou_idou = [-1, 0, 1]  # コマを置いた座標から周りの8方向の座標をテェックするためのリスト


def to_stone(i: int) -> str:
    if i == 1:
        return '●'
    if i == 2:
        return '○'
    return '-'


def print_board(board: list):
    for row in board:
        print(*list(map(to_stone, row)))
        # print(*list(map(lambda x: "○" if x == 1 else "●" if x == 2 else "-", row)))
        

def main():
    player_number = 1  # プレイヤーによって置くコマが異なる為、用意

    # board = np.zeros((8, 8))  # 8 * 8の碁盤を作成。
    board = [[0 for _ in range(8)] for _ in range(8)]
    # 最初の石を配置。
    board[3][3] = 1
    board[3][4] = 2
    board[4][3] = 2
    board[4][4] = 1
    print_board(board)  # コンソール上に碁盤を表示

    while True:
        try:
            if player_number % 2 != 0:  # プレイヤー1の時、すなわち配置するコマは1
                reverse_check = 0
                row, column = map(int, input("プレーヤー1（黒）").split())  # 入力となる2つの数字
                if board[row][column] == 0:  # 入力した座標に何も配置されていない時に、処理を行うことができる。
                    board[row][column] = 1  # 入力した座標にコマを配置
                    player_number += 1  # この変数に +1をすることによって、次のプレーヤーに交代する。
                    #  これより下に、オセロの動き方を記す。
                    for column_idou in zahyou_idou:  # このループ処理で、置いたコマの周りの座標を全て確認する。
                        for row_idou in zahyou_idou:
                            if board[row + row_idou][column + column_idou] == 2:  # 置いたコマの周りに相手のコマがある場合をチェック。あった場合は以下の処理を行う。
                                for reverse_check in range(2, 8):  # 角にコマを置いた場合が、確認する最大の回数で7回。範囲に位置を含めていないのは、最初に置いたコマの周りの１つだから。
                                    if board[row + row_idou * reverse_check][column + column_idou * reverse_check] == 0:
                                        break
                                    elif board[row + row_idou * reverse_check][column + column_idou * reverse_check] == 2:
                                        continue
                                        # 最初に自分の置いたコマ、その周りの８方向にあった相手のコマを結んだ線上に、自分のコマがあった場合。
                                    elif board[row + row_idou * reverse_check][column + column_idou * reverse_check] == 1:
                                        for reverse in range(reverse_check):  
                                            board[row + row_idou * reverse][column + column_idou * reverse] = 1
                    print_board(board)                  
                else:  # 入力したコマの座標にすでにコマが置かれている場合は、エラーを発生させる。
                    raise ValueError
            else:
                row, column = map(int, input("プレーヤー2（白）").split())
                if board[row][column] == 0:  # 入力した座標に何も配置されていない時に、処理を行うことができる。
                    board[row][column] = 2  # 入力した座標にコマを配置
                    player_number += 1  # この変数に +1をすることによって、次のプレーヤーに交代する。
                    #  これより下に、オセロの動き方を記す。
                    for column_idou in zahyou_idou:
                        for row_idou in zahyou_idou:
                            if board[row + row_idou][column + column_idou] == 1:
                                for reverse_check in range(2, 8):
                                    if board[row + row_idou * reverse_check][column + column_idou * reverse_check] == 0:
                                        break
                                    elif board[row + row_idou * reverse_check][column + column_idou * reverse_check] == 1:
                                        continue
                                        # 最初に自分の置いたコマ、その周りの８方向にあった相手のコマを結んだ線上に、自分のコマがあった場合。
                                    elif board[row + row_idou * reverse_check][column + column_idou * reverse_check] == 2:
                                        for reverse in range(reverse_check):  
                                            board[row + row_idou * reverse][column + column_idou * reverse] = 2
                    print_board(board)
                else:
                    raise ValueError
        except IndexError:
            print_board(board)
        except ValueError:
            print_board(board)
            print("ここには置けません。")


if __name__ == '__main__':
    main()
