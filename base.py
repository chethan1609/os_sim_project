import tkinter as tk
import numpy as np


def main():
    mainwindow = tk.Tk()
    mainwindow.title("OS Simulator")
    mainwindow.minsize(400, 300)
    matdisplay_btn = tk.Button(master=mainwindow, text="Banker's Algorithm", command=getinputBankers)
    matdisplay_btn.pack()
    mainwindow.mainloop()

def getinputBankers():
    input_win = tk.Tk()
    input_win.title("Banker's Algorithm Inputs")
    frame_0_0 = tk.Frame(master=input_win, borderwidth=1)
    frame_0_0.grid(row=0, column=0)
    n_proc_lbl = tk.Label(master=frame_0_0, text="Number of processes")
    n_proc_lbl.pack()
    
    frame_1_0 = tk.Frame(master=input_win, borderwidth=1)
    frame_1_0.grid(row=1, column=0)
    n_res_lbl = tk.Label(master=frame_1_0, text="Number of resources")
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
        bankers_input_mat(r, c)
    
    frame_2_1 = tk.Frame(master=input_win, borderwidth=1)
    frame_2_1.grid(row=2, column=1)
    submit_btn = tk.Button(master=frame_2_1, text="Submit", command=submit)
    submit_btn.pack()

    input_win.mainloop()

def bankers(matrix, available, r, c):
    alloc = matrix[0:r, 0:c]
    maxi = matrix[0:r, c:2*c]
    need = maxi - alloc
    work = available
    finished = [False]*r
    seq = []
    check = True
    
    while(len(seq)<r):
        check = False
        print(len(seq))

        print("need")
        print(need)

        print("available")
        print(work)

        for i in range(r):
            if finished[i]==False and (need[i, :] <= work).all():
                seq.append(i)
                work+=alloc[i, :]
                finished[i]=True
                check = True
                print("Worked on sequence " + str(i))
                break

        if(check == False):
            break
    
    text = ""

    if len(seq) != r:
        text = "The sequence couldn't be found"
    else:
        text = "A valid sequence is " + str(seq)
    
    print(text)
    bankers_win = tk.Tk()
    bankers_win.title("Banker's Algorithm Output")
    bankers_win.minsize(400, 300)
    frame = tk.Frame(master=bankers_win)
    res_lbl = tk.Label(master=frame, text=text)
    # res_lbl.place(relx=.5, rely=.5, anchor="center")
    res_lbl.pack()
    # quit_btn = tk.Button(master=bankers_win, text="Quit", command=bankers_win.destroy)
    # quit_btn.pack()

    bankers_win.mainloop()


def bankers_input_mat(r, c):
    window = tk.Tk()
    window.title("Banker's Algorithm Input")
    entryobj = []
    free = []


    for i in range(r):
        frame = tk.Frame(window, borderwidth=1)
        frame.grid(row=i+1, column=0)
        lbl = tk.Label(master=frame, text="Process {}".format(i))
        lbl.pack()

    for i in range(c):
        frame = tk.Frame(window, borderwidth=1)
        frame.grid(row=0, column=i+1)
        lbl = tk.Label(master=frame, text="Resource {} Allocated".format(i))
        lbl.pack()

    for i in range(c):
        frame = tk.Frame(window, borderwidth=1)
        frame.grid(row=0, column=c+i+1)
        lbl = tk.Label(master=frame, text="Resource {} Maximum".format(i))
        lbl.pack()

    
    for i in range(r):
        for j in range(2*c):
            frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
            frame.grid(row=i+1, column=j+1, padx=5, pady=5)
            entry = tk.Entry(master=frame)
            entryobj.append(entry)
            entry.pack()


    frame = tk.Frame(window, borderwidth=1)
    frame.grid(row=r+2, column=0)
    lbl = tk.Label(master=frame, text="Initial Available resource")
    lbl.pack()

    for i in range(c):
        frame = tk.Frame(window, borderwidth=1)
        frame.grid(row=r+2, column=i+1)
        entry = tk.Entry(master=frame)
        free.append(entry)
        entry.pack()
    

    def takesum():
        matrix = []
        for obj in entryobj:
            temp = obj.get()
            try:
                temp = int(temp)
            except ValueError:
                temp = 0
            matrix.append(temp)

        start = []
        for item in free:
            temp = item.get()
            try:
                temp = int(temp)
            except ValueError:
                temp = 0
            start.append(temp)

        matrix = np.array(matrix).reshape(r, 2*c)
        window.destroy()

        bankers(matrix, start, r, c)


    submitspace = tk.Frame(master=window, borderwidth=1)
    submitspace.grid(row=r+3, column=2*c)

    quitspace = tk.Frame(master=window, borderwidth=1 )
    quitspace.grid(row=r+3, column=0)

    quit_btn = tk.Button(master=quitspace, text="Quit", command = window.destroy)
    quit_btn.pack()

    submit_btn = tk.Button(master=submitspace, text="Submit", command=takesum)
    submit_btn.pack()

    window.mainloop()



if __name__ == "__main__":
    main()P = 5
R = 3
  
def calculateNeed(need, maxm, allot): 
  
    for i in range(P): 
        for j in range(R): 
               
            need[i][j] = maxm[i][j] - allot[i][j]  
   
def isSafe(processes, avail, maxm, allot): 
    need = [] 
    for i in range(P): 
        l = [] 
        for j in range(R): 
            l.append(0) 
        need.append(l) 
            
    calculateNeed(need, maxm, allot)  
    finish = [0] * P 
    safeSeq = [0] * P    
    work = [0] * R  
    for i in range(R): 
        work[i] = avail[i]  
    
    count = 0
    while (count < P): 
          
        found = False
        for p in range(P):  
           
            if (finish[p] == 0):  
           
                for j in range(R): 
                    if (need[p][j] > work[j]): 
                        break
                        
                if (j == R - 1):  
                   
                    for k in range(R):  
                        work[k] += allot[p][k]  
  
                    safeSeq[count] = p 
                    count += 1  
                    finish[p] = 1
  
                    found = True
                  
        if (found == False): 
            print("System is not in safe state") 
            return False
            
    print("System is in safe state.", 
              "\nSafe sequence is: ", end = " ") 
    print(*safeSeq)  
  
    return True
  
  
if __name__ =="__main__": 
      
    processes = [0, 1, 2, 3, 4] 
  
    
    avail = [3, 3, 2]  
    
    maxm = [[7, 5, 3], [3, 2, 2], 
            [9, 0, 2], [2, 2, 2], 
            [4, 3, 3]] 
    
    allot = [[0, 1, 0], [2, 0, 0], 
             [3, 0, 2], [2, 1, 1], 
             [0, 0, 2]]  
    
    isSafe(processes, avail, maxm, allot)  
  
