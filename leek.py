####################################################
# leek - the file manager
# - name    - leek (leek.py)
# - author  - Otakar Kočí (Otas02CZ)
# - date    - 2021 - 2022
# - description
# -  - lehky konzolovy spravce souboru pro windows operacni system
# -  - min verze pythonu je python 3.10 a win pravdepodobne win 8
####################################################

# IMPORTY ##########################################
import os
import pathlib
import shutil
import operator
from rich import print as rprint
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.prompt import Prompt as prompt
from rich.prompt import Confirm as confirm
from rich.table import Table
from rich.text import Text
from datetime import datetime
from configuration import Configuration
from localization import Localization
####################################################

class CFG:
    VERSION = "1.2.1"
    AUTHOR = "Otakar Kočí"
    DATE = "08/08/2022"
    WEBPAGE = ""
    GITHUB = ""
    PYTHON_VERSION = "3.10 (3.10.6)"
    RICH_VERSION = "12.5.1"
    PYINSTALLER_VERSION = "5.3"
    UPX_VERSION = "3.96"
    ZIP7_VERSION = "22.01"

# GLOBALNI PROMENNE ################################
console = Console()                         # objekt konzole pro vyuziti nekterych funkci knihovny rich
layout = Layout()                           # objekt layoutu pro vyuziti nekterych funkci knihovny rich
user_input = []                             # uklada se zde prikazovy input se vsemi parametry od uzivatele ke zpracovani
command = ""                                # globalni promenna pro ulozeni aktualniho prikazu
to_select = []                              # promenna seznamu polozek k poznaceni
selected = []                               # promenna seznamu polozek poznacenych
location = "root"                           # aktualni umisteni do ktereho se divame, root je pro zobrazeni korenu disku
drives = []                                 # promenna seznamu vsech disku
search_result = []                          # promenna seznamu vysledku vyhledavani
sort_result = []                            # promenna seznamu vysledku serazeni
viewable = []                               # dictionary zobrazitelnych polozek v aktualnim umisteni
visible = []                               # dictionary prave zobrazenych polozek v aktualnim umisteni podle promenne page
errors = []                                 # promenna seznamu erroru a take vsech chybovych hlaseni
info = []                                   # promenna seznamu informacnich a pozitivnich zprav od programu
page = 1                                    # aktualni strana
max_page = 1                                # celkovy pocet vsech stran
to_open = 0                                 # index polozky na strance aktualni zobrazene k otevreni
table = Table()                             # objekt tabulky pro vyuziti nekterych funkci knihovny rich
up = 0                                      # o kolik se posunouti
drive = ""                                  # aktualni disk
direction = ""                              # kterym smerem se posunout mezi stranami
distance = 0                                # o kolik se posunouti mezi stranami
type_select = ""                            # prepina mezi typem selectu
dirsize = 0                                 # uklada velikost zvoleneho adresare
successful = 0                              # pocet operaci uspesne zvladnutych
failed = 0                                  # pocet operaci neuspesne selhanych
new_dir = ""                                # nazev pro novy adresar
r_new_name = ""                             # novy nazev k prejmenovani vybrane polozky nebo take vybranych polozek
r_place = ""                                # umisteni pro pocitadlo pri prejmenovani polozek
r_counter_begin = 0                         # pocatek pocitadla
r_increment = 0                             # udava o kolik se pocitadlo meni
r_n_digit = 0                               # minimalni pocet cisel v prejmenovanem nazvu
r_file_type = ""                            # druhy nazev nebo koncovka k prejmenovani vybrane polozky nebo take vybranych polozek
r_advanced = False                          # pouziva se funkce pocitadla pro prejmenovani
pre_select = ""                             # umisteni pred zobrazenim selectu
pre_search = ""                             # umisteni pred pred zobrazenim searchu
find = ""                                   # hledany vyraz

####################################################

def get_list_of_drives() -> list:
    r"""
    Zjistí seznam windows-like disků na počítači a vráti jej v podobě listu.
    """
    
    drives = []
    dl = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for letter in dl:
        if os.path.exists(letter + ":"):
            drives.append(letter + ":\\\\")
    return drives

def get_list_of_files(location) -> list:
    r"""
    Získá seznam souborů a složek v adresáři z argumentu location a vrátí jej v podobě listu.
    Pokud dojde k chybě vrátí False.
    
    Arguments:
     - location (string) -> adresář pro získání seznamu souborů a složek
    """
    
    global errors
    try:
        return os.listdir(location)
    except:
        errors.append("permission_error")
        return False

def remove_file(location) -> bool:
    r"""
    Odstraní soubor, jehož cesta je specifikována v parametru location.
    Pokud dojde k chybě vrací False, jinak True.
    
    Arguments:
     - location (string) -> jako cesta k souboru k odstranění
    """
    
    try:
        os.remove(location)
        return True
    except:
        return False

def remove_directory(location) -> bool:
    r"""
    Odstraní složku, jejíž cesta je specifikována v parametru location.
    Pokud dojde k chybě vrací False, jinak True.
    
    Arguments:
     - location (string) -> jako cesta ke složce k odstranění
    """
    
    try:
        os.rmdir(location)
        return True
    except:
        return False

def remove_tree_directory(location) -> bool:
    r"""
    Odstraní složku s podsložkami, jejíž cesta je specifikována v parametru location.
    Pokud dojde k chybě vrací False, jinak True.
    
    Arguments:
     - location (string) -> jako cesta ke složce s podsložkami k odstranění
    """
    
    try:
        shutil.rmtree(location)
        return True
    except:
        return False

def create_directory(location, name) -> bool:
    r"""
    Vytvoří složku v zadaném adresáři se zadaným jménem.
    V případě chyby vrátí False, jinak vrátí True.
    
    Arguments:
     - location - jako cesta k umístění, kde se má vytvořit nová složka
     - name     - jako název nové složky
    """
    
    try:
        os.mkdir(location + "\\" + name)
        return True
    except:
        return False

def rename_file_or_directory(location, new) -> bool:
    r"""
    Přejmenuje soubor či složku v umístění z location na název přijatý v new.
    V případě chyby vrátí False, jinak vrátí True

    Arguments:
     - location (String) - cesta k souboru či složce k přejmenování (i s vlastním názvem)
     - new      (String) - nový název pro soubor k přejmenování
    """
    
    old = os.path.basename(location)
    try:
        os.rename(location, location.replace(old, new))
        return True
    except:
        return False

def get_info_about_file(location) -> os.stat_result:
    r"""
    Vrátí informace o souboru či složce v umístění z location získané pomocí funkce os.stat()

    Arguments:
     - location (String) - jako cesta k souboru či složce
    """
    
    try:
        return os.stat(location)
    except:
        return False

def move_file_or_directory(source, destination) -> bool:
    r"""
    Přesune soubor či složku z cesty v source do cesty v destination
    V případě chyby vrátí False, jinak vrátí True

    Arguments:
     - source (String)      - jako cesta k souboru či složce (i s názvem)
     - destination (String) - jako cesta k umístění kam se vše přesune (i s názvem)
    """
    
    try:
        shutil.move(source, destination)
        return True
    except:
        return False

