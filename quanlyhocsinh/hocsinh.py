# -*- coding: utf-8 -*-
from openerp.osv import fields,osv

class hocsinh (osv.osv):
    _name='hocsinh'

    _columns = {
        #cac thuoc tinh cua lop hoc phan
        'mahs':fields.char('Mã học sinh', size=10, required=1),
        'tenhs':fields.char('Tên học sinh',size=500, required=1),
        'ngaysinh':fields.date('Ngày sinh'),
        'diachi':fields.char('Địa chỉ' ,size=500),
        'sdt': fields.integer('Số điện thoại'),
        'gioitinh':fields.selection([('male','Nam'),('female','Nữ')],'Giới tính'),
        'malop':fields.many2one('lop','Lop',ondelete='NO ACTION'),
    }
    _defaults={
    }
    _sql_constraints = [
        ('uniq_name', 'unique(mahs)', "Mã học sinh bị trùng."),
    ]

hocsinh()



