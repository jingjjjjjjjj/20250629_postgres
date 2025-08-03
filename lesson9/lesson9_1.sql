# count 所有表格資訊 
# AS "筆數" --> 表格標題
SELECT count(*) AS "筆數"
FROM "台鐵車站資訊"

SELECT count(*) AS "筆數"
FROM "台鐵車站資訊"
WHERE name = '基隆';

# like '%臺北%' --> 值 ‘’ 
SELECT 
FROM "台鐵車站資訊"
WHERE "stationAddrTw" like '%臺北%';

/* count name 這一欄 */
SELECT count(name) AS "台北車站數"
FROM "台鐵車站資訊"
WHERE "stationAddrTw" like '%臺北%';

SELECT *
FROM "每日各站進出站人數" LEFT JOIN "台鐵車站資訊" ON "每日各站進出站人數"."車站代碼" = "台鐵車站資訊"."stationCode";

SELECT *
FROM "每日各站進出站人數" LEFT JOIN "台鐵車站資訊" ON "車站代碼" = "stationCode"
WHERE "stationName" = '基隆';

/*
 * 全省個站點2022年進站總人數
 */


SELECT "name" AS 站名,COUNT("name") AS 筆數, AVG("進站人數") AS "進站人數"
FROM "每日各站進出站人數" LEFT JOIN "台鐵車站資訊" ON "車站代碼" = "stationCode"
WHERE "日期" BETWEEN '2022-01-01' AND '2022-12-31'
GROUP BY "name";

/*
 * date_part() --> 用來從欄位「日期」中提取（抽取）年份部分的數值
 * 'year' 表示你想要提取的是「年份」這一部分。
    "日期" 是你的日期欄位名稱。
 */
SELECT "name" AS 站名,date_part('year', "日期") AS "年份",COUNT("name") AS 筆數, AVG("進站人數") AS "進站人數"
FROM "每日各站進出站人數" LEFT JOIN "台鐵車站資訊" ON "車站代碼" = "stationCode"
WHERE "日期" BETWEEN '2022-01-01' AND '2022-12-31'
GROUP BY "name","年份";


/*
 * DESC --> 降冪
 */
SELECT "name" AS 站名,date_part('year', "日期") AS "年份",COUNT("name") AS 筆數, AVG("進站人數") AS "進站人數"
FROM "每日各站進出站人數" LEFT JOIN "台鐵車站資訊" ON "車站代碼" = "stationCode"
WHERE "name" = '基隆'
GROUP BY "name","年份"
ORDER BY "進站人數" DESC;