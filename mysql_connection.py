import mysql.connector

def get_connection() :
    connection = mysql.connector.connect(
        host = 'yh-db.caohoyy07jik.ap-northeast-2.rds.amazonaws.com',
        database = 'recipe2_db', 
        user = 'recipe_user',
        password = 'recipe1234' 
    )
    return connection   
