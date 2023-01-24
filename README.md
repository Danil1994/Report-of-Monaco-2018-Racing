# Shvecov_Danil`s_project

+ ### Python developer [Shvecov Danil](https://github.com/Danil1994)
+ ### Mentor [Divnich Andrii](https://github.com/DivnychAndrii)

#### *Task from [foxminded](https://lms.foxminded.com.ua/) courses.*

Install

1. Create a virtual environment and install task-6-danil-shvecov
   package from TestPyPI. Open terminal and run

> Windows ```py -m pip install -i https://test.pypi.org/simple/ task-6-danil-shvecov```

> Unix/macOS ```python3 -m pip install --index-url https://test.pypi.org/simple/ task-6-danil-shvecov```

pip should install the package from TestPyPI and the output should look something like this:

```
Collecting task-6-danil-shvecov
Downloading https://test-files.pythonhosted.org/packages/.../task-6-danil-shvecov_0.0.1-py3-none-any.whl
Installing collected packages: task-6-danil-shvecov
Successfully installed task-6-danil-shvecov-0.0.1
```

You can make sure that you have been installed this package. Open terminal
and run

> Windows py
>
> Unix/macOS python
>
and import the package:

```
from task_6_danil_shvecov import define_laps_time
define_laps_time(['2018-05-24_12:02:58.917', '2018-05-24_12:04:03.332'])
 => '0:01:04.415'

```

#### About program

This package handle data about racers.
It reads data from files order racers by time and build, sort or print report that
shows the top 15 racers and the rest after underline, for example:
dafine_position(report):

1. Daniel Ricciardo | RED BULL RACING TAG HEUER | 1:12.013

2. Sebastian Vettel | FERRARI | 1:12.415

3. ...

------------------------------------------------------------------------

16. Brendon Hartley | SCUDERIA TORO ROSSO HONDA | 1:13.179

17. Marcus Ericsson | SAUBER FERRARI | 1:13.265

print_report(report):
{'SVF': ['Sebastian Vettel', 'FERRARI', '2018-05-24_12:02:58.917', '2018-05-24_12:04:03.332', '0:01:04.415']...

**data**  its separate folder contain time data about racers.

start.log contain start time (SVF2018-05-24_12:02:58.917)

end.log contain finish time (SVF2018-05-24_12:04:03.332)

abbreviations.txt contain decoding information abbreviations racers about.
(SVF_Sebastian Vettel_FERRARI)

You must use absolute path to the data-folder

**main** folder contain main code.
> *functions.py:*
> def build_report(start, finish, abbreviations) main function builds order about racer
> {'SVF': ['Sebastian Vettel', 'FERRARI', '2018-05-24_12:02:58.917', '2018-05-24_12:04:03.332', '0:01:04.415']...
>but not sort and not print it.

> def print_report(report) function prints order

>def define_position(order) define racers position and print it
1. Daniel Ricciardo | RED BULL RACING TAG HEUER | 1:12.013

2. Sebastian Vettel | FERRARI | 1:12.415

3. ...

------------------------------------------------------------------------

16. Brendon Hartley | SCUDERIA TORO ROSSO HONDA | 1:13.179

17. Marcus Ericsson | SAUBER FERRARI | 1:13.265

