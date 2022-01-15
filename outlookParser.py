# to be used to parse outlook calendar
import datetime as dt
import pandas as pd


# begin + end are datetime objects
def get_calendar(begin, end):
    outlook = win32com.client.Dispatch('Outlook.Application').GetNamespace('MAPI')
    calendar = outlook.getDefaultFolder(9).Items  # gets you all meetings in outlook calendar
    calendar.IncludeRecurrences = True
    calendar.Sort('[Start]')

    # setting time frame to focus
    # TO-DO: get time frame from when2meet and input here as restriction
    restriction = "[Start] >= '" + begin.strftime('%m/%d/%Y') + "' AND [END] <= '" + end.strftime('%m/%d/%Y') + "'"
    calendar = calendar.Restrict(restriction)
    return calendar  # at this point ur calendar obj is storing only events within ur desired time frame


cal = get_calendar(dt.datetime(2020, 1, 1), dt, dt.datetime(2020, 7, 31))

for i in range(len(cal)):
    cal_start = cal[i].start
    cal_end = cal[i].end

df = pd.DataFrame({'start': cal_start,
                   'end': cal_end})

# cal[i].start => starting time for same meeting
