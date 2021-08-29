from odoo import fields, models, api


class PlanillaHoraria(models.Model):
    _name = 'taller.planilla_horaria'
    _description = 'Planilla Horaria'

    empleado_id = fields.Many2one('taller.empleado',
                                  string='Empleado',
                                  required=True)
    fecha = fields.Date(string='Fecha',
                        default=fields.Datetime.now,
                        required=True)
    hora_ingreso = fields.Float(string='Hora Ingreso')  # Poner wid float_time
    hora_salida = fields.Float(string='Hora Salida')  # Poner wid float_time
    inicio_desc = fields.Float(string='Inicio Descanso')
    fin_desc = fields.Float(string='Fin Descanso')
    name = fields.Char(related='empleado_id.name')
