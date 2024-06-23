=== ReadMe ===

===Yeongu Notes ===

Yeongu Notes is a Windows notepad app, created to be simple and customizable.

Please note that this app was made for Windows 11 and that I have no academic background whatsoever in computer science, the code to this app was written through self-learning so this isn't perfectly stable or resource efficient, but it hopefully works well enough for your needs. :)




==== How to use ====




=== General ===

The general idea is similar to Windows' default Notepad. The app will open files as text, you edit it, and the text is saved. You may save it somewhere else or create a new file too. This is all organized by tabs.

There is a top menu with information about the total size of the text, number of characters selected, position of the cursor, zoom, and the path where the file is currently saved (if in full screen, also the navigation buttons).
Below the top info bar there's the tab selection bar which you can select the active tab (like in the default Notepad app).
Below this there is a menu bar on the left (listed below), a label to display info, time and date and on the right side a set of buttons (also listed below).

The rest of the screen is dedicated to the text area where you can edit the text like in any text editor.




=== Navigation and window ===

The window is fullscreen by default, if you click the maximize button (or click F11) the window the window size will reduce, and clicking it again fullscreens the window.

Inside the window there are tabs, each is a separate document with its own text, associated file, colour view info, etc. To change tabs you may use the tab selector at the top or use Ctrl + Tab / Ctrl + Shift + Tab. It is not possible to change the order of tabs or drag them.

If a window is open and file is opened through windows, like cmd or file explorer, a new tab will be added to the existing window, unless you change this in settings, in which case a new window is opened instead.




=== Menus ===

On the top bar there are 9 (or 8) menus, each with a set of options listed below:



== File ==

- Open: opens a file into a new tab. The app is designed for .txt files saving metadata to files only works for .txt files. However, other types of files can also be opened and edited, such as .log ,  .caption or .png. Opening a PNG will load its metadata and then save it back to the image.

- Save: Saves the content to the existing file, if there is one.

- Save as: Creates a new file and saves the content to it.

- Save all: Saves all tabs which already have a file and saves as the remaining ones.

- Backup all: Manually backs up all tabs.

- Exit: Exits the app.



== Edit ==

- Rearrange rows: Opens a different mode which allows the user to rearrange the position of rows by dragging them around or using arrow keys (left/right to change their position and up/down to change selection). Once you're done click 'Done' or press Enter, or click 'Cancel' (press Escape) to not apply the changes and keep the text as it was. Pressing Ctrl Z / Ctrl Y while rearranging rows undoes your last action or redoes it. Note that a row is limited by paragraphs, if the content is wrapped it will seem to have more lines than it actually does.

- Rearrange rows window: Works similar to rearrange rows but instead of changing the editor's mode, it opens a separate window which works like the rearrange rows feature, except that you don't have to click 'Done' or 'Cancel', actions are updated to the text in real time. If you open a window to rearrange rows, it will get the current content, but if you change the content while the window is opened the content on the window will not be updated. So if you open a rearrange rows window, don't edit the text or rearranging the rows will delete the changes. Always open a new window after editing the text.

- Find and replace: Opens a window which has 2 inputs: a find entry and a replace entry. This works like every find and replace, and it has features to find the text inside words or match the full word, to ignore or not casing, highlight all words that match or to find within the selection (Note that once you focus on the find and replace window your selection on the text will not be visible, but it will still be applied in this feature when you use it).

- Add indices: Writes to the start of each selected paragraph starting in 1 (if there is no selection then this applies to the entire content). This is not a label on the UI, it edits the content. It also adds a separator between the indices and the content, which is ' ' by default.

- Add programming indices: It's the same as 'Add indices' except that it starts from 0.

- Add indices starting from... : It's the same as 'Add indices' except that it starts from the number which the user chooses.

- Remove indices: This feature removes indices instead of adding them, it will look for the separator in the beginning of each line and if there's a number before it, both the number and the separator are deleted.

- Change separator: This allows you to change the separator between the indices and content. To do things like this: 
1 - Line one
2 - Line two
etc.
Changing the separator will also change the remove indices behaviour.

- Time and date: Adds the current time and date to the cursor position in the format yyyy-mm-dd hh:mm:ss.

- Overwrite: Overwrites the content instead of inserting to it, the normal feature in a text editor when clicking 'Insert'.

