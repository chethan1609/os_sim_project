import tkinter as tk

def main():
    print("Hello")

    mainwindow = tk.Tk()
    matdisplay_btn = tk.Button(master=mainwindow, text="MatDisplay", command=getinput)
    matdisplay_btn.pack()

    mainwindow.mainloop()

def getinput():
    input_win = tk.Tk()
    
    frame_0_0 = tk.Frame(master=input_win, borderwidth=1)
    frame_0_0.grid(row=0, column=0)
    n_proc_lbl = tk.Label(master=frame_0_0, text="Number of processes")
    n_proc_lbl.pack()
    
    frame_1_0 = tk.Frame(master=input_win, borderwidth=1)
    frame_1_0.grid(row=1, column=0)
    n_res_lbl = tk.Label(master=frame_1_0, text="Number of processes")
    n_res_lbl.pack()

    frame_0_1 = tk.Frame(master=input_win, borderwidth=1)
    frame_0_1.grid(row=0, column=1)
    n_proc_entry = tk.Entry(master=frame_0_1)
    n_proc_entry.pack()

    frame_1_1 = tk.Frame(master=input_win, borderwidth=1)
    frame_1_1.grid(row=1, column=1)
    n_res_entry = tk.Entry(master=frame_1_1)
    n_res_entry.pack()

    def submit():
        r = int(n_proc_entry.get())
        c = int(n_res_entry.get())

        input_win.destroy()
        matdisplay(r, c)
    
    frame_2_1 = tk.Frame(master=input_win, borderwidth=1)
    frame_2_1.grid(row=2, column=1)
    submit_btn = tk.Button(master=frame_2_1, text="Submit", command=submit)
    submit_btn.pack()



def matdisplay(r, c):
    window = tk.Tk()
    entryobj = []

    for i in range(r):
        frame = tk.Frame(window, borderwidth=1)
        frame.grid(row=i+1, column=0)
        lbl = tk.Label(master=frame, text="Process {}".format(i))
        lbl.pack()

    for i in range(c):
        frame = tk.Frame(window, borderwidth=1)
        frame.grid(row=0, column=i+1)
        lbl = tk.Label(master=frame, text="Resource {}".format(i))
        lbl.pack()


    
    for i in range(r):
        for j in range(c):
            frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
            frame.grid(row=i+1, column=j+1, padx=5, pady=5)
            entry = tk.Entry(master=frame)
            entryobj.append(entry)
            entry.pack()

    

    submitspace = tk.Frame(master=window, borderwidth=1)
    submitspace.grid(row=r+1, column=c)

    quitspace = tk.Frame(master=window, borderwidth=1 )
    quitspace.grid(row=r+1, column=0)

    quit_btn = tk.Button(master=quitspace, text="Quit", command = window.destroy)
    quit_btn.pack()


    def takesum():
        values = []
        for obj in entryobj:
            values.append(int(obj.get()))
        
        print(values)

        window.destroy()

    
    submit_btn = tk.Button(master=submitspace, text="Submit", command=takesum)
    submit_btn.pack()

    window.mainloop()



if __name__ == "__main__":
    main()