

# youtube code grabber from url
# must pass in url as a string
# function returns youtube video id

def youtube_code_getter(youtube_vide_url):
    x = str(youtube_vide_url).rsplit(sep='?v=')
    return x[1]

'''

djinja form to put on public profiles and videos

<form action="{% url 'message:start_music_talk' request.user.musician.pk %}" method="POST">
{% csrf_token %}
<input type="submit" value="Start conversation" >
</form>


geolocation javascript

'''
'''
<script type="text/javascript">
    $(window).load(function(){
        if(navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(function(position) {
                $.ajax({
                    data: ({
                        action: 'geolocation_cache',
                        ip: "99.95.152.28",
                        latitude: position.coords.latitude,
                        longitude: position.coords.longitude
                    }),
                    success: function() {}
                });
            });
        }
    });
    </script>


    '''