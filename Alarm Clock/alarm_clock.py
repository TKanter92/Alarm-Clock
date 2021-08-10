# CLASS: Alarm Clock
# Author: Tyler Kanter
# Create Date: August 10th, 2021


# Constructor
class Alarm_Clock:
    def __init__(self, name):
        self.current_time = '' 
        self.alarm_status = False
        self.alarm_set_time = ''
        self.name = name

# Method(s)

    def detail_alarm_clock(self):
        self.current_time = input("What is the current time?")
        self.alarm_set_time = input("What time would you like to set your alarm for?")
    
    def name_printer(self):
        print("My name is " + self.name)

    # prints specifics
    def alarm_clock_specs(self):
        print('Current Time: ' + str(self.current_time))
        print('Alarm is set to: ' + str(self.alarm_set_time))

    # Turns alarm on or off
    def toggle_alarm(self):
        if (self.alarm_status == False):
            self.alarm_status = True
        else:
            self.alarm_status = False

    # Stores a time in the alarm set section
    def set_alarm_time(self, alarm_time):
        if (self.alarm_status == True):
            self.alarm_set_time = alarm_time
            print('Your alarm is currently set to ' + alarm_time + '.')
        else:
            print('You currently do not have an alarm set.')

    