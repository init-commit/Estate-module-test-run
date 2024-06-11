# 

{
    'name' : 'Estate Mamangement',
    'version' : '1.0.0',
    'sequence' : '-100',
    'application' : True,
    'category' : 'Estate Management',
    'description' : """Estate Management demo by Everlast LTD""",
    'author' : 'Everlast',
    'website' : 'www.everlast.org',
    'summary' : 'My second module',
    'depends' : [],
    # data will contain all the xml files / importing
    'data' : [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/realtors.xml',
    ],
    # demo will be for importing demo files
    'demo' : [],
    'installable' : True,
    'auto_install' : False,
    # 'application' : True,
    'license' : 'AGPL-3',
}