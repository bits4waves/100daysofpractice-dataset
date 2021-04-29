import json
import csv
import re
import string
import math
import random

def bool_to_int(b):
    if b:
        return 1
    else:
        return 0

def get_video_view_count(d):
    if d['is_video']:
        return d['video_view_count']
    else:
        return 0

def get_csv_dict(json_dict, owner_ids_dict):
    csv_dict = dict()
    csv_dict['post-id'] = json_dict['id']
    csv_dict['shortcode'] = json_dict['shortcode']
    csv_dict['taken_at_timestamp'] = json_dict['taken_at_timestamp']
    csv_dict['owner-id'] = owner_ids_dict[int(json_dict['owner']['id'])]
    csv_dict['is_video'] = bool_to_int(json_dict['is_video'])
    csv_dict['edge_liked_by-count'] = json_dict['edge_liked_by']['count']
    csv_dict['edge_media_to_comment-count'] = json_dict['edge_media_to_comment']['count']
    csv_dict['video_view_count'] = get_video_view_count(json_dict)
    csv_dict['comments_disabled'] = bool_to_int(json_dict['comments_disabled'])
    csv_dict['__typename'] = json_dict['__typename']
    return csv_dict

def anonymize(data):
    return data

def write_to_csv(csv_file, csv_dict, at_first_line=False,
                 delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL):
    csv_writer = csv.DictWriter(csv_file,
                                csv_dict.keys(),
                                delimiter=delimiter,
                                quotechar=quotechar,
                                quoting=quoting)

    if at_first_line: csv_writer.writeheader()

    csv_writer.writerow(csv_dict)

def get_max_owner_id(json_filename):
    with open(json_filename, 'r', newline='') as json_file:
        max_owner_id = 0
        for line in json_file:
            json_dict = json.loads(line)['_node']
            max_owner_id = max(max_owner_id,
                               int(json_dict['owner']['id']))
    return max_owner_id

def get_owner_ids(json_filename):
    """Return a set with all the owner IDs in posts from ‘json_filename’."""
    with open(json_filename, 'r', newline='') as json_file:
        owner_ids = set()
        for line in json_file:
            json_dict = json.loads(line)['_node']
            owner_ids.add(int(json_dict['owner']['id']))
    return owner_ids


json_filename = 'posts.json'
csv_filename = 'posts.csv'

max_owner_id = get_max_owner_id(json_filename)
anon_chars = string.ascii_uppercase + string.digits
anon_str_len = math.ceil(math.log(max_owner_id, len(anon_chars)))

owner_ids = get_owner_ids(json_filename)
owner_ids_anon = set()
while(len(owner_ids_anon) < len(owner_ids)):
    anon_str = ''.join(random.choices(anon_chars, k=anon_str_len))
    owner_ids_anon.add(anon_str)
owner_ids_dict = dict(zip(owner_ids, owner_ids_anon))

with open(json_filename, 'r', newline='') as json_file, open(csv_filename, 'w', newline='') as csv_file:
    at_first_line = True
    for line in json_file:
        json_dict = json.loads(line)['_node']
        csv_dict = get_csv_dict(json_dict, owner_ids_dict)
        write_to_csv(csv_file, csv_dict, at_first_line)
        if at_first_line: at_first_line = False
