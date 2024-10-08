class Enemy:
    """
    敵キャラクターを表すクラス。
    アイテムの基礎機能を継承し、敵キャラクターのランダムな移動を管理する。

    Attributes:
        icon (str): 敵を表すアイコン
        now_x (int): 現在のx座標
        now_y (int): 現在のy座標
        next_x (int): 次の時刻でのx座標
        next_y (int): 次の時刻でのy座標
        status (bool): 敵の状態 (True: 存在する, False: 消滅した)
    """

    def __init__(self, x: int, y: int) -> None:
        """
        敵キャラクターの初期座標を設定し、アイコンを初期化する。

        Args:
            x (int): 初期のx座標
            y (int): 初期のy座標
        """
        pass

    def get_next_pos(self) -> tuple[int, int]:
        """
        敵キャラクターの次の移動先をランダムに決定する。

        ランダムに上下左右の方向のいずれかを選び、その方向に基づいて次の座標を返す。

        Returns:
            tuple[int, int]: 移動する座標 (x, y)
        """
        pass
