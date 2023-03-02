from calendar import monthcalendar, monthrange,setfirstweekday
from datetime import datetime
from time import sleep

setfirstweekday(0)

#lists

months_list=["ΙΑΝ","ΦΕΒ","ΜΑΡ","ΑΠΡ","ΜΑΙ","ΙΟΥΝ","ΙΟΥΛ","ΑΥΓ","ΣΕΠ",
            "ΟΚΤ","ΝΟΕ","ΔΕΚ"]

#global

current_time =datetime.now()
year_now=current_time.year
month_now=current_time.month
day_now=current_time.day
hour_now=current_time.hour
minutes_now=current_time.minute
year_running=year_now
month_running=month_now
date_now="-".join([str(year_now),str(month_now),str(day_now)])

#funcs

def print_Calendar(year,month):
    month_cal=monthcalendar(year,month)
    prev_month = month-1 if month > 1 else 12
    prev_year = year if month > 1 else year-1
    prev_days =monthrange(prev_year,prev_month)[1]
    now_days=monthrange(year,month)[1]
    print("_________________________________________________")
    print()
    print("{} \t{}".format(months_list[month-1],year))
    print()
    print("_________________________________________________")
    print()
    print("  ΔΕΥ |  ΤΡΙ |  ΤΕΤ |  ΠΕΜ |  ΠΑΡ |  ΣΑΒ |  ΚΥΡ")
    print()
    for week in range(len(month_cal)):
        for day in range(7):
            date_num=month_cal[week][day]
            if date_num != 0:
                strings=[str(year),str(month),str(date_num)]
                date_running="-".join(strings)
                if date_running in date_csv_list:
                    if day==6:
                        if date_num <10:
                            print("[ *{}]".format(date_num), end=" ")
                        else:
                            print("[*{}]".format(date_num), end=" ")
                    else:
                        if date_num <10:
                            print("[ *{}]".format(date_num), end=" |")
                        else:
                            print("[*{}]".format(date_num), end=" |")
                else:
                    if day==6:
                        if date_num <10:
                            print("[  {}]".format(date_num), end=" ")
                        else:
                            print("[ {}]".format(date_num), end=" ")
                    else:
                        if date_num <10:
                            print("[  {}]".format(date_num), end=" |")
                        else:
                            print("[ {}]".format(date_num), end=" |")
            elif week == 0 and day < month_cal[week].index(1):
                print("   {}".format(prev_days-month_cal[week].index(1)+day+1), end=' |')
            elif week == len(month_cal)-1 and day > month_cal[week].index(now_days):
                if day==6:
                    print("    {}".format(day-month_cal[week].index(now_days)), end=' ')
                else:
                    print("    {}".format(day-month_cal[week].index(now_days)), end=' |')
        print()
        print()
    print("_________________________________________________")
    print()
    print("Πατήστε\033[1m ENTER \033[0m για προβολή του επόμενου μήνα, \033[1m\"q\"\033[0m για έξοδο ή κάποια από τις\nπαρακάτω επιλογές:")
    print()
    print(" \033[1m\t\"-\"\033[0m για πλοήγηση στον προηγούμενο μήνα")
    print()
    print(" \033[1m\t\"+\"\033[0m για διαχείριση των γεγονότων του ημερολογίου")
    print()
    print(" \033[1m\t\"*\"\033[0m για εμφάνιση των γεγονότων ενός επιλεγμένου μήνα")
    print()

def next_running():
    global year_running
    global month_running
    year_running=year_running if month_running<12 else year_running+1
    month_running=month_running+1  if month_running < 12 else 1

def prev_running():
    global year_running
    global month_running
    year_running=year_running if month_running > 1 else year_running-1
    month_running=month_running-1 if month_running > 1 else 12

def year_loop():
    global year_input
    while True:
        try:
            year_input=int(input("Εισάγετε έτος: "))
        except:
            print()
            print("Παρακαλώ εισάγετε έτος από το 2000 εώς το 2100 (π.χ. 2023)")
            print()
            pass
        else:
            while year_input>2100  or year_input<2000:
                print()
                print("Παρακαλώ εισάγετε έτος από το 2000 εώς το 2100 (π.χ. 2023)")
                print()
                year_loop()
            break

def month_loop():
    global month_input
    while True:
        try:
            month_input=int(input("Εισάγετε μήνα: "))
        except:
            print()
            print("Παρακαλώ εισάγετε μήνα από το 1 εώς το 12 (π.χ. 6)")
            print()
            pass
        else:
            while month_input>12 or month_input<1:
                print()
                print("Παρακαλώ εισάγετε μήνα από το 1 εώς το 12 (π.χ. 6)")
                print()
                month_loop()
            break

