# Touch results file print #


import tkinter
from tkinter import filedialog, END

mainWindow = tkinter.Tk()

# window settings
results = tkinter.Text(mainWindow, height=18, width=40, state='normal')
results.grid(row=1, column=1, sticky='nswe', rowspan=1)
results.config(border=2, relief='sunken')
# get file
input_file = filedialog.askopenfilename(title="Search", filetypes=(("Text file", "*.txt"), ("all files", "*.*")))

AccelOrDecel = ""
time_result = []
distance_result = []
vmax = []
peakG = []
avg_accel = []
alt_diff = []
results_list = []

with open(input_file) as f:
    lines = f.readlines()

for line in lines:
    if "-" in line[0:10]:
        splitLine = [x for x in line.split(" ") if x != ""]
        performanceCheck = splitLine[0].split("-")
        if int(performanceCheck[0]) < int(performanceCheck[1]):
            AccelOrDecel = "Accel"
        else:
            AccelOrDecel = "Decel"
    elif " " in line[0]:
        splitLine = [x for x in line.split(" ") if x != ""]
        time_result.append(splitLine[1])
        distance_result.append(splitLine[2])
        vmax.append(splitLine[3])
        peakG.append(splitLine[4])
        alt_diff.append(splitLine[5])
        avg_accel.append(splitLine[6].strip("\n"))


results_list.append("You may need to press off of the window")
results_list.append("to be able to copy and paste\n")

results_list.append("{} time:".format(AccelOrDecel))
for result in time_result:
    results_list.append(result)
results_list.append("\n")

results_list.append("{} distance:".format(AccelOrDecel))
for result in distance_result:
    results_list.append(result)
results_list.append("\n")

results_list.append("{} VMAX:".format(AccelOrDecel))
for result in vmax:
    results_list.append(result)
results_list.append("\n")

results_list.append("{} PeakG:".format(AccelOrDecel))
for result in peakG:
    results_list.append(result)
results_list.append("\n")

results_list.append("{} Alt diff:".format(AccelOrDecel))
for result in alt_diff:
    results_list.append(result)
results_list.append("\n")

results_list.append("{} Average Accel:".format(AccelOrDecel))
for result in avg_accel:
    results_list.append(result)
results_list.append("\n")

results = tkinter.Text(mainWindow, height=18, width=40, state='normal')
results.grid(row=1, column=1, sticky='nswe', rowspan=1)
results.config(border=2, relief='sunken')

for m in results_list:
    results.insert(END, m + '\n')

mainWindow.mainloop()