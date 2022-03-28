def addBookPayLoad(isbn, aisle):
    body = {
        "name": "Learn Appium Automation with Java",
        "isbn": isbn,
        "aisle": aisle,
        "author": "John Foe"
    }
    return body


def getPassword():
    return 'Nir10061991'
