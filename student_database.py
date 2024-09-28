#Student database management system

#Lets create a new function

def manage_student_database():
    student_list = []
    students_ID = 1
    names_of_students = [] #To store student names for checking duplications

    while True:
        student_names = input("Please enter student's name (or type 'stop'): ")
        print(f"""Please enter student's name (or type 'stop' to exit): {student_names} """)
        if student_names.lower() == 'stop':
            break

        if student_names in names_of_students:
            print(f"The {student_names} name already exists.")
            continue
        
        else:
            student_tuple = (students_ID, student_names)
            student_list.append(student_tuple)
            names_of_students.append(student_names)
            students_ID += 1

    print("\n Complete List of student_list")
    print(student_list)
    
    print("\nList of student_list with IDs:")
    
    for student in student_list:
        print(f"ID: {student[0]}, Name: {student[1]}")
        
    print(f"Total number of student_list: {students_ID}")   
    length_of_names = sum(len(student[1]) for student in student_list)
    print(f"Total length of all student names combined: {length_of_names}")
    
    if student_list:
        longest_name_length = 0
        shortest_name_length = None
        longest_student_name = None
        shortest_student_name = None
        
        for student in student_list:
            name_length = len(student[1])
            
            if name_length > longest_name_length:
                longest_name_length = name_length
                longest_student_name = student
                
            if shortest_name_length is None or name_length < shortest_name_length:
                shortest_name_length = name_length
                shortest_student_name = student
    
    print(f"Name with maximum letters is: {longest_student_name}")
    print(f"Name with minimum letters is: {shortest_student_name}")
    
    
manage_student_database()