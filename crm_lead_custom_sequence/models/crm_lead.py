from odoo import models, fields, api
from datetime import datetime


class CrmLeadCustom(models.Model):
    _inherit = 'crm.lead'

    lead_seq = fields.Char(
        string="Lead ID",
        readonly=True,
        copy=False,
        default="New",
        tracking=True
    )

    @api.model
    def create(self, vals):
        if vals.get('type', 'lead') == 'lead' and vals.get('lead_seq', 'New') == 'New':
            seq_num = self.env['ir.sequence'].next_by_code('crm.lead.sequence') or 'New'

            # Convert month number → short name
            # seq_num = self.env['ir.sequence'].next_by_code('crm.lead.sequence')
            month_name = datetime.now().strftime('%b')
            year = datetime.now().year

            vals['lead_seq'] = f"LEAD/{year}/{month_name}/{seq_num.split('/')[-1]}"

        return super().create(vals)