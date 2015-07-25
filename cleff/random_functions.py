

# youtube code grabber from url
# must pass in url as a string
# function returns youtube video id

def youtube_code_getter(youtube_vide_url):
    x = str(youtube_vide_url).rsplit(sep='?v=')
    return x[1]