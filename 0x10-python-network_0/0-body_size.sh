#!/bin/bash
# that takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -sI "$1:$2" | sed -n 's/Content-Length: \([0-9]*\)/\1/p'
