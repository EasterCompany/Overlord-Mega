# -*- coding: utf-8 -*-

from elang.sqlmem import Database
localDB = Database()

localDB.table(
    "clients",
    [
        ("id", 'INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE'),
        ("primary_email", 'TEXT NOT NULL UNIQUE'),
        ("date_of_birth", 'DATETIME NOT NULL'),
        ("date_of_register", 'DATETIME NOT NULL'),
    ]
)
localDB.table(
    "client_hashes",
    [
        ("id", 'INTEGER NOT NULL PRIMARY KEY UNIQUE'),
        ("ph", 'TEXT NOT NULL'),
        ("ek", 'TEXT NOT NULL'),
    ]
)
localDB.table(
    "client_personal",
    [
        ("id", 'INTEGER NOT NULL PRIMARY KEY UNIQUE'),
        ("first_name", "TEXT"),
        ("middle_names", "TEXT"),
        ("last_name", "TEXT"),
        ("alias", "TEXT"),
        ("primary_address", "TEXT"),
        ("home_phone_number", "TEXT"),
        ("mobile_phone_number", "TEXT"),
        ("work_phone_number", "TEXT"),
        ("employment_status", "TEXT"),
        ("employer", "TEXT"),
        ("occupation", "TEXT"),
        ("nationality", "TEXT"),
        ("drivers_license_number", "TEXT"),
        ("passport_number", "TEXT"),
    ]
)
