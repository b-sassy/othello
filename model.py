from enum import Enum


class Stone(Enum):
    WHITE = 1
    BLACK = 2

    def matches(self, other) -> bool:
        return self == other


# ボードを作成するクラス。
class OthelloBoard():
    def __init__(self):
        self.__board = [[0 for _ in range(8)]for _ in range((8))]
        self.__board[3][3] = Stone.BLACK
        self.__board[3][4] = Stone.WHITE.value
        self.__board[4][3] = Stone.WHITE.value
        self.__board[4][4] = Stone.BLACK.value

    def get_board(self) -> list:  # ボードのリストを返すメソッド
        return self.__board
    
    def change_board(self, row: int, column: int, stone: Stone) -> None:  # ボードの状態を更新するメソッド
        if self.__is_blank(row, column):
            self.__board[row][column] = stone.value
            # この部分で、反転させる関数を呼び出す。
            return
        print("ここに石は置けません。")  # この下に再度繰り返す処理が必要か
        
    def __is_blank(self, row: int, column: int) -> bool:  # 石がボード上に存在しているかを確認するメソッド
        return self.__board[row][column] == 0


# プレーヤーを作成するクラス。
class OthelloPlayer:
    def __init__(self, stone: Stone):
        self.stone = stone
        self.zahyou_idou = [-1, 0, 1]

    def put_stone(self, row: int, column: int, board: OthelloBoard):  # 石をボード上に置くメソッド
        board.change_board(row, column, self.stone)  
        # この中に、石を反転させるメソットを記載。
    
    # def reverse_stones(self, row: int, column: int, board: OthelloBoard):
    #     for column_idou in self.zahyou_idou:
    #         for row_idou in self.zahyou_idou:
    #             if board[row + row_idou][column + column_idou] == 2:
    #                 for is_reverse in range(2, 8):
    #                     if board[row + row_idou * is_reverse][column + column_idou * is_reverse] == 0:
    #                         break
    #                     if board[row + row_idou * is_reverse][column + column_idou * is_reverse] == 2:
    #                         continue




class StandardIO:  # view.pyに入れる
    def input_coordinate(self) -> int:  # 受け取った入力を返すメソッド
        self.row, self.column = map(int, input().split())
        return self.row, self.column

    def __show_stone(self, i: int) -> str:  # リスト内の数字を石やブランクに変更するメソッド
        if i == 1:
            return '●'
        if i == 2:
            return '○'
        return '-'

    def show_board(self, board: list) -> None:  # 受け取ったリストを出力するメソッド
        for a_row in board:
            print(*list(map(self.__show_stone, a_row)))


# white_stone = Stone.WHITE
# print(white_stone.value)
# print(white_stone.name)
# print(white_stone.matches(Stone.BLACK))
# print(Stone.BLACK)
# black_stone = Stone.BLACK
# print(black_stone.value)
# print(black_stone.name)
# print(black_stone.matches(Stone.BLACK))
