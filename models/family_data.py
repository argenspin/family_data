from odoo import fields, models,api

class FamilyData(models.Model):
    _name = "family.data"
    name = fields.Selection(string="മുതിർന്ന കണ്ണി",\
        selection=[('kochumuhammed','Kochumuhammed'), ('saidu_muhammed','Saidu_Muhammed'), ('beevathu','Beevathu'),('aisha','Aisha'),('khadeeja','Khadeeja')], required=True)
    line_ids = fields.One2many('family.data.line','family_data_id')

class FamilyDataLine(models.Model):
    _name = "family.data.line"
    family_data_id = fields.Many2one('family.data',string="Family Data ID")
    name = fields.Char(string="പേര്")
    father_name = fields.Char(string="Name of Father")
    mother_name = fields.Char(string="Name of Mother")
    spouse_name = fields.Char(string="Wife / Husband Name")
    email = fields.Char(string="Email (ഉണ്ടെങ്കിൽ മാത്രം)")
    address = fields.Text(string="Address")
    dob = fields.Date(string="ജനിച്ച വർഷം")
    education = fields.Char(string="വിദ്യാഭ്യാസ യോഗ്യത")
    job = fields.Char(string="ജോലി (വിദേശത്താണെങ്കിൽ ജോലിയോടൊപ്പം ജോലി ചെയ്യുന്ന രാജ്യത്തിന്റെ പേരും ചേർക്കുക)")
    late_members = fields.Text(string="മാതാപിതാക്കൾ, മക്കൾ , പേരക്കുട്ടികൾ, ഭർത്താവ് , ഭാര്യ എന്നിങ്ങനെ ആരെങ്കിലും മരണപ്പെട്ടിട്ടുണ്ടെങ്കിൽ അവരുടെ പേര് , മരിച്ച തീയ്യതി")
    other_info = fields.Text(string="വേറെ എന്തെങ്കിലും വിവരങ്ങളോ അഭിപ്രായങ്ങളോ  ചേർക്കാൻ ഉണ്ടെങ്കിൽ ഇവിടെ എഴുതുക ")