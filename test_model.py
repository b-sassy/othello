import unittest
from model import Stone, OthelloBoard, HumanPlayer
from view import StandardIO

arrange = StandardIO()
playrer1 = HumanPlayer(Stone.WHITE, arrange)
playrer2 = HumanPlayer(Stone.BLACK, arrange)
use_board = OthelloBoard()


class TestOthelloBoard(unittest.TestCase):

    def test_is_board_range_within_range(self):
        # ボードの範囲内(0 ≤ row, column ≤ 7)
        self.assertTrue(use_board.is_board_range(2, 4))

    def test_is_board_range_out_of_range(self):
        # 範囲外の座標
        self.assertFalse(use_board.is_board_range(100, 10000))

    def test_is_board_range_str(self):
        # 文字列の入力
        self.assertFalse(use_board.is_board_range("hoge", "huga"))

    def test_is_blank(self):      
        # 空いてる座標
        self.assertTrue(use_board.is_blank(2, 4))

    def test_is_blank_filled(self):      
        # 埋まっている座標
        self.assertFalse(use_board.is_blank(3, 4))

    def test_is_blank_out_of_range(self):      
        # 範囲外の座標
        self.assertFalse(use_board.is_blank(100, 100))

    def test_is_blank_str(self):      
        # 座標の入力が文字列
        self.assertFalse(use_board.is_blank("hoge", "huga"))

    def test_reversible_stones_exist_witin_range(self):
        # 他の石を反転可能な座標
        self.assertTrue(use_board.reversible_stones_exist(2, 4, playrer1.stone, playrer1.hostile_stone))

    def test_reversible_stones_exist_out_of_range(self):
        # 範囲外の座標
        self.assertFalse(use_board.reversible_stones_exist(100, 100, playrer1.stone, playrer1.hostile_stone))

    def test_reversible_stones_exist_str(self):
        # 座標の入力が文字列
        self.assertFalse(use_board.reversible_stones_exist("hoge", "huga", playrer1.stone, playrer1.hostile_stone))


class TestPlayer1(unittest.TestCase):
    def test_a_select_coordinates(self):
        # 入力された座標の一致
        self.assertEqual(playrer1.select_coordinates(playrer1.stone, use_board), (2, 4))

    def test_a_select_coordinates_discrepancy(self):
        # 入力された座標の不一致
        self.assertNotEqual(playrer1.select_coordinates(playrer1.stone, use_board), (2, 4))

    def test_a_select_coordinates_out_of_range(self):
        # 範囲外の座標の入力
        self.assertFalse(playrer1.select_coordinates(playrer1.stone, use_board))

    def test_a_select_coordinates_str(self):
        # 文字列の入力
        self.assertFalse(playrer1.select_coordinates(playrer1.stone, use_board))

    def test_put_stone(self):
        # 入力した座標に石を置く上記のTestOthelloBoardにて確認できる
        self.assertIsNone(playrer1.put_stone(2, 4, use_board))
        # arrange.show_board(use_board.get_board())

    def test_get_hostile_stone(self):
        # 相手の石の取得
        self.assertEqual(playrer1.get_hostile_stone(playrer1.stone), playrer2.stone)

    def test_get_hostile_stone_discrepancy(self):
        # 相手の石の取得失敗
        self.assertNotEqual(playrer1.get_hostile_stone(playrer1.stone), playrer1.stone)
    
    def test_reversible_stones_exist_in_all_range(self):
        # ボード上に石を置ける座標がある
        self.assertTrue(playrer1.reversible_stones_exist_in_all_range(use_board))

    def test_get_selectable_coordinates_list(self):
        # 石を置ける座標のみ
        self.assertEqual(playrer1.get_selectable_coordinates_list(use_board), [[2, 4], [3, 5], [4, 2], [5, 3]])

    def test_get_selectable_coordinates_list_not_enough(self):
        # 石を置ける座標であるが、他にもおける座標が存在する
        self.assertNotEqual(playrer1.get_selectable_coordinates_list(use_board), [[2, 4]])

    def test_get_selectable_coordinates_list_too_much(self):
        # 石を置ける座標の中に置けない座標が存在する
        self.assertNotEqual(playrer1.get_selectable_coordinates_list(use_board), [[2, 4], [3, 5], [4, 2], [5, 3], [0, 0]])

    def test_get_selectable_coordinates_list_discrepancy(self):
        # 石を置けない座標のみ
        self.assertNotEqual(playrer1.get_selectable_coordinates_list(use_board), [[1, 4], [7, 5], [0, 2], [0, 0]])


class TestPlayer2(unittest.TestCase):    
    def test_a_select_coordinates(self):
        # 入力された座標の一致
        self.assertEqual(playrer2.select_coordinates(playrer2.stone, use_board), (4, 5))

    def test_a_select_coordinates_false(self):
        # 入力された座標の不一致
        self.assertNotEqual(playrer2.select_coordinates(playrer2.stone, use_board), (4, 5))

    def test_a_select_coordinates_out_of_range(self):
        # 範囲外の座標の入力
        self.assertFalse(playrer2.select_coordinates(playrer2.stone, use_board))

    def test_a_select_coordinates_str(self):
        # 文字列の入力
        self.assertFalse(playrer2.select_coordinates(playrer2.stone, use_board))

    def test_put_stone(self):
        # 入力した座標が置ければTrue、上記のTestOthelloBoardにて確認できる
        self.assertIsNone(playrer2.put_stone(4, 5, use_board), None)
        # arrange.show_board(use_board.get_board())

    def test_get_hostile_stone(self):
        # 相手の石の取得
        self.assertEqual(playrer2.get_hostile_stone(playrer2.stone), playrer1.stone)

    def test_get_hostile_stone_discrepancy(self):
        # 相手の石の取得失敗
        self.assertNotEqual(playrer2.get_hostile_stone(playrer2.stone), playrer2.stone)

    def test_reversible_stones_exist_in_all_range(self):
        # ボード上に石を置ける座標がある
        self.assertTrue(playrer2.reversible_stones_exist_in_all_range(use_board))

    def test_get_selectable_coordinates_list(self):
        # 石を置ける座標のみ
        # print(playrer2.get_selectable_coordinates_list(use_board))
        self.assertListEqual(playrer2.get_selectable_coordinates_list(use_board), [[2, 3], [2, 5], [4, 5]])

    def test_get_selectable_coordinates_list_not_enough(self):
        # 石を置ける座標であるが、他にもおける座標が存在する
        self.assertNotEqual(playrer1.get_selectable_coordinates_list(use_board), [[2, 3]])

    def test_get_selectable_coordinates_list_too_much(self):
        # 石を置ける座標の中に置けない座標が存在する
        self.assertNotEqual(playrer1.get_selectable_coordinates_list(use_board), [[2, 3], [2, 5], [4, 5], [0,0]])

    def test_get_selectable_coordinates_list_discrepancy(self):
        # 石を置けない座標のみ
        self.assertNotEqual(playrer1.get_selectable_coordinates_list(use_board), [[1, 4], [7, 5], [0, 2], [0, 0]])


if __name__ == "__main__":
    unittest.main()