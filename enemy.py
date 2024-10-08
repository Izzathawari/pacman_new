class Enemy:
    """エネミークラス
    敵キャラクターを表すクラス。
    アイテムの基礎機能を継承し、敵キャラクターのランダムな移動を管理する。

    Attributes:
　　　　　self.icon(str) : 表示されるアイテムのアイコン
        self.now_x(int) : 現在のx座標
        self.now_y(int) : 現在のy座標
        self.next_x(int) : 次の時刻でのx座標
        self.next_y(int) : 次の時刻でのy座標
        self.status(bool) : アイテムの状態（Trueなら存在する、Falseなら存在しない消滅した）
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
