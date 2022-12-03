# Copyright (c) 2022, Gym Management and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import date_diff

class GymMembership(Document):
	def before_save(doc):
		doc.diff_days = date_diff(doc.to_date, frappe.utils.nowdate())