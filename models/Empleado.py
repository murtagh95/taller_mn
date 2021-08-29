from odoo import fields, models


class Empleado(models.Model):
    _name = 'taller.empleado'
    _description = 'Empleado'

    name = fields.Char(string='Nombre', required=True)
    imagen = fields.Binary(string="Imagen")
    mail = fields.Char(string='Mail', required=True)
    domicilio = fields.Char(string='Domicilio', required=True)
    telefono = fields.Integer(string='Teléfono', required=True)
    cuil = fields.Char(string='CUIL', required=True)
    tipo = fields.Selection([
        ('admin', 'Administrativo/a'),
        ('ayuda', 'Ayudante'),
        ('jefemeca', 'Jefe Mecánico'),
        ('meca', 'Mecánico')],
        string='Tipo',
        required=True
    )

    # Restricciones SQL
    _sql_constraints = [
        ('unique_cuil', 'unique (cuil)',
         'No se debe repetir el número de CUIL')
    ]