def copy_entire_directory(source, destination) -> bool:
    r"""
    Zkopíruje celou složku se všemi věcmi vnořenými z umístění v source do umístění v destination
    V případě chyby vrátí False, jinak vrátí True

    Arguments:
     - source (String)      - jako cesta k souboru či složce (i s názvem)
     - destination (String) - jako cesta k umístění kam se vše zkopíruje (i s názvem) 
    """
    
    try:
        shutil.copytree(source, destination)
        return True
    except:
        return False

def copy_file(source, destination) -> bool:
    r"""
    Zkopíruje soubor z umístění v source do umístění v destination
    V případě chyby vrátí False, jinak vrátí True

    Arguments:
     - source (String)      - jako cesta k souboru či složce (i s názvem)
     - destination (String) - jako cesta k umístění kam se zkopíruje (i s názvem) 
    """
    try:
        shutil.copyfile(source, destination)
        return True
    except:
        return False
    
def is_numeric(word) -> bool:
    r"""
    Vyzkouší jestli string word je validní číslo, pokud ano vrátí True, jinak False

    Arguments:
     - word (String) - text, který má být zkontrolován, zda se jedná o validní číslo
    """
    
    word = word.strip()
    try:
        word = int(word)
        return True
    except:
        return False

def check_input(input) -> bool:
    r"""
    Zkontroluje jestli input zadaný od uživatele není prázdný
    a pokud není, tak jej rozdělí na substringy a uloží do
    globální proměnné user_input. Pokud je prázdný vrací False
    a nic neukládá, jinak vrací hodnotu True.

    Arguments:
     - input (String) - input od uživatele (sada příkazů s parametry)
    """
    
    global user_input, command, errors
    if input=="":
        errors.append("no_input")
        return False
    user_input = input.split()
    command = user_input[0]
    return True

def check_to_select() -> bool:
    r"""
    Zkontroluje jesli zadaný sled příkazů od uživatele je validní pro funkci select a uloží si zadání uživatele.
    Pracuje s globálními proměnnými  user_input, to_select, errors a type_select
    Pokud vše projde správně uloží položky k označení do seznamu to_select
    """
    
    global to_select, user_input, errors, type_select
    user_input.pop(0)
    to_select = []
    
    if len(user_input)==0:
        if type_select=="unselect":
            for i in range(len(selected)):
                to_select.append(i+1)
            type_select="unselect"
        else:
            for i in range(len(viewable)):   
                to_select.append(i+1)
            type_select = "all"
        return True
    if len(user_input)==1:
        if is_numeric(user_input[0]):
            to_select.append(int(user_input[0]))
            return True
        else:
            errors.append("select_bad_input")
            return False
    if len(user_input)==2:
        if user_input[1]=="-":
            errors.append("select_bad_input")
            return False
    if len(user_input)>3:
        if user_input[1]=="-":
            errors.append("select_bad_input")
            return False
    if len(user_input)==3:
        if user_input[1]=="-":
            begin = int(user_input[0])
            end = int(user_input[2])
            while (begin<=end):
                to_select.append(begin)
                begin += 1
            return True
    else:
        for i in user_input:
            if is_numeric(i):
                to_select.append(int(i))
        return True

def check_to_open() -> bool:
    r"""
    Zkontroluje jestli zadaný sled příkazů a parametrů
    je správným vstupem pro funkci open a nebo dirsize
    Pokud ne vrací False, jinak True
    """
    
    global user_input, to_open, errors
    vypisy = "open_bad_input"
    if user_input[0]=="dirsize":
        vypisy = "dirsize_bad_input"
    user_input.pop(0)
    if len(user_input)!=1:
        errors.append(vypisy)
        return False
    else:
        if is_numeric(user_input[0]):
            to_open = int(user_input[0])
            return True
        else:
            errors.append(vypisy)
            return False

def is_drive() -> bool:
    r"""
    Zjistí jestli aktuální umístění je kořenem nějakého disku
    Vrací False pokud ne, jinak True
    """
    
    global drives, location
    for i in drives:
        if i==location:
            return True
    return False

def open():
    r"""
    Otevře soubor či složku na zadaném ID ze zobrazených položek
    Pokud se jedná o soubor otevře jej ve výchozí aplikaci win
    jinak se přesune do složky a zobrazí její obsah
    """
     
    global location, info, to_open, errors, drives, page
    new_location = ""
    if to_open>len(visible) or to_open<1:
        errors.append("open_nonexistent")           
    else:
        if is_drive():
            new_location = location + visible[to_open-1]["name"]
        elif location=="root":
            new_location = visible[to_open-1]["name"]
        elif location=="select":
            new_location = visible[to_open-1]["name"]
        elif location=="search":
            new_location = visible[to_open-1]["name"]
        else:
            new_location = location + "\\" + visible[to_open-1]["name"]
        if os.path.isdir(new_location):
            location = new_location
            info.append("open_dir_success")
            page = 1
        elif os.path.isfile(new_location):
            os.startfile(new_location)
            info.append("open_file_success")
        else:
            errors.append("file_does_not_exist")

def get_dirsize():
    r"""
    Zjistí velikost aktuální složky a uloží ji do globální proměnné dirsize
    A ta se potom vypíše při refreshi obrazu
    """
    
    global info, to_open, errors, dirsize
    new_location = ""
    if to_open>len(visible) or to_open<1:
        errors.append("dirsize_nonexistent")
    else:
        if is_drive():
            new_location = location + visible[to_open-1]["name"]
        elif location=="select":
            new_location = selected[to_open-1]
        elif location=="search":
            new_location = selected[to_open-1]
        elif location=="root":
            new_location = visible[to_open-1]["name"]
        else:
            new_location = location + "\\" + visible[to_open-1]["name"]
        if os.path.isdir(new_location):
            dirsize = 0
            for path, dirs, files in os.walk(new_location):
                for f in files:
                    fp = os.path.join(path, f)
                    dirsize += os.path.getsize(fp)
            info.append("dirsize_success")
        else:
            errors.append("file_or_does_not_exist_dir_in_dirsize")

def check_validity_to_select():
    r"""
    Zjistí jestli uživatel nezadal duplicitní položky pro označení
    Nebo jestli nezadal neexistující položky
    Připravuje hotový seznam to_select
    Pro funkci do_select_or_add
    """
    
    global to_select, visible, errors, type_select
    error = False
    if type_select=="unselect":
        for i in range(len(selected)):
            if to_select[i] > len(selected) or to_select[i] < 1:
                to_select.pop(i)
                error = True
        type_select = "" 
    elif not type_select=="all":   
        for i in range(len(to_select)):
            if to_select[i] > len(visible) or to_select[i] < 1:
                to_select.pop(i)
                error = True
    if error:
        errors.append("invalid_index_of_select")

