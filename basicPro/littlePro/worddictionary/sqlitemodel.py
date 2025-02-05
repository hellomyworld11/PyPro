import os.path
import sqlite3

class SqliteModel(object):

    def __init__(self, filename, verbose=False):
        self.__dbname = filename
        if filename != ':memory:':
            os.path.abspath(filename)
        self.__conn = None
        self.__verbose = verbose
        self.__open()

    def __open(self):
        sql='''
        CREATE TABLE IF NOT EXISTS "stardict" (
            "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
            "word" VARCHAR(64) COLLATE NOCASE NOT NULL UNIQUE,
            "sw" VARCHAR(64) COLLATE NOCASE NOT NULL,
            "phonetic" VARCHAR(64),
            "definition" TEXT,
            "translation" TEXT,
            "pos" VARCHAR(16),
            "collins" INTEGER DEFAULT(0),
            "oxford" INTEGER DEFAULT(0),
            "tag" VARCHAR(64),
            "bnc" INTEGER DEFAULT(NULL),
            "frq" INTEGER DEFAULT(NULL),
            "exchange" TEXT,
            "detail" TEXT,
            "audio" TEXT
        );
        CREATE UNIQUE INDEX IF NOT EXISTS "stardict_1" ON stardict (id);
        CREATE UNIQUE INDEX IF NOT EXISTS "stardict_2" ON stardict (word);
        CREATE INDEX IF NOT EXISTS "stardict_3" ON stardict (sw, word collate nocase);
        CREATE INDEX IF NOT EXISTS "sd_1" ON stardict (word collate nocase);
        '''
        self.__conn = sqlite3.connect(self.__dbname, isolation_level = "IMMEDIATE")

