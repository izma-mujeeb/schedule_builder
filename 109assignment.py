"""
For my CPS109 assignment, I present to you a Schedule Builder. I find that, oftentimes, it is hard to find time 
during the day to get activities done outside of school while also maintaining and staying up to date with our school 
work. This lack of organization and time management tends to put us back the following day, having to do double the 
amount of work. The Schedule Builder that I have built helps fix this problem by creating an ideal schedule for you. 
It allows you to input what courses you need to study for and allocates 3 hours for the day for that specific course. 
In addition to this, you can input two other activities you need to get done for the day. The schedule builder will 
set aside one hour per activity, giving you a reasonable amount of time to complete it. Additionally, the schedule 
builder already has time set aside during the day for eating, spending time with your family, getting up and going 
back to sleep, all which are crucial parts of the day. For this schedule builder, specifically, it will generate a 
schedule for you from 8am - 11pm. By the end of seeing your schedule, you will be able to find what times during the 
day you have free time to do anything you want.
"""
import random
import time as time_1 
from colorama import Fore, Back, Style,init  
init(autoreset=True)
#the following function generates a random number that is used to find during what time of the day you would be 
#doing the two activities that you need to get done for the day  
def randomHour(): #USER DEFINED FUNCTION 
    rand_1 = random.randrange(11,22)  
    return rand_1  
#the following function figures what times during the day you are going to be occupied from you studying for your courses
#This schedule builder gives you 3 hours out of the day to study for one course, so this function generates what timings
#are left over that could be occupied by your activities 
def occupiedTime(time_arr):
    timeOcc = [] #VARIABLE DECLARATION 
    output = "" #VARIABLE DECLARATION
    for i in time_arr: #going through an array which is filled with the starting time for the courses 
        count = i 
        end = i + 3 #WHILE LOOP BELOW 
        while count != end: #this while loop iterates 3 times because you are given three hours to study for your course 
            output += str(count) 
            count += 1 #ARITHMETIC EXPRESSION 
            timeOcc.append(output) #appending the timings occupied by you studying to an array 
            output = ""  
    return timeOcc #outputs for example [3,4,5,8,9,10] - exam at 3 and exam at 8 pm  

#this function is used for writing all activities that you need to get done for the day in a txt file
# txt file ensures that all other activities disregarding studying are in one place 
def write_activites():
    f = open('assignment.txt','w')
    print("Alongside studying, it looks like you need to get done two other activities for the day")  
    for i in range(1,3):
        f.write(input("Please enter activity # "+str(i) +": ")) #asking the user for the activities 
        f.write('\n') 
    f.close() 
    return 2 #this function returns 2 because you will only be inputting two activities for the day  

#this function is used for reading all the actitivites in the txt file FILE INPUT AND OUTPUT   
def read_activities():
    activites = []
    activites.append('Eat\n') #activities that everyone will need to do 
    activites.append('Hang out with your family\n') #activities that everyone will need to do 
    f = open('assignment.txt','r')
    for i in range(write_activites()):  
        activites.append(f.readline()) 
    activites = [i.replace('\n','') for i in activites] #turning all activities into a list 
    return activites #returning the list of actitivites 

#this function is used alongside the occupiedTime() function to get rid of the study time from a list of timings of the day
def make_schedule(subject_arr, time_arr, num): #num = number of exams time_arr = [456,91011]   
    time = [12,13,14,15,16,17,18,19,20,21,22] #timings of the day[in 24 hour clock format]
    func = [eval(i) for i in occupiedTime(time_arr)]  #SEQUENCE TYPES 
    for i in range(len(func)): #FOR LOOP
        if func[i] in time: 
            time.remove(func[i]) #removing study time from the above list 
    return time  #returning the time list without the study time  
                   
