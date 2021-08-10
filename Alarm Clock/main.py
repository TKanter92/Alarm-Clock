# MAIN: Controller/Initiator of Application
# Author: Tyler Kanter
# Create Date: August 10th, 2021

# *** Imports:
from alarm_clock import Alarm_Clock

# ** Instantiation of Objects

alarm_clock_one = Alarm_Clock(input("What would you like to name the alarm clock?"))

Happy_Hour = Alarm_Clock(input("What would you like to name the alarm clock?"))

Daily_Reminder = Alarm_Clock(input("What would you like to name this alarm clock?"))

Lets_Celebrate = Alarm_Clock(input("What would you like this version of Alarm Clock to be named?"))

# ** Execution of Object Methods

alarm_clock_one.name_printer()
alarm_clock_one.detail_alarm_clock()
alarm_clock_one.alarm_clock_specs()


Happy_Hour.name_printer()
Happy_Hour.detail_alarm_clock()
Happy_Hour.alarm_clock_specs()


Daily_Reminder.name_printer()
Daily_Reminder.detail_alarm_clock()
Daily_Reminder.alarm_clock_specs()


Lets_Celebrate.name_printer()
Lets_Celebrate.detail_alarm_clock()
Lets_Celebrate.alarm_clock_specs()
