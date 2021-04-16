import json
import csv

POSTS_JSON = "posts.json"
POSTS_CSV = "posts.csv"
with open(POSTS_JSON, "r") as postsjson, open(POSTS_CSV, "w") as postscsv:
    atfirstline = True
    for linejson in postsjson:
        postdict = json.loads(linejson)['_node']
        csvwriter = csv.DictWriter(postscsv, postdict.keys())
        if atfirstline:
            csvwriter.writeheader()
            atfirstline = False
        csvwriter.writerow(postdict)

