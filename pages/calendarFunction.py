import calendar
import datetime


def calendarFunction(month):
    months = [
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December'
    ]

    year = datetime.date.today().year
    today = datetime.date.today()
    days = calendar.monthcalendar(year, month)

    calendar_values = {
        'days': days,
        'month': months[month - 1],
        'year': year,
        'today': today
    }

    return calendar_values
