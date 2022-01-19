import pymysql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'MyCMS',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': 3306
    }
}
def MySQLConnection():
    db = DATABASES["default"]
    try:
        connection = pymysql.connect(host=db["HOST"], user=db["USER"], password=db["PASSWORD"], database=db["NAME"])
        cursor = connection.cursor()
        return cursor, connection
    except Exception as exception:
        return False, False

def MySQLInsertResult(cursor, connection, id, name, vulnid, scanlog, result, date, ipaddress, port):
    sqlstring = "Insert into Result_result (`id`, `name`, `vulnid`, `ipdst`, `port`, `description`, `result`, `timestamp`) values(%s, '%s', '%s', '%s', %s, '%s', %s, "%(str(id), name, vulnid, ipaddress, str(port), scanlog, str(result))
    datestring = "str_to_date('" + str(date) + "', '%Y-%m-%d'));"
    sqlstring += datestring
    try:
        cursor.execute(sqlstring)
        connection.commit()
        return True
    except Exception as exception:
        print(exception)
        return False

def MySQLClose(database):
    try:
        database.close()
        return True
    except Exception as exception:
        return False

def ScanResultInsert(id, name, vulnid, scanlog, result, date, ipaddress, port):
    cursor, connection = MySQLConnection()
    print("1")
    if cursor is False:
        print("2")
        return False
    else:
        print("3")
        ret1 = MySQLInsertResult(cursor, connection, id, name, vulnid, scanlog, result, date, ipaddress, port)
        if ret1 is True:
            print("4")
            ret2 = MySQLClose(connection)
            if ret2 is True:
                print("5")
                return True
            else:
                print("6")
                del connection
                return False
        else:
            print("7")
            del connection
            return False




