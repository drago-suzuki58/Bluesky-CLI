def print_profile(profile):
    print(profile)
    with open('log/profile_debug.log', 'w') as f:
        f.write(profile)

def print_followers(followers):
    print(followers)
    with open('log/followers_debug.log', 'w') as f:
        f.write(followers)

def print_following(following):
    print(following)
    with open('log/following_debug.log', 'w') as f:
        f.write(following)