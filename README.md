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
from task_6 import create_list_object
list_object=(<file_path>)
for line in list_object:
    print(line)
 => Driver(abbr='DRR', name='Daniel Ricciardo', car='RED BULL RACING TAG HEUER', 
 start_time='2018-05-24_12:11:24.067', end_time='2018-05-24_12:14:12.054', 
 lap_time='0:02:47.987')

```

#### About program

This package handle data about racers.
It reads data from files order racers by time and build, sort or print report that
shows the top 15 racers and the rest after underline, for example:
print_ascending(report):

1. Daniel Ricciardo | RED BULL RACING TAG HEUER | 1:12.013

2. Sebastian Vettel | FERRARI | 1:12.415

3. ...

------------------------------------------------------------------------

16. Brendon Hartley | SCUDERIA TORO ROSSO HONDA | 1:13.179

17. Marcus Ericsson | SAUBER FERRARI | 1:13.265


**data**  its separate folder contain time data about racers.

start.log contain start time (SVF2018-05-24_12:02:58.917)

end.log contain finish time (SVF2018-05-24_12:04:03.332)

abbreviations.txt contain decoding information abbreviations racers about.
(SVF_Sebastian Vettel_FERRARI)

You must use absolute path to the data-folder

**create_list_object** create list with drivers 
> [Driver(abbr='DRR', name='Daniel Ricciardo', 
> car='RED BULL RACING TAG HEUER', 
> start_time='2018-05-24_12:11:24.067', 
> end_time='2018-05-24_12:14:12.054', 
> lap_time='0:02:47.987')]

**print_order(** print ascending order
1. Sebastian Vettel  |FERRARI                   |0:01:04.415
2. Valtteri Bottas   |MERCEDES                  |0:01:12.434
3. Stoffel Vandoorne |MCLAREN RENAULT           |0:01:12.463
---------------------------------------------
16. Brendon Hartley | SCUDERIA TORO ROSSO HONDA | 1:13.179


**print_descending** print descending order
>'19. Lewis Hamilton    |MERCEDES                  |0:06:47.540'
>18. Esteban Ocon      |FORCE INDIA MERCEDES      |0:05:46.972
>...
 
**print_driver** find info in the report and print it.
