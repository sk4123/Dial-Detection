import cv2
import os

def create_video_from_images(image_folder, output_video, frame_rate=30):
    # Get all image files from the folder, sorted alphabetically
    images = sorted([f for f in os.listdir(image_folder) if f.endswith(('.png', '.jpg', '.jpeg', '.bmp'))])

    if not images:
        print("No images found in the folder.")
        return

    # Read the first image to get the dimensions (height, width)
    first_image_path = os.path.join(image_folder, images[0])
    first_image = cv2.imread(first_image_path)
    height, width, _ = first_image.shape

    # Define the video writer object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 'mp4v' for .mp4
    out = cv2.VideoWriter(output_video, fourcc, frame_rate, (width, height))

    for image_name in images:
        image_path = os.path.join(image_folder, image_name)
        image = cv2.imread(image_path)

        if image is not None:
            out.write(image)
        else:
            print(f"Warning: {image_name} could not be read.")

    out.release()
    print(f"Video saved as {output_video}")

if __name__ == "__main__":
    image_folder = "path_to_your_image_folder"  # Update this path
    output_video = "output_video.mp4"  # Specify output file name
    frame_rate = 30  # Set desired frame rate (frames per second)
    
    create_video_from_images(image_folder, output_video, frame_rate)
