import subject


# ** CSCI 1001 [/] -> CSCI 1001
def get_subject_name(name):
    start_index = str.find(name, "* ") + 2
    end_index = str.find(name, " [")

    if end_index < 0:
        end_index = len(name)

    return name[start_index:end_index]


# open todo.txt for reading
f = open('todo.txt', 'r')
line = f.readline()
last_line = line
while len(line) > 0:
    # check if current line has ` :LOGBOOK: `
    if str.find(line, ":LOGBOOK:") > -1:
        # found a logbook
        subject_name = get_subject_name(last_line)

        print("Found a logbook")


    last_line = line
    line = f.readline()
f.close()
