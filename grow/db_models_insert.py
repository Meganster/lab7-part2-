import connection


class Department:
    def __init__(self, name, about):
        self.connection = connection.Connection(host="localhost", db_name="ask_db", user="'yury'", password="89096547567")
        self.name = name
        self.about = about
    
    def save(self):
        with self.connection as con:
            cursor = con.cursor()
            cursor.execute("""insert into grow_department (name, about)
                values (%s, %s)""", (self.name,
                                     self.about) )
            con.commit()
            cursor.execute("""insert into grow_employee (firstName, lastName, about, email, phone_number, department_id) values ("David", "Pranker", "Killer, iron man", "killer@supermail.com", "+9023523214", 1)""")
            con.commit()


department = Department("Rescue group", "Group to rescue anyone")
department.save()

