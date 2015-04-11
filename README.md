# plugin-loader

import helper for your app's plugin.

## Install

`$ pip install plugin-loader`

## Usage

Wildcard is *

```
from plugin_loader import load_plugin

plugins = load_plugin("flask_*")
```

your app's plugin name must be ruled.

ex.

+ flask_hoge, flask_fuga, ...
+ fluent_plugin_hoge, fluent_plugin_fuga, ...
+ gulp_hoge, gulp_fuga, ...

