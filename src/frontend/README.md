## Create an environment

```bash
$ python3 -m venv venv
```

On Windows:

```bash
$ py -3 -m venv venv
```

## Activate the environment

Before you work on your project, activate the corresponding environment:

```bash
$ . venv/bin/activate
```

On Windows:

```bash
> venv\Scripts\activate
```

Your shell prompt will change to show the name of the activated environment.

## Install Flask

Within the activated environment, use the following command to install Flask:

```bash
$ pip install Flask
```

Flask is now installed. Check out the Quickstart or go to the Documentation Overview.

## Install the dependencies

```bash
$ pip install -r requirements.txt
```

To run the application you can either use the flask command or python’s -m switch with Flask. Before you can do that you need to tell your terminal the application to work with by exporting the FLASK_APP environment variable:

```bash
$ export FLASK_APP=front.py
$ flask run
 * Running on http://127.0.0.1:5000/
```

If you are on Windows, the environment variable syntax depends on command line interpreter. On Command Prompt:

```
C:\path\to\app>set FLASK_APP=back.py
```

And on PowerShell:

```
PS C:\path\to\app> $env:FLASK_APP = "back.py"
```

Alternatively you can use python -m flask:

```
$ export FLASK_APP=back.py
$ python -m flask run
 * Running on http://127.0.0.1:5000/
```

This launches a very simple builtin server, which is good enough for testing but probably not what you want to use in production. For deployment options see Deployment Options.

## Debug Mode

(Want to just log errors and stack traces? See Application Errors)

The flask script is nice to start a local development server, but you would have to restart it manually after each change to your code. That is not very nice and Flask can do better. If you enable debug support the server will reload itself on code changes, and it will also provide you with a helpful debugger if things go wrong.

To enable all development features (including debug mode) you can export the FLASK_ENV environment variable and set it to development before running the server:

```bash
$ export FLASK_ENV=development
$ flask run
```

(On Windows you need to use set instead of export.)

This does the following things:

it activates the debugger

it activates the automatic reloader

it enables the debug mode on the Flask application.

You can also control debug mode separately from the environment by exporting FLASK_DEBUG=1.

There are more parameters that are explained in the Development Server docs.
