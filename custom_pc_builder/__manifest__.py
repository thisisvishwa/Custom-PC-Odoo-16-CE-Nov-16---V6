{
    'name': 'Custom PC Builder',
    'version': '1.0',
    'category': 'Website',
    'summary': 'Custom PC Building Module',
    'sequence': 1,
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'depends': ['base', 'website_sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/pc_build_view.xml',
        'views/component_view.xml',
        'data/component_data.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'description': """
Custom PC Building Module
=========================
This module allows users to customize a PC build by selecting components such as CPU, RAM, GPU, storage, and peripherals. 
Users can preview their PC build, save and retrieve them later. 
The module provides a user-friendly interface for users to create, customize, and view their PC builds.
""",
}