from openerp.osv import fields,osv

class lop (osv,osv):
    _name="lop"
    _columns = {
        'malop':fields.char('Mã lớp', size=10, required=1),
        'tenlop':fields.char('Tên lớp', size=10, required=1),
    }
    _defaults={
    }
lop()