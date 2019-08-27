# Import urllib.request module to fetch URLs
from urllib.request import Request, urlopen
from urllib.error import URLError

# Variable that detects when to exit while loop
success = 0

# while loop to continually ask user to re-enter URL if the URL does not respond as expected
while success == 0:

    # Get URL from user
    url = input("Enter URL: ")
    print("You entered ", url)

    # Set a req variable equal to the HTTP Request for the user inputted URL
    req = Request(url)

    # First try to see if the URL will resolve with the given HTTP Request
    # If the URL comes back with a HTTP response, print out the page contents
    try:
        response = urlopen(req)
        print(response.read())

    # If the URL does not resolve with the given HTTP Request
    # Output to the screen the specific error reason and code, then prompt the user to re-enter URL
    except URLError as e:
        if hasattr(e, 'reason'):
            print('*** Error resolving to the server. Re-enter correct url. ***')
            print('Reason: ', e.reason)
            print('Code: ', e.code)

    # Upon the URL successfully resolving from the 'try' block, set the success variable to '1' to exit while loop
    # Then notify user the application will exit
    else:
        success = 1
        print('*** Thanks for using the URL Requester ***')
        print('*** Exiting Application ***')