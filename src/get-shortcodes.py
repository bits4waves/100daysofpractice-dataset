import instaloader
import time
import os

I = instaloader.Instaloader()
query = instaloader.Hashtag.from_name(I.context, '100daysofpractice')
k = 1
for post in query.get_all_posts():
    print(k)
    shortcode = post.shortcode
    print(shortcode)
    with open('shortcodes-orig.txt', 'a') as file_object:
        file_object.write(shortcode + '\n')
    time.sleep(1)
    k += 1
