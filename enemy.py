from item import Item
import random


class Enemy(Item):
    """エネミークラス
    Itemを継承して作成したエネミークラス.
    アイテムの基礎機能を継承し、敵のランダムな移動を管理する.また、マップから許可を取った後、座標を更新するメソッド.


    Attributes:
        self.icon(str) : 表示されるアイテムのアイコン
        self.now_x(int) : 現在のx座標
        self.now_y(int) : 現在のy座標
        self.next_x(int) : 次の時刻でのx座標
        self.next_y(int) : 次の時刻でのy座標
        self.status(bool) : アイテムの状態(Trueなら存在する、Falseなら存在しない消滅した)
    """
    pass

    def __init__(self, x, y) -> None:
        super().__init__(x, y)
        self.icon = "👻"

    def get_next_pos(self) -> tuple[int, int]:
        """ランダムに動きたい方向を計算して次の座標を返すメソッド.
        random.choiceを用いて、ランダムに上下左右の方向のいずれかを選び、その方向に基づいて次の座標を返す。
        random.choice ()が文字列、range、list、tupleいずれもできる
        random.choice()をすると持っていることが
        random.choice() = tuple[x_random , y_random]
        それで現在の座標が self [x + x_random , y + y_random]である。


        random.choice(), returns a randomly selected element
        from the specified sequence.
        for example : [(x1,y1),(x2,y2),(x3,y3)]
        random.choice() = tuple[x_random , y_random] from the given list
        for example: random.choice() = (x1,y1)


        Returns:
            tuple[int, int]: 移動したい座標

        Examples:
            >>> enemy = Enemy(2, 3)
            >>> possible_moves = [(2, 3), (3, 3), (1, 3), (2, 4), (2, 2)]
            >>> next_move = enemy.get_next_pos()
            >>> next_move in possible_moves
            True
       """
        directions = [(0, 0), (1, 0), (-1 ,0), (0, 1), (0, -1)]
        dir = random.choice(directions)
        self.next_x = self.now_x + dir[0]
        self.next_y = self.now_y + dir[1]
        return (self.next_x, self.next_y)

        pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()
