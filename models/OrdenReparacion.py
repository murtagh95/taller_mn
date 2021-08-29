from odoo import fields, models


class OrdenReparacion(models.Model):
    _name = 'taller.orden_reparacion'
    _description = 'Orden Reparación'

    estado = fields.Selection(
        [('pres', 'Presupuesto'),
         ('desa', 'Desarmado'),
         ('compr', 'Compra Repuesto'),
         ('arma', 'Armando'),
         ('fina', 'Finalizado')],
        string='Estado',
        required=True
    )
    descripcion = fields.Html(string='Descripción')
    insumos_ids = fields.Many2many(
        'taller.insumo',
        relation='orden_reparacion_insumo_rel',
        column1='orden_reparacion_id',
        column2='insumo_id',
        string='Insumos',
        required=True
    )
    empleado_ids = fields.Many2many(
        'taller.empleado',
        relation='orden_reparacion_empleado_rel',
        column1='orden_reparacion_id',
        column2='empleado_id',
        string='Empleados',
        required=True
    )
    ingreso_vehiculo_id = fields.One2many(
        'taller.ingreso_vehiculo',
        'orden_reparacion_id',
        string='Ingreso Vehiculo'
    )
    name = fields.Char(compute='_calcular_nombre')

    def _calcular_nombre(self):
        """ Se calcula el nombre según el estado. """
        estado = self.estado or ""
        cliente = self.ingreso_vehiculo_id[0].cliente_id.name or ""

        if self.estado:
            self.name = str(estado) + " - " + str(cliente)
        else:
            self.name = ""
