from odoo import fields, models


class IngresoVehiculo(models.Model):
    _name = 'taller.ingreso_vehiculo'
    _description = 'Ingreso Vehiculo'

    # Relaciones
    empleado_id = fields.Many2one('taller.empleado',
                                  string='Empleado',
                                  required=True)
    cliente_id = fields.Many2one('taller.cliente',
                                 string='Cliente',
                                 required=True)
    vehiculo_id = fields.Many2one('taller.vehiculo',
                                  string='Vehiculo',
                                  required=True)
    orden_reparacion_id = fields.Many2one('taller.orden_reparacion',
                                          string='Orden Reparación',
                                          required=True)

    # Campo Booleanos de verificación vehicular
    herramienta = fields.Boolean(stirng='Tiene Herramientas',default=False)
    espejos = fields.Boolean(stirng='Espejos Sanos', default=True)
    radio = fields.Boolean(stirng='Tiene Radio', default=True)
    gato = fields.Boolean(stirng='Tiene Gato', default=True)
    tapa_ruedas = fields.Boolean(stirng='Tiene tapa en ruedas',
                                 default=False)
    vidrios = fields.Boolean(stirng='Vidrios Sanos', default=True)
    faros = fields.Boolean(stirng='Faros/Opticas Sanos', default=True)
    molduras = fields.Boolean(stirng='Molduras Sanas', default=True)

    detalle_repa = fields.Html(string='Detalle reparación')
    detalle_vehiculo = fields.Html(string='Detalle vehiculo')

    name = fields.Char(related='cliente_id.name')
