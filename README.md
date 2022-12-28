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

>Windows py
> 
> Unix/macOS python 
> 
and import the package:
```
from task_6_danil_shvecov import create_string_position
create_string_position(['LHM', 'Lewis Hamilton', 'MERCEDES\n', '0:06:47.540000', 'LHM'])
=>  'Lewis Hamilton    |MERCEDES                      |0:06:47.540')

```

#### About program 

This package handle data about racers. 
It reads data from files order racers by time and print report that
shows the top 15 racers and the rest after underline, for example:

1. Daniel Ricciardo      | RED BULL RACING TAG HEUER     | 1:12.013

2. Sebastian Vettel      | FERRARI                                            | 1:12.415

3. ...

------------------------------------------------------------------------

16. Brendon Hartley   | SCUDERIA TORO ROSSO HONDA | 1:13.179

17. Marcus Ericsson  | SAUBER FERRARI                            | 1:13.265

**data** folder contain time data about racers.

start.log contain start time (SVF2018-05-24_12:02:58.917)

end.log contain finish time (SVF2018-05-24_12:04:03.332)

abbreviations.txt contain decoding information abbreviations racers about.
(SVF_Sebastian Vettel_FERRARI)

This files must be saved to the path task_6/src/data/

**main** folder contain main code.

>*functions.py:*
>  def read_file(file_name) create dict like {abb:[time]...}
> if user enter wrong path to the folder program raises except FileNotFoundError

>def decoding_abbr(path_to_the_folder) decoding abbr from abbreviations.txt
> and create dict [['DRR', 'Daniel Ricciardo', 'RED BULL RACING TAG HEUER\n']...]
> if user enter wrong path to the folder program raises except FileNotFoundError

>def create_string_position(date_racer_about) 
> made great info string like 'Lewis Hamilton    |MERCEDES                      |0:06:47.540'
>
>from '['LHM', 'Lewis Hamilton', 'MERCEDES\n', '0:06:47.540000', 'LHM']'

> def build_report(start, finish) main function builds order about racer
> 1. Daniel Ricciardo      | RED BULL RACING TAG HEUER     | 1:12.013
>2. Sebastian Vettel      | FERRARI                                            | 1:12.415
>
>but doesn`t print it!

> def print_report() function get result of "build_report" function and print in the main function

**cli.py**` file handle commands from **CMD** 
*python* cli.py --files <folder_path> --asc (print report) or --desc (print abbr name and car)

*python* cli.py --files <folder_path> --driver “Sebastian Vettel”  shows statistic about driver

**!!!<folder_path> must be relative path!!!**

If user input wrong command/path_to_the_file raise special except.

**exception.py** file has all necessary exceptions.

**tests** folder has all necessary basic tests for the checking code.