def do_remove(localization : Localization):
    r"""
    Vymaže soubory, složky a vnořené položky ve složkách,
    které jsou poznačené a vymaže aktuální seznam poznačených
    """
    
    global info, errors, selected, successful, failed
    if len(selected)==0:
        errors.append("remove_nothing_to_remove")
        return
    else:
        for i in range(len(selected)):
            rprint(localization.get_text('remove_item_message').format(selected[i]))
        if not confirm.ask(localization.get_text('remove_confirm').format(len(selected))):
            info.append("remove_abort")
            return
        for i in range(len(selected)):
            if os.path.exists(selected[i]):
                if os.path.isfile(selected[i]):
                    if remove_file(selected[i]):
                        successful+=1
                        rprint(localization.get_text('item_removed').format(selected[i]))
                    else:
                        rprint(localization.get_text('unable_to_remove_item').format(selected[i]))
                        failed+=1
                elif os.path.isdir(selected[i]):
                    if len(os.listdir(selected[i]))==0:
                        if remove_directory(selected[i]):
                            successful+=1
                            rprint(localization.get_text('item_removed').format(selected[i]))
                        else:
                            rprint(localization.get_text('unable_to_remove_item').format(selected[i]))
                            failed+=1
                    else:
                        if remove_tree_directory(selected[i]):
                            successful+=1
                            rprint(localization.get_text('item_removed').format(selected[i]))
                        else:
                            rprint(localization.get_text('unable_to_remove_item').format(selected[i]))
                            failed+=1
            else:
                rprint(localization.get_text('nonexistent_path').format(selected[i]))
                failed+=1
    selected = []
    info.append("remove_successful")
    input(localization.get_text('press_enter_to_hide'))

def do_copy(localization : Localization):
    r"""
    Zkopíruje vybrané soubory, složky a vnořené položky v adresářích z
    poznačeného seznamu do aktuálního umístění zobrazeného
    """
    
    global info, errors, successful, failed
    if len(selected)==0:
        errors.append("copy_nothing_to_copy")
        return
    elif location=="select":
        errors.append("copy_no_copy_in_select")
        return
    elif location=="root":
        errors.append("copy_no_copy_in_root")
        return
    elif location=="search":
        errors.append("copy_no_copy_in_search")
    else:
        for i in range(len(selected)):
            if os.path.exists(selected[i]):
                if os.path.isfile(selected[i]):
                    if os.path.exists(location+"\\"+os.path.basename(selected[i])):
                        rprint(localization.get_text('copy_item_already_exists').format(os.path.basename(selected[i]), location))
                        failed+=1
                    elif copy_file(selected[i], location+"\\"+os.path.basename(selected[i])):
                        successful+=1
                        rprint(localization.get_text('item_copied').format(selected[i], location))
                    else:
                        rprint(localization.get_text('unable_to_copy_item').format(selected[i], location))
                        failed+=1
                elif os.path.isdir(selected[i]):
                    if os.path.exists(location+"\\"+os.path.basename(selected[i])):
                        rprint(localization.get_text('copy_folder_already_exists').format(os.path.basename(selected[i]), location))
                        failed+=1
                    elif copy_entire_directory(selected[i], location+"\\"+os.path.basename(selected[i])):
                        successful+=1
                        rprint(localization.get_text('item_copied').format(selected[i], location))
                    else:
                        rprint(localization.get_text('unable_to_copy_item').format(selected[i], location))
                        failed+=1
            else:
                rprint(localization.get_text('nonexistent_path').format(selected[i]))
                failed+=1
    info.append("copy_successful")
    input(localization.get_text('press_enter_to_hide'))

def do_move(localization : Localization):
    r"""
    Přesune soubory, složky a všechny vnořené položky adresářů
    z poznačených do aktuálního zobrazeného umístění
    """
    
    global info, errors, successful, failed
    if len(selected)==0:
        errors.append("move_nothing_to_move")
        return
    elif location=="select":
        errors.append("move_no_move_in_select")
        return
    elif location=="root":
        errors.append("move_no_move_in_root")
    elif location=="search":
        errors.append("move_no_move_in_search")
    else:
        for i in range(len(selected)):
            if os.path.exists(selected[i]):
                if move_file_or_directory(selected[i], location):
                    successful+=1
                    rprint(localization.get_text('item_moved').format(selected[i], location))
                else:
                    rprint(localization.get_text('unable_to_move').format(selected[i], location))
                    failed+=1
            else:
                rprint(localization.get_text('nonexistent_path').format(selected[i]))
                failed+=1
    info.append("move_successful")
    selected = []
    input(localization.get_text('press_enter_to_hide'))

def check_to_up() -> bool:
    r"""
    Zkontroluje jestli uživatel zadal správný sled příkazů a parametrů
    pro funkci up, pokud ne tak vrací False, jinak vrací True
    """
    
    global user_input, up, errors
    user_input.pop(0)
    if len(user_input)==0:
        up = 1
        return True
    elif len(user_input)!=1:
        errors.append("up_bad_input")
        return False
    else:
        if is_numeric(user_input[0]):
            up = int(user_input[0])
            return True
        else:
            errors.append("up_bad_input")
            return False

def make_dir():
    r"""
    V aktuálním adresáři umístění vytvoří složku
    Jméno složky si uživatel zadá parametrem
    při volání příkazu makedir
    """
    
    global new_dir, errors, info
    if location=="root":
        errors.append("make_dir_no_root")
    elif location=="select":
        errors.append("make_dir_no_select")
    elif location=="search":
        errors.append("make_dir_no_search")
    else:    
        if create_directory(location, new_dir):
            info.append("make_dir_successful")
        else:
            errors.append("make_dir_failed")
    new_dir = ""

def go_up():
    r"""
    Přesune aktuální umístění zobrazení nahoru nebo dolů
    Podle čísla v globální proměnné up
    """
    
    global location, info, errors, drives, up, page
    page = 1
    if location=="root":
        errors.append("no_up_in_root")
        up = 0
        return
    if up<1:
        errors.append("up_bad_input")
        return
    if location=="select":
        location = pre_select
        return
    if location=="search":
        location = pre_search
        return
    while up>0:
        for i in drives:
            if i==location:
                location = "root"
                up = 0
                info.append("up_success")
                return
        location = location.rsplit("\\", 1)[0]
        location = location + "\\"
        if not is_drive():
            location = location[:-1]
        up = up - 1
    info.append("up_success")

def print_app_info(localization : Localization):
    r"""
    Vypíše základní informace programu
    """
    
    clear()
    text = localization.get_text('app_info').format(CFG.VERSION, CFG.AUTHOR, CFG.DATE, CFG.WEBPAGE, CFG.GITHUB, CFG.PYTHON_VERSION, CFG.RICH_VERSION, CFG.PYINSTALLER_VERSION, CFG.UPX_VERSION, CFG.ZIP7_VERSION)
    rprint(Panel.fit(text, title=localization.get_text('app_info_leek_title'), style='bold magenta'))
    input(localization.get_text('press_enter_to_hide'))

