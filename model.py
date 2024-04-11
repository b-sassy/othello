from enum import Enum


# 石に関するクラス
class Stone(Enum):
    BLANK = 0
    WHITE = 1
    BLACK = 2


# ボードの状態に関するクラス。
class OthelloBoard():
    def __init__(self):
        self.__board = [[Stone.BLANK for _ in range(8)]for _ in range((8))]
        self.__board[3][3] = Stone.BLACK
        self.__board[3][4] = Stone.WHITE
        self.__board[4][3] = Stone.WHITE
        self.__board[4][4] = Stone.BLACK
        self.zahyou_idou = [-1, 0, 1]

    def get_board(self) -> list:  # ボードのリストを返すメソッド
        return self.__board
    
    def change_board(self, row: int, column: int, stone: Stone, enemy_stone) -> None:  # ボードの状態を更新するメソッド
        if self.__is_blank(row, column):
            self.__board[row][column] = stone
            # この部分で、反転させる関数を呼び出す。
            self.reverse_stones(row, column, stone, enemy_stone)
            return
        raise ValueError  # このエラーは、もう石が置けない時に出る。
        # print("ここに石は置けません。")  # この下に再度繰り返す処理が必要か
        
    def __is_blank(self, row: int, column: int) -> bool:  # 石がボード上に存在しているかを確認するメソッド
        return self.__board[row][column] == Stone.BLANK
    
    def reverse_stones(self, row: int, column: int, stone: Stone, enemy_stone):  # 石を反転するメソッド
        for column_idou in self.zahyou_idou:
            for row_idou in self.zahyou_idou:
                if self.__board[row + row_idou][column + column_idou] == enemy_stone:
                    for reverse_check in range(2, 8):
                        if self.__board[row + row_idou * reverse_check][column + column_idou * reverse_check] == Stone.BLANK:
                            break
                        if self.__board[row + row_idou * reverse_check][column + column_idou * reverse_check] == enemy_stone:
                            continue
                        if self.__board[row + row_idou * reverse_check][column + column_idou * reverse_check] == stone:
                            for reverse in range(reverse_check):
                                self.__board[row + row_idou * reverse][column + column_idou * reverse] = stone


# プレーヤーに関するクラス。
class OthelloPlayer:
    def __init__(self, stone: Stone):
        self.stone = stone
        self.enemy_stone = self.player_stone_reverse(stone)

    def put_stone(self, row: int, column: int, board: OthelloBoard):  # 石をボード上に置くメソッド
        board.change_board(row, column, self.stone, self.enemy_stone)  

    def player_stone_reverse(self, stone):  # 持っている石と逆の石(相手の石)を返すメソッド
        if stone == Stone.BLACK:
            return Stone.WHITE
        if stone == Stone.WHITE:
            return Stone.BLACK