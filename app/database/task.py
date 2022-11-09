from app.database import get_db


def output_formatter(results):
    out = []
    for results in results:
        result_dict = {
            "id": results[0],
            "title": [1],
            "subtitle":[2],
            "body": [3],
            "active": [4]

        }
        out.append(result_dict)
    return out


def scan ():
    conn = get_db()
    cursor = conn.execute ("SELECT * FROM task WHERE active=1", ())
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)





