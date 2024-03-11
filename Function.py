stu = ["Kannan", "Ravi", "Prabu"]


def result(ver: int, student: str):
    if ver >= 50:
        print("{0} has scored {1} - PASS".format(student, ver))
    elif ver < 50:
        print("{0} has scored {1} - FAIL".format(student, ver))


def score():
    for student in stu:
        def retry():
            try:
                ver = int(input("Please enter {0} Score: ".format(student)))
                while ver > 100 or ver < 0:
                    print("Please enter valid score")
                    ver = int(input("Please enter {0} Score: ".format(student)))
                result(ver, student)
            except ValueError:
                print("Please enter valid score")
                retry()
        retry()


score()
