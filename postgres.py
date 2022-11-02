'''
Работa с базами данных
'''

# psql postgres - вход в postgres(MacOS)

# \l - просмотр баз данных

# create database название_базы_данных; - создание базы данных

# \l - проверка наличия базы данных

# \c название_базы_данных - коннект с базой данных

# \d - просмотр всех таблиц

# drop database название_базы_данных; - удаление базы данных

# CREATE USER имя_юзера WITH PASSWORD ''; - создание нового юзера
# ключ. слово|идентификатор

# CREATE TABLE название_таблицы(название_столбцов)

# id serial primary key, name varchar(кол-во символов),
# last_name varchar (кол-во символов)

# alter role имя_юзера with super user; - снятие ограничений в правах

# exit
# psql -U имя_юзера
# \c postgress 
# grant all privilages on database имя_юзера to имя_юзера - добавление привилегии к другому юзеру

# create database название_базы_данных with owner имя_юзера;




# INSERT, SELECT, UPDATE, DELETE (манипуляция с данными)

# insert - добавление(вставка) записей (строк)
# INSERT INTO название_таблицы (название_столбцов) VALUE (значения);


'''
INSERT INTO student (name, surname, age) VALUES ('Abai', 'Makeev', 25);
-добавится одна запись

INSERT INTO student (name, surname, age) aVALUES ('Kanykei', 'Bolotbekova', 24), ('Janylai', 'Muratova', 19), ('Maksat', 'Urmanbetov', 31);
- добавится несколько
'''

# update - обновление записи
""
'''
UPDATE название_таблицы  SET столбец=значение, столбец2=значение WHERE условие;
- обновление одной записи

UPDATE название_таблицы SET столбец=значение, столбец2=значение;
- обновление всех записей

UPDATE название_таблицы  SET столбец=значение, столбец2=значение WHERE условие;
- обновление к-т части записей

пример

UPDATE student SET rating=rating + 2 WHERE id IN (1, 4);
'''

#DELETE - удаление записей

'''
DELETE FROM название_таблицы WHERE условие
- удаление одной записи

DELETE FROM название_таблицы WHERE условие
- удаление части записей

DELETE FROM название_таблицы
- удалить все записи
'''

# SELECT
'''
SELECT * FROM название_таблицы
- выборка всех столбцов по всем строкам

SELECT столбец 1, . . . .  FROM название_таблицы;
- выбор определенных столбцов

SELECT столбцы FROM название_таблицы WHERE условие;
- фильтрация записей

О П Е Р А Ц И И 

-- числа и дата
1) сравнение
= - равно
!=, <> - не равно
>, <, >=, <=
exmpl:  
SELECT * FROM student WHERE age > 25;

2) IN - проверяет в списке знания
SELECT * FROM student WHERE name in ('John', 'Jack');
SELECT * FROM student WHERE name='John' OR name='Jack';

3) BETWEEN - между, от ... до ....
SELECT * FROM название_таблицы WHERE столбец BETWEEN нижний_предел AND верхний_предел;
SELECT * FROM название_таблицы WHERE столбец >= нижний_предел AND столбец <= верхний_предел;


-- строки

1)LIKE

строка начинается с определенной подстроки
LIKE 'Ja%'
SELECT * FROM student WHERE name LIKE 'J%';

строка оканчивается на определенную подстроку
LIKE '%J'
SELECT * FROM student WHERE surname LIKE '%k';

строка содержит определенную подстроку
LIKE '%...%'
SELECT * FROM student WHERE surname LIKE '%on%';

2) ORDER BY -  сортировка
SELECT * FROM student ORDER BY name ASC/DECS;



'''

# ALTER TABLE student ADD COLUMN rating(название столбца) SMALLINT NOT NULL DEAFULT 0; - создание поля
# ALTER TABLE student ADD CHECK(rating BETWEEN 0 AND 100); - ограничение от 0 до 100

'''
Создание архитектуры БД: с использованием всех видов связей
'''
 



'''
Агрегационные функции
'''

'''SUM(), MAX(), MIN(), COUNT(), AVG()'''

# SELECT MAX(rating) FROM student

# количество студентов
# SELECT COUNT(*) FROM student;

#максимальный ретинг
# SELECT MAX(rating) from student;

# группирвка = разбиение списка записей группы
# Group by

# количетсво студентов по факультету
# select faculty, count (*) from student group by faculty;

# средний рейтинг по факультету
# SELECT faculty, AVG(rating) FROM student GROUP BY faculty;



'''limit - ограничение количества резултатов выборки'''

# LIMIT, FETCH, TOP

# SELECT * FROM student; - все записи
# SELECT * FROM student ORDER BY rating LIMIT 4; - первые четыре,
# SELECT * FROM student ORDER BY rating LIMIT 4 OFFSET 4; - записи с 5 по 8,

# SELECT FROM student ORDER BY rating FETCH FIRST 4 ROWS ONLY; - первые четыре,
# SELECT FROM student ORDER BY rating OFFSET 4 ROWS FETCH NEXT/FIRST 4 ROWS ONLY; 


'''distinct'''

# SELECT DISTINCT faculty FROM students; - убирает повторения

# join

# UPDATE student SET faculty '



'''
1) one to one - одной записи в одной таблице соответствует ТОЛЬКО ОДНА запись в другой таблице.
ALTER TABLE department ADD FOREIGN KEY (director) REFERENCES director(id);


2) one to many - одной записи в одной таблице соответсвует много записей в другой таблице
напр. таблице Faculty соответствуют записи таблицы Students.
(! Все виды связей строятся от one to many)

3) many to many 
товары <- промежуточная таблица -> заказы
Один и тот же товар могут покупать много раз и в одном заказе могут купить много товаров
ALTER TABLE purchase_product ADD FOREIGN KEY(purchase) REFERENCES purchase(id), add foreign ke
y(product) references product(id);

4) таблица связана с собой
сотрудники --> начальник
alter table employee add foreign key(head) references employee(id);

'''

'''
                J O I N
'''
# INNER JOIN
# LEFT JOIN
# RIGHT JOIN
# FULL JOIN






'''
И Н Д Е К С Ы. 

Импорт и экспорт данных.
'''

'''
Бинарное дерево поиска
B-tree
'''

'''

insert into employee(name, last_name, department) values ('John', 'Snow', 1), ('Kerry', 'Smith', 2), ('Molly', 'Weasly', 2), ('Mandy', 'Moor', 3), ('Kevin', 'Perry', 1), ('Shelly', 'Yang', 3), ('Kris', 'Lee', 1), ('Morgan', 'Morris', NULL);
select * from employee join department on employee

'''

# select e.name, e,last_name, d.name from employee as e inner join as d on e.department=d.id;



'''
Таски
'''
# 1) select plaintext from wordform order by wordformid asc limit 10;
# 10 часто встреч. слов
# 2) select plaintext from wordform where plaintext ilike 'a%';
# слова начинаются на а без учета регистра
#3) select title, genretype from work where genretype='p';
# 4)select avg(totalparagraphs) from work where genretype='t';
#5) select title from work where totalwords> (select avg(totalwords) from work); 
#6) select c.charname, c.speechcount, w.title from character_work as cw join character as c on cw.charid = c.charid join work as w on cw.workid = w.workid;
#7) 
