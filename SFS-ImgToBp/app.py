import os
from flask import Flask, render_template, request
from tkinter import filedialog
from PIL import Image, ImageDraw
import json

# Check if required libraries are installed
try:
    import flask
    import PIL
except ImportError as e:
    print(f"Error: {e}. Please make sure all required libraries are installed.")
    exit(1)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/process_image", methods=["POST"])
def process_image():
    # Check if file was uploaded
    if 'image' not in request.files:
        return "No file uploaded"

    file = request.files['image']

    # Check if a file was selected
    if file.filename == '':
        return "No file selected"

    # Create a unique folder name based on the input image's name
    folder_name = os.path.splitext(file.filename)[0]
    output_folder = os.path.join(os.getcwd(), folder_name)
    os.makedirs(output_folder, exist_ok=True)

    # Save the uploaded image to the output folder
    image_path = os.path.join(output_folder, file.filename)
    file.save(image_path)

    # Load the image and convert it to black and white
    image = Image.open(image_path).convert("1")

    # Create a blank blueprint
    blueprint = {
        "center": 10.0,
        "parts": [],
        "stages": [],
        "rotation": 0.0,
        "offset": {"x": 0.0, "y": 0.0},
        "interiorView": True
    }

    # Define the scaling factor for the output
    scaling_factor = float(request.form.get("scale-factor"))

    # Extract the black outlines from the image
    draw = ImageDraw.Draw(image)
    width, height = image.size
    pixels = image.load()

    fuel_tank_count = 0

    for y in range(height):
        for x in range(width):
            if pixels[x, y] == 0:  # black pixel
                # Add fuel tank at the position of the black pixel with scaling
                scaled_x = x * scaling_factor
                scaled_y = (height - y - 1) * scaling_factor
                fuel_tank = {
                    "n": "Fuel Tank",
                    "p": {"x": float(scaled_x), "y": float(scaled_y)},
                    "o": {"x": 1.0, "y": 1.0, "z": 0.0},
                    "t": "-Infinity",
                    "N": {
                        "width_original": 2.0,
                        "width_a": 2.0,
                        "width_b": 2.0,
                        "height": 1.0,
                        "fuel_percent": 1.0
                    },
                    "T": {"color_tex": "_", "shape_tex": "_"}
                }
                blueprint["parts"].append(fuel_tank)
                fuel_tank_count += 1

    # Save the modified blueprint to a file
    output_file = os.path.join(output_folder, "blueprint.txt")
    with open(output_file, "w") as f:
        json.dump(blueprint, f, indent=4)

    return f"Modified blueprint saved to {output_file}<br>Total fuel tanks: {fuel_tank_count}"

if __name__ == "__main__":
    app.run()
