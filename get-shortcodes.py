import instaloader
import time
import os

I = instaloader.Instaloader()
I.interactive_login(os.getenv('IG_USER'))
query = instaloader.Hashtag.from_name(I.context, "100daysofpractice")
k = 1
for post in query.get_all_posts():
    print(k)
    with open("shortcodes.txt", "a") as file_object:
        file_object.write(post.shortcode + "\n")
    time.sleep(1)
    k += 1
