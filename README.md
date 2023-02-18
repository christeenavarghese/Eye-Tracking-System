# Eye_Tracking_Project_Module
This is the project files for project module of THWS MAI (2022-2023). The application is build to help parents of children with special needs such as Autism Spectrum Disorder (ASD) to have a portable eye tracking application that is integrated with a game and can produce data representation that can track the User's condition.  The hardware required to run this Application must be affordable and preferably laptops with built-in webcams. 

# Contributors and Special Thanks
This project will not be possible with the other members of the group: 
1. https://github.com/christeenavarghese
2. https://github.com/HananHujaily
3. https://github.com/Simprabh
4. https://github.com/tengguna

Special Thanks to our Professor for supervising us:
Prof. Dr. Magda Gregorová


# Minimum Requirements
Disclaimer: Our group run this in Macbook Air M1 (2020), we occassionaly also run it in Windows 11 but there might be errors that we have not detect yet.
1. Laptop with a built-in webcam of 720p.
2. Already has the latest Anaconda installed. 
3. Already installed all the required library packages (check in Quick guide on running the code). 

# Quick guide on running the code
Here is the general guide if you are interested in running the code in your respective laptops or PC. 
1. Clone the project
```shell
git clone https://github.com/vincentw1997/Eye_Tracking_Project_Module.git
```
2. Install all the required libraries by copying this block of code and pasting it in your Terminal
```shell
conda create -n testing python=3.8.15
conda activate testing
python -m pip install opencv-contrib-python
python -m pip install caer
python -m pip install cmake
python -m pip install numpy
python -m pip install pygame
python -m pip install matplotlib
python -m pip install pandas
python -m pip install dlib
python -m pip install tk
python -m pip install pysqlite3
python -m pip install pillow
python -m pip install requests
python -m pip install openpyxl
```
4. Press y and confirm when prompted
5. Make sure that all the dependencies are installed properly
6. Download trained dataset (shape_predictor_68_face_landmarks.dat) from this webpage (https://github.com/davisking/dlib-models/blob/master/shape_predictor_68_face_landmarks.dat.bz2). Click download, extract and put it inside gaze_tracking folder.
7. Running the eye tracking and game part (again copy paste to terminal)
```shell
python combine_all_final.py
```
8. Running the data processing part
```shell
python data_processing.py
```

# Complete Overview
The eye tracking application consist of 4 main parts: 
1. Eye tracking
2. Head tracking
3. Game 
4. Data representation

First 3 parts are combined into the file combine_all_final.py. Where as the Data representation part are still separated from the main Python script. The combine_all_final.py will produce 2 Excel files (.xlsx) namely game_2.xlsx and Output_5.xlsx. 

game_2.xlsx will will show the movement of the cartoon characters based on the setting choosen during the gameplay Details of each columns are shown below:
1. Column A is the X-axis coordinates movement of the cartoon characters.
2. Column B is the Y-axis coordinates movement of the cartoon characters.
3. Columns C and D are the time taken since running the code.
4. Columns F, G and H are the counting for when the cartoon character is on left, center or right side of the frame respectively. 
5. Columns J and K are the counting for when the cartoon character is on the upper side or lower side of the frame respectively.

Output_5.xlsx will show the captured left eye coordinates given that the User is following the movement of the cartoon character and the head tracking is showing 'GOOD!' meaning the orientation of the head is perfect. Details of each column are shown below:
1. Column A is the time where the data is collected.
2. Column B is the X-axis coordinates of the centroid of the Iris (Pupil). 
3. Column C is the Y-axis coordinates of the centroid of the Iris (Pupil).
4. Columns E, F and G are the counters for the left, center or right for the pupil with respect to the frame respectively. 
5. Columns I and J are the counters for looking up and down respectively.

Data representation part will run when User run data_preprocessing.py. The output will be a graph and another Excel file (Data.xlsx) represented based on the data in previous 2 Excel files (game_2.xlsx and Output_5.xlsx).

Data.xlsx have its details of the columns already named in the Excel file itself.

# Future Works
Possible future works for this project are as follows:
1. Improving the accuracy of the eye tracking. 
2. Increase the sizes of the game area and tweak the range parameters for the counting of both game and eye tracking (left, center, right, up and down ranges)
3. Possibly using new models that not require a very strict parameter for the head tracking. 
4. Adding features such as stop buttons in the tracking and game part.
5. Combining both the eye tracking part and the data processing part into one integrated part. 
6. Adding website interface for better UX and UI. 

# Noteable Resources
We build this app based on several already established eye tracking and head tracking pipelines. If you are intrested with their works, please gave them a star. Here are several resources that you might want to look into:
1. https://github.com/antoinelame/GazeTracking (Eye tracking)
2. https://github.com/Doruk-Dilmen/Python-Gaze-estimation--Eye-tracking--using-single-low-cost-web-am-and-visualization-of-data (Eye Tracking)
3. https://learnopencv.com/head-pose-estimation-using-opencv-and-dlib/ (Head Tracking)
