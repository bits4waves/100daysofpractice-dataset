import json
import csv
import re

def bool_to_int(b):
    if b:
        return 1
    else:
        return 0

def get_video_count(d):
    if d['is_video']:
        return d['video_view_count']
    else:
        return 0


JSON_FILE = 'posts.json'
CSV_FILE = 'posts.csv'
with open(JSON_FILE, 'r', newline='') as json_file, open(CSV_FILE, 'w', newline='') as csv_file:
    at_firstline = True
    for line in json_file:
        json_dict = json.loads(line)['_node']
        csv_dict = dict()
        csv_dict['id'] = json_dict['id']
        csv_dict['shortcode'] = json_dict['shortcode']
        csv_dict['taken_at_timestamp'] = json_dict['taken_at_timestamp']
        csv_dict['owner-id'] = json_dict['owner']['id']
        csv_dict['is_video'] = bool_to_int(json_dict['is_video'])
        csv_dict['edge_liked_by-count'] = json_dict['edge_liked_by']['count']
        csv_dict['edge_media_to_comment-count'] = json_dict['edge_media_to_comment']['count']
        csv_dict['video_view_count'] = get_video_count(json_dict)
        csv_dict['comments_disabled'] = bool_to_int(json_dict['comments_disabled'])
        csv_dict['__typename'] = json_dict['__typename']

        csv_writer = csv.DictWriter(csv_file,
                                    csv_dict.keys(),
                                    delimiter=',',
                                    quotechar='"',
                                    quoting=csv.QUOTE_ALL)

        if at_firstline:
            csv_writer.writeheader()
            at_firstline = False

        csv_writer.writerow(csv_dict)
