#!/usr/bin/env python

import dbtext, os

import load_observations

def main():
    testdbname = "ttdb_" + str(os.getpid())  # some temporary name not to clash with other tests

    with dbtext.MSSQL_DBText(testdbname) as db:
        # Arrange
        db.create(sqlfile="empty_db.sql")

        # Act
        connection_string = db.get_connection_string()
        load_observations.main(connection_string)

        # Assert
        db.dumpchanges("{type}.json", exclude="trace*")

if __name__ == "__main__":
    main()