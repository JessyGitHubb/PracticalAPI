video_url = 'https://www.youtube.com/watch?v=DHyWrU7In20' 
#################################################################################
# do not change blew
#################################################################################
import subprocess
def download_audio(url, output_path='.'):
    yt_dlp_cmd = '/Library/Frameworks/Python.framework/Versions/3.11/bin/yt-dlp'
    command = [
        yt_dlp_cmd,
        '--verbose',
        '--extract-audio',
        '--audio-format', 'mp3',
        '--audio-quality', '0',
        '--ffmpeg-location', '/opt/homebrew/bin/ffmpeg',
        '--output', f'{output_path}/%(title)s.%(ext)s',
        url
    ]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode == 0:
        print(f"Downloaded successfully: {output_path}/{result.stdout.decode().split()[-1]}")
    else:
        print(f"Error in downloading: {result.stderr.decode()}")
# Example Usage
download_audio(video_url)
