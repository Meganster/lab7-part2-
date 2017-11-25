import connection


class Department:
    def __init__(self, name, about):
        self.connection = connection.Connection(host="localhost", db_name="ask_db", user="'yury'", password="89096547567")
        self.name = name
        self.about = about
    
    def create(self):
        with self.connection as c:
            cursor = c.cursor()
            cursor.execute("""create table
                grow_department (
                id INT(11) NOT NULL AUTO_INCREMENT,
                name CHAR(30) NOT NULL,
                about TEXT,
                PRIMARY KEY(id)
                )""")
            c.commit()
    
    def save(self):
        with self.connection as con:
            cursor = con.cursor()
            cursor.execute("""insert into grow_department (name, about)
                values (%s, %s)""", (self.name,
                                     self.about) )
            con.commit()


department = Department("Rapid reaction group", "Group of fast reaction to kill or rescue anyone")
department.save()
