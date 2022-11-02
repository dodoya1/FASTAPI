# FastAPIとは

FastAPI は、Pythonの標準である型ヒントに基づいてPython 3.6 以降でAPI を構築するための、モダンで、高速(高パフォーマンス)な、Web フレームワークです。([FastAPIドキュメント](https://fastapi.tiangolo.com/ja/))

FastAPI は、Flaskに非常によく似ている。

# 必要なこと等

1. ターミナルで以下を実行(必要なライブラリのインストール)
    ```
    $ pip3 install fastapi
    ```
    
    ```
    $ pip3 install uvicorn
    ```

2. FastAPIを起動してみる
    ```
    $ uvicorn main:app --reload
    ```

3. APIドキュメントの自動生成
    FastAPIを起動した後、
    http://127.0.0.1:8000/docs
    に移動すると、APIドキュメントが自動生成されていることがわかる。

    GET(orPOSTなど),ルーティング,関数

    また、
    http://127.0.0.1:8000/redoc
    に移動すると、先ほどとは異なる書式のAPIドキュメントが自動生成されていることがわかる。

# 各ファイルの説明

type_hints.pyは、FASTAPIを使用する上で知っておくべきPythonでの型ヒントの書き方について記したファイルである。

main.pyは、今回FASTAPIでWeb API開発しているファイルである。(パスパラメータver)

main2.pyは、今回FASTAPIでWeb API開発しているファイルである。(クエリパラメータver)

main3.pyは、今回FASTAPIでWeb API開発しているファイルである。(必須ではないオプションパラメータver)

# 参考文献

[【FastAPI超入門】直感的にWeb API開発ができるモダンなPython WebフレームワークFastAPIの基礎を80分でマスター](https://youtu.be/vVNCVgYb6Xw)