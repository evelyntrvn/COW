import datetime as dt
import pandas as pd
import win32com.client
import openpyxl

def get_calendar(begin,end):
    outlook = win32com.client.Dispatch('Outlook.Application').GetNamespace('MAPI')
    calendar = outlook.getDefaultFolder(9).Items
    calendar.IncludeRecurrences = True
    calendar.Sort('[Start]')
    restriction = "[Start] >= '" + begin.strftime('%m/%d/%Y') + "' AND [END] <= '" + end.strftime('%m/%d/%Y') + "'"
    calendar = calendar.Restrict(restriction)
    return calendar

def get_appointments(calendar,subject_kw = None,exclude_subject_kw = None, body_kw = None):

    if subject_kw == None:
        appointments = [app for app in calendar]
    else:
        appointments = [app for app in calendar if subject_kw in app.subject]

    if exclude_subject_kw != None:
        appointments = [app for app in appointments if exclude_subject_kw not in app.subject]

    cal_subject = [app.subject for app in appointments]
    cal_start = [app.start for app in appointments]
    cal_end = [app.end for app in appointments]
    cal_body = [app.body for app in appointments]

    df = pd.DataFrame({'subject': cal_subject,
                       'start': cal_start,
                       'end': cal_end,
                       'body': cal_body})
    return df

def make_cpd(appointments):
    appointments['Date'] = appointments['start']
    appointments['Hours'] = (appointments['end'] - appointments['start'])
    appointments.rename(columns={'subject':'Meeting Description'}, inplace = True)
    appointments.drop(['start','end'], axis = 1, inplace = True)
    summary = appointments.groupby('Meeting Description')['Hours'].sum()
    return summary

begin = dt.datetime(2021,1,1)
end = dt.datetime(2021,12,31)

cal = get_calendar(begin, end)
appointments = get_appointments(cal)
result = make_cpd(appointments)

# this just puts all the info into an xlsx sheet rn
result.to_excel('meeting hours.xlsx')