- strikethrough: Adds strikethrough on the current selection (or everything if there's none). Keep in mind that .txt files don't support this feature, so if you don't use the metadata feature, the strikethrough won't be there the next time the app is opened.



=== View ===

Zoom in / out / default: Zoom in or out by a factor of 1.1, or resets it to 100%

Word wrap: Toggles between using word wrap or not. The default enabling of wrap can be adjusted in settings. When wrap is False a horizontal scrollbar spawns when needed.

Rainbow cursor: Makes the cursor rapidly blink in random colours.

Go to: Prompts the user a line for which the cursor and scroll go to.

Spell check everything: Spell checks the entire text and highlights the misspelled words or removes the highlight if they're already highlighted. Note that if the tab's spell checking is off the highlighting won't go away or be updated until you toggle it back, even if you change the content.

Loading bar: Toggles manually the loading bar.

Toggle scrollbar/ horizontal scrollbar: Manually hide or show the scrollbars.



=== Tab ===

New tab: Creates a new empty tab.

Close tab: Closes the current tab, if it is not saved it will prompt the user to save it. If it's the last remaining tab the app is closed (the shortcut Ctrl + Shift + T will reopen the last closed tab).

Duplicate tab: Creates a tab with the same content and attributes as the current tab, except that the name will end with ' - Copy' and it will not be saved anywhere.

Rename tab: Renames the current tab and the filename associated with it. Note that if the filename already exists, instead of overwriting it's added [n] to the filename.

Recolour tab: Prompts the user a new colour for the current tab.

Change tab font: Changes the font of the current tab (only). Leaving the filed blank returns it to the default font. This allows you to have different tabs with different fonts without changing the default.

Clear memento stacks: Deletes all information of undo and redo history (in the current tab) as well as the list of last closed tabs, for piece of mind in important documents.

Backup tab: Backs up the current tab.

Refresh tabs: Refreshes all tabs, this is what happens when important changes are made, if there's a glitch this may be able to solve it.



=== Security ===

Mount / Dismount: Mounts the drive according to the given info given by the 'cmd_' constants in the config file. In order for this feature to function you must first fill these constants with methods to mount your secure location through the command line. What the code does is running these snippets in subprocesses to mount or dismount your drive. Ideally this is associated with a script that prompts for a password or some kind of security feature. In order for this to work properly the path for the encrypted drive should be unavailable when it is not mounted. I recommend VeraCrypt for drive encryption.

Stay mounted this time: When the drive is mounted through the app, it will automatically dismount it back when exiting, clicking this option will disable that behaviour so the drive stays mounted when leaving the app. Clicking it again toggles it back to True.



=== Documents ===

The documents tab is dedicated to choosing where your file is saved. You can choose where your preferred documents folder is in settings.
In the Documents menu all the folders inside your chosen folder are shown and so are the ones inside them. You can click any of these and the next time you save the file, it will be saved there. What this does is merely creating a blank file and associating it with the current tab. If you are editing a document that already exists it will stay as is (so you should save it before clicking a folder in documents). The blank file created will only have content after you save it, and if you chose to keep it unsaved it will be automatically deleted.
This mechanic works differently if the tab is secured; however secured tabs (which are discussed below) are meant for encrypted locations and the Documents folder is not. The security folder is the alternative to this feature. Note that just like renaming a tab, if you try to save your tab somewhere which already has a file with that name, the current tab will have [n] added instead of overwriting the existing content.



=== Security Folder ===

This folder works like the Documents folder except that this one is designed to be an encrypted location. This option only shows up after the drive is mounted (or the path to the folder is available by other means). This option will also move the file opposed to copying it, so not only it creates a blank file at the selected location but it also toggles the tab to being secured. This means that the existing saved file is removed if there is one. So if this feature is used and then the file is not saved (nor is the secured option turned off), the content will be lost, because the old file is deleted and the content is not saved to the blank file, which is deleted for being blank.



=== Configurations ===

Settings: The settings use the config.toml file to change the app's settings.  Clicking  'Defaults' loads the values from the config_default.toml file. 'Restart' will restart the app, 'Save' will save the current values to the config file, 'Apply' will not save the settings but it will start using them on the current session (this doesn't work for all settings), and 'Apply, Save & Exit' saves and applies the changes, then closes the window.
Anything with 'bg' or 'fg' refers to background or foreground colours. You may write the name of a colour (there's limited options) or its hex value, there's also the option to pick it from a colour picker.

The settings variables try to be explanatory enough but there's a couple options worth discussing:

ico_path: The path for the app's icon (in .ico format).

navigation_buttons: With this option set to false the app will not have the minimize, maximize and close navigation buttons when in fullscreen mode.

text_font: This app was tested and created using Samsung Sans Regular, but you may use your preferred font, just type the name which Windows recognizes the font for, as shown in Font settings in Windows. The same applies for other variables using fonts.

== use_tab_colours ==

When this option is turned on all new tabs will be associated with a random colour (which is not too dark or bright), and then a foreground colour (for the text in that colour) which is white or black based on what gives more contrast then a subcolour will be calculated which is slightly darker or lighter than the main colour (if the main colour is bright the subcolour is darker, otherwise it will be brighter). The buttons will turn either of these colours when pressed, the cursor will be the tab's colour and the selection will be the subcolour. The scrollbar will turn to the main colour when hovered as well.

If this option is off the tab colour will be dictated by the values in the settings for tab_0_colour, tab_1_colour... The number being their order.
The cursor colour, selection background, foreground and the other colours will also be based on the settings. If you change these colours but keep the use_tab_colours option on, none of these settings will matter.

use_file_menu: This toggles the use of the 'Documents' menu.

use_file_backup: This settings toggles the use of backup which is described below.

== use_spell_checking ==

When using spell checking words which are incorrectly spelled (in a certain language) are underlined in red. When this option is on every tab will have a spell checking button, tabs with this option on will be spell checked as the user types. The setting spell_check_typing_range controls the range of the spell checking, by default only the line which is being typed will be spell checked, the available options are 'full' for the entire doc, 'line' for only the line being typed or '2lines' for the current and previous lines compared to the cursor. Spell checking is available in the following languages: English, Spanish, French, Italian, Portuguese, German, Russian, Arabic, Latvian, Basque and Dutch. The setting use_typing_language_to_spell_check will make it so the language to spell check is the one being typed, if this is set to False then the languages listed in spell_check_languages will be used instead.
When use_spell_checking is off the buttons won't appear and nothing will be highlighted automatically but you can still manually spell check it from the 'View' menu or by using the shortcut.

auto_quotes: The auto quotes feature adds an extra quote or close parenthesis, barcket... when one is typed. For example, typing '(' will write '()' and leave the cursor inside the parenthesis, or if there is selected text, the selection will be inside parenthesis and the cursor will stay after. If there is already text before or after the cursor this will not apply. The available characters are: ' , " , ( , { , [ , < . This feature can be turned off in settings.

get_title_from_text: By default, when something is written between '===' in the first line of the content, the title of the tab and file are named based on what's within '==='. In settings this can be disabled.

info_lables_timer: When enabled the information shown on buttons when hovering over them will disappears after 5 seconds.

auto_secure_at_sf: Secure the tab automatically when clicking a folder in the Security Folder menu.

text_gaps: When enabled a gap on the left side of the screen appears. You can click it or drag along it to select lines in the text.

show_full_paths: If enabled the full paths are displayed at the top right side of the screen, otherwise only the drive name and 3 last directories are shown.

reopen_after_exit: When enabled, the currently open tabs (excluding secure tabs) will have their path saved to a .toml file once the app is exited. When the tab is opened the next time these files are reopened to keep where you left off.
This option is also available in the Configurations menu.

default_autosave / metadata / backup: These options allow you to chose the default states of the autosave, metadata and backup options when creating or opening a new file. (These features are discussed below.)
 These options are also available in the Configurations menu.

new_window_when_opening: When enabled, whenever an instance is running and a file is opened from Windows (such as through file explorer), a new window is opened, opposed to a new tab in the existing window.



=== Help ===

About Yeongu Notes: Spawns a window with version info, basic insights, license and contact info.


Documentation: Opens this ReadMe file in a new tab.




==== Options ====

There are 6 additional options which are toggleable through buttons on the right side of each tab:


Backup: Every tab with the backup option turned on will be backed up once the app is exited to a backup folder, secure tabs have a seperate folder. The files are named after the tabs and the timestamp and they're all .txt regardless of the original file. The backups are not updated, every time you leave the app a completely new backup of the file is saved, allowing for version history. You may change the default backup state in settings or choose not to have this option at all.


Spell check: Tabs with this option on will be spell checked as the user types. The setting spell_check_typing_range controls the range of the spell checking, by default only the line which is being typed will be spell checked, the available options are 'full' for the entire doc, 'line' for only the line being typed or '2lines' for the current and previous lines compared to the cursor. Spell checking is available in the following languages: English, Spanish, French, Italian, Portuguese, German, Russian, Arabic, Latvian, Basque and Dutch. The setting use_typing_language_to_spell_check will make it so the language to spell check is the one being typed, if this is set to False then the languages listed in spell_check_languages will be used instead.


Metadata: Text documents don't have a simple way to store metadata. When this option is on metadata will be written to and read from the text file. This data contains the view info such as srcoll position, cursor position, selection range, zoom level, tab settings and the strikethrough ranges. In practice, when the app is reopened or if the file is opened from this app, it will look the same as when it was closed and allows for strikethrough to be possible.
Of course, because this metadata is written directly to the file, it will be visible when opened from any other application. Only this app will be able to interpert that information and remove it from the content, making it look like it wasn't there in the first place. If this is disabled every time the application is closed the view info of the tab and strikethrough will be lost, and it will have a different colour and default options. Metadata is written to the file everytime the file is saved or when one of the options button is clicked.


Autosave: Every 2 min (by default) every tab which already has a file and has this option turned on is saved automatically. If there's any problem with the pc or if you accidentally click 'Don't save' instead of losing all progress at most 2 minutes will be lost, just make sure to first 'Save as' newly created files (it will also be noticeable which tabs have been autosaved by the '*' after their names).


Secure: This option is  only available when the security folder is accessible. Secured tabs have slight changes throughout many features. The main idea is that these tabs have more sensitive content and should be saved more carefully and also be more discreet.
The differences from a normal tab are the following:

- Secure tabs should only be saved in the same drive as the security folder. If the drive is different you'll either be prompted to change the location or the file will not be saved until you do. You may; however choose to save it in a different drive, but it will not be accidental.

- Secure tabs are backed up to a separate folder (ideally in the encrypted drive).

- They will not be reopened when the tab starts, regardless of the status of reopen after exit.

- When using the Security Documents menu, the old file will be deleted, instead of just creating a new copy (and using this menu will turn on the secure mode, unless disabled in the settings).


Read-only: This option will disable editing in app and also change the file's attributes to become read-only. This will not work in PNG's (since they're not supposed to be written to in the first place) and it will not write metadata to the file. Clicking this option again will make the file writeable again, even if the file was not made read-only from this app. You cannot save read-only tabs




=== Shortcuts list ===
('/' stands for 'or' as in both shortcuts work)

Ctrl + H / F1 - Open help
Ctrl + Z - Undo
Ctrl + Y - Redo
Escape - Close the app / close a window / close a menu
Ctrl + P / F3 - Open settings
Ctrl + O - Open file
Ctrl + T - Create new tab
Ctrl + W - Close tab
Ctrl + Shift + W - Close all but current tab
Ctrl + Shift + T - Reopen last closed tab (this will open the file only, if the tab was unsaved the information is lost)
Alt + Shift + D - Duplicate tab
Ctrl + S - Save file
Ctrl + Alt + S - Save all files
Ctrl + Shift + S / F12 - Save file as
F5 - Refresh tabs
Ctrl + Tab - Switch to next tab
Ctrl + Shift + Tab - Switch to previous tab
Ctrl + Shift + F4 - Exit without saving
Ctrl + Plus - Zoom in
Ctrl + Minus - Zoom out
Ctrl + 0 - Reset zoom
Ctrl + M - Mount (security)
Ctrl + D - Dismount (security)
Ctrl + F - Open find and replace
Alt + Shift + S - Apply strikethrough
Insert - Toggle ovewrite/insert typing
F6 - Insert current date and time
F7 - Insert current date
F2 - Rename current tab (and file)
Ctrl + K + S - Rearrange rows
Ctrl + K + W - Rearrange rows window
Ctrl + K + M - Add indices to lines starting in 1
Ctrl + K + P - Add indices to lines starting in 0
Ctrl + K + N - Add indices to lines starting in a custom value
Ctrl + K + R - Remove indices
Ctrl + G - Go to line
Ctrl + Shift + R - Make file read-only (if possible)
F10 - Secure tab (if security is mounted)
Alt + A - Toggle tab's autosave
Alt + M  - Toggle tab's metadata
Alt + S - Toggle tab's spell cheking
Alt + B - Toggle tab's backup
F11 - Enter and exit fullscreen
Ctrl + B - Backup all tabs
Alt + F7 / F4 - Spell check everything
Ctrl + I - Show about




=== License ===

Yeongu Notes © 2024 by Nuno Seren is licensed under CC BY-NC-SA 4.0



==== Thank you ====

If you're reading this I already truly appreciate your interest! This was an interesting project for me and I hope this can be helpful to someone else.

This is my email if you need to reach out for any reason: namyeongmi3@gmail.com


Version 1.1.3
Updated 2024-06-22