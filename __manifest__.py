{
    "name": "Plataforma de Agendamento para Bancos e Microfinanças",
    "version": "1.0.0",
    "odoo_version": "18.0.0",
    "summary": "Agendamento online de atendimento",
    "description": "",
    "author": "Jardel Elias Bernardo",
    'website': "https://github.com/odoomakers/ticket_scheduling",
    "depends": ['web', 'contacts'],
    'data': [
        'security/ir.model.access.csv',
    ],
    'assets': {
        'web.assets_frontent':[],
        'web.assets_backend': []
    },

    'application': True,
    "installable": True
}