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
      pass