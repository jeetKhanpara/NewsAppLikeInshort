import requests
import webbrowser
from tkinter import * 
from urllib.request import urlopen
from PIL import ImageTk,Image
import io

class NewsApp:

    def __init__(self) -> None:

        #fatch the data
        self.data = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=f7fae98b4ae14c0aaacb9683785b93be").json()
        # print(self.data)

        #load the gui
        self.load_gui()

        #load the 1st news item
        self.load_news_item(0)


    def load_gui(self):
        self.root = Tk()
        self.root.geometry('350x600')
        self.root.resizable(0,0)
        self.root.configure(background='black')
        self.root.title('TheNewsNew')

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def open_link(self,url):
        webbrowser.open(url)   

    def load_news_item(self,index):
        #clear the screen for new news item
        self.clear() 

        #image loading
        try:
            img_url =  self.data['articles'][index]['urlToImage'] 
            raw_data = urlopen(img_url).read() 
            im =  Image.open(io.BytesIO(raw_data)).resize((350,250))
            photo = ImageTk.PhotoImage(im)

            label = Label(self.root,image=photo)
            label.pack()
        except:
            img_url =  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRh6n0Q3H_HR7BWc67gTgXwYHOcXBWGO8gKNtJBxnEkwxRgd-4LCdxPdPEsxHufQnFzEjQ&usqp=CAU" 
            raw_data = urlopen(img_url).read() 
            im =  Image.open(io.BytesIO(raw_data)).resize((350,250))
            photo = ImageTk.PhotoImage(im)

            label = Label(self.root,image=photo)
            label.pack()


        #heading of the news
        heading = Label(self.root,text=self.data['articles'][index]['title'],bg='black',fg='white',wraplength=350,justify='center')
        heading.pack(pady=(10,20))  #neccessory
        heading.config(font=('verdana',15))

        #Details for that perticular news
        details = Label(self.root,text=self.data['articles'][index]['description'],bg='black',fg='white',wraplength=350,justify='center')
        details.pack(pady=(5,20))  #neccessory
        details.config(font=('verdana',12))

        #frame all previous,read_more and next buttons
        frame = Frame(self.root,bg='black')
        frame.pack(expand=True,fill=BOTH)

        if index != 0:
            prev = Button(frame,text='prev',width=15,height=3,command=lambda :self.load_news_item(index-1))
            prev.pack(side=LEFT)

        read_more = Button(frame,text='read_more',width=15,height=3,command=lambda :self.open_link(self.data['articles'][index]['url']))
        read_more.pack(side=LEFT)

        if index != (len(self.data['articles'])-1):
            next = Button(frame,text='next',width=15,height=3,command=lambda :self.load_news_item(index+1))
            next.pack(side=LEFT)

        self.root.mainloop()



     

obj1 = NewsApp()