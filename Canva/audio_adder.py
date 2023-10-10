import os
import subprocess

video_path = "/home/tcareless/Desktop/StockYoutTubeProject/Canva/VideoFinal_with_text.mp4"
audio_path_note7 = "/home/tcareless/Desktop/StockYoutTubeProject/Canva/note7_roll.mp3"
audio_path_bell = "/home/tcareless/Desktop/StockYoutTubeProject/Canva/nyse_bell.mp3"
audio_path_background = "/home/tcareless/Desktop/StockYoutTubeProject/Canva/background.mp3"
output_path = "/home/tcareless/Desktop/StockYoutTubeProject/Canva/VideoFinal_with_audio.mp4"

# List of delay times in milliseconds for note7 audio
delays = [1750, 3750, 5750, 7750, 9750]

# Construct the ffmpeg command to check if the video has an audio stream
check_cmd = ['ffmpeg', '-i', video_path]
result = subprocess.run(check_cmd, stderr=subprocess.PIPE, text=True)
has_audio = "Audio: " in result.stderr

# Increase the volume of note7 by 50% and apply delays
filter_parts = [f"[1:0]volume=1.5,adelay={delay}|{delay}[delayed{index}]" for index, delay in enumerate(delays)]
all_delays = ";".join(filter_parts)

background_delay = "[3:0]adelay=1000|1000[background_delayed]"

if has_audio:
    # The video has an audio stream
    amix_parts = ["[0:1]", "[2:0]", "[background_delayed]"] + [f"[delayed{index}]" for index in range(len(delays))]
    amix_filter = f"{''.join(amix_parts)}amix=inputs={len(delays) + 3}[aout]"

    cmd = [
        'ffmpeg',
        '-i', video_path,
        '-i', audio_path_note7,
        '-i', audio_path_bell,
        '-i', audio_path_background,
        '-filter_complex',
        f"{all_delays};{background_delay};{amix_filter}",
        '-map', '0:v', '-map', '[aout]', '-c:v', 'copy',
        output_path
    ]
else:
    # The video doesn't have an audio stream
    amix_parts = ["[2:0]", "[background_delayed]"] + [f"[delayed{index}]" for index in range(len(delays))]
    amix_filter = f"{''.join(amix_parts)}amix=inputs={len(delays) + 2}[aout]"

    cmd = [
        'ffmpeg',
        '-i', video_path,
        '-i', audio_path_note7,
        '-i', audio_path_bell,
        '-i', audio_path_background,
        '-filter_complex',
        f"{all_delays};{background_delay};{amix_filter}",
        '-map', '0:v', '-map', '[aout]', '-c:v', 'copy',
        output_path
    ]

# Execute the command
subprocess.run(cmd)

print("Audio added to video!")
