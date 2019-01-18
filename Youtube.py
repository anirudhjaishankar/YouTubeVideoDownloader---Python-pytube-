import tkinter as tk
from pytube import YouTube


app = tk.Tk();
l = tk.Label(text='Enter Video URL: ')
e = tk.Entry(app);
def getDetails():
    global e
    url = e.get()
    try:
        yt = YouTube(url)
        print(yt.title)
        x = yt.streams.filter(res='720p').first()
        print("Now Downloading "+ yt.title)
        print(x.filesize)
        x.download()
    except Exception as exp:
        print("ErrorDownloadVideo  |  " + str(url))
        print(exp)

b = tk.Button(text = 'Download',command = getDetails)
l.pack()
e.pack()
b.pack()
app.mainloop()
