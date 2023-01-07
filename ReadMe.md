# FIRST REST API BY FlASK

## python仮想環境の構築方法

- `python 3.10 -m venv .venv` pythonバージョンを指定し、デフォルトの仮想環境で実行
- VScode `command + shift + p` interpreter (python select interpreter) [python解释器]

## 基本設定

- requirements.txt 依頼注入
- .flaskenv flaskの基本設定

## run docker container

- dockerfile　設定
  - FROM python:3.10python:3.10画像をベースに使用。
  - EXPOSE 5000基本的にドキュメント1です。ポート 5000 が実行中のコンテナーが使用するものであることを Dockerfile のユーザーに伝えます。
  - WORKDIR /appDocker イメージで行うすべてのことがイメージの/appディレクトリで行われるようにします。
  - RUN pip install flaskイメージ内のコマンドを実行します。ここでのコマンドはpip install flask、アプリを実行するために必要なものです。
  - COPY . .少し不可解です！app.py現在のフォルダー (so ) 内のすべてをイメージの現在のフォルダー (so )にコピーします/app。
  - CMD ["flask", "run", "--host", "0.0.0.0"]コンテナの起動時に実行するコマンドをイメージに指示します。ここでコマンドはflask run --host=0.0.0.0.

- イメージを作成
    `docker build -t [image-name] .`  
    (option -t imageName [イメージにタグを付けて名前を付けます] 、. [現在のディレクトリ])

- Running the container with volumes for hot reloading
`docker run -dp 5000:5000 -w /app -v "$(pwd):/app" flask-smorest-api`
  - `-dp 5000:5000` -d: バックグラウンドでコンテナーを実行するため、ターミナルを閉じてもコンテナーは実行され続けます。 -p: コンピューターのポート 5000 をコンテナーのポート 5000 にマップします。
  - `-w /app` コマンドが実行されるコンテナの現在の作業ディレクトリを設定します。
  - `-v "$(pwd):/app"` ホストの現在のディレクトリをコンテナのディレクトリにバインド (リンク) します/app。注: Docker はバインド マウントに絶対パスを必要とするため、この例ではpwd、手動で入力する代わりに、作業ディレクトリの絶対パスを出力するために使用します。
  - `flask-smorest-api`- 実行するイメージ タグ

## model & view を作成

### Flask-Smorest MethodViews & Blueprints

> アイテムを分割し、エンドポイントを独自のファイルに格納
> Blueprint
`blp = Blueprint("[blueprintName]", __name__, description="description...")`

- `__name__`「インポート名」です
- descriptionドキュメント UI に表示されます

> MethodViews これらは、各メソッドが 1 つのエンドポイントにマップされるクラス

### マシュマロ(marshmallow) スキーマの追加

> データ型が正しいことを確認すること
> marshmallow1ライブラリは、必要なデータ フィールドを定義するために使用され、入力データをバリデーターに渡すことができます。marshmallow逆に、辞書に変換するPython オブジェクトを与えることもできます。
> Schema
>
> - `dump_only=True`引数は、マシュマロを使用して受信データを検証する場合、idフィールドが使用されないか、期待されないことを意味します。ただし、marshmallow を使用してクライアントに返されるデータをシリアルid化すると、フィールドが出力に含まれます。

## Flask-JWT-Extended によるユーザー認証
