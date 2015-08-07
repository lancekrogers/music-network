

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


'''

JQUERY Examples

$(document).ready(function() {
   $('div').mouseenter(function() {
       $(this).animate({
           height: '+=10px'
       });
   });
   $('div').mouseleave(function() {
       $(this).animate({
           height: '-=10px'
       });
   });
   $('div').click(function() {
       $(this).toggle(1000);
   });
});


def inflation(x,y):
    i = x
    for a in range(y):
        b = i * .025
        i = i + b
    return i



{% extends 'profiles/base.html' %}
{% block body %}

<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>
    <form method="POST" action="">
        {% csrf_token %}
        {{ form.media }}
        {{ form.as_p }}
    <input type="submit" value="Add Location">
    </form>

elasticsearch -d -Des.config=/Users/lancerogers/Library/ElasticSearch/elasticsearch.yml

{% endblock %}

'''