from odoo import models, fields


class ProjectBranch(models.Model):
    _name = "my.project.branch"
    _description = "Branch"

    name = fields.Char(required=True)


class ProjectStaff(models.Model):
    _name = "my.project.staff"
    _description = "Staff Member"
    _rec_name = "name"

    name = fields.Char(required=True)
    image_1920 = fields.Image(string="Photo")

    phone = fields.Char(string="Phone Number", required=True)

    branch_id = fields.Many2one(
        "my.project.branch",
        string="Manages Branch",
        required=True
    )

    job_role = fields.Selection(
        [
            ("manager", "Manager"),
            ("cashier", "Cashier"),
            ("hr", "HR"),
            ("accountant", "Accountant"),
            ("security", "Security"),
        ],
        string="Job Role",
        required=True,
        default="manager",
    )

    notes = fields.Text(string="Notes")
