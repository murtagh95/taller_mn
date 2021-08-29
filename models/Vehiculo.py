from odoo import fields, models


class Vehiculo(models.Model):
    _name = 'taller.vehiculo'
    _description = 'Vehiculo'

    cliente = fields.Many2many('taller.cliente',
                               relation='vehiculo_cliente_rel',
                               column1='vehiculo_id',
                               column2='cleinte_id',
                               string='Clientes',
                               required=True
                               )
    marca = fields.Char(string='Marca', required=True)
    modelo = fields.Char(string='Modelo', required=True)
    nro_motor = fields.Char(string='Nro Motor', required=True)
    kilometraje = fields.Integer(string='Kilometraje', required=True)
    anio = fields.Integer(string='Año', required=True)
    color = fields.Char(string='Color', required=True)
    tipo = fields.Selection(
        [('sedan', 'Sedan'),
         ('camioneta', 'Camioneta'),
         ('coupe', 'Coupé'),
         ('berlina', 'Berlina'),
         ('util', 'Utilitaria')],
        string='Tipo',
        required=True
    )
    patente = fields.Char(string='Patente', required=True)

    _sql_constraints = [
        ('unique_patente', 'unique (patente)',
         'No se debe repetir el número de patente')
    ]
