from item import Item


class Enemy(Item):
    """エネミークラス
    Itemを継承して作成したエネミークラス.
    ランダムに動きたい方向を計算する関数。（数字ごとに動く方向を当てはめて乱数で数字を与える。）と
    マップから移動して良いと許可が出たら座標を更新するメソッド
    を追加.

    Attributes:
        self.icon(str) : 表示されるアイテムのアイコン
        self.now_x(int) : 現在のx座標
        self.now_y(int) : 現在のy座標
        self.next_x(int) : 次の時刻でのx座標
        self.next_y(int) : 次の時刻でのy座標
        self.status(bool) : アイテムの状態(Trueなら存在する、Falseなら存在しない消滅した)
    """
    pass

    def __init__(self, x, y) -> None:
        super().__init__(x, y)
        self.icon = "👻"

    def get_next_pos(self) -> tuple[int, int]:
        """ランダムに動きたい方向を計算して次の座標を返すメソッド.
        random.choice()を用いて上下左右のいずれかの方向を選択し、
        現在座標に加えて次に移動したい座標を計算する.

        Returns:
            tuple[int, int]: 移動したい座標

        Examples:
            >>> enemy = Enemy(2, 3)
            >>> possible_moves = [(2, 3), (3, 3), (1, 3), (2, 4), (2, 2)]
            >>> next_move = enemy.get_next_pos()
            >>> next_move in possible_moves
            True
       """
        pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()
