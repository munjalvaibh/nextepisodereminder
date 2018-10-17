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
 
This Python scripts is able perform the above mentioned tasks successfully in very robust and efficient manner.Further more it can handle more cases like invalid input,invalid email,no valid information about the next episode is available.

**An additional feature is addeed, I am storing the output data in the database to decrease the execution time and computational power, whereas before using the data from the database,I check the information is up to date by comparing it with Today's Date, thus making information valid.(I am only storing TV Series those exact date of next episode are known and those all season are finished, as all other cases are ambiguous and need to be updated from time to time.)**

Script uses beautifulsoup libirary to pull out data from html files. 
<br>
Attaching the few screenshots for better understanding
<br>
<br>
To run this program on your system,follow given simple steps:
<br>
1.Python 3 must be installed if not:
      For Ubuntu:<br>
 <font color="green">
     sudo add-apt-repository ppa:jonathonf/python-3.6<br>
      sudo apt-get install python3.6<br></font>
      For Windows:<br>
      Download it from:<br>
      https://www.python.org/downloads/ <br>
 2.Now install following libraries:<br>
      pip install bs4<br>
      pip install requests<br>
      pip install NULL<br>
      pip install smptlib<br>
      pip install pymysql<br>
3.Install MySQL in your device<br> 
      For Ubuntu:<br>
      Follow this steps:<br>
      https://support.rackspace.com/how-to/installing-mysql-server-on-ubuntu/  <br>
      For Windows:<br>
      Download it from:<br>
      https://dev.mysql.com/doc/refman/8.0/en/windows-installation.html<br>
 4.After logging with your passsword in MySQL, Create a database of name Innovacer<br>
      CREATE DATABASE Innovacer;<br>

