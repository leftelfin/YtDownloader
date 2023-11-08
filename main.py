from pytube import YouTube

try:
    # get the youtube URL
    url = input("Enter the YouTube URL: ")
    
    YT = YouTube(url)
    
    print("Title:", YT.title)
    print("Views:", YT.views)

    
    YTDnl = YT.streams.get_highest_resolution()
    
    # Download the video to the current directory
    YTDnl.download()
    
    print("Download commenced successfully.")
except Exception as excp:
    print("Error:", str(excp))