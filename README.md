[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT) [![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)

<img src="images/StockEssence_logo_enlarge.gif" alt="drawing" width="200px"/>

# StockEssence
Displays data and ratios of stocks and rates them via API

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

First, make sure `Python` is up to date:
[Python3](https://www.python.org/downloads/)

Ensure Python is in PATH

#### Install PIP
Download get-pip.py:
```
$ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```

Inspect get-pip.py for any malevolence. Then run the following:
```
$ python get-pip.py
```

Install Python requests module:
```
$ pip install requests
```
Install Python Kivy module:
```
$ pip install kivy
```

### Installing

Simply clone or download repository

## Usage
Edit the list in src/data/my_companies.txt (One company symbol per line, leave the first line alone)

Navigate to the /src/ folder
```
$ python StockEssence.py
```
*Note: Initial load may take up to 1 second per symbol*

## Built With

* [Requests module for Python](http://docs.python-requests.org/en/master/) - Web API calls
* [kivy module for Python](https://kivy.org/) - GUI
* [Financial Modeling Prep](https://financialmodelingprep.com/) - Stock Data

## Contributing

Please read [CONTRIBUTING.md] for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/GriffinAustin/StockEssence/tags). 

## Authors

* **Griffin Austin** - *Initial work* - [GitHub](https://github.com/GriffinAustin)

See also the list of [contributors](https://github.com/GriffinAustin/StockEssence/graphs/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
