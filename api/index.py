import requests

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

    print("Response Status:", response.status_code)  # Debugging
    print("Response JSON:", response.json())  # Debugging

    if response.status_code == 200:
        data = response.json().get("data", {}).get("matchedUser")
        if data:
            return data["profile"]["userAvatar"]  # Only return avatar URL

    return None  # Return None if user not found