def alarm_clock(day, vacation):
    week = '7:00' if not vacation else '10:00'
    weekend = '10:00' if not vacation else 'off'
    return week if day not in [0, 6] else weekend
