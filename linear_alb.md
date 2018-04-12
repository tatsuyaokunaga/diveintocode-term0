
## ベクトルの概要について素人にも分かるように説明せよ

ベクトルとは向きと大きさを持つ量のことです。有向線分で表され、その矢印がベクトルの向きを意味し、長さがベクトルの大きさを意味しています。平面や空間上における力や速度、加速度などはベクトルで表されます。
これに対して大きさだけを持つ量をスカラーといいます。スカラーの例には個数や長さ、時間があります。
またベクトルの成分を縦に並べたものを縦ベクトルといい、横に並べたものを横ベクトルと言います。
ベクトルは通常の数（スカラー）と区別するため矢印を上に付けたり（例： $\vec{x}$）太字で書いたりします（例：$\boldsymbol{x}$）。
二つのベクトルがどのくらい同じ向きを向いているかを算出する方法がベクトルの内積です。ベクトルの内積が小さくなるほど、ベクトルの向きは反対となり、逆に大きくなるほどベクトルの向きは同じになります。
ベクトル $\boldsymbol{x}$ の長さをノルムといい、
$\|x\|$ であらわします。長さ（ノルム）が１のベクトルを単位と言います。
0でない二つのベクトル、$\boldsymbol{a}$、$\boldsymbol{b}$ の始点を繋げベクトル間の角度が９０°の場合、内積は必ず０になります。このとき $\boldsymbol{a}$, $\boldsymbol{b}$ は直交すると言います。
あるベクトル $\boldsymbol{a}$ に行列Aをかけても $\boldsymbol{a}$ の向きが変わらないとき、そのようなベクトルを固有ベクトルと言います。

## 行列の概要について素人にも分かるように説明せよ

数や関数などを長方形の形にまとめてカッコをつけたものを行列と言います。ベクトルの持つ要素を元と言い、元の数を次元と言います。行列とは同じ次元のベクトルをまとめて一つにしたものとも言えます。
以下の行列
$$
A =
\left(
\begin{array}{ccccc}
a_{11} & \cdots & a_{1i} & \cdots & a_{1n}\\
\vdots & \ddots & & & \vdots \\
a_{i1} & & a_{ii} & & a_{in} \\
\vdots & & & \ddots & \vdots \\
a_{n1} & \cdots & a_{ni} & \cdots & a_{nn}
\end{array}
\right)\\
$$
をm 行 n 列の行列といいます。
（）内の各要素の横の並びを行、縦の並びを列と言います。
行列どうしの演算で積と和（差）が可能です。
行列$A$と$B$の積を$AB$と書き、$A$の各行ベクトルを（上から）$B$の各列ベクトル（左から）のそれそれ列と行が同じ要素を掛けて足し、新しい行列の行と列の要素にいれていきます。ですので$A$の列数と$B$の行数が同じでなければ計算できません。
$AとB$の行列の和は、お互い同じ場所の要素同士を足します。なのでお互いの行と列が一致していれば計算できます。
列と行が同じn行n列行列のことをn次元正方行列と言います。
$AI=IA=A$ となる$Iを$単位行列といいます。
n次元正方行列$A$で$AB=BA=I$となるn次元正方行列$B$が存在すると、$A$のことを正則行列や正則であるといいます。また$B$を$A$の逆行列と言い、$A^{-1}$ と書きます。また行列Aの行と列を入れ替えてできる行列を行列Aの転置行列といい $^{t}A$ で表します。転置行列に変形しても元の意行列と同じであれば、その行列を対称行列と言います。
一方で対角線上以外の要素がすべて0である行列を対角行列といいます。対角行列は全て転置行列です。
また$A$の転置行列が逆行列と等しい場合、Aを直交行列と言い、$^{t}A
=A^{-1}$ と表します。
先ほどのベクトルで説明した固有値を式で表すと行列$A$、ベクトル $\boldsymbol{x}$ とすると
$A\boldsymbol{x}＝λ\boldsymbol{x}$ が成り立つ場合、λを固有値、$\boldsymbol{x}$ を固有ベクトルと言います。
また、対称行列$A$の固有値からなる対角行列をDとし、Vの各行はそれに対応する$A$の固有ベクトルとすると
$A$=$VDV^{t}$ が成り立ち、固有値分解と言います。

