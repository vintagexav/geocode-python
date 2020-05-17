# Mbrella move


This is a demo application. It will serve as a playground to discuss tech-to-tech during the next interview. Take a chance to demonstrate your clean code skills, while keeping in mind that the application will
not go to production. Therefore we don’t expect every edge case to be covered.

## Start

If you would like to store latitude/logitude of user address:
Provide Google API Key as environment variable in `GEOCODE_KEY`

Run without Docker (requires python 2.7)
`FLASK_APP=src/main.py FLASK_ENV=development flask run --port 5000`

Build with docker
`docker build -t mbrella .`

Run with docker
`docker run -p 5000:5000 mbrella`

Documentation:
`0.0.0.0:5000/files/documentation/`

Tests
`py.test test/test.py --log-cli-level=10 -s`

##  Improvements

- Additional endpoints, for instance /api/booking/confirm when a booking is confirmed 
- Move to Python 3.6 - for some reason requirements were failing with package `futures`
- Protect routes with user roles - see https://flask-user.readthedocs.io/en/latest/authorization.html
- Use JWT/ Session from Flask
- Encrypt ids 
- validate email
- Edge cases

##  Context

YourMove operates a free-floating private fleet of different sorts of vehicles: cars, bikes, motor scooters and kick scooters. Using a mobile application, a customer can book a vehicle, they choose a starting date and time, and a duration in order to make a reservation.

### Operations

Design a REST API with the following operations:


- Create a booking
- Retrieve a booking
- Delete a vehicle
- Update a user


### Bonuses

- Make sure a vehicle cannot be booked more than once at any given time
- We store the user address, and we want to geocode it (use a lib)
- Run the app in Docker

### Instructions

- Use a Python-based framework of your choice. If you have no preference, for instance because you do not have prior experience, prefer Django.
- We should be able to easily run your application on our computer.
- Upload your code to a private Github repository and grant us access (our usernames will be provided separately).
- Do not squash all your commits, nor push a single commit at the end. We will be looking at the history.
- Ignore all authentication concerns, but check the framework’s documentation: how would you protect your endpoints, with different roles (user, admin)?
