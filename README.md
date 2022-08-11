# Leek
Leek is a simple and minimalistic command-line file manager for Windows OS. It is controlled by short typed commands such as `help`, some of these commands require additional parametres such as `rename new_name.txt`. Everything is displayed in console using rich text formatting thanks to the Rich library. The application displays panels, tables and lines of text in the console. In leek selection of items is done by the item IDs and usually before using the apropriate command.

*Possible display of the application on startup*
![Leek console display system](https://github.com/Otas02CZ/leek/blob/main/docs/images/startup.png)
*Possible display of the application when in the Windows folder*
![Leek console display system](https://github.com/Otas02CZ/leek/blob/main/docs/images/windows_folder.png)

## Usage
Leek displays directory contents on pages of specified length. You can change the length of the page by typing `rows desired_length`. When there is more content than can be shown you can use `next` or `previous` commands to get to next or previous page respectively. In order to open a certain file or folder you use its shown ID and type `open id`. For commands that require a beforehand selection of items such as `rename copy copyrename delete move` you have to selected the items in the folder you are at the moment by typing a select command and the required ID, IDs or range of IDs - form example - `select 1` or `select 1 2 3 4 5 6` or `select 1 - 6`. Typing only `select` selects everything in the current folder. You can also use command `add` which adds specified items to the current selection and works in the same way as command `select`. To view the current selection type `showselect`. In order to remove items from this selection type `unselect` to remove everything or add the IDs from the selection list shown by command `showselect` to remove only specified items. In order to go up to the parent folder type `up`. If you wish to copy a selection into the folder you are at the moment type `copy`. Use of commands `remove move` works in the same manner. If you wish to rename a single item, then you have to select it and type `rename new_name` or if you wish to copyrename it type `copyrename new_name`. If you wish to rename or copyrename multiple selected items you also have to specify the counter options and the extension - for example - `rename new_name(or |none| to be omitted) after(position of the counter will be after new_name) counter_start counter_increment counter_digits(0 to fit the counter length) extension(can use |none| to omit or |base| to keep the current one)` - example `rename picture after 0 1 0 |base|`. If you wish to create a new folder type `makedir dirname`. There are multiple other functions such as searching, sorting, directory size getter, ... For all information about the funcions and about more comprehensive help please take a look into the built in help page in the application which can be summoned by typing `help`.

## Langauge support
Leek has built-in language support engine for every string of text present.
The current built-in language support consists of:
 - Czech - cs
 - English - en

In order to switch between languages type `locale language_tag` - example - `locale en`
If you want to add additional language support you can drop a translation to the `%APPDATA(Roaming)/Leek/locales` in a format of language_tag.llf - example `en.llf`
The format is specified like this:
 - it is a python dictionary in text form
 - contents of the file should be:
   - `{ "tag_name" : { "keyword" : "localized_string", ......}}` - example - `{ "en" : { "open_file_success" : "The specified file opened successfuly", ......}}`

You can use the translation templates and create your own translation and if you would like you could contribute with it to the project.
The only thing you need to do is to translate the localization strings and keep the ammount of {} brackets in the given string.
Translation templates:
 - [From Czech Translation Template](https://github.com/Otas02CZ/leek/blob/main/making%20locales/cs_localization_temp.llf)
 - [From English Translation Template](https://github.com/Otas02CZ/leek/blob/main/making%20locales/en_localization_temp.llf)

In order for the application to recognize the additional languages you need to set the `saveconfig` option to `true`.

## Feature list
The application is capable of:
 - Viewing files, folders and drives and information about them.
 - Opening files and folders.
 - Copying, moving, renaming, copy_renaming and deleting files and folders
 - Changing between the pages
 - Getting to the parental directory
 - Getting to the root of the file system and to the root of the drive
 - Informing about folders size
 - Sorting and searching
 - Providing information and error messages
 - Showing information about the application and built-in help
 - Changing simple configuration and saving or loading it
 - Changing between locales
 - Changing between units of size
 - and much more

## Command list
This is the list of commands:
 - select
 - add
 - showselect
 - unselect
 - root
 - roots
 - help
 - refresh
 - exit
 - info
 - rows
 - open 
 - drive
 - up
 - next
 - previous
 - remove
 - copy
 - move
 - makedir
 - rename
 - copyrename
 - search
 - dirsize
 - sort
 - locales
 - locale
 - saveconfig
 - sizeunit

## Perfomance, code, dependencies, compiling and copyright notice
The application was coded in quite a "naive" way in Python, so its perfomance is its worst aspect, in most of the cases the application is capable of providing realtime updates but if you use it for handling larger file or folder sets its perfomance quickly degrades.

The application utilizes Python of version 3.10 - exported on version 3.10.6, it also utilizes the Rich library of version 12.5.1. For exporting and compiling Pyinstaller is used of version 5.3, for release file compression UPX is used of version 3.96 and for any additional zip archives 7-Zip 22.01 is utilized.

If you wish to compile the applicatin with Pyinstaller you may use this command - `pyinstaller leek.py --onefile --hidden-import rich --hidden-import datetime --hidden-import operator --hidden-import shutil --hidden-import os --hidden-import stat --hidden-import pathlib --hidden-import configuration --hidden-import localization`.

I would like to express many thanks to all the contributors and creators of the programs and libraries which were or are used during the development of this application.

Licenses and legal information for the software used by this application is located in the folder [legal](https://github.com/Otas02CZ/leek/tree/main/legal)

List of used software and links:
- Python - [homepage](https://www.python.org/)
- Rich library - [homepage](https://github.com/Textualize/rich)
- Pyinstaller - [homepage](https://pyinstaller.org/en/stable/)
- UPX - [homepage](https://upx.github.io/)
- 7-Zip - [homepage](https://www.7-zip.org/)

UPX additional legal notice - UPX is Copyright © 1996-2020 by Markus F.X.J. Oberhumer, László Molnár & John F. Reiser. The term UPX is a shorthand for the Ultimate Packer for eXecutables. All trademarks, brands, and names are the property of their respective owners.

