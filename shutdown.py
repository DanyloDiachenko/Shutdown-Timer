import os;



"""Initial Params:"""
shutdownTimeHoursMax = 24;
shutdownTimeHoursMin = 0;

shutdownTimeMinutesMax = 60;
shutdownTimeMinutesMin = 1;

infoHours = "Info: maximum hours to shutodwn: 24, minimum: 0.";
infoMinutes = "Info: maximum minutes to shutodwn: 60, minimum: 1.";

line = "---------------------------------------------------------";

def emptyStringLine():
    print("");
    print(line);
    print("");

i = False;



"""Global Logic:"""
while i == False:
    print(infoHours);
    print(infoMinutes);
    print("");
    shutdownTimeHours = int(input("Write a number of hours before shutdown your PC: "));
    shutdownTimeMinutes = int(input("Write a number of minutes before shutdown your PC: "));
    if shutdownTimeHours > shutdownTimeHoursMax: 
        print("");
        print("Writed number of hours is bigger than maximal value of shutdown time of hours.");
        emptyStringLine();
        shutdownTimeHours;
    elif shutdownTimeHours < shutdownTimeHoursMin:
        print("")
        print("Writed number of hours is less than minimal value of shutdown time of hours.");
        emptyStringLine();
        shutdownTimeHours;
    elif shutdownTimeMinutes > shutdownTimeMinutesMax:
        print("");
        print("Writed number of minutes is bigger than maximal value of shutdown time of minutes.");
        emptyStringLine();
        shutdownTimeMinutes;
    elif shutdownTimeMinutes < shutdownTimeMinutesMin: 
        print("");
        print("Writed number of minutes is less than minimal value of shutdown time of minutes.");
        emptyStringLine();
        shutdownTimeMinutes;
    else: 
        shutdownTimeSeconds = shutdownTimeHours * 3600 + shutdownTimeMinutes * 60;
        print("");
        print("Do u agree to your PC will shutodwn after: %s hours, %s minutes?" % (shutdownTimeHours, shutdownTimeMinutes));
        print('If you agree, type "yes", if you disagree type "no"');
        print("");
        answer = input("yes or no? ");
        if answer == "yes":
            i = True;
            os.system("shutdown /s /t %s" % shutdownTimeSeconds);
        else: 
            I = False;
            emptyStringLine();