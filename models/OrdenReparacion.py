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
    name = fields.Char(related='estado')
