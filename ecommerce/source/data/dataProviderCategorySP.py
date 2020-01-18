import mysql.connector

from source.data.connectionString import ConnectionString


class DataProviderCategorySP:
    connection = None

    def getList(self):
        self.connection = ConnectionString.connectionStringEco()
        try:
            cursor = self.connection.cursor()
            cursor.callproc("getList")
            result = list(cursor.stored_results())[0].fetchall()
            for row in result:
                print("Id           :{0}".format(row[0]))
                print("Name         :{0}".format(row[1]))
                print("Description  :{0}".format(row[2]))
                print("______________________________")
        except mysql.connector.Error as mysqlError:
            print(mysqlError.msg)
        except Exception as ex:
            print(ex)
        finally:
            if self.connection.is_connected():
                self.connection.close()
                print("Mysql connection is closed")

    def getById(self, id):
        self.connection = ConnectionString.connectionStringEco()
        try:
            cursor = self.connection.cursor()
            cursor.callproc("getById2", [id])
            result = list(cursor.stored_results())[0].fetchall()
            for row in result:
                print("Id           :{0}".format(row[0]))
                print("Name         :{0}".format(row[1]))
                print("Description  :{0}".format(row[2]))
                print("______________________________")
        except mysql.connector.Error as mysqlError:
            print(mysqlError.msg)
        except Exception as ex:
            print(ex)
        finally:
            if self.connection.is_connected():
                self.connection.close()
                print("Mysql connection is closed")

    def insert(self, category):
        self.connection = ConnectionString.connectionStringEco()
        try:
            cursor = self.connection.cursor()
            cursor.callproc("insertCategory", [category.getName(), category.getDescription()])
            self.connection.commit()
            print("Final Result")
        except mysql.connector.Error as mysqlError:
            print(mysqlError.msg)
        except Exception as ex:
            print(ex)
        finally:
            if self.connection.is_connected():
                self.connection.close()
                print("Mysql connection is closed")

    # update, delete

    def update(self, category):
        self.connection = ConnectionString.connectionStringEco()
        try:
            cursor = self.connection.cursor()
            cursor.callproc("updateCategory", [category.getId(), category.getName(), category.getDescription()])
            self.connection.commit()
            print("updated successfully")
        except mysql.connector.Error as mysqlError:
            print(mysqlError.msg)
        except Exception as ex:
            print(ex)
        finally:
            if self.connection.is_connected():
                self.connection.close()
                print("Mysql connection is closed")

    def delete(self, id):
        self.connection = ConnectionString.connectionStringEco()
        try:
            cursor = self.connection.cursor()
            cursor.callproc("getlist")
            result = list(cursor.stored_results())[0].fetchall()
            for row in result:
                if row[0] == id:
                    cursor = self.connection.cursor()
                    cursor.callproc("deleteCategory", [id])
                    self.connection.commit()
                    print("deleted successfully")
                    break
            else:
                print("there is not such an Id")

        except mysql.connector.Error as mysqlError:
            print(mysqlError.msg)
        except Exception as jj:
            print(jj)
        finally:
            if self.connection.is_connected():
                self.connection.close()
                print("connection closed")
