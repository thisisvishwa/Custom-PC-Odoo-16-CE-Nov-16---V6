# API Documentation

## Overview

This document provides the API documentation for the Custom PC Building module in Odoo 16 Community Edition.

## Models

### PC Build

- `create(vals)`: Creates a new PC build with the given values.
- `write(vals)`: Updates the PC build with the given values.
- `unlink()`: Deletes the PC build.
- `copy(default=None)`: Duplicates the PC build.

### Component

- `create(vals)`: Creates a new component with the given values.
- `write(vals)`: Updates the component with the given values.
- `unlink()`: Deletes the component.
- `copy(default=None)`: Duplicates the component.

## Controllers

### Main

- `pc_build()`: Returns the PC build view.
- `component()`: Returns the component view.
- `save_pc_build()`: Saves the current PC build.
- `load_pc_build()`: Loads a saved PC build.

## Errors

- `InvalidComponentError`: Raised when an invalid component is selected.
- `InvalidPCBuildError`: Raised when an invalid PC build is created.

## Conclusion

This API documentation provides a comprehensive guide to the Custom PC Building module's API. For more detailed information, please refer to the user guide and developer guide.