def print_help(localization : Localization):
    r"""
    Vypíše pomoc programu uživateli
    """
    clear()
    rprint(Panel(Text(localization.get_text('app_help_leek_title'), style="bold white", justify="center")))
    text = Text(localization.get_text('app_help_part_one'), style="bold yellow", justify='full')
    rprint(Panel(text, title=localization.get_text('app_help_basic_title'),style="bold blue"))
    rprint(Panel(localization.get_text('app_help_part_two'), title=localization.get_text('app_help_command_list_leek_title'), style="bold green"))
    input(localization.get_text('press_enter_to_hide'))

def print_page(localization : Localization):
    r"""
    Vypíše informační text zobrazující informace
    o počtu stran, a na které stránce teď jsme
    Zároveň informuje o množství zobrazených
    a zobrazitelných položek
    """
    
    rprint(localization.get_text('list_info').format(page, max_page, len(viewable), len(visible)))

def print_sortinfo(cfg : Configuration, localization : Localization):
    r"""
    Vypíše informace o aktuálním nastavení řazení
    položek v aktuálním zobrazení
    """
    
    match cfg.get_cfg('sort_key'):
        case "none":
            if cfg.get_cfg('sort_direction')=="up":
                rprint(localization.get_text('none_up'))
            if cfg.get_cfg('sort_direction')=="down":
                rprint(localization.get_text('none_down'))
        case "name":
            if cfg.get_cfg('sort_direction')=="up":
                rprint(localization.get_text('name_up'))
            if cfg.get_cfg('sort_direction')=="down":
                rprint(localization.get_text('name_down'))
        case "created":
            if cfg.get_cfg('sort_direction')=="up":
                rprint(localization.get_text('created_up'))
            if cfg.get_cfg('sort_direction')=="down":
                rprint(localization.get_text('created_down'))
        case "size":
            if cfg.get_cfg('sort_direction')=="up":
                rprint(localization.get_text('size_up'))
            if cfg.get_cfg('sort_direction')=="down":
                rprint(localization.get_text('size_down'))
        case "changed":
            if cfg.get_cfg('sort_direction')=="up":
                rprint(localization.get_text('changed_up'))
            if cfg.get_cfg('sort_direction')=="down":
                rprint(localization.get_text('changed_down'))

def create_table(cfg : Configuration, localization : Localization):
    r"""
    Vytvoří tabulkový list pro zobrazení z funkce main
    """
    
    global table
    table = Table(title=location)
    table.add_column(localization.get_text('id'), justify="center", style="blue", no_wrap=True, min_width=4)
    table.add_column(localization.get_text('file_or_folder_name'), justify="left", style="green")
    table.add_column(localization.get_text('size').format(cfg.get_cfg('size_unit')), justify="center", style="yellow", no_wrap=True)
    table.add_column(localization.get_text('created'), justify="center", style="white", no_wrap=True)
    table.add_column(localization.get_text('modified'), justify="center", style="cyan", no_wrap=True)
    table.add_column(localization.get_text('rights'), justify="center", style="red", no_wrap=True)
    
    if location=="root":
        for i in range(len(visible)):
            table.add_row(str(visible[i]["id"]), visible[i]["name"], "", "", "", "")
    else:
        for i in range(len(visible)):
            if os.path.isdir(location + "\\" + visible[i]["name"]):
                table.add_row(str(visible[i]["id"]), visible[i]["name"], "-", timedate(visible[i]["created"]), timedate(visible[i]["changed"]), str(visible[i]["rights"]))
            else:
                table.add_row(str(visible[i]["id"]), visible[i]["name"], str(visible[i]["size"]/size_divider(cfg)), timedate(visible[i]["created"]), timedate(visible[i]["changed"]), str(visible[i]["rights"]))

def get_file_record_as_dictionary(files, i):
    r"""
    Vrátí záznam o položce (soubor nebo i složka)
    jako dictionary se všemi informacemi typu
    časy založení a úpravy, práva, velikost
    pro využití v tabulce
    
    Arguments:
     - files (list) - posílá seznam položek ke zpracování funkcí
     - i (int)      - index seznamu, ze kterého se požaduje získání informací
    """
    
    global location
    if location=="search":
        file_location = files[i]
    elif location=="select":
        file_location = files[i]
        file_info = get_info_about_file(file_location)
        if not file_info:
            return {"id" : i+1, "name" : "noneexistent", "size" : 0, "created" : 0, "changed" : 0, "rights" : 0}
        if os.path.isdir(file_location):
            return {"id" : i+1, "name" : files[i], "size" : 0, "created" : file_info[9], "changed" : file_info[8], "rights" : file_info[0]}
        if os.path.isfile(file_location):
            return {"id" : i+1, "name" : files[i], "size" : int(float(file_info[6])/1024), "created" : file_info[9], "changed" : file_info[8], "rights" : file_info[0]}
    elif is_drive():
        file_location = location + files[i]
    else:
        file_location = location + "\\" + files[i]
    file_info = get_info_about_file(file_location)
    if not file_info:
        return {"id" : i+1, "name" : "noneexistent", "size" : 0, "created" : 0, "changed" : 0, "rights" : 0}
    if os.path.isdir(file_location):
        return {"id" : i+1, "name" : files[i], "size" : 0, "created" : file_info[9], "changed" : file_info[8], "rights" : file_info[0]}
    if os.path.isfile(file_location):
        return {"id" : i+1, "name" : files[i], "size" : int(float(file_info[6])/1024), "created" : file_info[9], "changed" : file_info[8], "rights" : file_info[0]}

def timedate(seconds) -> str:
    r"""
    Ze sekund na vstupu vytvoří string času ve formátu DD/MM/YY-HH/MM/SS

    Arguments:
     - seconds (int) - čas pro zpracování zadaný v sekundách
    """
    
    return datetime.fromtimestamp(seconds).strftime("%d/%m/%Y-%H:%M:%S")

def create_viewable(cfg : Configuration):
    r"""
    Vytvoří dictionary zobrazitelných položek v aktuálním
    zvoleném adresáři, volá funkci get_file_as_dictionary(), která
    vrací jednotlivé informace o položkách, které se ukládají
    """
    
    global viewable, drives, errors, selected
    viewable = []
    if location=="root":
        for i in range(len(drives)):
            viewable.append({"id" : i+1, "name" : drives[i], "size" : 0, "created" : 0, "changed" : 0, "rights" : 0})
    elif location=="select":
        for i in range(len(selected)):
            viewable.append(get_file_record_as_dictionary(selected, i))
    elif location=="search":
        for i in range(len(search_result)):
            viewable.append(get_file_record_as_dictionary(search_result, i))
    else:
        files = get_list_of_files(location)
        if not files:
            if "open_dir_success" in errors:
                errors.remove("open_dir_success")
            return
        for i in range(len(files)):
            viewable.append(get_file_record_as_dictionary(files, i))
    do_sort(cfg)

