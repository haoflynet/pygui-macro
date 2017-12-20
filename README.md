# pygui-macro

Cross-platform gui macro command tool with python, automate your keyboard and mouse. You can use it to record keyboard and mouse action, and rerun it as a script.


### Support Events

- **on_press**: keyboard press event
- **on_release**: keyboard release event
- **on_move**: mouse move event
- **on_click**: mouse click event
- **on_scroll**: mouse scroll event

## Installation

Using pip, type in your command-line prompt

```
pip install pygui-macro
```

Or clone the repo and inside the pygui-macro directory, type

```
python setup.py install
```

## Usage
### Record

```
>>> pygui-macro record -h
usage: gui-macro.py record [-h] [-d DELAY] [-o ORIGINAL] [-oa] [-e END_KEY]
                           [-ie INCLUDE_EVENTS] [-f FILE] [-c] [-ar]

optional arguments:
  -h, --help            show this help message and exit
  -d DELAY, --delay DELAY
                        delay time to record (default: 3)
  -o ORIGINAL, --original ORIGINAL
                        original coordinate (default: 0, 0)
  -oa, --original_auto  set original coordinate automatically (default: False)
  -e END_KEY, --end_key END_KEY
                        end record hot key (default: Esc
  -ie INCLUDE_EVENTS, --include_events INCLUDE_EVENTS
                        which event be recorded (default: [])
  -f FILE, --file FILE  macro script filename (default: script
  -c, --continue        continuee (default: false)
  -ar, --auto_release   whether auto release the key (default: true)
```

Example

```
sudo pygui-macro record -ie on_press
```

### Run

```
>>> pygui-macro run -h
usage: gui-macro.py run [-h] [-f FILE]

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  specify the macro script filename (default: script)
```

Example

```
sudo pygui-macro run
```

## TODO
- verify script
- if statement
- while statement

## Copyright & License

Copyright (c) 2017 haoflynet - Released under The MIT License.