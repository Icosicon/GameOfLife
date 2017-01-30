import tkinter,threading#,base64,time,winsound,random,sys,os,ast
#from tkinter import messagebox,filedialog
#from ctypes import windll,byref,create_unicode_buffer,create_string_buffer
initdefault_universe=[[],[3],[2,3]]
GWL_EXSTYLE=-20
WS_EX_APPWINDOW=0x00040000
WS_EX_TOOLWINDOW=0x00000080
def set_appwindow(root):
    hwnd = windll.user32.GetParent(root.winfo_id())
    style = windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
    style = style & ~WS_EX_TOOLWINDOW
    style = style | WS_EX_APPWINDOW
    res = windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, style)
    root.wm_withdraw()
    root.after(10, lambda: root.wm_deiconify())
    
FR_PRIVATE  = 0x10
FR_NOT_ENUM = 0x20

def loadfont(fontpath, private=True, enumerable=False):
    if isinstance(fontpath, bytes):
        pathbuf = create_string_buffer(fontpath)
        AddFontResourceEx = windll.gdi32.AddFontResourceExA
    elif isinstance(fontpath, str): 
        pathbuf = create_unicode_buffer(fontpath)
        AddFontResourceEx = windll.gdi32.AddFontResourceExW
    else:
        raise TypeError('fontpath must be of type str or unicode')

    flags = (FR_PRIVATE if private else 0) | (FR_NOT_ENUM if not enumerable else 0)
    numFontsAdded = AddFontResourceEx(byref(pathbuf), flags, 0)
    return bool(numFontsAdded)
