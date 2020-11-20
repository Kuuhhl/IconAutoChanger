# IconAutoChanger
Automatically launches League of Legends and changes icon.
## Downloads
Binary version for windows can be found [here](https://github.com/Kuuhhl/IconAutoChanger/releases/)
## Installation
* Install dependencies (only in Python-version)
```
Python 3.8
lcu-driver
```
* Open `main.py` or `IconAutoChanger.exe`
* Input path to League of Legends Client executable if asked
* Put the file on your Desktop / an easily accessible folder
## Usage
To use it, just start the program. It should automatically launch your League of Legends Client and apply the custom icon.
## FAQ
### How do I customize my Icon?
* Find out the ID of the Icon you want (for example using [this](https://github.com/Kuuhhl/IconIDFinder))
* Press `Windows`+`R`
* Navigate to `%appdata%/IDAutoChanger/config.txt`
* Change bottom line to your desired Icon ID
### I get a SmartScreen warning (unknown author). What should I do?

Since my executable isn't digitally signed, you will probably get this warning. If you want to remove it, just add an Exception to your Windows Defender antivirus.
# Issues
If you have any issues, you can report them [here](https://github.com/Kuuhhl/IconAutoChanger/issues).
