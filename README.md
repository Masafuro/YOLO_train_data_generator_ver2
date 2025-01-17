# YOLO用画像&アノテーション自動生成スクリプト
[ENGLISH readme](https://github.com/Masafuro/YOLO_train_data_generator_ver2/blob/d315e1f01bbc767c314ce2da126b7d4c45184dcb/readme_EN.md)


フォーク：[Ieetenkiさん](https://github.com/leetenki/YOLO_train_data_generator)

グリーンバックで撮影した画像と背景画像を元に **学習用画像とアノテーションを自動で大量に生成** するスクリプト。

# 使い方
## 1. グリーンバック背景の画像を用意します。
### 1-1.objectフォルダ下に、 **ラベル名をつけたフォルダを用意し、** そこに画像を入れます。
object画像例

<img src="https://user-images.githubusercontent.com/1459353/212318265-0682b154-36fa-4498-bfa2-dfab8cc4af89.jpg" width="320px" >

Image by <a href="https://pixabay.com/users/oslometx-7322944/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=4223871">OsloMetX</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=4223871">Pixabay</a>

## 2.背景画像を用意します。
### 2-1. backgroundフォルダに画像を入れます。
background画像例

<img src="https://user-images.githubusercontent.com/1459353/212320624-aa5e62b3-9c8d-4485-aab0-8a76c02e0741.jpg" width="320px" >

Image by <a href="https://pixabay.com/users/12019-12019/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1751455">David Mark</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1751455">Pixabay</a>


## 3. グリーンバック背景削除のスクリプトを実行します。
> python deleteGreenback.py

削除する色範囲は下記のオプションで指定できます。（HSV系）
|  オプション  |  意味  | 初期値 |
| ---- | ---- | ---- |
|  --hl  |  h下限値  | 40 |
|  --sl  |  s下限値  | 30 |
| --vl | v下限値 | 30 |
|  --hh  |  h上限値  | 90 |
|  --sh  |  s上限値  | 255 |
| --vh | v上限値 | 255 |

### 3-1.trimmedフォルダ下にラベル名のフォルダができて、背景が削除された画像が生成されます。
生成されたobject画像から背景が削除された画像

<img src="https://user-images.githubusercontent.com/1459353/212319114-fca78b22-9b64-4ccf-85a7-a371a93c7e07.png" width="320px" >

### 3-2. deleteMinImage.pyの実行（オプション）
> python deleteMinImage.py
で10px以下の画像を削除できます。フォルダは選択画面がでるので、この場合、trimmedフォルダを選択すると小さすぎる画像を削除できます。


## 4.画像合成のスクリプトを実行します。
> python generate_sample.py --loop 10 --minSize 50

" --loop 10 "のオプションで画像合成のループ数を指定できます。
" --miSize 50 "のオプションは廃止されました。代わりにdeleteMinImage.pyにより小さすぎる画像自体を削除できます。


### 4-1. 起動時にファイルの保存先が選択できます。
サンプルではoutputフォルダを選択して出力しています。フォルダ内にimagesとlabelsのフォルダが生成されます。imagesには合成画像が、labelsにはyolo形式のラベルが生成されます。

合成された画像例

<img src="https://user-images.githubusercontent.com/1459353/212319566-a3245505-3818-4389-bf2c-459fb1424323.jpg" width="320px" >

### 4-2.出力されたラベルの例
> 0 0.34921875 0.6295427901524033 0.2125 0.2977725674091442

## 5.(オプション) アノテーション確認のスクリプトを実行することもできます。
> python annotationTest.py --sample 3

"--sample 3"のオプションで何個の確認画像を生成するか指定できます。

### 5-1.annotatedフォルダに画像が出力されます。
アノテーション情報を表示させた画像の例

<img src="https://user-images.githubusercontent.com/1459353/212320133-d1a68f17-f371-4ee3-94f1-8cbab6723952.jpg" width="320px" >

# 開発情報
##　フォルダ構造

アノテーションの出力はYOLO形式（のハズ）です。(2023/01/12 15:54 検証中
出力先は、起動時に選択できます。
<pre>
├─dev：開発中のフォルダ
│  ├─background
│  │  └─：合成する背景画像を入れる。
│  ├─object
│  │  ├─(ラベル名のフォルダ1)：グリーンバックで撮影した画像を入れる。
│  │  └─(ラベル名のフォルダ2)：複数のラベルフォルダを持つことができる。
│  ├─old：開発用の過去データ保管庫
│  ├─output：サンプル時最終出力先（出力先はスクリプト実行時に選択できます。）￥)
│  │  ├─images：合成された画像の出力先
│  │  └─labels：生成されたラベルの出力先
│  └─trimmed：グリーンバック画像をトリミングした画像を保管する場所
</pre>

## 環境構築
anacondaプロンプトの出力ファイル "delgb.yaml"を出力しておきました。インポートすると使えると思います。
