# -*- coding: utf-8 -*-
from openerp.osv import fields,osv

class loaisanpham (osv.osv):
    _name='loaisanpham'
    _rec_name = 'tenDM'
    _columns = {
        'maDM':fields.selection([('cntt','Công Nghệ Thông Tin'),('qtkd','Quản Trị Kinh Doanh'),('cntp','Công Nghệ Thực Phẩm'),('cdt','Cơ - Điện Tử')],'Ngành', required=1),
        'tenDM':fields.char('Tên lớp:', size=500, required=1),
        'nienkhoa':fields.selection([('2017','2017'),('2018','2018'),('2019','2019'),('2020','2020'),('2021','2021')],'Khoá')
    }
    _defaults={
    }
loaisanpham()


