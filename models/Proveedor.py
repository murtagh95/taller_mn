from odoo import fields, models


class Proveedor(models.Model):
    _name = 'taller.proveedor'
    _description = 'Proveedor'

    name = fields.Char(string='Nombre', required=True)
    cuit = fields.Char(string='CUIT', required=True)
    domicilio = fields.Char(string='Domicilio', required=True)
    razon_social = fields.Char(string='Razon Social', required=True)
    telefono = fields.One2many('taller.telefono_proveedor', 'proveedor',
                               string='Teléfonos',
                               required=True)
    mail = fields.One2many('taller.mail_proveedor', 'proveedor',
                           string='Mail',
                           required=True)

    # Restricciones SQL
    _sql_constraints = [
        ('unique_cuit', 'unique (cuit)',
         'No se debe repetir el número de CUIT')
    ]


class TelefonoProveedor(models.Model):
    _name = 'taller.telefono_proveedor'
    _description = 'Teléfono Proveedor'

    proveedor = fields.Many2one('taller.proveedor')
    numero = fields.Char(string='Número', required=True)
    name = fields.Char(compute='_calcular_nombre')

    def _calcular_nombre(self):
        """ Se calcula el nombre según el número ingresado. """
        for rec in self:
            if rec.numero:
                rec.name = str(rec.numero)
            else:
                rec.name = ""


class MailProveedor(models.Model):
    _name = 'taller.mail_proveedor'
    _description = 'Mail Proveedor'

    proveedor = fields.Many2one('taller.proveedor')
    correo = fields.Char(string='Mail', required=True)
    name = fields.Char(compute='_calcular_nombre')

    def _calcular_nombre(self):
        """ Se calcula el nombre según el mail. """
        for rec in self:
            if rec.mail:
                rec.name = str(rec.mail)
            else:
                rec.name = ""