class tools:
    class GeneratorOBJ:
        def __init__(self,generator,length):
            self.generator=generator
            self.length = length
        def __len__(self):
            return self.length
        def __iter__(self):
            return self.generator
    def insertCharBefore(origin,char,buffer):
        return("{}{}".format(char*(buffer-len(str(origin))),str(origin)))
    def insertCharAfter(origin,char,buffer):
        return("{}{}".format(str(origin),char*(buffer-len(str(origin)))))
    def insertDecimalPoint(origin,points):
        return("{}{}".format(str(origin),"0"*(points-(len(str(origin).split(".")[-1])))))
    def loadingPercentageString(iterable):
        for index,item in enumerate(iterable):
            percentage=((index+1)*100)/len(iterable)
            yield (tools.insertCharBefore(tools.insertDecimalPoint(percentage,2),"0",6),item)
    def loadingPercentageFloat(iterable):
        for index,item in enumerate(iterable):
            percentage=((index+1)*100)/len(iterable)
            yield (percentage,item)
    def loadingPercentageGenString(generator):
        for index,item in enumerate(generator):
            percentage=((index+1)*100)/generator.length
            yield (tools.insertCharBefore(tools.insertDecimalPoint(percentage,2),"0",6),item)
    def loadingPercentageGenFloat(generator):
        for index,item in enumerate(generator):
            percentage=((index+1)*100)/generator.length
            yield (percentage,item)
    def loadModules():
        global messagebox
        from tkinter import messagebox
        yield "."
        global base64
        try:
            import base64
        except Exception as detectedException:
            messagebox.showinfo("Error Loading Module","It appears an error has occured:\n{}".format(detectedException))
        yield "."
        for number in range(25):
            with open("loadingCache.txt","wb") as binfile:
                binfile.write(base64.b64encode((str(((number%56)//3)**79-4*2**54%4).encode("utf-8","ignore"))))
            yield ((number%56)//3)**79-4*2**54%4
        global time
        try:
            import time
        except Exception as detectedException:
            messagebox.showinfo("Error Loading Module","It appears an error has occured:\n{}".format(detectedException))
        yield "."
        for number in range(25):
            with open("loadingCache.txt","wb") as binfile:
                binfile.write(base64.b64encode((str(((number%56)//3)**79-4*2**54%4).encode("utf-8","ignore"))))
            yield ((number%56)//3)**79-4*2**54%4
        global winsound
        try:
            import winsound
        except Exception as detectedException:
            messagebox.showinfo("Error Loading Module","It appears an error has occured:\n{}".format(detectedException))
        yield "."
        for number in range(25):
            with open("loadingCache.txt","wb") as binfile:
                binfile.write(base64.b64encode((str(((number%56)//3)**79-4*2**54%4).encode("utf-8","ignore"))))
            yield ((number%56)//3)**79-4*2**54%4
        global random
        try:
            import random
        except Exception as detectedException:
            messagebox.showinfo("Error Loading Module","It appears an error has occured:\n{}".format(detectedException))
        yield "."
        global sys
        try:
            import sys
        except Exception as detectedException:
            messagebox.showinfo("Error Loading Module","It appears an error has occured:\n{}".format(detectedException))
        yield "."
        for number in range(25):
            with open("loadingCache.txt","wb") as binfile:
                binfile.write(base64.b64encode((str(((number%56)//3)**79-4*2**54%4).encode("utf-8","ignore"))))
            yield ((number%56)//3)**79-4*2**54%4
        global ast
        try:
            import ast
        except Exception as detectedException:
            messagebox.showinfo("Error Loading Module","It appears an error has occured:\n{}".format(detectedException))
        yield "."
        for number in range(25):
            with open("loadingCache.txt","wb") as binfile:
                binfile.write(base64.b64encode((str(((number%56)//3)**79-4*2**54%4).encode("utf-8","ignore"))))
            yield ((number%56)//3)**79-4*2**54%4
        global filedialog
        try:
            from tkinter import filedialog
        except Exception as detectedException:
            messagebox.showinfo("Error Loading Module","It appears an error has occured:\n{}".format(detectedException))
        yield "."
        for number in range(25):
            with open("loadingCache.txt","wb") as binfile:
                binfile.write(base64.b64encode((str(((number%56)//3)**79-4*2**54%4).encode("utf-8","ignore"))))
            yield ((number%56)//3)**79-4*2**54%4
        global os
        try:
            import os
        except Exception as detectedException:
            messagebox.showinfo("Error Loading Module","It appears an error has occured:\n{}".format(detectedException))
        yield "."
        for number in range(25):
            with open("loadingCache.txt","wb") as binfile:
                binfile.write(base64.b64encode((str(((number%56)//3)**79-4*2**54%4).encode("utf-8","ignore"))))
            yield ((number%56)//3)**79-4*2**54%4
        global windll
        try:
            from ctypes import windll
        except Exception as detectedException:
            messagebox.showinfo("Error Loading Module","It appears an error has occured:\n{}".format(detectedException))
        yield "."
        for number in range(25):
            with open("loadingCache.txt","wb") as binfile:
                binfile.write(base64.b64encode((str(((number%56)//3)**79-4*2**54%4).encode("utf-8","ignore"))))
            yield ((number%56)//3)**79-4*2**54%4
        
        global byref
        try:
            from ctypes import byref
        except Exception as detectedException:
            messagebox.showinfo("Error Loading Module","It appears an error has occured:\n{}".format(detectedException))
        yield "."
        for number in range(25):
            with open("loadingCache.txt","wb") as binfile:
                binfile.write(base64.b64encode((str(((number%56)//3)**79-4*2**54%4).encode("utf-8","ignore"))))
            yield ((number%56)//3)**79-4*2**54%4
        
        global create_unicode_buffer
        try:
            from ctypes import create_unicode_buffer
        except Exception as detectedException:
            messagebox.showinfo("Error Loading Module","It appears an error has occured:\n{}".format(detectedException))
        yield "."
        for number in range(25):
            with open("loadingCache.txt","wb") as binfile:
                binfile.write(base64.b64encode((str(((number%56)//3)**79-4*2**54%4).encode("utf-8","ignore"))))
            yield ((number%56)//3)**79-4*2**54%4
        
        global create_string_buffer
        try:
            from ctypes import create_string_buffer
        except Exception as detectedException:
            messagebox.showinfo("Error Loading Module","It appears an error has occured:\n{}".format(detectedException))
        yield "."
        for number in range(25):
            with open("loadingCache.txt","wb") as binfile:
                binfile.write(base64.b64encode((str(((number%56)//3)**79-4*2**54%4).encode("utf-8","ignore"))))
            yield ((number%56)//3)**79-4*2**54%4
        try:
            loadfont("Interface/Fonts/BebasNeue.otf")
        except Exception as detectedException:
            messagebox.showinfo("Error Loading Fonts","It appears an error has occured:\n{}".format(detectedException))
        yield "."
        for number in range(25):
            with open("loadingCache.txt","wb") as binfile:
                binfile.write(base64.b64encode((str(((number%56)//3)**79-4*2**54%4).encode("utf-8","ignore"))))
            yield ((number%56)//3)**79-4*2**54%4
        global initdefault_universe
        #global executabledir
        try:
            import argparse
        except Exception as detectedException:
            messagebox.showinfo("Error Loading Module","It appears an error has occured:\n{}".format(detectedException))
        yield "."
        try:
            parser=argparse.ArgumentParser()
            parser.add_argument("universefile",nargs="?",default=False)
            args=parser.parse_args()
            if args.universefile != False:
                universe=tools.getUniverseFromUniverseFileDir(args.universefile).split("|")
                initdefault_universe=[ast.literal_eval(universe[0]),ast.literal_eval(universe[1]),ast.literal_eval(universe[2])]
            #executabledir=os.path.dirname(sys.executable)
        except Exception as detectedException:
            print("Error Loading Arguments","It appears an error has occured:\n{}".format(detectedException))
        yield "."
    def getUniverseFromUniverseFileDir(directory):
        if len(directory.split("."))>0:
            if directory.split(".")[-1]=="universe":
               with open(directory,"rb") as binfile:
                   contents=((base64.b64decode(binfile.read())).decode("utf-8","ignore"))
                   #contents=binfile.read()
                   return contents
    def saveUniverseToUniverseFileDir(directory,universe):
        with open(directory,"wb") as binfile:
            binfile.write(base64.b64encode((str(universe).encode("utf-8","ignore"))))
class loadWindow(tkinter.Frame):
    def __init__(self,master=None):
        tkinter.Frame.__init__(self, master)    
        self.master = master
        self.init_window()
    def init_window(self):
        import os,sys
        #os.chdir(os.path.dirname(os.path.abspath(sys.executable)))
        #comment above for python dev and below for compiled exe
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        self.master.overrideredirect(True)
        self.master.resizable(0,0)
        self.master.configure(background='#ffffff')
        self.master.title("GOL Load")
        self.master.iconbitmap("Interface/ICO/Icon.ico")
        self.w=450
        self.h=225
        self.ws = self.master.winfo_screenwidth()
        self.hs = self.master.winfo_screenheight()
        self.x=(self.ws/2)-(self.w/2)
        self.y=(self.hs/2)-(self.h/2)
        self.master.wm_attributes("-topmost", True)
        self.master.geometry('%dx%d+%d+%d' % (self.w,self.h,self.x,self.y))
        self.images=[tkinter.PhotoImage(file="Interface/GIF/LOADING/Active.gif"),tkinter.PhotoImage(file="Interface/GIF/LOADING/Inactive.gif")]
        self.inactive = tkinter.Label(self.master,image=self.images[1],background="#FFFFFF")
        self.inactive.place(x=0,y=0)
        
        self.progressBar=tkinter.Frame(self.master,height=225,width=int(0),background="#1D60A7",borderwidth=0,highlightthickness=0,padx=0,pady=0)
        self.active = tkinter.Label(self.progressBar,image=self.images[0],background="#FFFFFF",borderwidth=0,highlightthickness=0,padx=0,pady=0)
        self.active.place(x=3,y=2)
        self.progressBar.place(x=0,y=0)

        self.loadmodules()
    def loadmodules(self,*args):
        self.completion=0
        threading.Thread(target=self.percentStart).start()
        self.checkForPercent()
    def percentStart(self):
        for a,b in tools.loadingPercentageGenFloat(tools.GeneratorOBJ(tools.loadModules(),316)):
            self.completion = a
        return 
    def cancel(self):
        self.master.destroy()
    def checkForPercent(self):
        if self.completion < 100:
            self.progressBar.config(width=int((self.completion/100)*450))
            self.master.after(50,self.checkForPercent)
        else:
            self.progressBar.config(width=450)
            self.cancel()
appLoad=loadWindow(tkinter.Tk())
appLoad.mainloop()
#windows
class window(tkinter.Frame):
    def __init__(self,master=None,universe=None):
        tkinter.Frame.__init__(self, master)    
        self.master = master
        self.born=universe[1]
        self.survives=universe[2]
        self.activecells=universe[0]
        self.init_window()
    def init_window(self):
        self.loadopen=True
        self.deltacell = ""
        self.mousedown=False
        self.gridcells={}
        self.master.overrideredirect(True)
        self.master.resizable(0,0)
        self.master.configure(background='#D4D4D4')
        self.master.bind("<Escape>",self.cancel)
        self.images=[tkinter.PhotoImage(file="Interface/GIF/Unactive/Drag.gif"),tkinter.PhotoImage(file="Interface/GIF/Active/Drag.gif"),tkinter.PhotoImage(file="Interface/GIF/Unactive/Cancel.gif"),tkinter.PhotoImage(file="Interface/GIF/Active/Cancel.gif"),tkinter.PhotoImage(file="INTERFACE/GIF/Unactive/Settings.gif"),tkinter.PhotoImage(file="INTERFACE/GIF/Active/Settings.gif"),tkinter.PhotoImage(file="INTERFACE/GIF/Unactive/Frame.gif"),tkinter.PhotoImage(file="Interface/GIF/Active/Frame.gif"),tkinter.PhotoImage(file="INTERFACE/GIF/Active/Information.gif"),tkinter.PhotoImage(file="INTERFACE/GIF/Active/Random.gif"),tkinter.PhotoImage(file="INTERFACE/GIF/Active/Sim Start.gif")]
        self.master.title("Game of Life")
        self.master.iconbitmap("Interface/ICO/Icon.ico")
        self.w1=475
        self.h1=300
        self.ws = self.master.winfo_screenwidth()
        self.hs = self.master.winfo_screenheight()
        self.x=(self.ws/2)-(self.w1/2)
        self.y1=(self.hs/2)-(self.h1/2)
        
        self.drag = tkinter.Label(self.master,image=self.images[0],background="#FFFFFF",bd=0,highlightthickness=0)
        self.drag.place(x=400,y=75)
        self.dragactive = False
        self.drag.bind("<ButtonPress-1>", self.StartMove)
        self.drag.bind("<ButtonRelease-1>", self.StopMove)
        self.drag.bind("<B1-Motion>", self.OnMotion)
        self.drag.bind("<Enter>",self.draghighlight)
        self.drag.bind("<Leave>",self.dragunhighlight)
        
        self.close = tkinter.Label(self.master,image=self.images[2],background="#FFFFFF",bd=0,highlightthickness=0)
        self.close.place(x=400,y=0,height=75,width=75)
        self.closeactive = False
        self.close.bind("<ButtonPress-1>", self.closepress)
        self.close.bind("<ButtonRelease-1>", self.closeunactive)
        self.close.bind("<ButtonPress-3>", self.closepress2)
        self.close.bind("<ButtonRelease-3>", self.closeunactive2)
        self.close.bind("<ButtonPress-2>", self.closepress3)
        self.close.bind("<ButtonRelease-2>", self.closeunactive3)
        self.close.bind("<Enter>",self.closehighlight)
        self.close.bind("<Leave>",self.closeunhighlight)
        
        self.information = tkinter.Label(self.master,image=self.images[4],background="#FFFFFF",bd=0,highlightthickness=0)
        self.information.place(x=400,y=150)
        self.informationactive = False
        self.information.bind("<ButtonPress-1>", self.settingspress)
        self.information.bind("<ButtonRelease-1>", self.settingsunactive)
        self.information.bind("<ButtonPress-3>", self.informationpress)
        self.information.bind("<ButtonRelease-3>", self.informationunactive)
        self.information.bind("<Enter>",self.settingshighlight)
        self.information.bind("<Leave>",self.settingsunhighlight)

        self.frameadvance = tkinter.Label(self.master,image=self.images[6],background="#FFFFFF",bd=0,highlightthickness=0)
        self.frameadvance.place(x=400,y=225)
        self.frameadvanceactive = False
        self.frameadvance.bind("<ButtonPress-1>", self.frameadvancepress)
        self.frameadvance.bind("<ButtonRelease-1>", self.frameadvanceunactive)
        self.frameadvance.bind("<ButtonPress-3>", self.frameadvancepress2)
        self.frameadvance.bind("<ButtonRelease-3>", self.frameadvanceunactive2)
        self.frameadvance.bind("<Enter>",self.frameadvancehighlight)
        self.frameadvance.bind("<Leave>",self.frameadvanceunhighlight)
        
        self.master.geometry('%dx%d+%d+%d' % (self.w1,self.h1,self.x,self.y1))
        
        self.progressBar=tkinter.Frame(self.master,height=75,width=int(0),background="#1D60A7",borderwidth=0,highlightthickness=0,padx=0,pady=0)
        self.progressFrame = tkinter.Label(self.progressBar,image=self.images[7],background="#1D60A7",bd=0,highlightthickness=0)
        self.progressFrame.bind("<ButtonPress-1>", self.frameadvancepress)
        self.progressFrame.bind("<ButtonRelease-1>", self.frameadvanceunactive)
        self.progressFrame.bind("<ButtonPress-3>", self.frameadvancepress2)
        self.progressFrame.bind("<ButtonRelease-3>", self.frameadvanceunactive2)
        self.progressFrame.bind("<Enter>",self.frameadvancehighlight)
        self.progressFrame.bind("<Leave>",self.frameadvanceunhighlight)
        
        self.progressFrame.place(x=2,y=0)
        self.progressBar.place(x=398,y=225)
        
        self.griddisplay = tkinter.Canvas(self.master,height=300,width=400,bd=0,highlightthickness=0)
        for xiter in range(40):
            for yiter in range(30):
                x=(xiter*10)+1
                y=yiter*10
                points=[x,y,x+9,y,x+9,y+9,x,y+9]
                self.gridcells[(xiter,yiter)]=self.griddisplay.create_polygon(points, outline="",fill=["#D4D4D4","#1D60A7"][(xiter,yiter) in self.activecells])
                self.griddisplay.tag_bind(self.gridcells[(xiter,yiter)],"<ButtonPress-1>",lambda event,arg=(xiter,yiter): self.togglecell(arg))
                self.griddisplay.tag_bind(self.gridcells[(xiter,yiter)],"<ButtonRelease-1>",self.unactivetoggledcell)
        self.griddisplay.bind("<B1-Motion>",self.dragactivecell)
        self.griddisplay.bind("<B3-Motion>",self.dragunactivecell)
        self.griddisplay.place(x=0,y=0)

    def acceptsimimport(self,window):
        self.activecells=window.activecells
        self.born=window.born
        self.survives=window.survives
        window.cancel()
        self.updatedisplay()
    def acceptsetimport(self,window):
        self.born=window.born
        self.survives=window.survives
        window.cancel()
    def dragactivecell(self,event):
        x=(event.x-1)//10
        y=(event.y)//10
        cell=(x,y)
        if self.loadopen:
            if (0<=x<40) and (0<=y<30):
                if (cell not in self.activecells) and (cell != self.deltacell):
                    self.activecells.append(cell)
                    self.griddisplay.itemconfig(self.gridcells[cell],fill=["#D4D4D4","#1D60A7"][cell in self.activecells])
    def unactivetoggledcell(self,event):
        self.deltacell=""
    def dragunactivecell(self,event):
        x=(event.x-1)//10
        y=(event.y)//10
        cell=(x,y)
        if self.loadopen:
            if (0<=x<40) and (0<=y<30):
                if cell in self.activecells:
                    self.activecells.remove(cell)
                    self.griddisplay.itemconfig(self.gridcells[cell],fill=["#D4D4D4","#1D60A7"][cell in self.activecells])
    def togglecell(self,cell,*args):
        self.deltacell=cell
        threading.Thread(target=self.popon).start()
        if self.loadopen:
            if cell in self.activecells:
                self.activecells.remove(cell)
            else:
                self.activecells.append(cell)
            self.griddisplay.itemconfig(self.gridcells[cell],fill=["#D4D4D4","#1D60A7"][cell in self.activecells])
        #self.updatedisplay() : removed due to inefficiency
    def updatedisplay(self):
        for cell in self.gridcells:
            self.griddisplay.itemconfig(self.gridcells[cell],fill=["#D4D4D4","#1D60A7"][cell in self.activecells])
    def draghighlight(self,*args):
        if self.dragactive==False:
            self.drag.config(background="#D4D4D4")
    def dragunhighlight(self,*args):
        if self.dragactive==False:
            self.drag.config(background="#FFFFFF")
    def StartMove(self, event):
        threading.Thread(target=self.popon).start()
        self.drag.config(background='#1D60A7',image=self.images[1])
        self.dragactive = True
        self.x1 = event.x
        self.y1 = event.y
    def StopMove(self, event):
        self.drag.config(background='#D4D4D4',image=self.images[0])
        self.dragactive = False
        self.x1 = None
        self.y1 = None
    def OnMotion(self, event):
        deltax = event.x - self.x1
        deltay = event.y - self.y1
        x = self.master.winfo_x() + deltax
        y = self.master.winfo_y() + deltay
        self.master.geometry('%dx%d+%d+%d' % (self.w1,self.h1,x,y))
    def cancel(self,*args):
        self.master.destroy()
    def frameadvancehighlight(self,*args):
        if self.frameadvanceactive==False:
            self.frameadvance.config(background="#D4D4D4")
    def frameadvanceunhighlight(self,*args):
        if self.frameadvanceactive==False:
            self.frameadvance.config(background="#FFFFFF")
    def frameadvancepress(self,*args):
        threading.Thread(target=self.popon).start()
        self.frameadvance.config(background='#1D60A7',image=self.images[7])
        self.frameadvanceactive=True
    def frameadvanceunactive(self,*args):
        self.frameadvance.config(background='#D4D4D4',image=self.images[6])
        self.frameadvanceactive=False
        if self.loadopen:
            self.loadopen=False
            threading.Thread(target=self.loadNext).start()
    def loadNext(self):
        for a,b in tools.loadingPercentageGenFloat(tools.GeneratorOBJ(self.calcnextframe(self.activecells),len(self.activecells)+1)):
            self.completion = a
            active_cascade=b
            self.checkForPercent()
        self.activecells=active_cascade
        self.loadopen=True
    def checkForPercent(self):
        if self.completion < 100:
            self.progressBar.config(width=int((self.completion/100)*75)+2)
            self.master.update()
        else:
            self.progressBar.config(width=77)
            time.sleep(0.01)
            self.progressBar.config(width=0)
    def frameadvancepress2(self,*args):
        threading.Thread(target=self.popon).start()
        self.frameadvance.config(background='#1D60A7',image=self.images[10])
        self.frameadvanceactive=True
    def frameadvanceunactive2(self,*args):
        self.frameadvance.config(background='#D4D4D4',image=self.images[6])
        self.frameadvanceactive=False
        self.spawnsim()
    def closehighlight(self,*args):
        if self.closeactive==False:
            self.close.config(background="#D4D4D4")
    def closeunhighlight(self,*args):
        if self.closeactive==False:
            self.close.config(background="#FFFFFF")
    def closepress(self,*args):
        threading.Thread(target=self.popon).start()
        self.close.config(background='#1D60A7',image=self.images[3])
        self.closeactive=True
    def closeunactive(self,*args):
        self.close.config(background='#D4D4D4',image=self.images[2])
        self.closeactive=False
        time.sleep(0.1)
        self.cancel()
    def closepress2(self,*args):
        threading.Thread(target=self.popon).start()
        self.close.config(background='#1D60A7',image=self.images[3])
        self.closeactive=True
    def closeunactive2(self,*args):
        self.close.config(background='#D4D4D4',image=self.images[2])
        self.closeactive=False
        if self.loadopen:
            self.activecells=[]
            self.updatedisplay()
    def closepress3(self,*args):
        threading.Thread(target=self.popon).start()
        self.close.config(background='#1D60A7',image=self.images[9])
        self.closeactive=True
    def closeunactive3(self,*args):
        self.close.config(background='#D4D4D4',image=self.images[2])
        self.closeactive=False
        if self.loadopen:
            self.randomize()
            self.updatedisplay()
    def settingshighlight(self,*args):
        if self.informationactive==False:
            self.information.config(background="#D4D4D4")
    def settingsunhighlight(self,*args):
        if self.informationactive==False:
            self.information.config(background="#FFFFFF")
    def settingspress(self,*args):
        self.information.config(background='#1D60A7',image=self.images[5])
        threading.Thread(target=self.popon).start()
        self.informationactive=True
    def settingsunactive(self,*args):
        self.information.config(background='#FFFFFF',image=self.images[4])
        self.informationactive=False
        self.spawnset()
    def informationpress(self,*args):
        self.information.config(background='#1D60A7',image=self.images[8])
        threading.Thread(target=self.popon).start()
        self.informationactive=True
    def informationunactive(self,*args):
        self.information.config(background='#FFFFFF',image=self.images[4])
        self.informationactive=False
        self.spawninfo()
    def popon(self,*args):
        sounds=['Interface/AUDIO/popoff.wav','Interface/AUDIO/pop.wav']
        winsound.PlaySound(sounds[random.randint(0,1)],winsound.SND_ASYNC)
    def calcnextframe(self,activecells):
        newactivecells,checkedcells=[],activecells[:]
        for cell in activecells:
            activenbs=0
            for neighbour in self.getallneighbours(cell):
                if neighbour not in checkedcells:
                    activenbnbs = len([a for a in self.getallneighbours(neighbour) if a in activecells])
                    if self.getnewstate(neighbour,activenbnbs):#activecells):
                        newactivecells.append(neighbour)
                        self.griddisplay.itemconfig(self.gridcells[neighbour],fill="#1D60A7")
                    else:
                        self.griddisplay.itemconfig(self.gridcells[neighbour],fill="#D4D4D4")
                    checkedcells.append(neighbour)
                if neighbour in activecells:
                    activenbs+=1
            if self.getnewstate(cell,activenbs):#,activecells):
                newactivecells.append(cell)
                self.griddisplay.itemconfig(self.gridcells[cell],fill="#1D60A7")
            else:
                self.griddisplay.itemconfig(self.gridcells[cell],fill="#D4D4D4")
            yield "."
        yield newactivecells
    def getallneighbours(self,cell):
        x,y=cell
        return [(x,(y-1)%30),((x+1)%40,(y-1)%30),((x+1)%40,y),((x+1)%40,(y+1)%30),(x,(y+1)%30),((x-1)%40,(y+1)%30),((x-1)%40,y),((x-1)%40,(y-1)%30)]
    def getnewstate(self,cell,cellneighbours):
        if cell in self.activecells:
            if cellneighbours in self.survives:
                return True
        else:
            if cellneighbours in self.born:
                return True
        return False
    def spawninfo(self):
        infowin = infowindow(tkinter.Toplevel())
        infowin.mainloop()
    def spawnsim(self):
        simwin = simulatewindow(tkinter.Toplevel(),self)
        set_appwindow(simwin.master)
        simwin.mainloop()
    def spawnset(self):
        setwin = settingswindow(tkinter.Toplevel(),self)
        setwin.mainloop()
    def randomize(self):
        self.activecells=[]
        for cell in self.gridcells:
            isactive=[True,False][random.randint(0,1)]
            if isactive:
                self.activecells.append(cell)
            self.griddisplay.itemconfig(self.gridcells[cell],fill=["#D4D4D4","#1D60A7"][cell in self.activecells])
class infowindow(tkinter.Frame):
    def __init__(self,master=None):
        tkinter.Frame.__init__(self, master)    
        self.master = master
        self.init_window()
    def init_window(self):
        self.master.overrideredirect(True)
        self.master.resizable(0,0)
        self.master.configure(background='#FFFFFF')
        self.master.bind("<Escape>",self.cancel)
        self.master.title("GOL Information")
        self.master.iconbitmap("Interface/ICO/Icon.ico")
        self.w=75*5
        self.h=75
        self.ws = self.master.winfo_screenwidth()
        self.hs = self.master.winfo_screenheight()
        self.x=(self.ws/2)-(self.w/2)
        self.y=(self.hs/2)-(self.h/2)
        self.master.wm_attributes("-topmost", True)
        self.master.geometry('%dx%d+%d+%d' % (self.w,self.h,self.x,self.y))
        self.images=[tkinter.PhotoImage(file="Interface/GIF/Unactive/Drag.gif"),tkinter.PhotoImage(file="Interface/GIF/Active/Drag.gif"),tkinter.PhotoImage(file="Interface/GIF/Unactive/Cancel.gif"),tkinter.PhotoImage(file="Interface/GIF/Active/Cancel.gif")]
        self.texts = [tkinter.PhotoImage(file="Interface/GIF/Message{}.gif".format(x+1)) for x in range(14)]
        self.drag = tkinter.Label(self.master,image=self.images[0],background="#FFFFFF")
        self.drag.place(x=0,y=0)
        self.dragactive = False
        self.drag.bind("<ButtonPress-1>", self.StartMove)
        self.drag.bind("<ButtonRelease-1>", self.StopMove)
        self.drag.bind("<B1-Motion>", self.OnMotion)
        self.drag.bind("<Enter>",self.draghighlight)
        self.drag.bind("<Leave>",self.dragunhighlight)

        self.close = tkinter.Label(self.master,image=self.images[2],background="#FFFFFF",bd=0,highlightthickness=0)
        self.close.place(x=75,y=0)
        self.closeactive = False
        self.close.bind("<ButtonPress-1>", self.closepress)
        self.close.bind("<ButtonRelease-1>", self.closeunactive)
        self.close.bind("<Enter>",self.closehighlight)
        self.close.bind("<Leave>",self.closeunhighlight)

        self.textsindex=0
        self.text = tkinter.Label(self.master,image=self.texts[self.textsindex],background="#FFFFFF",bd=0,highlightthickness=0)
        self.text.place(x=75*2,y=0)
        self.textactive = False
        self.text.bind("<Enter>",self.texthighlight)
        self.text.bind("<Leave>",self.textunhighlight)
        self.text.bind("<ButtonRelease-1>",self.animate)
    def texthighlight(self,*args):
        self.text.config(background="#D4D4D4")
    def textunhighlight(self,*args):
        self.text.config(background="#FFFFFF")
    def draghighlight(self,*args):
        if self.dragactive==False:
            self.drag.config(background="#D4D4D4")
    def dragunhighlight(self,*args):
        if self.dragactive==False:
            self.drag.config(background="#FFFFFF")
    def StartMove(self, event):
        threading.Thread(target=self.popon).start()
        self.drag.config(background='#1D60A7',image=self.images[1])
        self.dragactive = True
        self.x1 = event.x
        self.y1 = event.y
    def StopMove(self, event):
        self.drag.config(background='#D4D4D4',image=self.images[0])
        self.dragactive = False
        self.x1 = None
        self.y1 = None
    def OnMotion(self, event):
        deltax = event.x - self.x1
        deltay = event.y - self.y1
        x = self.master.winfo_x() + deltax
        y = self.master.winfo_y() + deltay
        self.master.geometry('%dx%d+%d+%d' % (self.w,self.h,x,y))
    def cancel(self,*args):
        self.master.destroy()
    def closehighlight(self,*args):
        if self.closeactive==False:
            self.close.config(background="#D4D4D4")
    def closeunhighlight(self,*args):
        if self.closeactive==False:
            self.close.config(background="#FFFFFF")
    def closepress(self,*args):
        threading.Thread(target=self.popon).start()
        self.close.config(background='#1D60A7',image=self.images[3])
        self.closeactive=True
    def closeunactive(self,*args):
        self.close.config(background='#D4D4D4',image=self.images[2])
        self.closeactive=False
        time.sleep(0.1)
        self.cancel()
    def animate(self,*args):
        threading.Thread(target=self.popon).start()
        self.textsindex = (self.textsindex+1)%14
        self.text.config(image=self.texts[self.textsindex])
    def popon(self):
        sounds=['Interface/AUDIO/popoff.wav','Interface/AUDIO/pop.wav']
        winsound.PlaySound(sounds[random.randint(0,1)],winsound.SND_ASYNC)
class simulatewindow(tkinter.Frame):
    def __init__(self,master,parent):
        tkinter.Frame.__init__(self,master)
        self.master=master
        self.parent=parent
        self.activecells=ast.literal_eval(str(parent.activecells))
        self.born = ast.literal_eval(str(parent.born))
        self.survives = ast.literal_eval(str(parent.survives))
        self.init_window()
    def init_window(self):
        self.gridcells={}
        self.simulating=False
        self.master.overrideredirect(True)
        self.master.resizable(0,0)
        self.master.configure(background='#FFFFFF')
        self.master.bind("<Escape>",self.cancel)
        self.master.title("Game of Life Simulate")
        self.master.iconbitmap("Interface/ICO/Icon.ico")
        self.w=350
        self.h=150
        self.ws = self.master.winfo_screenwidth()
        self.hs = self.master.winfo_screenheight()
        self.x=(self.ws/2)-(self.w/2)
        self.y=(self.hs/2)-(self.h/2)
        self.master.geometry('%dx%d+%d+%d' % (self.w,self.h,self.x,self.y))
        self.images=[tkinter.PhotoImage(file="Interface/GIF/Unactive/Drag.gif"),tkinter.PhotoImage(file="Interface/GIF/Active/Drag.gif"),tkinter.PhotoImage(file="Interface/GIF/Unactive/Cancel.gif"),tkinter.PhotoImage(file="Interface/GIF/Active/Cancel.gif"),tkinter.PhotoImage(file="Interface/GIF/Unactive/Sim Start.gif"),tkinter.PhotoImage(file="Interface/GIF/UNACTIVE/Sim Pause.gif"),tkinter.PhotoImage(file="Interface/GIF/Active/Sim Start.gif"),tkinter.PhotoImage(file="Interface/GIF/ACTIVE/Sim Pause.gif"),tkinter.PhotoImage(file="Interface/GIF/Active/Save.gif"),tkinter.PhotoImage(file="Interface/GIF/UNACTIVE/Save.gif"),tkinter.PhotoImage(file="Interface/GIF/ACTIVE/AcceptNew.gif")]
        self.drag = tkinter.Label(self.master,image=self.images[0],background="#FFFFFF",bd=0,highlightthickness=0)
        self.drag.place(x=275,y=0)
        self.dragactive = False
        self.drag.bind("<ButtonPress-1>", self.StartMove)
        self.drag.bind("<ButtonRelease-1>", self.StopMove)
        self.drag.bind("<B1-Motion>", self.OnMotion)
        self.drag.bind("<Enter>",self.draghighlight)
        self.drag.bind("<Leave>",self.dragunhighlight)

        self.close = tkinter.Label(self.master,image=self.images[2],background="#FFFFFF",bd=0,highlightthickness=0)
        self.close.place(x=275,y=75)
        self.closeactive = False
        self.close.bind("<ButtonPress-1>", self.closepress)
        self.close.bind("<ButtonRelease-1>", self.closeunactive)
        self.close.bind("<ButtonPress-3>", self.closepress2)
        self.close.bind("<ButtonRelease-3>", self.closeunactive2)
        self.close.bind("<Enter>",self.closehighlight)
        self.close.bind("<Leave>",self.closeunhighlight)

        self.save = tkinter.Label(self.master,image=self.images[9],background="#FFFFFF",bd=0,highlightthickness=0)
        self.save.place(x=0,y=0)
        self.saveactive = False
        self.save.bind("<ButtonPress-1>", self.savepress)
        self.save.bind("<ButtonRelease-1>", self.saveunactive)
        self.save.bind("<ButtonPress-3>", self.savepress2)
        self.save.bind("<ButtonRelease-3>", self.saveunactive2)
        self.save.bind("<Enter>",self.savehighlight)
        self.save.bind("<Leave>",self.saveunhighlight)

        self.controller = tkinter.Label(self.master,image=self.images[4],background="#FFFFFF",bd=0,highlightthickness=0)
        self.controller.place(x=0,y=75)
        self.controlleractive = False
        self.controller.bind("<ButtonPress-1>", self.controllerpress)
        self.controller.bind("<ButtonRelease-1>", self.controllerunactive)
        self.controller.bind("<Enter>",self.controllerhighlight)
        self.controller.bind("<Leave>",self.controllerunhighlight)
        
        self.griddisplay = tkinter.Canvas(self.master,height=150,width=200,bd=0,highlightthickness=0)
        for xiter in range(40):
            for yiter in range(30):
                x=(xiter*5)+1
                y=yiter*5
                points=[x,y,x+4,y,x+4,y+4,x,y+4]
                self.gridcells[(xiter,yiter)]=self.griddisplay.create_polygon(points, outline="",fill=["#D4D4D4","#1D60A7"][(xiter,yiter) in self.activecells])
        self.griddisplay.place(x=75,y=0)
    def openUniverseFile(self,*args):
        fileDir = filedialog.askopenfilename(filetypes=(("Universe files","*.universe"),("All files", "*.*") ))
        if fileDir:
            try:
                universe=tools.getUniverseFromUniverseFileDir(fileDir).split("|")
                self.activecells=ast.literal_eval(universe[0])
                self.born=ast.literal_eval(universe[1])
                self.survives=ast.literal_eval(universe[2])
                self.updatedisplay()
            except Exception as detectedError:
                if messagebox.askyesno("Error",message="ERROR OPENING UNIVERSE:\n{}\nOpen again?".format(detectedError)):
                    self.openUniverseFile()
    def saveUniverseFile(self,*args):
        fileDir = filedialog.asksaveasfilename(filetypes=(("Universe files","*.universe"),("All files", "*.*") ))
        if fileDir:
            try:
                if not fileDir.endswith(".universe"):
                    fileDir="{}.universe".format(fileDir)
                tools.saveUniverseToUniverseFileDir(fileDir,"{}|{}|{}".format(str(self.activecells),str(self.born),str(self.survives)))
            except Exception as detectedError:
                if messagebox.askyesno("Error",message="ERROR SAVING UNIVERSE:\n{}\nSave again?".format(detectedError)):
                    self.saveUniverseFile()
    def draghighlight(self,*args):
        if self.dragactive==False:
            self.drag.config(background="#D4D4D4")
    def dragunhighlight(self,*args):
        if self.dragactive==False:
            self.drag.config(background="#FFFFFF")
    def StartMove(self, event):
        threading.Thread(target=self.popon).start()
        self.drag.config(background='#1D60A7',image=self.images[1])
        self.dragactive = True
        self.x1 = event.x
        self.y1 = event.y
    def StopMove(self, event):
        self.drag.config(background='#D4D4D4',image=self.images[0])
        self.dragactive = False
        self.x1 = None
        self.y1 = None
    def OnMotion(self, event):
        deltax = event.x - self.x1
        deltay = event.y - self.y1
        x = self.master.winfo_x() + deltax
        y = self.master.winfo_y() + deltay
        self.master.geometry('%dx%d+%d+%d' % (self.w,self.h,x,y))
    def cancel(self,*args):
        self.master.destroy()
    def closehighlight(self,*args):
        if self.closeactive==False:
            self.close.config(background="#D4D4D4")
    def closeunhighlight(self,*args):
        if self.closeactive==False:
            self.close.config(background="#FFFFFF")
    def closepress(self,*args):
        threading.Thread(target=self.popon).start()
        self.close.config(background='#1D60A7',image=self.images[3])
        self.closeactive=True
    def closeunactive(self,*args):
        self.close.config(background='#D4D4D4',image=self.images[2])
        self.closeactive=False
        time.sleep(0.1)
        self.cancel()
    def closepress2(self,*args):
        threading.Thread(target=self.popon).start()
        self.close.config(background='#1D60A7',image=self.images[10])
        self.closeactive=True
    def closeunactive2(self,*args):
        self.close.config(background='#D4D4D4',image=self.images[2])
        self.parent.acceptsimimport(self)
        self.closeactive=False
    def controllerhighlight(self,*args):
        if self.controlleractive==False:
            self.controller.config(background="#D4D4D4")
    def controllerunhighlight(self,*args):
        if self.controlleractive==False:
            self.controller.config(background="#FFFFFF")
    def controllerpress(self,*args):
        threading.Thread(target=self.popon).start()
        self.controller.config(background='#1D60A7',image=[self.images[6],self.images[7]][self.simulating])
        self.controlleractive=True
    def controllerunactive(self,*args):
        self.simulating = not self.simulating
        self.controller.config(background='#D4D4D4',image=[self.images[4],self.images[5]][self.simulating])
        self.controlleractive=False
        if self.simulating:
            self.animate()            
    def savehighlight(self,*args):
        if self.saveactive==False:
            self.save.config(background="#D4D4D4")
    def saveunhighlight(self,*args):
        if self.saveactive==False:
            self.save.config(background="#FFFFFF")
    def savepress(self,*args):
        threading.Thread(target=self.popon).start()
        self.save.config(background='#1D60A7',image=self.images[8])
        self.saveactive=True
    def saveunactive(self,*args):
        self.save.config(background='#D4D4D4',image=self.images[9])
        self.saveactive=False
        self.saveUniverseFile()
    def savepress2(self,*args):
        threading.Thread(target=self.popon).start()
        self.save.config(background='#1D60A7',image=self.images[8])
        self.saveactive=True
    def saveunactive2(self,*args):
        self.save.config(background='#D4D4D4',image=self.images[9])
        self.saveactive=False
        self.openUniverseFile()
    def updatedisplay(self):
        for cell in self.gridcells:
            self.griddisplay.itemconfig(self.gridcells[cell],fill=["#D4D4D4","#1D60A7"][cell in self.activecells])
    def popon(self):
        sounds=['Interface/AUDIO/popoff.wav','Interface/AUDIO/pop.wav']
        winsound.PlaySound(sounds[random.randint(0,1)],winsound.SND_ASYNC)
    def animate(self):
        self.activecells=self.calcnextframe(self.activecells)
        if self.simulating:
            self.master.after(1,self.animate)
        else:
            return None
    def calcnextframe(self,activecells):
        newactivecells,checkedcells=[],activecells[:]
        for cell in activecells:
            activenbs=0
            for neighbour in self.getallneighbours(cell):
                if neighbour not in checkedcells:
                    activenbnbs = len([a for a in self.getallneighbours(neighbour) if a in activecells])
                    if self.getnewstate(neighbour,activenbnbs):#activecells):
                        newactivecells.append(neighbour)
                        self.griddisplay.itemconfig(self.gridcells[neighbour],fill="#1D60A7")
                    else:
                        self.griddisplay.itemconfig(self.gridcells[neighbour],fill="#D4D4D4")
                    checkedcells.append(neighbour)
                if neighbour in activecells:
                    activenbs+=1
            if self.getnewstate(cell,activenbs):#,activecells):
                newactivecells.append(cell)
                self.griddisplay.itemconfig(self.gridcells[cell],fill="#1D60A7")
            else:
                self.griddisplay.itemconfig(self.gridcells[cell],fill="#D4D4D4")
        return newactivecells
    def getallneighbours(self,cell):
        x,y=cell
        return [(x,(y-1)%30),((x+1)%40,(y-1)%30),((x+1)%40,y),((x+1)%40,(y+1)%30),(x,(y+1)%30),((x-1)%40,(y+1)%30),((x-1)%40,y),((x-1)%40,(y-1)%30)]
    def getnewstate(self,cell,cellneighbours):
        if cell in self.activecells:
            if cellneighbours in self.survives:
                return True
        else:
            if cellneighbours in self.born:
                return True
        return False
    def updatedisplay(self):
        for cell in self.gridcells:
            self.griddisplay.itemconfig(self.gridcells[cell],fill=["#D4D4D4","#1D60A7"][cell in self.activecells])
class settingswindow(tkinter.Frame):
    def __init__(self,master=None,parent=None):
        tkinter.Frame.__init__(self, master)    
        self.master = master
        self.born=ast.literal_eval(str(parent.born))
        self.survives=ast.literal_eval(str(parent.survives))
        self.parent=parent
        self.init_window()
    def init_window(self):
        self.master.overrideredirect(True)
        self.master.resizable(0,0)
        self.master.configure(background='#FFFFFF')
        self.master.bind("<Escape>",self.cancel)
        self.master.title("GOL Information")
        self.master.iconbitmap("Interface/ICO/Icon.ico")
        self.w=465
        self.h=150
        self.ws = self.master.winfo_screenwidth()
        self.hs = self.master.winfo_screenheight()
        self.x=(self.ws/2)-(self.w/2)
        self.y=(self.hs/2)-(self.h/2)
        self.master.wm_attributes("-topmost", True)
        self.master.geometry('%dx%d+%d+%d' % (self.w,self.h,self.x,self.y))
        self.images=[tkinter.PhotoImage(file="Interface/GIF/Unactive/Drag.gif"),tkinter.PhotoImage(file="Interface/GIF/Active/Drag.gif"),tkinter.PhotoImage(file="Interface/GIF/Unactive/Cancel.gif"),tkinter.PhotoImage(file="Interface/GIF/Active/Cancel.gif"),tkinter.PhotoImage(file="Interface/GIF/Unactive/Born.gif"),tkinter.PhotoImage(file="Interface/GIF/Unactive/Survives.gif")]
        self.drag = tkinter.Label(self.master,image=self.images[0],background="#FFFFFF",bd=0,highlightthickness=0)
        self.drag.place(x=390,y=0)
        self.dragactive = False
        self.drag.bind("<ButtonPress-1>", self.StartMove)
        self.drag.bind("<ButtonRelease-1>", self.StopMove)
        self.drag.bind("<B1-Motion>", self.OnMotion)
        self.drag.bind("<Enter>",self.draghighlight)
        self.drag.bind("<Leave>",self.dragunhighlight)

        self.close = tkinter.Label(self.master,image=self.images[2],background="#FFFFFF",bd=0,highlightthickness=0)
        self.close.place(x=390,y=75)
        self.closeactive = False
        self.close.bind("<ButtonPress-1>", self.closepress)
        self.close.bind("<ButtonRelease-1>", self.closeunactive)
        self.close.bind("<Enter>",self.closehighlight)
        self.close.bind("<Leave>",self.closeunhighlight)

        self.survivesdisplay = tkinter.Canvas(self.master,height=70,width=140,bd=0,highlightthickness=0)
        self.survivesbtns={}
        self.survivesbtnstxt={}
        for griditer in range(8):
            x=(griditer%4)*35
            y=(griditer//4)*35
            points=[x,y,x+35,y,x+35,y+35,x,y+35]
            self.survivesbtns[griditer+1]=self.survivesdisplay.create_polygon(points, outline="",fill=["#D4D4D4","#1D60A7"][griditer+1 in self.survives])
            self.survivesbtnstxt[griditer+1]=self.survivesdisplay.create_text((x+18,y+18),fill="#FFFFFF",text="{}".format(griditer+1),font="BebasNeue")
            self.survivesdisplay.tag_bind(self.survivesbtns[griditer+1],"<ButtonPress-1>",lambda event,arg=griditer+1: self.togglesurvivesbtn(arg))
            self.survivesdisplay.tag_bind(self.survivesbtnstxt[griditer+1],"<ButtonPress-1>",lambda event,arg=griditer+1: self.togglesurvivesbtn(arg))
        self.survivesdisplay.place(x=250,y=0)
        
        self.survivesbtn = tkinter.Label(self.master,image=self.images[5],background="#FFFFFF",bd=0,highlightthickness=0)
        self.survivesbtn.place(x=0,y=0)
        self.survivesbtnactive = False
        self.survivesbtn.bind("<Enter>",self.survivesbtnhighlight)
        self.survivesbtn.bind("<Leave>",self.survivesbtnunhighlight)
        self.survivesbtn.bind("<ButtonPress-1>",self.survivesdefault)

        self.borndisplay = tkinter.Canvas(self.master,height=70,width=140,bd=0,highlightthickness=0,bg="blue")
        self.bornbtns={}
        self.bornbtnstxt={}
        for griditer in range(8):
            x=(griditer%4)*35
            y=(griditer//4)*35
            points=[x,y,x+35,y,x+35,y+35,x,y+35]
            self.bornbtns[griditer+1]=self.borndisplay.create_polygon(points, outline="",fill=["#D4D4D4","#1D60A7"][griditer+1 in self.born])
            self.bornbtnstxt[griditer+1]=self.borndisplay.create_text((x+18,y+18),fill="#FFFFFF",text="{}".format(griditer+1),font="BebasNeue")
            self.borndisplay.tag_bind(self.bornbtns[griditer+1],"<ButtonPress-1>",lambda event,arg=griditer+1: self.togglebornbtn(arg))
            self.borndisplay.tag_bind(self.bornbtnstxt[griditer+1],"<ButtonPress-1>",lambda event,arg=griditer+1: self.togglebornbtn(arg))
        self.borndisplay.place(x=250,y=80)
        
        self.bornbtn = tkinter.Label(self.master,image=self.images[4],background="#FFFFFF",bd=0,highlightthickness=0)
        self.bornbtn.place(x=0,y=80)
        self.bornbtnactive = False
        self.bornbtn.bind("<Enter>",self.bornbtnhighlight)
        self.bornbtn.bind("<Leave>",self.bornbtnunhighlight)
        self.bornbtn.bind("<ButtonPress-1>",self.borndefault)
    def texthighlight(self,*args):
        self.text.config(background="#D4D4D4")
    def textunhighlight(self,*args):
        self.text.config(background="#FFFFFF")
    def draghighlight(self,*args):
        if self.dragactive==False:
            self.drag.config(background="#D4D4D4")
    def dragunhighlight(self,*args):
        if self.dragactive==False:
            self.drag.config(background="#FFFFFF")
    def StartMove(self, event):
        threading.Thread(target=self.popon).start()
        self.drag.config(background='#1D60A7',image=self.images[1])
        self.dragactive = True
        self.x1 = event.x
        self.y1 = event.y
    def StopMove(self, event):
        self.drag.config(background='#D4D4D4',image=self.images[0])
        self.dragactive = False
        self.x1 = None
        self.y1 = None
    def OnMotion(self, event):
        deltax = event.x - self.x1
        deltay = event.y - self.y1
        x = self.master.winfo_x() + deltax
        y = self.master.winfo_y() + deltay
        self.master.geometry('%dx%d+%d+%d' % (self.w,self.h,x,y))
    def cancel(self,*args):
        self.master.destroy()
    def closehighlight(self,*args):
        if self.closeactive==False:
            self.close.config(background="#D4D4D4")
    def closeunhighlight(self,*args):
        if self.closeactive==False:
            self.close.config(background="#FFFFFF")
    def survivesbtnhighlight(self,*args):
        if self.survivesbtnactive==False:
            self.survivesbtn.config(background="#D4D4D4")
    def survivesbtnunhighlight(self,*args):
        if self.survivesbtnactive==False:
            self.survivesbtn.config(background="#FFFFFF")
    def bornbtnhighlight(self,*args):
        if self.bornbtnactive==False:
            self.bornbtn.config(background="#D4D4D4")
    def bornbtnunhighlight(self,*args):
        if self.bornbtnactive==False:
            self.bornbtn.config(background="#FFFFFF")
    def closepress(self,*args):
        threading.Thread(target=self.popon).start()
        self.close.config(background='#1D60A7',image=self.images[3])
        self.closeactive=True
    def closeunactive(self,*args):
        self.close.config(background='#D4D4D4',image=self.images[2])
        self.closeactive=False
        self.parent.acceptsetimport(self)
    def popon(self):
        sounds=['Interface/AUDIO/popoff.wav','Interface/AUDIO/pop.wav']
        winsound.PlaySound(sounds[random.randint(0,1)],winsound.SND_ASYNC)
    def togglesurvivesbtn(self,btn,*args):
        threading.Thread(target=self.popon).start()
        if btn in self.survives:
            self.survives.remove(btn)
        else:
            self.survives.append(btn)
        self.survivesdisplay.itemconfig(self.survivesbtns[btn],fill=["#D4D4D4","#1D60A7"][btn in self.survives])
    def togglebornbtn(self,btn,*args):
        threading.Thread(target=self.popon).start()
        if btn in self.born:
            self.born.remove(btn)
        else:
            self.born.append(btn)
        self.borndisplay.itemconfig(self.bornbtns[btn],fill=["#D4D4D4","#1D60A7"][btn in self.born])
    def survivesdefault(self,*args):
        threading.Thread(target=self.popon).start()
        self.survives=[2,3]
        for btn in self.survivesbtns:
            self.survivesdisplay.itemconfig(self.survivesbtns[btn],fill=["#D4D4D4","#1D60A7"][btn in self.survives])
    def borndefault(self,*args):
        threading.Thread(target=self.popon).start()
        self.born=[3]
        for btn in self.bornbtns:
            self.borndisplay.itemconfig(self.bornbtns[btn],fill=["#D4D4D4","#1D60A7"][btn in self.born])
app =window(tkinter.Tk(),initdefault_universe)
set_appwindow(app.master)
app.mainloop()
