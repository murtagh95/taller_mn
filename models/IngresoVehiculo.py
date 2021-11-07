from odoo import fields, models, api


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
    #orden_reparacion_id = fields.Many2one('taller.orden_reparacion',
    #                                      string='Orden Reparación')

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

    name = fields.Char(compute='_calcular_nombre')

    def _calcular_nombre(self):
        """ Se calcula el nombre según el número ingresado. """
        for rec in self:
            cliente = self.cliente_id.name if self.cliente_id else ""
            vehiculo = self.vehiculo_id.marca if self.vehiculo_id else ""
            if vehiculo or cliente:
                rec.name = str(cliente) + " - " + str(vehiculo)
            else:
                rec.name = ""

    @api.onchange('cliente_id')
    def set_domain_programa(self):
        """ Se crea un dominio para que los vehículos mostrados solo sean los
         que tienen como dueño al cliente_id. """
        ids = []
        if self.cliente_id:
            for vehiculo in self.cliente_id.vehiculos_ids:
                ids.append(vehiculo.id)
        return {
            'domain': {'vehiculo_id': [('id', 'in', ids)], }
        }
