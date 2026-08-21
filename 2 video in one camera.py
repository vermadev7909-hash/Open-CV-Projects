import cv2

facecascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = facecascade.detectMultiScale(
        grey,
        scaleFactor=1.1,
        minNeighbors=15,
        minSize=(30, 30)
    )

    person_count = len(faces)

    for (x, y, w, h) in faces:
        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            3
        )

        cv2.rectangle(
            grey,
            (x, y),
            (x + w, y + h),
            255,
            3
        )

        frame[y:y + h, x:x + w] = cv2.medianBlur(
            frame[y:y + h, x:x + w],
            35
        )

        grey[y:y + h, x:x + w] = cv2.medianBlur(
            grey[y:y + h, x:x + w],
            35
        )

    cv2.putText(
        frame,
        f"People Count : {person_count}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        2
    )

    cv2.putText(
        grey,
        f"People Count : {person_count}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        255,
        2
    )

    cv2.imshow("Face Detection Counter", frame)
    cv2.imshow("Live", grey)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
