
# Gitとは

Gitとは、プログラムのソースコードなどの変更履歴を記録・追跡するための分散型バージョン管理システムのこと。
バージョン管理システムとは、コンピュータ上で作成、編集されるファイルの変更履歴を管理するためのシステムのこと。
Gitは開発現場、研究機関などで、コードを管理する際にかなり高頻度で使用されている。
Gitと類似したソフトウェアはフリーソフトウエアでは、以下の通り。
* GNU arch - 分散型。C言語、シェルスクリプトで実装している。
* Bazaar - 分散型。Pythonで実装している。
* CVS - 集中型。C言語で実装している。
* GNU CSSC - SCCSのクローン。もうほとんど使われていない。
* Darcs - 分散型。Haskellで実装している。
* Mercurial - 分散型。Python、C言語で実装している。
* Monotone - 分散型。C++で実装している。
* RCS - Revision Control System。C言語で実装している。
* Subversion - 集中型。CVSの改良版という位置づけ。C言語で実装している。
* Veracity - 分散型。C言語とJavascriptで実装している。Apache License。

Gitのメリットとして以下が挙げられる。

* 変更内容を把握できる
* 変更内容の間の差分を把握できる
* 過去の状態に戻すことができる
* 他人が編集した内容を間違って上書きしないで済む

# git init

Gitのリポジトリ（ファイルやディレクトリの状態を管理する領域）を新たに作成するためのコマンド。また、すでにリポジトリがある場合には実行すると再初期化される。git initコマンドを実行したディレクトリ内には、.gitディレクトリが作成され、ここにデータが格納されていく。

#  git add

レポジトリにファイルやディレクトリの変更内容を記録するためには、コミットする必要がある。そのためにはあらかじめ、コミットしたいファイルやディレクトリを登録する必要があるが、その実行コマンドがgit addである。また登録する場所のことを、ステージング領域（エリア）という。またはインデックスとも呼ばれる。

hoge.htmlをステージング領域に追加するコマンドは以下の通り。
```
$ git add hoge.html
```

上記ステージング領域に追加されたhoge.htmlをステージング領域から削除する方法は以下の通り。
```
 $ git reset hoge.html
 ```



# git commit

ステージング領域に登録されているファイルやディレクトリの変更履歴などをレポジトリに記録するコマンド。
コミットのログを確認するには、git logコマンドを使用する。このコマンドを使うことによって、誰が・いつ・なにを変更したか確認することができる。
コミットを取り消す方法には「git reset」を使う。「git reset」には「git reset --soft」と「git reset --hard」の２種類がある。

「git reset --soft」→ワークディレクトリの内容はそのままでコミットだけを取り消す。

「git reset --hard→コミットを取り消した上でワークディレクトリの内容も書き換える。

直前のコミットを取り消したい場合は、一つ前のコミットの意味を持つ「HEAD^」をつけて「git reset --soft　HEAD^」などと使用する。もしくは「HEAD^」の代わりに、戻るコミットのハッシュ値を指定する。

直前のコミットではなく、過去のコミットを削除する方法は「git rebase -i [commit]」コマンドを使用。

以下のコミット履歴があった場合、

```
commit c4a9f6aad4ea6f5b372b9bc742c1dfc06b8641f1 (HEAD -> master, origin/master, origin/HEAD)
Author: Akihiro Nakao <nakao@diveintocode.jp>
Date:   Wed Mar 21 16:42:30 2018 +0900

    commit message 3

commit cff10b7231c5238cbd7ddab0bc19c3b7f02ba35d
Author: Akihiro Nakao <nakao@diveintocode.jp>
Date:   Wed Mar 21 16:40:31 2018 +0900

    commit message 2

commit 7b6f15fdde0f56dae4541a1a896ef6dca630e28f
Author: Akihiro Nakao <genn777f3@gmail.com>
Date:   Fri Feb 23 19:38:22 2018 +0900

    commit message 1

```

 commit message 1までコミットを戻す方法は、以下のコマンドを使用する。


```
 $ git reset --soft  7b6f15fdde0f56dae4541a1a896ef6dca630e28f

```
