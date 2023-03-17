from BsExample import BsExample
from LgExample import LgExample

print("select option:\n1:Get list of jobs \n 2.Get list of lobbies")
option=input()
try:
    if option == "1":
        bs = BsExample()
        jobs = bs.get_jobs()
        print(jobs)
        print("save a file :y/n")
        saveSel=input()
        if saveSel=="y":
            print("Enter filename:")
            fileName=input()
            bs.save_file(jobs,fileName)
            print("file saved")
        
    if option =="2":
        lg = LgExample()
        lobbies = lg.get_lobbies()
        for lobby in lobbies:
            print(lobby)
        print("save a file :y/n")
        saveSel=input()
        if saveSel=="y":
            print("Enter filename:")
            fileName=input()
            lg.save_file(lobbies,fileName)
            print("file saved")
except Exception:
    print("Enter valid input")



        
