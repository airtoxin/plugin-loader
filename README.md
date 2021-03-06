# plugin-loader

import helper for your app's plugin.


[![](https://img.shields.io/pypi/v/plugin-loader.svg)](https://pypi.python.org/pypi/plugin-loader/)
[![](https://pypip.in/egg/plugin-loader/badge.svg)](https://pypi.python.org/pypi/plugin-loader/)
[![](https://img.shields.io/pypi/wheel/plugin-loader.svg)](https://pypi.python.org/pypi/plugin-loader/)
[![](https://img.shields.io/pypi/l/plugin-loader.svg)](https://pypi.python.org/pypi/plugin-loader/)

## Install

`$ pip install plugin-loader`

## Usage

Wildcard is *

```python
from plugin_loader import load_plugin

plugins = load_plugin("flask_*")
```

your app's plugin name must be ruled.

ex.

+ flask_hoge, flask_fuga, ...
+ fluent_plugin_hoge, fluent_plugin_fuga, ...
+ gulp_hoge, gulp_fuga, ...

## Develop

### update readme

`$ pandoc -f markdown -t rst README.md > README`
