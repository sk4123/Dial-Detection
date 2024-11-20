# Thanks Chat
import cv2
from ultralytics import YOLO

def process_video(input_video_path, output_video_path, model_path="yolov8n.pt"):
    # Load the YOLO model
    model = YOLO(model_path)

    # Open the input video
    cap = cv2.VideoCapture(input_video_path)
    
    if not cap.isOpened():
        print("Error: Could not open video file.")
        return
    
    # Get the video properties
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    # Define the codec and create VideoWriter object to save output
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Using XVID codec for better compatibility
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

    if not out.isOpened():
        print("Error: Could not open the output video file for writing.")
        cap.release()
        return

    # Process the video frame by frame
    while cap.isOpened():
        ret, frame = cap.read()
        
        if not ret:
            break  # If we can't read a frame, end of video
        
        # Make predictions with YOLO
        results = model(frame, mode="predict", conf=0.5)
        
        # Render predictions on the frame
        frame_with_boxes = results[0].plot()  # This draws boxes on the frame
        
        # Write the processed frame to the output video
        out.write(frame_with_boxes)

        # Optionally, display the frame with predictions (uncomment to view in real-time)
        # cv2.imshow("Frame", frame_with_boxes)
        
        # If you want to quit early, you can add:
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break

    # Release resources
    cap.release()
    out.release()

    # Close any OpenCV windows
    cv2.destroyAllWindows()
    print(f"Output video saved as: {output_video_path}")

# Example usage:
input_video = "G:/11_17/11_17_24_F1/see_cam_6_2.mp4"  # Replace with your input video path
output_video = 'predictions/output_video.mp4'  # Replace with your desired output path
model_path = "saved_models/m21/weights/best.pt"
process_video(input_video, output_video, model_path)
