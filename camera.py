import cv2

face_cascade_path = "./models/face_recognize/haarcascade_frontalface_default.xml.xml"
face_cascade = cv2.CascadeClassifier(face_cascade_path)#識別子読み込み
def camera():
    camera = cv2.VideoCapture(0)
    while True:
        ret, frame = camera.read() #フレーム取得
        cv2.imshow("AIcamera", frame) #フレームを画面に表示
        #qを押すとwhileループを抜ける
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
        

    #撮影用オブジェクトとウィンドウの解放
    camera.release()
    cv2.destroyAllWindows()

