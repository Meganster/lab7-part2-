import connection


class Department:
    def __init__(self):
        self.connection = connection.Connection(host="localhost", db_name="ask_db", user="'yury'", password="89096547567")

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
            cursor.execute("""create table
                grow_employee (
                id INT(11) NOT NULL AUTO_INCREMENT,
                firstName CHAR(30) NOT NULL,
                lastName CHAR(30) NOT NULL,
                about TEXT,
                email CHAR(50) NOT NULL,
                phone_number CHAR(50),
                department_id INT,
                FOREIGN KEY (department_id) REFERENCES grow_department(id),
                PRIMARY KEY(id)
                )""")
            c.commit()


department = Department()
department.create()
