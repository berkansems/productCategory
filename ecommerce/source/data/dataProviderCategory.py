import mysql.connector


class DataProviderCategory:

    def insert(self, category):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                database="eco",
                user="root",
                password="750486")

            query = "INSERT INTO category (Id,Name,Description) VALUES ('{0}','{1}','{2}')" \
                .format(category.getId(),category.getName(), category.getDescription())

            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()
            print(cursor.rowcount, "record inserted successfully")
            cursor.close()
        except mysql.connector.Error as mysqlError:
            print(mysqlError.msg)
        except Exception as ex: # bunu anlatabilirmisiniz?
            print(ex)
        finally:
            if connection.is_connected():
                connection.close()
                print("Mysql connection is closed")

    def getList(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                database="eco",
                user="root",
                password="750486")

            query = "SELECT * FROM category"
            cursor = connection.cursor()
            cursor.execute(query)
            records = cursor.fetchall()
            print("Total Category Number : {0}".format(cursor.rowcount))
            cursor.close()
            for row in records:
                print("Id          : {0}".format(row[0]))
                print("Name        : {0}".format(row[1]))
                print("Description : {0}".format(row[2]))
                print("************************")

        except mysql.connector.Error as mysqlError:
            print(mysqlError.msg)

        except Exception as jjj:
            print(jjj)

        finally:
            if connection.is_connected():
                connection.close()
                print("Mysql connection is closed")