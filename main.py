import streamlit as st
st.title("GPA Calc")

subcredit={"Probaility and Statistics":3, "Data Structures using Python": 4, "OOPS using Java": 3, "Computer Architecture and Organization":3, "Digital Electronics and Microprocessor":3, "OOPS using Java Laboratory":2, "Digital Electronics and Microprocessor Laboratory":1}
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
    if len(sublist)==no_of_subjects:
        st.write(sublist)
        st.write(credlist)

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
    if len(gradeplist) == no_of_subjects:
        st.write(gradeplist)


prolist=[]
for i in range(len(credlist)):
    prolist.append(credlist[i]*gradeplist[i])
if st.button("Calculate GPA"):
    gpa=sum(prolist)/sum(credlist)
    st.write(gpa)