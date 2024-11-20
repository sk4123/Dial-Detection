import cv2
import os

def extract_images_from_video(video_path, output_dir, frame_interval):
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Check if the video was opened successfully
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    # Get the video's total number of frames
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Loop through the frames
    frame_count = 0
    extracted_images = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break  # End of video

        # If the current frame is the desired interval, save it
        if frame_count % frame_interval == 0:
            output_image_path = os.path.join(output_dir, f"frame_{frame_count:04d}.png")
            cv2.imwrite(output_image_path, frame)
            extracted_images += 1

        # Increment the frame count
        frame_count += 1

    # Release the video capture object and print the result
    cap.release()
    print(f"Extracted {extracted_images} images from {total_frames} total frames.")

# Example usage
video_path = 'input_video.mp4'  # Path to your MP4 video
output_dir = 'extracted_images'  # Directory to save the images
frame_interval = 30  # Extract every 30th frame

extract_images_from_video(video_path, output_dir, frame_interval)
