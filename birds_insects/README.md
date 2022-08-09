# Birds Insects

I enjoy watching the birds and insects in my garden. I would like there to be more birds so I have planted more flowers to attract insects and I would like to see if it has made a difference. I'm hoping more insects will also mean more birds, since birds eat insects. In order to analyze whether this is the case I have started noting down the birds and insects I observe every day. I will store this data in a database that I can later analyze.

I make my notes in a file 'observations.csv', it looks like this:

	date,type,name
	2022-08-01,insect,bumblebee
	2022-08-02,bird,blackbird

There is an example file in this folder called 'observations.csv'

I have a database structure with two tables. The 'wildlife' table contains a row for each kind of insect or bird I observe in my garden. The 'observations' table contains a row for each observation. (One for each row in the spreadsheet). There is a file 'empty_db.sql' which can create an empty database with the right schema.

Write tests for the load_observations.py program that reads the spreadsheet and updates the database.
