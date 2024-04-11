from enum import Enum


class Stone(Enum):
    BLANK = 0
    WHITE = 1
    BLACK = 2

    def matches(self, other) -> bool:
        return self == other


# ボードを作成するクラス。
class OthelloBoard():
    def __init__(self):
        self.__board = [[Stone.BLANK for _ in range(8)]for _ in range((8))]
        self.__board[3][3] = Stone.BLACK
        self.__board[3][4] = Stone.WHITE
        self.__board[4][3] = Stone.WHITE
        self.__board[4][4] = Stone.BLACK

    def get_board(self) -> list:  # ボードのリストを返すメソッド
        return self.__board
    
    def change_board(self, row: int, column: int, stone: Stone) -> None:  # ボードの状態を更新するメソッド
        if self.__is_blank(row, column):
            self.__board[row][column] = stone
            # この部分で、反転させる関数を呼び出す。
            return
        raise ValueError
        # print("ここに石は置けません。")  # この下に再度繰り返す処理が必要か
        
    def __is_blank(self, row: int, column: int) -> bool:  # 石がボード上に存在しているかを確認するメソッド
        return self.__board[row][column] == Stone.BLANK


# プレーヤーを作成するクラス。
class OthelloPlayer:
    def __init__(self, stone: Stone):
        self.stone = stone
        self.zahyou_idou = [-1, 0, 1]

    def put_stone(self, row: int, column: int, board: OthelloBoard):  # 石をボード上に置くメソッド
        board.change_board(row, column, self.stone)  
        # この中に、石を反転させるメソットを記載。
    
    def reverse_stones(self, row: int, column: int, board: OthelloBoard):
        for column_idou in self.zahyou_idou:
            for row_idou in self.zahyou_idou:
                if board[row + row_idou][column + column_idou] == Stone.BLACK:
                    for is_reverse in range(2, 8):
                        if board[row + row_idou * is_reverse][column + column_idou * is_reverse] == Stone.BLANK:
                            break
                        if board[row + row_idou * is_reverse][column + column_idou * is_reverse] == Stone.BLACK:
                            continue
                        if board[row + row_idou * is_reverse][column + column_idou * is_reverse] == self.stone:
                            for reverse in range(is_reverse):
                                board[row + row_idou * reverse][column + column_idou * reverse] == self.stone




class StandardIO:  # view.pyに入れる
    def input_coordinate(self) -> int:  # 受け取った入力を返すメソッド
        self.row, self.column = map(int, input().split())
        return self.row, self.column

    def __show_stone(self, i: int) -> str:  # リスト内の数字を石やブランクに変更するメソッド
        if i == Stone.WHITE:
            return '●'
        if i == Stone.BLACK:
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
