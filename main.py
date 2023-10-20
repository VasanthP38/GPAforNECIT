import streamlit as st
st.title("GPA Calc")

subcredit={
     "Professional English- I": 3,
     "Calculus and Solid Geometry": 4,
     "Physics for Computer Engineers": 4,
     "Environmental Science": 3,
     "Python Programming": 3,
     "Engineering Graphics Laboratory": 2,
     "Python Programming Laboratory": 2,

     "Professional English- II": 3,
     "Complex Analysis and Laplace Transforms": 4,
     "Applied Physics": 3,
     "Chemistry for Computer Engineers": 4,
     "Structured Programming": 3,
     "Basics of Electronics Engineering": 3,
     "Structured Programming Laboratory": 2,
     "Electronics Laboratory": 2,

     "Probaility and Statistics": 3,
     "Data Structures using Python": 4,
     "OOPS using Java": 3,
     "Computer Architecture and Organization": 3,
     "Digital Electronics and Microprocessor": 3,
     "OOPS using Java Laboratory": 2,
     "Digital Electronics and Microprocessor Laboratory": 1,

     "Discrete Mathematics": 3,
     "Design and Analysis of Algorithms": 4,
     "Computer Networks and Internets": 3,
     "Database Management System": 3,
     "Operating System Principles": 3,
     "Software Engineering": 3,
     "Computer Networks and Internets Laboratory": 1,
     "Database Management System Laboratory": 2,
     "Operating System Principles Laboratory": 1,

     "Digital Signal Processing": 3,
     "Internet and Web Programming": 3,
     "Object Oriented Analysis and Design": 3,
     "Computer Graphics and Multimedia": 3,
     "Case Tools Laboratory": 2,
     "Computer Graphics and Multimedia Laboratory": 1,

     "Artificial Intelligence": 3,
     "Compiler Design": 3,
     "Cryptography and Network Security": 3,
     "Internet of Things Laboratory": 2,

     "Engineering Economcs and Financial Accounting": 3,
     "Machine Learning Techniques": 3,
     "Full Stack Development": 3,
     "Machine Learning Techniques Laboratory": 2
}
col1, col2 = st.columns([2, 2])
sublist=[]
credlist=[]
with col1:
    no_of_subjects = st.number_input("Enter number of subjects")
    ns=int(no_of_subjects)
    for i in range(ns):
        #subject= st.text_input(f"Enter Sub{i+1} Name")
        subject = st.selectbox(f"Enter Sub{i + 1} Name", subcredit)
        if subject:
            sublist.append(subject)
            credlist.append(subcredit[subject])
#    if len(sublist)==no_of_subjects:
#        st.write(sublist)
#        st.write(credlist)

gradeplist=[]
with col2:
    st.title("Grades Obtained")
    for i in range(ns):
        grade = st.text_input(f"Enter Grade Obtained in Sub{i + 1}")
        grade=grade.upper()
        if (grade == "O"):
            gradepoint = 10
        elif (grade == "A+"):
            gradepoint = 9
        elif (grade == "A"):
            gradepoint = 8
        elif (grade == "B+"):
            gradepoint = 7
        elif (grade == "B"):
            gradepoint = 6
        elif (grade == "A"):
            gradepoint = 5
        elif (grade == "RA" or grade == "AB"):
            gradepoint = 0
        if grade:
            gradeplist.append(gradepoint)
#    if len(gradeplist) == no_of_subjects:
#        st.write(gradeplist)


prolist=[]
for i in range(len(credlist)):
    prolist.append(credlist[i]*gradeplist[i])
if st.button("Calculate GPA"):
    gpa=sum(prolist)/sum(credlist)
    st.write(gpa)