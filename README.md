# HMS-tkinter

<h2>REQUIREMENTS FOR THE PROJECT :</h2>

1) Python language
2) VS Code editor or any other
3) Python modules used are specified in pyproject.toml

### To setup 

1. Open terminal in root directory of project
2. Install python with tkinter

```bash
# For Mac
$ brew install python-tk
```

for other OS refer: https://stackoverflow.com/questions/76105218/why-does-tkinter-or-turtle-seem-to-be-missing-or-broken-shouldnt-it-be-part

3. Install poetry
```bash
$ brew install poetry 
```

or 

```bash
$ pip install poetry
```

4. Install dependcies
```bash
$ poetry install
```

### To run

```bash
$ poetry run python Code/app_main.py
```

---
<br>

This project integrates what the student has learnt through the semester to analyze a given system requirement using Object Oriented (OO) techniques, design using UML class diagram, extract class relationships, and implement the system in Python.

### Implementation of the system.

1. Accept all the inputs and display the outputs. ✅
    1. Obvious
2. Implement the code to complete the process requirements. ✅
    1.  to write the core functionality of your hospital management system to ensure that it performs the tasks it is intended to do. Obvious
3. All inputs should be validated by testing the code using the try-except clause. ✅
4. Validation should include: not empty, data type validation, data range, no selection, etc. Use masked text box if applicable. ✅
5. Give proper error messages, in case there is some error. ✅
6. Implement a File Manager class which manages various text files, where it reads and stores data into various text files. It also has the main module (test code) of the system. ✅
    
    ```jsx
    class FileManager:
        def __init__(self, filename):
            self.filename = filename
    
        def read_data(self):
            try:
                with open(self.filename, 'r') as file:
                    data = file.read()
                return data
            except FileNotFoundError:
                return None
    
        def write_data(self, data):
            with open(self.filename, 'w') as file:
                file.write(data)
    
    # Main module (test code)
    if __name__ == "__main__":
        # Create an instance of FileManager
        file_manager = FileManager("data.txt")
    
        # Read data from the file
        existing_data = file_manager.read_data()
        if existing_data:
            print("Existing data:")
            print(existing_data)
        else:
            print("No existing data found.")
    
        # Write new data to the file
        new_data = input("Enter new data: ")
        file_manager.write_data(new_data)
    
        print("Data written successfully.")
    
    ```
    
7. The code must be well organized and documented. The use of good documentation, proper naming convention for files, classes, and variables is essential to integrate the modules of the project. ✅
8. It is important to make sure that each team implements all the requirements agreed in the business case report. (Check with your instructor what needs to be implemented if you have any difficulty in identifying the process). ✅
9. The output should display complete set of information. ✅

### GUI Interface Design.

1. Create a Python window form application and give proper name to the form/application. ✅
2. Using proper controls, design the form/window for the application. ✅
3. Customize the form/window color, background, font etc., ✅
4. Give proper names to the controls (Labels, Textbox etc.) ✅
5. The window/form design should be clear and complete. ✅
6. Your application should have at least four windows/forms with good navigation. ✅
7. Make sure that your application has consistent design, e.g. colors, fonts, font size, images used, forms location, etc. ✅
8. Customize the window/form properties and give proper title to the windows forms to make the application look & feel more professional. ✅
9. Customize the buttons with proper names. ✅
10. Have a proper reset button on each form and close button for the application. 

---

- [feedback.py](http://feedback.py) ✅
    - submiting data to `feedback.csv`

- [admin.py](http://admin.py) ✅
    - login authentication from `admin.csv`
- admin_profile.py  ❌
    - fetching data from `admin_details.csv`
- admin_profile_update.py ✅
    - fetching data from `admin_details.csv`
    - saving details to `admin_details.csv`
- admin_doctors.py ✅
    - fetching details from `doc_details.csv`
- admin_add_doctors.py
    - fetching and updating data in `doc_details.csv`
- admin_edit_doctors.py
    - fetching, updating and deleting in `doc_details.csv`
- admin_feedback.py ✅
    - fetching data from `feedback.csv`

- [emp.py](http://emp.py) ✅
    - authenticate from `employee.csv`
- emp_signup.py ✅
    - adding data to `employee.csv` and `doc_details.csv`
- doctor_profile.py ❌
    - fetching data from `doc_details.csv`
- doctor_profile_update.py ✅
    - fetching and updating details in `doc_details.csv`
- doctor_pat_hist.py ✅
    - fetching data from `pat_activity.csv` and `patient.csv`

- [patient.py](http://patient.py) ✅
    - authentication from `patient.csv`
- pat_signup.py ✅
    - adding data to `patient.csv` and `pat_details.csv`
- patient_profile.py ❌
    - fetching data from `pat_details.csv`
- patient_profile_update.py ✅
    - fetching and updating data in `pat_details.csv`
- patient_activity.py ✅
    - fetch and update