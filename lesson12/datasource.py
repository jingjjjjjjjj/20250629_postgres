import psycopg2
import os
from dotenv import load_dotenv
import datetime

load_dotenv()

def get_stations_names():
    """
    取得台鐵車站名稱列表
    :return: 台鐵車站名稱列表，連線失敗時回傳 None
    """
    try:
        conn = psycopg2.connect(
            host=os.getenv("HOST"),
            database=os.getenv("DATABASE"),
            user=os.getenv("USER"),
            password=os.getenv("PASSWORD"),
            port="5432"
        )

        cursor = conn.cursor()
        query = """
        SELECT name
        FROM "台鐵車站資訊";
        """
        cursor.execute(query)
        result = cursor.fetchall()

        # 使用 list comprehension 簡化程式碼
        result_list = [station[0] for station in result]

        return result_list

    except psycopg2.Error as e:
        print(f"資料庫連線或查詢失敗：{e}")
        return None
    except Exception as e:
        print(f"發生未預期的錯誤：{e}")
        return None
    finally:
        # 確保資源正確釋放
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

def get_min_and_max_date():
    """
    取得資料表中的最小和最大日期
    :return: (最小日期, 最大日期)，連線失敗時回傳 None
    """
    try:
        conn = psycopg2.connect(
            host=os.getenv("HOST"),
            database=os.getenv("DATABASE"),
            user=os.getenv("USER"),
            password=os.getenv("PASSWORD"),
            port="5432"
        )

        cursor = conn.cursor()
        query = """
            SELECT
                MIN(to_date(p."trnOpDate"::text, 'YYYYMMDD')) AS min_date,
                MAX(to_date(p."trnOpDate"::text, 'YYYYMMDD')) AS max_date
            FROM public."每日各站進出站人數2023" p;
        """
        cursor.execute(query)
        result = cursor.fetchone()

        return result

    except psycopg2.Error as e:
        print(f"資料庫連線或查詢失敗：{e}")
        return None
    except Exception as e:
        print(f"發生未預期的錯誤：{e}")
        return None
    finally:
        # 確保資源正確釋放
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

def _date_to_yyyymmdd_int(d):
    """輔助：把 date / datetime / ISO string 轉為 YYYYMMDD 的 integer"""
    if d is None:
        return None
    if isinstance(d, str):
        d = datetime.date.fromisoformat(d)
    if isinstance(d, datetime.datetime):
        d = d.date()
    if not isinstance(d, datetime.date):
        raise ValueError("start_date/end_date 必須是 date/datetime 或 ISO format 字串")
    return int(d.strftime("%Y%m%d"))


def get_station_data_by_date(station_name, start_date, end_date):
    """
    取得指定車站在特定日期範圍內的進出人數資料
    :param station_name: 車站名稱
    :param start_date: 起始日期 (datetime.date 或 'YYYY-MM-DD' 字串)
    :param end_date: 結束日期 (datetime.date 或 'YYYY-MM-DD' 字串)
    :return: 車站資料列表，連線失敗時回傳 None
    """
    try:
        # 先把日期參數轉為 YYYYMMDD 的 integer（避免和資料表的 integer 欄位直接比較時發生型別錯誤）
        start_int = _date_to_yyyymmdd_int(start_date)
        end_int = _date_to_yyyymmdd_int(end_date)
        if start_int is None or end_int is None:
            raise ValueError("start_date 和 end_date 不能為 None")

        conn = psycopg2.connect(
            host=os.getenv("HOST"),
            database=os.getenv("DATABASE"),
            user=os.getenv("USER"),
            password=os.getenv("PASSWORD"),
            port="5432"
        )

        cursor = conn.cursor()
        query = """
        SELECT
            to_date(p."trnOpDate"::text, 'YYYYMMDD') AS trnOpDate,
            t."stationName" AS 車站,
            p."gateInComingCnt",
            p."gateOutGoingCnt"
        FROM public."每日各站進出站人數2023" p
        JOIN public."台鐵車站資訊" t
          ON p."staCode" = t."stationCode"
        WHERE p."trnOpDate" BETWEEN %s AND %s
          AND t."stationName" = %s
        ORDER BY p."trnOpDate";
        """
        # 傳入的是整數邊界，避免與 date 做不相容的比較
        cursor.execute(query, (start_int, end_int, station_name))
        result = cursor.fetchall()

        return result

    except psycopg2.Error as e:
        print(f"資料庫連線或查詢失敗：{e}")
        return None
    except Exception as e:
        print(f"發生未預期的錯誤：{e}")
        return None
    finally:
        # 確保資源正確釋放
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()