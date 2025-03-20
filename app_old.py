import threading
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk,Image
#define global variables
global start_screen
global login_screen
global progress_bar
global result_label
global username_entry
global password_entry
global start_button
global selected_file
global select_button
global filename_label

#display the start page
def show_start_page():
    global start_screen
   # global login_screen
    global progress_bar
    global result_label
   # global username_entry
   # global password_entry
    global start_button
    #global selected_file
    global select_button
    global filename_label
    #create the start page
    start_screen = tk.Tk()
    start_screen.title('software')
    start_screen.geometry('500x500')
    page1=tk.Frame(start_screen)
    page2=tk.Frame(start_screen)
    page1.pack()
  
    #word label
    title_label = tk.Label(page1, text="DDOS analysis kit",font=('Arial',18))
    title_label.pack()
    result_label = tk.Label(page2,text="Results",font=("Arial",12))
    result_label.pack()
    filename_label = tk.Label(page1, text='', font=('Arial',12))
    filename_label.pack()


    #Image label
    img=Image.open("ddos1.png")
    image=ImageTk.PhotoImage(img)
    image_label = tk.Label(page1, image=image)
    image_label.pack()

    #progress bar
    progress_bar = ttk.Progressbar(page1,orient='horizontal',length=300)
    progress_bar.pack()

    #text area
    text_area = tk.Text(page2,height=5,width=52)
    text_area.pack()
    #upload function
    def upload(event=None):
        filename = filedialog.askopenfilename()
        pth= filename
        return pth
    # switch function
    def switchpage1():
           page1.pack_forget()
           page2.pack() 
    def switchpage2():
           page2.pack_forget()
           page1.pack()  
    #buttons
    select_button = tk.Button(page1,text='Click To Upload',command=upload,font=('Arial',12))
    select_button.pack()
    start_button = tk.Button(page1,text='Send Requests',font=('Arial',12))
    start_button.pack()
    switch_button = tk.Button(page1,text='switch to results', font=('Arial',12),command=switchpage1)
    switch_button.pack()
    switch2=tk.Button(page2,text='switch back to main page', font=('Arial',12),command=switchpage2)
    switch2.pack()
    #mainloop
    start_screen.mainloop()

#generate subtitle, quiz and extract words
def generate():
    pass

def select_file():
    global selected_file
    global select_button
    global filename_label

    result_label.config(text='')
    filename_label.config(text='')
    selected_file = filedialog.askopenfilename()
    
    if select_file:
         filename_label.config(text=selected_file)

def start_analysis():
        global selected_file
        global progress_bar
        global result_label
        global select_button
        global start_button

        if select_file:
            result_label.config(text='Sending Request')
            select_button.pack_forget()
            start_button.pack_forget()
            progress_bar.pack(pady=10)
            progress_bar.start()
            #start analysis

def complete_analysis(data_list,prediction):
     global progress_bar
     global result_label
     global select_button
     global start_button
     
     progress_bar.stop()
     progress_bar.pack_forget()
     #result_label.config(text=prediction)
     filename_label.config(text=str(data_list)[:-1])
     select_button.pack(pady=10)
     start_button.pack()


#packing the frames in the window

if __name__ == '__main__':
    show_start_page()
