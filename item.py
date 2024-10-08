class Item:
    """
    ゲーム内のアイテムを表すクラス。
    プレイヤーや他のオブジェクトのベースクラスとして機能し、共通の座標や状態を管理する。
    

    Attributes:
        now_x (int): 現在のx座標
        now_y (int): 現在のy座標
        next_x (int): 次に移動する予定のx座標
        next_y (int): 次に移動する予定のy座標
        status (bool): アイテムが存在するかどうかの状態
        icon (str): アイテムを表すアイコン
    """

    def __init__(self, x: int, y: int) -> None:
        """
        アイテムの初期座標と初期状態を設定する。

        Args:
            x (int): 初期のx座標
            y (int): 初期のy座標
        """
        pass

    def get_next_pos(self) -> tuple[int, int]:
        """
        次に移動する予定の座標を取得する。

        Returns:
            tuple[int, int]: 次の座標 (x, y)
        """
        pass

    def get_pos(self) -> tuple[int, int]:
        """
        現在の座標を取得する。

        Returns:
            tuple[int, int]: 現在の座標 (x, y)
        """
        pass

    def update_pos(self) -> None:
        """
        アイテムの座標を更新する。次の座標に現在の座標を変更する。
        """
        pass
