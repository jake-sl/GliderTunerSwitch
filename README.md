# GliderSwitch
 A Flask app for remotely triggering buttons on an antenna tuner. Intended for Raspberry Pi.

# Install on Raspberry Pi 3+

1. Install pip and required libraries
 `sudo apt install python3-pip`
 `pip3 install flask RPi.GPIO Flask-HTTPAuth`

2. Load code onto Raspberry Pi local memory 

3. Change the authentication keys hard coded into app.py

`
# Replace these with your own credentials
PASSWORD = "devanoogaishammy"

API_KEYS = {
    "api_user1": "bFc9gvadVgjH",
    "api_user2": "gZBUYUCAQnCM"
}

users = {
    "web_user": PASSWORD,
    **API_KEYS
}
`

4. Run the Flask app and start the server.
`export FLASK_APP=app.py
flask run --host=0.0.0.0`


## Other considerations:

1. Add the start command to system startup items (perhaps with @reboot in crontab)
2. Add `-p 3000` to to the flask run command to set the port to 3000 (or whatever) from the default 5000.
3. Note that you can add as many api users as needed, but there's a pre-shared password protecting the HTML web interface. We can probably deprecate the web interface in favor of the API working with a more comprehensive application.
4. I'd IP block every address outside of north america, since we all have VPN's and that will eliminate the majority of malicious traffic.
