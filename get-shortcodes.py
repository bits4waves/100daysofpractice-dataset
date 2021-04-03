import instaloader

L = instaloader.Instaloader()
hashtag = Hashtag.from_name(L.context, "100daysofpractice")
for post in hashtag.get_posts():
    with open("shortcode.txt") as file_object:
        file_object.write(post.shortcode + "\n")
    input()
