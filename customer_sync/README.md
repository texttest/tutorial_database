# Customer Sync

This is designed to simulate a legacy code situation. You've inherited a large database and a script designed to update it with additional customer data. The exercise is to write regression tests for the python code and check it updates the database consistently. When you have those regression tests in place you'll be able to refactor the python code with confidence.

The legacy database is simulated by the file 'legacy.db', which is a sqlite3 database containing only one record. You'll have to imagine that in reality this file would have thousands if not millions of records. there is a sql file that can be used to recreate this db - 'src/database.sql'. There is a python script 'test/dump_db.py' which will write the contents of it to files suitable for dbtext to use as input in a test case.

The code under 'src' is a fragment of a larger system. You'll have to imagine that in reality there would be tens or hundreds of such scripts. The 'test/test_rig.py' is designed to exercise this code for test purposes. It takes a file 'incoming.json' which contains the ExternalCustomer data. It also uses dbtext to set up a database of customers for it to be synchronized with. There are several example 'incoming.json' files in the 'test' folder.

## The code to refactor

The 'CustomerSync' class has a method 
 'syncWithDataLayer' method that take a ExternalCustomer instance, and will incorporate data from it into the corresponding Customer record in our system. This ExternalCustomer has been updated in an external system, and may or may not have a matching Customer in our database. If there is not, create a new Customer to match the incoming ExternalCustomer. If there is one, update it. If there are several matching Customers in our database, update them all (slightly differently).




