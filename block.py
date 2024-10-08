class Block:
    """
    ゲーム内のブロックを表すクラス。
    プレイヤーや敵の移動を制限する障害物として機能する。

    Attributes:
        now_x (int): ブロックのx座標
        now_y (int): ブロックのy座標
        icon (str): ブロックを表すアイコン
    """

    def __init__(self, x: int, y: int) -> None:
        """
        ブロックの初期座標とアイコンを設定する。

        Args:
            x (int): ブロックのx座標
            y (int): ブロックのy座標
        """
        pass