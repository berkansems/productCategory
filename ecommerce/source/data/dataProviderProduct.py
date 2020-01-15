import mysql.connector

from source.data.connectionString import ConnectionString
from source.data.dataProviderCategory import DataProviderCategory


class DataProviderProducts:

    def insert(self,product):
        try:
            self.connection=ConnectionString.connectionStringEco()
            query="Insert into products(Name,Description,Price,Category_Id) VALUES ('{0}','{1}','{2}','{3}')"\
            .format(product.getName(),product.getDescription(),product.getPrice(),product.getCategory_Id())
            cursor=self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            print(cursor.rowcount," row inserted successfully")
            cursor.close()
        except mysql.connector.Error as mysqlError:
            print(mysqlError.msg)
        except Exception as ll:
            print(ll)
        finally:
            if self.connection.is_connected():
                self.connection.close()
                print("connection closed")
    def getList(self):
        try:
            self.connection=ConnectionString.connectionStringEco()
            query="select * from products"
            cursor=self.connection.cursor()
            cursor.execute(query)
            result=cursor.fetchall()
            print(cursor.rowcount,"rows successfully found")
            dataProviderCategory=DataProviderCategory()

            for row in result:
                print("Id          :{0}".format(row[0]))
                print("Name        :{0}".format(row[1]))
                print("Description :{0}".format(row[2]))
                print("Price       :{0}".format(row[3]))
                #x=dataProviderCategory.getById(row[4])
                print("Category_Id :{0}".format(row[4]))
                dataProviderCategory.getById(row[4])
                print("**********************")
            cursor.close()
        except mysql.connector.Error as mysqlError:
            print(mysqlError.msg)
        except Exception as kk:
            print(kk)
        finally:
            if self.connection.is_connected():
                self.connection.close()
                print("connection Closed successfully")

    def Update(self,product):
        try:
            self.connection=ConnectionString.connectionStringEco()
            query="UPDATE products SET Name='{0}',Description='{1}',Price='{2}',Category_Id='{3}' where Id='{4}'"\
            .format(product.getName(),product.getDescription(),product.getPrice(),product.getCategory_Id(),product.getId())
            cursor=self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            print("updated successfully")
            cursor.close()
        except mysql.connector.Error as mysqlError:
            print(mysqlError.msg)
        except Exception as ka:
            print(ka)
        finally:
            if self.connection.is_connected():
                self.connection.close()
                print("connection closed")

    def getByCotegoryId(self,categoryId):
        try:
            self.connection=ConnectionString.connectionStringEco()
            query="Select*from products where Category_Id='{0}'".format(categoryId)
            cursor=self.connection.cursor()
            cursor.execute(query)
            result=cursor.fetchall()
            for row in result:
                print("Id          :{0}".format(row[0]))
                print("Name        :{0}".format(row[1]))
                print("Description :{0}".format(row[2]))
                print("Price       :{0}".format(row[3]))
                print("Category_Id :{0}".format(row[4]))
                print("-------------------------")
            cursor.close()
        except mysql.connector.Error as mysqlError:
            print(mysqlError.msg)
        except Exception as ka:
            print(ka)
        finally:
            if self.connection.is_connected():
                self.connection.close()
                print("connection closed")

    def delete(self,Id):
        try:
            self.connection=ConnectionString.connectionStringEco()
            query="DELETE FROM products WHERE Id='{0}'".format(Id)
            cursor=self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            print(cursor.rowcount,"row deleted successfully")
            cursor.close()
        except mysql.connector.Error as mysqlError:
            print(mysqlError.msg)
        except Exception as ka:
            print(ka)
        finally:
            if self.connection.is_connected():
                self.connection.close()
                print("connection closed")


