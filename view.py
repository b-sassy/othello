import streamlit as st
import pandas as pd
from model import Stone, OthelloBoard, HumanPlayer, CpuPlayer


# 標準入出力に関するクラス
class StandardIO:

    def receive_coordinates(self, stone: Stone):
        self.row, self.column = map(int, input(f"プレイヤー{stone} : ").split())
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
    
    def show_error_message(self):
        print("ここには置けません。もう1度置いてください。")
        print("====================================")

    def show_result(self, board: OthelloBoard, final_board: list) -> None:  # 勝ち負けを出力するメソッド
        if board.judge_victory(final_board):
            print("白の勝ちです。")
        if not board.judge_victory(final_board):
            print("黒の勝ちです。")
    
    def show_selectable_coordinates(self, player: HumanPlayer, board: OthelloBoard):  # 石を置くことが出来る座標を表示するメソッド
        print(f"{player.stone.name}を置ける座標", * player.get_selectable_coordinates_list(board))

    def show_selected_coordinates(self, player: CpuPlayer, board: OthelloBoard, stone: Stone):  # 石を置いた座標を表示するメソッド
        print(f"プレイヤー{stone}(CPU) :", " ".join(list(map(str, player.cpu_put_stone(board)))))


class StreamlitIO:

    def receive_coordinates(self, stone: Stone):
        self.row = st.number_input(f"行 {stone}", min_value=0, max_value=7)
        self.column = st.number_input(f"列 {stone}", min_value=0, max_value=7)
        if st.button("決定"):
            st.write(f"{self.row},{self.column}の座標に置きました。")
            return self.row, self.column
        else:
            st.write("座標を入力し、決定ボタンを押してください。")
        
    def __show_stone(self, i: int) -> str:
        # これでOK
        if i == Stone.WHITE:
            return '●'
        if i == Stone.BLACK:
            return '○'
        return '-'

    def show_board(self, board: list) -> None:
        # これでOK
        a = []
        for a_row in board:
            a.append(list(map(self.__show_stone, a_row)))
        st.dataframe(a)
        st.write("====================================")

    def show_error_message(self):
        st.write("ここには置けません。もう1度置いてください。")
        st.write("====================================")

    def show_result(self, board: OthelloBoard, final_board: list) -> None:
        if board.judge_victory(final_board):
            st.write("白の勝ちです。")
        else:
            st.write("黒の勝ちです。")
    
    def show_selectable_coordinates(self, player: HumanPlayer, board: OthelloBoard):
        st.write(f"{player.stone.name}を置ける座標")
        st.dataframe(player.get_selectable_coordinates_list(board))

    def show_selected_coordinates(self, player: CpuPlayer, board: OthelloBoard, stone: Stone):
        st.write(f"プレイヤー{stone}(CPU) :", player.cpu_put_stone(board))

