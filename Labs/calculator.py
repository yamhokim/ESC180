def display_current_value():
    print("Current Value: ", current_value)

def add(to_add):
    global current_value, temp
    temp = current_value
    current_value += to_add


def multiply(to_multiply):
    global current_value, temp
    temp = current_value
    current_value *= to_multiply

def division(to_divide):
    global current_value, temp
    if to_divide == 0:
        print("Can't divide by zero dummy!")
    else:
        temp = current_value
        current_value /= to_divide

def memory():
    global current_value, temp
    memory = current_value

def recall():
    global current_value
    if memory is None:
        print("No memory")
    else:
        current_value = memory

def undo():
    global current_value, temp
    current_value, temp = temp, current_value


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     if __name__ == '__main__':
    current_value = 0
    print("Welcome to the calculator program\n Current Value: ", current_value)
    add(5)
    display_current_value()
    multiply(4)
    display_current_value()
    division(2)
    display_current_value()
    undo()
    display_current_value()
