# Movie-Titles

This require Python 3. I used Python3.6 while I was implementing this function
This function will take one user command line argument and send a request using HTTP link
Once it receive response, it will process as Json data
It will store number of pages that it need to go through and number of expected result
Base on number of pages, it will go through one by one in for loop
During each pages, it will look for keyword 'Title' and store them to list
Then I check whether the list is empty or whether number of expected and actual result is the same or not
After that I used print using sorted() apit cuz I am not sure whether we want to permentally rearrange the whole list or not
I could add argparser for nicer userfriendly command line support
