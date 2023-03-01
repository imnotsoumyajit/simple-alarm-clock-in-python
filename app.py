from playsound import playsound
import time
# playsound("my-sound.mp3")

# Clear terminal and make everything in the same line 
# ANSI clear char that will manipulate the terminal

CLEAR="\033[2J"
CLEAR_AND_RETURN="\033[H" #return cursor to the home position and on the same line 

def alarm(secs):
    time_elapsed=0; #to keep track of How much time is elapsed
    print(CLEAR) #prints on the same line
    while(time_elapsed < secs):
        time.sleep(1) #wait for one second, and then continue
        time_elapsed+=1;
    
# from how many secs are left , fig out how many mins,hrs,days,etc.. are left and show it 
        time_left=secs-time_elapsed;
        minutes_left=time_left // 60      #in int eg: 130//60 = 2
        secs_left=time_left%60            #           130%60 = 10
        
        print(f'{CLEAR_AND_RETURN}The alarm will ring in {minutes_left:02d}minutes and {secs_left:02d}seconds')
    playsound("my-sound.mp3")

minutes=int(input("Enter Minutes : "))
seconds=int(input("Enter Seconds : "))
total_seconds=minutes*60 + seconds;
alarm(total_seconds)