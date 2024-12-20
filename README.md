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
-VSCodeというIDEをインストールする

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
  "field_size": 16,#フィルドサイズの1辺の長さ
  "enemy_num": 8,  #敵の数
  "food_num": 3 #食べ物の数
}
```

## Directory Structure
- プロジェクトの構成は以下の通り．
```shell
.
├── config.py             # パラメータ定義
├── main.py               # 実行ファイル
├── item.py               #ゲーム内の特徴ファイル
├── player.py             #プレイヤーファイル
├── enemy.py              #エネミーファイル
├── block.py              #ゲームの壁ファイル
├── field.py            
├── food.py               #プレイヤーの食べ物ファイル
├── game.py               #ゲームの機能ファイル
├── user_input.py         #ユーザ入力ファイル
├── input_without_enter.py
├── test_user_input.py  
├── parameters.json       # パラメータ指定用ファイル
├── result                # 結果出力ディレクトリ
└── utils.py              # 共有関数群
```
