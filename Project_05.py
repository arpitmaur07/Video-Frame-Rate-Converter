from tkinter import *
from tkinter.filedialog import askopenfile
import cv2

root = Tk()
root.title("Video Player in Different FPS")
root.geometry("860x550")
root.minsize(860,500)
root.configure(bg="#116562")
fps=StringVar()


def select():
    video = askopenfile(mode='r', filetypes=[('Video Files', ["*.mp4",'*.avi'])])
    if video is not None:
        lbl3.pack_forget()
        lbl4.pack(pady=20)
        b1['state'] = DISABLED
        b1['bg'] = 'white'   
        global videoName
        videoName = video.name
        global cap
        cap = cv2.VideoCapture(videoName)
        global frameTime
        # frameTime=int(10)        

def play():
    x=int(fps.get())
    if(x>100 or x<=0):
        frameTime=None
    else:    
        frameTime=101-int(fps.get())  
    if frameTime==None:
        print("Please select FPS between '1 to 100'.")
        
    else:
        while(cap.isOpened()):
            ret, frame = cap.read()
            cv2.imshow('Video Player',frame)
            if cv2.waitKey(frameTime) & 0xFF == ord('q'):
                break
        # cap.release()
        cv2.destroyAllWindows()
def fps_10():
    frameTime=100-10
    while(cap.isOpened()):
        ret, frame = cap.read()
        cv2.imshow('Video Player',frame)
        if cv2.waitKey(frameTime) & 0xFF == ord('q'):
            break
    # cap.release()
    cv2.destroyAllWindows()
    
    
def fps_30():
    frameTime=100-30
    while(cap.isOpened()):
        ret, frame = cap.read()
        cv2.imshow('Video Player',frame)
        if cv2.waitKey(frameTime) & 0xFF == ord('q'):
            break
    # cap.release()
    cv2.destroyAllWindows()
def fps_60():
    frameTime=100-60
    while(cap.isOpened()):
        ret, frame = cap.read()
        cv2.imshow('Video Player',frame)
        if cv2.waitKey(frameTime) & 0xFF == ord('q'):
            break
    # cap.release()
    cv2.destroyAllWindows()

def fps_90():
    frameTime=100-90
    while(cap.isOpened()):
        ret, frame = cap.read()
        cv2.imshow('Video Player',frame)
        if cv2.waitKey(frameTime) & 0xFF == ord('q'):
            break
    # cap.release()
    cv2.destroyAllWindows()

def exitWindow():
    root.destroy()    
    root.quit()

lbl1 = Label(root, text="Video Player in Different Frame Rates",fg="white",bg='#4a7abc', font="none 25 bold")
lbl1.config(anchor=CENTER)
lbl1.pack(fill='x')

lbl3 = Label(root,text="Click on 'Select Video' button and select video you want to play.",font="none 12 bold",bg='#116562',fg='white')
lbl3.config(anchor=CENTER)
lbl3.pack(pady=20)    


lbl4 = Label(root,text="You selected the video. Choose a FPS or enter manualy( Between '1 To 100').\nPress 'q' for quit video window.",font="none 14 ",bg='#116562',fg='white')
lbl4.config(anchor=CENTER)

lbl2 = Label(root,bg='#4a7abc')
lbl2.config(anchor=CENTER)
lbl2.pack(side=BOTTOM,fill='x',)


b1 = Button(lbl2, text='Select Video',font="none 10",bg='#4A7A8C',fg='white',activebackground='white',state=NORMAL,activeforeground='#4A7A8C',width=10,command=select)
b1.pack(side=LEFT,padx=10, pady=5,anchor="w")

fps_name_label = Label(lbl2, text = 'Enter Custom FPS',height=2,width=14,bg='#4a7abc',fg='white',font="none 12")
fps_name_label.pack(side=LEFT,padx=10, pady=5,anchor="w")
fps_name_entry = Entry(lbl2,textvariable = fps,width=4)
fps_name_entry.pack(side=LEFT,padx=10, pady=5,anchor="w")

b2 = Button(lbl2, text='PLAY',bg='green',fg='white',font="none 10 ",activebackground='white',activeforeground='green',width=9,command=play)
b2.pack(side=LEFT,padx=10, pady=5,anchor="w")

b7 = Button(lbl2, text='1/10',bg='#116562',fg='white',font="none 10",activebackground='white',activeforeground='#116562' ,width=7,command=fps_10)
b7.pack(side=LEFT,padx=10, pady=5,anchor="w")

b3 = Button(lbl2, text='1/30',bg='#116562',fg='white',font="none 10",activebackground='white',activeforeground='#116562' ,width=7,command=fps_30)
b3.pack(side=LEFT,padx=10, pady=5,anchor="w")

b4 = Button(lbl2, text='1/60',bg='#116562',fg='white',font="none 10",activebackground='white',activeforeground='#116562' ,width=7,command=fps_60)
b4.pack(side=LEFT,padx=10, pady=5,anchor="w")

b5 = Button(lbl2, text='1/90',bg='#116562',fg='white',font="none 10",activebackground='white',activeforeground='#116562' ,width=7,command=fps_90)
b5.pack(side=LEFT,padx=10, pady=5,anchor="w")

b6 = Button(lbl2, text='EXIT',bg='red',fg='white',font="none 10 bold",activebackground='white',activeforeground='red',width=9, command=exitWindow)
b6.pack(side=LEFT,padx=10, pady=5,anchor="w")
root.mainloop()