import sys
import termios


class InputWithoutEnter:
    '''エンターキーを押さずに入力を受け取るクラス'''

    def input_without_enter():
        '''エンターキーを押さずに入力を受け取る
        Returns:
            str: 入力された文字

        sysは入力と出力の便利なメソッドである
        '''

        # 標準入力のファイルディスクリプタを取得
        fd = sys.stdin.fileno() #sys.stdinはコマンドラインでユーザから入力を受け取り
                                #sys.stdin accept input from user in command line
                                #fileno()はファイルの番号である

        # fdの端末属性をゲットする #fd は file description 
        # oldとnewには同じものが入る。
        # newに変更を加えて、適応する
        # oldは、後で元に戻すため
        old = termios.tcgetattr(fd) #termios.tcgetattr(fd)は list を返す[iflag, oflag, cflag, lflag, ispeed, ospeed, cc]    
        new = termios.tcgetattr(fd)

        # new[3]はlflags
        # ICANON(カノニカルモードのフラグ)を外す
        new[3] &= ~termios.ICANON
        # ECHO(入力された文字を表示するか否かのフラグ)を外す
        new[3] &= ~termios.ECHO

        try:
            # 書き換えたnewをfdに適応する
            termios.tcsetattr(fd, termios.TCSANOW, new)
            # キーボードから入力を受ける。
            # lfalgsが書き換えられているので、エンターを押さなくても次に進む。echoもしない
            ch = sys.stdin.read(1)

        finally:
            # fdの属性を元に戻す
            # 具体的にはICANONとECHOが元に戻る
            termios.tcsetattr(fd, termios.TCSANOW, old)

        return ch
