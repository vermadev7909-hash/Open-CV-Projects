import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot open camera.")
        break

    cv2.imshow('frame', frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("s"):
            filename = "snap.jpg"
            cv2.imwrite(filename, frame)
            print(f"snapchat saved as {filename}")

    elif key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
