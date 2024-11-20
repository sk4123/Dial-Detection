from moviepy.editor import VideoFileClip, concatenate_videoclips

def concatenate_videos(video_paths, output_path, method="compose"):
    clips = [VideoFileClip(path) for path in video_paths]
    if method == "reduce":
        min_height = min(clip.h for clip in clips)
        min_width = min(clip.w for clip in clips)
        clips = [clip.resize(newsize=(min_width, min_height)) for clip in clips]
    final_clip = concatenate_videoclips(clips, method=method)
    final_clip.write_videofile(output_path)

path = "G:/Aerobatics Black Box 2022-2023 Team Stuff/Other Materials/Flight_Tests_5-3-2023/Camera/Flight_1/DCIM/Movie/RO/"

video_files = [path + "2023_0503_164514_F.mp4", path + "2023_0503_164726_F.mp4", path+"2023_0503_164926_F.mp4", path+"2023_0503_165127_F.mp4", path+"2023_0503_165329_F.mp4", path+"2023_0503_165542_F.mp4", path+"2023_0504_012914_F.mp4"]
concatenate_videos(video_files, path+"output.mp4")
