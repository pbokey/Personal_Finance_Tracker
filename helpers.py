import datetime
import threading
import csv

directory = "transactions/"
filename = None
time = datetime.datetime.now()
old_time = None
my_timer = None

def getCurrentTimeStamp():
    global time
    global old_time
    time = datetime.datetime.now()
    if (old_time == None):
        old_time = time
        createNewCsv()
        addMonthlyRecurringCharges()
    elif (old_time.month != time.month):
        createNewCsv()
        addMonthlyRecurringCharges()
        old_time = time

def createNewCsv():
    global filename
    month = time.month
    year = time.year
    filename = "{}{}_{}.csv".format(directory, year, month)
    f = open(filename, "w+")
    f.write("Timestamp, Type, Amount, Category, Vendor, Lat, Long \n")
    f.close()

def addMonthlyRecurringCharges():
    global filename
    monthly_charges = list()
    with open("monthly_charges.csv", newline='') as file:
        reader = csv.reader(file, dialect="excel")
        for row in reader:
            monthly_charges.append(row)
    monthly_charges = monthly_charges[1:]
    print(monthly_charges)

    with open(filename, "a", newline='') as file:
        writer = csv.writer(file,dialect="excel")
        for item in monthly_charges:
            item.insert(0, time)
            writer.writerow(item)

def add_transaction(tran_type, amount, category, vendor, lat, lon):
    getCurrentTimeStamp()
    item = [time, tran_type, amount, category, vendor, lat, lon]
    with open(filename, "a", newline='') as file:
        writer = csv.writer(file, dialect="excel")
        writer.writerow(item)
