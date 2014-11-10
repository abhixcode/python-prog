dbfilename = 'people-file'  #name of file which would store our data
ENDDB = 'enddb.'
ENDREC = 'endrec.'
RECSEP = '=>'

def storeDbase(db, dbfilename=dbfilename):
    "formatted dump of database to flat file"
    dbfile = open(dbfilename, 'w')
    for key in db:
        print(key, file=dbfile) #write key name to data file
        for(name, value) in db[key].items():
            print(name + RECSEP + repr(value), file=dbfile) #repr returns a string containing a printable representation of argument object
        print(ENDREC, file=dbfile)
    print(ENDDB, file=dbfile)
    dbfile.close()
    
def loadDbase(dbfilename=dbfilename):
    "parse data to reconstruct database"
    dbfile = open(dbfilename) #default open mode is read
    import sys
    sys.stdin = dbfile
    db = {}
    key = input()
    while key != ENDDB:
        rec = {}
        field = input()
        while field != ENDREC:
            name, value = field.split(RECSEP)
            rec[name] = eval(value)
            field = input()
        db[key] = rec
        key = input()
    return db

if __name__ == '__main__':
    from initdata import db
    storeDbase(db)    