import re

days_dic = {'monday': 1, 'tuesday': 2, 'wednesday': 3,
            'thursday': 4, 'friday': 5, 'saturday': 6, 'sunday': 7}

days_dic_reverse = {v: k.capitalize() for k, v in days_dic.items()}

print(days_dic_reverse)


def add_time(start, duration, start_day=None):
    start_data = Time.parse(start)
    days_passed = start_data.increment_by(duration)
    end_day = calc_endday(start_day, days_passed)
    text = construct_text(start_data, end_day, days_passed)
    return text


def calc_endday(start_day, days_passed):
    if not start_day:
        return None

    start_day_index = days_dic[start_day.lower()]
    end_day_index = start_day_index + days_passed
    end_day_index = end_day_index % 7
    if end_day_index <= 0:
        end_day_index += 7

    return days_dic_reverse[end_day_index]


def construct_text(time, start_day, days_passed):
    text = initialize_text(time)
    text = append_day_if_needed(text, start_day)
    text = append_days_passed_if_needed(text, days_passed)
    return text


def initialize_text(time):
    return str(time)


def append_day_if_needed(text, day):
    if day:
        text = text + ', ' + day

    return text


def append_days_passed_if_needed(text, days_passed):
    if days_passed <= 0:
        return text
    elif days_passed == 1:
        return text + ' (next day)'
    else:
        return text + fr' ({days_passed} days later)'


class Time:
    def __init__(self, hours, minutes, period='AM'):
        hours = int(hours)
        self.hour = hours if period == 'AM' else hours + 12
        self.minute = int(minutes)

    def __str__(self):
        hour = self.hour
        minute = self.minute
        period = 'AM'
        if hour >= 12:
            period = 'PM'
        if hour > 12:
            hour -= 12
        if hour == 0:
            hour = 12
        return str(hour) + ':' + fill_string(str(minute), '0', 2) + ' ' + period

    @staticmethod
    def parse(data):
        parsed_data = parse_time(data)
        return Time(parsed_data[0], parsed_data[1], parsed_data[2])

    def increment_by(self, increment_data):
        hours, minutes = parse_time(increment_data)
        new_hour = self.hour + int(hours)
        new_minute = self.minute + int(minutes)

        if (new_minute >= 60):
            new_minute -= 60
            new_hour += 1

        days_passed = int(new_hour / 24)
        new_hour -= (days_passed * 24)

        self.hour = new_hour
        self.minute = new_minute

        return days_passed


def fill_string(string, symbol, max_size):
    spaces_to_add = symbol * (max_size - len(string))
    return spaces_to_add + string


def parse_time(data):
    pattern = r'\w+'
    return re.findall(pattern, data)


def add_date(base_date, increment):
    result = []
    result.append(int(base_date[0]) + int(increment[0]))
    result.append(int(base_date[1]) + int(increment[1]))
    result.append(base_date[2])
    return result


print(add_time('3:00 PM', '3:10'))
print(add_time('11:30 AM', '2:32', 'Monday'))
print(add_time('11:43 AM', '00:20'))
print(add_time('10:10 PM', '3:30'))
# Returns: 1:40 AM (next day)
print(add_time('11:43 PM', '24:20', 'tueSday'))
# Returns: 12:03 AM, Thursday (2 days later)
print(add_time('6:30 PM', '205:12'))
# Returns: 7:42 AM (9 days later)
