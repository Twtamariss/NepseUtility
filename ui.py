import tkinter as tk
import tkinter.font as tkFont
import scraper
from broadcast import play
from time import sleep
from _thread import start_new_thread
import pickle
from splitter import split
tasks = {}
running = False

def cheakupdate(a,b):
    while running:
        global tasks
        string = ''
        try:
            scrap = scraper.scrape()
            scrap.refresh()
        except:
            play("Connection Problem")
            print("Error loading website maybe connection problem")
        message = ''
        app.GMessage_706['text'] = ''
        for key in list(tasks.keys()):
            print(str(key))
            tuple_cash = tasks[str(key)]
            x = scrap.get_addr(str(key))
            print(x)
            if x != None:    
                price = scrap.get_content(int(x),2)  
                print(price)
                print("______")
                if (float(tuple_cash[0]) - float(price)) >= 0:
                    message_c = f"Alert {split(str(key))} is available at {price} to buy" + f"Alert {split(str(key))} is available at {price} to buy"
                    message = message + message_c
                    app.GMessage_706['text'] = app.GMessage_706['text'] + f"Alert {str(key)} at {price} Buy?"
                if (float(tuple_cash[1]) - float(price)) <= 0:
                    message_c = f"Alert {split(str(key))} is available at {price} to sell" + f"Alert {split(str(key))} is available at {price} to sell"
                    message = message + message_c
                    app.GMessage_706['text'] = app.GMessage_706['text'] + f"Alert {str(key)} at {price} sell?"
                string = string + f"{str(key)} is at {price}\n"
            else:
                
                string = string + f"{str(key)} is not available\n"
                
            try:
                app.GMessage_810['text'] = string
            
            except IndexError:
                play('index error')
            
        if app.GLineEdit_931.get() == '':
            t = 10
        else:
            try:
                t = int(app.GLineEdit_931.get())
            except:
                print("time cannot be in floats")
                t = 10 
        play(message)  
        sleep(t)
        if running:
            pass
        else:
            print('process stopped')
            play('process stopped')
            break




    

def msg():
    global tasks
    string = ''
    for key in list(tasks.keys()):
        tuple_cash = tasks[str(key)]
        string = string + f"{str(key)} in b {tuple_cash[0]} s {tuple_cash[1]}\n"
    return string

