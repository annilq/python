import csv
from datetime import datetime
from matplotlib import pyplot as plt

dates,highs,lows=[],[],[]
with open("death_valley_2014.csv") as csvFile:
    reader=csv.reader(csvFile)
    header_row=next(reader)
    for row in reader:
        try:
            high_temp=int(row[1])
            low_temp=int(row[3])
            date=datetime.strptime(row[0],"%Y-%m-%d")
        except ValueError:
            print(date,"missed")
        else:
            highs.append(high_temp)
            lows.append(low_temp)
            dates.append(date)

for index,col in enumerate(header_row):
    print(index,":",col)


fig=plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,c="red",alpha=0.5)
plt.plot(dates,lows,c="blue",alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor="blue",alpha=0.1)
plt.title("daily high temperratures july 2014",fontsize=24)
plt.xlabel("",fontsize=16)
fig.autofmt_xdate()
plt.ylabel("temperature",fontsize=16)
plt.tick_params(axis='both',which="major",labelsize=16)
plt.show()