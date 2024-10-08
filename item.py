"""親クラス
block,enemy,food,playerの親クラス
"""

class Item:
    """block,enemy,food,playerの親クラス。

    ゲーム内のアイテムを表すクラス。
    
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
        """

     def get_next_pos(self) -> tuple[int, int]:
        """
        次に移動する予定の座標を取得する。

        Returns:
            tuple[int, int]: 次の座標 (x, y)
        """

    def get_pos(self) -> tuple[int, int]:
        """
        現在の座標を取得する。

        Returns:
            tuple[int, int]: 現在の座標 (x, y)
        """

    def update_pos(self) -> None:
        """
        アイテムの座標を更新する。次の座標に現在の座標を変更する。
        
        """
    
