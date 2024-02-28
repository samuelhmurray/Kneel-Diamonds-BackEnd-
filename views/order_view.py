import sqlite3
import json


def list_orders():
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
                SELECT
                    o.id,
                    o.metalId,
                    o.sizeId,
                    o.styleId
                FROM `Orders` o
                """
        )
        query_results = db_cursor.fetchall()

        orders = []
        for row in query_results:
            orders.append(dict(row))

        serialized_orders = json.dumps(orders)

    return serialized_orders


def retrieve_order(pk):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
                SELECT
                    o.id,
                    o.metalId,
                    o.sizeId,
                    o.styleId
                FROM `Orders` o
                WHERE o.id = ?               
                """,
            (pk,),
        )
        query_results = db_cursor.fetchone()

        serialized_order = json.dumps(dict(query_results))

    return serialized_order


def create_order(metalId, sizeId, styleId):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
            INSERT INTO `Orders` (metalId, sizeId, styleId)
            VALUES (?, ?, ?)
            """,
            (metalId, sizeId, styleId),
        )

        # Commit the transaction
        conn.commit()

    return True


def delete_order(pk):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
        DELETE FROM `Orders` WHERE id = ?
        """,
            (pk,),
        )
        number_of_rows_deleted = db_cursor.rowcount

    return True if number_of_rows_deleted > 0 else False
