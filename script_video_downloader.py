import pafy

print("\t\t\t\t#### Welcome to the youtube Downloader ####")
url = input("\t\t\t\tEnter the video link here: ")
url.strip()
print("\n\t\t\t\t*1: Download video without audio.")
print("\t\t\t\t*2: Download audio without video.")
print("\t\t\t\t*3: Download video + audio.")
choice = int(input("\t\t\t\t---- Enter your choice : "))

material = pafy.new(url)
    

#downloading the audio without video
if choice == 2:
    audio_qualities = material.audiostreams
    preference = int(input("\t\t\t\t- If you want to download the best audio quality press '1'\n\t\t\t\t- If you want to download a specific audio quality type '2' : "))
    print("\n")
    if preference == 1:
        s = material.getbestaudio()
        s.download()
    if preference == 2:
        print("\t\t\t\t#### Here is a list of the available qualities: ####")
        for i in audio_qualities:
            print("\t\t\t\t*",i)
        audio_choice = input("\t\t\t\t\t###### resolution: ")  
        j = 0
        for i in audio_qualities:
            if audio_choice in str(i):
                audio_qualities[j].download()
            j = j + 1   

# downloading video wihout audio
elif choice == 1:
    video_qualities = material.videostreams
    preference = int(input("\t\t\t\t- If you want to download the best video quality press '1'\n\t\t\t\t- If you want to download a specific video quality type '2' : "))
    print('\n')
    if preference == 1:
        s = material.getbestvideo()
        s.download()
    if preference == 2:
        print("\t\t\t\t#### Here is a list of the available qualities: ####")
        for i in video_qualities:
            print("\t\t\t\t*",i)
        video_choice = input("\t\t\t\t\t###### resolution: ")
        j = 0
        for i in video_qualities:
            if video_choice in str(i):
                video_qualities[j].download()
            j = j + 1

#downloading the video with audio
else:
    stream = material.streams
    preference = int(input("\t\t\t\t- If you want to download the best video&audio quality press '1'\n\t\t\t\t- If you want to download a specific video&audio quality type '2' : "))
    print('\n')
    if preference == 1:
        s = material.getbest()
        s.download()
    if preference == 2:
        print("\t\t\t\t#### Here is a list of the available qualities: ####")
        for i in stream:
            print("\t\t\t\t*",i)
        stream_choice = input("\t\t\t\t\t###### resolution: ")
        j = 0
        for i in stream:
            if stream_choice in str(i):
                stream[j].download()
            j = j + 1