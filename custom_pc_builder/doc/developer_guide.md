# Developer Guide

## Getting Started

This guide will help you understand the structure and development process of the `custom_pc_builder` module in Odoo 16 Community Edition.

## Module Structure

The `custom_pc_builder` module follows the standard Odoo module structure and MVC architecture. Here is a brief overview of the module's structure:

- `__init__.py`: Initializes the module.
- `__manifest__.py`: Contains metadata about the module.
- `models/`: Contains the models for the PC builds and components.
- `views/`: Contains the views for the component selection, preview, and saved PC builds.
- `controllers/`: Contains the controllers for handling user interactions.
- `static/src/`: Contains the CSS, JavaScript, and XML files for the module's look and feel and interactivity.
- `data/`: Contains the XML data file for pre-populating the database with component data.
- `security/`: Contains the CSV file for defining access rights for the module.
- `tests/`: Contains the test files for testing the functionality of the PC build and component models.
- `doc/`: Contains the user guide, developer guide, and API documentation.

## Development Process

The development process follows the best practices for Odoo module development. This includes writing clean, well-documented code, using version control, and thoroughly testing the module before deployment.

## Models

The `pc_build` and `component` models define the data structure of a PC build and its components. They are located in the `models/` directory.

## Views

The `pc_build_view.xml` and `component_view.xml` files define the user interface for viewing and interacting with PC builds and components. They are located in the `views/` directory.

## Controllers

The `main.py` file in the `controllers/` directory handles user interactions.

## Static Resources

The `custom_pc_builder.css`, `custom_pc_builder.js`, and `custom_pc_builder.xml` files define the look and feel of the module and its interactivity. They are located in the `static/src/` directory.

## Data

The `component_data.xml` file pre-populates the database with component data. It is located in the `data/` directory.

## Security

The `ir.model.access.csv` file defines access rights for the module. It is located in the `security/` directory.

## Tests

The `test_pc_build.py` and `test_component.py` files test the functionality of the PC build and component models. They are located in the `tests/` directory.

## Documentation

The `user_guide.md`, `developer_guide.md`, and `api_documentation.md` files provide comprehensive documentation for the module. They are located in the `doc/` directory.

## Theme

The theme of the module is defined in the `custom_pc_builder.css` file and the technical name of the theme is "custom_pc_v1_nov_16".

## Conclusion

The `custom_pc_builder` module provides a valuable feature for the ecommerce website, allowing users to customize a PC build. The module is developed following the best practices for Odoo module development and includes comprehensive documentation.