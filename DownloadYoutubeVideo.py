from pytube import YouTube


def download(video_url):
    youtube_object = YouTube(video_url)
    youtube_object = youtube_object.streams.get_highest_resolution()
    try:
        youtube_object.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")


link = input("Enter the YouTube video URL:\n")
print("downloading...")
download(link)
print("Done! Check the folder where this script is located, and you should see the downloaded video.")
input("Press Enter to finish.")
