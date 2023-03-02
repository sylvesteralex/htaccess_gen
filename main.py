import datetime

today = datetime.date.today()
python_birthday = datetime.date(1991, 2, 20)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print( (today - python_birthday).total_seconds() / 365.25/24/60/60 )
