import mysql.connector
import mysql
import mysql.connector.pooling
import app.service.config as cp
def db_connection(dbconfig):
    """Generate Database Connection"""
    cnxpool = mysql.connector.pooling.MySQLConnectionPool(pool_name="mypool",
                                                          pool_size=3,
                                                          **dbconfig)
    return cnxpool

def get_connection(dbconfig):
    """Calls Database connection method and returns connection"""
    cnxpool = db_connection(dbconfig)
    cnx1 = cnxpool.get_connection()
    return cnx1

def initiate_global_mysql_session():
    """Initiate Global database session"""
    dbconfig = {
        "host": cp.get_app_hostname(),
        "port": "3306",
        "user": cp.get_app_username(),
        "password": cp.get_app_password(),
        "database": cp.get_app_dbname(),
    }

    mysql_session = get_connection(dbconfig)
    cursor = mysql_session.cursor(dictionary = True)
    isolation_level = (
        "SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED;")
    cursor.execute(isolation_level)
    return {"mysql_session": mysql_session, "cursor": cursor}

def commit_mysql_session(mysql_session):
    """Commit Sql session"""
    if mysql_session['mysql_session'].is_connected():
        mysql_session['cursor'].close()
        mysql_session['mysql_session'].commit()
        mysql_session['mysql_session'].close()

def rollback_mysql_session(mysql_session):
    """Rollback Session"""
    if mysql_session['mysql_session'].is_connected():
        mysql_session['mysql_session'].rollback()

def instant_commit(mysql_session):
    """Instant Commit"""
    mysql_session['mysql_session'].commit()