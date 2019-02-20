# AIを実装してみよう　本の付属ソースコード

AIとは、「Artificial Intelligence」の略で人工知能のことを指しますが、人工知能、特に汎用人工知能はまだ完成したといえる段階ではなく、研究者や技術者の永遠のテーマのようなものです。この本では、人工知能に一番近い技術である機械学習を用いて実現できることについて解説します。機械学習はデータ分析に用いられることの多い手法です。機械学習と言われてもピンとこない方は、コンピュータを使った統計のようなものと捉えていただいて大丈夫だと思います。

## 付属ソースコード
- 顔認識（顔と目の位置の検出のみ）
- ゲームセンターでよく見かけるホッケーのゲームをAIにプレイさせてみる
- ブロック崩しをAIにさせてみる

## インストール方法

### AnacondaのPythonのインストール
Pythonというプログラミング言語を用いてAIの実装をします。Pythonの中でも、AnacondaとよばれるPythonの環境を管理するソフトを使うと、ライブラリやモジュールのインストールが簡単にできます。また、特定のOSにおいてインストールの難しいライブラリもAnacondaを使用してインストールすると正常に動作するケースが多いのでおすすめです。linuxやMacなどのOSではAnacondaをインストールしなくてもPythonが使える場合が多いですが、OSと関連の深いパッケージに悪影響を及ぼしてしまう（Ubuntuの場合apt-get でインストールしたライブラリが、今後自動で更新されなくなるなど）ことがあるため、AnacondaのPythonをインストールしましょう。<br>

ダウンロードは以下のリンクから行ってください。<br>
<a href="https://www.anaconda.com/download/">Download Anaconda Distribution</a><br>

インストール方法は以下のサイトを参考にしてください。<br>
<a href="https://weblabo.oscasierra.net/python-anaconda-install-windows/">Anaconda を Windows にインストールする手順</a><br>

### コマンドプロンプト（ターミナル）を立ち上げる
Anacondaをインストールし終わったら、次にコマンドプロンプトを立ち上げます。コマンドプロンプトはプログラムを実行するのに必要な環境です。
Windows10の場合は左下にある検索ボックスに「Anaconda」と入力し、ヒットした「Anaconda Prompt」（黒い画面のイラストが描かれたもの）をクリックします。
#### 動作確認したい方
黒い画面が出たら試しに以下のコマンドを入力してエンターキーを押してみます。

```
python
```
そして、以下のようなメッセージが出たらインストール成功です。インストールした環境によって少しづつ文面が違ってきますが、大丈夫です。
```
(base) C:\Users\username>python
Python 3.6.5 |Anaconda, Inc.| (default, Mar 29 2018, 13:32:41) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.                                                  >>>  
```

これで、動作確認はできましたので、右上のX印を押して終了して、アプリ（Anaconda Prompt）をもう一度再起動するか、コマンドプロンプトにexit()とタイプしてエンターを押してください。


### Pythonの仮想環境の作成とライブラリのインストール
インストールしたPythonはこのままでも使えますが、今回実行するプログラムは残念ながらPython 3.7系で動かないので、新しくPythonの仮想環境を作ります。
インターネットがつながった状態で、先ほど開いたAnaconda Promptに以下のコマンドを打ち込みます。
```
conda create -n aibook python=3.6.6
(途中確認のメッセージが出るので、yかエンターを押す)
(しばらく待つ)
conda activate aibook
pip install tensorflow
pip install keras
pip install gym
```

### ソースコードのダウンロード
ソースコードをダウンロードします。このgithubのページの右上に表示される「Clone or download」をクリックします。
ダウンロードした時のファイル名は「AiBook-master.zip」になっていると思うので、Windowsのダウンロードフォルダにあるzipファイルを解凍し、ホームディレクトリ（Windowsの場合　C:\Users\ユーザ名\）に配置してください。コンピュータの操作に自信がある方は、どこに配置していただいても構いません。解凍の方法が分からない方は、以下の記事を参考にしてください。

<a href="https://121ware.com/qasearch/1007/app/servlet/relatedqa?QID=018844">Windows 10で圧縮ファイルを展開する方法 - NEC・LaVie</a>



## 4.　コマンドプロンプトを操作してみよう
```
cd C:\
```
```
dir
```
```
cd AiBook-master
```
## 5. AIを動かすための環境構築

ライブラリと呼ばれる、Pythonのモジュールをインストールするためのコマンドを書きます。ライブラリをまとめてインストールしたい方は、下記の「ライブラリをまとめてインストール」を参照してください。
```
conda create -n aibook python=3.5.6
```
```
conda activate aibook
```
```
conda install git
```
```
conda install matplotlib
```
```
pip install tensorflow
```
```
pip install keras
```
```
pip install opencv-python
```
```
pip install scikit-image
```
```
pip install gym
```
### ライブラリをまとめてインストール

AiBook-masterディレクトリ（ソースコードのルートディレクトリ）に移動し、以下のコマンドを打ち込む。(pipでインストールが必要な部分のみ手順が短くなります)
```
pip install -r requirements.txt
```
続いて、以下のコマンドも打ち込む。
```
conda create -n aibook python=3.5.6
```
```
conda activate aibook
```
```
conda install git
```
```
conda install matplotlib
```
### 2019年2月20日現在の筆者の環境でのライブラリのバージョン
```
absl-py==0.7.0
astor==0.7.1
atari-py==0.1.7
certifi==2018.8.24
chardet==3.0.4
cloudpickle==0.7.0
cycler==0.10.0
dask==1.1.1
decorator==4.3.2
future==0.17.1
gast==0.2.2
grpcio==1.18.0
gym==0.11.0
h5py==2.9.0
idna==2.8
Keras==2.2.4
Keras-Applications==1.0.7
Keras-Preprocessing==1.0.8
kiwisolver==1.0.1
Markdown==3.0.1
matplotlib==3.0.0
mkl-fft==1.0.6
mkl-random==1.0.1
networkx==2.2
numpy==1.16.1
opencv-python==4.0.0.21
Pillow==5.4.1
protobuf==3.6.1
pyglet==1.3.2
pyparsing==2.2.1
python-dateutil==2.7.3
pytz==2018.5
PyWavelets==1.0.1
PyYAML==3.13
requests==2.21.0
scikit-image==0.14.2
scipy==1.2.0
six==1.12.0
tensorboard==1.12.2
tensorflow==1.12.0
termcolor==1.1.0
toolz==0.9.0
tornado==5.1.1
urllib3==1.24.1
Werkzeug==0.14.1
wincertstore==0.2
```
