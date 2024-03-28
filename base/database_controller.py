import pymysql

from base.utils.settings import SettingKeys, Settings


def connect():
    return pymysql.connect(host=SettingKeys.DB_HOST,
                           user=SettingKeys.DB_USER,
                           password=SettingKeys.DB_PASSWORD,
                           database=SettingKeys.DB_DATABASE)


class DataBase:
    def __init__(self):
        self.settings = Settings()


class DatabaseController(DataBase):
    def __init__(self):
        DataBase.__init__(self)

    @staticmethod
    def insert_data(data="", time=""):
        db = connect()
        cursor = db.cursor()
        query = "INSERT INTO insider.case (case_status, case_time) VALUES ('{}', '{}')".format(data, time)
        cursor.execute(query)
        db.commit()
        db.close()

