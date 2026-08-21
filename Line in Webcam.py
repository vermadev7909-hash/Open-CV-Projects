import cv2

# Initialize webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Coordinates for static line (optional)
start_point_1 = (10, 40)
end_point_1 = (150, 300)
color = (0, 255, 0)  # Green in BGR
thickness = 2

start_point_2 = (20, 40)
end_point_2 = (130, 300)
color = (0, 255, 0)  # Green in BGR
thickness = 2

# Variables for interactive drawing
drawing = False
ix, iy = -1, -1

# Mouse callback function
def draw_line(event, x, y, flags, param):
    global ix, iy, drawing, frame

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE and drawing:
        temp_frame = frame.copy()
        cv2.line(temp_frame, (ix, iy), (x, y), (255, 0, 0), 2)
        cv2.imshow("Live Stream", temp_frame)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.line(frame, (ix, iy), (x, y), (255, 0, 0), 2)

# Create window and set mouse callback
cv2.namedWindow("Live Stream")
cv2.setMouseCallback("Live Stream", draw_line)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Draw a static line on every frame
    cv2.line(frame, start_point_1, end_point_1, color, thickness)
    cv2.line(frame, start_point_2, end_point_2, color, thickness)

    cv2.imshow("Live Stream", frame)

    # Exit on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
