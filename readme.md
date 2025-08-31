<html lang="ja">
    <head>
        <meta charset="utf-8" />
    </head>
    <body>
<h1><center>Curve</center></h1>
<h2>なにものか？</h2>
<p>
パラメータつき曲線 (x(t),y(t)) を表示するプログラムです。
</p>
<center><img src="images/curve.gif"></center>
<h3>環境構築</h3>
<p>
使用するパッケージ<br>
・Numpy <br>
・matplotlib　　　　･･･ matplotlib 版<br>
・PyOpenGL, glfw　･･･ OpenGL版 [検討中]<br>

</p>
<h3>使い方</h3>
<p>
[0] config.ini の設定<br>
　　パラメータ付き曲線 (x(t),y(t)) のパラメータを指定します。
<div style="padding-left: 4em;" padding="1px 10px 1px 10px">
            <table border="1">
                <tr><th>項目</th><th>設定</th></tr>
                <tr><td>　nr_points　</td><td>　点の数 (例) 100　</td></tr>
                <tr><td>　tmin　</td><td>　t の最小値 (例) -np.pi * 3　</td></tr>
                <tr><td>　tmax　</td><td>　t の最大値 (例) np.pi * 3　</td></tr>
                <tr><td>　xt　</td><td>　x(t) の定義式 (例) np.sin(t)　</td></tr>
                <tr><td>　yt　</td><td>　y(t) の定義式 (例) np.cos(t)　</td></tr>
                <tr><td>　proj_t　</td><td>　t 方向の投影位置 (例) np.pi * 4　</td></tr>
                <tr><td>　proj_x　</td><td>　x 方向の投影位置 (例) -1.5　</td></tr>
                <tr><td>　proj_y　</td><td>　y 方向の投影位置 (例) -1.5　</td></tr>
            </table>
</div>
</p>

<p>
[1] matplotlib で曲線を表示する<br>
<br>
　　曲線を表示しマウスドラッグで視点を変える<br>
　　・python curve_matplotlib.py<br>
　　・python curve2_matplotlib.py<br>
<br>
　　視点を変えて曲線を連写する<br>
　　・python curve_continuous_shooting_matplotlib.py<br>
　　・python curve2_continuous_shooting_matplotlib.py<br>
</p>

<p>
[2] OpenGL で曲線を表示する [検討中]<br>
<br>
　　曲線を表示しマウスドラッグで視点を変える<br>
　　・python curve_opengl.py<br>
<br>
　　視点を変えて曲線を連写する<br>
　　・python curve_continuous_shooting_opengl.py<br>
</p>

    </body>
</html>
