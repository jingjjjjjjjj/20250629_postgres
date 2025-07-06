## 更改日期型別和更新字串成為DATE

```sql
alter table world 
alter column 日期 type date
using 日期::date;
```

## 問題
1. 查詢亞洲總共有多少人死亡
2. 查詢全世界2020年的總確診數
3. 查詢國家名有“阿”字，總死亡數大於10000
4. 
