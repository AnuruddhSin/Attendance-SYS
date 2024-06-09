# Attendance System

Welcome to the Attendance System project! This project provides a comprehensive solution for managing student attendance using face recognition technology. The system is designed to be user-friendly, efficient, and secure, ensuring accurate and reliable attendance tracking for educational institutions.

![Home](SS%20Images/Home.png)

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **Face Recognition**: Utilizes advanced face recognition technology to mark attendance.
- **Student Management**: Allows for easy management of student data including adding, updating, and deleting student information.
- **Attendance Reports**: Generates detailed attendance reports in various formats.
- **Developer Panel**: Provides tools for developers to manage and modify system settings.
- **User-Friendly Interface**: Easy-to-use graphical interface for smooth operation.
- **Help and Support**: Integrated help and support features for troubleshooting and assistance.

## Installation

To set up the Attendance System on your local machine, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/AnuruddhSin/Attendance-SYS.git
   ```
2. **Navigate to the Project Directory**:
   ```bash
   cd Attendance-SYS/ATMS_GUI
   ```
3. **Install the Required Dependencies**:
   Ensure you have Python installed. Then, install the necessary Python packages:
   ```bash
   pip install -r requirements.txt
   ```
4. **Set Up the Database**:
   Import the provided SQL file to set up the database schema:
   ```bash
   mysql -u your_username -p your_password attendance_mangement.sql
   ```
5. **Run the Application**:
   Execute the main Python script to start the application:
   ```bash
   python main.py
   ```

## Usage

Once the application is running, you can navigate through the various features using the graphical interface:

1. **Home Screen**: The main dashboard displaying an overview of the system.
2. **Student Management**: Add, update, and delete student information.
3. **Attendance Panel**: Mark attendance using face recognition.
4. **Reports**: Generate and view attendance reports.
5. **Developer Panel**: Access tools for developers to manage system settings.
6. **Help and Support**: Access documentation and support resources.

### Screenshots

#### Home Screen
![Home Screen](SS%20Images/Home.png)

#### Student Management System
![Student Management](SS%20Images/Student_Mang_Sys.png)

#### Attendance Panel
![Attendance Panel](SS%20Images/attend_panel.png)

#### Photos Management
![Photos](SS%20Images/Photos.png)

#### Face Recognition
![Face Recognition](SS%20Images/Face_rec.png)

#### Developer Panel
![Developer Panel](SS%20Images/developer_pannel.png)

## Project Structure

The project is structured as follows:

```
ATMS_GUI/
├── .idea/                   # IDE configuration files
├── Resources/               # Resource files (images, etc.)
├── SS Images/               # Screenshots for README
├── __pycache__/             # Compiled Python files
├── attendance.csv           # Sample attendance data (CSV format)
├── attendance.py            # Attendance module
├── attendance.xlsx          # Sample attendance data (Excel format)
├── attendance_mangement.sql # SQL script for database setup
├── classifier.xml           # XML file for face recognition
├── developer.py             # Developer panel module
├── face_recognition.py      # Face recognition module
├── facenet.py               # Facenet module for face recognition
├── haarcascade_frontalface_default.xml # Haarcascade classifier for face detection
├── helpsupport.py           # Help and support module
├── main.py                  # Main application script
├── option_training_code_tensor.py # TensorFlow training code
├── student.py               # Student management module
├── training_data.py         # Training data module
└── requirements.txt         # Python dependencies
```

## Contributing

Contributions to this project are welcome! If you have suggestions for improvements or new features, please submit an issue or a pull request. Follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push the branch to your fork.
4. Submit a pull request with a detailed description of your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or support, please contact:
- **Name**: Anuruddh Singh
- **Email**: anuruddh7234@gmail.com

Feel free to reach out if you have any questions or need assistance with the project.

