import re
from datetime import datetime

import pandas as pd


def convert24(date):
    # Parse the time string into a datetime object
    t = datetime.strptime(date, ' %I:%M %p - ')
    # Format the datetime object into a 24-hour time string
    return t.strftime('%H:%M - ')


def preprocess(data):
    pattern_24 = '\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s-\s'
    pattern_12 = "\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s[apm]+\s-\s"

    messages_24 = re.split(pattern_24, data)[1:]
    dates_24 = re.findall(pattern_24, data)

    messages_12 = re.split(pattern_12, data)[1:]
    dates_12 = re.findall(pattern_12, data)

    date_12 = []

    for date in dates_12:
        temp = date.split(',')
        temp[1] = convert24(temp[1])
        str_fin = ", ".join(temp)
        date_12.append(str_fin)
        print(date_12)

    messages = messages_12 + messages_24
    dates = date_12 + dates_24

    df = pd.DataFrame({'user_message': messages, 'message_date': dates})
    # convert message_date type
    df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%y, %H:%M - ')

    df.rename(columns={'message_date': 'date'}, inplace=True)

    users = []
    messages = []
    for message in df['user_message']:
        entry = re.split(r'([\w\W]+?):\s', message)
        if entry[1:]:  # user name
            users.append(entry[1])
            messages.append(" ".join(entry[2:]))
        else:
            users.append('group_notification')
            messages.append(entry[0])

    df['user'] = users
    df['message'] = messages
    df.drop(columns=['user_message'], inplace=True)

    df['only_date'] = df['date'].dt.date
    df['year'] = df['date'].dt.year
    df['month_num'] = df['date'].dt.month
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute

    period = []
    for hour in df[['day_name', 'hour']]['hour']:
        if hour == 23:
            period.append(str(hour) + "-" + str('00'))
        elif hour == 0:
            period.append(str('00') + "-" + str(hour + 1))
        else:
            period.append(str(hour) + "-" + str(hour + 1))

    df['period'] = period

    return df
