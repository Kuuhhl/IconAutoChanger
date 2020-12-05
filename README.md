# IconAutoChanger
Automatically sends requests to League of Legends on startup. This can be used for custom icons, custom clubdata, chat rank, etc. 
## Downloads
Binary version for windows can be found [here](https://github.com/Kuuhhl/IconAutoChanger/releases/)
## Installation (binary; recommended)
* Open `setup.exe`
* Follow installation steps
* After installation, open `ChangeSettings.exe` and configure your requests using the GUI.
* Restart your PC
### I get a SmartScreen warning (unknown author). What should I do?
Since my executable isn't digitally signed, you will probably get this warning. If you want to remove it, just add an Exception to your Windows Defender antivirus.

## Installation (python)
* Install dependencies (only in Python-version)
```
Python 3.8
lcu-driver
```
* Clone/Download repository
* Open `main.py`
* Configure your requests using the GUI.
* Put a shortcut to `main.py` into your AutoStart folder (Press `Windows` + `R`, run `shell:startup`.)
* Restart your PC
## Configuration
If you want to edit the requests being made, simply open `SettingsChanger.exe`/`settings.py`. You can use the GUI to edit the requests.
## Usage
Since we added the program to Autostart, you shouldn't have to do anything more than install it (see above).
## What can I do with these custom requests?
You can change things in the League of Legends Client. These include:
* Creating lobbies
* Changing icons
* Settings Clubs
* Sending friend requests
* Setting your rank shown in chat
* ...
### Examples
#### Set custom icon:

API-Endpoint: `/lol-chat/v1/me`

Method: `PUT`

Body:
```
{
"icon": 4832
}
```
#### Set chat rank:

API-Endpoint: `/lol-chat/v1/me`

Method: `PUT`

Body:
```
{
   "lol":{
      "rankedLeagueDivision":"IV",
      "rankedLeagueQueue":"RANKED_SOLO_5x5",
      "rankedLeagueTier":"IRON"
   }
}
```
#### Set club-tag:

API-Endpoint: `/lol-chat/v1/me`

Method: `PUT`

Body:
```
{
   "lol":{
      "clubsData":"bDI6aKW7DPD+sF8NuV+i6G3PDPhjyBKokFr+ezNA7141Jkl35XXwH43SFSC2q5D0mE5Yl4RibZzfaPGeWhcthdYm5fP+xB23+xsVQzHL5W9TjnVaDD40aZiCUEn3+GY5rP1xoI8Xw4e04XZZFKH+n2VCzuhXpUI3IgYC9TQJmWo="
   }
}
```
#### More
* You can browse endpoints of the LCU API with this website: https://lcu.vivide.re/
* If you need help with finding some endpoints, this server might be able to help you: https://discord.gg/bFQKCKzRuh 
