import cv2

facecascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)
cap0 = cv2.VideoCapture(0)
cap1 = cv2.VideoCapture(1)
while True:

    # Read a frame from webcam
    ret0, frame0 = cap0.read()
    ret1, frame1 = cap1.read()
    # Exit if frame is not captured
    if not ret0 or not ret1:
        break
    gray_frame0 = cv2.cvtColor(frame0, cv2.COLOR_BGR2GRAY)

    # Convert frame to grayscale
    g0 = cv2.cvtColor(frame0,cv2.COLOR_BGR2GRAY)
    g1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    # Detect faces
    faces0 = facecascade.detectMultiScale(g0,
        scaleFactor=1.1,
        minNeighbors=15,
        minSize=(30, 30)
    )

    faces1 = facecascade.detectMultiScale(g1,
                                          scaleFactor=1.1,
                                          minNeighbors=15,
                                          minSize=(30, 30)
                                          )

    # Count detected faces
    count0 = len(faces0)
    count1 = len(faces1)

    # Draw rectangle around each detected face
    for (x, y, w, h) in faces0:

        cv2.rectangle(
            frame0,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        for (x, y, w, h) in faces1:
            cv2.rectangle(
                frame1,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

    # Display people count
    cv2.putText(
        frame0,
        "People Count : " + str(count0),
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        2
    )

    cv2.putText(
        frame1,
        "People Count : " + str(count1),
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        2
    )

    # Show output frame
    cv2.imshow(" lapi cam",gray_frame0)
    cv2.imshow("logi cam", frame1)

    # Exit when Q key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap0.release()
cap1.release()
cv2.destroyAllWindows()
