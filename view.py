from model import Stone, OthelloBoard


# 入出力に関するクラス
class StandardIO:
    def input_coordinate(self, stone: Stone) -> int:  # 受け取った入力を返すメソッド
        self.row, self.column = map(int, input(f"プレイヤー{stone}：").split())
        return self.row, self.column

    def __show_stone(self, i: int) -> str:  # リスト内の数字を石やブランクに変更するメソッド
        if i == Stone.WHITE:
            return '●'
        if i == Stone.BLACK:
            return '○'
        if i == Stone.BLANK:
            return '-'
        return '='

    def show_board(self, board: list) -> None:  # 受け取ったリストを出力するメソッド
        for i, a_row in enumerate(board):
            print(*list(map(self.__show_stone, a_row)))
        print("====================================")
    
    def can_not_put(self):
        print("ここには置けません。もう1度置いてください。")
        print("====================================")

    def show_victory(self, final_board: list) -> None:
        if OthelloBoard.victory_judge(self, final_board):
            print("白の勝ちです。")
        print("黒の勝ちです。")

