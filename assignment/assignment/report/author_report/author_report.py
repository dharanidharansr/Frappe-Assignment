# Copyright (c) 2026, CR7 and contributors
# For license information, please see license.txt

# import frappe
from frappe import _


def execute(filters=None):
    columns = [
        {
            "fieldname": "author_name",
            "label": "Author Name",
            "fieldtype": "Data"
        },
        {
            "fieldname": "age",
            "label": "Age",
            "fieldtype": "Int"
        },
        {
            "fieldname": "rating",
            "label": "Rating",
            "fieldtype": "Currency"
        }
    ]

    data = [
        {
            "author_name": "Author 1",
            "age": 25,
            "rating": 1000
        },
        {
            "author_name": "Author 2",
            "age": 30,
            "rating": 2000
        },
        {
            "author_name": "Author 3",
            "age": 35,
            "rating": 3000
        }
    ]

    return columns, data

def execute_snapshot_report(filters: dict | None = None):
	"""Return columns and data for the report.

	This is the main entry point for snapshot report. When 'Synced
	Report' is enabled in report, framework will call this method
	every time the report is refreshed or a filter is updated. It
	accepts the same filters as normal execute. But a utility method -
	get_latest_sync, is also imported.

	"""
	from frappe.database.duckdb.database import get_latest_sync

	columns = get_columns()
	data = get_data()

	return columns, data

def get_columns() -> list[dict]:
	"""Return columns for the report.

	One field definition per column, just like a DocType field definition.
	"""
	return [
		{
			"label": _("Column 1"),
			"fieldname": "column_1",
			"fieldtype": "Data",
		},
		{
			"label": _("Column 2"),
			"fieldname": "column_2",
			"fieldtype": "Int",
		},
	]


def get_data() -> list[list]:
	"""Return data for the report.

	The report data is a list of rows, with each row being a list of cell values.
	"""
	return [
		["Row 1", 1],
		["Row 2", 2],
	]
