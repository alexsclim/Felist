# Felist
CS304 Database Project(Dragonboat Rostering App)

### Setup for OSX  
  
You should have the following installed:  
Python 2.7(Check this with `python -v`)  
Virtualenv  
Pip
Git  
SSH key is setup  
  
1) In the directory of your choice `mkdir felist`  
  
2) CD into your directory and run the command `virtualenv venv` to create your own virutal environment.   
Everytime you work on "Felist" make sure you activate your virtual environment by `. venv/bin/activate`
or `venv\scripts\activate` for Cool PC Users  
Deactivate it with `deactivate`.
  
3) Clone the repository into the Felist directory `git@github.com:alexsclim/Felist.git`  
  
4) CD into the app directory and then run the command `pip install -r requirements.txt`  
This will install Flask and all the other dependencies for the project.  
  
5) Make sure you are running MySQL locally. Then go into the _init_.py file and replace the stars in the line `app.config['MYSQL_DATABASE_PASSWORD'] = '******'` with your MySQL password for the username 'root'.  
  
6) Once you have your dependencies and are hosting MySQL locally, run the command in your root folder `./run.py` and view the project in your local browser under port 5000. If it says you do not have permission, use 'chmod a+x run.py' to change permissions.
