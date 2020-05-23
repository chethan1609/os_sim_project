import numpy as np

def bankers():
    alloc = [
        [0,1,0],
        [2,0,0],
        [3,0,2],
        [2,1,1],
        [0,0,2],
        ]
    maxi = [
        [7,5,3],
        [3,2,2],
        [9,0,2],
        [2,2,2],
        [4,3,3],
    ]
    
    available = [3,3,2]

    alloc = np.array(alloc)
    maxi = np.array(maxi)
    available=np.array(available)

    r = 5
    c = 3

    print("Alloc")
    print(alloc)

    print("Maxi")
    print(maxi)
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
    
    print("Seq")
    print(seq)

    
bankers()