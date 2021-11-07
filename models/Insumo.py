from odoo import fields, models


class Insumo(models.Model):
    _name = 'taller.insumo'
    _description = 'Insumo'

    codigo = fields.Char(string='Código')
    name = fields.Char(string='Nombre')
    marca = fields.Char(string='Marca')
    costo = fields.Integer(string='Costo')
    lote = fields.Char(string='Lote')
    categoria_id = fields.Many2one('taller.categoria_insumo',
                                   string='Categoria')


class CategoriaInsumo(models.Model):
    _name = 'taller.categoria_insumo'
    _description = 'Categoría Insumo'
    
    name = fields.Char(string='Nombre')
    active = fields.Boolean(string='Activo', default=True)
