import sqlite3
import json


def list_metals():
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
                SELECT
                    m.id,
                    m.metal,
                    m.price
                FROM `Metals` m
                """
        )
        query_results = db_cursor.fetchall()

        metals = []
        for row in query_results:
            metals.append(dict(row))

        serialized_orders = json.dumps(metals)

    return serialized_orders


def update_metal(id, metal_data):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
            UPDATE Metals
                SET
                    metal = ?,
                    price = ?
            WHERE id = ?
            """,
            (metal_data["metal"], metal_data["price"], id),
        )

    return True if db_cursor.rowcount > 0 else False
