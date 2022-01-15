# to be used to parse outlook calendar
import datetime as dt
import pandas as pd
import pywin32


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


# TO-DO: function to convert date to datetime obj before getting passed to get_calendar

def get_start_end_times(begin, end):
    cal = get_calendar(dt.datetime(2020, 1, 1), dt, dt.datetime(2020, 7, 31))

    cal_start = [event.start for event in cal]
    cal_end = [event.end for event in cal]

    df = pd.DataFrame({'start': cal_start,
                    'end': cal_end})
    return df

# cal[i].start => starting time for same meeting
