from youtube_transcript_api import YouTubeTranscriptApi as yta
import urllib.request
import json
import urllib




def transcribe_func(vid_id, title):   
    data = yta.get_transcript(vid_id)
    transcript = ''
    for value in data:
        for key,val in value.items():
            if key == 'text':
                transcript += val
    l = transcript.splitlines()
    final_tra = " ".join(l)
    file = open(f"{title}.doc",'w')
    file.write(final_tra)
    file.close()

def get_title(VideoID):
    params = {"format": "json", "url": "https://www.youtube.com/watch?v=%s" % VideoID}
    url = "https://www.youtube.com/oembed"
    query_string = urllib.parse.urlencode(params)
    url = url + "?" + query_string
    with urllib.request.urlopen(url) as response:
        response_text = response.read()
        data = json.loads(response_text.decode())
        return str(data['title'])





if __name__ == "__main__":

    url_list = ["https://www.youtube.com/watch?v=_YdLLDBwpjk",
"https://www.youtube.com/watch?v=uQIcQaB3ItY",
"https://www.youtube.com/watch?v=Mb5pG5-OkHc",
"https://www.youtube.com/watch?v=hOHpq-vWy3U",
"https://www.youtube.com/watch?v=xPw5VHRdFaQ",
"https://www.youtube.com/watch?v=GB6XAJhUxY8",
"https://www.youtube.com/watch?v=ETZHbYOuk7s"]
    
    try:
        for url in url_list:
            separate = url.split("v=")
            id = str(separate[1])

            # Get video title
            VID_TITLE = get_title(id)

            #get the video subtitle and convert it into .doc file
            transcribe_func(id, VID_TITLE)
    except:
        print("ERROR OCCURED!!!")
    finally:
        print("conversion complete......")