def date_loop():
    global date_input
    global date_year_loop
    global date_month_loop
    global date_day_loop
    global month_dates
    while True:
        try:
            date_input=input("Ημερομηνία γεγονότος: ")
            date_year_loop,date_month_loop,date_day_loop=str(date_input).split("-")
            month_dates=monthrange(int(date_year_loop),int(date_month_loop))[1]

        except:
            print()
            print("Παρακαλώ εισάγετε σωστή ημερομηνία σε μορφή ΥΥΥΥ-ΜΜ-DD (πχ. 2022-12-06)")
            print()
            pass
        else:
            while int(date_year_loop)<2022  or int(date_month_loop)<1 or \
                int(date_month_loop)>12 or int(date_day_loop) > month_dates:
                print()
                print("Παρακαλώ εισάγετε σωστή ημερομηνία σε μορφή ΥΥΥΥ-ΜΜ-DD (πχ. 2022-12-06)")
                print()
                date_loop()
            break

def hour_loop():
    global hour_input
    global hour_hour_loop
    global hour_minutes_loop
    while True:
        try:
            hour_input=input("Ώρα γεγονότος: ")
            hour_hour_loop,hour_minutes_loop=str(hour_input).split(":")
            if "0" != hour_hour_loop[0] and len(hour_hour_loop)==1:
                hour_hour_loop="0"+hour_hour_loop
            elif "0" == hour_hour_loop[0] and len(hour_hour_loop)==1:
                hour_hour_loop="0"+hour_hour_loop
            if "0" != hour_minutes_loop[0] and len(hour_minutes_loop)==1:
                hour_minutes_loop="0"+hour_minutes_loop
            elif "0" == hour_minutes_loop[0] and len(hour_minutes_loop)==1:
                hour_minutes_loop="0"+hour_minutes_loop
        except:
            print()
            print("Παρακαλώ εισάγετε σωστή ώρα σε μορφή ΗΗ:ΜΜ (πχ. 23:30)")
            print()
            pass
        else:
            while int(hour_hour_loop)<0 or int(hour_hour_loop)>23 or \
                int(hour_minutes_loop)<0 or int(hour_minutes_loop)>59 :
                print()
                print("Παρακαλώ εισάγετε σωστή ώρα σε μορφή ΗΗ:ΜΜ (πχ. 23:30)")
                print()
                hour_loop()
            break

def duration_loop():
    global duration_input
    while True:
        try:
            duration_input=int(input("Διάρκεια γεγονότος: "))
        except:
            print()
            print("Παρακαλώ εισάγετε σωστή διάρκεια σε μορφή θετικού ακέραιου (πχ. 60)")
            print()
            pass
        else:
            while duration_input<1:
                print()
                print("Παρακαλώ εισάγετε σωστή διάρκεια σε μορφή θετικού ακέραιου (πχ. 60)")
                print()
                duration_loop()
            break

def title_loop():
    global title_input
    while True:
        try:
            title_input=input("Τίτλος γεγονότος: ")
        except:
            print()
            print("Παρακαλώ εισάγετε σωστό τίτλο χωρίς κόμμα (πχ. Mathimatika)")
            print()
            pass
        else:
            while "," in title_input:
                print()
                print("Παρακαλώ εισάγετε σωστό τίτλο χωρίς κόμμα (πχ. Mathimatika)")
                print()
                title_loop()
            break

def search_events():
    print()
    print("=== Αναζήτηση γεγονότων ====")
    print()
    year_loop()
    print()
    month_loop()
    print()
    global same_indexes
    year_indexes=[index for index in range(len(year_csv_list))\
        if year_csv_list[index]==str(year_input)]
    month_indexes=[index for index in range(len(month_csv_list))\
        if month_csv_list[index]==str(month_input)]
    same_indexes=[value for value in year_indexes if value in month_indexes]
    if bool(same_indexes):
        for i in range(len(same_indexes)):
            index=same_indexes[i]
            print(" {}. [{}] -> Date: {}, Time: {}, Duration: {}".format(i,\
                title_csv_list[index],date_csv_list[index],time_csv_list[index] ,\
                    duration_csv_list[index]))
            print()
    else:
        print("Δεν υπάρχει κανένα γεγονός για εμφάνιση.")
        print()
        input("Πατήστε οποιοδήποτε χαρακτήρα για επιστροφή στο κυρίως μενού: ")
        menu()

