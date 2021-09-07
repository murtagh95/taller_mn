from odoo import fields, models, api
from odoo.exceptions import ValidationError


class Factura(models.Model):
    _name = 'taller.factura'
    _description = 'Factura'

    tipo = fields.Char(string='Tipo', required=True)
    serie = fields.Integer(string='Serie/Sucursal', required=True)
    nro_factura = fields.Integer(string='Nro Factura', required=True)

    @api.constrains('tipo', 'serie', 'nro_factura')
    def _verifico_campos_unicos(self):
        """ Se valida que no exista ya registros con los mismos datos. """

        factura = self.search([
            ('tipo', '=', self.tipo),
            ('serie', '=', self.serie),
            ('nro_factura', '=', self.nro_factura),
        ])
        if factura:
            raise ValidationError(
                "No se puede crear la factura debido que ya existe una factura"
                " con este tipo, serie y nro factura.")


class FacturaCompra(models.Model):
    _name = 'taller.factura_compra'
    _description = 'Factura Compra'
    _inherits = {'taller.factura': 'factura_id'}

    factura_id = fields.Many2one('taller.factura',
                                 required=True,
                                 ondelete='cascade')
    proveedor_id = fields.Many2one('taller.proveedor',
                                   string='Proveedor',
                                   required=True)
    orden_reparacion_id = fields.Many2one('taller.orden_reparacion',
                                          string='Orden Reparación',
                                          required=True)
    name = fields.Char(compute='_calcular_nombre', required=True)
    remito = fields.Char(string='Remito')
    fecha = fields.Datetime(string='Fecha',
                            default=fields.Datetime.now,
                            required=True)

    def _calcular_nombre(self):
        """ Se calcula el nombre de la factura compra en base al proveedor y
         la orden de reparación. """
        prov = self.proveedor_id.name or ""
        orden = self.orden_reparacion_id.name or ""
        if prov or orden:
            self.name = str(prov) + " - " + str(orden)
        else:
            self.name = ""


class FacturaVenta(models.Model):
    _name = 'taller.factura_venta'
    _description = 'Factura Venta'
    _inherits = {'taller.factura': 'factura_id'}

    factura_id = fields.Many2one('taller.factura',
                                 required=True,
                                 ondelete='cascade')
    cliente_id = fields.Many2one('taller.cliente',
                                 string='Proveedor',
                                 required=True)
    orden_reparacion_id = fields.Many2one('taller.orden_reparacion',
                                          string='Orden Reparación',
                                          required=True)
    name = fields.Char(compute='_calcular_nombre', required=True)
    precio = fields.Integer(string='Precio')

    def _calcular_nombre(self):
        """ Se calcula el nombre de la factura compra en base al proveedor y
         la orden de reparación. """
        prov = self.cliente_id.name or ""
        orden = self.orden_reparacion_id.name or ""
        if prov or orden:
            self.name = str(prov) + " - " + str(orden)
        else:
            self.name = ""
