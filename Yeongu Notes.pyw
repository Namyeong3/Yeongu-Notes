import tkinter as tk
import os 
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import Tk, Text
from tkinter import filedialog, ttk
import sys
import re
import shlex
import subprocess
from tkinter import Text, Tk, font
import toml
import tomli
import codecs
import pytoml
import random
import threading
import time
import datetime
from datetime import datetime
from tkinter import Tk, colorchooser
import customtkinter
import colorsys
from customtkinter import CTkButton
from datetime import datetime, timedelta
import json
from PIL import Image
import zlib
import textwrap
from PIL import Image, PngImagePlugin
from PIL.ExifTags import TAGS
import webcolors
import pyautogui
import ctypes as ct
import tempfile
import atexit
import chardet
import ast
import string
from spellchecker import SpellChecker
from typing import Literal
import queue
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)
os.environ['PYTHONIOENCODING'] = 'utf-8'

config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.toml")
config_default_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config_default.toml")
last_opened_files_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "last_opened_files.toml")
python_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Yeongu Notes.pyw")
exe_path = r"C:\Python Projects\Notetaking\Yeongu Notes\Yeongu Notes.exe"
help_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ReadMe.txt")
resources_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources')
images_folder = os.path.join(resources_folder, 'images')
ico_path = r"{}\ico\icons8-note-96.ico".format(images_folder)
TEMP_FILE_PATH = os.path.join(tempfile.gettempdir(), "communication_temp_file")
DELETE_TEMP_FILE = True

version = '1.1.3'

