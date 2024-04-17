from typing import Any
from model import Stone, OthelloBoard, HumanPlayer, CpuPlayer
from typing import Protocol


class IO(Protocol):
    def coordinate(self, stone: Stone):
        pass

# 標準入出力に関するクラス
class StandardIO:

    def coordinate(self, stone: Stone):
        self.row, self.column = map(int, input(f"プレイヤー{stone} : ").split())
        return self.row, self.column

    def __show_stone(self, i: int) -> str:  # リスト内の数字を石やブランクに変更するメソッド
        if i == Stone.WHITE:
            return '●'
        if i == Stone.BLACK:
            return '○'
        return '-'

    def show_board(self, board: list) -> None:  # 受け取ったリストを出力するメソッド
        for i, a_row in enumerate(board):
            print(*list(map(self.__show_stone, a_row)))
        print("====================================")
    
    def can_not_put(self):
        print("ここには置けません。もう1度置いてください。")
        print("====================================")

    def show_victory(self, board: OthelloBoard, final_board: list) -> None:  # 勝ち負けを出力するメソッド
        if board.victory_judge(final_board):
            print("白の勝ちです。")
        if not board.victory_judge(final_board):
            print("黒の勝ちです。")
    
    def show_can_put(self, player: HumanPlayer, board: OthelloBoard):  # 石を置くことが出来る座標を表示するメソッド
        print(f"{player.stone.name}を置ける座標", * player.can_put_coordinate(board))

    def show_put_coordinate(self, player: CpuPlayer, board: OthelloBoard, stone: Stone):  # 石を置いた座標を表示するメソッド
        print(f"プレイヤー{stone}(CPU) :", " ".join(list(map(str, player.cpu_put(board)))))
