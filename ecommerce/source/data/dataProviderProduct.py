import mysql.connector
class DataProviderProduct:

    def insert(self,product):

        try:
            connection=mysql.connector.connect(
                host="localhost",
                database="eco",
                user="root",
                password="750486"
            )
            query="insert into product (Id,Name,Description,Price,Category_Id1) values ('{0}','{1}','{2}','{3}','{4}')"\
                .format(product.getId(),product.getName(),product.getDescription(),product.getPrice(),product.getCategoryId())

            cursor=connection.cursor()
            cursor.execute(query)
            connection.commit()
            print(cursor.rowcount,"inserted successfully")
            cursor.close()
        except mysql.connector.Error as mysqlError:
            print(mysqlError.msg)

        except Exception as ex:
            print(ex)
        finally:
            if connection.is_connected():
                connection.close()
                print("mysql connection is closed")

    def getList(self):
        try:
            connection=mysql.connector.connect(
                host="localhost",
                database="eco",
                user="root",
                password="750486"
            )
            query="select*from product"
            cursor=connection.cursor()
            cursor.execute(query)
            result=cursor.fetchall()
            print("total category number : {0}".format(cursor.rowcount))
            for row in result:
                print("id             :{0}".format(row[0]))
                print("Name           :{0}".format(row[1]))
                print("Description    :{0}".format(row[2]))
                print("Price          :{0}".format(row[3]))
                print("CategoryId     :{0}".format(row[4]))
                print("************************")

        except mysql.connector.Error as mysqlError:
            print(mysqlError.msg)

        except Exception as ex:
            print(ex)

        finally:
            if connection.is_connected():
                connection.close()
                print("mysql connection is closed")
