# CYB333-Project
This script does not require and dependencies or repositories. This script is able to be executed and used entirley off of Python's built in functionalities.

The purpose of the scirpt is to limit the manual scrubbing of extensive logfiles. This script is able to automate that process and parse the logs on behalf of the executor and present the user with an easy to read output.

In order to execute the script ensure that Python3 is installed.
You can replace "webapp.log" in webapp = open("destination of file here", "r") with the destination file. 
You can then run the script.

Note the script will only search for lines containing the phrases I set as search parameters i.e. login failed, unauthorized access, and api error. 
