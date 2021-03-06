import csv
from os import listdir
from os.path import isfile, join
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

mypath = "CSV_Files_StockPrice_Large"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
onlyfiles = [mypath + "/" + f for f in onlyfiles]

no = [i for i in range(25)]
volfin = []
changfin = []


for files in onlyfiles:
    with open(files) as datafile1 :
        name = files.split('/')
        print(files)
        split_name = name[len(name) - 1]
        filename = split_name.split('.')

        datafile1reader = csv.reader(datafile1)
        high = []
        low = []
        volume = []
        i = 0
        for row in datafile1reader:
            if (i == 0):
                i = i + 1
                continue
            high.append(float(row[2]))
            low.append(float(row[3]))
            volume.append(float(row[5]))

        nelements = 0
        new_vol = []
        new_chang = []
        i = 1
        p = 0
        vol = 0
        chang = 0
        check = 0

        for k in range(len(high)):
            nelements = nelements + 1
            chang = chang + (high[k] - low[k])
            vol = vol + volume[k]

            if (nelements == 14):
                new_vol.append(vol)
                new_chang.append(chang)
                i = i + 1
                nelements = 0
                new_y = []
                p = 0
                check = 0
                vol = 0
                chang = 0




        new_vol = np.array(new_vol)
        new_chang = np.array(new_chang)
        val_20 = np.percentile(new_vol, 20)
        chang_20 = np.percentile(new_chang, 20)
        volfin.append(val_20)
        changfin.append(chang_20)


count = 0
score = 0
for files in onlyfiles:
    #datafile1 = open(files)
    with open(files) as datafile1 :
        name = files.split('/')
        print(files)
        split_name = name[len(name) - 1]
        filename = split_name.split('.')

        datafile1reader = csv.reader(datafile1)
        close_y = []
        open_val = []
        high = []
        low = []
        volume = []

        x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
        i = 0
        for row in datafile1reader:
            if(i == 0):
                i = i + 1
                continue
            close_y.append(float(row[4]))
            open_val.append(float(row[1]))
            high.append(float(row[2]))
            low.append(float(row[3]))
            volume.append(float(row[5]))

        nelements = 0
        new_y = []
        i = 1
        p = 0
        vol = 0
        chang = 0
        check = 0

        for k in range(len(close_y)):
            new_y.append(close_y[k])
            nelements = nelements + 1
            p = p + (close_y[k] - open_val[k])
            chang = chang + (high[k] - low[k])
            vol = vol + volume[k]

            if(nelements == 14):
                mini = min(new_y)
                maxi = max(new_y)
                for j in range(len(new_y)):
                    if(maxi == mini):
                        new_y[j] = 1
                        continue
                    new_y[j] = (new_y[j] - mini) / (maxi - mini)
                if p > 0:
                    check = 1


                if (vol < volfin[count] and chang < changfin[count]):
                    print("third class with " + str(vol) + " " + str(chang))
                    check = 2
                    score = score + 1

                plt.figure(figsize=(0.5, 0.5))
                #print(str(chang) + " " + str(vol))
                plt.plot(x,new_y)
                #plt.savefig("with_axis/" + filename[0] + "_" + str(i) + ".png")
                #print(p)
                plt.axis('off')
                plt.savefig("3classes/" + filename[0] + "_" + str(i) + "_" + str(check) + ".png")
                #profit_string = str(p)
                #profit_string = profit_string.replace("-","-")
                #profit_string = profit_string.replace(".","#")
                #plt.savefig("resizedImage_50x50_large_csv_withProfit_attached/" + filename[0] + "_" + str(i) + "_" + profit_string + ".png")
                plt.close()

                i = i + 1
                nelements = 0
                new_y = []
                p = 0
                check = 0
                vol = 0
                chang = 0



    count = count + 1
    print(score)
    print(count)