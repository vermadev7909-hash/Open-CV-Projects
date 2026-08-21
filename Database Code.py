import cv2
import os
from datetime import datetime

# Ask user for folder name
folder_name = input("Enter folder name to save snapshots: ").strip()

# Default folder if left blank
if not folder_name:
    folder_name = "Snapshots"

# Create folder if it doesn't exist
os.makedirs(folder_name, exist_ok=True)

# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

print("\nPress 's' to take a snapshot.")
print("Press 'q' to quit.")

snap_count = 0

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame.")
        break

    cv2.imshow("Live Stream - Press 's' to snap", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('s'):
        # Ask for filename
        filename = input("\nEnter snapshot name: ").strip()

        # Use timestamp if blank
        if not filename:
            filename = datetime.now().strftime("snapshot_%Y%m%d_%H%M%S")

        # Add extension if missing
        if not filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            filename += ".jpg"

        # Full save path
        filepath = os.path.join(folder_name, filename)

        # Save image
        cv2.imwrite(filepath, frame)

        snap_count += 1
        print(f"✅ Snapshot #{snap_count} saved as: {filepath}")

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

print(f"\nTotal snapshots taken: {snap_count}")
print(f"All images saved in folder: {folder_name}")
