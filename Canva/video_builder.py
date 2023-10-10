from moviepy.editor import *

# Load your image
image_clip = ImageClip("/home/tcareless/Desktop/StockYoutTubeProject/Canva/VideoFinal.png")

# Define text positions
positions = [
    (526, 558),
    (526, 763),
    (526, 965),
    (526, 1167),
    (526, 1372)
]

video_clips = []
all_texts_so_far = []

# Add a 2-second delay of just the image at the beginning
video_clips.append(image_clip.copy().set_duration(2))

for position in positions:
    # Create a temporary text clip to get its size
    temp_txt_clip = TextClip("TSLA: +4.79%", fontsize=48, color='white', font="DejaVu-Sans-Bold")
    txt_width, txt_height = temp_txt_clip.size
    centered_position = (position[0] - txt_width/2, position[1] - txt_height/2)

    txt_clip = temp_txt_clip.set_pos(centered_position).set_duration(2)
    all_texts_so_far.append(txt_clip)

    # Create a new composite clip that contains all texts added so far
    composite_clip = CompositeVideoClip([image_clip.copy().set_duration(2)] + all_texts_so_far)
    video_clips.append(composite_clip)

# Concatenate all clips for the final video
final_clip = concatenate_videoclips(video_clips)

# Save the result to a file (as a video)
final_clip.write_videofile("/home/tcareless/Desktop/StockYoutTubeProject/Canva/VideoFinal_with_text.mp4", codec='libx264', fps=24)

print("Text added and saved to VideoFinal_with_text.mp4")
