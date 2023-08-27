import os
import subprocess
import json
import tkinter as tk
from tkinter import filedialog

ffmpeg_bin_path = r".venv\ffmpeg-master-latest-win64-gpl-shared\bin"
os.environ["PATH"] += os.pathsep + ffmpeg_bin_path

ffprobe_path = os.path.join(ffmpeg_bin_path, "ffprobe.exe")

def get_video_info(filename):
    cmd = [
        ffprobe_path,
        "-v",
        "quiet",
        "-print_format",
        "json",
        "-show_streams",
        "-select_streams",
        "v",
        filename,
    ]
    output = subprocess.check_output(cmd).decode("utf-8")
    ffprobe_output = json.loads(output)

    video_stream = ffprobe_output["streams"][0]

    return {
        "width": video_stream["width"],
        "height": video_stream["height"],
        "bitrate": video_stream.get("bit_rate"),
        "codec": video_stream.get("codec_name"),
        "frame_rate": video_stream["r_frame_rate"],
    }

def select_video_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4 *.mkv *.avi")])
    return file_path

if __name__ == "__main__":
    filename = select_video_file()
    if not filename:
        print("No video file selected.")
    else:
        video_info = get_video_info(filename)
        print(video_info)
