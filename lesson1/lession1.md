## 建立表格

```sql
CREATE TABLE [IF NOT EXISTS] table_name (
   column1 datatype(length) column_constraint,
   column2 datatype(length) column_constraint,
   ...
   table_constraints
);
```

## 建立一個資料表
```sql
CREATE TABLE IF NOT EXISTS student (
   student_id SERIAL PRIMARY KEY,
   name VARCHAR(20) NOT NULL,
   major VARCHAR(20) UNIQUE
);
```

## 刪除資料表

```sql
DROP TABLE IF EXISTS student;
```

## 新增一筆資料

```sql
INSERT INTO student (name, major)
VALUES ('陳怡靚', '英文'),('小明', '數學'),('小美', '國文');
```


## 取得資料

```sql
SELECT student id, name, major FROM student;
```

```sql
SELECT * FROM student;
```

```sql
SELECT student_id, name, major
FROM  student;

SELECT  name, major
FROM  student;

SELECT  *
FROM  student
WHERE name='信忠';

SELECT  *
FROM  student
ORDER BY student_id DESC;

SELECT  *
FROM  student
ORDER BY student_id DESC
LIMIT 3;
```





```python

```

```bash

```