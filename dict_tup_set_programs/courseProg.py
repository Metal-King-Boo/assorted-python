# course information problem

def main():
    courseRooms = {'CS101': '3004',
                   'CS102': '4501',
                   'CS103': '6755',
                   'NT110': '1244',
                   'CM241': '1411',}

    courseInstructors = {'CS101': 'Haynes',
                         'CS102': 'Alvarado',
                         'CS103': 'Rich',
                         'NT110': 'Burke',
                         'CM241': 'Lee',}

    courseTime = {'CS101': '8:00 a.m.',
                  'CS102': '9:00 a.m.',
                  'CS103': '10:00 a.m.',
                  'NT110': '11:00 a.m.',
                  'CM241': '1:00 p.m.',}

    courseKey = input("Enter a valid Course Number: ").upper()
    try:
        print("The Room for", courseKey, "is", courseRooms[courseKey])
        print("The Instructor for", courseKey, "is", courseInstructors[courseKey])
        print("The Meeting Time for", courseKey, "is", courseTime[courseKey])
    except KeyError:
        print("Invalid Course Number")
main()