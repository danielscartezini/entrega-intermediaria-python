import requests

def fetch_posts():
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts")
        response.raise_for_status()  # Raise an exception for HTTP errors
        posts = response.json()
        for post in posts[:5]: # Display first 5 posts
            print(f"Title: {post['title']}\nBody: {post['body']}\n---\n")
        return posts
    except requests.exceptions.RequestException as e:
        print(f"Error fetching posts: {e}")
        return None

if __name__ == "__main__":
    print("Fetching posts from JSONPlaceholder...")
    fetch_posts()
