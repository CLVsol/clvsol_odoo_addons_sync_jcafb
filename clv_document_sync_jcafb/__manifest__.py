# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Document External Sync (for CLVhealth-JCAFB Solution)',
    'summary': 'Document External Sync Module used in CLVhealth-JCAFB Solution.',
    'version': '14.0.5.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'CLVsol Solutions',
    'license': 'AGPL-3',
    'website': 'https://github.com/CLVsol',
    'depends': [
        'clv_document',
        # 'clv_document_jcafb',
        'clv_external_sync',
    ],
    'data': [
        'data/document_category_sync.xml',
        'data/document_marker_sync.xml',
        'data/document_type_sync.xml',
        'data/document_type_parameter_sync.xml',
        'data/document_1_sync.xml',
        'data/document_2_sync.xml',
        'data/document_item_1_sync.xml',
        'data/document_item_2_sync.xml',
    ],
    'demo': [],
    'test': [],
    'init_xml': [],
    'test': [],
    'update_xml': [],
    'installable': True,
    'application': False,
    'active': False,
    'css': [],
}
