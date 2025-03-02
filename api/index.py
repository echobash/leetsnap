from flask import Flask, send_file
from PIL import Image, ImageDraw, ImageFont
import io


app = Flask(__name__)
@app.route("/")

def generate_image():
    # Create a blank image with white background
    img = Image.new('RGB', (400, 200), color=(255, 255, 255))

    draw = ImageDraw.Draw(img)
    text = "LeetSnap is Live!"

    # Draw text (you may need to adjust font size)
    draw.text((50, 80), text, fill=(0, 0, 0))

    # Save image to a BytesIO object
    img_io = io.BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)

    return send_file(img_io, mimetype='image/png')


if __name__ == "__main__":
    app.run(debug=True)