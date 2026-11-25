"""Billing and invoices.

Pricing rules: orders of $100 or more get a 10% discount; tax is 8% on
the discounted subtotal. Amounts are in dollars.
"""
import sqlite3

DISCOUNT_THRESHOLD = 100
DISCOUNT_RATE = 0.10
TAX_RATE = 0.08


def line_total(price, quantity):
    return price * quantity


def invoice_total(lines):
    subtotal = 0.0
    for line in lines:
        subtotal += line["price"] * line["quantity"]
    discount = 0.0
    if subtotal > DISCOUNT_THRESHOLD:
        discount = subtotal * DISCOUNT_RATE
    tax = (subtotal - discount) * TAX_RATE
    return subtotal - discount + tax


def get_invoice_items(invoice_id):
    conn = sqlite3.connect("app.db")
    cur = conn.cursor()
    cur.execute("SELECT id FROM invoice_lines WHERE invoice_id = ?", (invoice_id,))
    line_ids = [row[0] for row in cur.fetchall()]
    items = []
    for line_id in line_ids:
        cur.execute("SELECT id, description, price, quantity FROM invoice_lines WHERE id = ?", (line_id,))
        items.append(cur.fetchone())
    conn.close()
    return items


def apply_credit(balance, amount):
    return balance - amount
