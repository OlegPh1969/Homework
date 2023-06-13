# Задача 4.1.
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:

import sqlite3

def sql_connection():
	try :
		con = sqlite3.connect('teatchers.db')
		return con
	except sqlite3.Error as error:
		print(error)

def table_exists(con):
	cursor_obj = con.cursor()
	listOfTables = cursor_obj.execute(
		"""SELECT tbl_name FROM sqlite_master WHERE type='table' AND tbl_name ='Students';""").fetchall()
	if listOfTables == [] :
		return False
	else :
		return True

def create_table(con):
	try :
		cursor_obj = con.cursor()
		cursor_obj.execute("""CREATE TABLE Students(
			Student_Id INTEGER PRIMARY KEY, 
			Student_Name TEXT, 
			School_Id INTEGER NOT NULL);""")
		con.commit()
	except sqlite3.Error as error:
		print(error)

def insert_data_in_table(con):
	try :
		cursor_obj = con.cursor()
		cursor_obj.execute("""INSERT INTO Students(
			Student_Id, 
			Student_Name, 
			School_Id) 
			VALUES
			(201, 'Иван', 1),
			(202, 'Петр', 2),
			(203, 'Анастасия', 3),
			(204, 'Игорь', 4) ;
			""")
		con.commit()
	except sqlite3.Error as error:
		print(error)

def get_student_and_school_info(con, student_id):
	cursor_obj = con.cursor()
	cursor_obj.execute("""SELECT ST.Student_Id, ST.Student_Name, ST.School_Id, s.School_Name FROM  Students ST
		INNER JOIN school s ON ST.School_Id = s.School_Id;
		""")
	one_result = cursor_obj.fetchone()
	if one_result != [] :
		print('ID Студента:\t' , one_result[0], '\nИмя студента:\t', one_result[1],
       		'\nID школы:\t', one_result[2], '\nНазвание школы:\t', one_result[3]
        )
	

conn = sql_connection()
if conn != None:
	print("Успешно соединились с БД")
else:	
	print("Ошибка соедининия с БД, дальнейшая работа невозможна")
	exit

if  table_exists(conn) == False:
	print('Создаем и заполняем таблицу "Students"')
	create_table(conn)
	insert_data_in_table(conn)
else:
	print('таблица "Students" уже создана и заполнена')

student_id = 201
print(f'Выводим информацию о студенте с ID = {student_id}')
get_student_and_school_info(conn, student_id)


        