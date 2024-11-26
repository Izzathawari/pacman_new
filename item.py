"""親クラス
block,enemy,food,playerの親クラス
"""


class Item:
    """block,enemy,food,playerの親クラス。

    ゲーム内のアイテムを表すクラス。
    プレイヤーや他のオブジェクトのベースクラスとして機能し、共通の座標や状態を管理する。

    Attributes:
        now_x (int): 現在のx座標
        now_y (int): 現在のy座標
        next_x (int): 次に移動する予定のx座標
        next_y (int): 次に移動する予定のy座標
        status (bool):  アイテムの状態（Trueなら存在する、Falseなら存在しない消滅した）
        icon(str) : 表示されるアイテムのアイコン
    """

    def __init__(self, x, y) -> None:
        """
        Item初期座標と初期状態を設定する。

        Args:
            x (int): 初期のx座標
            y (int): 初期のy座標

        Returns:
             None

        Examples:
            >>> item = Item(2, 3)
            >>> item.now_x
            2
            >>> item.now_y
            3
            >>> item.next_x
            2
            >>> item.next_y
            3
            >>> item.icon
            ''
            >>> item.status
            True
        """
        self.now_x = x
        self.now_y = y
        self.next_x = x
        self.next_y = y
        self.status = True
        self.icon = ""

    def get_next_pos(self) -> tuple[int, int]:
        """
        次に移動する予定の座標を取得する。

        Returns:
            tuple[int, int]: 現在の座標 (x, y)

            Examples:
            >>> item = Item(2, 3)
            >>> item.get_next_pos()
            (2, 3)

        """
        return (self.now_x, self.now_y)

    def get_pos(self) -> tuple[int, int]:
        """
        現在の座標を取得する。

        Returns:
            tuple[int, int]: 現在の座標 (x, y)

        Examples:
            >>> item = Item(2,3)
            >>> item.get_pos()
            (2, 3)
        """
        return (self.now_x, self.now_y)

    def update_pos(self, stuck: bool = False) -> None:
        """
        アイテムの座標を更新する。次の座標に現在の座標を変更する。

        Args:
            stuck (bool): そのターンに動けない場合にTrueを渡す (default: False)

        Returns:
            None

        Examples:
            >>> item = Item(2, 3)
            >>> item.next_x = 3
            >>> item.next_y = 4
            >>> item.get_pos()
            (2, 3)
            >>> item.update_pos()
            >>> item.get_pos()
            (3, 4)

        """
        if stuck:  # そのターンに動けない場合更新しない
            self.next_x = self.now_x
            self.next_y = self.now_y
            return
        self.now_x = self.next_x
        self.now_y = self.next_y


if __name__ == "__main__":
    import doctest
    doctest.testmod()