class App:
    def __init__(self, root):
        #setting title
        root.title("Trader Assist")
        root.iconbitmap('trash_empty_ico.ico')
        #setting window size
        width=800
        height=600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.GLabel_340=tk.Label(root)
        self.GLabel_340["bg"] = "#90f090"
        self.ft = tkFont.Font(family='Times',size=12)
        self.GLabel_340["font"] = self.ft
        self.GLabel_340["fg"] = "#333333"
        self.GLabel_340["justify"] = "center"
        self.GLabel_340["text"] = "Refresh Time"
        self.GLabel_340.place(x=90,y=50,width=152,height=43)

        self.GLineEdit_931=tk.Entry(root)
        self.GLineEdit_931["bg"] = "#c2c2c2"
        self.GLineEdit_931["borderwidth"] = "1px"
        self.ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_931["font"] = self.ft
        self.GLineEdit_931["fg"] = "#000000"
        self.GLineEdit_931["justify"] = "center"
        self.GLineEdit_931["text"] = "10"
        self.GLineEdit_931.place(x=250,y=60,width=70,height=25)

        self.GButton_96=tk.Button(root)
        self.GButton_96["bg"] = "#009688"
        self.ft = tkFont.Font(family='Times',size=10)
        self.GButton_96["font"] = self.ft
        self.GButton_96["fg"] = "#000000"
        self.GButton_96["justify"] = "center"
        self.GButton_96["text"] = "Start"
        self.GButton_96.place(x=80,y=460,width=70,height=25)
        self.GButton_96["command"] = self.GButton_96_command

        self.GButton_9sav=tk.Button(root)
        self.GButton_9sav["bg"] = "#1ab2ff"
        self.ft = tkFont.Font(family='Times',size=10)
        self.GButton_9sav["font"] = self.ft
        self.GButton_9sav["fg"] = "#000000"
        self.GButton_9sav["justify"] = "center"
        self.GButton_9sav["text"] = "Save"
        self.GButton_9sav.place(x=80,y=550,width=70,height=25)
        self.GButton_9sav["command"] = self.GButton_9sav_command

        self.GButton_9load=tk.Button(root)
        self.GButton_9load["bg"] = "#1ab2ff"
        self.ft = tkFont.Font(family='Times',size=10)
        self.GButton_9load["font"] = self.ft
        self.GButton_9load["fg"] = "#000000"
        self.GButton_9load["justify"] = "center"
        self.GButton_9load["text"] = "Load"
        self.GButton_9load.place(x=200,y=550,width=70,height=25)
        self.GButton_9load["command"] = self.GButton_9load_command

        self.GButton_656=tk.Button(root)
        self.GButton_656["bg"] = "#f54545"
        self.ft = tkFont.Font(family='Times',size=10)
        self.GButton_656["font"] = self.ft
        self.GButton_656["fg"] = "#000000"
        self.GButton_656["justify"] = "center"
        self.GButton_656["text"] = "Stop"
        self.GButton_656.place(x=200,y=460,width=70,height=25)
        self.GButton_656["command"] = self.GButton_656_command

        self.GCheckBox_677=tk.Checkbutton(root)
        self.ft = tkFont.Font(family='Times',size=10)
        self.GCheckBox_677["font"] = self.ft
        self.GCheckBox_677["fg"] = "#333333"
        self.GCheckBox_677["justify"] = "center"
        self.GCheckBox_677["text"] = "Sounds"
        self.GCheckBox_677.place(x=300,y=240,width=70,height=25)
        self.GCheckBox_677["offvalue"] = "0"
        self.GCheckBox_677["onvalue"] = "1"
        self.GCheckBox_677["command"] = self.GCheckBox_677_command

        self.GMessage_810=tk.Message(root)
        self.GMessage_810["bg"] = "#b5b5b5"
        self.ft = tkFont.Font(family='Times',size=10)
        self.GMessage_810["font"] = self.ft
        self.GMessage_810["fg"] = "#333333"
        self.GMessage_810["justify"] = "center"
        self.GMessage_810["text"] = "Info"
        self.GMessage_810.place(x=360,y=10,width=425,height=261)

        self.GMessage_706=tk.Message(root)
        self.GMessage_706["bg"] = "#a3a3a3"
        self.ft = tkFont.Font(family='Times',size=10)
        self.GMessage_706["font"] = self.ft
        self.GMessage_706["fg"] = "#333333"
        self.GMessage_706["justify"] = "center"
        self.GMessage_706["text"] = "Console"
        self.GMessage_706.place(x=360,y=280,width=423,height=307)

        self.GLineEdit_723=tk.Entry(root)
        self.GLineEdit_723["borderwidth"] = "1px"
        self.ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_723["font"] = self.ft
        self.GLineEdit_723["fg"] = "#333333"
        self.GLineEdit_723["justify"] = "center"
        self.GLineEdit_723["text"] = "Symbol"
        self.GLineEdit_723.place(x=40,y=300,width=70,height=25)

        self.GLineEdit_803=tk.Entry(root)
        self.GLineEdit_803["borderwidth"] = "1px"
        self.ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_803["font"] = self.ft
        self.GLineEdit_803["fg"] = "#333333"
        self.GLineEdit_803["justify"] = "center"
        self.GLineEdit_803["text"] = "Buy"
        self.GLineEdit_803.place(x=130,y=300,width=70,height=25)

        self.GLineEdit_187=tk.Entry(root)
        self.GLineEdit_187["borderwidth"] = "1px"
        self.ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_187["font"] = self.ft
        self.GLineEdit_187["fg"] = "#333333"
        self.GLineEdit_187["justify"] = "center"
        self.GLineEdit_187["text"] = "Sell"
        self.GLineEdit_187.place(x=230,y=300,width=70,height=25)

        self.GLabel_738=tk.Label(root)
        self.ft = tkFont.Font(family='Times',size=10)
        self.GLabel_738["font"] = self.ft
        self.GLabel_738["fg"] = "#333333"
        self.GLabel_738["justify"] = "center"
        self.GLabel_738["text"] = "Symbol"
        self.GLabel_738.place(x=40,y=260,width=70,height=25)

        self.GLabel_203=tk.Label(root)
        self.ft = tkFont.Font(family='Times',size=10)
        self.GLabel_203["font"] = self.ft
        self.GLabel_203["fg"] = "#333333"
        self.GLabel_203["justify"] = "center"
        self.GLabel_203["text"] = "Buy"
        self.GLabel_203.place(x=130,y=260,width=70,height=25)

        self.GLabel_18=tk.Label(root)
        self.ft = tkFont.Font(family='Times',size=10)
        self.GLabel_18["font"] = self.ft
        self.GLabel_18["fg"] = "#333333"
        self.GLabel_18["justify"] = "center"
        self.GLabel_18["text"] = "Sell"
        self.GLabel_18.place(x=230,y=260,width=70,height=25)

        self.GButton_273=tk.Button(root)
        self.GButton_273["bg"] = "#1e9fff"
        self.GButton_273["disabledforeground"] = "#01aaed"
        self.ft = tkFont.Font(family='Times',size=10)
        self.GButton_273["font"] = self.ft
        self.GButton_273["fg"] = "#000000"
        self.GButton_273["justify"] = "center"
        self.GButton_273["text"] = "Next"
        self.GButton_273.place(x=220,y=360,width=70,height=25)
        self.GButton_273["command"] = self.GButton_273_command

        self.GMessage_696=tk.Message(root)
        self.ft = tkFont.Font(family='Times',size=8)
        self.GMessage_696["font"] = self.ft
        self.GMessage_696["fg"] = "#333333"
        self.GMessage_696["justify"] = "center"
        self.GMessage_696["text"] = "None"
        self.GMessage_696.place(x=50,y=110,width=300,height=120)

        self.GButton_560=tk.Button(root)
        self.GButton_560["bg"] = "#f97d7d"
        self.ft = tkFont.Font(family='Times',size=10)
        self.GButton_560["font"] = self.ft
        self.GButton_560["fg"] = "#000000"
        self.GButton_560["justify"] = "center"
        self.GButton_560["text"] = "Clear"
        self.GButton_560.place(x=20,y=400,width=70,height=25)
        self.GButton_560["command"] = self.GButton_560_command

        self.GLineEdit_94=tk.Entry(root)
        self.GLineEdit_94["borderwidth"] = "1px"
        self.ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_94["font"] = self.ft
        self.GLineEdit_94["fg"] = "#333333"
        self.GLineEdit_94["justify"] = "center"
        self.GLineEdit_94["text"] = "Symbol"
        self.GLineEdit_94.place(x=20,y=370,width=70,height=25)


    def GButton_96_command(self):
        global running, tasks
        running = True
        print("command start")
        play('Process Attaching')
        if len(tasks) != 0:
            play("Sucess")
            start_new_thread(cheakupdate,(1,1))
        else:
            play("Failed")
            print("no data to seek for")


                     


    def GButton_656_command(self):
        global running
        running = False
        print("stop command")



    def GCheckBox_677_command(self):
        print("command")


    def GButton_273_command(self):
        global tasks
        print("next command")
        if str(self.GLineEdit_723.get()).upper() != "":
            if (self.GLineEdit_803.get() != '') and (self.GLineEdit_187.get() != '') :
                ok = True
                try:
                    a = float(self.GLineEdit_187.get())   
                    b = float(self.GLineEdit_803.get()) 
                except:
                    ok = False
                if ok:
                    tasks[str(self.GLineEdit_723.get()).upper()] = (self.GLineEdit_803.get(), self.GLineEdit_187.get())
                    self.GMessage_696['text'] = msg()
                else:
                    print("entry not valid")   
            else:
                print("entry empty")         
        else:
            print("symbol empty")            

    def GButton_560_command(self):
        global tasks
        print("delete command")
        try:
            del tasks[str(self.GLineEdit_94.get()).upper()]
        except:
            print("Symbol doesnot exist")
        self.GMessage_696['text'] = msg()

    def GButton_9sav_command(self):
        global tasks
        if len(tasks) != 0:
            a = open('save.sav', "wb")
            b = pickle.dump(tasks, a)
            print("saved as save.sav")
            self.GMessage_696['text'] = msg()
        else:
            print("save failed no data to save")    
        

    def GButton_9load_command(self):
        global tasks
        a = open('save.sav', "rb")
        tasks = pickle.load(a)
        print("loaded as save.sav")
        self.GMessage_696['text'] = msg()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
