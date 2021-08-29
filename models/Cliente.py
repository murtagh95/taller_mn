from odoo import fields, models


class Cliente(models.Model):
    _name = 'taller.cliente'
    _description = 'Cliente'

    name = fields.Char(string='Nombre')
    dni = fields.Integer(string='DNI')
    mail = fields.Char(string='Mail')
    domicilio = fields.Char(string='Domicilio')
    responsabilidad_iva = fields.Char(string='Responsibilidad IVA')
    telefono = fields.One2many('taller.cliente_telefono', 'cliente',
                               string='Teléfonos')
    auto = fields.One2many('taller.vehiculo', 'cliente',
                           string='Vehículos')

    # Restricciones SQL
    _sql_constraints = [
        ('unique_dni', 'unique (dni)',
         'No se debe repetir el número de DNI')
    ]

class Telefono(models.Model):
    _name = 'taller.cliente_telefono'
    _description = 'Cliente Teléfono'

    cliente = fields.Many2one('taller.cliente')
    numero = fields.Integer(string='Número')
    name = fields.Char(compute='_calcular_nombre')

    def _calcular_nombre(self):
        """ Se calcula el nombre según el número ingresado. """
        if self.numero:
            self.name = str(self.numero)
        else:
            self.name = ""
