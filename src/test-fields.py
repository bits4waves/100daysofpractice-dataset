import json                    

"Test if any key besides ‘_node’ has meaningful data."

POST_FILE = "posts-orig.json"
with open(POST_FILE, "r") as posts:
    for line in posts:
        post = json.loads(line)
        for key in post.keys():
            if key != '_node':
                if post[key] is not None:
                    print(post[key])
                
