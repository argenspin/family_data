from odoo import models,fields,api

class HrEmployee(models.Model):
    _inherit = "hr.employee"
    department_id = fields.Many2one(string="Parents", readonly=True)

class HrDepartment(models.Model):
    _inherit = "hr.department"
    _description = "Parents"