SELECT
  s."stationName" AS 車站,
  s."stationCode" AS 車站代碼,
  to_date(d."trnOpDate"::text, 'YYYYMMDD') AS "日期",
  d."gateInComingCnt" AS "進站人數",
  d."gateOutGoingCnt" AS "出站人數",
  (d."gateInComingCnt" + d."gateOutGoingCnt") AS "合計"
FROM public."台鐵車站資訊" s
JOIN public."每日各站進出站人數2023" d
  ON s."stationCode" = d."staCode"
WHERE to_date(d."trnOpDate"::text, 'YYYYMMDD') = DATE '2023-01-01'
  AND s."stationName" = '基隆';
