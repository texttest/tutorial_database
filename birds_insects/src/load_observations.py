#!/usr/bin/env python

import csv

from sqlalchemy import create_engine, select
from sqlalchemy.engine import URL
from sqlalchemy.orm import Session

from model import Wildlife, Observation


def create_sqlalchemy_engine(connection_string):
	connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})

	engine = create_engine(connection_url)
	return engine


def main(connection_string):
	print("Loading observations")
	engine = create_sqlalchemy_engine(connection_string)
	with Session(engine, future=True) as session:
		with open("observations.csv") as f:
			reader = csv.DictReader(f, delimiter=",")
			for row in reader:
				print(f"loading {row}")
				date = row['date']
				type = row['type']
				name = row['name']
				stmt = select(Wildlife).filter_by(name=name, type=type)
				results = session.execute(stmt).scalars().all()
				if not results:
					wildlife = Wildlife(name=name, type=type)
					session.add(wildlife)
					results = [wildlife]
				for result in results:
					observation = Observation(date=date, wildlife=result)
					session.add(observation)
		session.commit()


if __name__ == "__main__":
	import sys
	if len(sys.argv) < 2:
		print("you must supply an argument - the name of the localdb database to connect to")
		sys.exit(-1)
	dbname = sys.argv[1]
	main("DRIVER={ODBC Driver 17 for SQL Server};SERVER=(localdb)\MSSQLLocalDB;Integrated Security=true;DATABASE={dbname};")