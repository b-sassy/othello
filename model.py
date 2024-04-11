from enum import Enum


class Stone(Enum):  #Enumで石に対応する数値を設定
    BLANK = 0
    WHITE = 1
    BLACK = 2

# ボードを作成するクラス。
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
        raise ValueError
        # print("ここに石は置けません。")  # この下に再度繰り返す処理が必要か
        
    def __is_blank(self, row: int, column: int) -> bool:  # 石がボード上に存在しているかを確認するメソッド
        return self.__board[row][column] == Stone.BLANK
    
    def reverse_stones(self, row: int, column: int, stone: Stone, enemy_stone):
        for column_idou in self.zahyou_idou:
            for row_idou in self.zahyou_idou:
                if self.__board[row + row_idou][column + column_idou] == enemy_stone:
                    for is_reverse in range(2, 8):
                        if self.__board[row + row_idou * is_reverse][column + column_idou * is_reverse] == Stone.BLANK:
                            break
                        if self.__board[row + row_idou * is_reverse][column + column_idou * is_reverse] == enemy_stone:
                            continue
                        if self.__board[row + row_idou * is_reverse][column + column_idou * is_reverse] == stone:
                            for reverse in range(is_reverse):
                                self.__board[row + row_idou * reverse][column + column_idou * reverse] = stone


# プレーヤーを作成するクラス。
class OthelloPlayer:
    def __init__(self, stone: Stone):
        self.stone = stone
        self.enemy_stone = self.player_stone_reverse(stone)

    def put_stone(self, row: int, column: int, board: OthelloBoard):  # 石をボード上に置くメソッド
        board.change_board(row, column, self.stone, self.enemy_stone)  

    def player_stone_reverse(self, stone):  # 石、ブランクに対応する番号が3つだと判定が複雑になりそうなので、持っている石と逆の石を返すメソッドを作成。
        if stone == Stone.BLACK:
            return Stone.WHITE
        if stone == Stone.WHITE:
            return Stone.BLACK


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
        # except IndexError:
        #     print(*list(map(self.__show_stone, a_row)))
        # except ValueError:
        #     print(*list(map(self.__show_stone, a_row)))
        #     print("ここには置けません。")
