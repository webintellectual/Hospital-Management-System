import csv
from tkinter import messagebox
import shutil

class FileManager:

    meta_data = {
                    'patient': 
                        {
                        'filename': 'patient',
                        'filename2': 'pat_details',
                        'NameField': 'pat_name',
                        'last_second_field': 'blood_grp'
                        },
                    'doctor': 
                        {
                        'filename': 'employee',
                        'filename2': 'doc_details',
                        'NameField': 'emp_name',
                        'last_second_field': 'specialization'
                        }
                }

    def add_feedback(self, ref, name, email, feedback):
        try:
            # Check if inputs are not empty
            if not name or not email or not feedback:
                raise ValueError("All fields must be filled out.")

            # Check if inputs are of correct data type (str in this case)
            if not isinstance(name, str) or not isinstance(email, str) or not isinstance(feedback, str):
                raise ValueError("All inputs must be of string type.")

            # Check if inputs are within valid range (for example, not too long)
            if len(name) > 100 or len(email) > 100 or len(feedback) > 500:
                raise ValueError("Inputs are too long.")

            with open('database/feedback.csv', 'a', newline='') as f:
                writer = csv.writer(f)

                # If the file is empty, write the headers
                if f.tell() == 0:
                    writer.writerow(['name', 'email', 'feedback'])

                writer.writerow([name, email, feedback])

            # Clear the entry boxes
            ref.name_var.set("")
            ref.email_var.set("")
            ref.feedback_var.set("")

            messagebox.showinfo("Success", "Feedback submitted successfully!")

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def authenticate(self, ref, username, password, filename):
        try:
            # Check if inputs are not empty
            if not username or not password:
                raise ValueError("Username and password must be filled out.")

            # Check if inputs are of correct data type (str in this case)
            if not isinstance(username, str) or not isinstance(password, str):
                raise ValueError("Username and password must be of string type.")

            # Check if inputs are within valid range (for example, not too long)
            if len(username) > 50 or len(password) > 50:
                raise ValueError("Username or password is too long.")

            with open(f'database/{filename}.csv', 'r') as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    if row['username'] == username and row['password'] == password:
                        messagebox.showinfo("Login", "Login successful!")
                        ref.login_button(username, password)
                        return

            messagebox.showwarning("Login", "Invalid username or password!")

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    
    def sign_up(self, ref, name, username, password, mobile, role):
        try:
            # Check if inputs are not empty
            if not name or not username or not password or not mobile:
                raise ValueError("All the Fields are compulsory.")

            # Check if inputs are of correct data type (str in this case)
            if not isinstance(name, str) or not isinstance(username, str) or not isinstance(password, str) or not isinstance(mobile, str):
                raise ValueError("All inputs must be of string type.")

            # Check if inputs are within valid range (for example, not too long)
            if len(name) > 100 or len(username) > 50 or len(password) > 50 or len(mobile) != 10:
                raise ValueError("Inputs are too long or mobile number is not of length 10.")

            # Check if mobile number is numeric
            if not mobile.isnumeric():
                raise ValueError("Invalid mobile number.")

            filename1 = self.meta_data[role]['filename']
            filename2 = self.meta_data[role]['filename2']
            NameField = self.meta_data[role]['NameField']
            last_second_field = self.meta_data[role]['last_second_field']

            with open(f'database/{filename1}.csv', 'r') as csv_file: # filename
                reader = csv.DictReader(csv_file)
                for row in reader:
                    if row['username'] == username:
                        raise ValueError("Username already exist, please try to login or use other Username.")

            with open(f'database/{filename1}.csv', 'a', newline='') as csv_file: # filename
                fieldnames = [ NameField, 'username', 'password', 'mobile_no'] # Name field name
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writerow({NameField: name, 'username': username, 'password': password, 'mobile_no': mobile}) # Name field name

            with open(f'database/{filename2}.csv', 'a', newline='') as csv_file: # filename2
                fieldnames = ['username', 'name', 'age', 'gender', 'email', 'phone', last_second_field, 'password']  # last second field
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writerow({'name': name, 'username': username, 'password': password, 'phone': mobile, 'age': 'N/A', 'gender': 'N/A', 'email': 'N/A', last_second_field: 'N/A'}) # last second field

            messagebox.showinfo("Info", "Account Successfully created.")
            ref.create_button()

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def update_profile(self, ref, role):
        try:
            filename2 = self.meta_data[role]['filename2']
            last_second_field_name = self.meta_data[role]['last_second_field'] # blood_grp or specialization

            username = ref.username_var.get()
            name = ref.name_var.get()
            age = ref.age_var.get()
            gender = ref.gender_var.get()
            email = ref.email_var.get()
            phone = ref.phone_var.get()
            if role == 'doctor':
                last_second_field_value = ref.specialization_var.get()
            elif role == 'patient':
                last_second_field_value = ref.blood_grp_var.get()
            password = ref.passwrd_var.get()

            # Check if inputs are not empty
            if not username or not name or not age or not gender or not email or not phone or not last_second_field_value or not password:
                raise ValueError("All fields must be filled out.")

            # Check if inputs are of correct data type (str in this case)
            if not isinstance(username, str) or not isinstance(name, str) or not isinstance(age, str) or not isinstance(gender, str) or not isinstance(email, str) or not isinstance(phone, str) or not isinstance(last_second_field_value, str) or not isinstance(password, str):
                raise ValueError("All inputs must be of string type.")

            # Check if inputs are within valid range (for example, not too long)
            if len(username) > 50 or len(name) > 100 or len(age) > 3 or len(gender) > 10 or len(email) > 100 or len(phone) != 10 or len(last_second_field_value) > 50 or len(password) > 50:
                raise ValueError("Inputs are too long or phone number is not of length 10.")

            # Check if phone number is numeric
            if not phone.isnumeric():
                raise ValueError("Invalid phone number.")

            data = []
            with open(f'database/{filename2}.csv', 'r') as csv_file: # filename2
                reader = csv.DictReader(csv_file)
                for row in reader:
                    if row['username'] == username:
                        row['name'] = name
                        row['age'] = age
                        row['gender'] = gender
                        row['email'] = email
                        row['phone'] = phone
                        row[last_second_field_name] = last_second_field_value # last second field
                        row['password'] = password
                    data.append(row)

            with open(f'database/{filename2}.csv', 'w', newline='') as csv_file: # filename2
                fieldnames = ['username', 'name', 'age', 'gender', 'email', 'phone', last_second_field_name, 'password'] # last second field
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(data)

            messagebox.showinfo("Update", "Profile details updated successfully!")

            if role == 'doctor':
                from doctor_profile import doctor_Profile
                ref.withdraw()
                save = doctor_Profile(username,password)
            elif role == 'patient':
                from patient_profile import patient_Profile
                ref.withdraw()
                save = patient_Profile(username,password)
            save.mainloop()

        except ValueError as e:
            messagebox.showerror("Error", str(e))
    
    def update_admin_profile(self, ref):
        try:
            username = ref.username_var.get()
            name = ref.name_var.get()
            age = ref.age_var.get()
            gender = ref.gender_var.get()
            email = ref.email_var.get()
            phone = ref.phone_var.get()
            password = ref.passwrd_var.get()

            # Check if inputs are not empty
            if not username or not name or not age or not gender or not email or not phone or not password:
                raise ValueError("All fields must be filled out.")

            # Check if inputs are of correct data type (str in this case)
            if not isinstance(username, str) or not isinstance(name, str) or not isinstance(age, str) or not isinstance(gender, str) or not isinstance(email, str) or not isinstance(phone, str) or not isinstance(password, str):
                raise ValueError("All inputs must be of string type.")

            # Check if inputs are within valid range (for example, not too long)
            if len(username) > 50 or len(name) > 100 or len(age) > 3 or len(gender) > 10 or len(email) > 100 or len(phone) != 10 or len(password) > 50:
                raise ValueError("Inputs are too long or phone number is not of length 10.")

            # Check if phone number is numeric
            if not phone.isnumeric():
                raise ValueError("Invalid phone number.")

            temp_file = 'temp.csv'
            with open('database/admin_details.csv', 'r') as csv_file, open(temp_file, 'w', newline='') as temp_csv_file:
                reader = csv.DictReader(csv_file)
                fieldnames = reader.fieldnames
                writer = csv.DictWriter(temp_csv_file, fieldnames=fieldnames)

                writer.writeheader()
                for row in reader:
                    if row['username'] == username:
                        row['name'] = name
                        row['age'] = age
                        row['gender'] = gender
                        row['email'] = email
                        row['phone'] = phone
                        row['password'] = password
                    writer.writerow(row)

            shutil.move(temp_file, 'database/admin_details.csv')

            from admin_profile import Admin_Profile
            ref.withdraw()
            save = Admin_Profile(username,password)
            save.mainloop()

        except ValueError as e:
            messagebox.showerror("Error", str(e))
    
    def fetch_doc_pat_history(self, ref, username):
        pat_activity_data = []
        with open('database/pat_activity.csv', 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                if row['doctor'] == username:
                    pat_activity_data.append(row)

        with open('database/patient.csv', 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                for activity in pat_activity_data:
                    if activity['username'] == row['username']:
                        ref.treeview.insert("", "end", values=(row['pat_name'], activity['date'], activity['problem'], activity['medicines']))
    
    def populate_doctor_combobox(self, ref): 
        doctor_names = []
        with open('database/doc_details.csv', 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                doctor_names.append(row['username'])

        ref.doctor_combobox['values'] = doctor_names
    
    def fetch_patient_activities(self, ref):
        with open('database/pat_activity.csv', 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                ref.treeview.insert("", "end", values=(row['date'], row['problem'], row['medicines'], row['doctor']))
    
    def submit_pat_activity(self, ref, date, problem, medicines, doctor, username):
        try:
            # Check if inputs are not empty
            if not date or not problem or not medicines or not doctor or not username:
                raise ValueError("All fields must be filled out.")

            # Check if inputs are of correct data type (str in this case)
            if not isinstance(date, str) or not isinstance(problem, str) or not isinstance(medicines, str) or not isinstance(doctor, str) or not isinstance(username, str):
                raise ValueError("All inputs must be of string type.")

            # Check if inputs are within valid range (for example, not too long)
            if len(date) > 10 or len(problem) > 100 or len(medicines) > 100 or len(doctor) > 50 or len(username) > 50:
                raise ValueError("Inputs are too long.")

            with open('database/pat_activity.csv', 'r', newline='') as csv_file:
                reader = csv.DictReader(csv_file)
                rows = list(reader)
                sr_no = int(rows[-1]['sr no.']) + 1 if rows else 1

            with open('database/pat_activity.csv', 'a', newline='') as csv_file:
                fieldnames = ['username', 'date', 'problem', 'medicines', 'doctor', 'sr no.']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writerow({'username': username, 'date': date, 'problem': problem, 'medicines': medicines, 'doctor': doctor, 'sr no.': sr_no})

            ref.date_var.set('')
            ref.problem_var.set('')
            ref.medicines_var.set('')
            ref.doctor_var.set('')
            ref.date_entry.focus_set()

            ref.update_treeview()

        except ValueError as e:
            messagebox.showerror("Error", str(e))
    
    def fetch_doctors_data(self, ref):
        with open('database/doc_details.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                ref.treeview.insert("", "end", values=[row['username'], row['name'], row['age'], row['gender'], row['email'], row['phone'], row['specialization'], row['password']])

    def fetch_feedbacks(self, ref):
        with open('database/feedback.csv', 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                ref.treeview.insert("", "end", values=(row['name'], row['email'], row['feedback']))
