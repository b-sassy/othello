from model import Stone, OthelloBoard, OthelloPlayer
from view import StandardIO


def main():
    use_board = OthelloBoard()  # ボードのインスタンスの生成
    arrangement_stone = StandardIO()  # 入力を受け取るインスタンスの生成
    arrangement_stone.show_board(use_board.get_board())  # 現状のボードの表示
    # 上記までで初期の盤面を出力する。
    # これ以降で、オセロを実際に行えるような処理を行う。
    player_1 = OthelloPlayer(Stone.WHITE)  # 白い石を持ったプレイヤーのインスタンスの生成
    player_2 = OthelloPlayer(Stone.BLACK)  # 黒い石を持ったプレイヤーのインスタンスの生成
    while True:
        try:
            arrangement_stone.input_coordinate(Stone.WHITE.name)  # プレイヤー1からの入力を受け取って、数値を返す。
            player_1.put_stone(arrangement_stone.row, arrangement_stone.column, use_board)  # プレイヤー1が石を置く処理
            # 置けなかった時のエラーは、上記の処理で起きる。
        except ValueError:
            arrangement_stone.can_not_put()  # エラーメッセージの表示
            arrangement_stone.show_board(use_board.get_board())  # 現状のボードの表示。
            continue
            # 指定した座標に石が置けなかったら、置けるまでプレイヤーはそのまま。       
        except IndexError:
            pass
        arrangement_stone.show_board(use_board.get_board())  # 更新されたボードの表示。
        while True: # 指定した座標に石が置けなかったら、置けるまでプレイヤーはそのまま。      
            try:
                arrangement_stone.input_coordinate(Stone.BLACK.name)  # プレイヤー2からの入力を受け取って、数値を返す。
                player_2.put_stone(arrangement_stone.row, arrangement_stone.column, use_board)  # プレイヤー2が石を置く処理
            except ValueError:
                arrangement_stone.can_not_put() # エラーメッセージの表示
                arrangement_stone.show_board(use_board.get_board())  # 更新されたボードの表示。     
                continue      
            except IndexError:
                pass
            arrangement_stone.show_board(use_board.get_board())  # 更新されたボードの表示。
            break  # 石が置けたら、繰り返しを中止し、プレイヤー1に戻る。
        
if __name__ == '__main__': 
    main()