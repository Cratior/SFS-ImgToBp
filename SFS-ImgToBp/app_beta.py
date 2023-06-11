import os
import json
from flask import Flask, render_template, request
from PIL import Image
import numpy as np

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
    return render_template('index_beta.html')

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
    black_pixels = np.argwhere(np.array(image) == 0)
    fuel_tank_count = 0
    outer_tank_width = 0.5
    outer_tank_height = 0.5
    border_tank_width = 1.0
    border_tank_height = 1.0
    spacing = -0.3  # Adjust the spacing between tanks

    for pixel in black_pixels:
        x, y = pixel
        scaled_x = x * scaling_factor
        scaled_y = (image.size[1] - y - 1) * scaling_factor

        fuel_tank_width = border_tank_width
        fuel_tank_height = border_tank_height

        # Calculate the required width and height based on context
        context_width, context_height = get_context_dimensions(image, x, y)

        if context_width > border_tank_width:
            fuel_tank_width = context_width
        if context_height > border_tank_height:
            fuel_tank_height = context_height

        # Check for overlapping fuel tanks and remove or move them
        is_overlapping = False
        for existing_tank in blueprint["parts"]:
            existing_x = existing_tank["p"]["x"]
            existing_y = existing_tank["p"]["y"]
            existing_width = existing_tank["N"]["width_original"]
            existing_height = existing_tank["N"]["height"]

            if (
                scaled_x <= existing_x + existing_width + spacing and
                scaled_x + fuel_tank_width + spacing >= existing_x and
                scaled_y <= existing_y + existing_height + spacing and
                scaled_y + fuel_tank_height + spacing >= existing_y
            ):
                is_overlapping = True
                break

        if not is_overlapping:
            fuel_tank = {
                "n": "Fuel Tank",
                "p": {"x": float(scaled_x), "y": float(scaled_y)},
                "o": {"x": 1.0, "y": 1.0, "z": 0.0},
                "t": "-Infinity",
                "N": {
                    "width_original": int(fuel_tank_width),
                    "width_a": int(fuel_tank_width),
                    "width_b": int(fuel_tank_width),
                    "height": int(fuel_tank_height),
                    "fuel_percent": 0.0
                },
                "T": {"color_tex": "", "shape_tex": ""}
            }

            blueprint["parts"].append(fuel_tank)
            fuel_tank_count += 1

    # Rotate the blueprint to the right by 90 degrees
    blueprint["rotation"] = -90.0

    # Save the modified blueprint to a file
    output_file = os.path.join(output_folder, "blueprint.txt")
    with open(output_file, "w") as f:
        json.dump(blueprint, f, indent=4, default=lambda x: int(x))

    # Return the fuel tank count as part of the response
    return f"Modified blueprint saved to {output_file}. Total fuel tanks: {fuel_tank_count}"


def get_context_dimensions(image, x, y):
    # Set the required margin for context
    margin = 3

    width, height = image.size
    context_width = 0
    context_height = 0

    # Check if the pixel is within the image dimensions
    if x < 0 or x >= width or y < 0 or y >= height:
        return context_width, context_height

    # Calculate the maximum width and height based on surrounding black pixels
    for i in range(max(x - margin, 0), min(x + margin + 1, width)):
        for j in range(max(y - margin, 0), min(y + margin + 1, height)):
            if image.getpixel((i, j)) == 0:  # Check if neighboring pixel is black
                context_width = max(context_width, abs(x - i))
                context_height = max(context_height, abs(y - j))

    return context_width, context_height


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080)
