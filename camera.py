import cv2

def camera():
    camera = cv2.VideoCapture(0)
    alpha ="abcdefghijkmnlopqrstuwxyz"
    keypress = input()
    while True:
        ret, frame = camera.read() #フレーム取得
        cv2.imshow("camera", frame) #フレームを画面に表示
        #qを押すとwhileループを抜ける
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
        

    #撮影用オブジェクトとウィンドウの解放
    camera.release()
    cv2.destroyAllWindows()

