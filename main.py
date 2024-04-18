import argparse
from model import Stone, OthelloBoard, HumanPlayer, CpuPlayer
from view import StandardIO


def main(mode):
    use_board = OthelloBoard()  # ボードのインスタンスの生成
    arrangement_stone = StandardIO()  # 入力を受け取るインスタンスの生成
    arrangement_stone.show_board(use_board.get_board())  # 現状のボードの表示
    # 対戦モードの選択（スクリプト実行時に渡す引数でモードの切り替え）
    if mode == "PvP":  # 対人
        player_1 = HumanPlayer(Stone.WHITE, arrangement_stone)
        player_2 = HumanPlayer(Stone.BLACK, arrangement_stone)
    if mode == "PvC":  # 対CPU
        player_1 = HumanPlayer(Stone.WHITE, arrangement_stone)
        player_2 = CpuPlayer(Stone.BLACK)
    if mode == "CvC":  # CPU対CPU
        player_1 = CpuPlayer(Stone.WHITE)
        player_2 = CpuPlayer(Stone.BLACK)

    while player_1.reversible_stones_exist_in_all_range(use_board) or player_2.reversible_stones_exist_in_all_range(use_board):  # 両方のプレイヤーが石を置けなくなるまで繰り返す。
        while player_1.reversible_stones_exist_in_all_range(use_board):  # プレイヤー1が置ける場合は繰り返す。
            try:
                arrangement_stone.show_selectable_coordinates(player_1, use_board)  # 石を置くことが出来る座標の表示。
                player_1.select_coordinates(Stone.WHITE.name, use_board)  # プレイヤー1からの入力を受け取って、数値を返す。
                player_1.put_stone(player_1.row, player_1.column, use_board) # プレイヤー1が石を置く処理
            except Exception as e:
                print(e)
                arrangement_stone.show_error_message()  # エラーメッセージの表示
                arrangement_stone.show_board(use_board.get_board())  # 現状のボードの表示。
                continue  # 指定した座標に石が置けなかったら、置けるまでプレイヤーはそのまま。
            break  # 石が置けたら、繰り返し処理からでて、次のプレイヤーに交代。
        arrangement_stone.show_board(use_board.get_board())  # 更新されたボードの表示。
        while player_2.reversible_stones_exist_in_all_range(use_board):  # プレイヤー2が置ける場合は繰り返す。
            try:
                arrangement_stone.show_selectable_coordinates(player_2, use_board) # 石を置くことが出来る座標の表示。
                player_2.select_coordinates(Stone.BLACK.name, use_board) # プレイヤー2からの入力を受け取って、数値を返す。
                player_2.put_stone(player_2.row, player_2.column, use_board)  # プレイヤー2が石を置く処理
            except Exception:
                arrangement_stone.show_error_message()  # エラーメッセージの表示
                arrangement_stone.show_board(use_board.get_board())  # 更新されたボードの表示。     
                continue      
            arrangement_stone.show_board(use_board.get_board())  # 更新されたボードの表示。
            break  # 石が置けたら、繰り返しを中止し、プレイヤー1に戻る。   
    arrangement_stone.show_result(use_board, use_board.get_board())  # ここで最後の結果を表示

if __name__ == '__main__': 
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', type=str, default="PvC")
    args = parser.parse_args()
    main(args.mode)