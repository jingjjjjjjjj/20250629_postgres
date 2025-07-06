## 更改日期型別和更新字串成為DATE

```sql
alter table world 
alter column 日期 type date
using 日期::date;
```