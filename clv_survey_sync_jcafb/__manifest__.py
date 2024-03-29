# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Survey External Sync (for CLVhealth-JCAFB Solution)',
    'summary': 'Survey External Sync Module used in CLVhealth-JCAFB Solution.',
    'version': '14.0.5.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'CLVsol Solutions',
    'license': 'AGPL-3',
    'website': 'https://github.com/CLVsol',
    'depends': [
        'clv_survey',
        'clv_external_sync',
    ],
    'data': [
        'data/survey_survey_sync.xml',
        # 'data/survey_question_1_sync.xml',
        'data/survey_question_2_sync.xml',
        # 'data/survey_question_3_sync.xml',
        # 'data/survey_question_4_sync.xml',
        'data/survey_question_5_sync.xml',
        'data/survey_question_answer_sync.xml',
        # 'data/survey_user_input_1_sync.xml',
        'data/survey_user_input_2_sync.xml',
        'data/survey_user_input_3_sync.xml',
        # # 'data/document_sync_2.xml',
        # 'data/survey_user_input_line_1_sync.xml',
        'data/survey_user_input_line_2_sync.xml',
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
