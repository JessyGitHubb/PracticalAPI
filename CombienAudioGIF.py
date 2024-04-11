audio_path = "f.mp3"
gif_path = "f.gif"
start_second = 10
stop_second = 44
#################################################################################
# do not change blew
#################################################################################
import os
os.environ["IMAGEIO_FFMPEG_EXE"] = "/opt/homebrew/bin/ffmpeg"
from moviepy.editor import VideoFileClip, AudioFileClip, CompositeVideoClip
os.environ["IMAGEIO_FFMPEG_EXE"] = "/opt/homebrew/bin/ffmpeg"
if not os.path.isfile(audio_path):
    raise IOError(f"File not found: {audio_path}")
audio = AudioFileClip(audio_path).subclip(start_second,stop_second)
if not os.path.isfile(gif_path):
    raise IOError(f"GIF file not found: {gif_path}")
gif_clip = VideoFileClip(gif_path)
if gif_clip.duration > stop_second-start_second: 
    gif_clip = gif_clip.subclip(0, stop_second-start_second)
elif gif_clip.duration < stop_second-start_second:
    gif_clip = gif_clip.loop(duration=audio.duration)
final_clip = gif_clip.set_audio(audio)
final_clip.write_videofile("output.mp4", codec="libx264",
                           threads=4,
                           preset='fast',
                           bitrate='256k',
                           fps=gif_clip.fps,
                           audio_codec='aac',
                           audio_bitrate='64k')
