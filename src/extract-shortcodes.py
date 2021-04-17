import json                    

# The idea is to parse the JSON strings in =posts-orig.json=, grab the shortcode from it, and append it to =shortcodes.txt=.
# First, let’s open it and print the first shortcode:

POST_FILE = "posts-orig.json"
SHORTCODE_FILE = "shortcodes.txt"
with open(POST_FILE, "r") as posts, open(SHORTCODE_FILE, "a") as shortcodes:
    for line in posts:
        shortcode = json.loads(line)['_node']['shortcode']
        print(shortcode, file=shortcodes)
