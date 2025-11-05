#AUTOMATIC NUMBER PLATE RECOGNITION

This project is a python application for automatic detection of number plate from a given car and also verifies the information from a local database on the system. The project can be implemented for surveillance, tollgate, security checkpoint etc

##TEST IMAGES
The test image are not included in this repository due to size limit.

You can download them here: https://drive.google.com/drive/folders/1JgbFq5HnR02n4iUyLwxEqNh2aHYaZQ7U?usp=drive_link

After downloading, extract the files into a folder named "TEST_IMAGES" at the project root.

##PROJECT DEPENDENCIES
**1. Python(3.0 and above)**
_Instead of above, you can just install_ **Anaconda** _it comes with some python dependencies preinstalled_
**2. DB-Browser for SQlite--- to manage and edit the database**

##Python Dependencies
1. Numpy
2. OpenCV
3. tkinker
4. Pillow
5. SQlite
6. pyperclip
7. Scikit-learn

##Installing python dependencies

1. Open the CMD or anaconda prompt
2. if CMD, navigate to the conda environment using 
	`conda activate`
3. if CMD, navigate to the file path as below
	`cd C:\Users\araoye\Desktop\Automatic_Number_Plate_Recognition`
4. install the necessary dependencies using 
	`pip install -r Requirements.txt
	the Requirements.txt contains the necessary python dependencies
5. if using anaconda prompt start from 3.

##Instructions to use

To use the project, follow the instructions below

1. Open the CMD or anaconda
2. if CMD, navigate to the conda environment using 
	`conda activate`
3. if CMD, naviagte to the file path as below
	`cd C:\Users\araoye\Desktop\Automatic_Number_Plate_Recognition\src`
	this file path will be different on your system
4. run gui.py using
	`python gui.py`
5. Select Image of the car to scan
6. Click Start to process
7. Use the any key on the system to exit the process and any key can also be used to start the process again
8. if using anaconda prompt start from 3.
