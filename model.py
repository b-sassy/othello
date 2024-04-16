import random
from enum import Enum

# 石に関するクラス
class Stone(Enum):
    BLANK = 0
    WHITE = 1
    BLACK = 2


# ボードの状態に関するクラス。
class OthelloBoard():
    def __init__(self):  # 最初のボードの状態を持つ。
        self.__board = [[Stone.BLANK for _ in range(8)]for _ in range((8))]
        self.__board[3][3] = Stone.WHITE
        self.__board[3][4] = Stone.BLACK
        self.__board[4][3] = Stone.BLACK
        self.__board[4][4] = Stone.WHITE
        self.zahyou_idou = [-1, 0, 1]  # 置いた石の全方位を網羅するためのリスト。
        self.white_result_list = 0
        self.black_result_list = 0

    def get_board(self) -> list:  # ボードのリストを返すメソッド
        return self.__board
    
    def change_board(self, row: int, column: int, stone: Stone, enemy_stone) -> None:  # ボードの状態を更新するメソッド
        if self.board_range(row, column) and self.is_blank(row, column):  # 指定した座標がボードの範囲、すでに石が乗っているかを確認。
            if self.can_reverse_on_board(row, column, stone, enemy_stone):  # 指定した座標に石が置けるか確認(反転させることができる石があるかを確認)
                self.__board[row][column] = stone  # 全ての条件を満たした時に、指定した座標に石を置く。
                self.reverse_stones(row, column, stone, enemy_stone) # 石を反転させる。
                return
            raise ValueError  # 反転できる石がなかった場合は、エラーを起こす。
        raise ValueError  # 石を置ける座標を超えてしまった場合、すでに石が乗っている場合は、エラーを起こす。
    
    def board_range(self, row: int, column: int) -> bool:  # 指定した座標がボードの座標の範囲内かを確認するメソッド。
        if row >= 0 and row <= 7 and column >= 0 and column <= 7:
            return True

    def is_blank(self, row: int, column: int) -> bool:  # 石がボード上に存在しているかを確認するメソッド
        return self.__board[row][column] == Stone.BLANK

    def can_reverse_on_board(self, row: int, column: int, stone: Stone, enemy_stone: Stone) -> bool:  # 石を置くことで、反転する石があるかを確認するメソッド
        for row_idou in self.zahyou_idou:
            for column_idou in self.zahyou_idou:
                try:
                    if row + row_idou <= -1 or column + column_idou <= -1:  # リストの範囲を超えた場合はエラーを起こす。
                        raise IndexError
                except IndexError:
                    continue
                try:
                    if self.__board[row + row_idou][column + column_idou] == enemy_stone:  # 指定した座標の周りに敵の石があった場合の処理。
                        for reverse_check in range(2, 8):  # 敵の石と自分の石を結んだ線上の確認。（確認する範囲は、最大でも7箇所）
                            try:
                                if row + row_idou * reverse_check <= -1 or column + column_idou * reverse_check <= -1:  # リストの範囲を超えた場合はエラーを起こす。
                                    raise IndexError
                                if self.__board[row + row_idou * reverse_check][column + column_idou * reverse_check] == Stone.BLANK:  # 途中で何も置かれていない座標があればその時点で繰り返し処理を終了。
                                    break
                                if self.__board[row + row_idou * reverse_check][column + column_idou * reverse_check] == stone:  # 1つでも自分の石があれば反転できるので、この場合はTrueを返す。
                                    return True
                            except IndexError:  # 範囲外であれば、最後まで続ける。
                                continue
                except IndexError:  # 置いた座標の周りにある敵の石の数が複数あれば、別の石に移る。
                    continue
        return False  # この処理を行う過程で、Trueが返されない場合は、反転できる意思が1つもないことを表すのでFalseを返す。

    def reverse_stones(self, row: int, column: int, stone: Stone, enemy_stone: Stone) -> None:  # 石を反転するメソッド
        for row_idou in self.zahyou_idou:
            for column_idou in self.zahyou_idou:
                try:
                    if row + row_idou <= -1 or column + column_idou <= -1:  # リストの範囲を超えた場合はエラーを起こす。
                        raise IndexError
                except IndexError:
                    continue
                try:        
                    if self.__board[row + row_idou][column + column_idou] == enemy_stone:  # 指定した座標の周りに敵の石があった場合の処理。
                        for reverse_check in range(2, 8):  # 敵の石と自分の石を結んだ線上の確認。（確認する範囲は、最大でも7箇所）
                            if row + row_idou * reverse_check <= -1 or column + column_idou * reverse_check <= -1:  # リストの範囲を超えた場合はエラーを起こす。
                                raise IndexError
                            if self.__board[row + row_idou * reverse_check][column + column_idou * reverse_check] == Stone.BLANK:  # 途中で何も置かれていない座標があればその時点で繰り返し処理を終了。
                                break
                            if self.__board[row + row_idou * reverse_check][column + column_idou * reverse_check] == enemy_stone:  # 敵の石が置かれていた場合は、繰り返し処理を続ける。
                                continue
                            if self.__board[row + row_idou * reverse_check][column + column_idou * reverse_check] == stone:  # 自分の石があった場合は、その時点までであった石を全て反転させる。
                                for reverse in range(reverse_check):
                                    self.__board[row + row_idou * reverse][column + column_idou * reverse] = stone
                                break  # 反転させる処理を実行したら処理は終了させる。（○、●、○、●、○ と並んでいた場合に全て反転させてしまうため）
                except IndexError:
                    continue
                
    def victory_judge(self, final_board: list) -> bool:  # 勝ち負けを判定するメソッド
        for i in range(8):
            self.white_result_list += final_board[i].count(Stone.WHITE)
            self.black_result_list += final_board[i].count(Stone.BLACK)
        if self.white_result_list > self.black_result_list:  # 白い石が黒石より多い時は、Trueを返す。
            return True
        if self.black_result_list > self.white_result_list:
            return False


