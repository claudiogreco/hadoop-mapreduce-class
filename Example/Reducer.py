#!/usr/bin/python

"""
Udacity's Introduction to Hadoop and MapReduce course.
Implementation example of a MapReduce reducer.
"""

import sys

sales_total = 0
old_key = None

# Loops around the data, which will be in the format: key\tval,
# where key is the store name, val is the sale amount.

for line in sys.stdin:
    mapped_data = line.strip().split("\t")

    # Checks if the string has been successfully parsed.
    if len(mapped_data) != 2:
        continue

    # Saves the store name and the sale amount.
    this_key, this_sale = mapped_data

    # Deals with the change of the store name.
    if old_key and old_key != this_key:
        print old_key, "\t", sales_total
        old_key = this_key;
        sales_total = 0

    # Updates the store name.
    old_key = this_key

    # Updates the sale amount.
    sales_total += float(this_sale)

# Deals with the last store name and sale amount.
if old_key != None:
    print old_key, "\t", sales_total