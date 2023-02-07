# python-line-webhook

Lineのメッセージを受け取ってPythonで何かしたい人向けのテンプレートです。

## 準備
- Python3.9以上をインストール
- 本リポジトリを任意のディレクトリにクローン


##  手順

### (1) Line Messaging APIチャネルの作成
1. LINE Developpers(https://developers.line.biz/ja/)からアカウントを登録する。
1. 新規チャネル作成より、Messaging APIを選択する。
1. チャネル名、所在国、業種等を入力し、チャネルを作成する。
1. 作成したチャネルの管理画面-[チャネル基本設定]から、チャネルシークレットを控えておく。
1. [Messaging API設定]から、QRコードで自分のLINEにアカウントを友だち追加する。
1. 応答設定を開き、「応答メッセージ」のチェックを外す。


### (2) Webhookの設定
1. サーバーに使用するポートを決める。(例：49200)
1. 自宅やクラウド等でサーバーを公開できる場合は、決めたポートをTCPでアクセス可能にする。なければ、[A.1 Ngrokを使ってポート公開する方法]を使って公開する。
1. Lineコンソールを開き、[Messaging API設定]から「webhookの利用」にチェックしたうえで公開用URLを設定する。例：`https://your.domain:49200` あるいは `https://xxxx-123-45-67-89.jp.ngrok.io`


### (3) サーバー起動
1. `run-server.py`の`【CHANNEL_SECRET】`を控えておいたLINEチャネルシークレットに置き換える。
1. `python3 run-server.py [ポート番号]`で起動する。


### A.1 Ngrokを使ってポート公開する方法
1. ngrok(https://ngrok.com/)のクライアントをインストールする。
2. 公式の手順にしたがって認証トークンをセットする。
3. `ngrok http [ポート番号]` で起動する。（「Forwarding」と記載されたものが公開用のURLとなる）
