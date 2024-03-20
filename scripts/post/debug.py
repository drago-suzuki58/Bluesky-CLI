def print_post(posts):
    print(posts)
    with open('log/post_debug.log', 'w') as f:
        f.write(posts)