class Settings:
    def __init__(self, config_file):
        self.config_file = config_file
        self.load_settings()

    def load_settings(self):
        try:
            with open(self.config_file, "rb") as f:
                config = tomli.load(f)
                settings = config.get("settings", {})

                for key, value in settings.items():
                    # Check if the value is "True" or "False" and convert to boolean
                    if value == "True":
                        value = True
                    elif value == "False":
                        value = False
                    setattr(self, key, value)
        except FileNotFoundError:
            # Handle the case when the config file does not exist
            self.load_default_settings()

    def load_default_settings(self):
        try:
            with open(self.config_file, "rb") as f:
                config = tomli.load(f)
                default_settings = config.get("settings", {})

                for key, value in default_settings.items():
                    # Check if the value is "True" or "False" and convert to boolean
                    if value == "True":
                        value = True
                    elif value == "False":
                        value = False
                    setattr(self, key, value)
        except FileNotFoundError:
            # Handle the case when the config file does not exist
            print('Hum, this was the backup function... Check the config.toml and config_default.toml files')

    def save_settings(self):
        config = {"settings": {}}

        # Retrieve key order from the existing config file
        with codecs.open(config_path, 'r', encoding='utf-8') as f:
            existing_config = pytoml.load(f)
            keys_order = list(existing_config["settings"].keys())

        for key in keys_order:
            if hasattr(self, key):
                value = getattr(self, key)

                # Check if the value is numeric, and if so, convert it to an integer or float
                if isinstance(value, str) and value.isdigit():
                    value = int(value)
                elif isinstance(value, str):
                    if self.is_float(value):
                        value = float(value)
                if isinstance(value, bool):
                    value = str(value).capitalize()

                config["settings"][key] = value

        with codecs.open(config_path, 'w', encoding='utf-8') as f:  # Use the global config path
            pytoml.dump(config, f)

    def is_float(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

class ConfigtSettings:
    def __init__(self, config_file):
        self.config_file = config_file
        self.load_config_settings()

    def load_config_settings(self):
        try:
            with open(self.config_file, "rb") as f:
                config = tomli.load(f)
                settings = config.get("settings", {})

                for key, value in settings.items():
                    # Check if the value is "True" or "False" and convert to boolean
                    if value == "True":
                        value = True
                    elif value == "False":
                        value = False
                    setattr(self, key, value)
        except FileNotFoundError:
            # Handle the case when the config file does not exist
            self.load_default_settings()

    def load_default_settings(self):
        try:
            with open(self.config_file, "rb") as f:
                config = tomli.load(f)
                default_settings = config.get("settings", {})

                for key, value in default_settings.items():
                    # Check if the value is "True" or "False" and convert to boolean
                    if value == "True":
                        value = True
                    elif value == "False":
                        value = False
                    setattr(self, key, value)
        except FileNotFoundError:
            # Handle the case when the config file does not exist
            print('Hum, this was the backup function... Check the config.toml and config_default.toml files')

    def save_config_settings(self):
        config = {"settings": {}}

        # Retrieve key order from the existing config file
        with codecs.open(config_path, 'r', encoding='utf-8') as f:
            existing_config = pytoml.load(f)
            keys_order = list(existing_config["settings"].keys())

        for key in keys_order:
            if hasattr(self, key):
                value = getattr(self, key)

                # Check if the value is numeric, and if so, convert it to an integer or float
                if isinstance(value, str) and value.isdigit():
                    value = int(value)
                elif isinstance(value, str):
                    if self.is_float(value):
                        value = float(value)
                if isinstance(value, bool):
                    value = str(value).capitalize()

                config["settings"][key] = value

        with codecs.open(config_path, 'w', encoding='utf-8') as f:  # Use the global config path
            pytoml.dump(config, f)

    def is_float(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

settings = Settings(config_path)
config_settings = ConfigtSettings(config_path)


cmd_mount_drive = settings.cmd_mount_drive
cmd_mount_drive_success_pattern = settings.cmd_mount_drive_success_pattern
cmd_dismount_drive = settings.cmd_dismount_drive
cmd_test_mount_status = settings.cmd_test_mount_status
cmd_test_mount_status_success_pattern = settings.cmd_test_mount_status_success_pattern

class SettingsWindow:
    def __init__(self, master):
        self.master = master
        self.entry_values = {}

    def open_settings_window(self, main_app):
        settings_window = tk.Toplevel(self.master)
        settings_window.title("Yeongu Notes - Settings")
        settings_window.iconbitmap(ico_path)
        dark_title_bar(settings_window)
        settings_window.focus_force()


        top_frame = tk.Frame(settings_window, highlightthickness=0)
        top_frame.pack(side=tk.TOP, fill=tk.X, pady=(0, 10))

        # Create a label to display the pressed key
        key_label = tk.Label(top_frame, fg=settings.ui_fg, text="Pressed Key: ")
        key_label.pack()

        self.canvas = tk.Canvas(settings_window, highlightthickness=0)

        scrollbar = customtkinter.CTkScrollbar(settings_window, command=self.canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Add arrow key and mouse wheel bindings
        self.canvas.bind_all("<MouseWheel>", lambda e: self.canvas.yview_scroll(int(-1 * (e.delta / 120)), "units"))
        self.canvas.bind_all("<Up>", lambda e, canvas=self.canvas: canvas.yview_scroll(-1, "units"))
        self.canvas.bind_all("<Down>", lambda e, canvas=self.canvas: canvas.yview_scroll(1, "units"))
        settings_window.bind_all("<Escape>", lambda event: self.exit_settings_window(settings_window, self.canvas))
        #settings_window.bind(settings.open_config, lambda event: self.exit_settings_window(settings_window))
        # Bind protocol method to handle window closure
        settings_window.protocol("WM_DELETE_WINDOW", lambda: self.exit_settings_window(settings_window, self.canvas))

        self.frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame, anchor='nw')

        self.frame.bind("<ButtonPress-1>", self.start_scroll)
        self.frame.bind("<B1-Motion>", self.move_scroll)

        self.populate_settings(self.frame, settings_window)

        self.canvas.configure(yscrollcommand=scrollbar.set)
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        # Set the scroll position to the top
        scrollbar.set(0, 0)

        button_frame = tk.Frame(settings_window, highlightthickness=0)
        button_frame.pack(side=tk.TOP, fill=tk.X)

        spacer_label = tk.Label(button_frame, padx=30)
        spacer_label.pack(side=LEFT)

        default_settings_button = tk.Button(button_frame, fg=settings.ui_fg, text="Defaults", command=lambda main_app=main_app: self.load_default_settings(main_app))
        default_settings_button.pack(side=tk.LEFT, padx=4)

        restart_app_button = tk.Button(button_frame, fg=settings.ui_fg, text="Restart", command=lambda main_app=main_app: self.restart_program(main_app))
        restart_app_button.pack(side=tk.LEFT, padx=4)

        save_button = tk.Button(button_frame, fg=settings.ui_fg, text="Save", command=lambda main_app=main_app: self.save_settings(main_app))
        save_button.pack(side=tk.LEFT, padx=4)

        apply_button = tk.Button(button_frame, fg=settings.ui_fg, text="Apply", command=lambda main_app=main_app: self.apply_settings(main_app))
        apply_button.pack(side=tk.LEFT, padx=4)

        combined_button = tk.Button(button_frame, fg=settings.ui_fg, text="Apply, Save & Exit", command=lambda: self.apply_save_exit(settings_window, self.canvas, main_app))
        combined_button.pack(side=tk.LEFT, padx=4)


        settings_window.bind("<KeyPress>", lambda e: self.handle_key_press2(e, key_label))

        # Set the size of the window (replace the values with your desired width and height)
        width, height = 750, 800
        settings_window.geometry(f"{width}x{height}")

        # Center the window on the screen
        screen_width = settings_window.winfo_screenwidth()
        screen_height = settings_window.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        settings_window.geometry(f"+{x}+{y}")

    def populate_settings(self, frame, settings_window):
        global settings

        row = 1
        for key, value in settings.__dict__.items():
            if key.startswith("__") or callable(value):
                continue

            label = tk.Label(frame, text=key, fg=settings.ui_fg)
            label.grid(row=row, column=0)

            entry_value = tk.StringVar()
            entry = tk.Entry(frame, textvariable=entry_value, selectbackground=settings.selection_bg, selectforeground=settings.selection_fg, fg=settings.ui_fg)
            entry_value.set(str(value))
            entry.grid(row=row, column=1)

            if key.endswith("_path"):
                browse_button = tk.Button(frame, fg=settings.ui_fg, text="Browse", command=lambda k=key, v=entry_value: self.browse_path(k, v, settings_window))
                browse_button.grid(row=row, column=2)

            # Check for color options and add a button to pick a color
            if ('color' in key.lower() or 'colour' in key.lower() or key.endswith('_bg') or key.endswith('_fg')) and type(value) not in [bool, 'bool']:
                color_button = tk.Button(frame, fg=settings.ui_fg, text="Pick Colour", command=lambda k=key, v=entry_value: self.pick_color(k, v, settings_window))
                color_button.grid(row=row, column=2)

            if type(value) == bool or str(value).lower() == 'true' or str(value).lower() == 'false':
                toggle_button = tk.Button(frame, fg=settings.ui_fg, text="Toggle", command=lambda k=key, v=entry_value: self.toggle_boolean(k, v))
                toggle_button.grid(row=row, column=2)

            self.entry_values[key] = entry_value
            row += 1

    def start_scroll(self, event):
        self.canvas.scan_mark(0, event.y)

    def move_scroll(self, event):
        self.canvas.scan_dragto(0, event.y, gain=1)

    def handle_key_press2(self, event, key_label):
        pressed_key = event.keysym
        if pressed_key.startswith("Shift"):
            pressed_key = "*"
        key_label.config(text=f"Pressed Key: {pressed_key}")

    def toggle_boolean(self, key, entry_var):
        current_value = entry_var.get()
        new_value = not bool(current_value.lower() == 'true')
        entry_var.set(str(new_value))

    def apply_save_exit(self, window, canvas, main_app):
        self.apply_settings(main_app)
        self.save_settings(main_app)
        self.exit_settings_window(window,canvas)

    def browse_path(self, key, entry_var, settings_window):
        folder_selected = filedialog.askdirectory(title=f"Select {key}")
        if folder_selected:
            entry_var.set(folder_selected)
        settings_window.focus_set()

    # Add a new method to handle picking colors
    def pick_color(self, key, entry_var, settings_window):
        color = self.prompt_colour(f"Select color for {key}", "Color Picker")
        if color:
            entry_var.set(color)
        settings_window.focus_set()

    def prompt_colour(self, message, title):
        prompt_root = Tk()
        prompt_root.withdraw()
        prompt_root.iconbitmap(bitmap=ico_path)
        color = colorchooser.askcolor(title=title)[1]
        prompt_root.destroy()
        return color

    def save_settings(self, main_app):
        settings_to_save = settings
        for key, entry_var in self.entry_values.items():
            value = entry_var.get()

            # Check if the value is numeric, and if so, convert it to an integer or float
            if value.isdigit():
                value = int(value)
            elif self.is_float(value):
                value = float(value)

            setattr(settings_to_save, key, value)

        with codecs.open(config_path, 'w', encoding='utf-8') as f:  # Specify 'utf-8' encoding
            # Add the [settings] section at the beginning of the file
            f.write("[settings]\n")

            # Use the pytoml library to save settings, excluding the __module__ attribute
            settings_to_save_dict = settings_to_save.__dict__
            settings_to_save_dict.pop('__module__', None)
            pytoml.dump(settings_to_save_dict, f)

    def apply_settings(self, main_app):
        for key, entry_var in self.entry_values.items():
            value = entry_var.get()

            # Check if the value is numeric, and if so, convert it to an integer or float
            if value.isdigit():
                value = int(value)
            elif self.is_float(value):
                value = float(value)
            elif value.lower() == 'true':
                value = True
            elif value.lower() == 'false':
                value = False

            # Update the corresponding attribute in the settings instance directly
            settings.__dict__[key] = value

        main_app.tab_controller.refresh_tabs()

    def load_default_settings(self, main_app):
        default_settings = Settings(config_default_path)
        
        for key, entry_var in self.entry_values.items():
            value = getattr(default_settings, key)
            
            # Update the corresponding entry value in the settings window
            entry_var.set(str(value))

    def is_float(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False
        
    def exit_settings_window(self, settings_window, canvas):
        if settings_window:
            # Unbind all keys and destroy the settings window
            canvas.unbind_all("<MouseWheel>")
            canvas.unbind_all("<Up>")
            canvas.unbind_all("<Down>")

            # Unbind scroll-related events from the scrollbar
            scrollbar = next((child for child in settings_window.winfo_children() if isinstance(child, customtkinter.CTkScrollbar)), None)
            if scrollbar:
                scrollbar.unbind("<MouseWheel>")

            settings_window.unbind_all("<Escape>")  # Unbind the Escape key
            settings_window.destroy()
            settings_window = None  # Reset the reference

    def restart_program(self, main_app):
        main_app.save_and_exit()
        try:
            os.startfile(exe_path)
        except Exception as e:
            print("Error:", e)

def dark_title_bar(root):
    """
    MORE INFO:
    https://learn.microsoft.com/en-us/windows/win32/api/dwmapi/ne-dwmapi-dwmwindowattribute
    """
    root.update()
    DWMWA_USE_IMMERSIVE_DARK_MODE = 20
    set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
    get_parent = ct.windll.user32.GetParent
    hwnd = get_parent(root.winfo_id())
    rendering_policy = DWMWA_USE_IMMERSIVE_DARK_MODE
    value = 2
    value = ct.c_int(value)
    set_window_attribute(hwnd, rendering_policy, ct.byref(value),
                        ct.sizeof(value))

class Tab:
    def __init__(self, notebook, notepad, tab_colour, tab_foreground_colour, wrap=settings.wrap, save_metadata=settings.default_metadata, reorderable_data={}, secured=False, autosave=settings.default_autosave, file=None, backup=settings.default_backup, png_json=False, spell=settings.default_spell_check, **kwargs):
        self.notepad = notepad
        self.notebook = notebook
        self.tab_controller = notepad.tab_controller
        self.file = file
        self.last_saved_file = file
        self.memento_stack = []
        self.redo_stack = []
        self.autosave = autosave
        self.zoom_factor = 1.0
        self.submenus = []
        self.is_cursor_on_outer_frame = False
        self.is_cursor_on_outer_frame = False
        self.safe_to_save = False
        self.metadata_handler = TextMetadataHandler(self.notepad)
        self.save_metadata = save_metadata
        self.backup = backup
        self.wrap = wrap
        self.secured = secured
        self.labels_on_queue = 0
        self.reorderable = reorderable_data != {}
        self.stop_regression = False
        self.last_saved_file_using_save_path = None
        self.duplicated = False
        self.font = None
        self.png_json = png_json
        self.png_var_no = 0
        self.spell = spell
        if self.reorderable:
            self.items_to_display, self.saved_text, self.saved_strikethrough_ranges, self.reorderable_start_index = reorderable_data
            self.reordered_text = self.saved_text
            self.reordered_strikethrough_ranges = self.saved_strikethrough_ranges
        else:
            self.reordered_text = None
            self.reordered_strikethrough_ranges = None

        if self.file:
            if os.path.exists(self.file):
                if not os.access(self.file, os.W_OK):
                    self.read_only = True
                else:
                    self.read_only = False
            else:
                self.read_only = False
        else:
            self.read_only = False

        self.view_info = {}

        self.tab_info = f"{datetime.now().strftime('%H:%M')}  {self.notepad.korean_date}"

        #Colours
        self.colour = tab_colour

        #If there's both read only and self.reorderable, make it only read only
        if self.reorderable and self.read_only:
            self.reorderable = False

        # Set other attributes dynamically
        for key, value in kwargs.items():
            #print(key, value)
            setattr(self, key, value)

        self.foreground_colour = tab_foreground_colour
        self.subcolour = self.calculate_subcolour()
        self.foreground_subcolour = "#ffffff" if self.calculate_brightness(self.subcolour) < 128 else "#000000"

        if settings.use_tab_colours:
            self.selection_bg = self.colour if self.calculate_brightness(self.colour) < self.calculate_brightness(self.subcolour) else self.subcolour
            self.selection_fg = self.foreground_colour if self.calculate_brightness(self.foreground_colour) > self.calculate_brightness(self.foreground_subcolour) else self.foreground_subcolour
            self.cursor_colour = self.colour if self.calculate_brightness(self.colour) > self.calculate_brightness(self.subcolour) else self.subcolour
        else:
            self.selection_bg = settings.selection_bg
            self.selection_fg = settings.selection_fg
            self.cursor_colour = settings.cursor_colour

        if self.read_only:
            self.create_top_bar_read_only()
        elif not self.reorderable:
            self.create_top_bar()
        else:
            self.create_top_bar_reorderable()
    
    def calculate_subcolour(self, light_factor=1.5, dark_factor=0.5):
        factor = dark_factor if self.foreground_colour == "#000000" else light_factor
        h, l, s = colorsys.rgb_to_hls(*(int(self.colour[i:i+2], 16) / 255.0 for i in (1, 3, 5)))
        l *= factor
        l = max(0, min(1, l))
        return "#{:02x}{:02x}{:02x}".format(*(round(val * 255) for val in colorsys.hls_to_rgb(h, l, s)))

    def calculate_brightness(self, hex_color):
        r, g, b = int(hex_color[1:3], 16), int(hex_color[3:5], 16), int(hex_color[5:], 16)
        return (r * 299 + g * 587 + b * 114) / 1000

    def create_top_bar(self):
        # Top bar components for each tab
        self.root = Frame(self.notebook, highlightthickness=0)
        self.top_bar = Frame(self.root, bg=settings.ui_bg, height=40, borderwidth=0, highlightthickness=0)
        self.content_area = Frame(self.root, bg=settings.text_bg, borderwidth=0, highlightthickness=0)
        self.text_area = Text(self.content_area, bg=settings.text_bg, fg=settings.text_fg, bd=0, highlightthickness=0, autoseparators=True, insertbackground=self.cursor_colour, exportselection=False, font=(settings.text_font, settings.font_size), wrap='word' if self.wrap else 'none')

        # Set icon for the top bar
        try:
            self.icon_spacer_label = tk.Label(self.top_bar, padx=16, bg=settings.ui_bg)
            self.icon_spacer_label.pack(side=LEFT)

            self.icon_button = CustomShortcutButton(self.top_bar, label1=None, label2=None, active_bg=self.colour, active_fg=self.foreground_colour, active_fg2=self.foreground_colour, command=lambda: self.display_time(fg=self.colour), img_path=r"{}\\Simple app icons\\icons8-note-24-border.png".format(images_folder))
            self.icon_button.place(x=0, y=0)

            self.create_buttons()

            if self.file == '' or not self.file or os.path.splitext(self.file)[1].lower() not in ['.png']:
                self.read_only_button = CustomShortcutButton(self.top_bar, label1=None, label2=None, active_bg=self.colour, active_fg=self.foreground_colour, active_fg2=self.foreground_colour, command=lambda: self.toggle_read_only(), img_toggle=[r"{}\writable.png".format(images_folder), r"{}\read_only.png".format(images_folder), self.read_only], info='Make the file read-only (Ctrl + Shift + R)', hover_bg='#9a9a9a')
                self.read_only_button.pack(side=RIGHT, padx=25)

            if self.notepad.is_mounted or self.secured:
                self.secured_button = CustomShortcutButton(self.top_bar, label1=None, label2=None, active_bg=self.colour, active_fg=self.foreground_colour, active_fg2=self.foreground_colour, command=lambda: self.toggle_secured(), img_toggle=[r"{}\secure.png".format(images_folder), r"{}\insecure.png".format(images_folder), self.secured], info='Secure this tab (F10)', hover_bg='#9a9a9a')
                self.secured_button.pack(side=RIGHT, padx=25)
  
            self.autosave_button = CustomShortcutButton(self.top_bar, label1=None, label2=None, active_bg=self.colour, active_fg=self.foreground_colour, active_fg2=self.foreground_colour, command=lambda: self.toggle_autosave(), img_toggle=[r"{}\autosave_on.png".format(images_folder), r"{}\autosave_off.png".format(images_folder), self.autosave], info=f'Save the files every {settings.autosave_interval_sec} seconds (Alt + A)', hover_bg='#9a9a9a')
            self.autosave_button.pack(side=RIGHT, padx=25)

            if self.file == '' or not self.file or os.path.splitext(self.file)[1].lower() in ['.txt']:
                self.rich_text_button = CustomShortcutButton(self.top_bar, label1=None, label2=None, active_bg=self.colour, active_fg=self.foreground_colour, active_fg2=self.foreground_colour, command=lambda: self.toggle_metadata(), img_toggle=[r"{}\metadata.png".format(images_folder), r"{}\metadata_off.png".format(images_folder), self.save_metadata], info='Save metadata to the file (Alt + M)', hover_bg='#9a9a9a')
                self.rich_text_button.pack(side=RIGHT, padx=25)

            if settings.use_spell_checking:
                self.spell_button = CustomShortcutButton(self.top_bar, label1=None, label2=None, active_bg=self.colour, active_fg=self.foreground_colour, active_fg2=self.foreground_colour, command=lambda: self.toggle_spell(), img_toggle=[r"{}\spell_check_on.png".format(images_folder), r"{}\spell_check_off.png".format(images_folder), self.spell], info="Use spell checking on this tab (Alt + S)", hover_bg='#9a9a9a')
                self.spell_button.pack(side=RIGHT, padx=25)

            if settings.use_file_backup:
                self.backup_button = CustomShortcutButton(self.top_bar, label1=None, label2=None, active_bg=self.colour, active_fg=self.foreground_colour, active_fg2=self.foreground_colour, command=lambda: self.toggle_backup(), img_toggle=[r"{}\backup_on.png".format(images_folder), r"{}\backup_off.png".format(images_folder), self.backup], info="Backup this tab's content whenever the app is exited (Alt + B)", hover_bg='#9a9a9a')
                self.backup_button.pack(side=RIGHT, padx=25)

            if self.file and os.path.splitext(self.file)[1].lower() in ['.png']:
                self.convert_json_button = CustomShortcutButton(self.top_bar, label1=None, label2=None, active_bg=self.colour, active_fg=self.foreground_colour, active_fg2=self.foreground_colour, command=lambda: self.toggle_covert_json(), img_toggle=[r"{}\convert_to_json.png".format(images_folder), r"{}\convert_from_json.png".format(images_folder), self.png_json], info="Convert the metadata to and from json", hover_bg='#9a9a9a')
                self.convert_json_button.pack(side=RIGHT, padx=25)

        except Exception as e:
            print(f"Error setting top bar icon: {e}")
            self.notepad.display_all(f"Error setting top bar icon: {e}")

        # Place the top bar at the top of the window
        self.top_bar.pack(side=TOP, fill=X, padx=0, pady=0)
        self.content_area.pack(side=TOP, fill=BOTH, padx=0, pady=0, expand=YES)
        
        self.text_area.bind("<Key>", self.notepad.handle_key_event)
        self.text_area.bind("<Control-v>", lambda event: self.notepad.handle_key_event(event=None, cut_paste=True))
        self.text_area.bind("<Control-V>", lambda event: self.notepad.handle_key_event(event=None, cut_paste=True))
        self.text_area.bind("<Control-x>", lambda event: self.notepad.handle_key_event(event=None, cut_paste=True))
        self.text_area.bind("<Control-X>", lambda event: self.notepad.handle_key_event(event=None, cut_paste=True))
        self.text_area.bind('<KeyRelease>', self.notepad.update_character_and_cursor_labels)
        self.text_area.bind('<ButtonRelease-1>', self.notepad.update_character_and_cursor_labels)
        self.text_area.bind('<Motion>', self.notepad.update_character_and_cursor_labels)
        self.text_area.bind("<Control-o>", self.notepad.open_and_break)
        self.text_area.bind('<Control-t>', self.notepad.create_and_break)
        self.text_area.bind('<Control-i>', self.notepad.show_about)
        self.text_area.bind("<Control-h>", lambda event: self.notepad.open_and_break(path=help_path))
        self.text_area.bind("<F1>", lambda event: self.notepad.open_and_break(path=help_path))
        self.text_area.bind('<Control-d>', lambda event: self.notepad.close_security_folder())
        self.text_area.bind('<Control-k>', self.return_break)
        self.text_area.bind("<B1-Motion>", self.handle_mouse_motion)


        #Because of case sensitive bindings
        self.text_area.bind("<Control-O>", self.notepad.open_and_break)
        self.text_area.bind('<Control-T>', self.notepad.create_and_break)
        self.text_area.bind('<Control-I>', self.notepad.show_about)
        self.text_area.bind("<Control-H>", lambda event: self.notepad.open_and_break(path=help_path))
        self.text_area.bind('<Control-D>', lambda event: self.notepad.close_security_folder())
        self.text_area.bind('<Control-K>', self.return_break)

        #self.text_area.tag_configure("sel", background=self.selection_bg, foreground=self.selection_fg)
        self.text_area.tag_configure("sel", background=self.selection_bg, foreground=self.selection_fg)
        self.text_area.tag_configure("strikethrough", overstrike=True)
        self.text_area.tag_configure("sub_highlight", background=self.subcolour, foreground=self.foreground_subcolour)
        self.text_area.tag_configure("highlight", background=self.colour, foreground=self.foreground_colour)
        self.text_area.tag_configure("misspelled", underline=True, underlinefg=settings.spell_check_colour)

        self.animation_bar = tk.Frame(self.content_area, bg=settings.ui_bg, height=3, borderwidth=0, highlightthickness=0, highlightbackground='black')
        self.animation_bar.pack(fill=X, pady=0)

        self.loading_bar = tk.PhotoImage(file=r"{}\loadingbar_long_sk.png".format(images_folder))  # Replace with your image path
        self.loading_bar_label = tk.Label(self.animation_bar, image=self.loading_bar, bg=settings.ui_bg)

        self.ctk_textbox_scrollbar = customtkinter.CTkScrollbar(self.content_area, command=self.text_area.yview, button_color='#757575' if settings.use_tab_colours else None, button_hover_color=self.colour if settings.use_tab_colours else None)

        # Add lines_label as text item inside the Canvas
        self.lines_label = tk.Label(self.content_area, padx=8 if settings.text_gaps else 0, bg=settings.text_bg, pady=0)
        self.lines_label.pack(side=LEFT, fill=Y)
        self.lines_label.bind("<Button-1>", self.on_lines_label_click)
        self.lines_label.bind("<B1-Motion>", self.on_lines_label_drag)
        self.lines_label.bind("<ButtonRelease-1>", self.on_lines_label_drag_release)


        self.notepad.root.focus_set()

        self.ctk_textbox_scrollbar.pack(side=RIGHT, fill=Y)

        self.toggle_scrollbar_visibility()
        
        if not self.wrap:
            self.ctk_x_textbox_scrollbar = customtkinter.CTkScrollbar(self.content_area, command=self.text_area.xview, orientation="horizontal", button_color='#757575' if settings.use_tab_colours else None, button_hover_color=self.colour if settings.use_tab_colours else None)
            self.ctk_x_textbox_scrollbar.pack(side=BOTTOM, fill=X)
            self.toggle_x_scrollbar_visibility()

        self.text_area.configure(yscrollcommand=self.ctk_textbox_scrollbar.set)
        if not self.wrap:
            self.text_area.configure(xscrollcommand=self.ctk_x_textbox_scrollbar.set)

        self.text_area.pack(expand=YES, fill=BOTH)

        spacer_label = tk.Label(self.top_bar, padx=39, bg=settings.ui_bg)
        spacer_label.pack(side=RIGHT)

        self.info_label = Label(self.top_bar, text=self.tab_info, fg=settings.ui_fg, bg=settings.ui_bg, font=(settings.regular_font, settings.font_size))
        self.info_label.pack(side=RIGHT, padx=26)
        self.display_time()

    def create_top_bar_read_only(self):
        # Top bar components for each tab
        self.root = Frame(self.notebook, highlightthickness=0)
        self.top_bar = Frame(self.root, bg=settings.ui_bg, height=40, borderwidth=0, highlightthickness=0, highlightbackground='black')
        self.content_area = Frame(self.root, bg=settings.text_bg, borderwidth=0, highlightthickness=0)
        self.text_area = Text(self.content_area, bg=settings.text_bg, fg=settings.text_fg, bd=0, highlightthickness=0, autoseparators=True, insertbackground=self.cursor_colour, exportselection=False, wrap='word' if self.wrap else 'none')

        bindtags = list(self.text_area.bindtags())
        bindtags.remove("Text")
        self.text_area.bindtags(tuple(bindtags))

        # Set icon for the top bar
        try:
            self.icon_spacer_label = tk.Label(self.top_bar, padx=16, bg=settings.ui_bg)
            self.icon_spacer_label.pack(side=LEFT)

            self.icon_button = CustomShortcutButton(self.top_bar, label1=None, label2=None, active_bg=self.colour, active_fg=self.foreground_colour, active_fg2=self.foreground_colour, command=lambda: self.display_time(fg=self.colour), img_path="{}\\Simple app icons\\icons8-note-24-border.png".format(images_folder))
            self.icon_button.place(x=0, y=0)

            self.create_buttons_read_only()

            self.read_only_button = CustomShortcutButton(self.top_bar, label1=None, label2=None, active_bg=self.colour, active_fg=self.foreground_colour, active_fg2=self.foreground_colour, command=lambda: self.toggle_read_only(), img_toggle=[r"{}\writable.png".format(images_folder), r"{}\read_only.png".format(images_folder), self.read_only], info='Make the file read-only (Ctrl + Shift + R)', hover_bg='#9a9a9a')
            self.read_only_button.pack(side=RIGHT, padx=25)

            if self.notepad.is_mounted or self.secured:
                self.secured_button = CustomShortcutButton(self.top_bar, label1=None, label2=None, active_bg=self.colour, active_fg=self.foreground_colour, active_fg2=self.foreground_colour, command=lambda: self.toggle_secured(), img_toggle=[r"{}\secure.png".format(images_folder), r"{}\insecure.png".format(images_folder), self.secured], info='Secure this tab (F10)', hover_bg='#9a9a9a')
                self.secured_button.pack(side=RIGHT, padx=25)

        except Exception as e:
            self.notepad.display_all(f"Error setting top bar icon: {e}")

        # Place the top bar at the top of the window
        self.top_bar.pack(side=TOP, fill=X, padx=0, pady=0)
        self.content_area.pack(side=TOP, fill=BOTH, padx=0, pady=0, expand=YES)

        self.text_area.bind("<MouseWheel>", self.mouse_wheel)
        self.text_area.bind("<Control-o>", self.notepad.open_and_break)
        self.text_area.bind('<Control-t>', self.notepad.create_and_break)
        self.text_area.bind('<Control-i>', self.notepad.show_about)
        self.text_area.bind("<Control-h>", lambda event: self.notepad.open_and_break(path=help_path))
        self.text_area.bind("<F1>", lambda event: self.notepad.open_and_break(path=help_path))
        self.text_area.bind('<Control-d>', lambda event: self.notepad.close_security_folder())
        self.text_area.bind('<Escape>', lambda event: self.notepad.save_and_exit())

        # Note: These key bindings are specified for the opposite case due to the case sensitive nature of Tkinter bindings
        self.text_area.bind("<Control-O>", self.notepad.open_and_break)
        self.text_area.bind('<Control-T>', self.notepad.create_and_break)
        self.text_area.bind('<Control-I>', self.notepad.show_about)
        self.text_area.bind("<Control-H>", lambda event: self.notepad.open_and_break(path=help_path))
        self.text_area.bind('<Control-D>', lambda event: self.notepad.close_security_folder())

        #self.text_area.tag_configure("sel", background=self.selection_bg, foreground=self.selection_fg)
        self.text_area.tag_configure("sel", background=self.selection_bg, foreground=self.selection_fg)
        self.text_area.tag_configure("strikethrough", overstrike=True)
        self.text_area.tag_configure("sub_highlight", background=self.subcolour, foreground=self.foreground_subcolour)
        self.text_area.tag_configure("highlight", background=self.colour, foreground=self.foreground_colour)
        self.text_area.tag_configure("misspelled", underline=True, underlinefg=settings.spell_check_colour)

        self.animation_bar = tk.Frame(self.content_area, bg=settings.ui_bg, height=3, borderwidth=0, highlightthickness=0, highlightbackground='black')
        self.animation_bar.pack(fill=X, pady=0)

        self.loading_bar = tk.PhotoImage(file=r"{}\loadingbar_long_sk.png".format(images_folder))  # Replace with your image path
        self.loading_bar_label = tk.Label(self.animation_bar, image=self.loading_bar, bg=settings.ui_bg)

        # Set the font size
        text_font = font.Font(font=(settings.text_font, settings.font_size))  # Adjust the family and size as needed
        self.text_area.configure(font=text_font)

        self.ctk_textbox_scrollbar = customtkinter.CTkScrollbar(self.content_area, command=self.text_area.yview, button_color='#757575' if settings.use_tab_colours else None, button_hover_color=self.colour if settings.use_tab_colours else None)

        # Add lines_label as text item inside the Canvas
        self.lines_label = tk.Label(self.content_area, padx=8 if settings.text_gaps else 0, bg=settings.text_bg, pady=0)
        self.lines_label.pack(side=LEFT, fill=Y)

        self.ctk_textbox_scrollbar.pack(side=RIGHT, fill=Y)
        self.toggle_scrollbar_visibility()
        
        if not self.wrap:
            self.ctk_x_textbox_scrollbar = customtkinter.CTkScrollbar(self.root, command=self.text_area.xview, orientation="horizontal", button_color='#757575' if settings.use_tab_colours else None, button_hover_color=self.colour if settings.use_tab_colours else None)
            self.ctk_x_textbox_scrollbar.pack(side=BOTTOM, fill=X)
            self.toggle_x_scrollbar_visibility()

        self.text_area.configure(yscrollcommand=self.ctk_textbox_scrollbar.set)
        if not self.wrap:
            self.text_area.configure(xscrollcommand=self.ctk_x_textbox_scrollbar.set)

        # Add controls (widget) with conditional scrollbar
        self.text_area.pack(expand=YES, fill=BOTH)

        spacer_label = tk.Label(self.top_bar, padx=113, bg=settings.ui_bg)
        spacer_label.pack(side=RIGHT)

        self.info_label = Label(self.top_bar, text=self.tab_info, fg=settings.ui_fg, bg=settings.ui_bg, font=(settings.regular_font, settings.font_size))
        self.info_label.pack(side=RIGHT, padx=26)
        self.display_time()

    def create_top_bar_reorderable(self):
        # Top bar components for each tab
        self.root = Frame(self.notebook, highlightthickness=0)
        self.top_bar = Frame(self.root, bg=settings.ui_bg, height=40, borderwidth=0, highlightthickness=0, highlightbackground='black')
        self.content_area = Frame(self.root, bg=settings.text_bg, borderwidth=0, highlightthickness=0)

        self.text_area = ReorderableListWidget(self.content_area, self.items_to_display, tab=self, selection_index=self.reorderable_start_index)

        # Set icon for the top bar
        try:
            self.icon_spacer_label = tk.Label(self.top_bar, padx=16, pady=4, bg=settings.ui_bg)
            self.icon_spacer_label.pack(side=LEFT)

            self.icon_button = CustomShortcutButton(self.top_bar, label1=None, label2=None, active_bg=self.colour, active_fg=self.foreground_colour, active_fg2=self.foreground_colour, command=lambda: self.display_time(fg=self.colour), img_path="{}\\Simple app icons\\icons8-note-24-border.png".format(images_folder))
            self.icon_button.place(x=0, y=0)

        except Exception as e:
            self.display(f"Error setting top bar icon: {e}")

        # Place the top bar at the top of the window
        self.top_bar.pack(side=TOP, fill=X, padx=0, pady=0)
        self.content_area.pack(side=TOP, fill=BOTH, padx=0, pady=0, expand=YES)

        self.done_button = CustomShortcutButton(self.top_bar, label1='Done', label2=None, active_bg='#006b07', active_fg=settings.ui_fg, hover_bg='green', hover_fg=settings.ui_fg, active_fg2=self.foreground_colour, command=self.text_area.apply_changes)
        self.done_button.pack(side=LEFT, padx=0)

        self.cancel_button = CustomShortcutButton(self.top_bar, label1='Cancel', label2=None, active_bg='#6b0000', active_fg=settings.ui_fg, hover_bg='red', hover_fg=settings.ui_fg,active_fg2=self.foreground_colour, command=self.text_area.cancel_changes)
        self.cancel_button.pack(side=LEFT, padx=0)

        self.text_area.bind("<Control-o>", self.notepad.open_and_break)
        self.text_area.bind('<Control-t>', self.notepad.create_and_break)
        self.text_area.bind('<Control-i>', self.notepad.show_about)
        self.text_area.bind("<Control-h>", lambda event: self.notepad.open_and_break(path=help_path))
        self.text_area.bind("<F1>", lambda event: self.notepad.open_and_break(path=help_path))
        self.text_area.bind('<Control-d>', lambda event: self.notepad.close_security_folder())
        self.text_area.bind('<Control-k>', self.return_break)

        # Note: These key bindings are specified for the opposite case due to the case sensitive nature of Tkinter bindings
        self.text_area.bind("<Control-O>", self.notepad.open_and_break)
        self.text_area.bind('<Control-T>', self.notepad.create_and_break)
        self.text_area.bind('<Control-I>', self.notepad.show_about)
        self.text_area.bind("<Control-H>", lambda event: self.notepad.open_and_break(path=help_path))
        self.text_area.bind('<Control-D>', lambda event: self.notepad.close_security_folder())
        self.text_area.bind('<Control-K>', self.return_break)

        self.animation_bar = tk.Frame(self.content_area, bg=settings.ui_bg, height=3, borderwidth=0, highlightthickness=0, highlightbackground='black')
        self.animation_bar.pack(fill=X, pady=0)

        self.loading_bar = tk.PhotoImage(file=r"{}\loadingbar_long_sk.png".format(images_folder))  # Replace with your image path
        self.loading_bar_label = tk.Label(self.animation_bar, image=self.loading_bar, bg=settings.ui_bg)

        self.ctk_textbox_scrollbar = customtkinter.CTkScrollbar(self.content_area, command=self.text_area.treeview.yview, button_color='#757575' if settings.use_tab_colours else None, button_hover_color=self.colour if settings.use_tab_colours else None)
        self.ctk_textbox_scrollbar.pack(side=RIGHT, fill=Y)
        self.toggle_scrollbar_visibility(enable=True)

        self.lines_label = tk.Label(self.content_area, padx=8 if settings.text_gaps else 0, bg=settings.text_bg, pady=0)
        self.lines_label.pack(side=LEFT, fill=Y)

        self.text_area.treeview.configure(yscrollcommand=self.ctk_textbox_scrollbar.set)

        # Add controls (widget) with conditional scrollbar
        self.text_area.pack(expand=YES, fill=BOTH)

        spacer_label = tk.Label(self.top_bar, padx=185, bg=settings.ui_bg)
        spacer_label.pack(side=RIGHT)

        self.info_label = Label(self.top_bar, text=self.tab_info, fg=settings.ui_fg, bg=settings.ui_bg, font=(settings.regular_font, settings.font_size))
        self.info_label.pack(side=RIGHT, padx=26)
        self.display_time()

    def return_break(self, event=None):
        return 'break'

    def toggle_scrollbar_visibility(self, enable=None):
        if enable is not None:
            # If enable argument is provided, set the scrollbar state accordingly
            if enable:
                self.ctk_textbox_scrollbar.configure(width=15)  # Adjust the width as needed
                if not self.reorderable:
                    self.text_area.configure(yscrollcommand=self.ctk_textbox_scrollbar.set)
                else:
                    self.text_area.treeview.configure(yscrollcommand=self.ctk_textbox_scrollbar.set)
            else:
                self.ctk_textbox_scrollbar.configure(width=0)
        else:
            # If enable argument is not provided, toggle the scrollbar state
            current_width = self.ctk_textbox_scrollbar.cget("width")
            if current_width == 0:
                self.ctk_textbox_scrollbar.configure(width=15)  # Adjust the width as needed
                if not self.reorderable:
                    self.text_area.configure(yscrollcommand=self.ctk_textbox_scrollbar.set)
                else:
                    self.text_area.treeview.configure(yscrollcommand=self.ctk_textbox_scrollbar.set)
            else:
                self.ctk_textbox_scrollbar.configure(width=0)

    def toggle_x_scrollbar_visibility(self, enable=None):
        if not self.wrap:
            if enable is not None:
                if enable:
                    self.ctk_x_textbox_scrollbar.configure(height=15)
                    self.text_area.configure(xscrollcommand=self.ctk_x_textbox_scrollbar.set)
                else:
                    self.ctk_x_textbox_scrollbar.configure(height=0)
            else:
                current_height = self.ctk_x_textbox_scrollbar.cget("height")
                if current_height == 0:
                    self.ctk_x_textbox_scrollbar.configure(height=15)
                    self.text_area.configure(xscrollcommand=self.ctk_x_textbox_scrollbar.set)
                else:
                    self.ctk_x_textbox_scrollbar.configure(height=0)

    def mouse_wheel(self, event):
        scroll_pixels = event.delta * -0.5

        if event.state == 9 and not self.wrap:
            self.text_area.xview("scroll", scroll_pixels, "pixels")
        else:
            self.text_area.yview("scroll", scroll_pixels, "pixels")

    def toggle_loading_animation(self, refresh_at_the_end=True, start_x=-1924, turn_off=False):
        self.notepad.refresh_after_loading = refresh_at_the_end
        self.notepad.is_mounted_at_loading_start = self.notepad.is_mounted

        if not self.notepad.is_animation_running:
            self.loading_bar_label.place(x=start_x, y=-2)
            self.root.after(50, self.move_image)
            self.notepad.is_animation_running = True
            self.notepad.stop_animation_quick = False
        else:
            self.notepad.is_animation_running = False
            if turn_off:
                self.notepad.stop_animation_quick = True

    def move_image(self):
        current_x = self.loading_bar_label.winfo_x()
        if current_x < self.root.winfo_width():
            self.loading_bar_label.place(x=current_x + 5, y=-2)
            if self.notepad.stop_animation_quick:
                self.notepad.is_animation_running = False
                self.loading_bar_label.place(x=-self.loading_bar_label.winfo_width(), y=-2)
                return
            self.root.after(4, self.move_image)
        elif self.notepad.is_animation_running:
            self.loading_bar_label.place(x=-self.loading_bar_label.winfo_width(), y=-2)
            self.root.after(4, self.move_image)
        else:
            self.notepad.is_animation_running = False
            if self.notepad.refresh_after_loading:
                if self.notepad.is_mounted_at_loading_start != self.notepad.is_mounted:
                    self.notepad.refresh_tabs()

    def handle_mouse_motion(self, event):
        # Check if text is selected
        if self.text_area.tag_ranges("sel"):
            # Get the mouse position
            x = event.x
            y = event.y
            # Get the size of the text area
            width = self.text_area.winfo_width()
            height = self.text_area.winfo_height()
            # Define the threshold for scrolling (e.g., 20 pixels from the edges)
            threshold = 20

            if not self.wrap:
                # Check if the mouse is near the left edge
                if x < threshold:
                    # Scroll left
                    self.text_area.xview_scroll(-1, "units")
                # Check if the mouse is near the right edge
                elif x > width - threshold:
                    # Scroll right
                    self.text_area.xview_scroll(1, "units")

            # Check if the mouse is near the top edge
            if y < threshold:
                # Scroll up
                self.text_area.yview_scroll(-1, "units")
            # Check if the mouse is near the bottom edge
            elif y > height - threshold:
                # Scroll down
                self.text_area.yview_scroll(1, "units")

    def create_buttons_read_only(self):
        settings_window_instance = SettingsWindow(self.root)
        # Create buttons instead of menu items
        file_buttons = {
            "Open, shortcut=Ctrl + O": self.notepad.open_file,
            "Save as, shortcut=F12": self.notepad.save_file_as,
            "Save all, shortcut=Ctrl + Alt + S": self.notepad.save_all_files,
            "Backup all, shortcut=Ctrl + B, info=Backup now all backup enabled tabs": self.notepad.backup_all_files if settings.use_file_backup else None,
            "Exit, shortcut=Esc": self.notepad.save_and_exit,
        }

        file_buttons = {key: value for key, value in file_buttons.items() if value is not None}

        view_buttons = {
            "Zoom in, shortcut=Ctrl + plus": self.notepad.zoom_in,
            "Zoom out, shortcut=Ctrl + minus": self.notepad.zoom_out,
            "Zoom default, shortcut=Ctrl + 0": self.notepad.zoom,
            "Word wrap": self.toggle_wrap,
            "Rainbow cursor, shortcut=Ctrl + Shift + F10": self.notepad.toggle_rainbow_cursor,
            "Go to, shortcut=Ctrl + G": self.notepad.go_to,
            "Spell check everything, shortcut=F4": self.spell_check_everything,
            "Loading bar, shortcut=Ctrl + Shift + F5": lambda: self.tab_controller.current_tab.toggle_loading_animation(refresh_at_the_end=False),
            "Toggle scrollbar": self.toggle_scrollbar_visibility,
            "Toggle horizontal scrollbar": self.toggle_x_scrollbar_visibility if not self.wrap else None
        }

        view_buttons = {key: value for key, value in view_buttons.items() if value is not None}

        config_buttons = {
            "Settings, shortcut=F3": lambda: settings_window_instance.open_settings_window(self.notepad),
            "Toggle reopen after exit, info=Reopen tabs in next startup": lambda: self.notepad.toggle_reopen_after_exit(),
            "Toggle default autosave, info=Autosave tabs by default": lambda: self.notepad.toggle_default_autosave(),
            "Toggle save metadata by default, info=Save tab metadata by default": lambda: self.notepad.toggle_default_metadata(),
            "Toggle spell checking by default, info=Save tab metadata by default": lambda: self.notepad.toggle_default_spell_checking(),
            "Toggle default backup, info=Back up tabs by default": lambda: self.notepad.toggle_default_backup(),
        }

        tab_buttons = {
            "New tab, shortcut=Ctlr + T": self.tab_controller.create_tab,
            "Close tab, shortcut=Ctrl + W": self.tab_controller.close_tab,
            "Duplicate tab, shortcut=Alt + Shift + D": self.notepad.duplicate_and_break,
            "Rename tab, shortcut=F2, info=Rename this tab's name and filename": lambda: self.notepad.rename_current_tab(file_update=False),
            "Recolour tab, info=Change this tab's colour": (lambda: self.notepad.recolour_current_tab()) if settings.use_tab_colours else None,
            "Change tab font, info=Make this tab use a custom font": lambda: self.notepad.change_tab_font(),
            "Clear memento stakcs, info=Delete all of this tab's undo and redo information and deletes the paths from closed tabs": self.clear_memento_stacks,
            "Backup tab, info=Backup this tab regardless of its backup status ": self.notepad.backup_file if settings.use_file_backup else None,
            "Refresh tabs, shortcut=F5, info=Refresh all tabs, ": self.notepad.refresh_tabs,
        }

        tab_buttons = {key: value for key, value in tab_buttons.items() if value is not None}

        # Filter out None values (options not included based on the condition)
        tab_buttons = {key: value for key, value in tab_buttons.items() if value is not None}

        miwon_buttons = {
            f"Mount, shortcut=Ctrl + M, info=Mount the security drive at {settings.security_documents_name}": lambda: self.notepad.open_security_folder(None),
            f"Dismount, shortcut=Ctrl + D, info=Dismount using {settings.security_button_name}": lambda: self.notepad.close_security_folder(),
            "Auto dismount, info=Toggle auto dismounting when exiting the app next time": self.toggle_disable_dismount_when_exit_once,
        }

        help_buttons = {
            "About Yeongu Notes, shortcut=Ctrl + I": self.notepad.show_about,
            "Documentation, shortcut=Ctrl + H": lambda: self.notepad.open_and_break(path=help_path),
        }

        button_info = [
            ("File", file_buttons),
            ("View", view_buttons),
            ("Tab", tab_buttons),
            (settings.security_button_name, miwon_buttons),
            ("Configurations", config_buttons),
            ("Help", help_buttons),
        ]

        for label, button_dict in button_info:
            # For other categories, create buttons as usual
            button_instance = CustomShortcutButton(self.top_bar, label1=label, label2=None, active_bg=self.colour, active_fg=self.foreground_colour, active_fg2=self.foreground_colour, command=lambda label=label, button_dict=button_dict: self.toggle_menu(label, button_dict), font=(settings.regular_font, settings.font_size))
            button_instance.pack(side=LEFT, padx=0)

            # Bindings for hovering over the category buttons
            button_instance.bind("<Enter>", lambda event, label=label, button_dict=button_dict: self.show_menu(label, button_dict))

            setattr(self, f"{label.lower().replace(' ', '_')}_category", button_instance)

    def create_buttons(self):
        settings_window_instance = SettingsWindow(self.root)
        # Create buttons instead of menu items
        file_buttons = {
            "Open, shortcut=Ctrl + O": self.notepad.open_file,
            "Save, shortcut=Ctrl + S": self.notepad.save_file,
            "Save as, shortcut=F12": self.notepad.save_file_as,
            "Save all, shortcut=Ctrl + Alt + S": self.notepad.save_all_files,
            "Backup all, shortcut=Ctrl + B, info=Backup now all backup enabled tabs":  self.notepad.backup_all_files if settings.use_file_backup else None,
            "Exit, shortcut=Esc": self.notepad.save_and_exit,
        }

        file_buttons = {key: value for key, value in file_buttons.items() if value is not None}

        edit_buttons = {
            "Rearrange rows, info=Rearange the position of rows, shortcut=Ctrl + K + S": self.convert_to_reorderable,
            "Rearrange rows window, info=Rearange the position of rows in a seperate window, shortcut=Ctrl + K + W": self.notepad.rearrange_rows,
            "Find and replace, shortcut=Ctrl + F": self.notepad.find_and_replace,
            "Add Indices, info=Add row index to the start of each row, shortcut=Ctrl + K + M": lambda: self.notepad.add_indices(1),
            "Add Programming Indices, info=Add row index to the start of each row starting from 0, shortcut=Ctrl + K + P": lambda: self.notepad.add_indices(0),
            "Add Indices starting from..., info=Add row index to the start of each row starting from a selected index, shortcut=Ctrl + K + N": self.notepad.add_indices_prompt_start,
            "Remove Indices, info=Remove row indices from the start of each row, shortcut=Ctrl + K + R": self.notepad.remove_indices,
            "Change Separator, info=Change separator between indices and text": self.notepad.change_separator,
            "Insert time and date, shortcut=F6": self.notepad.insert_current_datetime_at_cursor,
            "Insert date, shortcut=F7": self.notepad.insert_current_date_at_cursor,
            "Overwrite, shortcut=Insert, info=Update or add text with overwrite/insert": self.notepad.toggle_insert_text,
            "Strikethrough, shortcut=Alt + Shift + S": self.notepad.apply_strikethrough,
        }

        view_buttons = {
            "Zoom in, shortcut=Ctrl + plus": self.notepad.zoom_in,
            "Zoom out, shortcut=Ctrl + minus": self.notepad.zoom_out,
            "Zoom default, shortcut=Ctrl + 0": self.notepad.zoom,
            "Word wrap": self.toggle_wrap,
            "Rainbow cursor, shortcut=Ctrl + Shift + F10": self.notepad.toggle_rainbow_cursor,
            "Go to, shortcut=Ctrl + G": self.notepad.go_to,
            "Spell check everything, shortcut=F4": self.spell_check_everything,
            "Loading bar, shortcut=Ctrl + Shift + F5": lambda: self.tab_controller.current_tab.toggle_loading_animation(refresh_at_the_end=False),
            "Toggle scrollbar": self.toggle_scrollbar_visibility,
            "Toggle horizontal scrollbar": self.toggle_x_scrollbar_visibility if not self.wrap else None
        }

        view_buttons = {key: value for key, value in view_buttons.items() if value is not None}

        config_buttons = {
            "Settings, shortcut=F3": lambda: settings_window_instance.open_settings_window(self.notepad),
            "Toggle reopen after exit, info=Reopen tabs in next startup": lambda: self.notepad.toggle_reopen_after_exit(),
            "Toggle default autosave, info=Autosave tabs by default": lambda: self.notepad.toggle_default_autosave(),
            "Toggle save metadata by default, info=Save tab metadata by default": lambda: self.notepad.toggle_default_metadata(),
            "Toggle spell checking by default, info=Save tab metadata by default": lambda: self.notepad.toggle_default_spell_checking(),
            "Toggle default backup, info=Back up tabs by default": lambda: self.notepad.toggle_default_backup(),
        }

        tab_buttons = {
            "New tab, shortcut=Ctlr + T": self.tab_controller.create_tab,
            "Close tab, shortcut=Ctrl + W": self.tab_controller.close_tab,
            "Duplicate tab, shortcut=Alt + Shift + D": self.notepad.duplicate_and_break,
            "Rename tab, shortcut=F2, info=Rename this tab's name and filename": lambda: self.notepad.rename_current_tab(),
            "Recolour tab, info=Change this tab's colour": (lambda: self.notepad.recolour_current_tab()) if settings.use_tab_colours else None,
            "Change tab font, info=Make this tab use a custom font": lambda: self.notepad.change_tab_font(),
            "Clear memento stakcs, info=Delete all of this tab's undo and redo information": self.clear_memento_stacks,
            "Backup tab, info=Backup this tab regardless of its backup status ": self.notepad.backup_file if settings.use_file_backup else None,
            "Refresh tabs, shortcut=F5, info=Refresh all tabs, ": self.notepad.refresh_tabs,
        }

        # Filter out None values (options not included based on the condition)
        tab_buttons = {key: value for key, value in tab_buttons.items() if value is not None}

        miwon_buttons = {
            f"Mount, shortcut=Ctrl + M, info=Mount the security drive at {settings.security_documents_name}": lambda: self.notepad.open_security_folder(None),
            f"Dismount, shortcut=Ctrl + D, info=Dismount using {settings.security_button_name}": lambda: self.notepad.close_security_folder(),
            "Stay mounted this time, info=Toggle auto dismounting when exiting the app next time": self.toggle_disable_dismount_when_exit_once,
        }

        if self.notepad.is_mounted:
            # Get a list of folders inside security_folder
            security_folders = [folder for folder in os.listdir(settings.security_folder) if os.path.isdir(os.path.join(settings.security_folder, folder))]

            # Security Category Buttons (Menu)
            security_category_buttons = {}
            for folder in security_folders:
                security_category_buttons[folder] = lambda f=folder: self.notepad.save_path(os.path.join(settings.security_folder, f), secure=settings.auto_secure_at_sf)

            # Security Submenus
            submenu_list = []  # List to store submenu dictionaries
            for i, folder in enumerate(security_folders, start=1):
                submenu_dict = {}
                for subfolder in os.listdir(os.path.join(settings.security_folder, folder)):
                    subfolder_path = os.path.join(settings.security_folder, folder, subfolder)
                    if os.path.isdir(subfolder_path):  # Check if it's a subfolder, not a file
                        submenu_dict[subfolder] = lambda f=folder, s=subfolder: self.notepad.save_path(os.path.join(settings.security_folder, f, s), secure=settings.auto_secure_at_sf)

                locals()[f"security_submenu_category_{i}"] = submenu_dict
                submenu_list.append(submenu_dict)

            # Determine the number of submenu categories
            num_submenus = len(submenu_list)

            # Create sub_button_info dynamically
            sub_button_info = [(str(i), submenu_list[i - 1]) for i in range(1, num_submenus + 1)]

        if settings.use_file_menu and not self.secured:
            # Get a list of folders inside security_folder
            option_folders = [folder for folder in os.listdir(settings.file_options_folder) if os.path.isdir(os.path.join(settings.file_options_folder, folder))]

            # Security Category Buttons (Menu)
            file_category_buttons = {}
            for folder in option_folders:
                file_category_buttons[folder] = lambda f=folder: self.notepad.save_path(os.path.join(settings.file_options_folder, f))

            # Security Submenus
            file_submenu_list = []  # List to store submenu dictionaries
            for i, folder in enumerate(option_folders, start=1):
                file_submenu_dict = {}
                for subfolder in os.listdir(os.path.join(settings.file_options_folder, folder)):
                    subfolder_path = os.path.join(settings.file_options_folder, folder, subfolder)
                    if os.path.isdir(subfolder_path):  # Check if it's a subfolder, not a file
                        file_submenu_dict[subfolder] = lambda f=folder, s=subfolder: self.notepad.save_path(os.path.join(settings.file_options_folder, f, s))

                locals()[f"file_submenu_category_{i}"] = file_submenu_dict
                file_submenu_list.append(file_submenu_dict)

            # Determine the number of submenu categories
            num_submenus = len(file_submenu_list)

            # Create sub_button_info dynamically
            file_sub_button_info = [(str(i), file_submenu_list[i - 1]) for i in range(1, num_submenus + 1)]

        help_buttons = {
            "About Yeongu Notes, shortcut=Ctrl + I": self.notepad.show_about,
            "Documentation, shortcut=Ctrl + H": lambda: self.notepad.open_and_break(path=help_path),
        }

        # Define the new category only if self.notepad.is_mounted
        security_category = (settings.security_documents_name, security_category_buttons) if self.notepad.is_mounted else None

        file_category = ("Documents", file_category_buttons) if settings.use_file_menu and not self.secured else None

        button_info = [
            ("File", file_buttons),
            ("Edit", edit_buttons),
            ("View", view_buttons),
            ("Tab", tab_buttons),
            (settings.security_button_name, miwon_buttons),
            *([security_category] if security_category else []),
            *([file_category] if file_category else []),
            ("Configurations", config_buttons),
            ("Help", help_buttons),
        ]

        for label, button_dict in button_info:
            if label == settings.security_documents_name and self.notepad.is_mounted:
                # For other categories, create buttons as usual
                category_button = CustomShortcutButton(self.top_bar, label1=label, label2=None, active_bg=self.colour, active_fg=self.foreground_colour, active_fg2=self.foreground_colour, command=lambda label=label, button_dict=button_dict, sub_button_info=sub_button_info: self.toggle_security_menu(label, button_dict, sub_button_info), font=(settings.regular_font, settings.font_size), info="Click a folder to save as this file\'s directory and set it as secured")
                category_button.pack(side=LEFT, padx=0)

                # Bindings for hovering over the category buttons
                category_button.bind("<Enter>", lambda event, label=label, button_dict=button_dict: self.show_security_menu(label, button_dict, sub_button_info))

                setattr(self, f"{label.lower().replace(' ', '_')}_category", category_button)

            elif label == "Documents" and settings.use_file_menu and not self.secured:
                # For other categories, create buttons as usual
                category_button = CustomShortcutButton(self.top_bar, label1=label, label2=None, active_bg=self.colour, active_fg=self.foreground_colour, active_fg2=self.foreground_colour, command=lambda label=label, button_dict=button_dict, file_sub_button_info=file_sub_button_info: self.toggle_file_menu(label, button_dict, file_sub_button_info), font=(settings.regular_font, settings.font_size), info="Click a folder to save as this file\'s directory")
                category_button.pack(side=LEFT, padx=0)

                # Bindings for hovering over the category buttons
                category_button.bind("<Enter>", lambda event, label=label, button_dict=button_dict: self.show_file_menu(label, button_dict, file_sub_button_info))

                setattr(self, f"{label.lower().replace(' ', '_')}_category", category_button)

            else:
                # For other categories, create buttons as usual
                button_instance = CustomShortcutButton(self.top_bar, label1=label, label2=None, active_bg=self.colour, active_fg=self.foreground_colour, active_fg2=self.foreground_colour, command=lambda label=label, button_dict=button_dict: self.toggle_menu(label, button_dict), font=(settings.regular_font, settings.font_size))
                button_instance.pack(side=LEFT, padx=0)

                # Bindings for hovering over the category buttons
                button_instance.bind("<Enter>", lambda event, label=label, button_dict=button_dict: self.show_menu(label, button_dict))

                setattr(self, f"{label.lower().replace(' ', '_')}_category", button_instance)

    def toggle_menu(self, label, button_dict):
        is_menu = [widget for widget in self.top_bar.winfo_children() if isinstance(widget, Toplevel)]

        if is_menu:
            self.destroy_existing_menus()
        else:
            self.show_menu(label, button_dict)
   
    def toggle_security_menu(self, label, button_dict, sub_button_info):
        is_menu = [widget for widget in self.top_bar.winfo_children() if isinstance(widget, Toplevel)]

        if is_menu:
            self.destroy_existing_menus()
        else:
            self.show_security_menu(label, button_dict, sub_button_info)
   
    def toggle_file_menu(self, label, button_dict, file_sub_button_info):
        is_menu = [widget for widget in self.top_bar.winfo_children() if isinstance(widget, Toplevel)]

        if is_menu:
            self.destroy_existing_menus()
        else:
            self.show_file_menu(label, button_dict, file_sub_button_info)

    def show_menu(self, label, button_dict):
        # Destroy any existing menus
        self.destroy_existing_menus()

        button_dict_instance = button_dict
        clicked_button = getattr(self, f"{label.lower()}_category")

        # Create a larger frame around the buttons with a 5-pixel margin
        menu_frame = Toplevel(self.top_bar)
        menu_frame.wm_overrideredirect(True)
        outer_frame = Frame(menu_frame, bg=settings.ui_bg)  # Set background color to light blue
        outer_frame.pack(padx=0, pady=0)

        # Get the absolute coordinates of the clicked button
        x, y, w, h = clicked_button.winfo_rootx(), clicked_button.winfo_rooty(), clicked_button.winfo_width(), clicked_button.winfo_height()

        for text, command in button_dict_instance.items():
            # Create a frame for each button
            button_frame = Frame(outer_frame, bg=settings.ui_bg)
            button_frame.pack(fill='x', padx=0, pady=0)

            if ',' in text:
                label_text, rest = map(str.strip, text.split(',', 1))

                shortcut_text = None
                info_text = None

                # Check if 'shortcut=' is present
                if 'shortcut=' in rest or 'info=' in rest:
                    parts = [part.strip() for part in rest.split(',')]
                    for part in parts:
                        if part.startswith('shortcut='):
                            shortcut_text = part[len('shortcut='):]
                        elif part.startswith('info='):
                            info_text = part[len('info='):]

                button_with_shortcut = CustomShortcutButton(button_frame, label1=label_text, label2=shortcut_text, active_bg=self.subcolour, active_fg=self.foreground_subcolour, active_fg2=self.foreground_subcolour, command=command, info=info_text)
                button_with_shortcut.pack(expand=TRUE, fill='x', padx=0, pady=0)

            else:
                # Create a normal button for text without a shortcut with a simple style, expanding horizontally
                button_without_shortcut = CustomShortcutButton(button_frame, label1=text, label2=None, active_bg=self.subcolour, active_fg=self.foreground_subcolour, active_fg2=self.foreground_subcolour, command=command)
                button_without_shortcut.pack(expand=TRUE, fill='x',padx=0, pady=0)

        # Set the position of the Toplevel window under the clicked button
        menu_frame.wm_geometry(f"+{x}+{y+h}")

        # Bind the outer frame to hide after a short delay when the mouse leaves
        outer_frame.bind("<Leave>", lambda e: menu_frame.destroy())

        # Focus on the menu
        menu_frame.focus_force()

    def show_security_menu(self, label, button_dict, sub_button_info):
        # Destroy any existing menus
        self.destroy_existing_menus()

        button_dict_instance = button_dict
        clicked_button = getattr(self, f"{label.lower()}_category")

        # Create a larger frame around the buttons with a 5-pixel margin
        menu_frame = Toplevel(self.top_bar)
        menu_frame.wm_overrideredirect(True)
        self.menu_outer_frame = Frame(menu_frame, bg=settings.ui_bg)  # Set background color to light blue
        self.menu_outer_frame.pack(padx=0, pady=0)

        # Get the absolute coordinates of the clicked button
        x, y, w, h = clicked_button.winfo_rootx(), clicked_button.winfo_rooty(), clicked_button.winfo_width(), clicked_button.winfo_height()

        for i, (text, command) in enumerate(button_dict_instance.items()):
            menu_button = CustomShortcutButton(self.menu_outer_frame, label1=text, label2=None, active_bg=self.subcolour, active_fg=self.foreground_subcolour, active_fg2=self.foreground_subcolour, command=command)
            menu_button.pack(fill='x', padx=0, pady=0)

            # Get the label and button_dict from sub_button_info
            label, button_dict = sub_button_info[i]

            # Bindings for hovering over the category button
            menu_button.bind("<Enter>", lambda event, label=label, button_dict=button_dict: self.show_security_submenu(label, button_dict))

            setattr(self, f"{label.lower().replace(' ', '_')}_category", menu_button)

        # Set the position of the Toplevel window under the clicked button
        menu_frame.wm_geometry(f"+{x}+{y+h}")

        # Focus on the menu
        menu_frame.focus_force()

    def show_security_submenu(self, label, submenu):
        self.is_cursor_on_menu_outer_frame = True
        # Destroy any existing submenus
        self.destroy_existing_submenus()

        submenu_instance = submenu
        clicked_button = getattr(self, f"{label.lower()}_category")

        # Create a larger frame around the submenu buttons with a 5-pixel margin
        submenu_frame = Toplevel(self.top_bar)
        submenu_frame.wm_overrideredirect(True)
        outer_frame = Frame(submenu_frame, bg=settings.ui_bg)  # Set background color to light blue
        outer_frame.pack(padx=0, pady=0)

        # Get the absolute coordinates of the clicked button
        x, y, w, h = clicked_button.winfo_rootx(), clicked_button.winfo_rooty(), clicked_button.winfo_width(), clicked_button.winfo_height()

        for text, command in submenu_instance.items():
            submenu_button = CustomShortcutButton(outer_frame, label1=text, label2=None, active_bg=self.subcolour, active_fg=self.foreground_subcolour, active_fg2=self.foreground_subcolour, command=command)
            submenu_button.pack(fill='x', padx=0, pady=0)

        # Set the position of the Toplevel window under the clicked button
        submenu_frame.wm_geometry(f"+{x+w}+{y}")

        # Bind these functions to your frames
        outer_frame.bind("<Enter>", lambda e: self.handle_enter("outer_frame"))
        outer_frame.bind("<Leave>", lambda e: self.notepad.root.after(200, lambda: self.handle_leave("outer_frame")))
        self.menu_outer_frame.bind("<Enter>", lambda e: self.handle_enter("menu_outer_frame"))
        self.menu_outer_frame.bind("<Leave>", lambda e: self.notepad.root.after(200, lambda: self.handle_leave("menu_outer_frame")))

        # Keep track of the submenu
        self.submenus.append(submenu_frame)


    def show_file_menu(self, label, button_dict, sub_button_info):
        # Destroy any existing menus
        self.destroy_existing_menus()

        button_dict_instance = button_dict
        clicked_button = getattr(self, f"{label.lower()}_category")

        # Create a larger frame around the buttons with a 5-pixel margin
        menu_frame = Toplevel(self.top_bar)
        menu_frame.wm_overrideredirect(True)
        self.file_menu_outer_frame = Frame(menu_frame, bg=settings.ui_bg)  # Set background color to light blue
        self.file_menu_outer_frame.pack(padx=0, pady=0)

        # Get the absolute coordinates of the clicked button
        x, y, w, h = clicked_button.winfo_rootx(), clicked_button.winfo_rooty(), clicked_button.winfo_width(), clicked_button.winfo_height()

        for i, (text, command) in enumerate(button_dict_instance.items()):
            menu_button = CustomShortcutButton(self.file_menu_outer_frame, label1=text, label2=None, active_bg=self.subcolour, active_fg=self.foreground_subcolour, active_fg2=self.foreground_subcolour, command=command)
            menu_button.pack(fill='x', padx=0, pady=0)

            # Get the label and button_dict from sub_button_info
            label, button_dict = sub_button_info[i]

            # Bindings for hovering over the category button
            menu_button.bind("<Enter>", lambda event, label=label, button_dict=button_dict: self.show_file_submenu(label, button_dict))

            setattr(self, f"{label.lower().replace(' ', '_')}_file_category", menu_button)

        # Set the position of the Toplevel window under the clicked button
        menu_frame.wm_geometry(f"+{x}+{y+h}")

        # Focus on the menu
        menu_frame.focus_force()

    def show_file_submenu(self, label, submenu):
        self.is_cursor_on_menu_outer_frame = True
        # Destroy any existing submenus
        self.destroy_existing_submenus()

        submenu_instance = submenu
        clicked_button = getattr(self, f"{label.lower()}_file_category")

        # Create a larger frame around the submenu buttons with a 5-pixel margin
        submenu_frame = Toplevel(self.top_bar)
        submenu_frame.wm_overrideredirect(True)
        outer_frame = Frame(submenu_frame, bg=settings.ui_bg)  # Set background color to light blue
        outer_frame.pack(padx=0, pady=0)

        # Get the absolute coordinates of the clicked button
        x, y, w, h = clicked_button.winfo_rootx(), clicked_button.winfo_rooty(), clicked_button.winfo_width(), clicked_button.winfo_height()

        for text, command in submenu_instance.items():
            submenu_button = CustomShortcutButton(outer_frame, label1=text, label2=None, active_bg=self.subcolour, active_fg=self.foreground_subcolour, active_fg2=self.foreground_subcolour, command=command)
            submenu_button.pack(fill='x', padx=0, pady=0)

        # Set the position of the Toplevel window under the clicked button
        submenu_frame.wm_geometry(f"+{x+w}+{y}")

        # Bind these functions to your frames
        outer_frame.bind("<Enter>", lambda e: self.handle_enter("outer_frame"))
        outer_frame.bind("<Leave>", lambda e: self.notepad.root.after(200, lambda: self.handle_leave("outer_frame")))
        self.file_menu_outer_frame.bind("<Enter>", lambda e: self.handle_enter("menu_outer_frame"))
        self.file_menu_outer_frame.bind("<Leave>", lambda e: self.notepad.root.after(200, lambda: self.handle_leave("menu_outer_frame")))

        # Keep track of the submenu
        self.submenus.append(submenu_frame)

    def handle_enter(self, frame):
        if frame == "outer_frame":
            self.is_cursor_on_outer_frame = True
        elif frame == "menu_outer_frame":
            self.is_cursor_on_menu_outer_frame = True

    def handle_leave(self, frame):
        if frame == "outer_frame":
            self.is_cursor_on_outer_frame = False
        elif frame == "menu_outer_frame":
            self.is_cursor_on_menu_outer_frame = False

        if not (self.is_cursor_on_outer_frame or self.is_cursor_on_menu_outer_frame):
            self.destroy_existing_menus()
        elif not self.is_cursor_on_outer_frame:
            self.destroy_existing_submenus()

    def destroy_existing_submenus(self):
        # Destroy any existing submenus
        for submenu in self.submenus:
            submenu.destroy()

        # Clear the list
        self.submenus = []

    def destroy_existing_menus(self):
        # Destroy any existing menus
        for widget in self.top_bar.winfo_children():
            if isinstance(widget, Toplevel):
                widget.destroy()

    def display(self, info='', delay_ms=5000, fg=settings.ui_fg):
        self.labels_on_queue += 1

        if info == '':
            self.display_time()
            return

        self.info_label.config(text=info, fg=fg)

        # Schedule clearing the label after 20000 milliseconds
        self.root.after(delay_ms, self.clear_info_label)

    def display_time(self, fg=settings.ui_fg, ignore_labels_on_queue=False):
        if self.labels_on_queue == 0 or ignore_labels_on_queue:
            self.info_label.config(text=f"{datetime.now().strftime('%H:%M')}  {self.notepad.korean_date}", fg=fg)

    def display_path(self, info=''):
        if info is None:
            info = ''

        elif info == '':
            if self.file:
                if settings.show_full_paths:
                    info = self.file.replace('/', '\\').capitalize()
                else:
                    # Convert the path to Windows format
                    formatted_path = self.file.replace('/', '\\')

                    # Capitalize the drive letter
                    formatted_path = formatted_path[0].upper() + formatted_path[1:]

                    # Split the path into parts
                    parts = formatted_path.split('\\')

                    # Check if the path needs to be shortened
                    if len(parts) > 5:
                        drive, *folders = parts
                        folders = [' ...'] + folders[-4:]
                        formatted_path = drive + '\\' + '\\'.join(folders)

                    info = formatted_path

        self.tab_controller.path_label.config(text=info)

    def display_autosave(self, info='', delay_ms=2000, fg=settings.ui_fg):
        self.labels_on_queue = 1

        if info == '':
            self.display_time()
            return

        self.info_label.config(text=info, fg=fg)

        # Schedule clearing the label after 20000 milliseconds
        self.root.after(delay_ms, self.clear_info_label)

    def clear_info_label(self):
        if self.labels_on_queue == 1:
            #self.info_label.config(text='Welcome', fg=settings.ui_fg)
            self.labels_on_queue = 0
            self.display_time()
        else:
            self.labels_on_queue -= 1

    def toggle_autosave(self):
        if self.autosave:
            self.autosave = False
            self.notepad.save_file(ignore_save_as=True, save_metadata_only=True)
            self.display('Autosave Disabled')
        else:
            self.autosave = True
            self.notepad.save_file(ignore_save_as=True, save_metadata_only=True)
            self.display('Autosave Enabled')

    def toggle_metadata(self, state=None):
        if state:
            self.metadata = not state
        if self.save_metadata:
            self.save_metadata = False
            self.display('Metadata Disabled')
        else:
            self.save_metadata = True
            self.notepad.save_file(ignore_save_as=True, save_metadata_only=True)
            self.display('Metadata Enabled')

    def toggle_wrap(self):
        self.wrap = not self.wrap
        self.notepad.save_file(ignore_save_as=True, save_metadata_only=True)
        self.notepad.refresh_tabs()

    def convert_to_reorderable(self):
        if self.read_only:
            return

        self.notepad.disable_escape_app = True
        self.notepad.save_memento()
        self.notepad.save_current_page_view_info(tab=self)
        self.reorderable = True
        self.notepad.refresh_tabs()

    def toggle_read_only(self):
        if self.file:
            self.read_only = not self.read_only
            
            if self.read_only:
                self.notepad.save_file(ignore_save_as=True, ignore_metadata=True)

            try:
                # Get the current file permissions
                current_permissions = os.stat(self.file).st_mode

                # Toggle the write permissions by XORing with 0o222
                new_permissions = current_permissions ^ 0o222
                os.chmod(self.file, new_permissions)

            except FileNotFoundError:
                self.display(f"The file '{self.file}' does not exist.")
                if not self.stop_regression:
                    self.stop_regression = True
                    self.read_only_button.invoke()
                else:
                    self.stop_regression = False
            except PermissionError:
                self.display(f"Permission denied to modify the file '{self.file}'.")
                if not self.stop_regression:
                    self.stop_regression = True
                    self.read_only_button.invoke()
                else:
                    self.stop_regression = False

            if not self.read_only:
                self.notepad.save_file(ignore_save_as=True, save_metadata_only=True)

            self.notepad.refresh_tabs()

        else:
            self.display('Please save the file before converting it to read-only')
            if not self.stop_regression:
                self.stop_regression = True
                self.read_only_button.invoke()

    def toggle_secured(self):
        self.secured = not self.secured
        self.notepad.save_file(ignore_save_as=True, save_metadata_only=True)

    def toggle_spell(self):
        self.spell = not self.spell
        self.notepad.save_file(ignore_save_as=True, save_metadata_only=True)
        self.display(f"Spell check to this tab {'enabled' if self.spell else 'disabled'}")
        if self.spell:
            self.spell_check(range='full')
        else:
            self.text_area.tag_remove("misspelled", "1.0", "end")

    def toggle_backup(self):
        self.backup = not self.backup
        self.notepad.save_file(ignore_save_as=True, save_metadata_only=True)
        self.display(f"Backup to this tab {'enabled' if self.backup else 'disabled'}")

    def toggle_covert_json(self):
        self.png_json = not self.png_json
        if self.png_json:
            self.notepad.convert_to_json()
        else:
            self.notepad.convert_from_json()


    def toggle_disable_dismount_when_exit_once(self):
        self.notepad.disable_dismount_when_exit_once = not self.notepad.disable_dismount_when_exit_once
        if self.notepad.disable_dismount_when_exit_once:
            self.display('Drive will not be dismounted when you leave the app')
        else:
            self.display('Drive will be dismounted when you leave the app')

    def clear_memento_stacks(self):
        self.memento_stack = []
        self.redo_stack = []
        self.notepad.recently_closed_tabs_paths = []

        self.display('Memento stakcs cleared', delay_ms=10000)

    def on_lines_label_click(self, event):
        # Calculate the text widget coordinates relative to the screen
        text_widget_y = event.y_root - self.text_area.winfo_rooty()

        # Set focus to the text widget
        self.text_area.focus_set()

        # Set the insertion cursor (text cursor) to the calculated coordinates
        self.text_area.mark_set("insert", f"@1,{text_widget_y}")
        
        # Get cursor position and line number
        cursor_index = self.text_area.index(tk.INSERT)
        line_number = int(cursor_index.split('.')[0])
        
        # Select entire line and move cursor to the end
        self.text_area.tag_remove("sel", "1.0", "end")
        self.text_area.tag_add("sel", f"{line_number}.0", f"{line_number}.end")
        self.text_area.mark_set("insert", f"{line_number}.end")

        self.notepad.update_character_and_cursor_labels()

    def on_lines_label_drag(self, event):
        # Calculate the text widget coordinates relative to the screen
        text_widget_y = event.y_root - self.text_area.winfo_rooty()

        # Set focus to the text widget
        self.text_area.focus_set()

        # Set the insertion cursor (text cursor) to the calculated coordinates
        self.text_area.mark_set("insert", f"@1,{text_widget_y}")
        
        # Get cursor position and line number
        cursor_index = self.text_area.index(tk.INSERT)
        line_number = int(cursor_index.split('.')[0])
        
        # Check if the drag selection is already in progress
        if hasattr(self, "drag_start_line"):
            # Update the selection range
            self.text_area.tag_remove("sel", "1.0", "end")
            start_line = min(self.drag_start_line, line_number)
            end_line = max(self.drag_start_line, line_number) + 1
            self.text_area.tag_add("sel", f"{start_line}.0", f"{end_line}.0")
        else:
            # Start the drag selection
            self.drag_start_line = line_number

        self.notepad.update_character_and_cursor_labels()

    def on_lines_label_drag_release(self, event):        
        # Clear the drag start line attribute
        if hasattr(self, "drag_start_line"):
            del self.drag_start_line

    def get_typing_language_code(self):
        language_id = ct.windll.user32.GetKeyboardLayout(0) & 0xFFFF
        language_name_buffer = ct.create_unicode_buffer(256)
        ct.windll.kernel32.GetLocaleInfoW(language_id, 0x00000002, language_name_buffer, ct.sizeof(language_name_buffer))  # 0x00000002 is LOCALE_SLANGUAGE
        language_name = language_name_buffer.value.split('(')[0].strip().lower()
        
        language_map = {
            "english": "en",
            "spanish": "es",
            "french": "fr",
            "italian": "it",
            "portuguese": "pt",
            "german": "de",
            "russian": "ru",
            "arabic": "ar",
            "latvian": "lv",
            "basque": "eu",
            "dutch": "nl"
        }
        
        for key, value in language_map.items():
            if key in language_name:
                return value
        
        # Default to English if the language name doesn't match any in the map
        return "en"

    def spell_check_everything(self):
        correction_ranges = self.spell_check('full', thread=True, force=True, ignore_current_word=True)

        if correction_ranges:
            current_tags = self.text_area.tag_ranges("misspelled")
            ranges_list = []
            for i in range(0, len(current_tags), 2):
                start = self.text_area.index(current_tags[i])
                end = self.text_area.index(current_tags[i + 1])
                ranges_list.append((start, end))

            if ranges_list != correction_ranges:
                self.text_area.tag_remove("misspelled", "1.0", "end")
                for start_index, end_index in correction_ranges:
                    self.text_area.tag_add("misspelled", start_index, end_index)
            else:
                self.text_area.tag_remove("misspelled", "1.0", "end")

    def apply_spell_underline(self, coords):
        if not self.spell or self.reorderable:
            return

        current_tags = self.text_area.tag_ranges("misspelled")
        ranges_list = []
        for i in range(0, len(current_tags), 2):
            start = self.text_area.index(current_tags[i])
            end = self.text_area.index(current_tags[i + 1])
            ranges_list.append((start, end))

        if ranges_list != coords:
            self.text_area.tag_remove("misspelled", "1.0", "end")
            for start_index, end_index in coords:
                self.text_area.tag_add("misspelled", start_index, end_index)

    def valid_words(self, text, start_idx):
        def is_valid(word):
            disallowed_chars = ['/', '\\', ';', ':', '.', ',', '?', '@', '#', '%', '^', '&', '*', '+', '=', '|']
            # Check if word contains any digit or symbols like @
            if any(char.isdigit() or char in '@#%^&*()+=;:",.?/\\|' for char in word[1:-1]):
                return False
            # Check if word is surrounded by punctuation on both sides
            if word[0] in disallowed_chars and word[-1] in disallowed_chars:
                return False
            # Check if word contains more than one punctuation character or / or \
            if sum(1 for char in word if char in disallowed_chars) > 1:
                return False
            return True
        
        words = text.split()
        valid_words_with_coords = []
        current_idx = start_idx

        for word in words:
            stripped_word = word.strip(string.punctuation)
            if is_valid(word):
                word_start = text.find(word, current_idx)
                word_end = word_start + len(word)
                if stripped_word.lower() not in ['', 'i\'m', 'i\'d', 'i\'ll', 'i\'ve', 'you\'re', 'you\'ve', 'he\'s', 'she\'s', 'it\'s',
                                                'we\'re', 'we\'ve', 'they\'re', 'they\'ve', 'don\'t', 'doesn\'t', 'didn\'t', 'can\'t',
                                                'won\'t', 'wouldn\'t', 'shouldn\'t', 'isn\'t', 'aren\'t', 'wasn\'t', 'weren\'t', 'haven\'t',
                                                'hasn\'t', 'hadn\'t', 'couldn\'t', 'should\'ve', 'would\'ve', 'could\'ve', 'might\'ve',
                                                'must\'ve', 'that\'s', 'what\'s', 'here\'s', 'there\'s', 'who\'s', 'let\'s', 'where\'s',
                                                'how\'s', 'why\'s', 'when\'s', 'isn\'t']:
                    valid_words_with_coords.append((stripped_word, word_start, word_end))
            current_idx = word_end if 'word_end' in locals() else current_idx
        
        return valid_words_with_coords
    
    def spell_check(self, range: Literal['full', 'line', '2lines', 'selection'], specific_range=None, thread=False, ignore_current_word=False, force=False):
        if self.reorderable:
            return
        if not self.spell and not force:
            return
        try:
            if self.read_only:
                range = 'full'
            if not thread and not force:
                self.text_area.tag_remove("misspelled", "1.0", "end")
            else:
                coords = []

            if specific_range:
                start, end = specific_range
            elif range == 'line':
                start = self.text_area.index("insert linestart")
                end = self.text_area.index("insert lineend")
            elif range == '2lines':
                start = self.text_area.index("insert - 1 lines linestart")
                end = self.text_area.index("insert lineend")
            elif range == 'selection':
                start = self.text_area.index("sel.first")
                end = self.text_area.index("sel.last")
            else:
                start, end = "1.0", "end"

            if ignore_current_word:
                selected_text = self.text_area.get(start, end)
            else:
                cursor_pos = self.text_area.index("insert")
                word_start = self.text_area.search(r'\s', cursor_pos, backwards=True, regexp=True)
                word_end = self.text_area.search(r'\s', cursor_pos, regexp=True)
                if word_start == "":
                    word_start = "1.0"
                else:
                    word_start = self.text_area.index(f"{word_start} + 1c")

                if word_end == "":
                    word_end = self.text_area.index("end-1c")

                if "misspelled" in self.text_area.tag_names(cursor_pos):
                    selected_text = self.text_area.get(start, end)
                else:
                    selected_text = (self.text_area.get(start, word_start) + 
                                    ' ' * (int(word_end.split('.')[1]) - int(word_start.split('.')[1])) + 
                                    self.text_area.get(word_end, end))

            count_result = self.text_area.count("1.0", start)
            start_idx = count_result[0] if count_result else 0

            valid_words_with_coords = self.valid_words(selected_text, start_idx)

            if settings.use_typing_language_to_spell_check:
                languages = [self.get_typing_language_code()]
            else:
                languages = settings.spell_check_languages
            spellcheckers = {lang: SpellChecker(language=lang) for lang in languages}

            misspelled_words = []

            for word, word_start, word_end in valid_words_with_coords:
                if all(word in spellcheckers[lang].unknown([word]) for lang in languages):
                    misspelled_words.append((word, word_start, word_end))

            for word, word_start, word_end in misspelled_words:
                start_index = self.text_area.index(f"{start}+{word_start}c")
                end_index = self.text_area.index(f"{start}+{word_end}c")
                if not thread:
                    self.text_area.tag_add("misspelled", start_index, end_index)
                else:
                    coords.append((start_index, end_index))
        except TclError:
            pass

        finally:
            if thread:
                return coords


    def get_state(self):
        state = {key: value for key, value in vars(self).items() if key not in [
            'text_area', 'root', 'submenus', 'is_cursor_on_outer_frame', 
            'is_cursor_on_outer_frame', 'menu_outer_frame', 'notepad', 'ctk_textbox_scrollbar', 'info_label', 'top_bar', 'is_text_oversized', 'loading_bar_label', 
            'loading_bar', 'animation_bar', 'autosave_button', 'autosave_icon_off', 'autosave_icon_on', 'ctk_x_textbox_scrollbar', 'subcolour', 'foreground_subcolour',
            'items_to_display', 'reorderable', 'reordered_text', 'saved_text', 'saved_strikethrough_ranges', 'saved_misspelled_ranges', 'reordered_strikethrough_ranges', 'reorderable_start_index',
            'tab_controller', 'rich_text_button', 'secured_button', 'path_label', 'done_button', 'convert_json_button',
            'cancel_button', 'metadata_handler', 'read_only_button', 'notebook', 'reorderable_data'] and '_category' not in key and '_file_category' not in key}
        
        return state






class TabController:
    def __init__(self, root, notepad):
        self.notepad = notepad
        self.root = root

        self.notebook_style = ttk.Style()

        # Create a top bar
        self.top_bar = Frame(root, height=40, bg=settings.ui_bg, bd=0)
        self.top_bar.pack(side=TOP, fill=X)

        self.top_bar.bind("<Double-1>", lambda event: self.notepad.invoke_maximize_button())

        self.nav_spacer_label = tk.Label(self.top_bar, padx=58, bg=settings.ui_bg)
        self.nav_spacer_label.pack(side=RIGHT)

        self.zoom_label = Label(self.top_bar, text='100%', fg=settings.ui_fg, bg=settings.ui_bg, font=(settings.regular_font, 10))
        self.zoom_label.pack(side=RIGHT, padx=20)

        self.keyboard_layout_label = Label(self.top_bar, text='', fg='#7a7a7a', bg=settings.ui_bg, font=(settings.regular_font, 10, 'italic'))
        self.keyboard_layout_label.pack(side=RIGHT, padx=20)

        self.path_label = Label(self.top_bar, text='', fg='#7a7a7a', bg=settings.ui_bg, font=(settings.regular_font, 10, 'italic'))
        self.path_label.pack(side=RIGHT, padx=20)

        # Import the Notebook.tab element from the default theme
        self.notebook_style.element_create('Plain.Notebook.tab', "from", 'clam')

        # Redefine the TNotebook Tab layout to use the new element
        self.notebook_style.layout("TNotebook.Tab",
            [('Plain.Notebook.tab', {'children':
                [('Notebook.padding', {'side': 'top', 'children':
                    [('Notebook.focus', {'side': 'top', 'children':
                        [('Notebook.label', {'side': 'top', 'sticky': ''})],
                    'sticky': 'nswe'})],
                'sticky': 'nswe'})],
            'sticky': 'nswe'})])

        self.notebook_style.map("TNotebook.Tab", 
            background=[('selected', 'blue'), ('', settings.ui_bg)],
            bordercolor=[('selected', settings.ui_bg), ('', settings.ui_bg)],
            lightcolor=[('selected', 'blue'), ('', settings.ui_bg)],
            expand=[('selected', [0, 0, 0, 0])]
        )

        # Add status labels
        self.cursor_label = Label(self.top_bar, text='Ln 0, Col 0', fg=settings.ui_fg, bg=settings.ui_bg, font=(settings.regular_font, 10))
        self.cursor_label.place(x=10, y=2)

        self.character_label = Label(self.top_bar, text='0 characters, 0 lines', fg=settings.ui_fg, bg=settings.ui_bg, font=(settings.regular_font, 10))
        self.character_label.place(x=150, y=2)

        self.notebook_style.configure("TNotebook.Tab", font=(settings.medium_font, 11), padding=[10, 2])

        self.notebook_style.layout("TNotebook", [])
        self.notebook_style.configure("TNotebook", highlightbackground="#848a98",tabmargins=0, background=settings.ui_bg, foreground=settings.ui_fg, padding=[0, 0], lightcolor='green')

        # Create and pack the ttk.Notebook widget
        self.notebook = ttk.Notebook(root, style="TNotebook")
        self.notebook.pack(expand=YES, fill=BOTH, side=TOP)

        if settings.navigation_buttons:
            # Add minimize, maximize, and close buttons with customized appearance
            self.minimize_button = CustomShortcutButton(self.top_bar, img_path=r"{}\minimize.png".format(images_folder), command=self.notepad.minimize, active_bg='#555555', bg=settings.ui_bg)
            self.maximize_button = CustomShortcutButton(self.top_bar, img_toggle=[r"{}\maximize.png".format(images_folder), r"{}\maximize_off.png".format(images_folder), not self.root.attributes('-fullscreen')], active_bg='#555555', command=self.notepad.maximize, bg=settings.ui_bg)
            self.close_button = CustomShortcutButton(self.top_bar, img_path=r"{}\x.png".format(images_folder), hover_bg='red', active_bg='#6b0000', command=lambda: self.notepad.save_and_exit(force_exit=True), bg=settings.ui_bg)

            # Place the buttons with customized appearance
            self.close_button.place(x=self.root.winfo_screenwidth() - 29, y=0)
            self.maximize_button.place(x=self.root.winfo_screenwidth() - 63, y=0)
            self.minimize_button.place(x=self.root.winfo_screenwidth() - 97, y=0)

        #Debug ruler
        '''for i in range(1920, 0, -10):  # Change the step size to -10 for placing from the end
            if (1920 - i) % 100 == 0:  # Adjusted condition to calculate the correct index for the yellow dots
                tk.Canvas(self.top_bar, width=3, height=3, bg='yellow').place(x=i, y=10)
            else:
                tk.Canvas(self.top_bar, width=3, height=3, bg='red').place(x=i, y=10)'''
                        
        self.saved_tabs = {}
        self.tabs = []
        self.current_tab = None
        self.stop_switch_tab_flag = False

        self.notebook.bind("<<NotebookTabChanged>>", self.on_tab_change)

    def on_tab_change(self, event=None):
        if not self.notepad.disable_autosave_temporarily or not self.stop_switch_tab_flag:
            selected_tab_index = self.notebook.index(self.notebook.select())
            self.switch_tab(selected_tab_index)

    def duplicate_tab(self, tab_index=None):
        if tab_index is None:
            tab_index = self.notebook.index(self.notebook.select())

        tab = self.tabs[tab_index]
        
        '''if tab.read_only:
            tab.display('Cannot duplicate read-only files')
            return'''

        if tab.reorderable:
            tab.display('Cannot duplicate reorderable tabs')
            return

        if tab.secured:
            tab.display('Cannot duplicate secured tabs', fg='orange')
            return

        tab_content = tab.text_area.get(1.0, tk.END)[:-1]

        self.notepad.save_current_page_view_info(tab=tab)

        tab_colour = tab.colour
        tab_name = self.notebook.tab(tab_index, "text").rstrip('*')
        tab_state = tab.get_state()

        new_tab = self.create_tab(tab_colour=tab_colour, tab_name=tab_name, **tab_state)

        new_tab.text_area.insert(1.0, tab_content)
        self.notepad.apply_saved_page_view_info(tab=new_tab)

        #Make new tab unsaved and not overwrite the original's file
        new_tab.file = None
        new_tab.safe_to_save = False
        new_tab.last_saved_file = None
        new_tab.last_saved_file_using_save_path = None
        new_tab.duplicated = True
        self.rename_tab(tab_index=len(self.tabs)-1, new_name=tab_name + ' - Copy', file_update=False)
        tab.memento_stack.pop()
        
        self.update_tab_name_indicator(len(self.tabs)-1, False)
        self.saved_tabs[len(self.tabs)-1] = False

        if new_tab.read_only:
            new_tab.text_area.config(insertwidth=0)

    def refresh_tabs(self):
        self.notepad.test_status()
        initial_index = self.notebook.index(self.notebook.select())
        tabs_copy = self.tabs.copy()
        convert_back_to_text_after_refresh = False
        after_refresh_tab = None
        after_refresh_new_tab = None

        for i, tab in enumerate(tabs_copy):
            convert_back_to_text = tab.reordered_text is not None
            reorderable = tab.reorderable

            if not (tab.reorderable or convert_back_to_text):
                tab_content = tab.text_area.get(1.0, tk.END)

                if tab_content.endswith('\n'):
                    tab_content = tab_content[:-1]

                self.notepad.save_current_page_view_info(tab=tab)

            if tab.reorderable and not convert_back_to_text:
                self.notepad.save_current_page_view_info(tab=tab)
                reorderable_data = [item if item is not None else "" for item in tab.text_area.get("1.0", "end-1c").split("\n")], tab.text_area.get(1.0, tk.END)[:-1], tab.text_area.tag_ranges("strikethrough"), int(tab.text_area.index(tk.INSERT).split('.')[0]) - 1
            else:
                reorderable_data = {}

            tab_colour = tab.colour
            tab_name = self.notebook.tab(0, "text")
            tab_state = tab.get_state()

            #print(f'Tab name: {tab_name}\n')
            #print(f'Tab state: {tab_state}\n\n\n')

            self.close_tab(tab_index=0, ignore_unsaved=True, update_saved_tabs=False, destroy_if_no_tabs=False)

            new_tab = self.create_tab(tab_colour=tab_colour, tab_name=tab_name, reorderable_data=reorderable_data, **tab_state)

            if not (new_tab.reorderable or convert_back_to_text):
                new_tab.text_area.insert(1.0, tab_content)
                self.notepad.apply_saved_page_view_info(tab=new_tab)

            if new_tab.read_only:
                new_tab.text_area.config(insertwidth=0)

            if convert_back_to_text:
                convert_back_to_text_after_refresh = True
                after_refresh_tab = tab
                after_refresh_new_tab = new_tab

            elif reorderable and i == initial_index:
                after_refresh_tab = tab
                after_refresh_new_tab = new_tab

        self.notepad.root.after(150, lambda: self.after_refresh(initial_index, after_refresh_tab, after_refresh_new_tab, convert_back_to_text_after_refresh))

    def after_refresh(self, tab_index, tab, new_tab, convert_back_to_text):
        if convert_back_to_text:
            tab_content = tab.reordered_text
            new_tab.text_area.insert(1.0, tab_content)
            new_tab.reorderable = False
            self.notepad.apply_saved_page_view_info(tab=new_tab)
            self.notepad.zoom_refresh()
            if tab.reordered_strikethrough_ranges:
                ranges = tab.reordered_strikethrough_ranges
                new_tab.text_area.tag_remove("strikethrough", "1.0", tk.END)
                for i in range(0, len(ranges), 2):
                    new_tab.text_area.tag_add("strikethrough", ranges[i], ranges[i + 1])        

        self.switch_tab(tab_index)

        self.notepad.disable_escape_app = False

        def set_reorderable_focus():
                new_tab.text_area.focus()
                selected_item = new_tab.text_area.treeview.selection()[0]
                new_tab.text_area.treeview.selection_set(selected_item)
                new_tab.text_area.treeview.event_generate("<Button-1>")
                self.notepad.disable_escape_app = True

        if new_tab:
            if new_tab.reorderable:
                self.root.after(150, set_reorderable_focus)

    def create_tab(self, tab_name=None, tab_colour=None, tab_foreground_colour=None, wrap=settings.wrap, save_metadata=True, reorderable_data={}, secured=False, autosave=settings.default_autosave, file=None, backup=settings.default_backup, png_json=False, spell=settings.default_spell_check, **kwargs):
        if settings.use_tab_colours:
            if tab_colour == None:
                try:
                    # Attempt to retrieve color from settings
                    tab_colour = getattr(settings, f"tab_{len(self.tabs)}_colour", None)

                    # Check if the retrieved color is a valid hexadecimal value
                    if tab_colour is not None and not re.match(r'^#(?:[0-9a-fA-F]{3}){1,2}$', tab_colour):
                        raise ValueError("Invalid hex color format")

                except (AttributeError, ValueError):
                    # If settings module is not available, or color is not a valid hex value, assign a random color
                    tab_colour = "#{:06x}".format(random.randint(0, 0xFFFFFF))

                if tab_colour is None:
                    # If the color is not defined in settings, assign a random color
                    while True:
                        # Generate a random color
                        tab_colour = "#{:06x}".format(random.randint(0, 0xFFFFFF))

                        hex_color = tab_colour.lstrip("#")
                        rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

                        # Calculate luminance (Y' value)
                        luminance = (0.299 * rgb[0] + 0.587 * rgb[1] + 0.114 * rgb[2]) / 255

                        luminance_threshold = 0.2

                        if not (luminance < luminance_threshold or luminance > 1 - luminance_threshold):
                            break

        else:
            if hasattr(settings, f'tab_{len(self.tabs)}_colour'):
                tab_colour = getattr(settings, f'tab_{len(self.tabs)}_colour')
            else:
                tab_colour = settings.selection_bg
            
            if not tab_colour.startswith('#'):
                tab_colour = webcolors.name_to_hex(tab_colour)

        hex_color = tab_colour.lstrip("#")
        rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

        # Calculate luminance (Y' value)
        luminance = (0.299 * rgb[0] + 0.587 * rgb[1] + 0.114 * rgb[2]) / 255

        # Set contrast color based on luminance
        tab_foreground_colour = "#ffffff" if luminance < 0.5 else "#000000"

        new_tab = Tab(self.notebook, self.notepad, tab_colour, tab_foreground_colour, wrap=wrap, save_metadata=save_metadata, reorderable_data=reorderable_data, secured=secured, autosave=autosave, file=file, backup=backup, png_json=png_json, spell=spell, **kwargs)
        self.tabs.append(new_tab)

        if tab_name:
            self.notebook.add(new_tab.root, text=tab_name)
        else:
            existing_numbers = [int(re.search(r'Untitled (\d+)', self.notebook.tab(tab_id, "text")).group(1)) if re.search(r'Untitled (\d+)', self.notebook.tab(tab_id, "text")) else 0 for tab_id in self.notebook.tabs()]
            highest_number = max(existing_numbers, default=0)
            self.notebook.add(new_tab.root, text=f"Untitled {highest_number + 1}")

        self.current_tab = new_tab

        self.switch_tab(len(self.tabs)-1)

        return new_tab

    def switch_tab(self, tab_index, do_not_focus=False):       
        self.stop_switch_tab_flag = True
        self.root.title(f"Yeongu Notes - {self.notebook.tab(tab_index, 'text')}")

        if self.notepad.is_animation_running:
            animation_x = self.current_tab.loading_bar_label.winfo_x() + 25
            self.current_tab.toggle_loading_animation(turn_off=True)
        else:
            animation_x = None

        if 0 <= tab_index < len(self.tabs):
            self.notebook.select(self.tabs[tab_index].root)
            self.current_tab = self.tabs[tab_index]

            #self.notepad.save_current_page_view_info(tab=self.current_tab)

            tab_colour = self.current_tab.colour
            foreground_tab_colour = self.current_tab.foreground_colour

            # Mapping styles for selected and unselected tabs
            self.notebook_style.map("TNotebook.Tab", 
                background=[('selected', tab_colour), ('', settings.ui_bg)],
                bordercolor=[('selected', settings.ui_bg), ('', settings.ui_bg)],
                lightcolor=[('selected', tab_colour), ('', settings.ui_bg)],
                expand=[('selected', [0, 0, 0, 0])],
                foreground=[('selected', foreground_tab_colour), ('', settings.ui_fg)],
            )

            if self.current_tab.reorderable:
                self.notepad.disable_escape_app = True

                if animation_x is not None:
                    self.current_tab.toggle_loading_animation(refresh_at_the_end=self.notepad.refresh_after_loading, start_x=animation_x)

                return
            else:
                self.notepad.disable_escape_app = False

            self.root.after(50, lambda: self.restore_cursor_position(self.current_tab, animation_x=animation_x, do_not_focus=do_not_focus))

            self.current_tab.display_path()
            if self.current_tab.reorderable:
                self.notepad.disable_escape_app = True
                return
            else:
                self.notepad.disable_escape_app = False
            self.notepad.update_zoom_label()
            self.notepad.update_character_and_cursor_labels()

    def switch_to_next_tab(self):
        # Switch to the next tab, looping around if necessary
        current_index = self.notebook.index(self.notebook.select())
        next_index = (current_index + 1) % len(self.tabs)
        self.switch_tab(next_index)

    def switch_to_previous_tab(self):
        # Switch to the previous tab, looping around if necessary
        current_index = self.notebook.index(self.notebook.select())
        previous_index = (current_index - 1) % len(self.tabs)
        self.switch_tab(previous_index)

    def restore_cursor_position(self, tab, animation_x=None, do_not_focus=False):
        if tab.reorderable:
            return

        if not do_not_focus:
            tab.text_area.focus_set()

        if animation_x is not None:
            tab.toggle_loading_animation(refresh_at_the_end=self.notepad.refresh_after_loading, start_x=animation_x)

        self.notepad.decide_scrollbar_toggle()

        self.stop_switch_tab_flag = False


    def close_tab(self, tab_index=None, ignore_unsaved=False, update_saved_tabs=True, destroy_if_no_tabs=True):
        if tab_index is None:
            tab_index = self.notebook.index(self.notebook.select())

        if 0 <= tab_index < len(self.tabs):
            if not ignore_unsaved:
                unsaved_changes = not self.saved_tabs.get(tab_index, True)

                if unsaved_changes:
                    # Prompt the user to save changes before closing
                    message = f"Would you like to save the changes to '{self.notebook.tab(tab_index, 'text').rstrip('*')}'?"
                    response = CustomEntryDialog(self.root,title='Unsaved changes', window_title='Close tab', message=message, bg=self.tabs[tab_index].colour, fg=self.tabs[tab_index].foreground_colour, entry=False, height=170).result

                    if response is None or response == 'cancel':  # User clicked Cancel
                        return None
                    elif response == 'yes':  # User clicked Yes to save changes
                        self.notepad.save_file_as()

                        # Check if the file was successfully saved
                        if not self.saved_tabs.get(tab_index, False):
                            # File wasn't saved, don't close the tab
                            return None

            # Close the tab
            tab_to_close = self.tabs[tab_index]

            if self.tabs[tab_index].file:
                self.notepad.recently_closed_tabs_paths.append(self.tabs[tab_index].file)
                self.notepad.recently_closed_tabs_paths = self.notepad.recently_closed_tabs_paths[-20:]


            # Assuming tab_to_close is an instance of your Tab class
            for widget in tab_to_close.root.winfo_children():
                try:
                    widget.unbind_all()
                except:
                    pass

            # Forget the tab
            self.notebook.forget(tab_to_close.root)

            # Remove references to the closed tab
            self.tabs.remove(tab_to_close)
            del tab_to_close


            if update_saved_tabs:

                # Check if tab_index exists
                if tab_index in self.saved_tabs:

                    # Delete the index and its associated value
                    del self.saved_tabs[tab_index]

                    # Shift the indices greater than tab_index to occupy its place
                    for key in list(self.saved_tabs.keys()):
                        if key > tab_index:
                            # Move the value to the previous key
                            self.saved_tabs[key - 1] = self.saved_tabs[key]
                            # Remove the original key
                            del self.saved_tabs[key]

                # Update saved state for the next tab if there is one
                if self.tabs:
                    next_tab_index = self.notebook.index(self.notebook.select())
                    self.saved_tabs[next_tab_index] = self.saved_tabs.get(next_tab_index, True)

            # Check if there's only one tab left, destroy the entire app
            if not self.tabs and destroy_if_no_tabs:
                if not self.notepad.is_initially_mounted and self.notepad.is_mounted and not self.notepad.disable_dismount_when_exit_once:
                    self.notepad.close_security_folder_and_exit()
                else:
                    self.notepad.backup_all_files()
                    self.notepad.save_paths()
                    self.root.destroy()

    def get_autosave_enabled_tabs(self):
        autosaved_enabled_tabs = []
        for i, tab in enumerate(self.tabs):
            if tab.autosave and not tab.reorderable and not tab.read_only:
                autosaved_enabled_tabs.append(i)
        return autosaved_enabled_tabs

    def update_tab_name_indicator(self, tab_index, saved_state):
        current_tab_name = self.notebook.tab(self.tabs[tab_index].root, "text")

        if saved_state:
            # Tab is now saved, remove '*' from the tab name
            if current_tab_name.endswith('*'):
                updated_tab_name = current_tab_name[:-1]
                self.notebook.tab(self.tabs[tab_index].root, text=updated_tab_name)
                self.root.title(f"Yeongu Notes - {self.notebook.tab(tab_index, 'text')}")
        else:
            # Tab is not saved, add '*' to the tab name
            if not current_tab_name.endswith('*'):
                updated_tab_name = current_tab_name + '*'
                self.notebook.tab(self.tabs[tab_index].root, text=updated_tab_name)
                self.root.title(f"Yeongu Notes - {self.notebook.tab(tab_index, 'text')}")

    def rename_tab(self, tab_index, new_name, file_update=True, undo_redo=False):
        if 0 <= tab_index < len(self.tabs):
            new_name = new_name.rstrip('*')

            # Update the current_tab file attribute
            if self.tabs[tab_index].file and file_update and not self.tabs[tab_index].duplicated:
                file_path, extension = os.path.splitext(self.tabs[tab_index].file)
                new_file_path = os.path.join(os.path.dirname(file_path), f"{new_name}{extension}")

                if extension in ['.png']:
                    if not undo_redo:
                        self.tabs[tab_index].display('Cannot rename .png files')

                index = 0

                if not self.tabs[tab_index].safe_to_save:
                    while os.path.exists(new_file_path):
                        # Increment the index and update the file path
                        index += 1
                        file_name_match = re.match(r'^(.*?) \[\d+\]$', new_name)
                        if file_name_match:
                            base_name = file_name_match.group(1)
                            new_name = f"{base_name} [{index}]"
                        else:
                            new_name = f"{new_name} [{index}]"

                        directory = os.path.dirname(self.tabs[tab_index].file)
                        new_file_path = os.path.join(directory, f"{new_name}{extension}")

                    self.tabs[tab_index].safe_to_save = True

                os.rename(self.tabs[tab_index].file, new_file_path)
                self.tabs[tab_index].file = new_file_path
                self.tabs[tab_index].last_saved_file = new_file_path

            is_tab_saved = self.saved_tabs.get(tab_index, True)

            # Truncate the name if it exceeds 20 characters
            if new_name:
                if not is_tab_saved:
                    new_name = new_name + '*'
            else:
                return

            # Update the tab name in the notebook
            self.notebook.tab(self.tabs[tab_index].root, text=new_name)
            self.root.title(f"Yeongu Notes - {self.notebook.tab(tab_index, 'text')}")

            self.tabs[tab_index].display_path()

    def recolour_tab(self, tab_index, new_colour):
        self.current_tab = self.tabs[tab_index]
        self.current_tab.colour = new_colour

        try:
            # Attempt to retrieve color from settings
            tab_colour = getattr(settings, f"tab_{len(self.tabs)}_colour", None)

            # Check if the retrieved color is a valid hexadecimal value
            if tab_colour is not None and not re.match(r'^#(?:[0-9a-fA-F]{3}){1,2}$', tab_colour):
                raise ValueError("Invalid hex color format")

        except (AttributeError, ValueError):
            # If settings module is not available, or color is not a valid hex value, assign a random color
            tab_colour = "#{:06x}".format(random.randint(0, 0xFFFFFF))

        if tab_colour is None:
            # If the color is not defined in settings, assign a random color
            tab_colour = "#{:06x}".format(random.randint(0, 0xFFFFFF))

        hex_color = tab_colour.lstrip("#")
        rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

        # Calculate luminance (Y' value)
        luminance = (0.299 * rgb[0] + 0.587 * rgb[1] + 0.114 * rgb[2]) / 255

        # Set contrast color based on luminance
        self.current_tab.foreground_colour = "#ffffff" if luminance < 0.5 else "#000000"

        self.refresh_tabs()

        self.tabs[tab_index].display_time(fg=new_colour)

class Memento:
    def __init__(self, text_content, separator, cursor_position, strikethrough_ranges, misspelled_ranges, selection_range, scrollbar_info, x_scrollbar_info, tab_file, tab_name):
        self.text_content = text_content
        self.separator = separator
        self.cursor_position = cursor_position
        self.strikethrough_ranges = strikethrough_ranges
        self.misspelled_ranges = misspelled_ranges
        self.selection_range = selection_range
        self.scrollbar_info = scrollbar_info
        self.x_scrollbar_info = x_scrollbar_info
        self.tab_file = tab_file
        self.tab_name = tab_name

class Notepad():
    def __init__(self, **kwargs):
        self.root = tk.Tk()
        #self.root.overrideredirect(True)
        self.root.option_add("*Font", f"\"{settings.regular_font}\" 12")
        
        #Set window size
        #self.dark_title_bar()
        self.default_width = 1500
        self.default_height = 800
        #self.root.geometry(f"{self.default_width}x{self.default_height}+{self.root.winfo_screenwidth() // 2 - self.default_width // 2}+{self.root.winfo_screenheight() // 2 - self.default_height // 2}")
        self.root.attributes('-fullscreen', True)

        self.tab_controller = TabController(self.root, notepad=self)
        self.metadata_handler = TextMetadataHandler(notepad=self)
        self.root.tk_setPalette(background=settings.text_bg, foreground=settings.text_fg, activeBackground=settings.text_active_bg, activeForeground=settings.text_active_fg)

        # Set the window text
        self.root.title("Yeongu Notes")
        self.root.wm_iconbitmap(ico_path) 

        #Variables
        self.separator = ' '
        self.disable_memento_temporarily = False
        self.disable_autosave_temporarily = False
        self.is_mounted = False
        self.is_rainbow_cursor = False
        self.rainbow_stop = threading.Event()
        self.is_animation_running = False
        self.stop_animation_quick = False
        self.refresh_after_loading = True
        self.is_mounted_at_loading_start = None
        self.last_click_time = self.last_spacebar_click_time = datetime.now()
        self.click_cooldown = timedelta(seconds=0.2)
        self.insert_text = False
        self.reopen_after_exit = settings.reopen_after_exit
        self.security_drive = os.path.splitdrive(settings.security_folder)[0]
        self.disable_escape_app = False
        self.disable_dismount_when_exit_once = False
        self.recently_closed_tabs_paths = []
        self.mispelled_coords_queue = queue.Queue()

        # To make the textarea auto resizable
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.root.bind(settings.zoom_in, lambda event: self.zoom_in())
        self.root.bind(settings.zoom_out, lambda event: self.zoom_out())
        self.root.bind('<Control-MouseWheel>', self.zoom_with_scroll)
        self.root.protocol("WM_DELETE_WINDOW", lambda: self.save_and_exit(force_exit=True))

        self.is_initially_mounted = self.test_status()

        current_date = datetime.now()
        day_translation = {"Monday": "월", "Tuesday": "화", "Wednesday": "수", "Thursday": "목", "Friday": "금", "Saturday": "토", "Sunday": "일"}
        #self.korean_date = f"{current_date.year}년 {current_date.month}월 {current_date.day}일, ({day_translation[current_date.strftime('%A')]}요일)"
        #self.korean_date = f"{current_date.year}년 {current_date.month}월 {current_date.day}일 {day_translation[current_date.strftime('%A')]}요일"
        self.korean_date = f"{current_date.month}월 {current_date.day}일 {day_translation[current_date.strftime('%A')]}요일"

        try:
            previous_files, tab_on_focus_index = self.read_paths()

            encrypted_tabs = False

            if not self.is_mounted:
                indices_to_delete = []
                for i in range(len(previous_files)):
                    file = previous_files[i]
                    drive_letter = os.path.splitdrive(file)[0]

                    if drive_letter == self.security_drive:
                        encrypted_tabs = True
                    elif not os.path.exists(file):
                        # Update tab_on_focus_index based on the index of the non-existent file
                        if i >= tab_on_focus_index:
                            tab_on_focus_index -= 1
                        indices_to_delete.append(i)

                for i in indices_to_delete:
                    del previous_files[i]
            else:
                indices_to_delete = []
                for i in range(len(previous_files)):
                    file = previous_files[i]
                    drive_letter = os.path.splitdrive(file)[0]

                    if not os.path.exists(file):
                        # Update tab_on_focus_index based on the index of the non-existent file
                        if i >= tab_on_focus_index:
                            tab_on_focus_index -= 1
                        indices_to_delete.append(i)

                for i in indices_to_delete:
                    del previous_files[i]

            if tab_on_focus_index > len(previous_files) or tab_on_focus_index < 0:
                tab_on_focus_index = 0

            if encrypted_tabs:
                message = f"Mounting at security drive required to open all tabs.\nYou may skip this process and open the remaining tabs."
                result = CustomEntryDialog(self.root,title='Encrypted tabs', window_title='Security Error', message=message, bg=settings.text_active_bg, fg=settings.text_active_bg, entry=False, yes_no_prompt=True, yes='Encrypt drive', cancel=f'Skip tabs at {settings.security_documents_name}', height=220).result

                if result == 'cancel':
                    previous_files = [file for file in previous_files if os.path.splitdrive(file)[0] != self.security_drive]
                elif result == 'yes':
                    self.open_security_folder(init=True, show_loading=True)
                    
                    if not self.is_mounted:
                        previous_files = [file for file in previous_files if os.path.splitdrive(file)[0] != self.security_drive]
                else:
                    self.root.destroy()
                    return

            if previous_files:
                try:
                    for file in previous_files:
                        try:
                            self.open_file(path=file)
                        except:
                            pass
                except:
                    self.tab_controller.create_tab()
                    self.tab_controller.current_tab.text_area.mark_set("insert", f"{0}.{0}")
            elif cmd_path is None:
                self.tab_controller.create_tab()
                self.tab_controller.current_tab.text_area.mark_set("insert", f"{0}.{0}")

        except:
            self.tab_controller.create_tab()
            self.tab_controller.current_tab.text_area.mark_set("insert", f"{0}.{0}")

        if cmd_path:
            self.open_file(path=cmd_path)
            self.root.after(75, lambda: self.tab_controller.switch_tab(len(self.tab_controller.tabs) - 1)) 
        else:
            if tab_on_focus_index < 0:
                tab_on_focus_index = 0
            elif tab_on_focus_index > len(self.tab_controller.tabs) - 1:
                tab_on_focus_index = len(self.tab_controller.tabs) - 1
            self.root.after(75, lambda: self.tab_controller.switch_tab(tab_on_focus_index))
        
        self.root.after(150, lambda: self.save_memento(ignore_save=True))
        self.tab_controller.current_tab.text_area.focus_set()
        self.update_time()
        self.update_character_and_cursor_labels()
        self.root.deiconify()

        if settings.use_spell_checking:
            self.root.after(100, self.check_mispelled_coords_queue())

        # Start the autosave thread
        self.autosave_thread = threading.Thread(target=self.autosave_loop)
        self.autosave_thread.daemon = True  # This will make the thread exit when the main program exits
        self.autosave_thread.start()

        self.temp_file_thread = threading.Thread(target=self.monitor_temp_file, daemon=True)
        self.temp_file_thread.start()

        settings_window_instance = SettingsWindow(self.root)

        self.root.bind('<Control-z>', lambda event: self.undo())
        self.root.bind('<Control-y>', lambda event: self.redo())
        self.root.bind('<Escape>', lambda event: self.save_and_exit())
        self.root.bind('<Control-p>', lambda event, main_app=self: settings_window_instance.open_settings_window(main_app))
        self.root.bind('<F3>', lambda event, main_app=self: settings_window_instance.open_settings_window(main_app))
        self.root.bind('<Control-w>', lambda event: self.tab_controller.close_tab())
        self.root.bind('<F12>', lambda event: self.save_file_as())
        self.root.bind('<Control-Shift-S>', lambda event: self.save_file_as())
        self.root.bind('<F5>', lambda event: self.refresh_tabs())
        self.root.bind('<Control-s>', lambda event: self.save_file())
        self.root.bind('<Control-Alt-s>', lambda event: self.save_all_files())
        self.root.bind("<Control-Tab>", lambda event: self.tab_controller.switch_to_next_tab())
        self.root.bind("<Control-Shift-Tab>", lambda event: self.tab_controller.switch_to_previous_tab())
        self.root.bind('<Control-Shift-F4>', lambda event: self.exit_without_saving())
        self.root.bind('<Control-plus>', lambda event: self.zoom_in())
        self.root.bind('<Control-minus>', lambda event: self.zoom_out())
        self.root.bind('<Control-0>', lambda event: self.zoom())
        self.root.bind('<Control-m>', lambda event: self.open_security_folder(None))
        self.root.bind('<Alt-Shift-D>', lambda event: self.duplicate_and_break())
        self.root.bind('<Control-f>', lambda event: self.find_and_replace())
        self.root.bind('<Alt-Shift-S>', lambda event: self.apply_strikethrough())
        self.root.bind('<Insert>', lambda event: self.toggle_insert_text())
        self.root.bind('<F6>', lambda event: self.insert_current_datetime_at_cursor())
        self.root.bind('<F7>', lambda event: self.insert_current_date_at_cursor())
        self.root.bind('<F2>', lambda event: self.rename_current_tab())
        self.root.bind('<Control-k>w', lambda event: (self.rearrange_rows(), 'break'))
        self.root.bind('<Control-k>s', lambda event: (self.tab_controller.current_tab.convert_to_reorderable(), 'break'))
        self.root.bind('<Control-k>m', lambda event: (self.add_indices(1), 'break'))
        self.root.bind('<Control-k>p', lambda event: (self.add_indices(0), 'break'))
        self.root.bind('<Control-k>n', lambda event: (self.add_indices_prompt_start(), 'break'))
        self.root.bind('<Control-k>r', lambda event: (self.remove_indices(), 'break'))
        self.root.bind('<Control-g>', lambda event: self.go_to())
        self.root.bind("<F1>", lambda event: self.open_and_break(path=help_path))
        self.root.bind('<Control-Shift-R>', lambda event: self.invoke_read_only_button())
        self.root.bind('<F10>', lambda event: self.invoke_secured_button())
        self.root.bind('<Alt-a>', lambda event: self.invoke_autosave_button())
        self.root.bind('<Alt-m>', lambda event: self.invoke_metadata_button())
        self.root.bind('<Alt-s>', lambda event: self.invoke_spell_button())
        self.root.bind('<Alt-b>', lambda event: self.invoke_backup_button())
        self.root.bind('<F11>', lambda event: self.invoke_maximize_button())
        #self.root.bind("<Map>", lambda event: self.on_maximize())
        self.root.bind("<Control-b>", lambda event: self.backup_all_files())
        self.root.bind("<Control-Shift-W>", lambda event: self.close_all_but_current_tab())
        self.root.bind("<Control-Shift-T>", self.reopen_last_closed_tab)
        self.root.bind('<Alt-F7>', lambda event: self.tab_controller.current_tab.spell_check_everything())
        self.root.bind('<F4>', lambda event: self.tab_controller.current_tab.spell_check_everything())

        self.root.bind('<Control-Shift-F10>', lambda event: self.toggle_rainbow_cursor())
        self.root.bind('<Control-Shift-F5>', lambda event: self.tab_controller.current_tab.toggle_loading_animation(refresh_at_the_end=False))
        self.root.bind('<Control-Shift-F6>', lambda event: self.display(self.is_animation_running))

        # Note: These key bindings are specified for the opposite case due to the case sensitive nature of Tkinter bindings
        self.root.bind('<Control-Z>', lambda event: self.undo())
        self.root.bind('<Control-Y>', lambda event: self.redo())
        self.root.bind('<Control-P>', lambda event, main_app=self: settings_window_instance.open_settings_window(main_app))
        self.root.bind('<Control-W>', lambda event: self.tab_controller.close_tab())
        self.root.bind('<Control-S>', lambda event: self.save_file())
        self.root.bind('<Control-Alt-S>', lambda event: self.save_all_files())
        self.root.bind('<Control-M>', lambda event: self.open_security_folder(None))
        self.root.bind('<Control-F>', lambda event: self.find_and_replace())
        self.root.bind('<Control-K>W', lambda event: (self.rearrange_rows(), 'break'))
        self.root.bind('<Control-K>S', lambda event: (self.tab_controller.current_tab.convert_to_reorderable(), 'break'))
        self.root.bind('<Control-K>M', lambda event: (self.add_indices(1), 'break'))
        self.root.bind('<Control-K>P', lambda event: (self.add_indices(0), 'break'))
        self.root.bind('<Control-K>N', lambda event: (self.add_indices_prompt_start(), 'break'))
        self.root.bind('<Control-K>R', lambda event: (self.remove_indices(), 'break'))
        self.root.bind('<Control-G>', lambda event: self.go_to())
        self.root.bind('<Alt-M>', lambda event: self.invoke_metadata_button())
        self.root.bind('<Alt-A>', lambda event: self.invoke_autosave_button())
        self.root.bind("<Control-B>", lambda event: self.backup_all_files())
        self.root.bind('<Alt-S>', lambda event: self.invoke_spell_button())
        self.root.bind('<Alt-B>', lambda event: self.invoke_backup_button())

    def run(self):
        self.root.update_idletasks()
        self.root.focus_force()
        self.root.mainloop()

    def on_maximize(self):
        if not hasattr(self, "triggered_time"):
            self.triggered_time = 0
        
        current_time = time.time()
        if current_time - self.triggered_time > 0.5:
            if self.root.state() == 'zoomed':
                # Window is maximized
                pyautogui.click(x=1826, y=16)
                self.invoke_maximize_button()
                self.triggered_time = current_time

    def handle_key_event(self, event, cut_paste=False):
        if self.tab_controller.current_tab.reorderable:
            return
        
        if cut_paste:
            self.save_memento()
            self.root.after(100, self.decide_scrollbar_toggle)
            thread = threading.Thread(target=lambda: self.mispelled_coords_queue.put(self.tab_controller.current_tab.spell_check(range=settings.spell_check_typing_range, thread=True, ignore_current_word=False)))
            self.root.after(1, thread.start())

            return

        if ((event.keysym in ['Return', 'space', 'BackSpace', 'Delete'] or
            (event.char.isprintable() and event.char) or
            (event.keysym == 'Tab' and event.state == 8))):

            self.save_memento()

            if settings.get_title_from_text:
                first_non_empty_line = self.tab_controller.current_tab.text_area.search(r'\S', '1.0', stopindex='end', regexp=True, count=1)
                if first_non_empty_line:
                    if '===' in self.tab_controller.current_tab.text_area.get(first_non_empty_line, f"{first_non_empty_line} lineend"):
                        self.root.after(100, self.extract_content_between_equals)

            self.root.after(100, self.decide_scrollbar_toggle)
            if not event.keysym in ['Return', 'BackSpace', 'Delete'] and ((self.mispelled_coords_queue.empty() and self.can_click()) or (event.keysym in ['space'] and self.can_click_spacebar())):
                thread = threading.Thread(target=lambda: self.mispelled_coords_queue.put(self.tab_controller.current_tab.spell_check(range=settings.spell_check_typing_range, thread=True, ignore_current_word=True if event.keysym == 'space' else False)))
                self.root.after(1, thread.start())

        if self.insert_text and event.char and event.char.isprintable():
            cursor_position = self.tab_controller.current_tab.text_area.index("insert")
            next_char_index = cursor_position + "+1c"
            
            if cursor_position != " lineend" and self.tab_controller.current_tab.text_area.get(cursor_position) != '\n':
                self.tab_controller.current_tab.text_area.delete(cursor_position, next_char_index)

        if event.char in ['\'', '\"', '(', '[', '{', '<'] and settings.auto_quotes:
            self.save_memento()
            event = self.add_quotes_around_word(event)

            if event == 'dont_break':
                return
            else:
                return "break"

    def check_mispelled_coords_queue(self):
        if not self.mispelled_coords_queue.empty():
            coords = self.mispelled_coords_queue.get()
            self.tab_controller.current_tab.apply_spell_underline(coords)
        self.root.after(100, self.check_mispelled_coords_queue)

    def add_quotes_around_word(self, event):
        current_tab = self.tab_controller.current_tab

        if not current_tab.text_area.tag_ranges("sel"):
            sel_start = sel_end = current_tab.text_area.index("insert")

            # Check if there is non-whitespace text before and after the cursor
            if event.char in ['\'', '\"']: #For quotes both before and after characters need to be whitespaces
                if not current_tab.text_area.get(current_tab.text_area.index("insert - 1 char")).isspace() or not current_tab.text_area.get(current_tab.text_area.index("insert")).isspace():
                    return 'dont_break'
            else: #For parenthesis and such, only the next character needs to be a whitespace
                if not current_tab.text_area.get(current_tab.text_area.index("insert")).isspace():
                    return 'dont_break'

            word_start = sel_start
            word_end = sel_end

            quoted_word = f'{event.char}{self.get_opposite_parenthesis(event.char)}'
            len_quoted_word = 1
        else:
            sel_start, sel_end = current_tab.text_area.tag_ranges("sel")

            word_start = sel_start
            word_end = sel_end

            if not word_start:
                word_start = "1.0"

            if not word_end:
                word_end = "end"

            selected_word = current_tab.text_area.get(word_start, word_end)

            quoted_word = f'{event.char}{selected_word}{self.get_opposite_parenthesis(event.char)}'
            len_quoted_word = len(quoted_word)

        current_tab.text_area.delete(word_start, word_end)
        current_tab.text_area.insert(word_start, quoted_word)

        new_cursor_position = f'{word_start}+{len_quoted_word}c'
        current_tab.text_area.mark_set("insert", new_cursor_position)
        current_tab.text_area.see(new_cursor_position)

        #Restore selection range
        current_tab.text_area.tag_remove(tk.SEL, "1.0", tk.END)
        if current_tab.text_area.index(word_start).split('.')[0] == current_tab.text_area.index(word_end).split('.')[0]:
            current_tab.text_area.tag_add(tk.SEL, f'{str(word_start)}+1c', f'{str(word_end)}+1c')
        else:
            current_tab.text_area.tag_add(tk.SEL, f'{str(word_start)}+1c', f'{str(word_end)}')

    def get_opposite_parenthesis(self, parenthesis):
        # Define a mapping of open to close parentheses
        parenthesis_mapping = {'\'': '\'', '\"': '\"', '(': ')', '[': ']', '{': '}', '<': '>'}
        # Return the opposite parenthesis
        return parenthesis_mapping.get(parenthesis, '')

    def minimize(self):
        self.root.iconify()

    def maximize(self):
        if self.root.attributes('-fullscreen'):
            # Exit fullscreen
            self.root.attributes('-fullscreen', False)
            dark_title_bar(self.root)

            self.root.geometry(f"{self.default_width}x{self.default_height}+{self.root.winfo_screenwidth() // 2 - self.default_width // 2}+{self.root.winfo_screenheight() // 2 - self.default_height // 2}")

            if settings.navigation_buttons:
                if hasattr(self.tab_controller, 'close_button'):
                    self.tab_controller.close_button.place_forget()
                if hasattr(self.tab_controller, 'maximize_button'):
                    self.tab_controller.maximize_button.place_forget()
                if hasattr(self.tab_controller, 'minimize_button'):
                    self.tab_controller.minimize_button.place_forget()

                self.tab_controller.nav_spacer_label.config(padx=0)

            for tab in self.tab_controller.tabs:
                tab.icon_button.place_forget()
                tab.icon_spacer_label.config(padx=0)

            self.tab_controller.current_tab.loading_bar_label.place(x=-1924, y=-2)
            
            self.decide_scrollbar_toggle()
        else:
            self.root.attributes('-fullscreen', True)

            if settings.navigation_buttons:
                # Place the buttons with customized appearance
                self.tab_controller.close_button.place(x=self.root.winfo_screenwidth() - 29, y=0)
                self.tab_controller.maximize_button.place(x=self.root.winfo_screenwidth() - 63, y=0)
                self.tab_controller.minimize_button.place(x=self.root.winfo_screenwidth() - 97, y=0)
                self.tab_controller.nav_spacer_label.config(padx=76)

            for tab in self.tab_controller.tabs:
                tab.icon_button.place(x=0, y=0)
                tab.icon_spacer_label.config(padx=16)

            self.tab_controller.current_tab.loading_bar_label.place(x=-1924, y=-2)

            self.decide_scrollbar_toggle()

    def refresh_tabs(self):
        if not self.can_click():
            return
        self.tab_controller.refresh_tabs()

    def can_click(self):
        last_click_time = self.last_click_time
        current_time = datetime.now()
        self.last_click_time = current_time
        return current_time - last_click_time > self.click_cooldown

    def can_click_spacebar(self):
        last_spacebar_click_time = self.last_spacebar_click_time
        current_time = datetime.now()
        self.last_spacebar_click_time = current_time
        return current_time - last_spacebar_click_time > self.click_cooldown

    def save_memento(self, ignore_save=False, event=None):
        if self.disable_memento_temporarily:
            return
        
        #self.display(f'{len(self.tab_controller.current_tab.memento_stack) + 1} mementos saved ')
        #print(f'{len(self.tab_controller.current_tab.memento_stack) + 1} mementos saved ')

        # Get the current tab before saving the memento
        current_tab = self.tab_controller.current_tab
        
        # Set saved state to False for the current tab
        tab_index = self.tab_controller.notebook.index(self.tab_controller.notebook.select())

        # Save the current state of the text, separator, and cursor position
        current_text = current_tab.text_area.get(1.0, tk.END)
        cursor_position = current_tab.text_area.index("insert")
        strikethrough_ranges = [str(coord) for coord in self.tab_controller.current_tab.text_area.tag_ranges("strikethrough")]
        misspelled_ranges = [str(coord) for coord in self.tab_controller.current_tab.text_area.tag_ranges("misspelled")]
        selection_range = current_tab.text_area.tag_ranges("sel")
        scrollbar_info = {"vertical_scroll_position": current_tab.ctk_textbox_scrollbar.get()[0], "is_scrollbar_shown": self.tab_controller.current_tab.ctk_textbox_scrollbar.cget("width") != 0,}
        x_scrollbar_info = {"horizontal_scroll_position": current_tab.ctk_x_textbox_scrollbar.get()[0], "is_scrollbar_shown": current_tab.ctk_x_textbox_scrollbar.cget("height") != 0} if hasattr(current_tab, 'ctk_x_textbox_scrollbar') else None
        tab_file = current_tab.file
        tab_name = self.tab_controller.notebook.tab(self.tab_controller.tabs[tab_index].root, "text")
        memento = Memento(current_text, self.separator, cursor_position, strikethrough_ranges, misspelled_ranges, selection_range, scrollbar_info, x_scrollbar_info, tab_file, tab_name)

        # Save the Memento to the current tab's stack
        current_tab.memento_stack.append(memento)

        if not ignore_save:
            if self.tab_controller.saved_tabs.get(tab_index, True):
                self.tab_controller.update_tab_name_indicator(tab_index, False)  
         
            self.tab_controller.saved_tabs[tab_index] = False

        # Check if the maximum number of undo steps is reached
        if len(current_tab.memento_stack) > settings.max_undo_steps:
            # Remove the oldest undo step
            current_tab.memento_stack.pop(0)

    def undo(self):
        current_tab = self.tab_controller.current_tab

        if current_tab.read_only:
            return

        if current_tab.reorderable:
            current_tab.text_area.undo()
            return

        if len(self.tab_controller.current_tab.memento_stack) > 1:
            tab_index = self.tab_controller.notebook.index(self.tab_controller.notebook.select())

            # Save the current state to the redo stack
            redo_text = current_tab.text_area.get(1.0, tk.END)
            redo_cursor_position = current_tab.text_area.index("insert")
            redo_strikethrough_ranges = [str(coord) for coord in current_tab.text_area.tag_ranges("strikethrough")]
            redo_misspelled_ranges = [str(coord) for coord in current_tab.text_area.tag_ranges("misspelled")]
            redo_selection_range = current_tab.text_area.tag_ranges("sel")
            redo_scrollbar_info = {"vertical_scroll_position": current_tab.ctk_textbox_scrollbar.get()[0], "is_scrollbar_shown": current_tab.ctk_textbox_scrollbar.cget("width") != 0,}
            redo_x_scrollbar_info = {"horizontal_scroll_position": current_tab.ctk_x_textbox_scrollbar.get()[0], "is_scrollbar_shown": current_tab.ctk_x_textbox_scrollbar.cget("height") != 0} if hasattr(current_tab, 'ctk_x_textbox_scrollbar') else {"horizontal_scroll_position": 0, "is_scrollbar_shown": False}
            redo_tab_file = current_tab.file
            redo_tab_name = self.tab_controller.notebook.tab(self.tab_controller.tabs[tab_index].root, "text")
            redo_memento = Memento(redo_text, self.separator, redo_cursor_position, redo_strikethrough_ranges, redo_misspelled_ranges, redo_selection_range, redo_scrollbar_info, redo_x_scrollbar_info, redo_tab_file, redo_tab_name)
            current_tab.redo_stack.append(redo_memento)

            previous_memento = current_tab.memento_stack[-1]

            if self.separator != previous_memento.separator:
                self.separator = previous_memento.separator
                self.display(f'Separator reverted to: {self.separator}')

            # Get the previous and current text content
            previous_text_content = previous_memento.text_content
            current_text_content = current_tab.text_area.get(1.0, tk.END)

            # Split the text content into lines
            previous_lines = previous_text_content.split('\n')
            current_lines = current_text_content.split('\n')

            line, char = map(int, previous_memento.cursor_position.split('.'))

            def restore_scroll_position():
                current_tab.toggle_scrollbar_visibility(enable=previous_memento.scrollbar_info["is_scrollbar_shown"])
                current_tab.text_area.yview_moveto(previous_memento.scrollbar_info["vertical_scroll_position"])

                if not current_tab.wrap and hasattr(current_tab, 'ctk_x_textbox_scrollbar'):
                    current_tab.toggle_x_scrollbar_visibility(enable=previous_memento.x_scrollbar_info["is_scrollbar_shown"])
                    current_tab.text_area.xview_moveto(previous_memento.x_scrollbar_info["horizontal_scroll_position"])

            # Check if the number of lines is the same
            if len(previous_lines) == len(current_lines):
                # Iterate through lines and replace if different
                for i in range(len(previous_lines)):
                    if previous_lines[i] != current_lines[i]:
                        current_tab.text_area.replace(f"{i + 1}.0", f"{i + 1}.end", previous_lines[i])

            else:
                if not current_tab.wrap:
                    if len(previous_lines) > len(current_lines):
                        diff = len(current_lines) - len(previous_lines)
                        for _ in range(diff):
                            current_tab.text_area.insert(tk.END, "\n")

                    elif len(previous_lines) < len(current_lines):
                        diff = len(previous_lines) - len(current_lines)
                        for _ in range(diff):
                            current_tab.text_area.delete(tk.END + "-1l", tk.END)

                    current_tab.text_area.replace(1.0, tk.END, previous_text_content[:-1])

                    restore_scroll_position()

                else:

                    max_lines = current_tab.text_area.winfo_height() // (current_tab.zoom_factor * 22) # Adjust the multiplier as needed
                    diff = len(current_lines) - len(previous_lines)

                    # Replace the entire text content with the one from the previous memento
                    current_tab.text_area.replace(1.0, tk.END, previous_text_content[:-1])

                    if abs(diff) > max_lines:
                        restore_scroll_position()

            # Restore the selection range
            current_tab.text_area.tag_remove(tk.SEL, "1.0", tk.END)
            if previous_memento.selection_range:
                # Unpack the tuple into separate arguments
                start, end = previous_memento.selection_range
                current_tab.text_area.tag_add(tk.SEL, start, end)

            # Clear all existing "strikethrough" and "misspelled" tags
            current_tab.text_area.tag_remove("strikethrough", "1.0", tk.END)
            current_tab.text_area.tag_remove("misspelled", "1.0", tk.END)

            if previous_memento.strikethrough_ranges:
                current_tab.text_area.tag_add("strikethrough", *previous_memento.strikethrough_ranges)

            if previous_memento.misspelled_ranges:
                current_tab.text_area.tag_add("misspelled", *previous_memento.misspelled_ranges)


            if not current_tab.duplicated:
                if self.tab_controller.notebook.tab(self.tab_controller.tabs[tab_index].root, "text") != previous_memento.tab_name:
                    self.tab_controller.rename_tab(tab_index, previous_memento.tab_name, undo_redo=True)

            self.decide_scrollbar_toggle()

            if not current_tab.duplicated:
                current_tab.file = previous_memento.tab_file
                current_tab.display_path()

            if self.tab_controller.saved_tabs.get(tab_index, True):
                self.tab_controller.update_tab_name_indicator(tab_index, False)

            current_tab.memento_stack.pop()

    def redo(self):
        if self.tab_controller.current_tab.read_only:
            return
        
        if self.tab_controller.current_tab.reorderable:
            self.tab_controller.current_tab.text_area.redo()
            return
        
        if self.tab_controller.current_tab.redo_stack:
            current_tab = self.tab_controller.current_tab
            tab_index = self.tab_controller.notebook.index(self.tab_controller.notebook.select())

            # Save the current state to the undo stack
            current_text = current_tab.text_area.get(1.0, tk.END)
            cursor_position = current_tab.text_area.index("insert")
            strikethrough_ranges = [str(coord) for coord in self.tab_controller.current_tab.text_area.tag_ranges("strikethrough")]
            misspelled_ranges = [str(coord) for coord in self.tab_controller.current_tab.text_area.tag_ranges("misspelled")]
            selection_range = current_tab.text_area.tag_ranges("sel")
            scrollbar_info = {"vertical_scroll_position": current_tab.ctk_textbox_scrollbar.get()[0], "is_scrollbar_shown": self.tab_controller.current_tab.ctk_textbox_scrollbar.cget("width") != 0,}
            x_scrollbar_info = {"horizontal_scroll_position": current_tab.ctk_x_textbox_scrollbar.get()[0], "is_scrollbar_shown": current_tab.ctk_x_textbox_scrollbar.cget("height") != 0} if hasattr(current_tab, 'ctk_x_textbox_scrollbar') else {"horizontal_scroll_position": 0, "is_scrollbar_shown": False}
            tab_file = current_tab.file
            tab_name = self.tab_controller.notebook.tab(self.tab_controller.tabs[tab_index].root, "text")            
            memento = Memento(current_text, self.separator, cursor_position, strikethrough_ranges, misspelled_ranges, selection_range, scrollbar_info, x_scrollbar_info, tab_file, tab_name)
            self.tab_controller.current_tab.memento_stack.append(memento)

            redo_memento = current_tab.redo_stack[-1]

            # Remove the oldest redo step if the limit is reached
            if len(self.tab_controller.current_tab.redo_stack) > settings.max_redo_steps:
                self.tab_controller.current_tab.redo_stack.pop(0)

            if self.separator != redo_memento.separator:
                self.separator = redo_memento.separator
                self.display(f'Separator reverted to: {self.separator}')

            # Get the previous and current text content
            previous_text_content = redo_memento.text_content
            current_text_content = current_tab.text_area.get(1.0, tk.END)

            # Split the text content into lines
            previous_lines = previous_text_content.split('\n')
            current_lines = current_text_content.split('\n')

            line, char = map(int, redo_memento.cursor_position.split('.'))

            def restore_scroll_position():
                current_tab.toggle_scrollbar_visibility(enable=redo_memento.scrollbar_info["is_scrollbar_shown"])
                current_tab.text_area.yview_moveto(redo_memento.scrollbar_info["vertical_scroll_position"])

                if not current_tab.wrap and hasattr(current_tab, 'ctk_x_textbox_scrollbar'):
                    current_tab.toggle_x_scrollbar_visibility(enable=redo_memento.x_scrollbar_info["is_scrollbar_shown"])
                    current_tab.text_area.xview_moveto(redo_memento.x_scrollbar_info["horizontal_scroll_position"])

            # Check if the number of lines is the same
            if len(previous_lines) == len(current_lines):
                # Iterate through lines and replace if different
                for i in range(len(previous_lines)):
                    if previous_lines[i] != current_lines[i]:
                        current_tab.text_area.replace(f"{i + 1}.0", f"{i + 1}.end", previous_lines[i])

            else:
                if not current_tab.wrap:
                    if len(previous_lines) > len(current_lines):
                        diff = len(current_lines) - len(previous_lines)
                        for _ in range(diff):
                            current_tab.text_area.insert(tk.END, "\n")

                    elif len(previous_lines) < len(current_lines):
                        diff = len(previous_lines) - len(current_lines)
                        for _ in range(diff):
                            current_tab.text_area.delete(tk.END + "-1l", tk.END)

                    current_tab.text_area.replace(1.0, tk.END, previous_text_content[:-1])

                    restore_scroll_position()

                else:

                    max_lines = current_tab.text_area.winfo_height() // (current_tab.zoom_factor * 22) # Adjust the multiplier as needed
                    diff = len(current_lines) - len(previous_lines)

                    # Replace the entire text content with the one from the previous memento
                    current_tab.text_area.replace(1.0, tk.END, previous_text_content[:-1])

                    if abs(diff) > max_lines:
                        restore_scroll_position()

            # Restore the selection range
            self.tab_controller.current_tab.text_area.tag_remove(tk.SEL, "1.0", tk.END)
            if redo_memento.selection_range:
                # Unpack the tuple into separate arguments
                start, end = redo_memento.selection_range
                self.tab_controller.current_tab.text_area.tag_add(tk.SEL, start, end)

            # Clear all existing "strikethrough" and "misspelled" tags
            current_tab.text_area.tag_remove("strikethrough", "1.0", tk.END)
            current_tab.text_area.tag_remove("misspelled", "1.0", tk.END)

            if redo_memento.strikethrough_ranges:
                current_tab.text_area.tag_add("strikethrough", *redo_memento.strikethrough_ranges)

            if redo_memento.misspelled_ranges:
                current_tab.text_area.tag_add("misspelled", *redo_memento.misspelled_ranges)

            # Set the cursor back to the saved position
            self.tab_controller.current_tab.text_area.mark_set("insert", f"{line}.{char}")

            if not current_tab.duplicated:
                if self.tab_controller.notebook.tab(self.tab_controller.tabs[tab_index].root, "text") != redo_memento.tab_name:
                    self.tab_controller.rename_tab(tab_index, redo_memento.tab_name, undo_redo=True)

            self.decide_scrollbar_toggle()

            if not current_tab.duplicated:
                current_tab.file = redo_memento.tab_file
                current_tab.display_path()

            if self.tab_controller.saved_tabs.get(tab_index, True):
                self.tab_controller.update_tab_name_indicator(tab_index, False)  

            # Pop the state from the redo stack
            redo_memento = self.tab_controller.current_tab.redo_stack.pop()

    def decide_scrollbar_toggle(self):
        if self.tab_controller.current_tab.reorderable:
            return

        current_tab = self.tab_controller.current_tab
        
        if int(self.tab_controller.current_tab.text_area.index("insert").split('.')[0]) == 1:
            # Attempt to scroll up by one pixel and check if the yview position changes
            current_tab.text_area.yview_scroll(1, 'pixels')
            yview_after_scroll_up = current_tab.text_area.yview()
            current_tab.text_area.yview_scroll(-1, 'pixels')
            # Attempt to scroll down by one pixel and check if the yview position changes
            yview_after_scroll_down = current_tab.text_area.yview()

        else:
            # Attempt to scroll up by one pixel and check if the yview position changes
            yview_after_scroll_up = current_tab.text_area.yview()
            # Attempt to scroll down by one pixel and check if the yview position changes
            current_tab.text_area.yview_scroll(-1, 'pixels')
            yview_after_scroll_down = current_tab.text_area.yview()
            current_tab.text_area.yview_scroll(1, 'pixels')

        # Toggle the scrollbar visibility based on the result
        if yview_after_scroll_up != yview_after_scroll_down:
            current_tab.toggle_scrollbar_visibility(enable=True)
        else:
            current_tab.toggle_scrollbar_visibility(enable=False)

        if not current_tab.wrap:
            self.decide_x_scrollbar_toggle()

    def decide_x_scrollbar_toggle(self):
        current_tab = self.tab_controller.current_tab

        # Attempt to scroll up by one pixel and check if the yview position changes
        current_tab.text_area.xview_scroll(-1, 'pixels')
        xview_after_scroll_up = current_tab.text_area.xview()
        current_tab.text_area.xview_scroll(1, 'units')

        # Attempt to scroll down by one pixel and check if the yview position changes
        current_tab.text_area.xview_scroll(1, 'pixels')
        xview_after_scroll_down = current_tab.text_area.xview()
        current_tab.text_area.xview_scroll(-1, 'units')

        # Toggle the scrollbar visibility based on the result
        if xview_after_scroll_up != xview_after_scroll_down:
            current_tab.toggle_x_scrollbar_visibility(enable=True)
        else:
            current_tab.toggle_x_scrollbar_visibility(enable=False)

    def zoom_in(self):
        self.tab_controller.current_tab.zoom_factor *= 1.1
        self.update_font_size()
        self.decide_scrollbar_toggle()

    def zoom_out(self):
        if self.tab_controller.current_tab.zoom_factor / 1.1 >= 0.1:  # Ensures zoom is not lower than 10%
            self.tab_controller.current_tab.zoom_factor /= 1.1
        else:
            self.tab_controller.current_tab.zoom_factor = 0.1  # Set zoom factor to 10% if it would go lower
        self.update_font_size()
        self.decide_scrollbar_toggle()

    def zoom(self, zoom_factor = 1.0):
        self.tab_controller.current_tab.zoom_factor = zoom_factor
        self.update_font_size()
        self.decide_scrollbar_toggle()

    def zoom_refresh(self):
        self.update_font_size()
        self.decide_scrollbar_toggle()

    def display(self, info='', delay_ms=5000, fg=settings.ui_fg, tab_index=None):
        if tab_index is None:
            self.tab_controller.current_tab.display(info, delay_ms, fg=fg)
        else:
            self.tab_controller.tabs[tab_index].display(info, delay_ms, fg=fg)

    def display_all(self, info='', delay_ms=5000, fg=settings.ui_fg):
        for tab in self.tab_controller.tabs:
            tab.display(info, delay_ms, fg=fg)

    def display_time(self, fg=settings.ui_fg):
        for tab in self.tab_controller.tabs:
            tab.display_time(fg=fg)

    def update_character_and_cursor_labels(self, event=None):
        if self.tab_controller.current_tab.reorderable:
            return

        text_widget = self.tab_controller.current_tab.text_area
        cursor_position = text_widget.index(tk.INSERT)
        line, col = map(int, cursor_position.split('.'))
        text = f'Ln {line}, Col {col}'
        self.tab_controller.cursor_label.config(text=text)
        # Calculate line and column
        line, col = cursor_position.split('.')

        # Count characters and lines
        characters = len(self.tab_controller.current_tab.text_area.get('1.0', 'end-1c'))
        lines = len(self.tab_controller.current_tab.text_area.get('1.0', 'end').split('\n')) - 1

        plural_lines = 's'
        if lines == 1:
            plural_lines = ''

        # If text is selected, calculate selected characters
        if text_widget.tag_ranges(tk.SEL):
            start, end = text_widget.tag_ranges(tk.SEL)
            selected_characters = len(text_widget.get(start, end))
            if selected_characters > characters:
                selected_characters = characters
            text = f'{format(selected_characters, ',')} of {format(characters, ',')} characters  |  {format(lines, ',')} line{plural_lines}'
        else:
            plural_char = 's'
            if characters == 1:
                plural_char = ''
            text = f'{format(characters, ',')} character{plural_char}  |  {format(lines, ',')} line{plural_lines}'

        # Update the label
        self.tab_controller.character_label.config(text=text)

        self.update_keyboard_layout_label()

    def extract_content_between_equals(self):
        text_widget = self.tab_controller.current_tab.text_area

        # Get the content of the text widget
        content = text_widget.get('1.0', 'end-1c')

        # Split the content into lines
        lines = content.split('\n')

        # Find the first non-blank line index
        first_non_blank_line_index = next((i for i, line in enumerate(lines) if line.strip()), None)

        # If there's a non-blank line, search for the pattern in it
        if first_non_blank_line_index is not None:
            first_non_blank_line = lines[first_non_blank_line_index]
            pattern = re.compile(r'===\s*([^=]+)\s*===')
            match = pattern.search(first_non_blank_line)

            if match:
                suggested_title = self.tab_controller.notebook.tab(self.tab_controller.current_tab.root, "text").rstrip('*')

                # Use regular expression to separate the title and the [n]
                suggested_title = re.sub(r'\s*(\[\d+\])?$', '', suggested_title)

                extracted_content = match.group(1).strip()
                if extracted_content != suggested_title:
                    suggested_title = extracted_content
                    self.tab_controller.current_tab.safe_to_save = False
                    try:
                        self.tab_controller.rename_tab(self.tab_controller.notebook.index(self.tab_controller.notebook.select()), suggested_title)
                    except OSError:
                        self.display("Filenames can't contain characters such as  \\ / : * ? \" < > |", fg='orange')

    def update_zoom_label(self):
        percentage = round(self.tab_controller.current_tab.zoom_factor * 100)
        text = f'{percentage}%'
        self.tab_controller.zoom_label.config(text=text)

    def zoom_with_scroll(self, event):
        if self.tab_controller.current_tab.reorderable:
            return
        # Check if the scroll event is triggered with the Ctrl key
        if event.state & 4:
            if event.delta > 0:
                self.zoom_in()
            elif event.delta < 0:
                self.zoom_out()

    def update_font_size(self):
        # Calculate the new font size based on the zoom factor
        new_font_size = int(settings.font_size * self.tab_controller.current_tab.zoom_factor)

        # Set font size based on the updated size
        if self.tab_controller.current_tab.font:
            text_font = font.Font(family=self.tab_controller.current_tab.font, size=new_font_size)
        else:
            text_font = font.Font(family=settings.text_font, size=new_font_size)
        self.tab_controller.current_tab.text_area.configure(font=text_font)

        self.update_zoom_label()

        if self.tab_controller.current_tab.read_only:
            self.decide_scrollbar_toggle()

    def show_about(self, event=None):
        about_text = textwrap.dedent(f"""
        Yeongu Notes
        Version: {version}

        Yeongu Notes is a simple, open source text editor created to simplify the edition of .txt files. Adding an extra layer of security.

        
        Key features:

        Costumizability: You can easily change the colours of the UI and different tabs, keep up where you left off, make your files read-only, autosave files, backup files or keep it simple if you wish!

        Simple edit tools: The editor allows to easily write indices to each line or to remove them and you can also easily rearange the position of rows in the text.
                 
        Security: If you have an encypted storage location, and a way to mount it using cmd commands, this can be integrated in the app. Allowing to directly save files to a secure location, unmounting the drive once the editor is closed and preventing the user from accidentally saving secured files somewhere unsafe.

        Images: The editor allows to read and write to PNG images' metadata.


        Yeongu Notes © 2024 by Nuno Seren is licensed under CC BY-NC-SA 4.0

        You may contact me through namyeongmi3@gmail.com""")

        showinfo("About", about_text)

        return 'break'

    def backup_all_files(self):
        if not settings.use_file_backup:
            return
        
        self.display_all('Backing up all backup enabled tabs')
        for tab_index, tab in enumerate(self.tab_controller.tabs):
            if tab.backup:
                self.backup_file(tab_index=tab_index)

    def backup_file(self, tab_index=None):
        if not settings.use_file_backup:
            return

        if tab_index is None:
            current_tab = self.tab_controller.current_tab
            tab_index = self.tab_controller.notebook.index(self.tab_controller.notebook.select())
        else:
            current_tab = self.tab_controller.tabs[tab_index]

        tab_name = self.tab_controller.notebook.tab(tab_index, "text").rstrip('*')
        text_content = current_tab.text_area.get(1.0, tk.END)[:-1]

        base_folder = settings.backup_folder_path if not current_tab.secured else settings.secure_backup_folder_path
        timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
        backup_file = os.path.join(base_folder, f"{timestamp}_{tab_name}.txt")

        # Check if the path already exists
        while os.path.exists(backup_file):
            # Append a suffix to the filename
            timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
            backup_file = os.path.join(base_folder, f"{timestamp}_{tab_name}.txt")

        try:
            with open(backup_file, "w", encoding="utf-8") as file:
                file.write(text_content)
        except Exception as e:
            self.display_all(f'There was an error backing up a file: {e}')

        metadata = {
            "colour": current_tab.colour,
            "foreground_colour": current_tab.foreground_colour,
            "autosave": current_tab.autosave,
            "secured": current_tab.secured,
            "cursor_position": str(current_tab.text_area.index("insert")),
            "selection": [str(coord) for coord in current_tab.text_area.tag_ranges("sel")],
            "zoom_level": current_tab.zoom_factor,
            "vertical_scroll_position": current_tab.ctk_textbox_scrollbar.get()[0],  # Assuming ctk_textbox_scrollbar is a ttk.Scrollbar
            "is_vertical_scrollbar_shown": self.tab_controller.current_tab.ctk_textbox_scrollbar.cget("width") != 0,
            "horizontal_scroll_position": current_tab.ctk_x_textbox_scrollbar.get()[0] if hasattr(current_tab, 'ctk_x_textbox_scrollbar') else 0,
            "is_horizontal_scrollbar_shown": current_tab.ctk_x_textbox_scrollbar.cget("height") != 0 if hasattr(current_tab, 'ctk_x_textbox_scrollbar') else False,
            "strikethrough": [str(coord) for coord in current_tab.text_area.tag_ranges("strikethrough")],
            "wrap": current_tab.wrap,
            "backup": current_tab.backup,
            "font": current_tab.font,
            "spell": current_tab.spell,
        }

        current_tab.metadata_handler.write_metadata(backup_file, metadata)

        self.display('File backed up successfully', delay_ms=2000, tab_index=tab_index)

    def convert_from_json(self, dictionary={}):
        insert_at_the_end = False

        if not dictionary:
            try:
                dictionary = ast.literal_eval(self.tab_controller.current_tab.text_area.get(1.0, tk.END)[:-1])
            except:
                self.display('Invalid JSON format', fg='red')
                self.tab_controller.current_tab.png_json = True
                self.tab_controller.current_tab.convert_json_button.invoke_no_command()
                return

            insert_at_the_end = True

        def check_separator(sep):
            for key, value in dictionary.items():
                if sep in str(key) or sep in str(value):
                    return True
            return False
        
        separator = "։"  # Initial separator
        while True:
            if check_separator(separator):
                separator += "։"  # Add a space after ":" if found in any key or value
            else:
                break

        formatted_string = ""
        for key, value in dictionary.items():
            formatted_string += f"{key}{separator}\n{value}\n\n\n"

        self.tab_controller.current_tab.png_var_no = len(dictionary)

        if insert_at_the_end:
            self.tab_controller.current_tab.text_area.delete(1.0, tk.END)
            self.tab_controller.current_tab.text_area.insert(1.0, formatted_string[:-3])
            self.save_memento()

            self.decide_scrollbar_toggle()

        return formatted_string[:-3]

    def convert_to_json(self, formatted_string=None):        
        insert_at_the_end = False

        if formatted_string is None:
            formatted_string = self.tab_controller.current_tab.text_area.get(1.0, tk.END)[:-1]
            insert_at_the_end = True

        def check_separator(sep):
            return sep in formatted_string

        dictionary = {}
        separator = "։"  # Initial separator
        while check_separator(separator):
            separator += "։"  # Add a space after ":" until it's not found in the formatted string

        separator = separator[:-1]

        while formatted_string:
            index = formatted_string.find(separator)
            if index != -1:
                # Extract key
                key_index = index
                while key_index >= 0 and formatted_string[key_index] != "\n":
                    key_index -= 1
                if key_index >= 0:
                    key = formatted_string[key_index + 1:index]
                else:
                    key = formatted_string[:index]

                # Extract value
                value_index = index + len(separator)
                value_end_index = formatted_string.find("\n\n\n", value_index)
                if value_end_index != -1:
                    value = formatted_string[value_index:value_end_index][1:]
                    formatted_string = formatted_string[value_end_index + 2:]
                else:
                    value = formatted_string[value_index:][1:]
                    formatted_string = ""

                dictionary[key] = value
            else:
                break

        if insert_at_the_end:
            if len(dictionary) < self.tab_controller.current_tab.png_var_no:
                message = f"Number of variables decresed in conversion, are you sure the format is right (with ։ (Armenian Full Stop))"
                result = CustomEntryDialog(self.root,title='Check for format', window_title='Format Warning', message=message, 
                                            bg=self.tab_controller.current_tab.colour, yes='Proceed', no='Go back',
                                            fg=self.tab_controller.current_tab.foreground_colour, entry=False, yes_no_prompt=True, height=190).result

                if result == 'cancel':  # User clicked Cancel
                    self.tab_controller.current_tab.png_json = False
                    self.tab_controller.current_tab.convert_json_button.invoke_no_command()
                    self.undo()
                    return
                elif result == 'no':  # User clicked No, exit without saving
                    self.tab_controller.current_tab.png_json = False
                    self.tab_controller.current_tab.convert_json_button.invoke_no_command()
                    self.undo()
                    return

            self.tab_controller.current_tab.text_area.delete(1.0, tk.END)
            self.tab_controller.current_tab.text_area.insert(1.0, json.dumps(dictionary, indent=4))
            self.save_memento()

            self.decide_scrollbar_toggle()

        return dictionary

    def open_file(self, path=None):
        if path is None:
            file = askopenfilename(defaultextension=".txt",
                                filetypes=[("All Files", "*.*"),
                                            ("Text Documents", "*.txt"),
                                            ("Image Files", "*.png")])
        else:
            file = path

        if file == "":
            # No file to open
            return

        if not os.path.exists(file):
            self.display_all("Error: File to open does not exist")
            if path is not None:
                raise Exception("An error occurred")
            else:
                return

        _, file_extension = os.path.splitext(file)

        # Extract the file name from the path
        file_name = os.path.splitext(os.path.basename(file))[0]

        metadata = None
        autosave = settings.default_autosave
        secured = False
        backup = settings.default_backup if settings.use_file_backup else False
        wrap = settings.wrap
        spell = settings.default_spell_check if settings.use_spell_checking else False

        if file_extension.lower() not in ['.png', '.jpg', 'jpeg']:
            if os.access(file, os.W_OK): #only proceed if document is not read only
                self.metadata_handler.read_metadata(file)
                metadata = self.metadata_handler.get_tab_metadata(file)

        if not os.access(file, os.W_OK):
            read_only = True
        else:
            read_only = False

        if settings.auto_secure_at_sd:
            drive_letter = os.path.splitdrive(file)[0]
            if drive_letter == self.security_drive:
                secured = True

        if not metadata or metadata is None:
            save_metadata = False

            if file_extension.lower() not in ['.txt']:
                autosave = False

        else:
            save_metadata = True
            if 'secured' in metadata:
                secured = metadata['secured']

            if 'autosave' in metadata:
                autosave = metadata['autosave']

            if 'backup' in metadata:
                backup = metadata['backup']

            if 'wrap' in metadata:
                wrap = metadata['wrap']

            if 'spell' in metadata:
                spell = metadata['spell']

        # Create a new tab and attribute the filename
        new_tab = self.tab_controller.create_tab(file=file, tab_name=file_name, tab_colour=metadata['colour'] if metadata else None, tab_foreground_colour=metadata['foreground_colour'] if metadata else None, save_metadata=save_metadata, secured=secured, autosave=autosave, backup=backup, wrap=wrap, spell=spell)

        def detect_encoding(file_path):
            with open(file_path, 'rb') as f:
                raw_data = f.read()
                encoding_result = chardet.detect(raw_data)
                return encoding_result['encoding']

        if file_extension.lower() in ['.png']:

            image = Image.open(file)
            if not read_only:
                new_tab.text_area.insert(1.0, self.convert_from_json(image.info))
            else:
                new_tab.text_area.config(insertwidth=0)
            image.close()

        elif file_extension.lower() in ['.txt']:
            detected_encoding = detect_encoding(file)

            try:
                with open(file, "r", encoding='utf-8', errors="replace") as file_content:
                    new_tab.text_area.insert(1.0, self.metadata_handler.clear_metadata_from_text(file_content.read()))
                    if not read_only:
                        new_tab.text_area.mark_set("insert", 1.0)
                    else:
                        new_tab.text_area.config(insertwidth=0)

            except:
                with open(file, "r", encoding=detected_encoding, errors="replace") as file_content:
                    new_tab.text_area.insert(1.0, self.metadata_handler.clear_metadata_from_text(file_content.read()))
                    if not read_only:
                        new_tab.text_area.mark_set("insert", 1.0)
                    else:
                        new_tab.text_area.config(insertwidth=0)

        else:
            detected_encoding = detect_encoding(file)

            try:
                with open(file, "r", encoding='utf-8', errors="replace") as file_content:
                    new_tab.text_area.insert(1.0, self.metadata_handler.clear_metadata_from_text(file_content.read()))
                    if not read_only:
                        new_tab.text_area.mark_set("insert", 1.0)
                    else:
                        new_tab.text_area.config(insertwidth=0)

            except:
                with open(file, "r", encoding=detected_encoding, errors="replace") as file_content:
                    new_tab.text_area.insert(1.0, self.metadata_handler.clear_metadata_from_text(file_content.read()))
                    if not read_only:
                        new_tab.text_area.mark_set("insert", 1.0)
                    else:
                        new_tab.text_area.config(insertwidth=0)

        new_tab.display_path()

        if metadata:
            #self.metadata_handler.clear_metadata_from_text_widget(new_tab.text_area)

            cursor_position = metadata.get("cursor_position", "1.0")
            selection_coords = metadata.get("selection", [])
            zoom_level = metadata.get("zoom_level", 1.0)
            vertical_scroll_position = metadata.get("vertical_scroll_position", 0.0)
            is_vertical_scrollbar_shown = metadata.get("is_vertical_scrollbar_shown", True)
            horizontal_scroll_position = metadata.get("horizontal_scroll_position", 0.0)
            is_horizontal_scrollbar_shown = metadata.get("is_horizontal_scrollbar_shown", True)
            strikethrough_coords = metadata.get("strikethrough", [])
            font = metadata.get("font", None)

            if font:
                new_tab.font = font

            # Apply strikethrough if available
            if strikethrough_coords:
                new_tab.text_area.tag_add("strikethrough", *strikethrough_coords)

            if not read_only:
                # Set cursor position
                new_tab.text_area.mark_set("insert", cursor_position)

                # Restore selection if available
                if selection_coords:
                    new_tab.text_area.tag_add("sel", *selection_coords)
            else:
                new_tab.text_area.config(insertwidth=0)

            self.zoom(zoom_factor=zoom_level)

            new_tab.safe_to_save = True

            def claer_metadata_and_apply_scrollbar_info():
                new_tab.toggle_scrollbar_visibility(enable=is_vertical_scrollbar_shown)
                new_tab.text_area.yview('moveto', vertical_scroll_position)

                if not new_tab.wrap and hasattr(new_tab, 'ctk_x_textbox_scrollbar'):
                    new_tab.toggle_x_scrollbar_visibility(enable=is_horizontal_scrollbar_shown)
                    new_tab.text_area.xview('moveto', horizontal_scroll_position)
                    
                new_tab.text_area.update_idletasks()

            #Calculate roughly how much text there is
            text_area_content = new_tab.text_area.get("1.0", "end-1c")
            original_size = len(text_area_content)
            compressed_size = len(zlib.compress(text_area_content.encode()))
            if original_size == 0: #Text hasn't loaded yet
                compression_ratio = 0.001 #Arbitraty, value, to trigger the 'big' text behaviour 
            else:
                compression_ratio = compressed_size / original_size
            
            self.root.update_idletasks()

            # Choose how long to wait before ajusting the scrollbar, due to the compute required to paste the text. Larger text, more wait
            if compression_ratio == 0.001:
                self.root.after(200, claer_metadata_and_apply_scrollbar_info)
            elif compression_ratio < 0.05:
                self.root.after(150, claer_metadata_and_apply_scrollbar_info)
            elif compression_ratio < 0.4:
                self.root.after(100, claer_metadata_and_apply_scrollbar_info)
            else:
                self.root.after(10, claer_metadata_and_apply_scrollbar_info)

        if new_tab.spell and settings.spell_check_when_opening_file:
            new_tab.spell_check('full')

        new_tab.last_saved_file = file
        self.save_memento(ignore_save=True)

        try:
            file_content.close()
        except:
            pass

        try: # Switch to the newly opened tab
            tab_index = self.tab_controller.tabs.index(new_tab)
            self.tab_controller.switch_tab(tab_index)
        except:
            pass
    
        self.tab_controller.current_tab.safe_to_save = True

    def save_file_as(self, tab_index=None):
        if tab_index is None:
            current_tab = self.tab_controller.current_tab
            initial_file_name = self.tab_controller.notebook.tab("current", "text").rstrip('*')
            initial_file_path = current_tab.file
            initial_file_base_name = os.path.splitext(os.path.basename(initial_file_path))[0] if initial_file_path else initial_file_name
            
            default_extension = os.path.splitext(initial_file_path)[1] if initial_file_path else ".txt"

            current_tab.file = asksaveasfilename(
                initialfile=initial_file_base_name,
                defaultextension=default_extension,
                filetypes=[
                    ("All Files", "*.*"),
                    ("Text Documents", "*.txt"),
                    ("PNG", "*.png")
                ]
            )
            tab_index = self.tab_controller.notebook.index(self.tab_controller.notebook.select())
        else:
            self.tab_controller.switch_tab(tab_index)
            current_tab = self.tab_controller.tabs[tab_index]
            initial_file_name = self.tab_controller.notebook.tab("current", "text").rstrip('*')
            initial_file_path = current_tab.file
            initial_file_base_name = os.path.splitext(os.path.basename(initial_file_path))[0] if initial_file_path else initial_file_name
            
            default_extension = os.path.splitext(initial_file_path)[1] if initial_file_path else ".txt"

            current_tab.file = asksaveasfilename(
                initialfile=initial_file_base_name,
                defaultextension=default_extension,
                filetypes=[
                    ("All Files", "*.*"),
                    ("Text Documents", "*.txt"),
                    ("PNG", "*.png")
                ]
            )


        if current_tab.file is None or current_tab.file == '':
            current_tab.file = initial_file_path
            return 'Abort'

        if current_tab.file:
            drive_letter = os.path.splitdrive(current_tab.file)[0]
            if current_tab.secured:
                if drive_letter != self.security_drive:
                    self.display('File is saved in a non secure location', delay_ms=5000, fg='#ff3333')

                    message = f"The tab \"{self.tab_controller.notebook.tab(tab_index, 'text').rstrip('*')}\" is not saved in a secure location. Would you like to save it anyway?"
                    result = CustomEntryDialog(self.root,title='Saved at an insecure location', window_title='Security Error', message=message, initial_value=self.tab_controller.notebook.tab("current", "text").rstrip('*'), bg=self.tab_controller.current_tab.colour, fg=self.tab_controller.current_tab.foreground_colour, entry=False, yes_no_prompt=True, height=170).result

                    if result == 'cancel':  # User clicked Cancel
                        return 'Abort'
                    elif result == 'no':  # User clicked No, exit without saving
                        return

            file = current_tab.file
            try:
                text_content = current_tab.text_area.get(1.0, tk.END)

                if text_content.endswith('\n'):
                    text_content = text_content[:-1]

                _, file_extension = os.path.splitext(file)

                if file_extension.lower() in ['.png']:
                    try:
                        # Assuming `text_content` contains JSON data
                        if current_tab.png_json:
                            text_content = ast.literal_eval(current_tab.text_area.get(1.0, tk.END)[:-1])
                        else:
                            text_content = self.convert_to_json(text_content)

                        self.display('Saving metadata to PNG', delay_ms=2000)
                        self.root.update_idletasks()

                        image = Image.open(initial_file_path)
                        metadata = PngImagePlugin.PngInfo()

                        # Preserve existing metadata
                        if text_content:
                            for key, value in text_content.items():
                                metadata.add_text(key, str(value))

                        image.save(file, format='PNG', pnginfo=metadata)
                        image.close()

                    except:
                        error_message = "Error: Content is not in a valid JSON format."
                        self.display(error_message, fg='red')
                        return

                else:
                    with open(current_tab.file, "w", encoding="utf-8") as file:
                        file.write(text_content)

                if current_tab.save_metadata and file_extension.lower() in ['.txt']:
                    metadata = {
                    "colour": current_tab.colour,
                    "foreground_colour": current_tab.foreground_colour,
                    "autosave": current_tab.autosave,
                    "secured": current_tab.secured,
                    "cursor_position": str(current_tab.text_area.index("insert")),
                    "selection": [str(coord) for coord in current_tab.text_area.tag_ranges("sel")],
                    "zoom_level": current_tab.zoom_factor,
                    "vertical_scroll_position": current_tab.ctk_textbox_scrollbar.get()[0],  # Assuming ctk_textbox_scrollbar is a ttk.Scrollbar
                    "is_vertical_scrollbar_shown": self.tab_controller.current_tab.ctk_textbox_scrollbar.cget("width") != 0,
                    "horizontal_scroll_position": current_tab.ctk_x_textbox_scrollbar.get()[0] if hasattr(current_tab, 'ctk_x_textbox_scrollbar') else False,
                    "is_horizontal_scrollbar_shown": current_tab.ctk_x_textbox_scrollbar.cget("height") != 0 if hasattr(current_tab, 'ctk_x_textbox_scrollbar') else False,
                    "strikethrough": [str(coord) for coord in current_tab.text_area.tag_ranges("strikethrough")],
                    "wrap": current_tab.wrap,
                    "backup": current_tab.backup,
                    "font": current_tab.font,
                    "spell": current_tab.spell,
                    }

                    current_tab.metadata_handler.write_metadata(current_tab.file, metadata)

                current_tab.safe_to_save = True
                current_tab.last_saved_file = current_tab.file

                if current_tab.duplicated:
                    current_tab.duplicated = False

                # Extract the file name from the path (excluding extension)
                file_name = os.path.splitext(os.path.basename(current_tab.file))[0]

                # Mark the current tab as saved in TabController
                self.tab_controller.saved_tabs[tab_index] = True
                self.tab_controller.update_tab_name_indicator(tab_index, self.tab_controller.saved_tabs[tab_index])

                # Rename the current tab to the file name (excluding extension)
                self.tab_controller.rename_tab(tab_index, file_name)

                current_tab.display_path()

                try:
                    file.close()
                except:
                    pass

            except Exception as e:
                self.display(f"Error saving file: {e}")
                return False

            return True
        else:
            return False

    def close_all_but_current_tab(self, ignore_save_as=False, prompt_for_tabs_with_file=False):
        current_tab_index = self.tab_controller.notebook.index(self.tab_controller.notebook.select())
        self.disable_memento_temporarily = True

        for tab_index in reversed(range(len(self.tab_controller.tabs))):
            if tab_index == current_tab_index:
                continue
            value = self.tab_controller.saved_tabs.get(tab_index, None)

            if value is None or value:
                self.tab_controller.close_tab(tab_index=tab_index, ignore_unsaved=True)
            else:
                self.tab_controller.switch_tab(tab_index=tab_index, do_not_focus=True)
                self.tab_controller.close_tab(tab_index=tab_index, ignore_unsaved=False)

        self.disable_memento_temporarily = False

    def save_all_files(self, ignore_save_as=False, prompt_for_tabs_with_file=False):
        self.disable_memento_temporarily = True
        unsaved_tabs = [index for index, saved in self.tab_controller.saved_tabs.items() if not saved]
        for tab_index in list(self.tab_controller.saved_tabs.keys()):
            value = self.tab_controller.saved_tabs.get(tab_index, None)
            if not value:
                tab = self.tab_controller.tabs[tab_index]

                try:
                    if tab.file is not None and os.path.exists(tab.file):
                        if prompt_for_tabs_with_file:

                            if  len(unsaved_tabs) == 1:
                                response = 'yes'
                            else:
                                self.tab_controller.switch_tab(tab_index=tab_index, do_not_focus=True)
                                message = f"Would you like to save the changes to '{self.tab_controller.notebook.tab(tab_index, 'text').rstrip('*')}'?"
                                response = CustomEntryDialog(self.root,title='Unsaved changes', window_title='Close tab', message=message, bg=self.tab_controller.tabs[tab_index].colour, fg=self.tab_controller.tabs[tab_index].foreground_colour, entry=False, height=170).result

                            if response is None or response == 'cancel':  # User clicked Cancel
                                return "Abort"
                            elif response == 'no':  # User clicked no to save changes
                                continue

                            secured_prompt_result = self.save_file(tab_index=tab_index, ignore_save_as=True, prompt_secured=True)
                            if secured_prompt_result == 'Abort':
                                return "Abort"

                        else:
                            secured_prompt_result = self.save_file(tab_index=tab_index, ignore_save_as=True, prompt_secured=True)
                            if secured_prompt_result == 'Abort':
                                return "Abort"

                    elif self.tab_controller.notebook.index(self.tab_controller.notebook.select()) >= 0 and not ignore_save_as:
                        if self.save_file_as(tab_index) == 'Abort':
                            return 'Abort'
                except:
                    self.save_file()
                    self.tab_controller.close_tab(tab_index=tab_index, ignore_unsaved=True, destroy_if_no_tabs=False)


        self.disable_memento_temporarily = False

    def save_file(self, tab_index=None, ignore_save_as=False, ignore_metadata=False, save_metadata_only=False, prompt_secured=False):
        if tab_index is None:
            current_tab = self.tab_controller.current_tab
            tab_index = self.tab_controller.notebook.index(self.tab_controller.notebook.select())
        else:
            current_tab = self.tab_controller.tabs[tab_index]

        if current_tab.file and os.path.exists(current_tab.file):
            drive_letter = os.path.splitdrive(current_tab.file)[0]
            #print('Tab is secured: ', current_tab.secured)
            #print('Drive letter: ', drive_letter)
            #print('Security drive: ', self.security_drive)

            if current_tab.duplicated:
                self.display("There was an error. Your file was not saved to prevent overwriting of another file", delay_ms=10000)
                return
                
            if drive_letter != self.security_drive and current_tab.secured:

                self.display('Chosen path is not a secure location', delay_ms=5000, fg='#ff3333')

                if prompt_secured:

                    message = f"The tab \"{self.tab_controller.notebook.tab(tab_index, 'text').rstrip('*')}\" is not saved in a secure location. Would you like to save it anyway?"
                    result = CustomEntryDialog(self.root,title='Saved at an insecure location', window_title='Security Error', message=message, initial_value=self.tab_controller.notebook.tab("current", "text").rstrip('*'), bg=current_tab.colour, fg=current_tab.foreground_colour, entry=False, yes='Save as', no='Save Insecurely', width=450, height=180).result

                    if result == 'cancel':  # User clicked Cancel
                        return 'Abort'
                    elif result == 'no':  # User clicked No, save insecurely
                        pass
                    elif result == 'yes':
                        save_as_result = self.save_file_as()
                        if save_as_result == 'Abort':
                            return 'Abort'
                        return
                
                else:
                    return
            
            # Extract filename and extension
            file_name, extension = os.path.splitext(os.path.basename(current_tab.file))
            
            if not os.access(current_tab.file, os.W_OK):
                if not ignore_save_as:
                    self.save_file_as()
                    return
                else:
                    return

            # Check for existing files with similar names
            index = 0
            new_file_path = current_tab.file
            file_name_match = re.match(r'^(.*?) \[\d+\]$', file_name)

            if not current_tab.safe_to_save:
                while os.path.exists(new_file_path):
                    # Increment the index and update the file path
                    index += 1
                    file_name_match = re.match(r'^(.*?) \[\d+\]$', file_name)
                    if file_name_match:
                        base_name = file_name_match.group(1)
                        file_name = f"{base_name} [{index}]"
                    else:
                        file_name = f"{file_name} [{index}]"

                    directory = os.path.dirname(current_tab.file)
                    new_file_path = os.path.join(directory, f"{file_name}{extension}")

            self.tab_controller.rename_tab(tab_index, os.path.splitext(os.path.basename(new_file_path))[0], file_update=False)

            text_content = current_tab.text_area.get(1.0, tk.END)

            if text_content.endswith('\n'):
                text_content = text_content[:-1]

            file = current_tab.file = new_file_path

            _, file_extension = os.path.splitext(file)

            if file_extension.lower() in ['.png']:
                try:
                    # Assuming `text_content` contains JSON data
                    if current_tab.png_json:
                        text_content = ast.literal_eval(current_tab.text_area.get(1.0, tk.END)[:-1])
                    else:
                        text_content = self.convert_to_json(text_content)

                    self.display('Saving metadata to PNG', delay_ms=2000)
                    self.root.update_idletasks()

                    image = Image.open(file)
                    metadata = PngImagePlugin.PngInfo()

                    # Preserve existing metadata
                    if text_content:
                        for key, value in text_content.items():
                            metadata.add_text(key, str(value))

                    image.save(file, format='PNG', pnginfo=metadata)
                    image.close()

                except:
                    error_message = "Error: Content is not in a valid format."
                    self.display(error_message, fg='red')
                    return

            else:
                if not save_metadata_only:
                    with open(current_tab.file, "w", encoding="utf-8") as file:
                        file.write(text_content)

            current_tab.safe_to_save = True

            # Update the current_tab file attribute
            current_tab.file = new_file_path
            current_tab.last_saved_file = current_tab.file

            if not save_metadata_only:
                self.tab_controller.saved_tabs[tab_index] = True
                self.tab_controller.update_tab_name_indicator(tab_index, self.tab_controller.saved_tabs[tab_index])

            if current_tab.save_metadata and not ignore_metadata and file_extension.lower() in ['.txt']:
                metadata = {
                    "colour": current_tab.colour,
                    "foreground_colour": current_tab.foreground_colour,
                    "autosave": current_tab.autosave,
                    "secured": current_tab.secured,
                    "cursor_position": str(current_tab.text_area.index("insert")),
                    "selection": [str(coord) for coord in current_tab.text_area.tag_ranges("sel")],
                    "zoom_level": current_tab.zoom_factor,
                    "vertical_scroll_position": current_tab.ctk_textbox_scrollbar.get()[0],  # Assuming ctk_textbox_scrollbar is a ttk.Scrollbar
                    "is_vertical_scrollbar_shown": self.tab_controller.current_tab.ctk_textbox_scrollbar.cget("width") != 0,
                    "horizontal_scroll_position": current_tab.ctk_x_textbox_scrollbar.get()[0] if hasattr(current_tab, 'ctk_x_textbox_scrollbar') else 0,
                    "is_horizontal_scrollbar_shown": current_tab.ctk_x_textbox_scrollbar.cget("height") != 0 if hasattr(current_tab, 'ctk_x_textbox_scrollbar') else False,
                    "strikethrough": [str(coord) for coord in current_tab.text_area.tag_ranges("strikethrough")],
                    "wrap": current_tab.wrap,
                    "backup": current_tab.backup,
                    "font": current_tab.font,
                    "spell": current_tab.spell,
                    }


                current_tab.metadata_handler.write_metadata(current_tab.file, metadata)

        elif self.tab_controller.notebook.index(self.tab_controller.notebook.select()) >= 0:
            #print(f'Tab file: {current_tab.file}, does it exist: {os.path.exists(current_tab.file)}, is it \'\' : {current_tab.file == ''}')
            if not ignore_save_as:
                # If the file hasn't been saved before, use the existing save_file_as method
                self.save_file_as()

    def autosave_loop(self):
        while True:
            # Sleep for 2 minutes (120 seconds)
            time.sleep(settings.autosave_interval_sec)

            self.autosave_function()

    def autosave_function(self):
        if self.disable_autosave_temporarily:
            return

        tab_indices_to_save = self.tab_controller.get_autosave_enabled_tabs()
        for index in tab_indices_to_save:
            self.tab_controller.tabs[index].display_autosave('Autosaving...', 2000)
            self.save_file(tab_index=index, ignore_save_as=True, prompt_secured=False)

    def rearrange_rows(self):
        if self.tab_controller.current_tab.read_only:
            return
        
        items_to_display = [item if item is not None else "" for item in self.tab_controller.current_tab.text_area.get("1.0", "end-1c").split("\n")]
        rearrange_window = ReorderableListWindow(self.root, items_to_display, notepad=self)
        rearrange_window.text_area = self.tab_controller.current_tab.text_area
        rearrange_window.update_window_size()


    def add_indices_prompt_start(self):
        if self.tab_controller.current_tab.read_only:
            return
        
        try:
            # Prompt the user for the starting index
            response = CustomEntryDialog(self.root,title='Start from index', window_title='Add indices starting from...', initial_value=1, bg=self.tab_controller.current_tab.colour, fg=self.tab_controller.current_tab.foreground_colour, height=155).result

            if response not in ['yes', 'no', 'cancel']:
                try:
                    start_index = int(response)
                except:
                    return

            try:
                if not start_index or start_index is None:
                    self.display('Start index is not in a valid format')
                    return
            except:
                return

            # Call the modified add_indices with the provided starting index
            self.add_indices(start_index)

        except tk.TclError as e:
            self.display(f"Error: {e}")

    def add_indices(self, start_at=1):
        if self.tab_controller.current_tab.read_only:
            return
        
        self.save_memento()
        self.save_current_page_view_info()
        try:
            # Get the selected text indices and content
            selected_indices_content = self.choose_selected_text()

            # Get the full text
            full_text = self.tab_controller.current_tab.text_area.get(1.0, tk.END)

            # Split the full text into lines
            lines = full_text.split("\n")

            lines_with_strikethrough = set()

            for coord in self.tab_controller.current_tab.view_info[3]:
                split_coord = coord.split('.')
                if len(split_coord) == 2:
                    line_index, char_index = map(int, split_coord)
                    lines_with_strikethrough.add(line_index)

            # Update strikethrough ranges based on the changes made to the text
            updated_ranges = []

            for new_index, (old_index, line_content) in enumerate(selected_indices_content, start=start_at):
                # Calculate the length of the added index and separator
                added_length = len(str(new_index)) + len(self.separator)

                # Check if the line has strikethrough
                line_has_strikethrough = old_index in lines_with_strikethrough

                if line_has_strikethrough:
                    added_length = len(str(new_index)) + len(self.separator)
                    # Adjust the character positions and starting index in the strikethrough ranges
                    adjusted_ranges = []
                    for coord in self.tab_controller.current_tab.view_info[3]:
                        line, char = map(int, coord.split('.'))

                        if line == old_index:
                            char += added_length
                            adjusted_ranges.append(f"{line}.{char}")

                    updated_ranges.extend(adjusted_ranges)

                # Adjust the line content with the new index
                lines[old_index - 1] = f"{new_index}{self.separator}{line_content}"

            # Update the variable with the adjusted ranges
            self.tab_controller.current_tab.view_info = (*self.tab_controller.current_tab.view_info[:3], updated_ranges, *self.tab_controller.current_tab.view_info[4:])

            # Join the lines back into the modified text
            modified_text = "\n".join(lines)

            # Update the original text
            self.tab_controller.current_tab.text_area.replace(1.0, tk.END, modified_text[:-1])

        except tk.TclError as e:
            self.display(f"Error: {e}")

        self.apply_saved_page_view_info()

    def remove_indices(self):
        if self.tab_controller.current_tab.read_only:
            return
        
        self.save_memento()
        self.save_current_page_view_info()
        try:
            # Get the selected text indices and content
            selected_indices_content = self.choose_selected_text()

            # Get the full text
            full_text = self.tab_controller.current_tab.text_area.get(1.0, tk.END)

            # Define a regex pattern to match lines starting with a number and separator
            pattern = re.compile(r'^(\d+){0}(.*)$'.format(re.escape(self.separator)))

            # Split the full text into lines
            lines = full_text.split("\n")

            lines_with_strikethrough = set()

            for coord in self.tab_controller.current_tab.view_info[3]:
                split_coord = coord.split('.')
                if len(split_coord) == 2:
                    line_index, char_index = map(int, split_coord)
                    lines_with_strikethrough.add(line_index)

            # Update strikethrough ranges based on the changes made to the text
            updated_ranges = []

            # Remove indices from the specified lines
            for index, line in selected_indices_content:
                match = pattern.match(line)
                if match:
                    modified_line = match.group(2)
                    # Check if the line is empty after removing indices
                    lines[index - 1] = modified_line if modified_line else ""

                    # Check if the line has strikethrough
                    line_has_strikethrough = index in lines_with_strikethrough

                    if line_has_strikethrough:
                        added_length = len(match.group(1) + self.separator)
                        # Adjust the character positions and starting index in the strikethrough ranges
                        adjusted_ranges = []
                        for coord in self.tab_controller.current_tab.view_info[3]:
                            line, char = map(int, coord.split('.'))

                            if line == index:
                                char -= added_length
                                adjusted_ranges.append(f"{line}.{char}")

                        updated_ranges.extend(adjusted_ranges)

            # Update the variable with the adjusted ranges
            self.tab_controller.current_tab.view_info = (*self.tab_controller.current_tab.view_info[:3], updated_ranges, *self.tab_controller.current_tab.view_info[4:])

            # Join the lines back into the modified text
            modified_text = "\n".join(lines)

            # Update the original text
            self.tab_controller.current_tab.text_area.replace(1.0, tk.END, modified_text[:-1])

        except tk.TclError as e:
            self.display(f"Error: {e}")

        self.apply_saved_page_view_info()

    def choose_selected_text(self):
        try:
            # Get the selected text indices
            selected_indices = self.tab_controller.current_tab.text_area.tag_ranges(tk.SEL)

            if not selected_indices:
                # If no text is selected, select the entire text
                selected_indices = (1.0, tk.END)

            # Split the selected text into lines
            start_line, start_char = map(int, str(self.tab_controller.current_tab.text_area.index(selected_indices[0])).split('.'))
            end_line, end_char = map(int, str(self.tab_controller.current_tab.text_area.index(selected_indices[1])).split('.'))

            # Get the indices and content of lines containing characters within the selection
            result = []
            for index in range(start_line, end_line + 1):
                start_index = f"{index}.{start_char}" if index == start_line else f"{index}.0"
                end_index = f"{index}.{end_char}" if index == end_line else f"{index + 1}.0"
                
                # Check the content through the index of the line
                if any(char in self.tab_controller.current_tab.text_area.get(f"{index}.0", f"{index + 1}.0") for char in self.tab_controller.current_tab.text_area.get(start_index, end_index)):
                    result.append((index, self.tab_controller.current_tab.text_area.get(f"{index}.0", f"{index + 1}.0").rstrip('\n')))

            return result

        except tk.TclError as e:
            self.display(f"Error: {e}")

    def save_and_exit(self, event=None, force_exit=False):
        if self.disable_escape_app and not force_exit:
            #self.display('Exiting the app is disabled. Try Control + Shift + F4')
            return
        unsaved_tabs = [index for index, saved in self.tab_controller.saved_tabs.items() if not saved]

        if unsaved_tabs:
            message = "There are unsaved changes.\nWould you like to save before exiting?"
            result = CustomEntryDialog(self.root,title='Unsaved changes', window_title='Exit Notepad', message=message, initial_value=self.tab_controller.notebook.tab("current", "text").rstrip('*'), bg=self.tab_controller.current_tab.colour, fg=self.tab_controller.current_tab.foreground_colour, entry=False, height=170).result

            if result == 'cancel':  # User clicked Cancel
                return
            elif result == 'yes':  # User clicked Yes, save changes
                if not self.save_all_files(ignore_save_as=False, prompt_for_tabs_with_file=True) == 'Abort':
                    if not self.is_initially_mounted and self.is_mounted and not self.disable_dismount_when_exit_once:
                        self.close_security_folder_and_exit()
                    else:
                        self.backup_all_files()
                        self.save_paths()

                        self.root.destroy()

            elif result == 'no':  # User clicked No, exit without saving
                for tab in self.tab_controller.tabs:
                    if tab.last_saved_file_using_save_path:
                        #print(f'tab.last_saved_file_using_save_path: {tab.last_saved_file_using_save_path}, tab.last_saved_file: {tab.last_saved_file}')
                        if (os.path.normpath(tab.last_saved_file) if tab.last_saved_file is not None else None) != (os.path.normpath(tab.last_saved_file_using_save_path) if tab.last_saved_file_using_save_path is not None else None):
                            os.remove(tab.last_saved_file_using_save_path)

                if not self.is_initially_mounted and self.is_mounted and not self.disable_dismount_when_exit_once:
                    self.close_security_folder_and_exit()
                else:
                    self.backup_all_files()
                    self.save_paths()

                    self.root.destroy()
        else:
            if not self.is_initially_mounted and self.is_mounted and not self.disable_dismount_when_exit_once:
                self.close_security_folder_and_exit()
            else:
                self.backup_all_files()
                self.save_paths()

                self.root.destroy()

    def exit_without_saving(self):
        response = messagebox.askyesno("Exit Without Saving",
                                       "Are you sure you want to exit without saving changes?", icon=messagebox.WARNING)

        if response:
            if not self.is_initially_mounted and self.is_mounted and not self.disable_dismount_when_exit_once:
                self.close_security_folder_and_exit(save_paths=False)
            else:
                try:
                    self.backup_all_files()
                except:
                    pass
                self.root.destroy()

    def prompt_colour(self, title):
        prompt_root = Tk()
        prompt_root.withdraw()
        prompt_root.iconbitmap(bitmap=ico_path)
        colour = colorchooser.askcolor(title=title, parent=prompt_root, initialcolor=self.tab_controller.current_tab.colour)
        prompt_root.destroy()

        return colour[1] if colour else None

    def rename_current_tab(self, file_update=True):
        self.save_memento()
        if self.tab_controller.current_tab.read_only:
            file_update=False

        new_name = CustomEntryDialog(self.root,title='Rename tab:', window_title='Rename tab', initial_value=self.tab_controller.notebook.tab("current", "text").rstrip('*'), bg=self.tab_controller.current_tab.colour, fg=self.tab_controller.current_tab.foreground_colour, height=155).result
        if new_name in [None, 'cancel']:
            return
        tab_index = self.tab_controller.notebook.index(self.tab_controller.notebook.select())
        self.tab_controller.current_tab.safe_to_save = False
        self.tab_controller.rename_tab(tab_index, new_name, file_update=file_update)

    def recolour_current_tab(self):
        new_colour = self.prompt_colour('Recolour tab:')
        if new_colour == None:
            return
        tab_index = self.tab_controller.notebook.index(self.tab_controller.notebook.select())
        self.tab_controller.recolour_tab(tab_index, new_colour)
        self.save_file(save_metadata_only=True)

    def change_separator(self):
        self.save_memento()
        # Prompt the user for the starting index
        response = CustomEntryDialog(self.root,title='Change separator', window_title='Change separator', message='Type a separator to use between indices and text', initial_value=self.separator, bg=self.tab_controller.current_tab.colour, fg=self.tab_controller.current_tab.foreground_colour, entry=True, height=215).result
        if response is None or response == 'cancel':
            self.display(f'Separator not changed')
            return
        self.separator = response
        self.display(f'Separator changed to: {self.separator}')

    def change_tab_font(self):
        # Prompt the user for the starting index
        response = CustomEntryDialog(self.root,title='Change tab font', window_title='Change font', message="Type a font to be used in this tab's text area (Leave blank to reset to default font)", 
                                     initial_value=self.tab_controller.current_tab.font if self.tab_controller.current_tab.font else "Default settings font",
                                     bg=self.tab_controller.current_tab.colour, fg=self.tab_controller.current_tab.foreground_colour, entry=True, height=225).result
        if response == 'cancel':
            self.display(f'Font not changed for this tab')
            return

        elif response == "Default settings font" or response is None or response == '':
            self.tab_controller.current_tab.font = None
            self.display(f"Font reset to default for this tab")

        else:
            self.tab_controller.current_tab.font = response
            self.display(f"Font changed to '{self.tab_controller.current_tab.font}' for this tab")

        self.update_font_size()

    def toggle_rainbow_cursor(self):
        if not self.is_rainbow_cursor:
            self.rainbow_stop.clear()
            self.rainbow_thread = threading.Thread(target=self.rainbow_cursor, args=(self.rainbow_stop,))
            self.rainbow_thread.daemon = True
            self.rainbow_thread.start()
            self.is_rainbow_cursor = True
        else:
            self.rainbow_stop.set()
            self.is_rainbow_cursor = False

    def rainbow_cursor(self, stop_event):
        colours = ['red', 'blue', 'green', 'yellow', 'purple', 'pink', '#8650ad', '#02f0e0', '#d12a43', '#a2d12a', '#02d170', '#db9635']
        while not stop_event.is_set():
            for colour in colours:
                if stop_event.is_set():
                    self.tab_controller.current_tab.text_area.config(insertbackground=settings.cursor_colour)
                    break

                self.tab_controller.current_tab.text_area.config(insertbackground=colour)
                time.sleep(0.1)

    def test_status(self):
        if os.path.exists(settings.security_folder):
            self.is_mounted = True
            return True
        else:
            self.is_mounted = False
            return False

    def dismount_drive_and_exit(self, save_paths):
        self.disable_autosave_temporarily = True
        self.tab_controller.stop_switch_tab_flag = True

        try:
            cmd = cmd_test_mount_status
            result = subprocess.run(cmd, creationflags=subprocess.CREATE_NO_WINDOW, capture_output=True, text=True, encoding='utf-8')

            # Define the pattern to check for
            pattern = re.compile(cmd_test_mount_status_success_pattern)

            # Check if the pattern is present in the output
            if pattern.search(result.stdout):
                try:
                    command = shlex.split(cmd_dismount_drive)
                    subprocess.run(command, creationflags=subprocess.CREATE_NO_WINDOW, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='utf-8')

                    self.is_mounted = False

                except Exception as e:
                    self.display(f"Error: {e}")
                    self.display_all(f'Error dismounting drive')

            else:
                self.is_mounted = False
                self.display_all('Drive already dismounted')

        except subprocess.CalledProcessError as e:
            self.display(f"Error: {e}")
            self.display_all(f'Error dismounting drive')

        if self.reopen_after_exit:
            self.save_paths()

        self.root.destroy()

    def dismount_drive(self):
        self.disable_autosave_temporarily = True
        self.tab_controller.stop_switch_tab_flag = True

        self.display_all('Dismounting drive...')

        try:
            cmd = cmd_test_mount_status
            result = subprocess.run(cmd, creationflags=subprocess.CREATE_NO_WINDOW, capture_output=True, text=True, encoding='utf-8')

            # Define the pattern to check for
            pattern = re.compile(cmd_test_mount_status_success_pattern)

            # Check if the pattern is present in the output
            if pattern.search(result.stdout):
                try:
                    command = shlex.split(cmd_dismount_drive)
                    subprocess.run(command, creationflags=subprocess.CREATE_NO_WINDOW, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='utf-8')

                    if not self.test_status():

                        self.is_mounted = False

                        self.tab_controller.refresh_tabs()

                        self.root.after(200, lambda: self.display_all('Drive dismounted successfully'))
                    else:
                        self.display_all(f'Drive not dismounted')

                except Exception as e:
                    self.display(f"Error: {e}")
                    self.display_all(f'Error dismounting drive')

            else:
                self.is_mounted = False
                self.display_all('Drive already dismounted')

        except subprocess.CalledProcessError as e:
            self.display(f"Error: {e}")
            self.display_all(f'Error dismounting drive')

        self.disable_autosave_temporarily = False
        self.tab_controller.stop_switch_tab_flag = False

    def mount_drive(self, folder_name, init, show_loading):
        self.disable_autosave_temporarily = True

        self.display_all('Mounting drive...')

        try:
            cmd = cmd_test_mount_status
            result = subprocess.run(cmd, creationflags=subprocess.CREATE_NO_WINDOW, text=True, encoding='utf-8', stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            # Define the pattern to check for
            pattern = re.compile(r'\*\*\* Drive \w+ is reachable\. \*\*\*')

            # Check if the pattern is present in the output
            if pattern.search(result.stdout):
                self.is_mounted = True
                if not init:
                    self.tab_controller.current_tab.toggle_loading_animation()
                    self.display_all(f'Drive already mounted')
            else:
                try:
                    command = shlex.split(cmd_mount_drive)
                    result = subprocess.run(command, creationflags=subprocess.CREATE_NO_WINDOW, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')

                    if not init:
                        self.tab_controller.current_tab.toggle_loading_animation()

                    # Define the pattern to check for
                    pattern = re.compile(cmd_mount_drive_success_pattern)

                    # Check if the pattern is present in the output
                    if pattern.search(result.stdout):
                        self.is_mounted = True
                        if not init:
                            self.display_all('Drive mounted successfully')
                    else:
                        self.is_mounted = False
                        if not init:
                            self.display_all(f'Error mounting drive: Operation interrupted')

                except Exception as e:
                    self.display(f"Error during mounting: {e}")
                    if not init:
                        self.display_all(f'Error mounting drive')

        except subprocess.CalledProcessError as e:
            self.display(f"Error: {e}")
            if not init:
                self.display_all(f'Error mounting drive')

        self.disable_autosave_temporarily = False

    def open_security_folder(self, folder_name=None, init=False, show_loading=False):
        if not init:
            self.tab_controller.current_tab.toggle_loading_animation()

            # Create a threading.Thread and start it
            script_thread = threading.Thread(target=self.mount_drive, args=(folder_name, init,show_loading,))
            script_thread.start()
        else:
            self.mount_drive(folder_name, init=init, show_loading=show_loading)

    def save_path(self, path, category_file='', secure=False):                   
        self.save_memento()
        tab_name = self.tab_controller.notebook.tab("current", "text").rstrip('*')
        tab_index = self.tab_controller.notebook.index(self.tab_controller.notebook.select())
        tab = self.tab_controller.current_tab

        if tab.file:
            file_path, extension = os.path.splitext(tab.file)
        else:
            extension = '.txt'

        full_path = os.path.join(path, category_file, f"{tab_name}{extension}")

        drive_letter = os.path.splitdrive(full_path)[0]
        if tab.secured:
            if drive_letter != self.security_drive:
                self.display('Chosen path is not a secure location', delay_ms=5000, fg='#ff3333')

                message = f"The tab \"{self.tab_controller.notebook.tab(tab_index, 'text').rstrip('*')}\" is not saved in a secure location. Would you like to save it anyway?"
                result = CustomEntryDialog(self.root,title='Saved at an insecure location', window_title='Security Error', message=message, initial_value=self.tab_controller.notebook.tab("current", "text").rstrip('*'), bg=tab.colour, fg=tab.foreground_colour, entry=False, yes_no_prompt=True, width=325, height=190).result

                if result == 'cancel':  # User clicked Cancel
                    return
                elif result == 'no':  # User clicked No, exit without saving
                    return

        def decide_rename(tab, full_path):
            if tab.last_saved_file_using_save_path is None:
                if os.path.normpath(full_path) != (os.path.normpath(tab.last_saved_file) if tab.last_saved_file is not None else None):
                    return True
                else:
                    return False
            elif  os.path.normpath(full_path) ==  os.path.normpath(tab.last_saved_file_using_save_path) or  os.path.normpath(full_path) !=  (os.path.normpath(tab.last_saved_file) if tab.last_saved_file is not None else None):
                return False
            else:
                return True

        if decide_rename(tab, full_path):
            #print(f'statement is true, full_path: {full_path}, tab.last_saved_file_using_save_path: {tab.last_saved_file_using_save_path}, tab.last_saved_file: {tab.last_saved_file}')
            #self.display('renamed')
            index = 0

            while os.path.exists(full_path):
                # Increment the index and update the file path
                index += 1
                file_name_match = re.match(r'^(.*?) \[\d+\]$', tab_name)
                if file_name_match:
                    base_name = file_name_match.group(1)
                    tab_name = f"{base_name} [{index}]"
                else:
                    tab_name = f"{tab_name} [{index}]"

                directory = os.path.dirname(full_path)
                full_path = os.path.join(directory, f"{tab_name}{extension}")
                self.tab_controller.rename_tab(tab_index, tab_name, file_update=False)

                # Create the directory structure if it doesn't exist
                os.makedirs(os.path.dirname(full_path), exist_ok=True)

        if tab.last_saved_file_using_save_path is not None and os.path.exists(tab.last_saved_file_using_save_path):
            # Only remove the previous saved file if it is not the same as the last saved file or if it's secured, and never remove it if the new one is the same as the old one
            if (((os.path.normpath(tab.last_saved_file) if tab.last_saved_file is not None else None) != os.path.normpath(tab.last_saved_file_using_save_path)) or tab.secured) and (os.path.normpath(tab.last_saved_file_using_save_path) != os.path.normpath(full_path)):
                # Remove the path from last_saved_file_using_save_path
                os.remove(tab.last_saved_file_using_save_path)

        tab.last_saved_file_using_save_path = full_path

        tab.safe_to_save = True

        if secure and not tab.secured:
            tab.secured_button.invoke()

        if (os.path.normpath(tab.last_saved_file) if tab.last_saved_file is not None else None) != os.path.normpath(full_path):
            # Save the file
            with open(full_path, "w", encoding="utf-8") as file:
                pass

        # Set the current tab file attribute
        tab.file = full_path
        tab.display_path()

    def close_security_folder(self):
        # Create a threading.Thread and start it
        script_thread = threading.Thread(target=self.dismount_drive)
        script_thread.start()

        return "break"

    def close_security_folder_and_exit(self, save_paths=True):

        #self.display_all('Dismounting drive before exiting...')
        self.backup_all_files()

        self.tab_controller.notebook.destroy()

        self.tab_controller.exit_label = Label(self.tab_controller.root, text='Dismounting drive before exiting...', fg=settings.ui_fg, bg=settings.ui_bg, font=(settings.bold_font, 22))
        self.tab_controller.exit_label.pack(expand=YES, fill=BOTH, side=TOP)

        self.root.update_idletasks()

        # Create a threading.Thread and start it
        self.dismount_drive_and_exit(save_paths=save_paths)

    def find_and_replace(self):
        if self.tab_controller.current_tab.read_only:
            return

        FindReplaceDialog(self.root, self, self.tab_controller.current_tab.text_area)

    def apply_strikethrough(self):
        if self.tab_controller.current_tab.read_only:
            return

        self.save_memento()

        # Get the current selected range
        if self.tab_controller.current_tab.text_area.tag_ranges(tk.SEL):
            start, end = self.tab_controller.current_tab.text_area.index(tk.SEL_FIRST), self.tab_controller.current_tab.text_area.index(tk.SEL_LAST)
        else:
            start = 1.0
            end = "end"
        
        # Check if any part of the selected text has strikethrough
        if any("strikethrough" in tag for tag in self.tab_controller.current_tab.text_area.tag_names(start)):
            # Remove strikethrough from the selected text
            self.tab_controller.current_tab.text_area.tag_remove("strikethrough", start, end)
        else:
            # Apply strikethrough to the selected text
            self.tab_controller.current_tab.text_area.tag_add("strikethrough", start, end)

    def toggle_insert_text(self):
        self.insert_text = not self.insert_text

    def insert_current_datetime_at_cursor(self):
        if self.tab_controller.current_tab.read_only:
            return
        
        self.save_memento()

        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        text_area = self.tab_controller.current_tab.text_area
        if self.tab_controller.current_tab.text_area.tag_ranges(tk.SEL):
            start_index = text_area.index(tk.SEL_FIRST)
            end_index = text_area.index(tk.SEL_LAST)
            text_area.delete(start_index, end_index)

        cursor_position = text_area.index(tk.INSERT)
        text_area.insert(cursor_position, current_datetime)

    def insert_current_date_at_cursor(self):
        if self.tab_controller.current_tab.read_only:
            return
        
        self.save_memento()

        current_datetime = datetime.now().strftime("%Y-%m-%d")
        text_area = self.tab_controller.current_tab.text_area
        if self.tab_controller.current_tab.text_area.tag_ranges(tk.SEL):
            start_index = text_area.index(tk.SEL_FIRST)
            end_index = text_area.index(tk.SEL_LAST)
            text_area.delete(start_index, end_index)

        cursor_position = text_area.index(tk.INSERT)
        text_area.insert(cursor_position, current_datetime)

    def save_current_page_view_info(self, tab=None):
        if tab is None:
            current_tab = self.tab_controller.current_tab
        else:
            current_tab = tab

        saved_cursor_position = current_tab.text_area.index("insert")
        saved_selection_range = current_tab.text_area.tag_ranges("sel")
        saved_strikethrough_ranges = [str(coord) for coord in current_tab.text_area.tag_ranges("strikethrough")]
        saved_misspelled_ranges = [str(coord) for coord in current_tab.text_area.tag_ranges("misspelled")]
        saved_scrollbar_info = {"vertical_scroll_position": current_tab.ctk_textbox_scrollbar.get()[0], "is_scrollbar_shown": current_tab.ctk_textbox_scrollbar.cget("width") != 0,}
        saved_x_scrollbar_info = {"horizontal_scroll_position": current_tab.ctk_x_textbox_scrollbar.get()[0], "is_scrollbar_shown": current_tab.ctk_x_textbox_scrollbar.cget("height") != 0} if hasattr(current_tab, 'ctk_x_textbox_scrollbar') else {"horizontal_scroll_position": 0, "is_scrollbar_shown": False}
        initial_saved_wrap = current_tab.wrap

        current_tab.view_info = saved_cursor_position, saved_selection_range, saved_strikethrough_ranges, saved_misspelled_ranges, saved_scrollbar_info, saved_x_scrollbar_info, initial_saved_wrap

    def apply_saved_page_view_info(self, tab=None):
        if not tab:
            current_tab = self.tab_controller.current_tab
        else:
            current_tab = tab

        saved_cursor_position, saved_selection_range, saved_strikethrough_ranges, saved_misspelled_ranges, saved_scrollbar_info, saved_x_scrollbar_info, initial_saved_wrap = current_tab.view_info

        self.zoom_refresh()

        # Restore the selection range
        current_tab.text_area.tag_remove(tk.SEL, "1.0", tk.END)
        if saved_selection_range:
            # Unpack the tuple into separate arguments
            current_tab.text_area.tag_add(tk.SEL, *saved_selection_range)

                # Apply the "strikethrough" tag to the text widget in the new_tab
        if saved_strikethrough_ranges:
            current_tab.text_area.tag_add("strikethrough", *saved_strikethrough_ranges)

        if saved_misspelled_ranges:
            current_tab.text_area.tag_add("misspelled", *saved_misspelled_ranges)

        # Set the cursor back to the saved position
        line, char = map(int, saved_cursor_position.split('.'))
        current_tab.text_area.mark_set("insert", f"{line}.{char}")

        def apply_scrollbar_info():
            current_tab.toggle_scrollbar_visibility(enable=saved_scrollbar_info["is_scrollbar_shown"])
            current_tab.text_area.yview('moveto', saved_scrollbar_info["vertical_scroll_position"])

            if not current_tab.wrap and hasattr(current_tab, 'ctk_x_textbox_scrollbar'):
                if initial_saved_wrap and current_tab.wrap:
                    current_tab.toggle_x_scrollbar_visibility(enable=saved_x_scrollbar_info["is_scrollbar_shown"])
                    current_tab.text_area.xview('moveto', saved_x_scrollbar_info["horizontal_scroll_position"])
                else:
                    current_tab.toggle_x_scrollbar_visibility(enable=True)
                    current_tab.text_area.xview('moveto', saved_x_scrollbar_info["horizontal_scroll_position"])

            current_tab.text_area.update_idletasks()

        #Calculate roughly how much text there is
        text_area_content = current_tab.text_area.get("1.0", "end-1c")
        original_size = len(text_area_content)
        compressed_size = len(zlib.compress(text_area_content.encode()))
        if original_size == 0: #Text hasn't loaded yet
            compression_ratio = 0.001 #Arbitraty, value, to trigger the 'big' text behaviour 
        else:
            compression_ratio = compressed_size / original_size

        # Choose how long to wait before ajusting the scrollbar, due to the compute required to paste the text. Larger text, more wait
        if compression_ratio == 0.001:
            self.root.after(200, apply_scrollbar_info)
        elif compression_ratio < 0.05:
            self.root.after(150, apply_scrollbar_info)
        elif compression_ratio < 0.4:
            self.root.after(100, apply_scrollbar_info)
        else:
            self.root.after(10, apply_scrollbar_info)

    def open_and_break(self, event=None, path=None):
        self.open_file(path=path)
        return "break"

    def create_and_break(self, event=None):
        if event and event.state & 0x1:  # Check if the Shift key is pressed
            return
        self.tab_controller.create_tab(save_metadata=settings.default_metadata ,autosave=settings.default_autosave)
        return "break"

    def show_about_and_break(self, event=None):
        self.show_about()
        return "break"
 
    def duplicate_and_break(self, event=None):
        self.tab_controller.duplicate_tab()
        return "break"

    def toggle_default_autosave(self):
        global config_settings

        config_settings.load_config_settings()

        setattr(settings, 'default_autosave', not settings.default_autosave)
        setattr(config_settings, 'default_autosave', not settings.default_autosave)

        if settings.default_autosave:
            self.display_all('Autosave will be enabled by default', fg='#adffb4')
        else:
            self.display_all('Autosave will be disabled by default', fg='#ffadad')

        config_settings.save_config_settings()

    def toggle_default_metadata(self):
        global config_settings

        config_settings.load_config_settings()

        setattr(settings, 'default_metadata', not settings.default_metadata)
        setattr(config_settings, 'default_metadata', not settings.default_metadata)

        if settings.default_metadata:
            self.display_all('Tabs will be autosaved by default', fg='#adffb4')
        else:
            self.display_all('Tabs will not be autosaved by default', fg='#ffadad')

        config_settings.save_config_settings()

    def toggle_default_spell_checking(self):
        global config_settings

        config_settings.load_config_settings()

        setattr(settings, 'default_spell_check', not settings.default_spell_check)
        setattr(config_settings, 'default_spell_check', not settings.default_spell_check)

        if settings.default_spell_check:
            self.display_all('Tabs will be spell checked by default', fg='#adffb4')
        else:
            self.display_all('Tabs will not be spell checked by default', fg='#ffadad')

        config_settings.save_config_settings()

    def toggle_default_backup(self):
        global config_settings

        config_settings.load_config_settings()

        setattr(settings, 'default_backup', not settings.default_backup)
        setattr(config_settings, 'default_backup', not settings.default_backup)

        if settings.default_backup:
            self.display_all('Tabs will be backed up by default', fg='#adffb4')
        else:
            self.display_all('Tabs will not be backed up by default', fg='#ffadad')

        config_settings.save_config_settings()

    def save_paths(self):
        files = []
        tab_on_focus_index = 0
        if self.tab_controller.notebook:
            try:
                tab_on_focus_index = self.tab_controller.notebook.index(self.tab_controller.notebook.select())
                secured_tab_indexes = [index for index, tab in enumerate(self.tab_controller.tabs) if tab.secured and tab.file != '']
                tab_on_focus_index -= sum(1 for index in secured_tab_indexes if index <= tab_on_focus_index)
                if tab_on_focus_index < 0:
                    tab_on_focus_index = 0
            except:
                pass

        if self.reopen_after_exit:
            for tab in self.tab_controller.tabs:
                if tab.secured or tab.last_saved_file == '': #add here the logic
                    continue
                path = tab.last_saved_file
                if path is not None:
                    files.append(path)

        data = {"files": files, "tab_on_focus_index": tab_on_focus_index}

        with open(last_opened_files_path, "w", encoding="utf-8") as file:
            toml.dump(data, file)

    def read_paths(self):
        try:
            with open(last_opened_files_path, "r", encoding="utf-8") as file:
                data = toml.load(file)
                files = data.get("files", [])
                tab_on_focus_index = data.get("tab_on_focus_index", 0)
        except (toml.TomlDecodeError, FileNotFoundError):
            # Handle errors gracefully
            files = []
            tab_on_focus_index = 0

        return files, tab_on_focus_index

    def update_time(self):
        current_date = datetime.now()
        day_translation = {"Monday": "월", "Tuesday": "화", "Wednesday": "수", "Thursday": "목", "Friday": "금", "Saturday": "토", "Sunday": "일"}
        #self.korean_date = f"{current_date.year}년 {current_date.month}월 {current_date.day}일, ({day_translation[current_date.strftime('%A')]}요일)"
        #self.korean_date = f"{current_date.year}년 {current_date.month}월 {current_date.day}일 {day_translation[current_date.strftime('%A')]}요일"
        self.korean_date = f"{current_date.month}월 {current_date.day}일 {day_translation[current_date.strftime('%A')]}요일"
        self.display_time()
        
        # Calculate time until the next minute
        next_minute = (current_date.replace(second=0, microsecond=0) + timedelta(minutes=1))
        time_until_next_minute = (next_minute - current_date).total_seconds() * 1000
        
        self.root.after(int(time_until_next_minute), self.update_time)  # Update time every 60000 milliseconds (1 minute)

    def go_to(self):
        cursor_line = CustomEntryDialog(self.root,title='Go to line:', window_title='Go to', initial_value=1, bg=self.tab_controller.current_tab.colour, fg=self.tab_controller.current_tab.foreground_colour, height=155).result
        if cursor_line in [None, 'cancel', 0]:
            return

        # Convert cursor_line to an integer
        try:
            cursor_line = int(cursor_line)
        except ValueError:
            # Handle non-integer input
            self.display('Line number must be an integer')
            return
        
        # Get the index for the beginning of the specified line with column 0
        cursor_index = f"{cursor_line}.0"
        
        # Set the cursor position in the text widget
        self.tab_controller.current_tab.text_area.mark_set(tk.INSERT, cursor_index)
        self.tab_controller.current_tab.text_area.see(cursor_index)
        self.update_character_and_cursor_labels()

    def invoke_metadata_button(self):
        tab = self.tab_controller.current_tab

        if hasattr(tab, 'rich_text_button'):
            tab.rich_text_button.invoke()

    def invoke_autosave_button(self):
        tab = self.tab_controller.current_tab

        if hasattr(tab, 'autosave_button'):
            tab.autosave_button.invoke()

    def invoke_secured_button(self):
        tab = self.tab_controller.current_tab

        if hasattr(tab, 'secured_button'):
            tab.secured_button.invoke()

    def invoke_read_only_button(self):
        tab = self.tab_controller.current_tab

        if hasattr(tab, 'read_only_button'):
            tab.read_only_button.invoke()

    def invoke_spell_button(self):
        tab = self.tab_controller.current_tab

        if hasattr(tab, 'spell_button'):
            tab.spell_button.invoke()

    def invoke_backup_button(self):
        tab = self.tab_controller.current_tab

        if hasattr(tab, 'backup_button'):
            tab.backup_button.invoke()

    def invoke_maximize_button(self):
        if hasattr(self.tab_controller, 'maximize_button'):
            self.tab_controller.maximize_button.invoke()
        else:
            self.maximize()

    def update_keyboard_layout_label(self):
        language_id = ct.windll.user32.GetKeyboardLayout(0) & 0xFFFF
        language_name_buffer = ct.create_unicode_buffer(256)
        ct.windll.kernel32.GetLocaleInfoW(language_id, 0x00000002, language_name_buffer, ct.sizeof(language_name_buffer))  # 0x00000002 is LOCALE_SLANGUAGE
        language_name = language_name_buffer.value.split('(')[0].strip()
        self.tab_controller.keyboard_layout_label.config(text=language_name)

    def create_temp_file_path(self):
        # Create the directory if it doesn't exist
        os.makedirs(os.path.dirname(TEMP_FILE_PATH), exist_ok=True)

        # Create the temporary file if it doesn't exist
        if not os.path.exists(TEMP_FILE_PATH):
            with open(TEMP_FILE_PATH, 'w'):
                pass

    def read_temp_message(self):
        with open(TEMP_FILE_PATH, 'r') as file:
            return file.read()

    def blank_out_temp_file(file_path):
        with open(TEMP_FILE_PATH, 'w') as file:
            pass

    def monitor_temp_file(self):
        while True:
            # Check if the temporary file exists, create if necessary
            if not os.path.exists(TEMP_FILE_PATH):
                self.create_temp_file_path()

            # Read the modification time of the temporary file
            previous_mtime = os.path.getmtime(TEMP_FILE_PATH)

            # Wait for a short interval before checking again
            time.sleep(1)

            # Check if the modification time has changed
            if os.path.exists(TEMP_FILE_PATH):
                current_mtime = os.path.getmtime(TEMP_FILE_PATH)
                if current_mtime != previous_mtime:
                    # File has been modified, read the message
                    message = self.read_temp_message()
                    try:
                        # Parse the message as JSON
                        message_json = json.loads(message)
                        if len(message_json) > 1:
                            # Extract the file path from the JSON object
                            path = message_json[1].strip()  # Strip leading and trailing whitespace
                            if os.path.exists(path):
                                self.open_file(path=path)
                                self.root.lift()
                                self.root.attributes('-topmost', True)
                                self.root.after_idle(self.root.attributes, '-topmost', False)
                                self.root.after(10, self.tab_controller.current_tab.text_area.focus_force)
                                self.blank_out_temp_file()
                            else:
                                self.display_all("Another instance tried opening the following file:", path)
                    except json.JSONDecodeError:
                        self.display_all("Another instance has communicated:", message)

    def reopen_last_closed_tab(self, event=None):
        if self.recently_closed_tabs_paths:
            last_path = self.recently_closed_tabs_paths.pop()
            self.open_file(last_path)

class TextMetadataHandler:
    def __init__(self, notepad):
        self.metadata_dict = {}
        self.notepad = notepad

    def read_metadata(self, file_path):
        if os.access(file_path, os.W_OK): #only proceed if document is not read only
            try:
                if os.path.splitext(file_path)[1].lower() not in ['.png', '.jpg', 'jpeg']:
                    with open(file_path, "r", encoding="utf-8") as file:
                        file_content = file.read()
                        metadata_start_index = file_content.find("\n\n\n*** Metadata starts (notes.py) ***")
                        
                        if metadata_start_index != -1:
                            file.seek(metadata_start_index)
                            metadata_end_index = file_content.find("*** Metadata ends (notes.py) ***", metadata_start_index)
                            
                            if metadata_end_index != -1:
                                metadata_text = file_content[metadata_start_index + len("\n\n\n*** Metadata starts (notes.py) ***"):metadata_end_index]
                                tab_metadata = json.loads(metadata_text)
                                self.metadata_dict[file_path] = tab_metadata
            except Exception as e:
                pass

    def write_metadata(self, file_path, metadata):
        if os.access(file_path, os.W_OK) and os.path.splitext(file_path)[1].lower() not in ['.png', '.jpg', 'jpeg']: #only proceed if document is not read only
            try:
                with open(file_path, "r+", encoding="utf-8") as file:
                    content = file.read()
                    if "\n\n\n*** Metadata starts (notes.py) ***" in content and "*** Metadata ends (notes.py) ***" in content:
                        start_index = content.find("\n\n\n*** Metadata starts (notes.py) ***")
                        end_index = content.find("*** Metadata ends (notes.py) ***") + len("*** Metadata ends (notes.py) ***")
                        file.seek(0)
                        file.truncate()
                        file.write(content[:start_index] + content[end_index:])
                    
                    file.write(f"\n\n\n*** Metadata starts (notes.py) ***\n{json.dumps(metadata)}\n*** Metadata ends (notes.py) ***\n")
                    self.metadata_dict[file_path] = metadata
            except Exception as e:
                pass

    def get_tab_metadata(self, file_path):
        return self.metadata_dict.get(file_path, {})

    def clear_metadata_from_text_widget(self, text_widget):
        try:
            # Search for metadata boundaries in the text widget content
            start_index = text_widget.search("\n\n\n*** Metadata starts (notes.py) ***", '1.0', 'end')
            end_index = text_widget.search("*** Metadata ends (notes.py) ***", '1.0', 'end')

            if start_index and end_index:
                end_line, _ = map(int, end_index.split('.'))
                # Delete the metadata content from the text widget
                text_widget.delete(start_index, f'{end_line + 1}.0')

        except Exception as e:
            self.notepad.display(f"Error clearing metadata from text widget: {e}")

    def clear_metadata_from_text(self, text):
        try:
            # Search for metadata boundaries in the text
            start_index = text.find("\n\n\n*** Metadata starts (notes.py) ***")
            end_index = text.find("*** Metadata ends (notes.py) ***")

            if start_index != -1 and end_index != -1:
                # Find the end of the metadata content
                end_line = text.find("\n", end_index)
                if end_line != -1:
                    # Remove the metadata content from the text
                    text_without_metadata = text[:start_index] + text[end_line: + 1]

                    return text_without_metadata

        except Exception as e:
            print(f"Error removing metadata from text: {e}")

        return text 

class CustomEntryDialog:
    def __init__(self, master, title='', message=None, entry=True, initial_value=None, bg=settings.ui_bg, fg=settings.text_fg, window_title='Notepad', yes_no_prompt=False, yes='Save', no='Don\'t save', cancel='Cancel', width=450, height=250):
        self.master = master
        self.dialog = tk.Toplevel(self.master)
        self.dialog.iconbitmap(ico_path)
        self.dialog.title(window_title)
        dark_title_bar(self.dialog)
        self.dialog.lift()
        self.dialog.focus_force()
        self.master.after(100, self.dialog.focus_force)

        self.title = title
        self.message = message
        self.initial_value = initial_value
        self.bg = bg
        self.fg = fg
        self.entry = entry
        self.yes_no_prompt = yes_no_prompt
        self.yes = yes
        self.no = no
        self.cancel = cancel
        self.width = width
        self.height = height

        self.setup_ui()

        # Call the wait_window method after setting up the UI
        self.dialog.wait_window(self.dialog)

    def setup_ui(self):
        self.result = None

        self.dialog.geometry(f"{self.width}x{self.height}")

        # Calculate the center coordinates of the screen
        x = (self.dialog.winfo_screenwidth() // 2 - self.dialog.winfo_reqwidth())
        y = (self.dialog.winfo_screenheight() // 2 - self.dialog.winfo_reqheight())

        # Set the window to be centered on the screen
        self.dialog.geometry("+{}+{}".format(x, y))

        tk.Label(self.dialog, text=self.title, anchor='center', padx=3, pady=10, font=(settings.regular_font, 14)).pack(fill='both')
        if self.message is not None:
            tk.Label(self.dialog, text=self.message, anchor='center', padx=3, pady=10, wraplength=self.width-20, font=(settings.regular_font, 10)).pack(fill='both')

        if self.entry:
            self.entry_var = tk.StringVar(value=self.initial_value)
            entry_widget = tk.Entry(self.dialog, textvariable=self.entry_var, selectbackground=self.bg, selectforeground=self.fg, font=(settings.regular_font, 12))
            entry_widget.pack(fill='both', padx=5, pady=5)
            entry_widget.focus_set()  # Set focus to the entry widget
            self.master.after(100, entry_widget.focus_set)
            entry_widget.selection_range(0, tk.END)

            # Create a frame to contain the buttons
            button_frame = Frame(self.dialog)
            button_frame.pack(anchor='center', pady=15)

            # Create OK button and pack it to the left inside the frame
            ok_button = Button(button_frame, width=8, text="OK", command=self.ok_action, activebackground=self.bg)
            ok_button.pack(side='left', padx=5)

            # Create Cancel button and pack it to the right inside the frame
            cancel_button = Button(button_frame, width=8, text="Cancel", command=self.cancel_action, activebackground=self.bg)
            cancel_button.pack(side='right', padx=5)

            entry_widget.bind("<Return>", lambda event: self.ok_action())
            entry_widget.bind("<Escape>", lambda event: self.cancel_action())

        else:
            self.btn_frame = tk.Frame(self.dialog)
            button_width = 60  # Set your desired constant width



            if self.yes_no_prompt:
                yes_button = CTkButton(self.btn_frame, text=self.yes, command=self.yes_action, width=button_width, fg_color=settings.ui_bg, hover_color='green', font=(settings.bold_font, 14))
                yes_button.pack(side='left', padx=20, pady=5)

                cancel_button = CTkButton(self.btn_frame, text=self.cancel, command=self.cancel_action, width=button_width, fg_color=settings.ui_bg, hover_color='red', font=(settings.bold_font, 14))
                cancel_button.pack(side='right', padx=20, pady=5)
            else:
                spacer_label = tk.Label(self.btn_frame, width=6, bg=settings.text_bg)
                spacer_label.pack(side=LEFT)

                yes_button = CTkButton(self.btn_frame, text=self.yes, command=self.yes_action, width=button_width, fg_color=settings.ui_bg, hover_color='green', font=(settings.bold_font, 14))
                yes_button.pack(side='left', padx=5, pady=5)

                no_button = CTkButton(self.btn_frame, text=self.no, command=self.no_action, width=button_width, fg_color=settings.ui_bg, hover_color='red', font=(settings.bold_font, 14))
                no_button.pack(side='left', padx=5, pady=5)

                cancel_button = CTkButton(self.btn_frame, text=self.cancel, command=self.cancel_action, width=button_width, fg_color=settings.ui_bg, hover_color='blue', font=(settings.bold_font, 14))
                cancel_button.pack(side='left', padx=5, pady=5)

            if not self.yes_no_prompt:
                self.buttons = [yes_button, no_button, cancel_button]
            else:
                self.buttons = [yes_button, cancel_button]
            self.selected_button_index = 0  # Initial selected button index

            self.update_button_highlight()  # Highlight the initial selected button

            # Bindings for Enter, Escape, and Arrow keys
            self.dialog.bind("<Return>", lambda event: self.invoke_selected_button())
            self.dialog.bind("<Escape>", lambda event: self.cancel_action())
            self.dialog.bind("<Left>", lambda event: self.navigate_buttons(event, direction='left'))
            self.dialog.bind("<Right>", lambda event: self.navigate_buttons(event, direction='right'))

            self.btn_frame.pack(fill='both')

    def navigate_buttons(self, event, direction):
        # Logic to navigate between buttons using arrow keys
        if direction == 'left':
            self.selected_button_index = (self.selected_button_index - 1) % len(self.buttons)
        elif direction == 'right':
            self.selected_button_index = (self.selected_button_index + 1) % len(self.buttons)

        self.update_button_highlight()  # Update button highlight based on selection

    def update_button_highlight(self):
        # Update fg_color to highlight the selected button using hover color
        for i, button in enumerate(self.buttons):
            if i == self.selected_button_index:
                hover_color = button.cget('hover_color')
                button.configure(fg_color=hover_color)
            else:
                button.configure(fg_color=settings.ui_bg)  # Set the default color for other buttons

    def invoke_selected_button(self):
        # Invoke the action based on the selected button index
        selected_button = self.buttons[self.selected_button_index]
        selected_button.invoke()

    def ok_action(self):
        self.result = self.entry_var.get()
        self.dialog.destroy()

    def yes_action(self):
        self.result = "yes"
        self.dialog.destroy()

    def no_action(self):
        self.result = "no"
        self.dialog.destroy()

    def cancel_action(self):
        self.result = "cancel"
        self.dialog.destroy()



class FindReplaceDialog:
    def __init__(self, master, notepad, text_widget):
        self.master = master
        self.notepad = notepad
        self.tab = self.notepad.tab_controller.current_tab
        self.text_widget = text_widget
        self.dialog = tk.Toplevel(self.master)
        self.dialog.title('Find and Replace')
        self.dialog.geometry("300x300")
        self.dialog.wm_iconbitmap(ico_path)
        dark_title_bar(self.dialog)
        self.current_occurrence_index = -1
        self.last_highlight = None
        self.find_character_enabled = True
        self.case_sensitive = False
        self.find_words_boundary_coordinates = ('1.0', tk.END)

        # Center the window on the screen
        screen_width = self.dialog.winfo_screenwidth()
        screen_height = self.dialog.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (510/2))
        y_cordinate = int((screen_height/2) - (510/2))
        if not self.tab.read_only:
            self.dialog.geometry(f"540x100+{x_cordinate}+{y_cordinate}")
        else:
            self.dialog.geometry(f"540x50+{x_cordinate}+{y_cordinate}")

        self.setup_ui()

        self.highlight_initial_selection()

    def setup_ui(self):
        # Get the currently selected text in the text widget
        selected_text = self.text_widget.get(tk.SEL_FIRST, tk.SEL_LAST) if self.text_widget.tag_ranges(tk.SEL) else ""

        # Create labels for Find and Replace
        self.find_label = tk.Frame(self.dialog)
        self.find_label.pack(side=TOP, padx=5, pady=5, anchor='w', expand=True, fill=X)

        if not self.tab.read_only:
            self.replace_label = tk.Frame(self.dialog)
            self.replace_label.pack(side=TOP, padx=5, pady=5, anchor='w', expand=True, fill=X)

        # Create the find_entry with the selected text as the initial value
        self.find_entry = EntryWithPlaceholder(self.find_label, width=20, selectbackground=self.tab.colour, selectforeground=self.tab.foreground_colour, placeholder='Find')
        self.find_entry.insert(0, selected_text)
        self.find_entry.pack(side=LEFT, padx=2, pady=5)
        self.find_entry.focus_set()

        self.info_label = tk.Label(self.find_label, text="0 of 0", font=(settings.thin_font, 9))
        self.info_label.pack(side=LEFT, padx=2, pady=5)

        # Create buttons using the loaded images
        find_prev_button = CustomShortcutButton(self.find_label, label1=None, label2=None, bg=settings.text_bg, active_bg=self.tab.colour, active_fg=self.tab.foreground_colour, active_fg2=self.tab.foreground_colour, command=self.find_previous, img_path=r"{}\up_arrow_small.png".format(images_folder), info='Find previous')
        find_prev_button.pack(side=LEFT, padx=2, pady=5)

        find_next_button = CustomShortcutButton(self.find_label, label1=None, label2=None, bg=settings.text_bg, active_bg=self.tab.colour, active_fg=self.tab.foreground_colour, active_fg2=self.tab.foreground_colour, command=self.find_next, img_path=r"{}\down_arrow_small.png".format(images_folder), info='Find next')
        find_next_button.pack(side=LEFT, padx=2, pady=5)

        highlight_all_button = CustomShortcutButton(self.find_label, label1=None, label2=None, bg=settings.text_bg, active_bg=self.tab.colour, active_fg=self.tab.foreground_colour, active_fg2=self.tab.foreground_colour, command=self.highlight_all, img_path=r"{}\highlight_2.png".format(images_folder), info='Highlight All')
        highlight_all_button.pack(side=RIGHT, padx=2, pady=5)

        find_words_boundary_button = CustomShortcutButton(self.find_label, label1=None, label2=None, bg=settings.text_bg, active_bg=self.tab.colour, active_fg=self.tab.foreground_colour, active_fg2=self.tab.foreground_colour, command=self.toggle_find_words_in_boundaries, img_path=r"{}\selection.png".format(images_folder), info='Find in selection')
        find_words_boundary_button.pack(side=RIGHT, padx=2, pady=5)

        find_char_button = CustomShortcutButton(self.find_label, label1=None, label2=None, bg=settings.text_bg, active_bg=self.tab.colour, active_fg=self.tab.foreground_colour, active_fg2=self.tab.foreground_colour, command=self.toggle_find_whole_word, img_toggle=[r"{}\match_whole_word.png".format(images_folder), r"{}\match_whole_word_off.png".format(images_folder), not self.find_character_enabled], info='Match whole word')
        find_char_button.pack(side=RIGHT, padx=2, pady=5)

        case_sinsitive_button = CustomShortcutButton(self.find_label, label1=None, label2=None, bg=settings.text_bg, active_bg=self.tab.colour, active_fg=self.tab.foreground_colour, active_fg2=self.tab.foreground_colour, command=self.toggle_case_sensitive, img_toggle=[r"{}\match_case.png".format(images_folder), r"{}\match_case_off.png".format(images_folder), self.case_sensitive], info='Match Case')
        case_sinsitive_button.pack(side=RIGHT, padx=2, pady=5)

        if not self.tab.read_only:
            self.replace_entry = EntryWithPlaceholder(self.replace_label, width=20, selectbackground=self.tab.colour, selectforeground=self.tab.foreground_colour, placeholder='Replace')
            self.replace_entry.pack(side=LEFT, padx=2, pady=5)

            replace_button = CustomShortcutButton(self.replace_label, label1=None, label2=None, bg=settings.text_bg, active_bg=self.tab.colour, active_fg=self.tab.foreground_colour, active_fg2=self.tab.foreground_colour, command=self.replace, img_path=r"{}\replace.png".format(images_folder), info='Replace')
            replace_button.pack(side=LEFT, padx=2, pady=5)

            replace_all_button = CustomShortcutButton(self.replace_label, label1=None, label2=None, bg=settings.text_bg, active_bg=self.tab.colour, active_fg=self.tab.foreground_colour, active_fg2=self.tab.foreground_colour, command=self.replace_all, img_path=r"{}\all.png".format(images_folder), info='Replace All')
            replace_all_button.pack(side=LEFT, padx=2, pady=5)

        self.dialog.bind("<Escape>", self.on_escape)
        self.dialog.bind("<Destroy>", self.on_escape)
        self.dialog.bind('<Control-z>', lambda event: (self.notepad.undo(), self.find_next()))
        self.dialog.bind('<Control-y>', lambda event: (self.notepad.redo(), self.find_next()))
        self.dialog.bind('<Control-Z>', lambda event: (self.notepad.undo(), self.find_next()))
        self.dialog.bind('<Control-Y>', lambda event: (self.notepad.redo(), self.find_next()))
        
        self.find_entry.bind("<KeyRelease>", self.update_info_label)

    def toggle_find_whole_word(self):
        self.find_character_enabled = not self.find_character_enabled
        self.update_info_label()

    def toggle_find_words_in_boundaries(self):
        self.find_words_boundary_coordinates = self.get_selected_coordinates()
        self.current_occurrence_index = 0
        self.update_info_label()

    def toggle_case_sensitive(self):
        self.case_sensitive = not self.case_sensitive
        self.update_info_label()

    def get_selected_coordinates(self):
        # Helper method to get the coordinates of the selected text or use default if no selection
        try:
            start_pos = self.text_widget.index(tk.SEL_FIRST)
            end_pos = self.text_widget.index(tk.SEL_LAST)
            return start_pos, end_pos
        except tk.TclError:
            return '1.0', tk.END  # Use default boundaries if no selection
        finally:
            self.update_info_label()

    # Update the highlight_initial_selection method
    def highlight_initial_selection(self):
        # Get the currently selected text in the text widget
        selected_text = self.text_widget.get(tk.SEL_FIRST, tk.SEL_LAST) if self.text_widget.tag_ranges(tk.SEL) else ""
        
        if selected_text:
            selected_occurrence = (self.text_widget.index(tk.SEL_FIRST), self.text_widget.index(tk.SEL_LAST))
            all_occurrences = list(self.find_all(selected_text))
        
            if all_occurrences:
                for i, occurrence in enumerate(all_occurrences):
                    if occurrence[0] == selected_occurrence[0] and occurrence[1]:
                        self.current_occurrence_index = i - 1
                        break
                else:
                    # No exact match found, consider the first occurrence
                    self.current_occurrence_index = 0
            else:
                # No occurrences found, set index to -1
                self.current_occurrence_index = -1

            # Find the next occurrence
            self.find_next()

    def find_all(self, keyword, regexp=True):
        if keyword is None or keyword == '':
            return

        start_pos, end_pos = self.find_words_boundary_coordinates  # Use boundary coordinates
        occurrences = []

        while start_pos and start_pos < end_pos:
            try:
                if not self.find_character_enabled:
                    next_pos = self.text_widget.search(r'\y' + re.escape(keyword) + r'\y', start_pos, end_pos, regexp=True, nocase=not self.case_sensitive)
                    if next_pos:
                        occurrences.append((next_pos, f"{next_pos} + {len(keyword)}c"))
                        start_pos = f"{next_pos} + {len(keyword)}c"
                    else:
                        break
                else:
                    next_pos = self.text_widget.search(keyword, start_pos, end_pos, regexp=regexp, nocase=not self.case_sensitive)
                    if next_pos:
                        occurrences.append((next_pos, f"{next_pos} + {len(keyword)}c"))
                        start_pos = f"{next_pos} + {len(keyword)}c"
                    else:
                        break
            except tk.TclError:
                break  # Handle TclError gracefully

        return occurrences

    def find_next(self):
        keyword = self.find_entry.get()
        all_occurrences = list(self.find_all(keyword)) if self.find_all(keyword) is not None else []

        if all_occurrences:
            self.current_occurrence_index = (self.current_occurrence_index + 1) % len(all_occurrences)
            self.update_highlight(*all_occurrences[self.current_occurrence_index])
        else:
            # No occurrences found
            self.current_occurrence_index = -1

        # Update the info label
        self.info_label.config(text=f"{self.current_occurrence_index + 1} of {len(all_occurrences)}")


    def find_previous(self):
        keyword = self.find_entry.get()
        all_occurrences = list(self.find_all(keyword)) if self.find_all(keyword) is not None else []

        if all_occurrences:
            self.current_occurrence_index = (self.current_occurrence_index - 1) % len(all_occurrences)
            self.update_highlight(*all_occurrences[self.current_occurrence_index])
        else:
            # No occurrences found
            self.current_occurrence_index = -1

        # Update the info label
        self.info_label.config(text=f"{self.current_occurrence_index + 1} of {len(all_occurrences)}")

    def replace(self):
        self.notepad.save_memento()
        keyword = self.find_entry.get()
        replacement = self.replace_entry.get()

        if self.text_widget.tag_ranges("highlight"):
            start_pos = self.text_widget.tag_ranges("highlight")[0]
            end_pos = self.text_widget.tag_ranges("highlight")[1]

            self.text_widget.delete(start_pos, end_pos)
            self.text_widget.insert(start_pos, replacement)

            self.update_highlight(start_pos, f"{start_pos}+{len(replacement)}c")

            self.find_next()

    def replace_all(self):
        self.notepad.save_memento()
        keyword = self.find_entry.get()
        replacement = self.replace_entry.get()
        start_pos = '1.0'
        replacement_count = 0

        while True:
            if not self.find_character_enabled:
                start_pos = self.text_widget.search(r'\y' + re.escape(keyword) + r'\y', start_pos, tk.END, regexp=True, nocase=not self.case_sensitive)
            else:
                keyword_start_pos, keyword_end_pos = self.find_words_boundary_coordinates
                start_pos = self.text_widget.search(keyword, start_pos, keyword_end_pos, regexp=True, nocase=not self.case_sensitive)
            if not start_pos:
                break

            end_pos = f"{start_pos}+{len(keyword)}c"
            self.text_widget.replace(start_pos, end_pos, replacement)
            replacement_count += 1

            # Continue searching for the next occurrence
            start_pos = end_pos

        if replacement_count > 0:
            # If replacements were made, update the highlight to the first occurrence
            self.update_highlight('1.0', '1.0+0c')
        else:
            # No occurrences found
            self.current_occurrence_index = -1
        
        self.update_info_label()

    def update_info_label(self, event=None):
        if event:
            self.text_widget.tag_remove("sub_highlight", '1.0', tk.END)

        keyword = self.find_entry.get()
        all_occurrences = list(self.find_all(keyword)) if self.find_all(keyword) is not None else []

        selected_text = self.text_widget.get(tk.SEL_FIRST, tk.SEL_LAST) if self.text_widget.tag_ranges(tk.SEL) else ""
        
        if selected_text:
            selected_occurrence = (self.text_widget.index(tk.SEL_FIRST), self.text_widget.index(tk.SEL_LAST))

            if all_occurrences:
                for i, occurrence in enumerate(all_occurrences):
                    if occurrence[0] == selected_occurrence[0] and occurrence[1]:
                        self.current_occurrence_index = i - 1
                        break
                else:
                    # No exact match found, consider the first occurrence
                    self.current_occurrence_index = 0
            else:
                # No occurrences found, set index to -1
                self.current_occurrence_index = -1

            # Find the next occurrence
            self.find_next()
        
        else:
            self.current_occurrence_index = -1

        self.info_label.config(text=f"{self.current_occurrence_index + 1} of {len(all_occurrences)}")

    def update_highlight(self, start_pos, end_pos):
        self.text_widget.tag_remove("highlight", '1.0', tk.END)
        self.text_widget.tag_add("highlight", start_pos, end_pos)
        self.text_widget.tag_remove(tk.SEL, '1.0', tk.END)  # Remove the existing selection
        self.text_widget.tag_add(tk.SEL, start_pos, end_pos)  # Add the new selection
        self.text_widget.mark_set(tk.INSERT, end_pos)
        self.text_widget.see(tk.INSERT)

    def highlight_all(self):
        existing_ranges = []
        tag_ranges = self.text_widget.tag_ranges("sub_highlight")

        for i in range(0, len(tag_ranges), 2):
            start_pos = str(tag_ranges[i])
            end_pos = str(tag_ranges[i + 1])
            length = int(end_pos.split('.')[1]) - int(start_pos.split('.')[1])
            existing_ranges.append((start_pos, f"{start_pos} + {length}c"))

        keyword = self.find_entry.get()
        all_occurrences = list(self.find_all(keyword))

        if all_occurrences == existing_ranges:
            self.text_widget.tag_remove("sub_highlight", '1.0', tk.END)
        else:
            for occurrence in all_occurrences:
                self.text_widget.tag_add("sub_highlight", occurrence[0], occurrence[1])

    def on_escape(self, event):
        try:
            if self.text_widget.tag_ranges("highlight"):
                self.text_widget.tag_remove("highlight", '1.0', tk.END)

            if self.text_widget.tag_ranges("sub_highlight"):
                self.text_widget.tag_remove("sub_highlight", '1.0', tk.END)
        except tk.TclError:
            pass


        self.dialog.destroy()


class EntryWithPlaceholder(tk.Entry):
    def __init__(self, master=None, placeholder="", **kwargs):
        super().__init__(master, **kwargs)

        self.placeholder = placeholder
        self.default_fg_color = self["fg"]
        self.is_placeholder = False  # Flag to track if the placeholder is currently displayed
        self.bind("<FocusIn>", self.on_focus_in)
        self.bind("<FocusOut>", self.on_focus_out)
        self.put_placeholder()

    def put_placeholder(self):
        if not self.get() and not self.is_placeholder:
            self.insert(0, self.placeholder)
            self["fg"] = "grey"
            self.is_placeholder = True

    def insert(self, index, string):
        if self.is_placeholder:
            self.delete(0, "end")
            self["fg"] = self.default_fg_color
            self.is_placeholder = False
        super().insert(index, string)

    def on_focus_in(self, event):
        if self.is_placeholder:
            self.delete(0, "end")
            self["fg"] = self.default_fg_color
            self.is_placeholder = False

    def on_focus_out(self, event):
        if not self.get():
            self.put_placeholder()

class CustomShortcutButton(tk.Frame):
    all_instances = []
    def __init__(self, parent, label1=None, label2=None, command=lambda: None, bg=settings.ui_bg, 
                 fg=settings.ui_fg, fg2='#7a7a7a', active_bg=settings.selection_bg, active_fg=settings.selection_fg,
                 active_fg2='#7a7a7a', hover_bg='#757575', hover_fg=settings.text_fg, hover_fg2='black', img_path=None,
                 img_toggle=None, info=None, font=(settings.regular_font, 10), info_font=(settings.regular_font, 10)):
        
        tk.Frame.__init__(self, parent, bg=settings.ui_bg, bd=0)
        CustomShortcutButton.all_instances.append(self)

        self.bg = bg
        self.fg = fg
        self.fg2 = fg2
        self.active_bg = active_bg
        self.active_fg = active_fg
        self.active_fg2 = active_fg2
        self.hover_bg = hover_bg
        self.hover_fg = hover_fg
        self.hover_fg2 = hover_fg2
        self.info = info
        self.command = command
        self.info_font = info_font
        
        self.update_position_job_id = None

        self.hover_timer = None
        self.info_toplevel = None

        if self.info is not None:
            self.hide_info()

        if img_path is not None:
            self.img = tk.PhotoImage(file=img_path)
        else:
            self.img = None

        self.clicked = False

        if command is None:
            return

        if img_toggle is not None:
            self.img_on_path, self.img_off_path, self.img_status = img_toggle
            self.img_on = tk.PhotoImage(file=self.img_on_path)
            self.img_off = tk.PhotoImage(file=self.img_off_path)

        if label2 is None:
            self.is_label2 = False
        else:
            self.is_label2 = True

        # Outer frame containing both labels
        self.outer_frame = tk.Frame(self, bg=self.bg, bd=0)

        self.label1 = tk.Label(self.outer_frame, text=label1, bg=self.bg, fg=self.fg, anchor='w', padx=5, image=self.img, font=font)
        self.label1.pack(side='left', expand=True, fill='both')
        self.label1.bind("<Button-1>", lambda event: self.on_click(command))

        if self.is_label2:
            self.label2 = tk.Label(self.outer_frame, text=label2, bg=self.bg, fg=self.fg2, anchor='e', padx=5, font=font)
            self.label2.pack(side='right', expand=True, fill='both')
            self.label2.bind("<Button-1>", lambda event: self.on_click(command))

        if hasattr(self, 'img_status'):
            self.toggle_image(update=False)

        self.outer_frame.bind("<Enter>", lambda event: self.on_hover())
        self.outer_frame.bind("<Leave>", lambda event: self.on_leave())
        self.outer_frame.pack(side='left', expand=True, fill='both')

    def start_hover_timer(self):
        # Start the hover timer when mouse enters the button
        self.hover_timer = self.after(750, self.show_info)

    def show_info(self):
        # Show the info label in a new Toplevel
        self.hide_info_all()
        if self.info is not None:
            cursor_width, cursor_height = 16, 16  # Hardwired cursor dimensions, adjust as needed
            self.info_toplevel = tk.Toplevel(self.master)
            self.info_toplevel.wm_overrideredirect(True)

            def update_position():
                if hasattr(self, 'info_toplevel') and self.info_toplevel and self.info_toplevel.winfo_exists():
                    x, y = self.winfo_pointerx() + cursor_width, self.winfo_pointery() + cursor_height
                    screen_width = self.info_toplevel.winfo_screenwidth()
                    label_width = self.info_toplevel.winfo_width()
                    if x + label_width > screen_width:  # Check if label collides with right side of the screen
                        x = screen_width - label_width
                    try:
                        self.info_toplevel.wm_geometry(f"+{x}+{y}")
                    except tk.TclError:
                        pass  # Ignore TclError due to the window being closed
                    self.update_position_job_id = self.after(10, update_position)  # Update position every 10 milliseconds

            update_position()

            info_label = tk.Label(self.info_toplevel, text=self.info, bg=self.bg, fg=self.fg, relief=GROOVE, padx=5, pady=5, font=self.info_font)
            info_label.pack()

            # Schedule the task to close the Toplevel after 3 seconds
            if settings.info_labels_timer:
                self.info_toplevel.after(5000, lambda: self.info_toplevel.destroy())

    def hide_info(self):
        if hasattr(self, 'info_toplevel') and self.info_toplevel and self.info_toplevel.winfo_exists():
            self.info_toplevel.destroy()

        # Cancel the scheduled update_position task
        if self.update_position_job_id is not None:
            self.after_cancel(self.update_position_job_id)

    @classmethod
    def hide_info_all(cls):
        for instance in cls.all_instances:
            instance.hide_info()

    def on_hover(self):
        if not self.clicked:
            self.label1.config(bg=self.hover_bg, fg=self.hover_fg)
            if self.is_label2:
                self.label2.config(bg=self.hover_bg, fg=self.hover_fg2)

        if self.info is not None:
            self.start_hover_timer()

    def on_leave(self):
        if not self.clicked:
            self.label1.config(bg=self.bg, fg=self.fg)
            if self.is_label2:
                self.label2.config(bg=self.bg, fg=self.fg2)

        if self.hover_timer is not None:
            self.after_cancel(self.hover_timer)

        self.hide_info_all()

    def on_click(self, command):
        self.clicked = True
        self.label1.config(bg=self.active_bg, fg=self.active_fg)  # Change to your desired click colors
        if self.is_label2:
            self.label2.config(bg=self.active_bg, fg=self.active_fg2)
        self.hide_info()
        if self.hover_timer is not None:
            self.after_cancel(self.hover_timer)
        # Delay the color change back to the original state
        self.after(300, lambda: self.reset_colors(command))

    def reset_colors(self, command):
        self.clicked = False
        if self.label1.winfo_exists():  # Check if label1 still exists
            self.label1.config(bg=self.bg, fg=self.fg)
        if self.is_label2 and self.label2.winfo_exists():  # Check if label2 still exists
            self.label2.config(bg=self.bg, fg=self.fg2)

        if hasattr(self, 'img_status'):
            self.toggle_image()
        
        command()

    def toggle_image(self, event=None, update=True):
        if update:
            self.img_status = not self.img_status

        if self.img_status:
            self.label1.config(image=self.img_on)
        elif not self.img_status:
            self.label1.config(image=self.img_off)

    def invoke(self):
        self.on_click(self.command)

    def invoke_no_command(self):
        self.on_click(lambda: None)

class ReorderableListWindow:
    def __init__(self, master=None, items=None, notepad=None, **kwargs):
        self.text_area = None
        self.master = master
        self.notepad = notepad
        self.tab = notepad.tab_controller.current_tab
        self.reorderable_list = tk.Toplevel(self.master)
        self.reorderable_list.title("Rearrange Rows")
        self.reorderable_list.wm_iconbitmap(ico_path)
        dark_title_bar(self.reorderable_list)
        self.border_threshold = 20

        treeview_style = ttk.Style()
        row_height = int(settings.font_size * self.tab.zoom_factor * 2)
        treeview_style.configure("Treeview", background=settings.text_bg, highlightthickness=0, bd=0, font=(self.tab.font if self.tab.font else settings.text_font, int(settings.font_size * self.tab.zoom_factor)), rowheight=row_height) # Modify the font of the body
        #treeview_style.configure("Treeview.Heading", font=('Consolas', 12,'bold')) # Modify the font of the headings
        treeview_style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])

        treeview_style.map("Treeview", background=[("selected", self.tab.subcolour)], foreground=[("selected", self.tab.foreground_subcolour)])

        self.treeview = ttk.Treeview(self.reorderable_list, columns=("Item",), show="", selectmode="browse", style="Treeview")
        self.treeview.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.treeview.focus_set()

        # Configure tags for row and individual columns
        self.treeview.tag_configure('row', background=settings.text_bg, foreground=settings.text_fg)

        # Create and pack the scrollbar
        self.ctk_textbox_scrollbar = customtkinter.CTkScrollbar(self.treeview, command=self.treeview.yview, orientation="vertical", fg_color=settings.text_bg, button_color='#757575' if settings.use_tab_colours else None, button_hover_color=self.tab.colour if settings.use_tab_colours else None)

        if items:
            for item in items:
                # Insert item and apply tags
                item_id = self.treeview.insert("", "end", values=(f"{item}\u200B",))
                self.treeview.item(item_id, tags=('row',))

        self.treeview.bind("<ButtonPress-1>", self.on_press)
        self.treeview.bind("<B1-Motion>", self.on_drag)
        self.treeview.bind("<ButtonRelease-1>", self.on_release)
        self.treeview.bind("<Left>", self.move_row_up)
        self.treeview.bind("<Right>", self.move_row_down)
        self.treeview.bind('<Control-z>', lambda event: self.notepad.undo())
        self.treeview.bind('<Control-y>', lambda event: self.notepad.redo())
        self.treeview.bind('<Control-Z>', lambda event: self.notepad.undo())
        self.treeview.bind('<Control-Y>', lambda event: self.notepad.redo())
        self.treeview.bind('<Return>', self.exit)
        self.treeview.bind('<Escape>', self.exit)
        self.drag_data = {'x': 0, 'y': 0, 'item': None, 'window': None}

        self.treeview.focus_force()

        # Calculate and set the initial window size
        self.update_window_size()

        self.ctk_textbox_scrollbar.pack(side="right", fill="y")

        # Configure the treeview to use the scrollbar
        self.treeview.configure(yscrollcommand=self.ctk_textbox_scrollbar.set)

        self.toggle_scrollbar_visibility(enable=True)

    def toggle_scrollbar_visibility(self, enable=None):
        if enable is not None:
            # If enable argument is provided, set the scrollbar state accordingly
            if enable:
                self.ctk_textbox_scrollbar.configure(width=15)  # Adjust the width as needed
            else:
                self.ctk_textbox_scrollbar.configure(width=0)
        else:
            # If enable argument is not provided, toggle the scrollbar state
            current_width = self.ctk_textbox_scrollbar.cget("width")
            if current_width == 0:
                self.ctk_textbox_scrollbar.configure(width=15)  # Adjust the width as needed
            else:
                self.ctk_textbox_scrollbar.configure(width=0)

    def update_window_size(self):
        if self.text_area and isinstance(self.text_area, tk.Text):
            num_rows = int(self.text_area.index('end-1c').split('.')[0])  # Count the number of rows in the text area
            min_height = 2  # Minimum height in rows
            suggested_height = max(num_rows, min_height)  # Use the larger of num_rows and min_height
            row_height = 20  # Assuming each row is 30 pixels high
            final_height = max(suggested_height * row_height, min_height * row_height)+2  # Use the larger of the two

            # Hardwired maximum values for width and height
            max_width = 400
            max_height = 600

            # Calculate the maximum line length
            max_line_length = max(len(line) for line in self.text_area.get("1.0", tk.END).split("\n"))

            self.treeview.selection_set(self.treeview.get_children()[int(self.notepad.tab_controller.current_tab.text_area.index(tk.INSERT).split('.')[0]) - 1])
            selected_item = self.treeview.selection()[0]
            self.treeview.focus(selected_item)
            self.treeview.see(selected_item)

            # Calculate the width based on the maximum line length
            calculated_width = max_line_length * 5  # Assuming each character is 10 pixels wide

            # Use the hardwired maximum width if the calculated width exceeds it
            final_width = min(calculated_width, max_width)

            # Calculate the height based on the number of lines in the text area
            num_lines = len(self.text_area.get("1.0", tk.END).split("\n"))
            calculated_height = num_lines * 20  # Assuming each line is 20 pixels high

            # Use the hardwired maximum height if the calculated height exceeds it
            final_height = min(calculated_height, max_height)

            self.reorderable_list.geometry(f"{final_width}x{final_height}")

            # Calculate the center coordinates of the screen
            x = (self.reorderable_list.winfo_screenwidth() // 2 - self.reorderable_list.winfo_reqwidth())
            y = (self.reorderable_list.winfo_screenheight() // 2 - self.reorderable_list.winfo_reqheight())

            # Set the window to be centered on the screen
            self.reorderable_list.geometry("+{}+{}".format(x, y))


    def on_press(self, event):
        item_id = self.treeview.identify_row(event.y)
        if item_id:
            # Change the appearance of the selected row (set background color to empty or any desired effect)
            self.treeview.item(item_id, tags=("empty_row",))
            self.drag_data['item'] = item_id
            self.drag_data['x'] = event.x_root
            self.drag_data['y'] = event.y_root
            self.create_drag_window()

    def create_drag_window(self):
        item_id = self.drag_data['item']
        item_values = self.treeview.item(item_id)['values'][0]

        x, y, width, height = self.treeview.bbox(item_id)

        self.drag_data['window'] = tk.Toplevel(self.reorderable_list)
        self.drag_data['window'].withdraw()
        self.drag_data['window'].overrideredirect(True)
        self.drag_data['window'].geometry(f"{width}x{height}+{self.drag_data['x']-x}+{self.drag_data['y']-y}")

        label = ttk.Label(self.drag_data['window'], text=item_values, anchor="w", background=settings.text_bg, foreground=settings.text_fg, font=(self.tab.font if self.tab.font else settings.text_font, int(settings.font_size * self.tab.zoom_factor)))
        label.pack(fill="both", expand=True)

    def on_drag(self, event):
        if self.drag_data['window'] is not None:
            item_id = self.drag_data['item']
            try:
                x, y, width, height = self.treeview.bbox(item_id)
                x, y = event.x_root - self.drag_data['x'], event.y_root - self.drag_data['y']
                self.drag_data['window'].geometry(f"{width}x{height}+{event.x_root - width // 2}+{event.y_root - height // 2}")
                self.drag_data['window'].deiconify()

                destination_item = self.treeview.identify_row(event.y)
                if destination_item and destination_item != self.drag_data['item']:
                    destination_index = self.treeview.index(destination_item)
                    self.treeview.move(self.drag_data['item'], "", destination_index)

                # Update the mouse position for smooth dragging
                self.drag_data['x'] = event.x_root
                self.drag_data['y'] = event.y_root

                # Update the main window's text after rearranging the rows
                self.update_main_window_text()
            except:
                pass
            finally:
                # Check if the mouse is near the top edge
                if event.y < self.border_threshold:
                    # Scroll up
                    self.treeview.yview_scroll(-1, "units")
                    self.tab.text_area.yview_scroll(-1, "units")
                # Check if the mouse is near the bottom edge
                elif event.y > self.treeview.winfo_height() - self.border_threshold:
                    # Scroll down
                    self.treeview.yview_scroll(1, "units")
                    self.tab.text_area.yview_scroll(1, "units")

    def on_release(self, event):
        if self.drag_data['window'] is not None:
            self.drag_data['window'].destroy()
            self.drag_data['window'] = None

            # Reset the appearance of the selected row
            self.treeview.item(self.drag_data['item'], tags=('row',))

            # Update the main window's text after rearranging the rows
            self.update_main_window_text()

        if self.notepad:
            self.notepad.save_memento()

    def update_main_window_text(self):
        # Get the current text content and ranges
        current_text = self.text_area.get(1.0, tk.END)
        current_ranges = self.text_area.tag_ranges("strikethrough")

        # Group the ranges into tuples (start, end)
        grouped_ranges = [(current_ranges[i], current_ranges[i+1]) for i in range(0, len(current_ranges), 2)]

        # Extract lines from the current text
        initial_lines = current_text.split('\n')

        new_text_order = []
        for item_id in self.treeview.get_children():
            values = self.treeview.item(item_id)['values']
            if values:
                new_text_order.append(str(values[0].strip("\u200B")))

        # Join lines to form the new text
        new_text = "\n".join(new_text_order)

        # Extract lines from the new text
        final_lines = new_text.split('\n')

        # Create a dictionary to store the changes in line positions
        line_changes = {}

        # Compare initial and final lines to identify changes in position
        for initial_idx, line in enumerate(initial_lines):
            if line != '':
                try:
                    final_idx = final_lines.index(line)
                    if initial_idx != final_idx:
                        line_changes[initial_idx + 1] = final_idx + 1
                except ValueError:
                    # Line not found in the final text
                    line_changes[initial_idx + 1] = None

        # Insert new text
        self.text_area.replace(1.0, tk.END,  new_text)

        # Restore strikethrough ranges
        for start, end in grouped_ranges:
            # Adjust the coordinates
            start_line, _ = map(int, str(start).split('.'))
            end_line, _ = map(int, str(end).split('.'))

            if start_line in line_changes:
                start_line = line_changes[start_line]
            else:
                new_start = str(start)

            # Check if the end line was changed
            if end_line in line_changes:
                end_line = line_changes[end_line]
            else:
                new_end = str(end)

            new_start = f"{start_line}.{str(start).split('.')[1]}"
            new_end = f"{end_line}.{str(end).split('.')[1]}"

            # Add the adjusted coordinates
            self.text_area.tag_add("strikethrough", new_start, new_end)

    def move_row_up(self, event):
        selected_item = self.treeview.selection()
        if selected_item:
            current_index = self.treeview.index(selected_item)
            if current_index > 0:
                new_index = current_index - 1
            else:
                new_index = len(self.treeview.get_children()) - 1
            self.treeview.move(selected_item, "", new_index)
            self.treeview.see(selected_item)
            self.update_main_window_text()

            if self.notepad:
                self.notepad.save_memento()

    def move_row_down(self, event):
        selected_item = self.treeview.selection()
        if selected_item:
            current_index = self.treeview.index(selected_item)
            if current_index < len(self.treeview.get_children()) - 1:
                new_index = current_index + 1
            else:
                new_index = 0
            self.treeview.move(selected_item, "", new_index)
            self.treeview.see(selected_item)
            self.update_main_window_text()

            if self.notepad:
                self.notepad.save_memento()

    def exit(self, event=None):
        self.reorderable_list.destroy()



class ReorderableListWidget(tk.Frame):
    def __init__(self, master=None, items=None, tab=None, selection_index=0, **kwargs):
        super().__init__(master, **kwargs)
        self.tab = tab
        self.notepad = tab.notepad
        self.is_item_released = True
        self.border_threshold = 20


        treeview_style = ttk.Style()
        row_height = int(settings.font_size * self.tab.zoom_factor * 2)
        treeview_style.configure("Treeview", background=settings.text_bg, highlightthickness=0, bd=0, font=(tab.font if tab.font else settings.text_font, int(settings.font_size * self.tab.zoom_factor)), rowheight=row_height, autoseparators=True)
        #treeview_style.configure("Treeview.Heading", font=('Consolas', 12,'bold')) # Modify the font of the headings
        treeview_style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])

        treeview_style.map("Treeview", background=[("selected", self.tab.subcolour)], foreground=[("selected", self.tab.foreground_subcolour)])

        self.treeview = ttk.Treeview(self, columns=("Item",), show="", selectmode="browse", style="Treeview")
        self.treeview.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.treeview.focus_set()

        # Configure tags for row and individual columns
        self.treeview.tag_configure('row', background=settings.text_bg, foreground=settings.text_fg)

        if items:
            for item in items:
                # Insert item and apply tags
                item_id = self.treeview.insert("", "end", values=(f"{item}\u200B",))
                self.treeview.item(item_id, tags=('row',))

        self.treeview.bind("<ButtonPress-1>", self.on_press)
        self.treeview.bind("<B1-Motion>", self.on_drag)
        self.treeview.bind("<ButtonRelease-1>", self.on_release)
        self.treeview.bind("<Left>", self.move_row_up)
        self.treeview.bind("<Right>", self.move_row_down)
        self.treeview.bind("<Escape>", lambda event: self.tab.cancel_button.invoke())
        self.treeview.bind("<Return>", lambda event: self.tab.done_button.invoke())
        #self.treeview.bind("<Control-z>", self.undo_and_return_break)
        #self.treeview.bind("<Control-y>", self.redo_and_return_break)
        self.drag_data = {'x': 0, 'y': 0, 'item': None, 'window': None}
        self.undo_stack = []
        self.redo_stack = []
        self.max_undo_steps = settings.max_undo_steps
        self.max_redo_steps = settings.max_redo_steps

        try:
            self.treeview.selection_set(self.treeview.get_children()[selection_index + 1])
        except:
            self.treeview.selection_set(self.treeview.get_children()[selection_index])
        selected_item = self.treeview.selection()[0]
        self.treeview.focus(selected_item)
        self.treeview.see(selected_item)

    def undo(self, event=None):
        if self.undo_stack:
            item_id, new_index = self.undo_stack.pop()
            current_index = self.treeview.index(item_id)
            self.redo_stack.append((item_id, current_index))
            self.treeview.move(item_id, "", new_index)
            self.treeview.see(item_id)
            self.treeview.selection_set(item_id)

    def redo(self, event=None):
        if self.redo_stack:
            item_id, new_index = self.redo_stack.pop()
            current_index = self.treeview.index(item_id)
            self.undo_stack.append((item_id, current_index))
            self.treeview.move(item_id, "", new_index)
            self.treeview.see(item_id)
            self.treeview.selection_set(item_id)

    def record_undo(self, item_id, current_index):
        self.undo_stack.append((item_id, current_index))

    def on_press(self, event):
        item_id = self.treeview.identify_row(event.y)
        if item_id:
            # Change the appearance of the selected row (set background color to empty or any desired effect)
            self.treeview.item(item_id)
            self.drag_data['item'] = item_id
            self.drag_data['x'] = event.x_root
            self.drag_data['y'] = event.y_root
            self.create_drag_window()

    def create_drag_window(self):
        item_id = self.drag_data['item']
        item_values = self.treeview.item(item_id)['values'][0]

        try:
            x, y, width, height = self.treeview.bbox(item_id)
        except:
            return

        self.drag_data['window'] = tk.Toplevel(self.master)
        self.drag_data['window'].withdraw()
        self.drag_data['window'].overrideredirect(True)
        self.drag_data['window'].geometry(f"{width}x{height}+{16 if settings.text_gaps else 0}+{self.drag_data['y']-y}")

        label = ttk.Label(self.drag_data['window'], text=item_values, style="Row.TLabel", anchor="w", background=self.tab.colour, foreground=self.tab.foreground_colour, font=(self.tab.font if self.tab.font else settings.text_font, int(settings.font_size * self.tab.zoom_factor)))
        label.pack(fill="both", expand=True)

    def on_drag(self, event):
        if self.drag_data['window'] is not None:
            item_id = self.drag_data['item']
            try:
                x, y, width, height = self.treeview.bbox(item_id)

                x, y = 0, event.y_root - self.drag_data['y']
                
                # Calculate the width of content on the right side
                #right_content_width = self.master.winfo_screenwidth() - (event.x_root + width)

                # Calculate the x-coordinate to keep the window aligned with the left side
                #x_coord = max(self.tab.lines_label.winfo_reqwidth() + 4, event.x_root - width - right_content_width)
                
                self.drag_data['window'].geometry(f"{width}x{height}+{16 if settings.text_gaps else 0}+{event.y_root - height // 2}")
                self.drag_data['window'].deiconify()

                destination_item = self.treeview.identify_row(event.y)
                if destination_item and destination_item != self.drag_data['item']:
                    destination_index = self.treeview.index(destination_item)
                    if self.is_item_released:
                        self.record_undo(self.drag_data['item'], self.treeview.index(self.drag_data['item']))
                        self.is_item_released = False
                    self.treeview.move(self.drag_data['item'], "", destination_index)

                # Update the mouse position for smooth dragging
                self.drag_data['x'] = event.x_root
                self.drag_data['y'] = event.y_root
            except:
                pass
            finally:
                # Check if the mouse is near the top edge
                if event.y < self.border_threshold:
                    # Scroll up
                    self.treeview.yview_scroll(-1, "units")
                # Check if the mouse is near the bottom edge
                elif event.y > self.treeview.winfo_height() - self.border_threshold:
                    # Scroll down
                    self.treeview.yview_scroll(1, "units")

    def on_release(self, event):
        if self.drag_data['window'] is not None:
            self.drag_data['window'].destroy()
            self.drag_data['window'] = None

            # Reset the appearance of the selected row
            self.treeview.item(self.drag_data['item'], tags=('row',))
            self.update_saved_text()

            self.is_item_released = True

    def move_row_up(self, event):
        selected_item = self.treeview.selection()
        if selected_item:
            current_index = self.treeview.index(selected_item)
            if current_index > 0:
                new_index = current_index - 1
            else:
                new_index = len(self.treeview.get_children()) - 1
            self.treeview.move(selected_item, "", new_index)
            self.treeview.see(selected_item)
            self.record_undo(selected_item, current_index)
            self.update_saved_text()

    def move_row_down(self, event):
        selected_item = self.treeview.selection()
        if selected_item:
            current_index = self.treeview.index(selected_item)
            if current_index < len(self.treeview.get_children()) - 1:
                new_index = current_index + 1
            else:
                new_index = 0
            self.treeview.move(selected_item, "", new_index)
            self.treeview.see(selected_item)
            self.record_undo(selected_item, current_index)
            self.update_saved_text()


    def update_saved_text(self):
        # Get the current text content and ranges
        current_text = self.tab.saved_text
        current_ranges = self.tab.saved_strikethrough_ranges

        # Group the ranges into tuples (start, end)
        grouped_ranges = [(current_ranges[i], current_ranges[i+1]) for i in range(0, len(current_ranges), 2)]

        # Extract lines from the current text
        initial_lines = current_text.split('\n')

        new_text_order = []
        for item_id in self.treeview.get_children():
            values = self.treeview.item(item_id)['values']
            if values:
                new_text_order.append(str(values[0].strip("\u200B")))

        # Join lines to form the new text
        new_text = "\n".join(new_text_order)

        # Extract lines from the new text
        final_lines = new_text.split('\n')

        # Create a dictionary to store the changes in line positions
        line_changes = {}

        # Compare initial and final lines to identify changes in position
        for initial_idx, line in enumerate(initial_lines):
            if line != '':
                try:
                    final_idx = final_lines.index(line)
                    if initial_idx != final_idx:
                        line_changes[initial_idx + 1] = final_idx + 1
                except ValueError:
                    # Line not found in the final text
                    line_changes[initial_idx + 1] = None

        # Update the current text variable
        self.tab.reordered_text = new_text

        new_ranges = []
        # Restore strikethrough ranges
        for start, end in grouped_ranges:
            # Adjust the coordinates
            start_line, _ = map(int, str(start).split('.'))
            end_line, _ = map(int, str(end).split('.'))

            if start_line in line_changes:
                start_line = line_changes[start_line]
            else:
                new_start = str(start)

            # Check if the end line was changed
            if end_line in line_changes:
                end_line = line_changes[end_line]
            else:
                new_end = str(end)

            new_start = f"{start_line}.{str(start).split('.')[1]}"
            new_end = f"{end_line}.{str(end).split('.')[1]}"

            new_ranges.extend([new_start, new_end])

        # Update the current ranges variable
        self.tab.reordered_strikethrough_ranges = new_ranges

    def apply_changes(self, event=None):
        #print(self.tab.reordered_text)
        self.tab.tab_controller.refresh_tabs()
        self.notepad.disable_escape_app = False
        #self.notepad.root.after(500, self.notepad.zoom_refresh)


    def cancel_changes(self, event=None):
        self.tab.reordered_text = self.tab.saved_text
        self.tab.reordered_strikethrough_ranges = self.tab.saved_strikethrough_ranges
        self.tab.tab_controller.refresh_tabs()
        self.notepad.disable_escape_app = False
        #self.notepad.root.after(500, self.notepad.zoom_refresh)
        return "break"



@atexit.register
def delete_temp_file():
    global DELETE_TEMP_FILE
    if os.path.exists(TEMP_FILE_PATH) and DELETE_TEMP_FILE:
        os.remove(TEMP_FILE_PATH)

def write_message(message):
    with open(TEMP_FILE_PATH, 'w') as file:
        file.write(message)

def is_another_instance_running():
    # Check if the temporary file exists
    if not os.path.exists(TEMP_FILE_PATH):
        # If the file does not exist, create it
        with open(TEMP_FILE_PATH, 'w'):
            pass
        # No other instance is running
        return False
    # Another instance is already running
    return True

def pass_sys_argv():
    # Serialize sys.argv to a JSON string
    argv_json = json.dumps(sys.argv)
    write_message(argv_json)

if __name__ == "__main__":

    if not settings.new_window_when_opening and is_another_instance_running():
        if len(sys.argv) > 1:
            #print("Another instance is already running.")
            pass_sys_argv()
            DELETE_TEMP_FILE = False
    else:
        #print("No other instance is running.")
        if len(sys.argv) > 1:
            cmd_path = sys.argv[1]

        else:
            cmd_path = None

        # Run main application
        notepad = Notepad()
        notepad.run()


r'''
Create .exe executable:

cd C:\Python Projects\Notetaking
C:\Users\namye\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\Scripts\auto-py-to-exe.exe

or

cd C:\Python Projects\Notetaking
C:\Users\namye\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\Scripts\pyinstaller --noconfirm --onedir --windowed --icon "C:/Python Projects/Notetaking/resources/images/ico/icons8-note-96.ico" --add-data "C:/Python Projects/Notetaking/config.toml;." --add-data "C:/Python Projects/Notetaking/config_default.toml;." --add-data "C:/Python Projects/Notetaking/last_opened_files.toml;." --add-data "C:/Python Projects/Notetaking/ReadMe.txt;." --add-data "C:/Python Projects/Notetaking/resources;resources/" --add-data "C:/Python Projects/Notetaking/additional_resources/spellchecker;spellchecker/"  "C:/Python Projects/Notetaking/Yeongu Notes.pyw"

'''