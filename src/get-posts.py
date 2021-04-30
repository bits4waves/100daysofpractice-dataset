import os
import instaloader
import json

POST_FILE = "posts-orig.json"
HASHTAG = "100daysofpractice"
IG_USER = os.getenv("IG_USER")

L = instaloader.Instaloader(fatal_status_codes=[400, 429])
L.load_session_from_file(IG_USER)

# Resumable iterator for recent hashtag posts, from #874.
hashtag_posts = instaloader.NodeIterator(
    context=L.context,
    query_hash="9b498c08113f1e09617a1703c22b2f32",
    edge_extractor=lambda d: d["data"]["hashtag"]["edge_hashtag_to_media"],
    node_wrapper=lambda n: instaloader.Post(L.context, n),
    query_variables={"tag_name": HASHTAG},
    query_referer=f"https://www.instagram.com/explore/tags/{HASHTAG}/",
)

with open(POST_FILE, "a") as file:
    with instaloader.resumable_iteration(
            context=L.context,
            iterator=hashtag_posts,
            load=instaloader.load_structure_from_file,
            save=instaloader.save_structure_to_file,
            format_path=lambda magic: f"resume_info_{magic}.json.xz",
    ) as (is_resuming, start_index):
        if is_resuming:
            # After resuming, the first post is the last post that had been returned in
            # the previous iteration. Here we avoid that this post shortcode is
            # repeated.
            next(hashtag_posts)
            # Here we write all shortcodes to the file
        for post in hashtag_posts:
            postdict = vars(post)
            del postdict['_context'] # json can't process this key (and we don't need it)
            print(json.dumps(postdict), file=file)
