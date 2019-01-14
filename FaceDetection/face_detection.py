import cv2
import numpy as np

if __name__ == '__main__':
    
    ESC_KEY = 27    
    INTERVAL= 33     # 待ち時間
    FRAME_RATE = 28  # fps

    DEVICE_ID = 0

    # カメラ映像取得
    cap = cv2.VideoCapture(DEVICE_ID)

    # 保存ビデオファイルの準備
    end_flag, c_frame = cap.read()
    height, width, channels = c_frame.shape

    # Haar-like特徴分類器の読み込み
    face_cascade = cv2.CascadeClassifier('frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('eye.xml')
    
    num=0
    # 変換処理ループ
    while end_flag == True:
        num=num+1
        # イメージファイルの読み込み
        img=c_frame
        # グレースケール変換
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # 顔を検知
        faces = face_cascade.detectMultiScale(gray)
                
        #print faces
        for (x,y,w,h) in faces:    
            # 検知した顔を矩形で囲む
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            # 顔画像（グレースケール）
            roi_gray = gray[y:y+h, x:x+w]
            # 顔増（カラースケール）
            roi_color = img[y:y+h, x:x+w]
            # 顔の中から目を検知
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex,ey,ew,eh) in eyes:
                 #検知した目を矩形で囲む
                 cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

        # フレーム表示
        cv2.imshow("Raw Video", img)

        # Escキーで終了
        key = cv2.waitKey(INTERVAL)
        if key == ESC_KEY:
            break

        # 次のフレーム読み込み
        end_flag, c_frame = cap.read()

    # 終了処理
    cv2.destroyAllWindows()
    cap.release()
