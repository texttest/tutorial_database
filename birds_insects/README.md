Birds Insects
=============

I enjoy watching the birds and insects in my garden. I would like there to be more birds so I have planted more flowers to attract insects and I would like to see if it has made a difference. I'm hoping more insects will also mean more birds, since birds eat insects. In order to analyze whether this is the case I have started noting down the birds and insects I observe every day. I will store this data in a database that I can later analyze. Perhaps if I plant more flowers I will get more insects and then more birds?

I make my notes in a file 'observations.csv', it looks like this:

	date,type,name
	2022-08-01,insect,bumblebee
	2022-08-02,bird,blackbird

There is an example file in this folder called 'observations.csv'

I have a database structure with two tables. The 'wildlife' table contains a row for each kind of insect or bird I observe in my garden. The 'observations' table contains a row for each observation. (One for each row in the spreadsheet). There is a file 'empty_db.sql' which can create an empty database with the right schema. There is also a folder 'db_tables' with some data for the birds and insects I expect I will observe.

Exercises
----------
TextTest is already set up with a test_rig.py that calls the code in 'load_observations.py'. There are currently no test cases though.

1. Create a test case using the 'observations.csv' file provided. The test should check the code can read the file and add these new entries to the 'observations' database table. 
2. Great excitement! I saw a *woodpecker*. This is a bird I haven't seen before. Create a new observations.csv file with this observation and a new test that checks not only that the observation is added to the database, but also that the 'wildlife' table is updated with the new type of wildlife. 
3. I got confused and managed to write the same observation twice in my csv file. (Observations of identical wildlife on the same day). This led to duplicated entries in my database which I wasn't happy about. Add a test to reproduce this problem.
4. Fix the code by updating the function 'add_observation' in 'load_observations.py':

    def add_observation(date, result, session):
        isodate = datetime.date.fromisoformat(date)
        stmt = select(Observation).filter_by(date=isodate, wildlife=result)
        results = session.execute(stmt).scalars().all()
        if not results:
            observation = Observation(date=isodate, wildlife=result)
            session.add(observation)

5. Check the test now works properly and no duplicate observations occur.
