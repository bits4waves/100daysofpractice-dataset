import argparse
import os
import instaloader

parser = argparse.ArgumentParser()
parser.add_argument('shortcode')
args = parser.parse_args()

I = instaloader.Instaloader()
I.login(os.getenv('IG_USER'), os.getenv('IG_PASSWORD'))
post = instaloader.Post.from_shortcode(I.context, args.shortcode)
print(post.owner_profile.username)
