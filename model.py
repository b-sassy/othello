from enum import Enum


# 石に関するクラス
class Stone(Enum):
    BLANK = 0
    WHITE = 1
    BLACK = 2
    WALL = 3


# ボードの状態に関するクラス。
class OthelloBoard():
    def __init__(self):
        self.__board = [[Stone.BLANK for _ in range(10)]for _ in range((10))]
        for i in range(10):
            self.__board[i][0] = Stone.WALL
            self.__board[i][9] = Stone.WALL
            self.__board[0][i] = Stone.WALL
            self.__board[9][i] = Stone.WALL
        self.__board[4][4] = Stone.WHITE
        self.__board[4][5] = Stone.BLACK
        self.__board[5][4] = Stone.BLACK
        self.__board[5][5] = Stone.WHITE
        self.zahyou_idou = [-1, 0, 1]
        self.judgment_reverse_list = []

    def get_board(self) -> list:  # ボードのリストを返すメソッド
        return self.__board
    
    def change_board(self, row: int, column: int, stone: Stone, enemy_stone) -> None:  # ボードの状態を更新するメソッド
        print("ボードの更新に入れているか")
        print(row, column)
        if self.__is_blank(row, column):
            print(f"石重複判定 {self.__is_blank(row, column)}")
            print("hogehogehoge")
            # ここまでは入った
            res = self.can_reverse_on_board(row, column, stone, enemy_stone)
            print("res", res)
            if res:
                print("hugahugahuga")
                self.__board[row][column] = stone 
                print("石を置いたよ")
                self.reverse_stones(row, column, stone, enemy_stone)
                print("反転させたよ")
                return
            raise ValueError
        raise ValueError  # このエラーは、石が置けない時に発生する。
        
    def __is_blank(self, row: int, column: int) -> bool:  # 石がボード上に存在しているかを確認するメソッド
        return self.__board[row][column] == Stone.BLANK

    def can_reverse_on_board(self, row: int, column: int, stone: Stone, enemy_stone: Stone):  # 石を置くことで、反転する石があるかを確認するメソッド
        for column_idou in self.zahyou_idou:
            for row_idou in self.zahyou_idou:
                if self.__board[row + row_idou][column + column_idou] == enemy_stone: 
                    # try:  # 置いた石の周りが敵の石だった場合
                    for reverse_check in range(2, 8):
                        try:
                            print(row_idou, column_idou)
                            print("reverse_check", reverse_check)
                            print("反転可否", self.__board[row + row_idou * reverse_check][column + column_idou * reverse_check])
                            if self.__board[row + row_idou * reverse_check][column + column_idou * reverse_check] == stone:
                                print('fuga')
                                return True
                            if self.__board[row + row_idou * reverse_check][column + column_idou * reverse_check] == Stone.BLANK and reverse_check == 7:
                                raise ValueError
                        except IndexError as e:
                            print("範囲外", e)
                            continue
                        except Exception as i:
                            print("次へ", i)
                            continue
        print("ループ終了")
        return False

    def reverse_stones(self, row: int, column: int, stone: Stone, enemy_stone: Stone):  # 石を反転するメソッド
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
    
    def victory_judge(self, final_board: list) -> bool:
        white_stone_count = final_board.count(Stone.WHITE)
        black_stone_count = final_board.count(Stone.BLACK)
        if white_stone_count > black_stone_count:
            return True


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