class Convert:
    def __init__(self, upper=False, lower=False, split=False):
        self.upper = upper
        self.lower = lower
        self.split = split

    def __call__(self, func):
        def wrapper():
            text = input("Matnni kiriting: ")
            if self.upper:
                text = text.upper()
            if self.lower:
                text = text.lower()
            if self.split:
                text = text.split()
            return func(text)
        return wrapper
@Convert(upper=False, lower=True, split=True)
def process_text(text):
    return text

if __name__ == '__main__':
    print(process_text())



from datetime import datetime

def date_format(func):
    def wrapper(date_str):
        try:
            date = datetime.strptime(date_str, "%dth %b %Y")
        except ValueError:
            try:
                date = datetime.strptime(date_str, "%d/%m/%Y")
            except ValueError:
                print("Please use '6th Oct 2025' or '6/11/2025'.")
                return
        return func(date.year, date.month, date.day)
    return wrapper

@date_format
def process_date(year, month, day):
    return f"Year: {year}, Month: {month}, Day: {day}"


print(process_date("input date: "))