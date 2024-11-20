from ultralytics import YOLO

# Configure the tracking parameters and run the tracker
model = YOLO("saved_models/m21/weights/best.pt")
results = model.track(source="G:/11_17/11_17_24_F1/see_cam_6_2.mp4", show=True)