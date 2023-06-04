# Enview Vehicle Alerts Application
This project demonstrates how to use Python flask to create web application for vehicle alerts.

Specifications for the project can be found here:
 [Enview Take Home](https://sepia-seahorse-5d3.notion.site/Backend-Take-Home-Exercise-2c3fa4eba8c246c3bb71429e319309b9).
 [enview_take_home.pdf](https://github.com/souravsarangi/enview-app-master/files/11646705/enview_take_home.pdf)

The tools used are:
* Python's `requests` package.
* Python's `flask` web framework.
* working with JSONs.
* modular programming

## Tasks
Your task is to build a service that accepts events from our IoT device and generates alerts.
- Use a web framework of your choice to build two APIs:
    - POST /event: Our IoT device will call this endpoint to send the driving event
    - GET /alert/{alert_id}: This endpoint will respond with a single alert of ID `alert_id`
- On getting an event, the service will store the event in a database. You may use a mock database- a simple in-memory data structure like a list will suffice. You will not be evaluated on your database integration.
- Every 5 minutes, there must be at least one run of our [rule](https://www.notion.so/Backend-Take-Home-Exercise-2c3fa4eba8c246c3bb71429e319309b9?pvs=21) on the events received in the past five minutes.
- It is OK for alerts to be generated up to five minutes after the [rule](https://www.notion.so/Backend-Take-Home-Exercise-2c3fa4eba8c246c3bb71429e319309b9?pvs=21) condition is met.
- When an alert is generated, it must be stored in the database with an associated unique ID.
- The alert must be made available through a [GET endpoint](https://www.notion.so/Backend-Take-Home-Exercise-2c3fa4eba8c246c3bb71429e319309b9?pvs=21).

## Demo


## Prerequisites
All required Python packages can be found in the `requirements.txt` file. Additionally, the provided `Makefile` can be used to created a virtual environment by running `make venv`. You will also need a Heroku account and have installed the Heroku CLI. For more information on the Heroku CLI, go to https://devcenter.heroku.com/articles/heroku-cli#download-and-install.

## Running the app locally using Flask
You may want to run the app using Flask locally before deploying it to Heroku, especially if you have made any changes to the code. To run locally:

1. clone the repository.
1. in the repository, run `make deploy`.
1. open the link provided in the command line.

If you are using Windows, you can:
1. create and activate the virtual environment.
1. `set FLASK_APP=enview_app/app.py` in the command line.
1. run `python -m flask run`.
1. open the link in the command line.

(Recommended) Alternatively, you can deploy using [Docker](https://www.docker.com/).
1. `docker build -t enview_app .`
1. `docker run -d -p 5000:5000 enview_app`

## Deploying to Heroku
Make sure your app is ready to be deployed to Heroku by running Flask locally. To deploy to Heroku:

1. clone the repository (if you haven't yet).
1. `heroku login` and enter your credentials.
1. `heroku create` or `heroku create app-name` where app-name is a custom app name.
1. `git push heroku master`.
1. `heroku config:set DEPLOY=heroku`.
1. `heroku open` or open the app online through your Heroku profile.

## Future work
Since this is a short demonstration of what can be done using Python for creating web application, one may consider extensions to the project. Some ideas include:
1. showing a plot of the forecast.
1. using client's location to display other location specific data.

## License
This project is distributed under the GNU General Purpose License. Please see `LICENSE` for more information.