def manage_events():
    global date_input
    global hour_input
    global duration_input
    global title_input
    print("----------------------------------------------------")
    print()
    print("Διαχείριση γεγονότων ημερολογίου, επιλέξτε ενέργεια:")
    print()
    print("\t1 Καταγραφή νέου γεγονότος")
    print()
    print("\t2 Διαγραφή γεγονότος")
    print()
    print("\t3 Ενημέρωση γεγονότος")
    print()
    print("\t0 Επιστροφή στο κυρίως μενού")
    print()
    manage_choice=input("\t-> ")
    print()
    if manage_choice=="0":
        menu()
    elif manage_choice=="1":
        print()
        print("=== Επιλογή  Ημερομηνίας ====")
        print()
        date_input="-".join([str(int(date_year_loop)),str(int(date_month_loop)),str(int(date_day_loop))])
        print()
        hour_loop()
        hour_input=":".join([str(hour_hour_loop),str(hour_minutes_loop)])
        print()
        duration_loop()
        print()
        title_loop()
        print()
        Lines.append('{},{},{},{}\n'.format(date_input,hour_input,duration_input,title_input))
        with open("events.csv","w") as fw:
            fw.writelines(Lines)
        print()
        print("Το γεγονός  : [{}] -> Date: {}, Time: {}, Duration: {}  καταγράφηκε.".format(title_input,date_input,hour_input,duration_input))
        print()
        sleep(1)
        input("Πατήστε οποιοδήποτε χαρακτήρα για επιστροφή στο κυρίως μενού: ")
        menu()
    elif manage_choice=="2":
        search_events()
        event_choice=input("Επιλέξτε γεγονός προς διαγραφή: ")
        print()
        for i in range(len(same_indexes)):
            if event_choice == str(i):
                print("Το παρακάτω γεγονός διαγράφηκε:")
                print()
                print(" {}. [{}] -> Date: {}, Time: {}, Duration: {}".format(i,\
                title_csv_list[same_indexes[i]],date_csv_list[same_indexes[i]],time_csv_list[same_indexes[i]] ,\
                    duration_csv_list[same_indexes[i]]))
                print()
                sleep(1)
                delete_index=same_indexes[i]+1
                Lines.pop(delete_index)
                with open("events.csv","w") as fw:
                    fw.writelines(Lines)
        print()
        input("Πατήστε οποιοδήποτε χαρακτήρα για επιστροφή στο κυρίως μενού: ")
        menu()
    elif manage_choice=="3":
        search_events()
        event_choice=input("Επιλέξτε γεγονός προς ενημέρωση: ")
        print()
        for i in range(len(same_indexes)):
            if event_choice == str(i):
                print()
                date_input=input("Ημερομηνία γεγονότος ({}): ".format(date_csv_list[same_indexes[i]]))
                print()
                if date_input!="":
                    date_loop()
                    date_csv_list[same_indexes[i]]=date_input
                    print()
                hour_input=input("Ώρα γεγονότος ({}): ".format(time_csv_list[same_indexes[i]]))
                print()
                if hour_input!="":
                    hour_loop()
                    time_csv_list[same_indexes[i]]=hour_input
                    print()
                duration_input=input("Διάρκεια γεγονότος ({}): ".format(duration_csv_list[same_indexes[i]]))
                print()
                if duration_input!="":
                    duration_loop()
                    duration_csv_list[same_indexes[i]]=duration_input
                    print()
                title_input=input("Τίτλος γεγονότος ({}): ".format(title_csv_list[same_indexes[i]]))
                print()
                if title_input!="":
                    title_loop()
                    title_csv_list[same_indexes[i]]=title_input
                    print()
                refresh_index=same_indexes[i]+1
                Lines[refresh_index]='{},{},{},{}\n'.format(date_csv_list[same_indexes[i]],\
                    time_csv_list[same_indexes[i]],duration_csv_list[same_indexes[i]],\
                        title_csv_list[same_indexes[i]])
                with open("events.csv","w") as fw:
                    fw.writelines(Lines)
        print()
        input("Πατήστε οποιοδήποτε χαρακτήρα για επιστροφή στο κυρίως μενού: ")
        menu()
    else:
        print("Πατήθηκε λάθος κουμπι")
        print()
        input("Πατήστε οποιοδήποτε χαρακτήρα για επιστροφή στο κυρίως μενού: ")
        menu()

