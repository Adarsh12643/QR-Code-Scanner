import cv2
from pyzbar.pyzbar import decode

def scan_qr_code():
    # Initialize the webcam
    cap = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Decode the QR code
        decoded_objects = decode(frame)

        for obj in decoded_objects:
            # Draw a rectangle around the QR code
            points = obj.polygon
            if len(points) > 4:
                hull = cv2.convexHull(points)
                points = hull.reshape(-1, 2)
            for i in range(len(points)):
                cv2.line(frame, tuple(points[i]), tuple(points[(i + 1) % len(points)]), (0, 255, 0), 3)

            # Display the decoded text
            qr_data = obj.data.decode("utf-8")
            print(f"QR Code Data: {qr_data}")
            cv2.putText(frame, qr_data, (points[0][0], points[0][1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Display the resulting frame
        cv2.imshow('QR Code Scanner', frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture and close windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    scan_qr_code()