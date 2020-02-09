import mysql.connector

class ConnectionString:

    @staticmethod
    def connectionStringEco():
        connection = mysql.connector.connect(
            host="localhost",
            database="ecommerce",
            user="root",
            password="750486")
        return connection