def file_open():
    #csv handling
    global Lines
    global date_csv_list
    global time_csv_list
    global title_csv_list
    global duration_csv_list
    global year_csv_list
    global month_csv_list
    global day_csv_list
    global hour_csv_list
    global minutes_csv_list
    date_csv_list=[]
    time_csv_list=[]
    duration_csv_list=[]
    title_csv_list=[]
    year_csv_list=[]
    month_csv_list=[]
    day_csv_list=[]
    hour_csv_list=[]
    minutes_csv_list=[]
    with open("events.csv","r")as frf:
        Lines=frf.readlines()
    with open("events.csv","w")as frw:
        for line in Lines:
            if not line.isspace():
                frw.write(line)
    with open("events.csv","r")as frl:
        Lines=frl.readlines()
    for i in range(1,len(Lines)):
        line=Lines[i]
        line.strip()
        date_csv,time_csv,duration_csv,title_csv=line.split(",")
        date_csv_list.append(date_csv.strip())
        time_csv_list.append(time_csv.strip())
        duration_csv_list.append(duration_csv.strip())
        title_csv_list.append(title_csv.strip())
    for date in date_csv_list:
        year_csv,month_csv,day_csv=date.split("-")
        year_csv_list.append(year_csv)
        month_csv_list.append(month_csv)
        day_csv_list.append(day_csv)
    for time in time_csv_list:
        hour_csv,minutes_csv=time.split(":")
        hour_csv_list.append(hour_csv)
        minutes_csv_list.append(minutes_csv)

def menu():
    file_open()
    print_Calendar(year_running,month_running)
    while True:
        menu_choice=input("\t-> ")
        print()
        if menu_choice == "q":
            print()
            print("\033[1mΈξοδος σε:\033[0m")
            sleep(0.6)
            print()
            print(3)
            sleep(0.6)
            print()
            print(2)
            sleep(0.6)
            print()
            print(1)
            sleep(0.6)
            print()
            quit()
        elif menu_choice == "Q":
            print()
            print("\033[1mΈξοδος σε:\033[0m")
            sleep(0.6)
            print()
            print(3)
            sleep(0.6)
            print()
            print(2)
            sleep(0.6)
            print()
            print(1)
            sleep(0.6)
            print()
            quit()
        elif menu_choice=="":
            next_running()
        elif menu_choice=="-":
            prev_running()
        elif menu_choice=="*":
            search_events()
            input("Πατήστε οποιοδήποτε χαρακτήρα για επιστροφή στο κυρίως μενού: ")
        elif menu_choice=="+":
            manage_events()
            break
        else:
            print("Πατήθηκε λάθος κουμπί. Παρακαλώ προσπαθείστε ξανά ")
            print()
            continue
        print_Calendar(year_running,month_running)

def notifications():
    global date_now
    global hour_now
    global minutes_now
    global minutes_for_event
    global hour_for_event
    print()
    file_open()
    for i in range(len(date_csv_list)):
        date=date_csv_list[i]
        if date_now ==date and int(hour_now)<=int(hour_csv_list[i]):
            if int(hour_now)==int(hour_csv_list[i]) and int(minutes_now)<=int(minutes_csv_list[i]):
                hour_for_event=int(hour_csv_list[i])-int(hour_now)
                minutes_for_event=int(minutes_csv_list[i])-int(minutes_now)
                if minutes_for_event<0:
                    minutes_for_event+=60
                    hour_for_event-=1
                    print()
                if minutes_for_event>=0 and hour_for_event>=0:
                    print("Ειδοποίηση: σε {} ώρες και {} λεπτά από τώρα έχειπρογραμματιστεί το γεγονός «{}»."\
                        .format(hour_for_event,minutes_for_event,title_csv_list[i]))
                    print()
            else:
                hour_for_event=int(hour_csv_list[i])-int(hour_now)
                minutes_for_event=int(minutes_csv_list[i])-int(minutes_now)
                if minutes_for_event<0:
                    minutes_for_event+=60
                    hour_for_event-=1
                    print()
                if minutes_for_event>=0 and hour_for_event>=0:
                    print("Ειδοποίηση: σε {} ώρες και {} λεπτά από τώρα έχειπρογραμματιστεί το γεγονός «{}»."\
                        .format(hour_for_event,minutes_for_event,title_csv_list[i]))
                    print()
    input("Πατήστε οποιοδήποτε χαρακτήρα για εισαγωγή στο κυρίως μενού: ")
    print()
    menu()

#code start

notifications()