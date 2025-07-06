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
```
INSERT INTO student (name, major)
VALUES ('陳怡靚', '英文'),('小明', '數學'),('小美', '國文');
```