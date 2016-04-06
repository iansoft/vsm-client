import datetime

def get_time_delta(dt):
    try:

        timedelta = datetime.datetime.now() - datetime.datetime.strptime(dt,"%Y-%m-%d %H:%M:%S")
        secs = timedelta.days * 3600 * 24 + timedelta.seconds
        ab = 1 if secs > 0 else -1
        days = abs(secs) / (3600 * 24) * ab
        hours = (abs(secs) - abs(days) * 3600 * 24) / 3600 * ab

        if (hours >= 1) or (days >= 1):
            return str(days) + "days, " + str(hours) + " hours ago"
        minutes = secs / 60
        if minutes >= 1:
            return str(minutes) + " minutes ago"
        return str(secs) + " seconds ago"
    except:
        return dt

def get_time_delta2(dt):
    try:
        timedelta = datetime.datetime.now() - datetime.datetime.strptime(dt,"%Y-%m-%d %H:%M:%S")
        secs = timedelta.days * 3600 * 24 + timedelta.seconds
        ab = 1 if secs > 0 else -1
        days = abs(secs) / (3600 * 24) * ab
        hours = (abs(secs) - abs(days) * 3600 * 24) / 3600 * ab
        if (hours >= 1) or (days >= 1):
            return str(days) + "days, " + str(hours) + " hours"
        minutes = secs / 60
        if minutes >= 1:
            return str(minutes) + " minutes"
        return str(secs) + " seconds"
    except:
        return dt

def get_time_delta3(secs):
    try:
        secs = int(float(secs))
        ab = 1 if secs > 0 else -1
        days = abs(secs) / (3600 * 24) * ab
        hours = (abs(secs) - abs(days) * 3600 * 24) / 3600 * ab
        if (hours >= 1) or (days >= 1):
            return str(days) + "days, " + str(hours) + " hours"
        minutes = secs / 60
        if minutes >= 1:
            return str(minutes) + " minutes"
        return str(secs) + " seconds"
    except:
        return secs