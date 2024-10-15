"""親クラス
block,enemy,food,playerの親クラス
"""


class Item:
    """block,enemy,food,playerの親クラス。

    Attributes:
        now_x (int): 現在のx座標
        now_y (int): 現在のy座標
        next_x (int): 次の時刻でのx座標
        next_y (int): 次の時刻でのy座標
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

    def get_pos(self) -> tuple[int, int]:
        """
        現在の座標を取得する。

        Returns:
            tuple[int, int]: 現在の座標 (x, y)

        Examples:
            >>> item = Item(2, 3)
            >>> item.get_pos()
            (2, 3)
        """

    def update_pos(self) -> None:
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


if __name__ == "__main__":
    import doctest
    doctest.testmod()
