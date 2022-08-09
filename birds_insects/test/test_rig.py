#!/usr/bin/env python

import dbtext, os

import load_observations

def main():
    testdbname = "ttdb_" + str(os.getpid())  # some temporary name not to clash with other tests

    # Switch dbtext.MSSQL_DBText for dbtext.Sqlite3_DBText or dbtext.MySQL_DBText as you prefer
    with dbtext.MSSQL_DBText(testdbname) as db:
        # Arrange
        db.create(sqlfile="empty_db.sql")

        # Act
        connection_string = db.get_connection_string()
        load_observations.main(connection_string)

        # Assert
        db.dumptables("dbtext", "*", exclude="trace*", usemaxcol="")

if __name__ == "__main__":
    main()