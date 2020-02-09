import mysql.connector

from source.data.connectionString import ConnectionString


class DataProviderCategory:
    connection=None

    def insert(self, category):
        try:
            self.connection=ConnectionString.connectionStringEco()
            query="INSERT INTO category(Name,Description) VALUES ('{0}','{1}')".format(category.getName(),category.getDescription())
            cursor=self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            print(cursor.rowcount,"row inserted successfully")
            cursor.close()
        except mysql.connector.Error as mysqlError:
            print(mysqlError.msg)
        except Exception as ss:
            print(ss)
        finally:
            if self.connection.is_connected():
                self.connection.close()
                print("connection is closed")

    def getList(self):
        global connection
        try:
            self.connection=ConnectionString.connectionStringEco()
            query="select * from category"
            cursor=self.connection.cursor()
            cursor.execute(query)
            result= cursor.fetchall()
            print("total imported rows are :{0}".format(cursor.rowcount))
            print("-----------------------")
            for row in result:
                print("Id           :{0}".format(row[0]))
                print("Name         :{0}".format(row[1]))
                print("Description  :{0}".format(row[2]))
            cursor.close()
        except mysql.connector.Error as mysqlError:
            print(mysqlError.msg)
        except Exception as kk:
            print(kk)
        finally:
            if self.connection.is_connected():
                self.connection.close()
                print("mysql closed successfully")

    def update(self,category):
        global connection
        try:
            self.connection=ConnectionString.connectionStringEco()
            query="UPDATE category SET Name='{0}',Description='{1}' where Id={2}"\
                .format(category.getName(),category.getDescription(),category.getId())
            cursor=self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            print(cursor.rowcount,"updated successfully")
            cursor.close()
        except mysql.connector.Error as mysqlError:
            print(mysqlError)
        except Exception as kk:
            print(kk)
        finally:
            if self.connection.is_connected():
                self.connection.close()
                print("connection close")

    def getById(self,id):
        global connection
        try:
            self.connection=ConnectionString.connectionStringEco()
            query="select * from category where id ='{0}'".format(id)

            cursor=self.connection.cursor()
            cursor.execute(query)
            result=cursor.fetchone()
            print(result)

            cursor.close()
        except mysql.connector.Error as MysqlError:
            print(MysqlError.msg)
        except Exception as something:
            print(something)
        finally:
            if self.connection.is_connected:
                self.connection.close()

    def delete(self,Id):
        global connection
        try:
            self.connection=ConnectionString.connectionStringEco()
            query="DELETE FROM category where Id={0}".format(Id)
            cursor=self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            print(cursor.rowcount,"deleted successfully")
            cursor.close()
        except mysql.connector.Error as mysqlError:
            print(mysqlError.msg)
        except Exception as ll:
            print(ll)
        finally:
            if self.connection.is_connected():
                self.connection.close()
                print("connection closed")