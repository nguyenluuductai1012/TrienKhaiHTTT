# -*- coding: utf-8 -*-
from openerp.osv import fields,osv

class sanpham (osv.osv):
    _name='sanpham'

    _columns = {
        #cac thuoc tinh cua lop hoc phan
        'masp':fields.char('Mã sản phẩm', size=10, required=1),
        'tensp':fields.char('Tên sản phẩm',size=500, required=1),
        'ngaysinh':fields.date('Ngày sinh'),
        'sl':fields.char('Số lượng' ,size=500),
        'dg': fields.char('Đơn giá',size=500),
        'sdt': fields.integer('Số điện thoại'),
        'gioitinh':fields.selection([('male','Nam'),('female','Nữ')],'Giới tính'),
        'maloai':fields.many2one('loaisanpham','Loại sản phẩm',ondelete='NO ACTION'),
    }
    _defaults={
    }
    _sql_constraints = [
        ('uniq_name', 'unique(tensp)', "Tên sản phẩm bị trùng."),
    ]

sanpham()



