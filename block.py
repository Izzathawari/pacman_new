from item import Item
import doctest


class Block (Item):
    """
    ゲーム内のブロックを表すクラス。
    プレイヤーや敵の移動を制限する障害物として機能する。

   Attributes:
        x (int): x座標
        y (int): y座標
        icon (str): 表示アイコン

    Examples:
        >>> block = Block(3, 3)
        >>> block.now_x
        3
        >>> block.now_y
        3
        >>> block.icon
        '🌴'
        >>> isinstance(block, Item)
        True
    """

    def __init__(self, x, y) -> None:
        super().__init__(x, y)
        self.icon = "🌴"


if __name__ == "__main__":
    doctest.testmod()
