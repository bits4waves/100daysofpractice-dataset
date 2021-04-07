import argparse

parser = argparse.ArgumentParser()
parser.add_argument('shortcode')
args = parser.parse_args('008-CMh_h-')
print(args.echo)
