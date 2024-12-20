from graphics import *

progress_list = []
module_trailer_list = []
module_retriever_list = []
exclude_list = []

mark_list = [0, 20, 40, 60, 80, 100, 120]


def input_credits():
    global pass_credit, defer_credit, fail_credit
    for i in range(3):
        name = ['pass', 'defer', 'fail']
        while True:
            try:
                credit = int(input(f'Enter your {name[i]} credits: '))
                if credit not in mark_list:
                    print('out of range \n')
                    continue
                else:
                    if i == 0:
                        pass_credit = credit
                    elif i == 1:
                        defer_credit = credit
                    else:
                        fail_credit = credit
                    break
            except ValueError:
                print("Enter an integer")
    global outcome_tuple
    outcome_tuple = (pass_credit, defer_credit, fail_credit)


def prediction():
    input_credits()
    total = pass_credit + defer_credit + fail_credit
    while total != 120:
        print("total not equal 120")
        input_credits()
        total = pass_credit + defer_credit + fail_credit
        continue
    else:
        if pass_credit == 120:
            print('progress')
            progress_list.append(outcome_tuple)
        elif pass_credit == 100:
            print('module trailer')
            module_trailer_list.append(outcome_tuple)
        elif fail_credit >= 80:
            print('Exclude')
            exclude_list.append(outcome_tuple)
        else:
            print('module retriever')
            module_retriever_list.append(outcome_tuple)


def histrogram():
    win = GraphWin("Histogram Result", 800, 650)
    win.setBackground("white")

    title = Text(Point(200, 25), "HISTROGRAM RESULTS")
    title.setFace("arial")
    title.setSize(20)
    title.setStyle("bold")
    title.setTextColor("black")
    title.draw(win)

    progress_ll = len(progress_list)
    module_trailer_ll = len(module_trailer_list)
    module_retriever_ll = len(module_retriever_list)
    exclude_ll = len(exclude_list)
    total_ll = progress_ll + module_trailer_ll + module_retriever_ll + exclude_ll

    total_title = Text(Point(121, 600), f"{total_ll} , Outcomes In Total")
    total_title.setStyle("bold")
    total_title.setSize(18)
    total_title.draw(win)

    aLine = Line(Point(20, 550), Point(780, 550))
    aLine.draw(win)

    total_number_marks = progress_ll + module_trailer_ll + module_retriever_ll + exclude_ll
    x = 480 / total_number_marks  # to get the scale

    progress_height = 550 - (x * progress_ll)
    progress_rectangle = Rectangle(Point(30, progress_height), Point(212, 550))
    progress_rectangle.setFill("coral")
    progress_rectangle.draw(win)

    trailer_height = 550 - (x * module_trailer_ll)
    module_trailer_rectangle = Rectangle(Point(222, trailer_height), Point(404, 550))
    module_trailer_rectangle.setFill("cornsilk1")
    module_trailer_rectangle.draw(win)

    retriever_height = 550 - (x * module_retriever_ll)
    module_retriever_rectangle = Rectangle(Point(414, retriever_height), Point(592, 550))
    module_retriever_rectangle.setFill("cyan4")
    module_retriever_rectangle.draw(win)

    exclude_height = 550 - (x * exclude_ll)
    exclude_rectangle = Rectangle(Point(602, exclude_height), Point(784, 550))
    exclude_rectangle.setFill("darkslateblue")
    exclude_rectangle.draw(win)

    progress_title = Text(Point(121, 575), "Progress")
    progress_title.draw(win)

    trailer_title = Text(Point(313, 575), "Trailer")
    trailer_title.draw(win)

    retriever_title = Text(Point(503, 575), "Retriever")
    retriever_title.draw(win)

    exclude_title = Text(Point(693, 575), "Exclude")
    exclude_title.draw(win)

    total_progress = Text(Point(121, progress_height - 10), progress_ll)
    total_progress.draw(win)

    total_moduel_trailer = Text(Point(313, trailer_height - 10), module_trailer_ll)
    total_moduel_trailer.draw(win)

    total_module_retriever = Text(Point(503, retriever_height - 10), module_retriever_ll)
    total_module_retriever.draw(win)

    total_exclude = Text(Point(693, exclude_height - 10), exclude_ll)
    total_exclude.draw(win)

    try:
        win.getMouse()
        win.close()
    except:
        print()


def list_exstension():
    for i in progress_list:
        print(f'Progress List {i} \n')
    for j in module_trailer_list:
        print(f'Module Trailer List {j}\n')
    for k in module_retriever_list:
        print(f'Module Retriever List {k}\n')
    for l in exclude_list:
        print(f'Exclude List{l}\n')


def write_to_file():
    text_file = open("file.txt", 'a')
    for i in progress_list:
        text_file.write(f'Progress List {i} \n')
    for j in module_trailer_list:
        text_file.write(f'Module Trailer List {j}\n')
    for k in module_retriever_list:
        text_file.write(f'Module Retriever List {k}\n')
    for l in exclude_list:
        text_file.write(f'Exclude List{l}\n')

    text_file.close()


def read_file():
    text_file = open("file.txt")
    print(text_file.read())
    text_file.close()


prediction()
while True:
    choice = input("Enter q to quite or any key to continue")
    if choice == "q":
        histrogram()
        write_to_file()
        read_file()
        list_exstension()
        break
    else:
        prediction()