#the following is where the main input from the user is done 
schedule_arr = []         
subject_arr = [] 
time_arr = [] 
mydict = {12:12, 1:13, 2:14, 3:15, 4:16, 5:17, 6:18, 7:19, 8:20, 9:21, 10:22} 
pm_am = ""
num = 2 #number of courses they can enter 
print("To start off...you will be asked to enter the two courses you would like to study for today") 
print("Be mindful that since your day will start at 11am and end at 11pm, the earliest you can start studying is 12pm and the latest is 8pm [since for each class you will be studying for 3 hours]")
print('When entering your second studying time, make sure it is 3 hours after your first studying time')
print()
for i in range(1,3):
    try:
        subject = input("Please enter the name of course #" +str(i)+" ") #entering name of course #i 
        print() 
        time = int(input("What time would you like to start studying for this course? DO NOT enter pm or am ")) #entering the starting time of course #i
        print()
        if time in mydict: #if timings is an am   
            time_arr.append(mydict[time]) #if timings is a pm convert the timing to a timing in the 24 hour clock
            schedule_arr.append(str(int(mydict[time]))+'-'+str(int(mydict[time])+3)+""+str('Study for '+subject)) #appending the timings and subjects to a different array 
    except: 
       time = int(input("Please enter an integer value input ")) #asking the user to enter a value that is greater than 3 hours because studying for each course is 3 hours long 
       if time in mydict:  #appending the new timings[two different ways because we are accounting for timings in the 12 hour clock and timings in the 24 hour clock]
           time_arr.append(mydict[time]) 
           schedule_arr.append(str(int(mydict[time]))+'-'+str(int(mydict[time])+3)+""+str('Study for '+subject))  
    time = 0  
time_for_act = make_schedule(subject_arr,time_arr,num) #calling on the make_schedule function to get rid of the study time from the courses  
activities = read_activities() #calling the read_activities() function to read all acitivites in the txt file 
for i in activities: #going through all the acitivites and finding a time that is not already used up by the studying time for the acitivites 
    while True:
        hour = randomHour() #this while loop iterates until we find a time that is not occupied 
        if hour in time_for_act:  
            break 
    if hour in time_for_act:
        if len(str(hour)) == 1: #the if statement is for 2 digit timings and the else statement is for 1 digit timings 
            schedule_arr.append(str(int(hour))+"    "+str(i)) #appending the time in an array 
            time_for_act.remove(int(hour)) #removing the time since it has not been used up 
        else: #IF ELSE STATEMENTS 
            schedule_arr.append(str(int(hour))+"   "+str(i)) 
            time_for_act.remove(int(hour)) 
#the following lines of code are used to            
order = []
mydict_2 = {12:12, 13:1, 14:2, 15:3, 16:4, 17:5, 18:6, 19:7, 20:8, 21:9, 22:10, 23:11} #dictonary used to put everything back to the 12 hour clock format 
for i in schedule_arr:
    order.append(str(i[0])+str(i[1])) 
order = [i.replace('-','') for i in order] #this order array is used to put all of the timings in order since the schedule should be in order of time 
order = [eval(i) for i in order] 
order = sorted(order)  
dict_1 = {} 
file = open('cps109_a1_output.txt', 'w') #writing to an output file as stated in the assignment 
for i in "YOUR SCHEDULE FOR TODAY": #printing a header for the schedule 
    print(Fore.MAGENTA+i,end="")  
    time_1.sleep(0.1) 
print()
for i in range(len(order)):
    dict_1[schedule_arr[i][:5]] = schedule_arr[i][5:]   
print(Fore.CYAN + '11am: Wake up') #first task on the schedule PRINT STATEMENTS 
file.write('11am: Wake up') 
file.write('\n') 
for i in order:
    if len(str(i)) == 1: #if the timing is one digit 
        if str(i)+"    " in dict_1:
            print(Fore.CYAN + str(mydict_2[i]) + 'pm : '+dict_1[str(i)+"    "]) #displaying the task for that specific timing 
            file.write(str(mydict_2[i]) + 'pm : '+dict_1[str(i)+"    "])
            file.write('\n') 
    elif len(str(i)) == 2: #if the timing is two digits 
        if str(i)+"   " in dict_1:
            print(Fore.YELLOW + str(mydict_2[i])+'pm : '+dict_1[str(i)+"   "]) #displaying the task for that specific timing 
            file.write(str(mydict_2[i])+'pm : '+dict_1[str(i)+"   "])
            file.write('\n')
    if (str(i)+'-'+str(int(i+3))) in dict_1:
        print(Fore.MAGENTA + str(mydict_2[i]) +'-'+str(mydict_2[i+3])+ 'pm: '+ dict_1[str(i)+'-'+str(int(i+3))]) #displaying the task for that specific timing 
        file.write(str(mydict_2[i]) +'-'+str(mydict_2[i+3])+ 'pm: '+ dict_1[str(i)+'-'+str(int(i+3))])
        file.write('\n')
print(Fore.MAGENTA+'11pm: Go to bed') #last task of the day  
file.write('11pm: Go to bed')
file.close() 
    
    
 
    
    



 