## 線形代数の機械学習、深層学習における使用について
機械学習ではよく
$$
y=a_{1}x_{1}+a_{2}x_{2}
$$
のような計算が大量に現れます。例えば以下のような感じです。
$$
y_{1}=a_{1}x_{1}+a_{2}x_{2} \\
y_{2}=b_{1}x_{1}+b_{2}x_{2}\\
y_{3}=a_{1}x_{1}+c_{2}x_{2}\\
y_{4}=c_{1}x_{1}+c_{2}x_{2}\\
$$
そこで
$$
A=
\begin{pmatrix}
a_{1} & a_{2}  \\
b_{1} & b_{2} \\
c_{1} & c_{2}\\
d_{1} & d_{2}\\
\end{pmatrix}\\

\boldsymbol{y}=
\begin{pmatrix}
y_{1} \\
y_{2} \\
y_{3}\\
y_{4}\\
\end{pmatrix}\\

\boldsymbol{x}=
\begin{pmatrix}
x_{1} \\
x_{2} \\
\end{pmatrix}
$$
すると
$$
\boldsymbol{y}=A\boldsymbol{x}
$$
と非常に簡潔に式を表しておくことができるのです。
このようにで線形代数を使えば簡潔に式を表示させることができ、連立方程式を解くために発展してきた様々な線形代数の操作を使うことができるようになります。
よって機械学習、深層学習の文脈での線形代数とは、数の集合を同時に操作するための便利な手法を提供してくれる、数学的ツールといえます。
線形代数は、複雑な問題を単純で直感的に理解できる、計算効率のよい問題に変換してくれます。以下は線形代数を使えばいかに高速で単純な解法を導くことができるかを示す例です。
```
# 2つの配列を掛ける
x = [1,2,3]
y = [2,3,4]
product = []
for i in range(len(x)):
    product.append(x[i]*y[i])
# 線形代数バージョン
x = numpy.array([1,2,3])
y = numpy.array([2,3,4])
x * y
```
## 固有値と固有ベクトル
###例題１
$$
A=
\begin{pmatrix}
3 & 2 & 4 \\
2 & 0 & 2 \\
4 & 2 & 3\\
\end{pmatrix}
$$
の固有値を求める。
まず、$det(A-λE)=0$ を満たす$λ$が固有値であるから
$$
\begin{align}
det(A-λE)&＝
\begin{vmatrix}
3-λ & 2 & 4 \\
2 & -λ & 2 \\
4 & 2 & 3-λ\\
\end{vmatrix}\\
&=(3-λ)(-λ)(3-λ)+2\times2\times4+4\times2\times2\
-(3-λ)\times2\times2-2\times2\times(3-λ)-4\times(-λ)\times4\\
&=-λ(3-λ)^2+16+16-4(3-λ)-4(3-λ)-16(3-λ)\\
&=-λ(3-λ)^2+24λ+8\\
&=8+15λ+6λ^2-λ^3\\
&=(1+λ)^2(8-λ)\\
\end{align}
$$

よって固有値は $λ=-1,8$
となる。

