from ZODB import DB
from ZODB import FileStorage
from ZODB import connection
import transaction


def zodb_test():
    db = DB(FileStorage.FileStorage('Data.fs')).open()

    # Via http://www.ibm.com/developerworks/aix/library/au-zodb/
    dbroot = db.root()
    dbroot['a_number'] = 3
    dbroot['a_string'] = 'Gift'
    dbroot['a_list'] = [1, 2, 3, 5, 7, 12]
    dbroot['a_dictionary'] = { 1918: 'Red Sox', 1919: 'Reds' }
    dbroot['deeply_nested'] = {
      1918: [ ('Red Sox', 4), ('Cubs', 2) ],
      1919: [ ('Reds', 5), ('White Sox', 3) ],
      }
    transaction.commit()
    db.close()
