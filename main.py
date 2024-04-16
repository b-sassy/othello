from model import Stone, OthelloBoard, OthelloPlayer
from view import StandardIO


def main():
    use_board = OthelloBoard()  # ボードのインスタンスの生成
    arrangement_stone = StandardIO()  # 入力を受け取るインスタンスの生成
    arrangement_stone.show_board(use_board.get_board())  # 現状のボードの表示
    # 以降、オセロを実際に行えるような処理を行う。
    player_1 = OthelloPlayer(Stone.WHITE)  # 白い石を持ったプレイヤーのインスタンスの生成
    player_2 = OthelloPlayer(Stone.BLACK)  # 黒い石を持ったプレイヤーのインスタンスの生成
    while player_1.can_put_judge(use_board) or player_2.can_put_judge(use_board):  # 両方のプレイヤーが石を置けなくなるまで繰り返す。
        while player_1.can_put_judge(use_board):  # プレイヤー1が置ける場合は繰り返す。
            try:
                player_1.cpu_random_choice(use_board)
                arrangement_stone.input_coordinate(Stone.WHITE.name)  # プレイヤー1からの入力を受け取って、数値を返す。
                player_1.put_stone(arrangement_stone.row, arrangement_stone.column, use_board)  # プレイヤー1が石を置く処理
            except Exception:
                arrangement_stone.can_not_put()  # エラーメッセージの表示
                arrangement_stone.show_board(use_board.get_board())  # 現状のボードの表示。
                continue  # 指定した座標に石が置けなかったら、置けるまでプレイヤーはそのまま。
            break  # 意思が置けたら、繰り返し処理からでて、次のプレイヤーに交代。
        arrangement_stone.show_board(use_board.get_board())  # 更新されたボードの表示。
        while player_2.can_put_judge(use_board):  # プレイヤー2が置ける場合は繰り返す。
            try:
                player_2.cpu_random_choice(use_board)
                arrangement_stone.input_coordinate(Stone.BLACK.name)  # プレイヤー2からの入力を受け取って、数値を返す。
                # ここに、ランダムでリストの値を返す処理を書く。
                player_2.put_stone(arrangement_stone.row, arrangement_stone.column, use_board)  # プレイヤー2が石を置く処理
            except Exception:
                arrangement_stone.can_not_put()  # エラーメッセージの表示
                arrangement_stone.show_board(use_board.get_board())  # 更新されたボードの表示。     
                continue      
            arrangement_stone.show_board(use_board.get_board())  # 更新されたボードの表示。
            break  # 石が置けたら、繰り返しを中止し、プレイヤー1に戻る。   
    arrangement_stone.show_victory(use_board, use_board.get_board())  # ここで最後の結果を表示


if __name__ == '__main__': 
    main()