from odoo import fields, models


class Insumo(models.Model):
    _name = 'taller.insumo'
    _description = 'Insumo'

    codigo = fields.Char(string='Código')
    name = fields.Char(string='Nombre')
    marca = fields.Char(string='Marca')
    costo = fields.Integer(string='Costo')
    lote = fields.Char(string='Lote')
    tipo_id = fields.One2many(
        'taller.categoria_insumo',
        'insumo_ids',
        string='Tipos'
    )


class CategoriaInsumo(models.Model):
    _name = 'taller.categoria_insumo'
    _description = 'Categoría Insumo'

    insumo_ids = fields.Many2one('taller.insumo',
                                 string='Código insumo')
    name = fields.Char(string='Nombre')
    active = fields.Boolean(string='Activo')