・ $λ=-1$ に対する固有ベクトルは、
$$
(A+E)\vec{ｘ}=
\begin{pmatrix}
4 & 2 & 4 \\
2 & 1 & 2 \\
4 & 2 & 4\\
\end{pmatrix}\vec{ｘ}=
\begin{pmatrix}
4 & 2 & 4 \\
2 & 1 & 2 \\
4 & 2 & 4\\
\end{pmatrix}
\begin{pmatrix}
x_{1} \\
x_{2} \\
x_{3} \\
\end{pmatrix}=0\\
$$
の解であり、固有ベクトルは以下の式
$$
2x_{1}+x_{2}+2x_{3}=0\\
$$
の解になる。
$$
x_{2}=-2x_{1}-2x_{3}\\
$$
であり、
$$
s=x_{1}、t=x_{3}
$$
とすると固有ベクトルは
$$
\begin{pmatrix}
x_{1} \\
x_{2} \\
x_{3} \\
\end{pmatrix}=s
\begin{pmatrix}
1 \\
-2 \\
0 \\
\end{pmatrix}+
t
\begin{pmatrix}
0 \\
-2 \\
1 \\
\end{pmatrix}
(s,tは任意定数、s,t\neq0)\\
$$


・ $λ=8$ に対する固有ベクトルは、
$$
(A-8E)\vec{ｘ}=
\begin{pmatrix}
-5 & 2 & 4 \\
2 & -8 & 2 \\
4 & 2 & -5\\
\end{pmatrix}\vec{ｘ}=
\begin{pmatrix}
-5 & 2 & 4 \\
2 & -8 & 2 \\
4 & 2 & -5\\
\end{pmatrix}
\begin{pmatrix}
x_{1} \\
x_{2} \\
x_{3} \\
\end{pmatrix}=0\\

