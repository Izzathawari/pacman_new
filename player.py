from item import Item

class player:
    """
    playerクラス

    playerクラスはplayerの性格を含む。

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