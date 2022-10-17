<div id="top"></div>


<!-- PROJECT LOGO -->
<br/>
<div align="center">
  <a href="https://github.com/KDerec/softdesk/blob/master/images/logo.png">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Test and debug a Python project</h3>
  <p align="center">
    This student project is the #8 of my training.<br>You can follow the previous <a href="https://github.com/KDerec/softdesk">here</a> and next one <a href="https://github.com/KDerec/CRM_epic_events">here</a>.
  </p>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#built-with">Built With</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project
### 🌱 Developped skills
- Analyze application performance with Locust.
- Implement a Python test suite.
- Handle errors and exceptions in Python.
- Debug the code of a Python application.

### 📖 Scenario
I work for **Güdlft**, a company that created a digital platform to coordinate strength competitions (deadlifting 🏋🏻‍♂️, strongman) exclusively for branded fitness apparel companies.  

Now, Güdlft has created a team called **Regional Outreach** to create a lighter (and less expensive) version of their current platform for regional organizers.  

The team drew up a list of functional specifications for a prototype, broken down into several phases.  
Sam, the main developer took care of **phase 1**, but he's getting sick, so I'm in charge of **fixing the bugs** in phase 1 and **adding the feature** expected in **phase 2**.

### 🚧 Project goal
The goal of the application is to streamline the management of competitions between clubs (hosting, registration, fees and administration).  
This is a proof of concept (POC) project, The aim is the keep things as light as possible, and use feedback from the users to iterate.  
The app is powered by **JSON** files. This is to get around having a DB until we actually need one. The main ones are:
    
* competitions.json - list of competitions
* clubs.json - list of clubs with relevant information. You can look here to see what email addresses the app will accept for login.


With the forked project, correct the **error**, **bugs** and add the **feature** of this issues section [here](https://github.com/OpenClassrooms-Student-Center/Python_Testing/issues).  

Create **tests** and **performance report**.

### 🚀 Deliverable
#### [Test coverage](https://github.com/KDerec/Python_Testing/blob/master/docs/pytest_coverage.JPG)
<a href="https://github.com/KDerec/Python_Testing/blob/master/docs/pytest_coverage.JPG"><img src="docs/pytest_coverage.JPG" alt="pytest-coverage">  
#### [Performance report](https://htmlpreview.github.io/?https://github.com/KDerec/Python_Testing/blob/master/docs/locust_report.html)
See complete report with request, response time statistics and beautiful charts [here](https://htmlpreview.github.io/?https://github.com/KDerec/Python_Testing/blob/master/docs/locust_report.html).
#### [Tests](https://github.com/KDerec/Python_Testing/tree/master/tests)
Unit tests for server.py and utils.py

<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

* [Python 3.9](https://www.python.org/)
* [Flask 1.1](https://flask.palletsprojects.com/en/2.2.x/)
* [Virtual environment](https://virtualenv.pypa.io/en/stable/installation.html)

**Before you begin, please ensure you have this installed globally.**

<p align="right">(<a href="#top">back to top</a>)</p>


## Installation

1. <a href="#python-installation">Install Python</a> ;
2. Clone the project in desired directory ;
   ```sh
   git clone https://github.com/KDerec/Python_Testing.git
   ```
3. Change directory to project folder ;
   ```sh
   cd path/to/Python_Testing
   ```
4. Create a virtual environnement ;
      ```sh
      virtualenv .
      ```
5. Activate the virtual environment ;
    * For Windows :
      ```sh
      Scripts\activate
      ```
    * For Linux :
      ```sh
      source bin/activate
      ```
6. Install package of requirements.txt ;
   ```sh
   pip install -r requirements.txt
   ```

<p align="right">(<a href="#top">back to top</a>)</p>


#### Python installation

1. Install Python. If you are using Linux or macOS, it should be available on your system already. If you are a Windows user, you can get an installer from the Python homepage and follow the instructions to install it:
   - Go to [python.org](https://www.python.org/)
   - Under the Download section, click the link for Python "3.xxx".
   - At the bottom of the page, click the Windows Installer link to download the installer file.
   - When it has downloaded, run it.
   - On the first installer page, make sure you check the "Add Python 3.xxx to PATH" checkbox.
   - Click Install, then click Close when the installation has finished.

2. Open your command prompt (Windows) / terminal (macOS/ Linux). To check if Python is installed, enter the following command (this should return a version number.):
   ``` sh
   python -V
   # If the above fails, try:
   python3 -V
   # Or, if the "py" command is available, try:
   py -V
   ```

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage
### Run the server
1. Change directory to flaskr folder ;
   ```sh
   cd path/to/Python_Testing/flaskr
   ```
2. Run the server ;
   ```sh
   python server.py
   ```

3. Go to http://127.0.0.1:5000/, login with an email accounts of [clubs.json](https://github.com/KDerec/Python_Testing/blob/master/flaskr/clubs.json), for example, john@simplylift.co and enjoy.

### Tests and coverage test
1. To run tests and coverage test, go to ;
   ```sh
   cd path/to/Python_Testing/tests
   ```
2. Enter the two commands below ;
   ```sh
   coverage run -m pytest
   coverage report -m
   ```
### Performance test
1. Run server (see above) ;
1. Go to ;
   ```sh
   cd path/to/Python_Testing/tests/performance_tests
   ```
2. Enter ;
   ```sh
   locust
   ```
3. Go to http://localhost:8089/, enter a number of users, spawn rate and host (http://127.0.0.1:5000/ by default) and click on "Start swarming".

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- CONTACT -->
## Contact
Kévin Dérécusson 👇🏻  
Email : kevin.derecusson@outlook.fr  
LinkedIn : https://www.linkedin.com/in/kevin-derecusson/  

<p align="right">(<a href="#top">back to top</a>)</p>


<i>This student project is the #8 of my training.<br>You can follow the previous <a href="https://github.com/KDerec/softdesk">here</a> and next one <a href="https://github.com/KDerec/CRM_epic_events">here</a>.</i>
