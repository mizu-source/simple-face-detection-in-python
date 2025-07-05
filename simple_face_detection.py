import cv2
import pathlib
import matplotlib.colors as mcolors

def get_bgr(color_name):
    """Convert color name to BGR tuple with proper error handling"""
    try:
        rgb = mcolors.to_rgb(color_name)  # Get RGB in [0,1] range
        # Convert to BGR [0,255] and reverse the order (RGB → BGR)
        return (int(255 * rgb[2]), int(255 * rgb[1]), int(255 * rgb[0]))
    except ValueError:
        print(f"Invalid color '{color_name}', using white as fallback.")
        return (255, 255, 255)  # White in BGR

def main():
    # Load face cascade
    cascade_path = pathlib.Path(cv2.__file__).parent / "data/haarcascade_frontalface_default.xml"
    face_cascade = cv2.CascadeClassifier(str(cascade_path))
    
    if face_cascade.empty():
        print("Error loading Haar cascade.")
        return

    # Start camera with proper settings
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Use DirectShow backend on Windows
    if not cap.isOpened():
        print("Camera not accessible.")
        return

    # Set camera properties for better compatibility
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))  # Better color format

    print("Face detection running. Press 'q' to quit.")

    # Define colors using the corrected function
    rect_color = get_bgr("limegreen")  # Should be (50, 205, 50) in BGR
    text_color = get_bgr("deepskyblue")  # Should be (255, 191, 0) in BGR

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame.")
            break

        # Convert to grayscale for detection (but keep original for display)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces with optimized parameters
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        # Draw face rectangles and labels
        for i, (x, y, w, h) in enumerate(faces):
            cv2.rectangle(frame, (x, y), (x+w, y+h), rect_color, 2)
            cv2.putText(frame, f"Face {i+1}", (x, y-10), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, rect_color, 2)

        # Display face count
        cv2.putText(frame, f"Faces: {len(faces)}", (10, 30),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.9, text_color, 2)

        # Show the frame with detections
        cv2.imshow("Face Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    print("Stopped.")

if __name__ == "__main__":
    main()
