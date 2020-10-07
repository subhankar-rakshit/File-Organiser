#!usr/bin/env python3

import os, shutil, sys
from tkinter import *
from tkinter import messagebox as msg
from tkinter import filedialog


dictionary_of_extension={
    'Documents' : ('.pdf','.doc','.xls','txt','.csv','.zip','.xml', '.zip'),
    'Photos' : ('.jpg','.jpeg','.png','.JPG'),
    'Videos' : ('.mp4','.mkv','.3gp','.flv','.mpeg'),
    'Audios' : ('.mp3','.wav','.m4a'),
    'Programs' : ('.py','.cpp','.c','.sh','.js'),
    'App' : ('.exe','.apk'),
}


class rakshit:
    
    def __init__(self,window):
        self.window = window
        window.title("File Separator")
        
        
        #-----------------------------------GUI Design--------------------------

        self.menu = Menu(window)
        self.file = Menu(self.menu, tearoff = 0)
        self.file.add_command(label='Open Folder', command = self.Open_Folder)
        self.file.add_command(label='Exit', command = self.Exit)

        self.help = Menu(self.menu, tearoff = 0)
        self.help.add_command(label='help', command = self.Help_Fuction)
        self.help.add_command(label = 'about', command = self.About_Fuction)


        self.menu.add_cascade(label = 'File', menu = self.file)
        self.menu.add_cascade(label = 'Help', menu = self.help)
        window.config(menu = self.menu)

        # frame-0 for Heading purpose.
        self.frame0 = Frame(window,width=720,height=70)
        Label(self.frame0,text="File Separator", font="lucida 33 bold",bg='violet',padx=22,pady=10).pack()
        Label(self.frame0,text="Devoloped by ./Rakshit", font="lucida 7 bold",bg='lavender').pack()
        self.frame0.pack()
        
        # frame-1 for Label purpose.
        self.frame1 = Frame(window,width=720,height=70)
        self.frame1.pack(pady=10)
        self.frame1.config(bg='dark sea green')

        self.label1 = Label(self.frame1,text = "Choose Folder ",font = "lucidia 18 bold",bg='dark sea green',pady=10)
        self.label1.grid(row = 0, column = 0)

        self.browse_button = Button(self.frame1, text = "Open Folder", command = self.Open_Folder)
        self.browse_button.grid(row = 0, column = 1)

        

        # frame-2 for Button.
        self.frame2 = Frame(window,width=480,height=70)
        self.submit_buttton = Button(self.frame2,text='Click Here', command=self.action)
        self.submit_buttton.pack()
        self.submit_buttton.configure(background='cyan')
        self.frame2.pack()

    def Help_Fuction(self):
        msg.showinfo("Help","Please select the folder that you want to organise and then press the click button and see the magic.")

    def About_Fuction(self):
        msg.showinfo('About Me','Developed by ./Rakshit')


    def Open_Folder(self):
        self.browse_folder = filedialog.askdirectory()

        self.create_label()

    def create_label(self):
        self.label2 = Label(self.frame1, text = self.browse_folder, bg='dark sea green')
        self.label2.grid(row = 0, column = 2, padx = 10)
        
       
    def Exit(self):
        window.destroy()
        
    def file_finder(self,folder_path,file_extensions):
        self.files = []
        for file in os.listdir(folder_path):
            for extension in file_extensions:
                if file.endswith(extension):
                    self.files.append(file)
        return self.files
        # return [file for file in os.listdir(folder_path) for extension in file_extensions if file.endswith(extension)]


    def action(self):
        self.cur_folder_path = self.browse_folder
        
        if os.path.exists(self.cur_folder_path):
            self.folder_list1 = []
            self.folder_list2 = []
            self.counter = 0
            for extension_type, extension_list in dictionary_of_extension.items():

                self.folder_name = extension_type
                self.folder_path = os.path.join(self.cur_folder_path,self.folder_name)

                os.chdir(self.cur_folder_path)

            #--------------------------------------------------------------------------

                if os.path.exists(self.folder_name):
                    self.folder_list1.append(self.folder_name)
                else:
                    self.folder_list2.append(self.folder_name)
                    os.mkdir(self.folder_path)
                    
            #--------------------------------------------------------------------------

                for item in self.file_finder(self.cur_folder_path,extension_list):
                    self.item_path = os.path.join(self.cur_folder_path,item)
                    self.item_new_path = os.path.join(self.folder_path,item)
                    shutil.move(self.item_path,self.item_new_path)
                    self.counter+=1

            # -------------------------------Frame-3-----------------------------
            self.frame3 = Frame(window,width=720,height=70)
            Label(self.frame3,text = f"{self.folder_list1} These folders are already presented.",font=('Helvetica', 14),bg='dark sea green',pady=5).pack(side='left')
            self.frame3.pack(anchor='w',pady=15)

            # -------------------------------Frame-4-----------------------------
            self.frame4 = Frame(window,width=720,height=70)
            Label(self.frame4,text = f"{self.folder_list2} Newly Created Folder.",font=('Helvetica', 14),bg='dark sea green',pady=5).pack(side='left')
            self.frame4.pack(anchor='w',pady=15)

        else:
            msg.showerror('Error','Please enter a valid path!')
            # self.entry_box.delete(0,'end')
        
        if self.counter!=0:
            msg.showinfo('Done!','File has been separated.')

       

# Window options.
window =Tk()
window.config(bg='dark sea green')  
window.geometry("900x500")

obj = rakshit(window)
window.mainloop()
sys.exit(0)