# -----------------------------------------------------------------------------
#
#    Copyright (C) 2020 jeo Software  (http://www.jeosoft.com.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# -----------------------------------------------------------------------------
{
    'name': 'cooperativas',
    'version': '9.0.0.0.0',
    'license': 'Other OSI approved licence',
    'category': 'Default Application',
    'summary': 'Customization for cooperativas',
    'author': 'jeo Software',
    'depends': [
        # basic applications
        'sale_management',
        'account_invoicing',
        'purchase',

        # minimum modules for argentinian localizacion + utilities + fixes
        # 'standard_depends_ce',

    ],
    'data': [
    ],
    'test': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': [],

    #
    # Here begins docker-odoo-environment manifest
    # --------------------------------------------

    # port where odoo starts serving pages
    'port': '8069',

    'repos': [
        {'usr': 'jobiols', 'repo': 'cl-cooperativas', 'branch': '9.0'},
        {'usr': 'marionumza', 'repo': 'odoo-coop', 'branch': 'master'},
        {'usr': 'jobiols', 'repo': 'odoo-addons', 'branch': '9.0'},

        {'usr': 'ingadhoc', 'repo': 'odoo-argentina', 'branch': '9.0'},
        {'usr': 'ingadhoc', 'repo': 'argentina-sale', 'branch': '9.0'},
        {'usr': 'ingadhoc', 'repo': 'account-financial-tools',
         'branch': '9.0'},
        {'usr': 'ingadhoc', 'repo': 'account-payment', 'branch': '9.0'},
        {'usr': 'ingadhoc', 'repo': 'miscellaneous', 'branch': '9.0'},
        {'usr': 'ingadhoc', 'repo': 'argentina-reporting',
         'branch': '9.0'},
        {'usr': 'ingadhoc', 'repo': 'reporting-engine', 'branch': '9.0'},
        {'usr': 'ingadhoc', 'repo': 'aeroo_reports', 'branch': '9.0'},
        {'usr': 'ingadhoc', 'repo': 'sale', 'branch': '9.0'},
        {'usr': 'ingadhoc', 'repo': 'odoo-support', 'branch': '9.0'},
        {'usr': 'ingadhoc', 'repo': 'product', 'branch': '9.0'},
        {'usr': 'ingadhoc', 'repo': 'stock', 'branch': '9.0'},
        {'usr': 'ingadhoc', 'repo': 'account-invoicing', 'branch': '9.0'},
        {'usr': 'ingadhoc', 'repo': 'patches', 'branch': '9.0'},

        {'usr': 'oca', 'repo': 'partner-contact', 'branch': '9.0'},
        {'usr': 'oca', 'repo': 'web', 'branch': '9.0'},
        {'usr': 'oca', 'repo': 'server-tools', 'branch': '9.0'},
        {'usr': 'oca', 'repo': 'social', 'branch': '9.0'},
        {'usr': 'oca', 'repo': 'server-brand', 'branch': '9.0'},
        {'usr': 'oca', 'repo': 'manufacture', 'branch': '9.0'},
        {'usr': 'oca', 'repo': 'manufacture-reporting', 'branch': '9.0'},
        {'usr': 'oca', 'repo': 'management-system', 'branch': '9.0'},
        {'usr': 'oca', 'repo': 'sale-workflow', 'branch': '9.0'},
        {'usr': 'oca', 'repo': 'stock-logistics-warehouse', 'branch': '9.0'},
        {'usr': 'oca', 'repo': 'stock-logistics-reporting', 'branch': '9.0'},
        {'usr': 'oca', 'repo': 'stock-logistics-workflow', 'branch': '9.0'},
        {'usr': 'oca', 'repo': 'queue', 'branch': '9.0'},
    ],

    'docker': [
        {'name': 'odoo', 'usr': 'jobiols', 'img': 'odoo-jeo', 'ver': '9.0'},
        {'name': 'postgres', 'usr': 'postgres', 'ver': '10.1-alpine'},
        {'name': 'nginx', 'usr': 'nginx', 'ver': 'latest'},
        {'name': 'aeroo', 'usr': 'adhoc', 'img': 'aeroo-docs'},
    ],

}
