# teacherdict
# techtest

This is repository for the tech test for Halian International. The test requirement is as below


**Teacher Directory**
A client has requested we create a Directory app containing all the Teachers in a given school.
Each teacher should have the following information
First Name
Last Name
Profile picture
Email Address
Phone Number
Room Number
Subjects taught
Teachers can have the same first name and last name but their email address should be unique
A teacher can teach no more than 5 subjects
The directory should allow Teachers to filtered by first letter of last name or by subject.
You should be able to click on a teach in the directory and open up the profile page. From there you
can see all details for the teacher.
An Importer will be needed to allow Teachers details to be added to the system in bulk. This should
be secure so only logged in users can run the importer.
The CSV attached contains a list of teacher who need to be uploaded as well as the filename for the
profile image. Profile images are in the attached Zip file.
if an image is not present for the profile then you should use a default placeholder image.
You can use SQLite for the database backend for simplicity
Your code should be uploaded to either Github or Bitbucket. And have instructions on how to set up
the project and how to run it.


Please find below the  steps to setup the porject

1.  Clone or download the repository.
2.  It is better to run the project in Virtual Env. 
    Run ```python3 -m venv techtestenv```
3.  Run ``` source techtestenv/bin/activate```
4.  Now go inside the directory **teacherdict*** in the cloned project and run
    ``` pip install -r requirement.txt```
    This is download all the dependent packages.
5.  Now run from the same folder to bring up the local server.
    1. ```python manage.py makemigrations```
    2. ```python manage.py migrate```
    3. ```python manage.py runserver``
6. One the localserver is up visit http://127.0.0.1:8000/
