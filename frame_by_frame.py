import cv2

cap = cv2.VideoCapture(
    "/Users/theohillmann/Documents/github-projects/mestrado/360-Walkability/data/cut1/cut1_360.mp4"
)

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("Video", frame)

    key = cv2.waitKey(0) & 0xFF

    if key == 27:
        break
    elif key != 32:
        continue

cap.release()
cv2.destroyAllWindows()