\Leftrightarrow

 \left\{
\begin{array}\
-5x_{1}+2x_{2}+4x_{3}=0\\
2x_{1}-8x_{2}+2x_{3}=0\\
4x_{1}+2x_{2}-5x_{3}=0\\
\end{array}
\right.
$$
の解なので固有ベクトルは
$$
\begin{pmatrix}
x_{1} \\
x_{2} \\
x_{3} \\
\end{pmatrix}=t
\begin{pmatrix}
2 \\
1 \\
2 \\
\end{pmatrix}(tは任意定数、t\neq0)\\
$$
###例題２
まず例題１と同様にAの固有値と固有ベクトルを求める
$$
\begin{align}
det(A-λE)&＝
\begin{vmatrix}
1-λ & 0 & 0 \\
1 & 2-λ & -3 \\
1 & 1 & -2-λ\\
\end{vmatrix}\\
&=(1-λ)(2-λ)(-2-λ)-(1-λ)\times(-3)\\
&=(1-λ)(-4+λ^2)+3(1-λ)\\
&=(1-λ)(-1+λ^2)\\
&=(1-λ)^2(1+λ)\\
\end{align}
$$
よって固有値は $λ=1,-1$
となる。

・ $λ=1$ に対する固有ベクトルは、
$$
(A-E)\vec{ｘ}=
\begin{pmatrix}
0 & 0 & 0 \\
1 & 1 & -3 \\
1 & 1 & -3\\
\end{pmatrix}\
\begin{pmatrix}
x_{1} \\
x_{2} \\
x_{3} \\
\end{pmatrix}=0\\

\Leftrightarrow

x_{1}+x_{2}-3x_{3}=0\\
x_{1}=-x_{2}+3x_{3}なので、
s=x_2、t=x_3
とすると固有ベクトルは\\

\begin{pmatrix}
x_{1} \\
x_{2} \\
x_{3} \\
\end{pmatrix}=s
\begin{pmatrix}
-1 \\
1 \\
0 \\
\end{pmatrix}+
t
\begin{pmatrix}
3 \\
0 \\
1 \\
\end{pmatrix}
(s,tは任意定数、s,t\neq0)\\
$$

・ $λ=-1$ に対する固有ベクトルは、
$$
(A+E)\vec{ｘ}=
\begin{pmatrix}
2 & 0 & 0 \\
1 & 3 & -3 \\
1 & 1 & -1\\
\end{pmatrix}\
\begin{pmatrix}
x_{1} \\
x_{2} \\
x_{3} \\
\end{pmatrix}=0\\

\Leftrightarrow
\left\{
\begin{array}\
2x_{1}=0\\
x_{1}+3x_{2}-3x_{3}=0\\
x_{1}+x_{2}-x_{3}=0\\
\end{array}
\right.

\Leftrightarrow
\begin{pmatrix}
x_{1} \\
x_{2} \\
x_{3} \\
\end{pmatrix}=s
\begin{pmatrix}
0 \\
1 \\
1 \\
\end{pmatrix}
(tは任意定数、t\neq0)\\
$$
以上から
$$
\vec{v_{1}}=
\begin{pmatrix}
-1 \\
1 \\
0 \\
\end{pmatrix},
\vec{v_{2}}=
\begin{pmatrix}
3 \\
0 \\
1 \\
\end{pmatrix},
\vec{v_{3}}=
\begin{pmatrix}
0 \\
1 \\
1 \\
\end{pmatrix}とすると\\
A[\vec{v_{1}},\vec{v_{2}},\vec{v_{3}}]=[λ_{1}\vec{v_{1}},λ_{2}\vec{v_{2}},λ_{3}\vec{v_{3}},]\\
\Leftrightarrow
AP=[1\vec{v_{1}},1\vec{v_{2}},-1\vec{v_{3}},]\\
\Leftrightarrow
AP=P
\begin{pmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & -1\\
\end{pmatrix}\
-(1)
\\
\det P
\neq0であるため、逆行列P^{-1}が存在しP^{-1}を(1)の両辺左側からかけると\\
P^{-1}AP＝
\begin{pmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & -1\\
\end{pmatrix}\
$$


## 対角行列
Aの固有値と固有ベクトルを求める。
$$
\begin{align}
det(A-λE)&＝
\begin{vmatrix}
3-λ & 1 & -1 \\
1 & 2-λ & 0 \\
-1 & 0 & 2-λ\\
\end{vmatrix}\\
\end{align}
=0\\
\Leftrightarrow
(3-λ)(2-λ)^2-(2-λ)+(2-λ)(-1)=(2-λ)(4-λ)(1-λ)
$$
よって固有値は $λ=1,2,4$
となる。

・ $λ=1$ に対する固有ベクトルは、
$$
(A-E)\vec{ｘ}=
\begin{pmatrix}
2 & 1 & -1 \\
1 & 1 & 0 \\
-1 & 0 & 1\\
\end{pmatrix}\
\begin{pmatrix}
x_{1} \\
x_{2} \\
x_{3} \\
\end{pmatrix}=0\\

\Leftrightarrow
\left\{
\begin{array}\
2x_{1}+x_{2}-x_{3}=0\\
x_{1}+x_{2}=0\\
-x_{1}+x_{3}=0\\
\end{array}
\right.
\Leftrightarrow
\left\{
\begin{array}\
x_{1}+x_{2}=0\\
x_{1}=x_{3}\\
\end{array}
\right.
\Leftrightarrow
\begin{pmatrix}
x_{1} \\
x_{2} \\
x_{3} \\
\end{pmatrix}=t
\begin{pmatrix}
1\\
-1 \\
1 \\
\end{pmatrix}
(tは任意定数、t\neq0)\\
$$
・ $λ=2$ に対する固有ベクトルは、
$$
(A-E)\vec{ｘ}=
\begin{pmatrix}
1 & 1 & -1 \\
1 & 0 & 0 \\
-1 & 0 & 0\\
\end{pmatrix}\
\begin{pmatrix}
x_{1} \\
x_{2} \\
x_{3} \\
\end{pmatrix}=0\\
\Leftrightarrow
\left\{
\begin{array}\
x_{1}+x_{2}-x_{3}=0\\
x_{1}=0\\
\end{array}
\right.
\Leftrightarrow

\begin{pmatrix}
x_{1} \\
x_{2} \\
x_{3} \\
\end{pmatrix}=t
\begin{pmatrix}
0 \\
1 \\
1 \\
\end{pmatrix}
(tは任意定数、t\neq0)\\
$$
・ λ=4 に対する固有ベクトルは、
$$
(A-4E)\vec{ｘ}=
\begin{pmatrix}
-1 & 1 & -1 \\
1 & -2 & 0 \\
-1 & 0 & -2\\
\end{pmatrix}\
\begin{pmatrix}
x_{1} \\
x_{2} \\
x_{3} \\
\end{pmatrix}=0\\
\Leftrightarrow
\left\{
\begin{array}\
-x_{1}+x_{2}-x_{3}=0\\
x_{1}-2x_{2}=0\\
-x_{1}-2x_{3}=0\\
\end{array}
\right.
\Leftrightarrow
\left\{
\begin{array}\
x_{1}=-x_{2}+x_{3}\\
x_{1}=2x_{2}\\
x_{1}=-2x_{3}\\
\end{array}
\right.


\Leftrightarrow
\begin{pmatrix}
x_{1} \\
x_{2} \\
x_{3} \\
\end{pmatrix}=t
\begin{pmatrix}
2 \\
1 \\
-1 \\
\end{pmatrix}
(tは任意定数、t\neq0)\\


B^{t}ABが対角行列とは、すなわち対角化のことであるから\\B^{t}=B^{-1}ならばBはもとめる直交行列である。よって\\

\vec{v_{1}}=
\begin{pmatrix}
1 \\
-1 \\
1 \\
\end{pmatrix},
\vec{v_{2}}=
\begin{pmatrix}
0 \\
1 \\
1 \\
\end{pmatrix},
\vec{v_{3}}=
\begin{pmatrix}
2 \\
1 \\
-1 \\
\end{pmatrix}\\
B＝[\vec{v_{1}},\vec{v_{2}},\vec{v_{3}}]とすると\\
A[\vec{v_{1}},\vec{v_{2}},\vec{v_{3}}]=[λ_{1}\vec{v_{1}},λ_{2}\vec{v_{2}},λ_{3}\vec{v_{3}},]\\

\Leftrightarrow
AB=[1\vec{v_{1}},1\vec{v_{2}},2\vec{v_{3}},]\\
\Leftrightarrow
AB=B
\begin{pmatrix}
1 & 0 & 0 \\
0 & 2 & 0 \\
0 & 0 & 4\\
\end{pmatrix}\
-(1)
\\
detB
\neq0であるため、逆行列B^{-1}が存在しB^{-1}を(1)の両辺左側からかけると\\
B^{-1}AB＝
\begin{pmatrix}
1 & 0 & 0 \\
0 & 2 & 0 \\
0 & 0 & 4\\
\end{pmatrix}\\
となり対角化される。そこで\\
 B^{t}＝
 \begin{pmatrix}
 1 & -1 & 1 \\
 0 & 1 & 1 \\
 2 & 1 & -1\\
 \end{pmatrix}\\
 であるから\\
 B^{t}B =
 \begin{pmatrix}
 1 & -1 & 1 \\
 0 & 1 & 1 \\
 2 & 1 & -1\\
 \end{pmatrix}
 \begin{pmatrix}
 1 &  0 & 2 \\
 -1 & 1 & 1 \\
 1 & 1 & -1\\
 \end{pmatrix}\\

=
 \begin{pmatrix}
  3 & 0 & 0 \\
  0 & 2 & 0 \\
  0 & 0 & 6\\
  \end{pmatrix}-(2)
 \\
 よって(2)が単位行列になるには、Bの各列に各々\frac{1}{\sqrt{3}},\frac{1}{\sqrt{2}},\frac{1}{\sqrt{6}}を掛ければ\\
 B^{t}B=Eとなり\\
 B^{t}＝B^{-1}であるのでBは直交行列。ゆえに\\
 B=
\frac{1}{\sqrt{6}}
 \begin{pmatrix}
  \sqrt{2} & 0 & 2 \\
  -\sqrt{2} & \sqrt{3} & 1 \\
  \sqrt{2} & \sqrt{3} & -1\\
  \end{pmatrix}
 \\

 がもとめるBである。
$$
