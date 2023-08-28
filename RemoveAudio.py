from moviepy.video.io.VideoFileClip import VideoFileClip
import codecfinder as cf
import os

def remove_audio(input_path, output_path, codec):
    print("you are in remove audio function")
    video_clip = VideoFileClip(input_path)
    video_without_audio = video_clip.without_audio()
    
    # Save the video without audio using the provided codec
    video_without_audio.write_videofile(output_path, codec=codec)

def extract_audio(input_path, output_path):
    print("you are in remove extract audio function")
    video_clip = VideoFileClip(input_path)
    audio_clip = video_clip.audio
    
    # Save the audio clip as an audio file
    audio_clip.write_audiofile(output_path)

# if __name__ == "__main__":
#     input_video_path = input("Enter the input video path: ")  # Get input video path from user
#     if not os.path.exists(input_video_path):
#         print("Input video file does not exist.")
#     else:
#         output_video_path = "output_video_no_audio.mp4"  # Replace with your desired output file path
        
#         # Get codec information from the selected video
#         video_info = get_video_info(input_video_path)
#         if video_info and "codec" in video_info:
#             codec = video_info["codec"]
#         else:
#             codec = "libx264"  # Default codec if codec info is not available
        
#         # Remove audio using the same codec
#         remove_audio(input_video_path, output_video_path, codec)

file_path = cf.select_video_file()
print("file path is: "+file_path)
if not file_path:
    print("No video file selected.")
else:
    video_info = cf.get_video_info(file_path)
    print("this is information of the video file: "+str(video_info))
    if "codec" in video_info:
        codec = video_info["codec"]
        print("this is the codec: "+codec)
    else:
        codec = "libx264"  # Default codec if codec info is not available
    output_path_for_video = os.path.splitext(file_path)[0] + "_no_audio.mp4"  # Output video file with "_no_audio.mp4" added to the name
    output_path_for_audio = os.path.splitext(file_path)[0] + "audio.mp3"  # Output video file with "_no_audio.mp4" added to the name
    remove_audio(file_path, output_path_for_video, codec)
    extract_audio(file_path, output_path_for_audio)