# Pacman Project

プロジェクトの概要をここに記載します．
このREADMEは雛形ですので，適宜修正してください．

## Requirement
- Python 3.12.5
- Linux (Windows)
- Git
- Github
- venv
- pyenv
- VSCode (IDE)

## Installation
- 結果出力用ディレクトリを作成
```shell
mkdir result
```
- 各種モジュールのインストール
```shell
pip install -r requirements.txt
```
- pyenvはPythonのバージョン管理ツール, pyenvの3.12.5のバージョン
```shell
pyenv install 3.12.5
```
- venvはPythonの仮想環境を作るためのツール。venv の使う利点が仮想環境を使えば、プロジェクトごとに独立した環境を作り、それぞれに必要なバージョンのPythonやライブラリをインストールできます。
```shell
cd <プロジェクトディレクトリのパス>
python -m venv venv
source venv/bin/activate
```


## Usage
- メインプログラムを実行．
  - `result/[日付][実行時刻]/` 下に実行結果とログが出力されます．
```shell
python main.py
```
- デフォルトのパラメータ設定をjson出力．
```shell
python config.py  # parameters.jsonというファイルが出力される．
```
- 以下のように，上記で生成されるjsonファイルの数値を書き換えて，実行時のパラメータを指定できます．
```shell
python main.py -p parameters.json
```
- 詳しいコマンドの使い方は以下のように確認できます．
```shell
python main.py -h
```


## Parameter Settings

- 指定できるパラメータは以下の通り．
```json
{
    "param1": 0,    # ダミーのパラメータ1
    "param2": {     # ダミーのパラメータ2
        "k1": "v1",
        "k2": "v2"
    }
}
```

## Directory Structure
- プロジェクトの構成は以下の通り．
```shell
.
├── config.py           # パラメータ定義
├── main.py             # 実行ファイル
├── parameters.json     # パラメータ指定用ファイル
├── result              # 結果出力ディレクトリ
│   └── 20211026_165841
└── utils.py            # 共有関数群
```
