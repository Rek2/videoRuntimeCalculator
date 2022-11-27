import tkinter as tk

#Function called when button pressed, calculates the runtime and displays
#it on screen for the user
def calcRunTime():

    runTime = entry1.get() #Get the run time from user input and store in var

    try:
        runTime = int(runTime) #Try convert runTime to int
    except:
        label1 = tk.Label(root, text= "Please input a valid number") #if it can't be ask user to input a valid number
    else:
        label1 = tk.Label(root, text='Total runtime of all videos: ')

        #Write the runTime into text file on a new line
        f = open("VideoRunTimes.txt", "a")
        f.write(f'{runTime}' + "\n")
        f.close()

        #Read VideoRunTimes.txt and append each line into runTimeList as an integer
        with open("VideoRunTimes.txt", "r") as f:
            runTimeList = [] #List to store various videos runtimes

            #For each line in the txt file, append the integer to a list
            for line in f:
                runTimeList.append(int(line.strip("\n")))

        label2 = tk.Label(root, text=sum(runTimeList)) #Label 2 = list of run times
        label3 = tk.Label(root, text="List of videos runtimes:")

        formatedList = "" #Str to store list after its formated for easier viewing

        #For each element in runTimeList, add it to formatedList with a comma at the end
        #unless it is the last element in the list
        for i in range(len(runTimeList)):
            formatedList += str(runTimeList[i])
            if i < len(runTimeList) - 1:
                formatedList += ", "

        label4 = tk.Label(root, text=formatedList)#Label 4 = formated list

        #Display all labels
        canvas1.create_window(200, 240, window=label2)
        canvas1.create_window(200, 260, window=label3)
        canvas1.create_window(200, 280, window=label4)

    canvas1.create_window(200, 220, window=label1)

#Create buttons and labels for the main program window
root = tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 400)
canvas1.pack()

entry1 = tk.Entry (root)
canvas1.create_window(200, 140, window=entry1)

button1 = tk.Button(text='Caluclate Runtime', command=calcRunTime)
canvas1.create_window(200, 180, window=button1)

label2 = tk.Label(root, text='Enter video runtime (in seconds):')
canvas1.create_window(200, 100, window=label2)

root.mainloop()
