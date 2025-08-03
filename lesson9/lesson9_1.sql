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

# count name 這一欄 
SELECT count(name) AS "台北車站數"
FROM "台鐵車站資訊"
WHERE "stationAddrTw" like '%臺北%';