# nextepisodereminder
Problem Statement:
The script requires email address and list of favourite TV series for multiple
users as input. The prompt needs to be as follows:
Email address:
TV Series:
Store the input data in MySQLdb table(s).
Result Required
A single email needs to be send to the input email address with all the
appropriate response for every TV series. The content of the mail could
depend on the following use cases:
1. Exact date is mentioned for next episode.
2. Only year is mentioned for next season.
3. All the seasons are finished and no further details are available.
 
This Python scripts is able perform the above mentioned tasks successfully above mentioned tasks in very robust and efficient manner.Further more it can handle more cases like invalid input,invalid email,no valid information about the next episode is available.

Afterthat, I am storing the output data in database to decrease the execution time and computational power,whereas before using the data from database,I check the the information is updated by comparing it with Today's Date,thus making information valid.(I am only storing TV Series whose exact date of next episode are known and whose all season are finished, as all other cases are ambigious and need to  be updated time to time.)

To run this program on your system,follow given simple steps:
</br>
1.Python 3 must be installed if not:
      For Ubuntu:
      sudo add-apt-repository ppa:jonathonf/python-3.6
      sudo apt-get install python3.6
      For Windows:
      Download it from:
      https://www.python.org/downloads/ 
 2.Now install following libraries:
      pip install bs4
      pip install requests
      pip install NULL
      pip install smptlib
      pip install pymysql
3.Install MySQL in your device 
      For Ubuntu:
      Follow this steps:
      https://support.rackspace.com/how-to/installing-mysql-server-on-ubuntu/
      For Windows:
      Download it from:
      https://dev.mysql.com/doc/refman/8.0/en/windows-installation.html
 4.After logging with your passsword in MySQL, Create a database of name Innovacer
      CREATE DATABASE Innovacer;
      
