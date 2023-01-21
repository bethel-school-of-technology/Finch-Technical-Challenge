## Ask - 
+ Create a web application in your favorite language that calls Finch’s Sandbox API to get an access token.
+ Use the access token to get the employer’s full employee directory.
+ Your user interface should allow each individual employee to be selected and show the employee's personal and employment data.



## Setup
This app has been implement using Python 3 on the backend with Flask 2.2 on the front end to render the UI elements

1. Clone this repo
2. Make sure you have python installed on your machine
3. Next, you must create a Python virtual environment.
```
python3 -m venv venv
$source venv/bin/activate
```
4. Installing Dependencies - The first step is to install the Flask Python package
```
$pip install Flask==1.1.2
```

## Running the Flask app
+ To launch the Flask app locally, run the following command
```
flask run
```
+ By default, Flask will run the application you defined in app.py on port 5000. While the application is running, go to http://localhost:5000 using your web browser