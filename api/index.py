from flask import Flask, request, jsonify
import requests
from mangum import Mangum  # ✅ Required for Vercel

app = Flask(__name__)

LEETCODE_API_URL = "https://leetcode.com/graphql"

def fetch_leetcode_avatar(username):
    """Fetch LeetCode user avatar using GraphQL API."""
    query = """
    query getUserProfile($username: String!) {
      matchedUser(username: $username) {
        profile {
          userAvatar
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
            return data["profile"]["userAvatar"]

    return None  # Return None if user not found

@app.route("/")
def get_avatar():
    username = request.args.get("username", "default_user")  # Get username from query params
    avatar_url = fetch_leetcode_avatar(username)

    if not avatar_url:
        return jsonify({"error": "LeetCode user not found"}), 404

    return jsonify({"avatar": avatar_url})  # Return JSON response

# ✅ Required for Vercel
handler = Mangum(app)

if __name__ == "__main__":
    app.run(debug=True)
