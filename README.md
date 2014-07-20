旧友リムーブ(OldFriendRemover)
===============

##概要
自分がフォローしているユーザーのうち、最終ツイートが指定した日数よりも前のユーザーをリムーブします。

##バージョン
ver 1.1

##動作環境
Python 2.6以上がインストールされたPC

###動作確認済み環境
Python 2.7.5 on OS X 10.9.4 (2014/7/19)

##動かし方
1. ソースコード内の"consumer_key", "consumer_secret", "access_token", "access_token_secret" にそれぞれ自分の鍵を設定。

2. ターミナルで実行。"When do you wanna unfollow users who tweeted at last?"と言われたら、日数を整数で指定。

3. あとは該当するユーザー名が流れてくるので、y/nを入力する。oを押すとブラウザで開ける。

##使用上の注意
使ってると必ずAPI切れ起こします(宣言)

ので、ユーザーごとの検証はランダムで行っています。時間をおいて複数回実行するとよいと思います。

##連絡先
Twitter… [@hideo54](https://www.twitter.com/hideo54)

Email… hideo54.pub@gmail.com

バグがあればご報告ください。
