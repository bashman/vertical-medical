# -*- coding: utf-8 -*-
# Copyright 2015 ACSONE SA/NV
# Copyright 2016 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    "name": "Medical Medicament",
    "summary": "Introduce Medicament notion into the medical product.",
    "version": "10.0.1.0.0",
    "category": "Medical",
    "website": "https://github.com/OCA/vertical-medical/",
    "author": "ACSONE SA/NV, LasLabs, Odoo Community Association (OCA)",
    "license": "GPL-3",
    "application": True,
    "installable": True,
    "depends": [
        "medical",
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/medical_drug_form.xml",
        "data/medical_drug_route.xml",
        "views/product_product_view.xml",
        "views/medical_medicament_view.xml",
        "views/medical_medicament_component_view.xml",
        "views/medical_drug_form_view.xml",
        "views/medical_drug_route_view.xml",
        "views/medical_menu.xml",
    ],
    "demo": [
        "demo/medical_medicament_component_demo.xml",
        "demo/medical_medicament_demo.xml",
    ],
}
