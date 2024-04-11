from model import Stone


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
        return '-'

    def show_board(self, board: list) -> None:  # 受け取ったリストを出力するメソッド
        for a_row in board:
            print(*list(map(self.__show_stone, a_row)))
        print("====================================")
    
    def can_not_put(self):
        print("ここには置けません。もう1度置いてください。")
        print("====================================")
