import sqlite3

def createDB():
    executeQuery("""CREATE TABLE recipies(recipieID, userID, recipieName, createdDate, ingredients, instructions) """)
    print("Database created")
    executeQuery("CREATE TABLE users(userID, firstName, lastName)")
    print("Tables Created")

def executeQuery(Query):
    try:    
        conn=sqlite3.connect("recipe_book.db")
        cur=conn.cursor()
        response=cur.execute(Query)
        conn.commit()
        return response.fetchall()
    except Exception as e:
        print("An Exception occured")
        print(e)
    finally:
        conn.close()
                
if __name__=='__main__':
    createDB()