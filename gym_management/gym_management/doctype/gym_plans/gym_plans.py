# Copyright (c) 2022, Gym Management and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class GymPlans(Document):
	def before_insert(self):
		self.total = self.month * self.rate