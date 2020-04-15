# -*- coding: utf-8 -*-
client_database_tables = (
    (
        "clients",
        (
            ("id", 'INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE'),
            ("primary_email", 'TEXT NOT NULL UNIQUE'),
            ("date_of_birth", 'DATETIME NOT NULL'),
            ("date_of_register", 'DATETIME NOT NULL'),
        )
    ),
    (
        "client_hashes",
        (
            ("id", 'INTEGER NOT NULL PRIMARY KEY UNIQUE'),
            ("ph", 'TEXT NOT NULL'),
            ("ek", 'TEXT NOT NULL'),
        )
    ),
    (
        "client_personal",
        (
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
        )
    ),
    (
        "client_payment_info",
        (
            ("id", 'INTEGER NOT NULL PRIMARY KEY UNIQUE'),
            ("bank", 'TEXT'),
            ("name_on_card", 'TEXT NOT NULL'),
            ("card_number", 'TEXT NOT NULL'),
            ("account_number", 'TEXT NOT NULL'),
            ("sort_code", 'TEXT NOT NULL'),
            ("expiry_date", 'DATETIME NOT NULL'),
            ("security_code", 'TEXT NOT NULL')
        )
    )
)