def do_sort(cfg : Configuration):
    r"""
    Zajistí seřazení zobrazitelných položek dle vstupu uživatele pro
    Funkci sort pro zobrazení položek umístění 
    """
    
    global viewable
    
    match cfg.get_cfg('sort_key'):
        case "none":
            return
        case "name":
            viewable.sort(key=operator.itemgetter("name"))
        case "created":
            viewable.sort(key=operator.itemgetter("created"))
        case "size":
            viewable.sort(key=operator.itemgetter("size"))
        case "changed":
            viewable.sort(key=operator.itemgetter("changed"))
    
    match cfg.get_cfg('sort_direction'):
        case "down":
            viewable.reverse()
            


def go_root():
    r"""
    Přesuneme aktuální zobrazení adresáře do rootu
    aktuálního disku
    """
    
    global location, info, errors, page
    if location=="root":
        errors.append("no_drive_no_root")        
    else:
        location = location[:4]
        info.append("root_success")
        page = 1        

def check_new_dir_name() -> bool:
    r"""
    Zkontroluje jestli uživatel zadal správný sled příkazů a parametrů
    Pro volání funkce makedir, pokud ne vrací False, jinak True
    """
    
    global new_dir, user_input, errors
    user_input.pop(0)
    if len(user_input)!=1:
        errors.append("make_dir_bad_input")
        return False
    else:
        new_dir = str(user_input[0])
        return True

def check_drive() -> bool:
    r"""
    Zkontroluje jestli uživatel zadal správný sled příkazů a parametrů
    Pro volání funkce drive, pokud ne vrací False, jiank True
    """
    
    global user_input, drive, errors
    user_input.pop(0)
    if len(user_input)!=1:
        errors.append("drive_bad_input")
        return False
    else:
        if user_input[0].isalpha() and len(user_input[0])==1:
            drive = str(user_input[0])
            return True
        else:
            errors.append("drive_bad_input")
            return False

def go_drive():
    r"""
    Přesune aktuální zobrazení umístění
    na disk v globální proměnné drive
    """
    
    global info, errors, drive, location, page
    if drive.islower():
        drive = drive.upper()
    drive = drive + ":\\\\"
    for i in drives:
        if i==drive:
            location = drive
            info.append("drive_success")
            page = 1
            return
    errors.append("drive_does_not_exist")            

def calculate_pages(cfg : Configuration):
    r"""
    Zjistí úplný počet stránek listů zobrazení
    Uloží jej do proměnné názvu max_page
    """
    
    global rows, viewable, visible, page, max_page
    max_page = 1
    while len(viewable)>(max_page*cfg.get_cfg('rows')):
        max_page = max_page + 1

def create_visible(cfg : Configuration):
    r"""
    Vytvoří dictionary viditelných položek pro zobrazení
    na aktuální zvolené stránce pomocí listů
    """
    
    global viewable, visible
    j = 0
    calculate_pages(cfg)
    visible = []
    for i in range(len(viewable)):
        if not i<((cfg.get_cfg('rows')*page)-cfg.get_cfg('rows')):
            if i<cfg.get_cfg('rows')*page:
                visible.append(viewable[i].copy())
                visible[j]["id"] = j+1
                j+=1
    
def go_unselect():
    r"""
    Zruší označení vybraných položek podle listu to_select a vyčistí jej
    Odoznačování se děje dle id v seznamu označených
    """
    
    global selected, info, to_select, errors
    to_select = list(set(to_select))
    to_select.sort(reverse=True)
    if len(selected)>0:
        for i in range(len(to_select)):
            selected.pop(to_select[i]-1)
    to_select = []
    info.append("unselect_success")

def check_next_previous() -> bool:
    r"""
    Zkontroluje správný vstup funkce next a previous,
    pokud není správný tak vrátí False, jinak True
    """
    
    global user_input, errors, distance
    user_input.pop(0)
    if len(user_input)==0:
        distance = 1
        return True
    elif len(user_input)!=1:
        if direction=="next":
            errors.append("next_bad_input")
        else:
            errors.append("previous_bad_input")
        return False
    else:
        if is_numeric(user_input[0]):
            distance = int(user_input[0])
        else:
            if direction=="next":
                errors.append("next_bad_input")
            else:
                errors.append("previous_bad_input")
            return False
        if distance<1:
            if direction=="next":
                errors.append("next_bad_input")
            else:
                errors.append("previous_bad_input")
            return False
    return True

def check_to_rename(how) -> bool:
    r"""
    Zkontroluje správnost vstupu pro funkci rename a copyrename
    Pokud není v pořádku, tak vrátí hodnotu False, jinak True
    Funkce kontroluje jak vstup pro rename tak pro copyrename
    Který vstup má kontrolovat definuje parametr how
    
    Arguments:
     - how (String) - určuje jestli se má kontrolovat
                    - funkce copyrename nebo rename
    """
    
    global user_input, r_new_name, errors, r_place, r_counter_begin, r_increment, r_n_digit, r_advanced, r_file_type
    r_advanced = False
    r_place = r_new_name = r_file_type = error = ""
    r_counter_begin = r_n_digit = r_increment = 0
    match how:
        case "rename": error = "rename_bad_input"
        case "copyrename": error = "copyrename_bad_input"
    user_input.pop(0)
    if len(user_input)==1:
        r_advanced = False
        r_new_name = str(user_input[0])
        return True
    elif len(user_input)==6:
        r_advanced = True
        r_new_name = str(user_input[0])
        r_place = str(user_input[1])
        if r_place != "after" and r_place != "before":
            errors.append(error)
            return False
        r_counter_begin = int(user_input[2])
        r_increment = int(user_input[3])
        r_n_digit = int(user_input[4])
        r_file_type = str(user_input[5])
        return True
    else:
        errors.append(error)
        return False

