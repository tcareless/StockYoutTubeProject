import numpy as np
from PIL import Image, ImageDraw, ImageFont

# Step 1: Create a white background image
width, height = 1080, 1920
background = 255 * np.ones((height, width, 3), dtype=np.uint8)  # RGB white
image = Image.fromarray(background)

# Step 2: Overlay grid and coordinates
draw = ImageDraw.Draw(image)

# Vertical lines and x-coordinates
for x in range(0, width, 100):
    draw.line([(x, 0), (x, height)], fill="black")
    draw.text((x, 0), str(x), fill="blue")

# Horizontal lines and y-coordinates
for y in range(0, height, 100):
    draw.line([(0, y), (width, y)], fill="black")
    draw.text((0, y), str(y), fill="red")

image.save("grid_image.jpg")
