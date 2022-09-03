<div id="top"></div>


<!-- PROJECT LOGO -->
<br/>
<div align="center">
  <a href="https://github.com/KDerec/softdesk/blob/master/images/logo.png">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Test and debug a Python project</h3>
  <p align="center">
    This student project is the #8 of my training (<i>IN PROGRESS...</i>).<br>You can follow the previous <a href="https://github.com/KDerec/softdesk">here</a> and next one is in progress.
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
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project
This is a proof of concept (POC) project to show a light-weight version of our competition booking platform. The aim is the keep things as light as possible, and use feedback from the users to iterate.

The app is powered by [JSON files](https://www.tutorialspoint.com/json/json_quick_guide.htm). This is to get around having a DB until we actually need one. The main ones are:
    
* competitions.json - list of competitions
* clubs.json - list of clubs with relevant information. You can look here to see what email addresses the app will accept for login.
### 🌱 Developped skills
- Analyze application performance with Locust.
- Implement a Python test suite.
- Handle errors and exceptions in Python.
- Debug the code of a Python application.

### 🚀 Project goal
Correct the error, the four bugs and add the feature of the issues section [here](https://github.com/OpenClassrooms-Student-Center/Python_Testing/issues).  
Create test and performance report.

<p align="right">(<a href="#top">back to top</a>)</p>


### Built With

* [Python v3.x+](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/en/2.2.x/)
* [Virtual environment](https://virtualenv.pypa.io/en/stable/installation.html)

Before you begin, please ensure you have this installed globally.

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
      virtualenv.
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
7. Flask requires that you set an environmental variable to the python file. However you do that, you'll want to set the file to be `server.py`.  
   Check [here](https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application) for more details

8. You should now be ready to test the application. In the directory, type either <code>flask run</code> or <code>python -m flask run</code>. The app should respond with an address you should be able to go to using your browser.


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

In progress

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Kévin Dérécusson - kevin.derecusson@outlook.fr

Project Link: [https://github.com/KDerec/Python_Testing](https://github.com/KDerec/Python_Testing)

<p align="right">(<a href="#top">back to top</a>)</p>