# ASCII Reader

ASCII Reader is a Python POC for reading data from ASCII files and printing a report to the console.

## Prerequisites

- This script has been tested against Python versions [3.8.10](https://www.python.org/downloads/release/python-3810/) and [3.12.2](https://www.python.org/downloads/release/python-3122/)
- Grab ASCII files [here](https://drive.google.com/file/d/1rG61SEnvdsZ4WX6MY1SEIvHbtendKJn-/view?usp=sharing)


## Usage

Pass in a Customer's first and last name as args to get their invoices and associated items

```bash
$ python ./main.py Indiana Jones
```

Names can be any case

```bash
$ python ./main.py iNdIaNa JoNeS
```

```bash
$ python ./main.py indiana jones
```

```bash
$ python ./main.py INDIANA JONES
```
## TODOs

- Improve performance
- Accept multiple names as args
- Flag to save report to a custom named file
