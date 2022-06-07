# CIS-422-DAN
The Doggy Adoption Network by Elizabeth, Evan, Jack, and Nathan.
This program is implemented in a webapp. We developed the program using the flask development server. After downloading the source files, you need to install the dependencies, and run the application on your device’s development server.

Installing dependencies:
Option 1: Run the bash command:
./install-dan
From within the DANv1 directory. This will install all of the dependencies for the project.
Option 2: Manually install all of the dependencies by running the following pip install commands (note, you will need to have the latest version of pip installed on your device):
	pip install pandas
pip install numpy
pip install mysql-connector
pip install flask
pip install flask_wtf

If you don’t want to install these dependencies on your machine, you might want to instead install them in a virtual environment.

Running the program:
	This program can be run using the bash command from inside of the DANv1 directory:
	./run
	If this is unsuccessful for any reason, the command “python3 main.py” will also work.
After the program is run, the terminal will output information about the development server, and it will print the address of the development server.

 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
 * Restarting with watchdog (fsevents)
 * Debugger is active!
 * Debugger PIN: 316-158-054

Copy this address into a web browser, and it will bring you to the deployed application running on your device.