def do_rename(localization : Localization):
    r"""
    Provede přejmenování vyznačených souborů či složek, nebo souboru či složky
    Přejmenování je buďto jednoduché (pouze pro jednu položku)
    Nebo složité (je pro více položek), v tomto případě funguje
    I funkce počítadla, která do názvu přidává čísla
    """
    
    global info, r_new_name, errors, r_place, r_counter_begin, r_increment, r_n_digit, r_advanced, failed, successful, selected, r_file_type
    if len(selected)==0:
        errors.append("rename_nothing_to_rename")
    elif not r_advanced:
        if len(selected)==1:
            if rename_file_or_directory(selected[0], r_new_name):
                rprint(localization.get_text('item_renamed').format(selected[0], r_new_name))
                successful+=1
                info.append("rename_successful")
            else:
                rprint(localization.get_text('unable_to_rename').format(selected[0], r_new_name))
                failed+=1
        else:
            errors.append("rename_more_select_no_advanced")
            return      
    else:
        if len(selected)!=1:
            counter = r_counter_begin
            for i in range(len(selected)):
                new_name = ""
                match r_place:
                    case "before":
                                    if r_n_digit == 0:
                                        digits_to_append = 0
                                    else:
                                        digits_to_append = r_n_digit - len(str(counter))
                                    if digits_to_append<0: digits_to_append = 0
                                    new_name = str(counter)
                                    while digits_to_append>0:
                                        new_name = "0" + new_name
                                        digits_to_append-=1
                                    counter+=r_increment
                                    if r_new_name!="|none|":
                                        new_name+=r_new_name
                                    if r_file_type!="|none|":
                                        if r_file_type == "|base|":
                                            new_name+=pathlib.Path(selected[i]).suffix
                                        else: 
                                            new_name+=r_file_type
                    case "after":
                                    if r_n_digit == 0:
                                        digits_to_append = 0
                                    else:
                                        digits_to_append = r_n_digit - len(str(counter))
                                    if digits_to_append<0: digits_to_append = 0
                                    new_name = str(counter)
                                    while digits_to_append>0:
                                        new_name = "0" + new_name
                                        digits_to_append-=1
                                    if r_new_name!="|none|":
                                        new_name = r_new_name + new_name
                                    counter+=r_increment
                                    if r_file_type!="|none|":
                                        if r_file_type == "|base|":
                                            new_name+=pathlib.Path(selected[i]).suffix
                                        else: 
                                            new_name+=r_file_type
                if rename_file_or_directory(selected[i], new_name):
                    successful+=1
                    rprint(localization.get_text('item_renamed').format(selected[i], new_name))
                else:
                    rprint(localization.get_text('unable_to_rename').format(selected[i], new_name))
                    failed+=1
            info.append("rename_successful")
        else:
            errors.append("rename_advanced_but_one")
    selected = []
    input(localization.get_text('press_enter_to_hide'))

def do_copyrename(localization : Localization):
    r"""
    Umožňuje funcionalitu zkopírování a přejmenování zaráz,
    Funguje jako kombinace copy a rename,
    Kopíruje ze seznamu označených do aktuálního adresáře,
    Umožňuje jak pojmenování jednoduché tak složité
    """
    
    global info, r_new_name, errors, r_place, r_counter_begin, r_increment, r_n_digit, r_advanced, failed, successful, selected, r_file_type
    if len(selected)==0:
        errors.append("copyrename_nothing_to_copyrename")
        return
    elif location=="select":
        errors.append("copyrename_no_copy_in_select")
        return
    elif location=="root":
        errors.append("copyrename_no_copy_in_root")
        return
    elif location=="search":
        errors.append("copyrename_no_copy_in_search")
        return
    elif not r_advanced:
        if len(selected)==1:
            if os.path.exists(selected[0]):
                if os.path.isfile(selected[0]):
                    if os.path.exists(location+"\\"+r_new_name):
                        rprint(localization.get_text('copy_item_already_exists').format(r_new_name, location))
                        failed+=1
                    elif copy_file(selected[0], location+"\\"+r_new_name):
                        successful+=1
                        rprint(localization.get_text('item_copyrenamed').format(selected[0], location+"\\"+r_new_name))
                    else:
                        rprint(localization.get_text('unable_to_copyrename_item').format(selected[0], location, r_new_name))
                        failed+=1
                if os.path.isdir(selected[0]):
                    if os.path.exists(location+"\\"+r_new_name):
                        rprint(localization.get_text('copy_folder_already_exists').format(r_new_name, location))
                        failed+=1
                    elif copy_entire_directory(selected[0], location+"\\"+r_new_name):
                        successful+=1
                        rprint(localization.get_text('item_copyrenamed').format(selected[0], location+"\\"+r_new_name))
                    else:
                        rprint(localization.get_text('unable_to_copyrename_item').format(selected[0], location, r_new_name))
                        failed+=1
            else:
                rprint(localization.get_text('nonexistent_path').format(selected[i]))
                failed+=1
        else:
            errors.append("coopyrename_more_select_no_advanced")
            return
    else:
        if len(selected)!=0:
            counter = r_counter_begin
            for i in range(len(selected)):
                new_name = ""
                match r_place:
                    case "before":
                                    if r_n_digit == 0:
                                        digits_to_append = 0
                                    else:
                                        digits_to_append = r_n_digit - len(str(counter))
                                    if digits_to_append<0: digits_to_append = 0
                                    new_name = str(counter)
                                    while digits_to_append>0:
                                        new_name = "0" + new_name
                                        digits_to_append-=1
                                    counter+=r_increment
                                    if r_new_name!="|none|":
                                        new_name+=r_new_name
                                    if r_file_type!="|none|":
                                        if r_file_type == "|base|":
                                            new_name+=pathlib.Path(selected[i]).suffix
                                        else: 
                                            new_name+=r_file_type
                    case "after":
                                    if r_n_digit == 0:
                                        digits_to_append = 0
                                    else:
                                        digits_to_append = r_n_digit - len(str(counter))
                                    if digits_to_append<0: digits_to_append = 0
                                    new_name = str(counter)
                                    while digits_to_append>0:
                                        new_name = "0" + new_name
                                        digits_to_append-=1
                                    if r_new_name!="|none|":
                                        new_name = r_new_name + new_name
                                    counter+=r_increment
                                    if r_file_type!="|none|":
                                        if r_file_type == "|base|":
                                            new_name+=pathlib.Path(selected[i]).suffix
                                        else: 
                                            new_name+=r_file_type
                if os.path.exists(selected[i]):
                    if os.path.isfile(selected[i]):
                        if os.path.exists(location+"\\"+new_name):
                            rprint(localization.get_text('copy_item_already_exists').format(new_name, location))
                            failed+=1
                        elif copy_file(selected[i], location+"\\"+new_name):
                            rprint(localization.get_text('item_copyrenamed').format(selected[i], location+"\\"+new_name))
                            successful+=1
                        else:
                            rprint(localization.get_text('unable_to_copyrename_item').format(selected[i], location, new_name))
                            failed+=1
                    if os.path.isdir(selected[i]):
                        if os.path.exists(location+"\\"+new_name):
                            rprint(localization.get_text('copy_folder_already_exists').format(new_name, location))
                            failed+=1
                        elif copy_entire_directory(selected[i], location+"\\"+new_name):
                            rprint(localization.get_text('item_copyrenamed').format(selected[i], location+"\\"+new_name))
                            successful+=1
                        else:
                            rprint(localization.get_text('unable_to_copyrename_item').format(selected[i], location, new_name))
                            failed+=1
                else:
                    rprint(localization.get_text('nonexistent_path').format(selected[i]))
                    failed+=1
        else:
            errors.append("coopyrename_advanced_but_one")
            return
    info.append("copyrename_successful")
    input(localization.get_text('press_enter_to_hide'))

