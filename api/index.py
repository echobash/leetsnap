import requests
from flask import Flask, send_file, request
from PIL import Image, ImageDraw, ImageFont
import io

app = Flask(__name__)

LEETCODE_API_URL = "https://leetcode.com/graphql"


def fetch_leetcode_data(username):
    """Fetch LeetCode user stats using GraphQL API."""
    query = """
    query getUserProfile($username: String!) {
      matchedUser(username: $username) {
        profile {
          userAvatar
        }
        submitStatsGlobal {
          acSubmissionNum {
            count
          }
        }
        ranking {
          ranking
        }
      }
    }
    """

    response = requests.post(
        LEETCODE_API_URL,
        json={"query": query, "variables": {"username": username}},
        headers={"Content-Type": "application/json"}
    )

    if response.status_code == 200:
        data = response.json().get("data", {}).get("matchedUser")
        if data:
            return {
                "total_solved": data["submitStatsGlobal"]["acSubmissionNum"][0]["count"],
                "ranking": data["ranking"]["ranking"],
                "avatar": data["profile"]["userAvatar"]
            }

    return None  # Return None if user not found


@app.route("/")
def generate_image():
    username = request.args.get("username", "echobash")  # Get username from query params

    user_data = fetch_leetcode_data(username)
    if not user_data:
        return "LeetCode user not found", 404

    # Create a blank image
    img = Image.new("RGB", (500, 250), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Load a default font
    try:
        font = ImageFont.truetype("arial.ttf", 24)  # Works on Windows
    except:
        font = ImageFont.load_default()  # Use default font if unavailable

    # Draw text
    draw.text((20, 50), f"User: {username}", fill="black", font=font)
    draw.text((20, 100), f"Total Solved: {user_data['total_solved']}", fill="black", font=font)
    draw.text((20, 150), f"Ranking: {user_data['ranking']}", fill="black", font=font)

    # Save image to a BytesIO object
    img_io = io.BytesIO()
    img.save(img_io, "PNG")
    img_io.seek(0)

    return send_file(img_io, mimetype="image/png")


if __name__ == "__main__":
    app.run(debug=True)
