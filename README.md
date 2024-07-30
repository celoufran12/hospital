# Hospital Triage System

This is a simple Hospital Triage web application built using Flask and SQLite.

## Installation

1. Clone the repository:
    ```
    git clone https://github.com/yourusername/emergency_waitlist.git
    ```
2. Navigate to the project directory:
    ```
    cd emergency_waitlist
    ```
3. Install the dependencies:
    ```
    pip install -r requirements.txt
    ```
4. Initialize the database run the `init_db.py` script.
    

## Usage

1. Run the application:
    ```
    python app.py
    ```
2. Open your browser and go to `http://127.0.0.1:5000/` to view the patient waitlist.
3. Go to `http://127.0.0.1:5000/admin` to access the admin panel and manage patients.

## Project Details

This project is part of a series of assignments to build a web application. It includes:

- **HTML/CSS**: Frontend design
- **JavaScript**: Client-side interactions
- **Flask**: Server-side interactions using Python
- **SQLite**: Database management

### Application Features

- **Patient Management**: Add and view patients based on severity and wait time.
- **Admin Panel**: Administer the application by adding new patients. To access the admin panel, navigate to `/admin`.

## Developer and User Documentation

### Developer

- Clone the repository and install dependencies as mentioned above.
- Run `app.py` to start the server.

### User

- **Patients**: View the list of patients sorted by severity and wait time.
- **Admin**: Add new patients via the admin panel.


## Demo

### Screenshots

The following are screenshots of the 2 pages of the application/webapp. The regular user page (1st image) and the admin page where you can add, update or remove users/patients (2nd image).

![regular page](https://github.com/celoufran12/hospital/blob/main/regular_user_page.PNG)

![admin page](https://github.com/celoufran12/hospital/blob/main/admin_page.PNG)


### Video

Here's a video we've recorded demonstrating that the website works. The regular user page refreshes every 10 seconds to get the latest list.

[![Demo video](https://github.com/celoufran12/hospital/blob/main/regular_user_page.PNG)](https://github.com/celoufran12/hospital/blob/main/compressed_CSI3140_Hospital_demo.mp4)

<video width="320" height="240" controls>
  <source src="https://github.com/celoufran12/hospital/blob/main/compressed_CSI3140_Hospital_demo.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>
