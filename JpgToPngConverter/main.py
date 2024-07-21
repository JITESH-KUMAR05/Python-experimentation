from PIL import Image
import sys
import os

# check if command-line arguments are provided
if len(sys.argv) < 3:
    print("Usage: python main.py <image_folder> <output_folder>")
    sys.exit(1)

# grab first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# check if new/ exists, if not create
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# loop through images, convert to png
for filename in os.listdir(image_folder):
    if filename.endswith(".jpg") or filename.endswith(".jpeg"):
        img = Image.open(os.path.join(image_folder, filename))
        clean_name = os.path.splitext(filename)[0]
        img.save(os.path.join(output_folder, f"{clean_name}.png"), "png")
        print(f"Converted {filename} to PNG")
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print('all done!')
