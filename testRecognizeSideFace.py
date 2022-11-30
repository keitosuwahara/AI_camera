# -*- coding: utf-8 -*-
import numpy as np

# OpenCVモジュールのインポート
import cv2
#opencv4.0.1で動作を確認しました

# DNNモデルのパス フォルダの構成に気を付けてください（.prototxtと.caffemodelの場所）
PROTOTXT_PATH = "./models/face_recognize/deploy.prototxt"
WEIGHTS_PATH = "./models/face_recognize/res10_300x300_ssd_iter_140000_fp16.caffemodel"
#300x300にリサイズしてネットワークに入れるので、変な比率の画像は苦手
PATH_IMG = "./static/image/illastrate.jpg"

# 信頼度の閾値
CONFIDENCE = 0.5
# 1でcrop　0でBOX表示
CROP = 0

def imread(filename, flags=cv2.IMREAD_COLOR, dtype=np.uint8):
    try:
        n = np.fromfile(filename, dtype)
        img = cv2.imdecode(n, flags)
        return img
    except Exception as e:
        print(e)
        return None

def main():
    # 画像の読み込み
    img = imread(PATH_IMG)

    # モデルの読み込み
    net = cv2.dnn.readNetFromCaffe(PROTOTXT_PATH, WEIGHTS_PATH)

    # 300x300に画像をリサイズと正規化
    (h, w) = img.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(img, (300, 300)), 1.0,
                                (300, 300), (104.0, 177.0, 123.0))
    # 顔検出の実行
    net.setInput(blob)
    detections = net.forward()

    # 検出結果の可視化  
    if CROP: 
        if detections[0, 0, 0, 2] > CONFIDENCE:
            img_copy = img.copy()
            box = detections[0, 0, 0, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")
            img_crop = img_copy[startY:endY, startX:endX, :]
            cv2.imshow('img_crop', img_crop)
            cv2.waitKey(0)
            cv2.destroyAllWindows()   
            cv2.imwrite("./static/image/out.jpg", img_crop)
    else:
        img_copy = img.copy()
        for i in range(0, detections.shape[2]):
            confidence = detections[0, 0, i, 2]
    
            if confidence > CONFIDENCE:
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")
                cv2.rectangle(img_copy, (startX, startY), (endX, endY),
                            (255, 0, 0), 2)
    
        # 結果の表示
        cv2.imshow('img', img_copy)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        cv2.imwrite("./static/image/out.jpg", img_copy)
if __name__ == '__main__':
    main()