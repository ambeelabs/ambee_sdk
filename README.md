# ambee_sdk

[![License](https://shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Downloads](https://static.pepy.tech/badge/ambee-sdk)](https://pepy.tech/project/ambee-sdk)
[![Documentation Status](https://readthedocs.org/projects/ambee-sdk/badge/?version=latest)](https://ambee-sdk.readthedocs.io/en/latest/?badge=latest)

Ambee SDK for python provides classes and methods to make use of ambee's APIs inside your python code. You can make calls to our apis, get output in dataframe format, make calls to multiple locations and more.

Read our API documentation: [Ambee: Developers tool](https://docs.ambeedata.com/DeveloperTools/)

Readthedocs - [Welcome to ambee-sdk’s documentation! &mdash; ambee-sdk 0.1.0a documentation](https://ambee-sdk.readthedocs.io/en/latest/index.html)

## Getting Started

```py
import ambee_sdk as ambee
import datetime
```

```python
x_api_key = "Your Key Here"
```

```python
aq = ambee.air_quality(x_api_key=x_api_key)
aq.get_latest(by='latlng', lat=12, lng=77)
```