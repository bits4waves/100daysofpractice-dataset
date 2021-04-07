import argparse
import instaloader

parser = argparse.ArgumentParser()
parser.add_argument('shortcode')
args = parser.parse_args()

I = instaloader.Instaloader()
post = instaloader.Post.from_shortcode(I.context, args.shortcode)
print(post.owner_profile.username)
