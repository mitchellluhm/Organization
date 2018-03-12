import subject

subjects = []


# ** CSCI 1001 [/] -> CSCI 1001
def get_subject_name(name):
    start_index = str.find(name, "* ") + 2
    end_index = str.find(name, " [")

    if end_index < 0:
        end_index = len(name)

    return name[start_index:end_index]


def get_or_create_subject(name):
    print("in get or create")
    if len(subjects) > 0:
        for sub in subjects:
            if name == sub.get_name():
                print("Subject found")
                return sub

    print("Subject not found")
    new_subject = subject.Subject(name)
    subjects.append(new_subject)
    return new_subject


# open todo.txt for reading
f = open('todo.txt', 'r')
line = f.readline()
last_line = line
while len(line) > 0:
    # check if current line has ` :LOGBOOK: `
    if str.find(line, ":LOGBOOK:") > -1:
        # found a logbook
        subject_name = get_subject_name(last_line)

        subject_obj = get_or_create_subject(subject_name)

        print("Found a logbook")


    last_line = line
    line = f.readline()
f.close()
