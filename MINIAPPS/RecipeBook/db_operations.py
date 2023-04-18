from create_database import executeQuery
import time


def setUserID():
    first = 0
    incrementalValue = 1
    query = "SELECT userID FROM users ORDER BY userID DESC LIMIT 1"
    response = executeQuery(query)
    try:
        id = "u" + str(int(response[first][first][1:]) + incrementalValue)
    except:
        id = "u1"
    return id


def setRecipieID():
    first = 0
    incrementalValue = 1
    query = "SELECT recipieID FROM recipies ORDER BY recipieID DESC LIMIT 1"
    response = executeQuery(query)
    try:
        id = "r" + str(int(response[first][first][1:]) + incrementalValue)
    except:
        id = "r1"
    return id


def addUser(firstName, lastName):
    userID = setUserID()

    query = "INSERT INTO users VALUES(\
        '{userID}',\
        '{firstName}',\
        '{lastName}')".format(
        userID=userID, firstName=firstName, lastName=lastName
    )
    executeQuery(query)
    return userID


def addRecipie(userID, recipieName, ingredients, instructions):
    recipieID = setRecipieID()

    query = "INSERT INTO recipies VALUES(\
        '{recipieID}',\
        '{userID}',\
        '{recipieName}',\
        '{createdDate}',\
        '{ingredients}',\
        '{instructions}')".format(
        recipieID=recipieID,
        userID=userID,
        recipieName=recipieName,
        createdDate=time.strftime("%Y-%m-%d %H:%M:%S"),
        ingredients=ingredients,
        instructions=instructions,
    )
    executeQuery(query)


print(executeQuery("SELECT * FROM users"))

addRecipie(
    userID="u2",
    recipieName="potato Chips",
    ingredients="Money Rs10 Time 10 min",
    instructions="Go to Marvari Aunty shop and buy a packet of potato chips",
)


print(executeQuery("SELECT * FROM recipies"))
