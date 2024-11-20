import cv2
import os

def extract_frames_from_mjpeg(mjpeg_file, output_folder, frame_interval=10):
    """
    Converts an MJPEG video to a series of images by extracting every `frame_interval`-th frame.

    :param mjpeg_file: Path to the MJPEG input file.
    :param output_folder: Directory where images will be saved.
    :param frame_interval: Interval at which frames should be saved (every `x` frames).
    """
    # Open the video file
    cap = cv2.VideoCapture(mjpeg_file)

    # Check if the video was opened successfully
    if not cap.isOpened():
        print("Error: Unable to open video file.")
        return

    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    frame_count = 0
    saved_count = 0

    while True:
        # Read the next frame
        ret, frame = cap.read()

        # If no frame is returned, we are at the end of the video
        if not ret:
            break

        # If the current frame count is divisible by the frame_interval, save the frame
        if frame_count % frame_interval == 0:
            # Construct the output file path
            output_path = os.path.join(output_folder, f"11_17_alex_{saved_count:04d}.jpg")
            
            # Save the frame as an image
            cv2.imwrite(output_path, frame)
            print(f"Saved {output_path}")

            saved_count += 1

        frame_count += 1

    # Release the video capture object
    cap.release()
    print(f"Extracted {saved_count} frames to {output_folder}.")

if __name__ == "__main__":
    # Example usage
    mjpeg_file = "web_cam_7.mjpeg"  # Path to your MJPEG file
    output_folder = 'output_images2'       # Folder to save images
    frame_interval = 30                   # Extract every 10th frame

    extract_frames_from_mjpeg(mjpeg_file, output_folder, frame_interval)
