from openerp.osv import fields,osv

class hocsinh (osv,osv):
    _name="hocsinh"
    _columns = {
        'mahs':fields.char('Mã học sinh', size=10, required=1),
        'tenhs':fields.char('Tên học sinh', size=60, required=1),
        'gioitinh':fields.selection([('male','Nam'),('female','Nữ')],'Giới tính'),
        'ngaysinh':fields.datetime('Ngày sinh'),
        'diachi':fields.char('Địa chỉ', size=150, required=1),
        'malop':fields.many2one('lop','Lớp',ondelete='NO ACTION'),
    }
    _defaults={
    }
    #_sql_constraints = [
    #    ('uniq_name', 'unique(mahs)', "Mã học sinh bị trùng."),
    #]
hocsinh()
