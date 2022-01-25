# gudlift-registration

1. Why


    This is a proof of concept (POC) project to show a light-weight version of our competition booking platform. The aim is the keep things as light as possible, and use feedback from the users to iterate.

2. Getting Started

    This project uses the following technologies:

    * Python v3.9.1+

    * Flask v2.0.1+

        Whereas Django does a lot of things for us out of the box, Flask allows us to add only what we need. 
     

    * [Virtual environment](https://virtualenv.pypa.io/en/stable/installation.html)

        This ensures you'll be able to install the correct packages without interfering with Python on your machine.

        Before you begin, please ensure you have this installed globally. 


3. Installation

    - After cloning, change into the directory and type <code>virtualenv .</code>. This will then set up a a virtual python environment within that directory.

    - Next, type <code>source bin/activate</code>. You should see that your command prompt has changed to the name of the folder. This means that you can install packages in here without affecting affecting files outside. To deactivate, type <code>deactivate</code>

    - Rather than hunting around for the packages you need, you can install in one step. Type <code>pip install -r requirements.txt</code>. This will install all the packages listed in the respective file. If you install a package, make sure others know by updating the requirements.txt file. An easy way to do this is <code>pip freeze > requirements.txt</code>

    - Flask requires that you set an environmental variable to the python file. However you do that, you'll want to set the file to be <code>server.py</code>. Check [here](https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application) for more details. Ex. (in your terminal): export FLASK_APP=server.py

    - You should now be ready to test the application. In the directory, type either <code>flask run</code> or <code>python -m flask run</code>. The app should respond with an address you should be able to go to using your browser.

4. Current Setup

    The app is powered by [JSON files](https://www.tutorialspoint.com/json/json_quick_guide.htm). This is to get around having a DB until we actually need one. The main ones are:
     
    * competitions.json - list of competitions
    * clubs.json - list of clubs with relevant information. You can look here to see what email addresses the app will accept for login.

5. Testing

    * You are free to use whatever testing framework you like-the main thing is that you can show what tests you are using.

    * The latest issues present in the code were tested using pytest==6.2.5 and pytest-flask==1.2.0 and then resolved in their respective branches.
    
    * All tests (pytest) were run before and after the bugs and improvements were handled. The results for these tests are included as .txt files.
    
    1. You can find all bugs and improvements in the following branches: 
       1. improvement/points_display_board 
       2. bug/points_updates 
       3. bug/book_past_competitions 
       4. bug/book_more_than_12 
       5. bug/spend_more_than_own_points
       6. bug/unknown_email_crash 
       7. feature/3_points_per_place
    
    * In addition to the pytest results, locust performance results (regarding speed) are included via screenshots (before and after)