# プレーヤーに関するクラス。
class OthelloPlayer:
    def __init__(self, stone: Stone):  # 自分の石と、相手の石の状態を持つ。
        self.stone = stone
        self.enemy_stone = self.player_stone_reverse(stone)

    def put_stone(self, row: int, column: int, board: OthelloBoard) -> None:  # 石をボード上に置くメソッド
        board.change_board(row, column, self.stone, self.enemy_stone)  

    def player_stone_reverse(self, stone: Stone) -> Stone:  # 持っている石と逆の石(相手の石)を返すメソッド
        if stone == Stone.BLACK:
            return Stone.WHITE
        if stone == Stone.WHITE:
            return Stone.BLACK
        
    def can_put_judge(self, board: OthelloBoard) -> bool:  # 石を置くことが出来る座標があるかを確認するメソッド
        judge_list = []
        for row in range(8):
            for column in range(8):
                if board.board_range(row, column) and board.can_reverse_on_board(row, column, self.stone, self.enemy_stone) and board.is_blank(row, column):
                    judge_list.append("True")
        if judge_list.count("True") > 0:
            return True
        return False

    def cpu_random_select(self, board: OthelloBoard) -> list:  # 石を置くことが出来る座標をリストに格納するメソッド
        cpu_can_put_list = []
        cpu_can_put_all_list = []
        for row in range(8):
            for column in range(8):
                if board.board_range(row, column) and board.can_reverse_on_board(row, column, self.stone, self.enemy_stone) and board.is_blank(row, column):
                    cpu_can_put_list.append(row)
                    cpu_can_put_list.append(column)
                    cpu_can_put_all_list.append(cpu_can_put_list)
                    cpu_can_put_list = []
        return cpu_can_put_all_list
    
    def cpu_put(self, board: OthelloBoard) -> int:  # CPUが置いた座標を返すメソッド
        self.selected_coordinate = random.choice(self.cpu_random_select(board))
        self.row, self.column = self.selected_coordinate[0], self.selected_coordinate[1]
        return self.row, self.column
    
