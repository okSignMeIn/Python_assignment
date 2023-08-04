import requests

base_url = "https://jsonplaceholder.typicode.com/posts"

def get_all_posts():
    response = requests.get(base_url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error getting all posts")
        return None

def get_post_by_id(post_id):
    url = f"{base_url}/{post_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error getting post by id")
        return None

def create_post(title, body, user_id):
    data = {
        "title": title,
        "body": body,
        "userId": user_id
    }
    response = requests.post(base_url, json=data)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed")
        return None

def update_post_by_id(post_id, title, body, user_id):
    url = f"{base_url}/{post_id}"
    data = {
        "title": title,
        "body": body,
        "userId": user_id
    }
    response = requests.put(url, json=data)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed")
        return None

def delete_post_by_id(post_id):
    url = f"{base_url}/{post_id}"
    response = requests.delete(url)
    if response.status_code == 200:
        return True
    else:
        print(f"Failed")
        return False