def check_get_rows(cfg : Configuration):
    r"""
    Funkce, která zkontrojue správnost vstupu pro funkci rows
    a zároveň i nové rows nastaví
    """
    
    global user_input, info, errors, page
    user_input.pop(0)
    new_rows = 0
    if len(user_input)!=1:
        errors.append("rows_bad_input")
    else:
        if is_numeric(user_input[0]):
            new_rows = int(user_input[0])
        else:
            errors.append("rows_bad_input")
        if new_rows<10:
            errors.append("rows_bad_input")
        else:
            cfg.set_cfg('rows', new_rows)
            info.append("rows_success")
            page = 1
            
def check_get_locale(cfg : Configuration, localization : Localization) -> None:
    r"""
    Funkce, která zkontroluje vstup pro funkci locale a nastaví novou hodnotu pokud je vstup správný
    """
    
    global user_input, info, errors
    user_input.pop(0)
    if len(user_input)!=1:
        errors.append("locale_bad_input")
    else:
        locale_exists = False
        new_locale = str(user_input[0])
        for existing_locale in localization.locales:
            if new_locale == existing_locale:
                locale_exists = True
                break
        if locale_exists:
            cfg.set_cfg('locale', new_locale)
            info.append("locale_successful")
        else:
            errors.append("locale_bad_input")

def check_get_saveconfig(cfg : Configuration) -> None:
    r"""
    Funkce, která zkontroluje vstup pro funkci saveconfig a nastaví novou hodnotu pokud je vstup správný
    """
    
    global user_input, info, errors
    user_input.pop(0)
    if len(user_input)!=1:
        errors.append("saveconfig_bad_input")
    else:
        if user_input[0] == "true":
            cfg.set_cfg('save_cfg', True)
            info.append("saveconfig_successful")
        elif user_input[0]  == "false":
            cfg.set_cfg('save_cfg', False)
            info.append("saveconfig_successful")
        else:
            errors.append("saveconfig_bad_input")
            
def check_get_sizeunit(cfg : Configuration) -> None:
    r"""
    Funkce, která zkontroluje vstup pro funkci sizeunit a nastaví novou hodnotu pokud je vstup správný
    """
    
    global user_input, info, errors
    user_input.pop(0)
    if len(user_input)!=1:
        errors.append("sizeunit_bad_input")
    else:
        if user_input[0] == "B" or user_input[0] == "KB" or user_input[0] == "MB" or user_input[0] == "GB" or user_input[0] == "TB":
            cfg.set_cfg('size_unit', user_input[0])
            info.append("sizeunit_successful")
        else:
            errors.append("sizeunit_bad_input")

def check_to_search() -> bool:
    r"""
    Zkontroluje jestli uživatel zadal správný sled příkazů a parametrů pro funkci search
    Pokud tomu tak není vrací False, jinak vrací zpět True 
    """
    
    global user_input, info, errors, find
    user_input.pop(0)
    if len(user_input)==1:
        find = str(user_input[0])
        return True
    else:
        errors.append("search_bad_input")
        return False

def do_search(localization : Localization):
    r"""
    Vyhledává výraz zadaný od uživatele v aktuálním umístění zobrazení
    Výsledky vyhledávání zobrazí na vlastním listu
    """
    
    global info, errors, find, search_result, location, pre_select, pre_search
    
    if location=="root":
        search_result = []
        for i in drives:
            for root, dirs, files in os.walk(i):
                rprint(localization.get_text('searching_in').format(root))
                for dir in dirs:
                    if find in os.path.basename(dir):
                        search_result.append(root+"\\"+dir)
                for file in files:
                    if find in os.path.basename(file):
                        search_result.append(root+"\\"+file)
    elif location=="select":
        search_result = []
        for i in selected:
            for root, dirs, files in os.walk(i):
                rprint(localization.get_text('searching_in').format(root))
                for dir in dirs:
                    if find in os.path.basename(dir):
                        search_result.append(root+"\\"+dir)
                for file in files:
                    if find in os.path.basename(file):
                        search_result.append(root+"\\"+file)
            if find in os.path.basename(i):
                search_result.append(i)
    elif location=="search":
        search_backup = search_result.copy()
        search_result = []
        for i in search_backup:
            for root, dirs, files in os.walk(i):
                rprint(localization.get_text('searching_in').format(root))
                for dir in dirs:
                    if find in os.path.basename(dir):
                        search_result.append(root+"\\"+dir)
                for file in files:
                    if find in os.path.basename(file):
                        search_result.append(root+"\\"+file)
            if find in os.path.basename(i):
                search_result.append(i)
    else:
        search_result = []
        for root, dirs, files in os.walk(location):
            rprint(localization.get_text('searching_in').format(root))
            for dir in dirs:
                if find in os.path.basename(dir):
                    search_result.append(root+"\\"+dir)
            for file in files:
                if find in os.path.basename(file):
                    search_result.append(root+"\\"+file)
    if location!="search":
        pre_search = location
        location = "search"
    info.append("search_successful")
    
def check_and_set_sort(cfg : Configuration):
    r"""
    Zkontroluje jestli uživatel zadal správný vstup pro funkci sort,
    Pokud ne nastaví původní hodnoty sortu
    """
    
    global errors, user_input
    user_input.pop(0)
    sort_key_backup = cfg.get_cfg('sort_key')
    sort_direction_backup = cfg.get_cfg('sort_direction')
    if len(user_input)==2:
        cfg.set_cfg('sort_key', str(user_input[0]))
        if cfg.get_cfg('sort_key')!="none" and cfg.get_cfg('sort_key')!="name" and cfg.get_cfg('sort_key')!="size" and cfg.get_cfg('sort_key')!="created" and cfg.get_cfg('sort_key')!="changed":
            cfg.set_cfg('sort_key', sort_key_backup)
            errors.append("sort_bad_input")
            return
        cfg.set_cfg('sort_direction', str(user_input[1]))
        if cfg.get_cfg('sort_direction')!="up" and cfg.get_cfg('sort_direction')!="down":
            cfg.set_cfg('sort_direction', sort_direction_backup)
            errors.append("sort_bad_input")
            return
    else:
        errors.append("sort_bad_input")
        return
    return

def do_next_previous():
    r"""
    Přepíná mezi zobrazenými stránkami o daný počet
    Funkce pro příkazy next a previous
    """
    global info, errors, drives, distance, direction, page
    while distance>0:
        if page==max_page and direction=="previous":
            if not page==1:
                page = page - 1
                distance = distance - 1
            else:
                distance = 0
                direction = ""
                errors.append("nowhere_to_go_previous")
                return
        elif page==max_page and direction=="next":
            distance = 0
            direction = ""
            errors.append("nowhere_to_go_next")
            return
        elif page==1 and direction=="previous":
            distance = 0
            direction = ""
            errors.append("nowhere_to_go_previous")
            return
        else:
            match direction:
                case "next":
                    page = page + 1
                    distance = distance - 1
                case "previous":
                    page = page - 1
                    distance = distance - 1
    match direction:
                case "next":
                    info.append("next_success")
                case "previous":
                    info.append("previous_success")

