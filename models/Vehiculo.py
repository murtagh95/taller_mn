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
        string='Tipo'
    )
    patente = fields.Char(string='Patente', required=True)
    name = fields.Char(compute='_calcular_nombre')

    _sql_constraints = [
        ('unique_patente', 'unique (patente)',
         'No se debe repetir el número de patente')
    ]

    def _calcular_nombre(self):
        """ Se calcula el nombre uniendo la marca más el modelo más la
        patente. """
        for rec in self:
            modelo = rec.modelo or ""
            marca = rec.marca or ""
            patente = rec.patente or ""
            if modelo or marca or patente:
                rec.name = str(modelo) + " - " + str(marca) + " - " + \
                           str(patente)
            else:
                rec.name = ""
