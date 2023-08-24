import cv2
import numpy as np

def apply_gameboy_effect(frame):
    # Custom Game Boy Camera color palette
    palette = np.array([
        [15, 56, 15],   # Dark green
        [48, 98, 48],   # Dark green
        [139, 172, 15], # Light green
        [155, 188, 15], # Light green
    ], dtype=np.uint8)

    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Apply the color palette using NumPy's vectorized operations
    gameboy_frame = palette[gray_frame // 64]
    
    return gameboy_frame

def add_scanlines(frame):
    scanline_intensity = 48  # Adjust this value to control scanline darkness
    scanline = np.zeros_like(frame)
    scanline[1::2, :] = scanline_intensity
    scanlined_frame = cv2.addWeighted(frame, 1, scanline, 1, 0)
    return scanlined_frame

def main():
    # Open a connection to the webcam
    cap = cv2.VideoCapture(0)
    
    # Set the width and height of the video capture
    cap.set(3, 500)  # Width
    cap.set(4, 500)  # Height
    
    while True:
        # Capture a frame from the webcam
        ret, frame = cap.read()
        
        # Resize the frame to a smaller resolution
        small_frame = cv2.resize(frame, (160, 144))
        
        # Apply the Game Boy Camera effect
        gameboy_frame = apply_gameboy_effect(small_frame)
        
        # Resize the frame back to the original size
        gameboy_frame = cv2.resize(gameboy_frame, (500, 500))
        
        # Add scanline effect
        gameboy_frame = add_scanlines(gameboy_frame)
        
        # Display the frame
        cv2.imshow("CRT Monitor Game Boy Camera Effect", gameboy_frame)
        
        # Wait for a key press and check if it's 'q'
        key = cv2.waitKey(17)  # Approximately 16.7 milliseconds for 59.7 FPS
        if key == ord('q'):
            break
    
    # Release the webcam and close the window
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
