import frappe
from frappe.query_builder import DocType

@frappe.whitelist()
def update_customer_contacts():

    Customer = DocType("Customer")
    DynamicLink = DocType("Dynamic Link")

    query = (
        frappe.qb.from_(Customer)
        .join(DynamicLink)
        .on(Customer.name == DynamicLink.link_name)
        .select(
            Customer.name,
            Customer.customer_name,
            DynamicLink.parent
        )
        .where(DynamicLink.link_doctype == "Customer")
        .limit(5)
    )

    results = query.run(as_dict=True)

    if results:
        customer = frappe.get_doc("Customer", results[0]["name"])
        customer.customer_name = customer.customer_name + " Updated"
        customer.save()

    for row in results:
        frappe.db.set_value(
            "Customer",
            row["name"],
            "territory",
            "India"
        )

    return results