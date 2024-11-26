from item import Item


class Player(Item):
    """プレイヤークラス
    Itemを継承して作成したプレイヤークラス.
    ゲーム内で操作されるプレイヤーを表すクラス。プレイヤーの座標や状態、顔の表情を管理し、
    移動やアイコンの変更などの操作を行う.


    Attributes:
        self.icon(str) : 表示されるアイテムのアイコン
        self.now_x(int) : 現在のx座標
        self.now_y(int) : 現在のy座標
        self.next_x(int) : 次の時刻でのx座標
        self.next_y(int) : 次の時刻でのy座標
        self.status(bool) : アイテムの状態(Trueなら存在する、Falseなら存在しない消滅した)
    """

    def __init__(self, x, y) -> None:
        super().__init__(x, y)
        self.icon = "😶"

    def get_next_pos(self, dir: tuple[int, int]) -> tuple[int, int]:
        """
        入力された移動方向に基づき、次の移動座標を計算する.

        Args:
            dir (tuple[int, int]): キー入力から受け取った次に移動したい方向.

        Returns:
            tuple[int, int]: 次に移動したい座標(例:入力が(1,0)で現在のプレイヤーの座標が
            (2,3)だった時,戻り値は(3,3))

        Examples:
            >>> player = Player(2, 3)
            >>> player.get_next_pos((1, 0))
            (3, 3)
            >>> player = Player(2, 3)
            >>> player.get_next_pos((0, 1))
            (2, 4)

        """

        self.next_x = self.now_x + dir[0]
        self.next_y = self.now_y + dir[1]
        return (self.next_x, self.next_y)

        pass

    def change_face_good(self) -> None:
        """
        プレイヤーのアイコンを😊に変更する.

        Examples:
            >>> player = Player(2, 3)
            >>> player.icon
            '😶'
            >>> player.change_face_good()
            >>> player.icon
            '😊'
        """

        self.icon = "😊"

        pass

    def change_face_bad(self) -> None:
        """
        プレイヤーのアイコンを😭に変更する.

        Examples:
            >>> player = Player(2, 3)
            >>> player.icon
            '😶'
            >>> player.change_face_bad()
            >>> player.icon
            '😭'
        """

        self.icon = "😭"

        pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()