def do_select_or_add(what) -> bool:
    r"""
    Podle již zpracovaného vstupu od uživatele pro funkci select nebo add
    poznačí nebo přidá k poznačeným zvolené položky

    Arguments:
     - what (String) - zda jde o funkci select nebo add
    """
    global selected, info, location, to_select, errors, type_select
    error = ""
    information = ""
    if location=="select":
        errors.append("no_select_in_select")
        return False
    match what:
        case "add":
            error = "no_add_in_roots"
            information = "add_success"
        case "select":
            selected = []
            error = "no_select_in_roots"
            information = "select_success"
    if location=="root":
        errors.append(error)
        return False
    elif is_drive():
        if type_select=="all":
            type_select = ""
            for i in range(len(to_select)):
                new_location = location + viewable[to_select[i]-1]["name"]
                if selected.count(new_location)==0:
                    selected.append(new_location)
            if errors.count("invalid_index_of_select")==0:
                info.append(information)
            to_select = []
            return True
        else:
            for i in range(len(to_select)):
                new_location = location + visible[to_select[i]-1]["name"]
                if selected.count(new_location)==0:
                    selected.append(new_location)
            if errors.count("invalid_index_of_select")==0:
                info.append(information)
            to_select = []
            return True
    elif location=="search":
        if type_select=="all":
            type_select = ""
            for i in range(len(to_select)):
                new_location = viewable[to_select[i]-1]["name"]
                if selected.count(new_location)==0:
                    selected.append(new_location)
            if errors.count("invalid_index_of_select")==0:
                info.append(information)
            to_select = []
            return True
        else:
            for i in range(len(to_select)):
                new_location = visible[to_select[i]-1]["name"]
                if selected.count(new_location)==0:
                    selected.append(new_location)
            if errors.count("invalid_index_of_select")==0:
                info.append(information)
            to_select = []
            return True
    else:
        if type_select=="all":
            type_select = ""
            for i in range(len(to_select)):
                new_location = location + "\\" + viewable[to_select[i]-1]["name"]
                if selected.count(new_location)==0:
                    selected.append(new_location)
            if errors.count("invalid_index_of_select")==0:
                info.append(information)
            to_select = []
            return True
        else:
            for i in range(len(to_select)):
                new_location = location + "\\" + visible[to_select[i]-1]["name"]
                if selected.count(new_location)==0:
                    selected.append(new_location)
            if errors.count("invalid_index_of_select")==0:
                info.append(information)
            to_select = []
            return True

def clear():
    r"""
    V konzoli zavolá cls příkaz pro vyčištění zobrazení
    """

    os.system('cls')

def refresh_all(cfg : Configuration):
    r"""
    Zaktualizuje seznam disků, vytvoří seznam zobrazitelných položek a položek zobrazených, zobrazení aktualizuje
    """

    global drives
    drives = get_list_of_drives()
    create_viewable(cfg)
    create_visible(cfg)

def size_divider(cfg : Configuration) -> int:
    match cfg.get_cfg('size_unit'):
        case 'B' : return 1
        case 'KB': return 1000
        case "MB": return 1000000
        case "GB": return 1000000000
        case "TB": return 1000000000000

def print_info_error_message(cfg : Configuration, localization : Localization, error_keys : list, info_keys : list):
    for error_key in error_keys:
        localized_message = localization.get_text(error_key)
        if localized_message=='none':
            rprint(f"[bold red] {error_key} [/bold red]")
        else:
            rprint(localized_message)
    for info_key in info_keys:
        match info_key:
            case 'dirsize_success':
                rprint(localization.get_text(info_key).format(to_open, int(dirsize/size_divider(cfg)), cfg.get_cfg('size_unit')))
            case 'remove_successful':
                rprint(localization.get_text(info_key).format(successful, failed))
            case 'copy_successful':
                rprint(localization.get_text(info_key).format(successful, failed))
            case 'rename_successful':
                rprint(localization.get_text(info_key).format(successful, failed))
            case 'copyrename_successful':
                rprint(localization.get_text(info_key).format(successful, failed))
            case 'print_locales':
                rprint(localization.get_text(info_key).format(localization.get_locales()))
            case _:   
                localized_message = localization.get_text(info_key)
                if localized_message=='none':
                    rprint(f"[bold red] {info_key} [/bold red]")
                else:
                    rprint(localized_message)    

if __name__ == "__main__":
    r"""
    Hlavní tělo aplikace, nechává zobrazit většinu informací,
    přijímá od uživatele příkay s parametry a podle nich volá v matchi zadané funkce
    je držen proměnnou work
    Zpracovává vstup od uživatele
    """
    config = Configuration()
    localization = Localization(config)
    info.append(config.load_cfg())
    info.append(localization.load_localization())
    
    while True:
        refresh_all(config)
        clear()
        create_table(config, localization)

        rprint(table)
        print_page(localization)
        print_sortinfo(config, localization)
        print_info_error_message(config, localization, errors, info)
        errors = []
        info = []
        successful = failed = 0
        if check_input(prompt.ask(localization.get_text('insert_cmd'))):
            match user_input[0]:
                case "select": 
                    if check_to_select():
                        check_validity_to_select()
                        do_select_or_add("select")
                case "rename":
                    if check_to_rename("rename"):
                        do_rename(localization)
                case "remove":
                    do_remove(localization)
                case "copy": 
                    do_copy(localization)
                case "move":
                    do_move(localization)
                case "up":
                    if check_to_up():
                        go_up()
                case "search":
                    if check_to_search():
                        do_search()
                case "sort": 
                    check_and_set_sort(config)
                case "showselect": 
                    pre_select = location
                    location = "select"
                    info.append("showselect_success")
                    page = 1
                case "copyrename":
                    if check_to_rename("copyrename"):
                        do_copyrename(localization)
                case "unselect":
                    type_select = "unselect"
                    if check_to_select():
                        check_validity_to_select()
                        go_unselect()
                case "root":
                    go_root()
                case "drive": 
                    if check_drive():
                        go_drive()
                case "roots":
                    location = "root"
                    info.append("roots_success")
                case "next":
                    if check_next_previous():
                        direction="next"
                        do_next_previous()
                case "previous":
                    if check_next_previous():
                        direction="previous"
                        do_next_previous()
                case "help": 
                    print_help(localization)
                case "refresh":
                    info.append("refreshed")
                case "add":
                    if check_to_select():
                        check_validity_to_select()
                        do_select_or_add("add")
                case "exit":
                    break
                case "open":
                    if check_to_open():
                        open()
                case "rows":
                    check_get_rows(config)
                case "info":
                    print_app_info(localization)
                case "dirsize":
                    if check_to_open():
                        get_dirsize()
                case "makedir":
                    if check_new_dir_name():
                        make_dir()
                case "locales":
                    info.append('print_locales')
                case "locale":
                    check_get_locale(config, localization)
                case "saveconfig":
                    check_get_saveconfig(config)
                case "sizeunit":
                    check_get_sizeunit(config)
                case _:
                    errors.append("unknown_command")
    rprint(localization.get_text(config.save_cfg()))
    rprint(localization.get_text('bye_message'))
