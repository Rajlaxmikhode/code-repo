class student_detalis:

    def calculate_average(self,marks_dict):
        count=0
        total=0
        for subject,marks in marks_dict.items():
            if subject!="name":
                total+=marks
                count+=1
        return total/count
           
    def get_student (self,student_id):
        students={"std101": {"name":"Saniya.H","Maths":89,"Science":90,"English":89,"hindi":98,"kannada":79,"English":76,"social":68},
            "std102": {"name":"Dheeraj.K","Maths":39,"Science":78,"English":79,"hindi":90,"kannada":79,"English":76,"social":57},
            "std103": {"name":"Pinki.R","Maths":99,"Science":88,"English":69,"hindi":97,"kannada":88,"English":56,"social":60},
            "std104": {"name":"Sheela.K.j","Maths":91,"Science":78,"English":70,"hindi":90,"kannada":77,"English":59,"social":59},
            }    
        if student_id not in students:
            print("Student not found")  
            return None
           
        data=students[student_id]
        avg= self.calculate_average(data)
        avg=round(avg,2)
        grade=self.calculate_grade(avg)
        print(f"{data['name']}\nAverage scored: {avg}, \n{grade}")
       # print(f"{name}\nAverage: {avg}\nGrade: {grade}")
        

    def calculate_grade(self,avg):
        if avg>=40:
            print("PASS")
        if avg<40:
            return "Grade-c"
        elif avg<70 and avg>=40:
            return "Grade-B"
        else:
            return "Grade-A"
        

    
s=student_detalis()
id=input("Enter your id: ").strip()
s.get_student(id)


        

        
