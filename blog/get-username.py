import argparse

parser = argparse.ArgumentParser()
parser.add_argument('shortcode')
args = parser.parse_args()
print(args.echo)
