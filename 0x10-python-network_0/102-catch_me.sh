#!bin/bash
# a Bash script that makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!, in the body of the response.
curl -sLX PUT -d "You got me!" -o /dev/null -w 'You got me!\n' 0.0.0.0:5000/catch_me
