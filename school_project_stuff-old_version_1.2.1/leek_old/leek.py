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
import shutil
from xmlrpc.client import Boolean, boolean
from rich import print as rprint
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.prompt import Prompt as prompt
from rich.prompt import Confirm as confirm
from rich.table import Table
from rich.text import Text
from datetime import datetime
####################################################

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
viewable = {}                               # dictionary zobrazitelnych polozek v aktualnim umisteni
visible = {}                                # dictionary prave zobrazenych polozek v aktualnim umisteni podle promenne page
errors = []                                 # promenna seznamu erroru a take vsech chybovych hlaseni
info = []                                   # promenna seznamu informacnich a pozitivnich zprav od programu
work = True                                 # promenna udrzujici cyklus main v chodu, pokud False tak se program vypne
rows = 46                                   # max pocet radku k zobrazeni na jednu stranu
page = 1                                    # aktualni strana
max_page = 1                                # celkovy pocet vsech stran
to_open = 0                                 # index polozky na strance aktualni zobrazene k otevreni
table = Table()                             # objekt tabulky pro vyuziti nekterych funkci knihovny rich
up = 0                                      # o kolik se posunouti
drive = ""                                  # aktualni disk
direction = ""                              # kterym smerem se posunout mezi stranami
distance = 0                                # o kolik se posunouti mezi stranami
version = "0.1"                             # verze programu
author = "Otakar Kočí"                      # autor programu
year = "2022"                               # rok verze
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
    return os.stat(location)

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
    
def search_file_or_folder(location, name): ################### NEHOTOVE
    print("work")

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
            for i in viewable:   
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

def check_to_open():
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

def is_drive():
    global drives, location
    for i in drives:
        if i==location:
            return True

def open():
    global location, info, to_open, errors, drives, page
    new_location = ""
    if to_open>len(visible) or to_open<1:
        errors.append("open_nonexistent")        
    elif location=="select":
        location = visible[to_open-1]["name"]
    else:
        if is_drive():
            new_location = location + visible[to_open-1]["name"]
        elif location=="root":
            new_location = visible[to_open-1]["name"]
        else:
            new_location = location + "\\" + visible[to_open-1]["name"]
        if os.path.isdir(new_location):
            location = new_location
            info.append("open_dir_success")
            page = 1
        elif os.path.isfile(new_location):
            os.startfile(new_location)
            info.append("open_file_succes")
        else:
            errors.append("file_does_not_exist")

def get_dirsize():
    global info, to_open, errors, dirsize
    new_location = ""
    if to_open>len(visible) or to_open<1:
        errors.append("dirsize_nonexistent")
    else:
        if is_drive():
            new_location = location + visible[to_open-1]["name"]
        elif location=="select":
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

def do_remove():
    global info, errors, selected, successful, failed
    if len(selected)==0:
        errors.append("remove_nothing_to_remove")
        return
    else:
        for i in range(len(selected)):
            rprint("[bold red]Bude odstraněna položka - " + selected[i] + "[/bold red]")
        if not confirm.ask("Opravdu chcete smazat " + str(len(selected)) + " položek??"):
            info.append("remove_abort")
            return
        for i in range(len(selected)):
            if os.path.exists(selected[i]):
                if os.path.isfile(selected[i]):
                    if remove_file(selected[i]):
                        successful+=1
                    else:
                        errors.append("Nelze odstranit položku - " + selected[i])
                        failed+=1
                elif os.path.isdir(selected[i]):
                    if len(os.listdir(selected[i]))==0:
                        if remove_directory(selected[i]):
                            successful+=1
                        else:
                            errors.append("Nelze odstranit položku - " + selected[i])
                            failed+=1
                    else:
                        if remove_tree_directory(selected[i]):
                            successful+=1
                        else:
                            errors.append("Nelze odstranit položku - " + selected[i])
                            failed+=1
            else:
                errors.append("Neexistuje tato cesta - " + selected[i])
    selected = []
    info.append("remove_successful")

def do_copy():
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
    else:
        for i in range(len(selected)):
            if os.path.exists(selected[i]):
                if os.path.isfile(selected[i]):
                    if os.path.exists(location+"\\"+os.path.basename(selected[i])):
                        errors.append("Položka - " + os.path.basename(selected[i]) + " již existuje v umístění - " + location + " , nelze kopírovati")
                        failed+=1
                    elif copy_file(selected[i], location+"\\"+os.path.basename(selected[i])):
                        successful+=1
                    else:
                        errors.append("Nelze kopírovat položku - " + selected[i] + " do umístění - " + location)
                        failed+=1
                elif os.path.isdir(selected[i]):
                    #create_directory(location, os.path.basename(selected[i]))
                    if os.path.exists(location+"\\"+os.path.basename(selected[i])):
                        errors.append("Složka - " + os.path.basename(selected[i]) + " již existuje v umístění - " + location + " , nelze kopírovati")
                        failed+=1
                    elif copy_entire_directory(selected[i], location+"\\"+os.path.basename(selected[i])):
                        successful+=1
                    else:
                        errors.append("Nelze kopírovat položku - " + selected[i] + " do umístění - " + location)
                        failed+=1
            else:
                errors.append("Neexistuje tato cesta - " + selected[i])
    info.append("copy_successful")

def do_move():
    global info, errors, successful, failed
    if len(selected)==0:
        errors.append("move_nothing_to_move")
        return
    elif location=="select":
        errors.append("move_no_move_in_select")
        return
    elif location=="root":
        errors.append("move_no_move_in_root")
    else:
        for i in range(len(selected)):
            if os.path.exists(selected[i]):
                if move_file_or_directory(selected[i], location):
                    successful+=1
                else:
                    errors.append("Nelze přesunout položku - " + selected[i] + " do umístění - " + location)
                    failed+=1
            else:
                errors.append("Neexistuje tato cesta - " + selected[i])
    info.append("move_successful")
    selected = []

def check_to_up():
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
    global new_dir, errors, info
    if location=="root":
        errors.append("make_dir_no_root")
    elif location=="select":
        errors.append("make_dir_no_select")
    else:    
        if create_directory(location, new_dir):
            info.append("make_dir_successful")
        else:
            errors.append("make_dir_failed")
    new_dir = ""

def go_up():
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
        location="root"
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
  
def print_errors():
    global errors
    for i in errors:
        match i:
            case "no_input":
                rprint("[bold red]Nezadali jste žádný vstup[/bold red]")
            case "select_bad_input":
                rprint("[bold red]Zadali jste špatný vstup pro funkci select[/bold red]")
            case "unknown_command":
                rprint("[bold red]Zadali jste neznámý, nebo špatný příkaz[/bold red]")
            case "open_bad_input":
                rprint("[bold red]Zadali jste špatný vstup pro funkci open[/bold red]")
            case "file_does_not_exist":
                rprint("[bold red]Soubor či složka neexistuje[/bold red]")
            case "permission_error":
                rprint("[bold red]Nemáte oprávnění k tomuto úkonu[/bold red]")
            case "up_bad_input":
                rprint("[bold red]Zadali jste špatný vstup pro funkci up[/bold red]")
            case "drive_does_not_exist":
                rprint("[bold red]Vámi zvolený disk neexistuje[/bold red]")
            case "drive_bad_input":
                rprint("[bold red]Zadali jste špatný vstup pro funkci drive[/bold red]")
            case "no_drive_no_root":
                rprint("[bold red]Není zvolen disk, nejde se proto dostat do jeho kořene[/bold red]")
            case "no_select_in_roots":
                rprint("[bold red]Kořeny disků nelze označovat[/bold red]")
            case "no_add_in_roots":
                rprint("[bold red]Kořeny disků nelze přidat k označeným[/bold red]")
            case "open_nonexistent":
                rprint("[bold red]Nelze otevřít soubor či složku na indexu, který neexistuje[/bold red]")
            case "invalid_index_of_select":
                rprint("[bold red]Zadali jste špatné ID, při spouštění posledního příkazu, tato ID jsou ignorována[/bold red]")
            case "no_select_in_select":
                rprint("[bold red]Nemůžete si poznačit věci již poznačené[/bold red]")
            case "rows_bad_input":
                rprint("[bold red]Zadali jste špatný vstup pro funkci rows[/bold red]")
            case "next_bad_input":
                rprint("[bold red]Zadali jste špatný vstup pro funkci next[/bold red]")
            case "previous_bad_input":
                rprint("[bold red]Zadali jste špatný vstup pro funkci previous[/bold red]")
            case "nowhere_to_go_next": 
                rprint("[bold red]Nelze otevřít další stranu, jelikož neexistuje[/bold red]")
            case "nowhere_to_go_previous":
                rprint("[bold red]Nelze otevřít předchozí stranu, jelikož neexistuje[/bold red]")
            case "no_up_in_root":
                rprint("[bold red]Nejde jít více nahoru, již jsme v rootu[/bold red]")
            case "up_bad_input":
                rprint("[bold red]Zadali jste špatný vstup pro funkci up[/bold red]")
            case "dirsize_nonexistent":
                rprint("[bold red]Zadali jste neexistující index, při zavolání funkce dirsize[/bold red]")
            case "file_or_does_not_exist_dir_in_dirsize":
                rprint("[bold red]Nelze zjistit velikost pro položku na zadaném indexu[/bold red]")
            case "dirsize_bad_input":
                rprint("[bold red]Zadali jste špatný vstup pro funkci dirsize[/bold red]")
            case "remove_nothing_to_remove":
                rprint("[bold red]Není co bych smazal[/bold red]")
            case "copy_nothing_to_copy":
                rprint("[bold red]Nejsou vybrány žádné položky ke kopírování[/bold red]")
            case "copy_no_copy_in_select":
                rprint("[bold red]Nelze kopírovat do vyznačených[/bold red]")
            case "copy_no_copy_in_root":
                rprint("[bold red]Nelze kopírovat do kořene disků[/bold red]")
            case "move_nothing_to_move":
                rprint("[bold red]Nejsou vybrány žádné položky k přesunutí[/bold red]")
            case "move_no_move_in_select":
                rprint("[bold red]Nelze přesouvat do vyznačených[/bold red]")
            case "move_no_move_in_root":
                rprint("[bold red]Nelze přesouvat do kořene disků[/bold red]")
            case "make_dir_no_root":
                rprint("[bold red]Nelze vytvořit nový adresář v kořeni disků[/bold red]")
            case "make_dir_no_select":
                rprint("[bold red]Nelze vytvořit nový adresář v seznamu poznačených[/bold red]")
            case "make_dir_bad_input":
                rprint("[bold red]Zadali jste špatný vstup pro funkci makedir[/bold red]")
            case "make_dir_failed":
                rprint("[bold red]Nelze vytvořit nový adresář[/bold red]")
            case "rename_bad_input":
                rprint("[bold red]Zadali jste špatný vstup pro funkci rename[/bold red]")
            case "rename_more_select_no_advanced":
                rprint("[bold red]Je vybráno více položek k přejmenování, ale nezadali jste rozšiřující parametry funkce rename[/bold red]")
            case "rename_advanced_but_one":
                rprint("[bold red]Zadali jste rozšířené parametry funkce rename, ale máte zvolenou pouze jednu položku k přejmenování[/bold red]")
            case "rename_nothing_to_rename":
                rprint("[bold red]Nejsou vybrány žádné položky k přejmenování[/bold red]")
            case "copyrename_no_copy_in_select":
                rprint("[bold red]Nelze kopírovat (a přejmenovávat) do vyznačených[/bold red]")
            case "copyrename_no_copy_in_root":
                rprint("[bold red]Nelze kopírovat (a přejmenovávat) do kořene disků[/bold red]")
            case "copyrename_bad_input":
                rprint("[bold red]Zadali jste špatný vstup pro funkci copyrename[/bold red]")
            case "copyrename_more_select_no_advanced":
                rprint("[bold red]Je vybráno více položek ke kopírování a přejmenování, ale nezadali jste rozšiřující parametry funkce copyrename[/bold red]")
            case "copyrename_advanced_but_one":
                rprint("[bold red]Zadali jste rozšířené parametry funkce copyrename, ale máte zvolenou pouze jednu položku ke kopírování a přejmenování[/bold red]")
            case "copyrename_nothing_to_copyrename":
                rprint("[bold red]Nejsou vybrány žádné položky ke kopírování a přejmenování[/bold red]")
            case _:
                rprint("[bold red]" + i + "[/bold red]")
    errors = []

def print_info():
    global info, successful, failed
    for i in info:
        match i:
            case "select_success":
                rprint("[bold green]Soubory a složky úspěšně poznačeny[/bold green]")
            case "open_dir_success":
                rprint("[bold green]Vybraná složka je otevřená[/bold green]")
            case "open_file_success":
                rprint("[bold green]Vybraný soubor otevřen v externí aplikaci[/bold green]")
            case "refreshed":
                rprint("[bold green]Je zaktualizováno[/bold green]")
            case "up_success":
                rprint("[bold green]Posunuto výše[/bold green]")
            case "root_success":
                rprint("[bold green]Jsme v kořeni disku[/bold green]")
            case "roots_success":
                rprint("[bold green]Jsme v kořeni disků[/bold green]")
            case "drive_success":
                rprint("[bold green]Zobrazen Vámi zvolený disk[/bold green]")
            case "add_success":
                rprint("[bold green]Soubory a složky úspěšně přidány k poznačeným[/bold green]")
            case "showselect_success":
                rprint("[bold green]Poznačené soubory a složky jsou zobrazeny[/bold green]")
            case "unselect_success":
                rprint("[bold green]Zvolená poznačení jsou odznačena[/bold green]")
            case "rows_success":
                rprint("[bold green]Maximální počet řádků tabulky výpisu úspěšně změněn[/bold green]")
            case "next_success":
                rprint("[bold green]Zobrazen Vámi zvolený další list[/bold green]")
            case "previous_success":
                rprint("[bold green]Zobrazen Vámi zvolený předchozí list[/bold green]")
            case "dirsize_success":
                rprint("[bold green]Velikost složky na indexu [/bold green][bold blue]" + str(to_open) + "[bold green] je [/bold green][bold blue]" + str(int(dirsize/1024)) + "[/bold blue][bold green] KB[/bold green]")
            case "remove_successful":
                rprint("[bold green]Úspěšně odstraněno [/bold green][bold blue]" + str(successful) + "[/bold blue][bold green] položek, selhalo odstraňování [/bold green][bold red]" + str(failed) + "[/bold red][bold green] položek[/bold green]")
                rprint("[bold green]Seznam poznačených položek je smazán, jelikož položky neexistují[/bold green]")
            case "remove_abort":
                rprint("[bold green]Odstraňování zrušeno[/bold green]")
            case "copy_successful":
                rprint("[bold green]Úspěšně zkopírováno [/bold green][bold blue]" + str(successful) + "[/bold blue][bold green] položek, selhalo kopírování [/bold green][bold red]" + str(failed) + "[/bold red][bold green] položek[/bold green]")
            case "copy_successful":
                rprint("[bold green]Úspěšně přesunuto [/bold green][bold blue]" + str(successful) + "[/bold blue][bold green] položek, selhalo přesouvání [/bold green][bold red]" + str(failed) + "[/bold red][bold green] položek[/bold green]")
            case "make_dir_successful":
                rprint("[bold green]Nový adresář úspěšně vytvořen[/bold green]")
            case "rename_successful":
                rprint("[bold green]Úspěšně přejmenováno [/bold green][bold blue]" + str(successful) + "[/bold blue][bold green] položek, selhalo přejmenování [/bold green][bold red]" + str(failed) + "[/bold red][bold green] položek[/bold green]")
            case "copyrename_successful":
                rprint("[bold green]Úspěšně zkopírováno a přejmenováno [/bold green][bold blue]" + str(successful) + "[/bold blue][bold green] položek, selhalo kopírování a přejmenování [/bold green][bold red]" + str(failed) + "[/bold red][bold green] položek[/bold green]")
    info = []
    successful = failed = 0

def print_app_info():
    clear()
    rprint("[bold green]-------------------------------------------------------[/bold green]")
    rprint("[bold blue] ------ Leek - the file manager[/bold blue]")
    rprint("[bold red] ------ Pórek - správce souborů[/bold red]")
    rprint("[bold green]-------------------------------------------------------[/bold green]")
    rprint("[bold cyan] ------ verze: [/bold cyan][bold white]" + version + "[/bold white]")
    rprint("[bold magenta] ------ autor: [/bold magenta][bold white]" + author + "[/bold white]")
    rprint("[bold green] ------ vytvořeno: [/bold green][bold white]" + year + "[/bold white]")
    rprint("[bold green]-------------------------------------------------------[/bold green]")
    rprint("[bold red] ------ Tento program využívá Python3 a rich, díky :smiley:[/bold red]")
    rprint("[bold green]-------------------------------------------------------[/bold green]")

    input("Zmáčkněte Enter pro skrytí těchto informací: ")

def print_help():
    text = Text(justify="full")
    rprint(Panel(Text("Vítejte v podpoře programu Leek (no leak)", style="bold white", justify="center")))
    textik = "Leek (pórek) je jednoduchý konzolový správce souborů ovládaný krátkými příkazy, jakožto každý správce souborů umí zobrazovat soubory, složky a základní informace o nich, veškeré zobrazování se děje na tabulkových listech"
    textik+= ", jejichž velikost si můžete sami upravit. Zároveň můžete volně mezi těmito listy přecházet. Soubory, disky a složky voláte dle jejich zobrazovaného ID. Leek je schopen volně přecházet mezi disky, vracet se zpět na root disku i na root celku."
    textik+= " Zobrazení můžete kdykoli aktualizovat. Součástí leek je i jednoduché sledování chyb a úspěšných operací, které uživateli umožní se jednoduše vyznat ve výsledcích zadaných příkazů."
    textik+= " V leeku si můžete poznačovat soubory pro budoucí práci s nimi, soubory poznačené si také můžete nechat zobrazit, nebo je odoznačovat. Leek samozřejmě umí soubory a složky přesouvat,"
    textik+= " přejmenovávat, kopírovat, kopírovat a přejmenovávat, mazat, vyhledávat v nich a zobrazení různě seřazovat."
    text.append(textik, style="bold yellow")
    rprint(Panel(text, title="Základní informace" ,style="bold blue"))
    textik = " - [bold blue]select [číslo/čísla oddělená mezerou/rozsah (tento parametr je volitelný)][/bold blue]\n - - Odoznačí aktuální poznačené a poznačí si výběr, k označení se používá ID položek v aktuální lokaci, příklady parametrů ->\n - - - select |-> bez parametru označí všechny položky v aktualním adresáři\n"
    textik+= " - - - select 1 |-> označí položku s ID 1\n - - - select 1 2 3 7 8 9 |-> označí položky s napsanými ID\n - - - select 1 - 15 |-> označí položky z daného rozsahu\n - - Veškeré duplicitní záznamy se ignorují, chybné a neexistující výběry zobrazí chybu.\n"
    textik+= " - [bold blue]add [číslo/čísla oddělená mezerou/rozsah (tento parametr je volitelný)][/bold blue]\n - - Přidá k označeným vybrané, k označení se používá ID položek v aktuální lokaci, příklady parametrů ->\n - - - add |-> bez parametru přidá k označeným všechny položky v aktuálním adresáři\n"
    textik+= " - - - add 1 |-> přidá k označeným položku s ID 1\n - - - add 1 2 3 7 8 9 |-> přidá k označeným položky s napsanými ID\n - - - add 1 - 15 |-> přidá k označeným položky z daného rozsahu\n - - Veškeré duplicitní záznamy se ignorují, chybné a neexistující výběry zobrazí chybu.\n"
    textik+= " - [bold blue]showselect[/bold blue]\n - - Zobrazí seznam označených\n"
    textik+= " - [bold blue]unselect [číslo/čísla oddělená mezerou/rozsah (tento parametr je volitelný)][/bold blue]\n - - Odoznačí aktuální poznačené podle zadaného výběru, k odoznačení se používá ID položek v seznamu označených (zobrazte si je pomocí showselect), příklady parametrů ->\n - - - unselect |-> bez parametru odoznačí všechno označené v seznamu označených\n"
    textik+= " - - - unselect 1 |-> odoznačí položku s ID 1 v seznamu označených\n - - - unselect 1 2 3 7 8 9 |-> odoznačí položky s napsanými ID v seznamu označených|n - - - unselect 1 - 15 |-> odoznačí položky z daného rozsahu v seznamu označených\n - - Veškeré duplicitní záznamy se ignorují, chybné a neexistující výběry zobrazí chybu.\n"
    textik+= " - [bold blue]root[/bold blue]\n - - zobrazí kořen aktuálního adresáře\n - [bold blue]roots[/bold blue]\n - - zobrazí kořeny adresářů\n - [bold blue]help[/bold blue]\n - - zobrazí pomoc, kterou teď čtete, přece víte jak jste se sem dostali\n - [bold blue]refresh[/bold blue]\n - - přenačte zobrazení a disky\n"
    textik+= " - [bold blue]exit[/bold blue]\n - - ukončí program\n - [bold blue]info[/bold blue]\n - - zobrazí informace o programu\n"
    textik+= " - [bold blue]rows !číslo (povinný parametr)![/bold blue]\n - - Nastaví počet řádků tabulky na číslo zadané v parametru, příklady parametrů ->\n - - - rows 20 |-> nastaví počet řádků na 20\n - - Minimum řádků je 10, jakékoli menší číslo vyústí v chybu\n"
    textik+= " - [bold blue]open !číslo (povinný parametr)![/bold blue]\n - - Otevře soubor či složku na daném iD v aktuální lokaci, příklady parametrů ->\n - - - open 4 |-> otevře položku na ID 4 v aktuální lokaci\n - - Pokud se jedná o soubor, tak bude otevřen ve výchozí aplikaci systému\n - - Pokud jde o složku, tak do ní budete přesunuti\n"
    textik+= " - [bold blue]drive !znak disku (povinný parametr)![/bold blue]\n - - Otevře disk daný znakem disku, příklady parametrů ->\n - - - drive f |-> otevře disk F:\\\\\n - - Pokud zadáte něco jiného, než platný znak disku, tak to bude považováno za chybu\n"
    textik+= " - [bold blue]up [číslo (tento parametr je volitelný)][/bold blue]\n - - Přesune Vás o adresář výše, v případě zadání čísla Vás posune o tolik adresářů výše, kolik je dané číslo, příklady parametrů ->\n - - - up |-> posune Vás o jeden adresář výše\n"
    textik+= " - - - up 6 |-> posune Vás o 6 adresářů výše\n - - Pokud zadáte číslo menší jak 1, tak se zobrazí chyba\n - - Pokud zadáte číslo větší, než kolikrát je možné jít výše, tak se program pokusí jít co nejvýše\n"
    textik+= " - [bold blue]next [číslo (tento parametr je volitelný)][/bold blue]\n - - Pokud je více stran k zobrazení všech položek v aktuální lokaci, tak se můžete díky tomuto příkazu posunout na další stranu, či o více stran podle čísla, které zadáte, příklady parametrů ->\n"
    textik+= " - - - next |-> posune Vás na další stranu\n - - - next 6 |-> posune Vás o 6 stran od začátku\n - - Pokud zadáte číslo menší jak 1, tak program ohlásí chybu\n - - Pokud zadáte povel na přechod na stranu neexistující, tak se program pokusí k ní dostat co nejblíže a ohlásí chybu\n"
    textik+= " - [bold blue]previous [číslo (tento parametr je volitelný)][/bold blue]\n - - Pokud je více stran k zobrazení všech položek v aktuální lokaci, tak se můžete díky tomuto příkazu posunout na předchozí stranu, či o více stran podle čísla, které zadáte, příklady parametrů ->\n"
    textik+= " - - - previous |-> posune Vás na předchozí stranu|n - - - previous 6 |-> posune Vás o 6 stran k začátku\n - - Pokud zadáte číslo menší jak 1, tak program ohlásí chybu\n - - Pokud zadáte povel na přecho na stranu neexistující, tak program se program pokusí k ní dostat co nejblíže a ohlásí chybu\n"
    textik+= " - [bold blue]remove[/bold blue]\n - - Smaže aktuální označené položky - soubory, složky i soubory a složky vnořené.\n - - Zjistí počet úspěšných a chybných odstranění a vypíše informace o výsledku příkazu.\n"
    textik+= " - [bold blue]copy[/bold blue]\n - - Zkopíruje označené položky do aktuálního adresáře - soubory, složky i soubory a složky vnořené.\n - - Zjistí počet úspěšných a chybných kopírovaní a vypíše informace o výsledku příkazu.\n"
    textik+= " - [bold blue]move[/bold blue]\n - - Přesune označené položky do aktuálního adresáře - soubory, složky i soubory a složky vnořené.\n - - Zjistí počet úspěšných a chybných přesunutí a vypíše informace o výsledku příkazu.\n"
    textik+= " - [bold blue]makedir !název (povinný parametr)![/bold blue]\n - - Vytvoří v aktuálním adresáři nový adresář se zadaným názvem od uživatele, příklady parametrů ->\n - - - makedir NewFolder |-> vytvoří v aktuálním adresáři nový adresář s názvem NewFolder\n - - Vypíše informace o výsledku provedení příkazu.\n"
    textik+= " - [bold blue]rename !nový_název (povinný parametr)! [!kde začátek_počítadla změna_počítadla minimální_počet_míst přípona_nebo_koncovka (polovinné parametry)!][/bold blue]\n"
    textik+= " - - Přejmenuje vybraný soubor či složku, nebo vybrané soubory či složky. Přejmenovává položky v seznamu poznačených.\n - - Pokud je pouze jedna položka k přejmenování je povinný parametr pouze nový_název, jinak jsou povinné i další parametry.\n"
    textik+= " - - nový_název - jedna část názvu, kde - after/before - pozice počítadla před či za novým_názvem, začátek_počítadla - startovní index\n - - změna_počítadla - o jaké číslo se bude počítadlo pravidelně měnit, minimální_počet_míst - minimální počet míst počítadla, přípona_nebo_koncovka - název připojený ke konci nového názvu\n"
    textik+= " - - Zjistí počet chybných a úspěšných přejmenování a vypíše výsledek příkazu a zda nedošlo k chybě, príklady parametrů ->\n - - - rename ahoj.txt |-> pokud pouze jeden soubor je vybrán tak bude přejmenován na název ahoj.txt\n"
    textik+= " - - - rename obrazek after 0 1 4 .jpg |-> všechny položky které jsou poznačené budou přejmenovány takto - obrazek0000.jpg, obrazek0001.jpg, ..........\n"
    textik+= " - [bold blue]copyrename !nový_název (povinný parametr)! [!kde začátek_počítadla změna_počítadla minimální_počet_míst přípona_nebo_koncovka (polovinné parametry)!][/bold blue]\n"
    textik+= " - - Zkopíruje a přejmenuje vybraný soubor či složku, nebo vybrané soubory či složky. Kopíruje a přejmenovává položky v seznamu poznačených do aktuálního adresáře.\n - - Pokud je pouze jedna položka ke kopírování a přejmenování je povinný parametr pouze nový_název, jinak jsou povinné i další parametry.\n"
    textik+= " - - nový_název - jedna část názvu, kde - after/before - pozice počítadla před či za novým_názvem, začátek_počítadla - startovní index\n - - změna_počítadla - o jaké číslo se bude počítadlo pravidelně měnit, minimální_počet_míst - minimální počet míst počítadla, přípona_nebo_koncovka - název připojený ke konci nového názvu\n"
    textik+= " - - Zjistí počet chybných a úspěšných kopírování a přejmenování a vypíše výsledek příkazu a zda nedošlo k chybě, príklady parametrů ->\n - - - copyrename ahoj.txt |-> pokud pouze jeden soubor je vybrán tak bude kopírován do aktuálního adresáře a přejmenován na název ahoj.txt\n"
    textik+= " - - - copyrename obrazek after 0 1 4 .jpg |-> všechny položky které jsou poznačené budou zkopírovány do aktuálního adresáře a přejmenovány takto - obrazek0000.jpg, obrazek0001.jpg, ..........\n"
    
    rprint(Panel(textik, title="Seznam příkazů a vysvětlení", style="bold green"))
    
    input("Zmáčkněte Enter pro skrytí těchto informací: ")

def print_page():
    rprint("[bold blue]Stránka " + str(page) + " z " + str(max_page) + ". Celkem " + str(len(viewable)) + " souborů/složek/disků. Zobrazeno " + str(len(visible)) + ".[/bold blue]")

def create_table():
    global table
    table = Table(title=location)
    table.add_column("ID", justify="center", style="blue", no_wrap=True)
    table.add_column("Název souboru / složky", justify="left", style="green", no_wrap=True)
    table.add_column("Velikost v KB", justify="center", style="yellow", no_wrap=True)
    table.add_column("Založeno", justify="center", style="white", no_wrap=True)
    table.add_column("Upraveno", justify="center", style="cyan", no_wrap=True)
    table.add_column("Práva", justify="center", style="red", no_wrap=True)
    
    if location=="root":
        for i in range(len(visible)):
            table.add_row(str(visible[i]["id"]), visible[i]["name"], "", "", "", "")
    else:
        for i in range(len(visible)):
            table.add_row(str(visible[i]["id"]), visible[i]["name"], str(visible[i]["size"]), timedate(visible[i]["created"]), timedate(visible[i]["changed"]), str(visible[i]["rights"]))

def get_file_record_as_dictionary(files, i):
    global location
    if location=="select":
        file_location = files[i]
        file_info = get_info_about_file(file_location)
        if os.path.isdir(file_location):
            return {"id" : i+1, "name" : files[i], "size" : "--", "created" : file_info[9], "changed" : file_info[8], "rights" : file_info[0]}
        if os.path.isfile(file_location):
            return {"id" : i+1, "name" : files[i], "size" : int(float(file_info[6])/1024), "created" : file_info[9], "changed" : file_info[8], "rights" : file_info[0]}
    elif is_drive():
        file_location = location + files[i]
    else:
        file_location = location + "\\" + files[i]
    file_info = get_info_about_file(file_location)
    if os.path.isdir(file_location):
        return {"id" : i+1, "name" : files[i], "size" : "--", "created" : file_info[9], "changed" : file_info[8], "rights" : file_info[0]}
    if os.path.isfile(file_location):
        return {"id" : i+1, "name" : files[i], "size" : int(float(file_info[6])/1024), "created" : file_info[9], "changed" : file_info[8], "rights" : file_info[0]}

def timedate(seconds):
    return datetime.fromtimestamp(seconds).strftime("%d/%m/%Y-%H:%M:%S")

def create_viewable():
    global viewable, drives, errors, selected
    viewable = {}
    if location=="root":
        for i in range(len(drives)):
            viewable[i] = {"id" : i+1, "name" : drives[i], "size" : "", "created" : "", "changed" : "", "rights" : ""}
    elif location=="select":
        for i in range(len(selected)):
            viewable[i] = get_file_record_as_dictionary(selected, i)
    else:
        files = get_list_of_files(location)
        if not files:
            if "open_dir_success" in errors:
                errors.remove("open_dir_success")
            return
        for i in range(len(files)):
            viewable[i] = get_file_record_as_dictionary(files, i)

def go_root():
    global location, info, errors, page
    if location=="root":
        errors.append("no_drive_no_root")        
    else:
        location = location[:4]
        info.append("root_success")
        page = 1        

def check_new_dir_name():
    global new_dir, user_input, errors
    user_input.pop(0)
    if len(user_input)!=1:
        errors.append("make_dir_bad_input")
        return False
    else:
        new_dir = str(user_input[0])
        return True

def check_drive():
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

def calculate_pages():
    global rows, viewable, visible, page, max_page
    max_page = 1
    while len(viewable)>(max_page*rows):
        max_page = max_page + 1

def create_visible():
    global viewable, visible
    j = 0
    calculate_pages()
    visible = {}
    for i in range(len(viewable)):
        if not i<((rows*page)-rows):
            if i<rows*page:
                visible[j] = viewable[i].copy()
                visible[j]["id"] = j+1
                j = j + 1
    
def go_unselect():
    global selected, info, location, to_select, errors
    to_select = list(set(to_select))
    to_select.sort(reverse=True)
    if len(selected)>0:
        for i in range(len(to_select)):
            selected.pop(to_select[i]-1)
    to_select = []
    info.append("unselect_success")

def check_next_previous():
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
    global user_input, r_new_name, errors, r_place, r_counter_begin, r_increment, r_n_digit, r_advanced, r_file_type
    r_advanced = False
    r_place = r_new_name = r_file_type = error = ""
    r_counter_begin = r_n_digit = r_increment = 0
    match how:
        case "copy": error = "rename_bad_input"
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

def do_rename():
    global info, r_new_name, errors, r_place, r_counter_begin, r_increment, r_n_digit, r_advanced, failed, successful, selected, r_file_type
    if len(selected)==0:
        errors.append("rename_nothing_to_rename")
    elif not r_advanced:
        if len(selected)==1:
            if rename_file_or_directory(selected[0], r_new_name):
                successful+=1
                info.append("rename_successful")
            else:
                errors.append("Nelze přejmenovat položku - " + selected[i] + " na - " + r_new_name)
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
                                    digits_to_append = r_n_digit - len(str(counter))
                                    if digits_to_append<0: digits_to_append = 0
                                    new_name = str(counter)
                                    while digits_to_append>0:
                                        new_name = "0" + new_name
                                        digits_to_append-=1
                                    counter+=r_increment
                                    if r_new_name!="\\none\\":
                                        new_name+=r_new_name
                                    if r_file_type!="\\none\\":
                                        new_name+=r_file_type
                    case "after":
                                    if r_new_name!="\\none\\":
                                        new_name+=r_new_name
                                    digits_to_append = r_n_digit - len(str(counter))
                                    if digits_to_append<0: digits_to_append = 0
                                    new_name = str(counter)
                                    while digits_to_append>0:
                                        new_name = "0" + new_name
                                        digits_to_append-=1
                                    counter+=r_increment
                                    if r_file_type!="\\none\\":
                                        new_name+=r_file_type
                if rename_file_or_directory(selected[i], new_name):
                    successful+=1
                else:
                    errors.append("Nelze přejmenovat položku - " + selected[i] + " na - " + new_name)
                    failed+=1
            info.append("rename_successful")
        else:
            errors.append("rename_advanced_but_one")
    selected = []

def do_copyrename():
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
    elif not r_advanced:
        if len(selected)==1:
            if os.path.exists(selected[0]):
                if os.path.isfile(selected[0]):
                    if os.path.exists(location+"\\"+r_new_name):
                        errors.append("Položka - " + r_new_name + " již existuje v umístění - " + location + " , nelze kopírovati")
                        failed+=1
                    elif copy_file(selected[0], location+"\\"+r_new_name):
                        successful+=1
                    else:
                        errors.append("Nelze kopírovat položku - " + selected[0] + " do umístění - " + location + " a přejmenovat ji na - " + r_new_name)
                        failed+=1
                if os.path.isdir(selected[0]):
                    if os.path.exists(location+"\\"+r_new_name):
                        errors.append("Složka - " + r_new_name + " již existuje v umístění - " + location + " , nelze kopírovati")
                        failed+=1
                    elif copy_entire_directory(selected[0], location+"\\"+r_new_name):
                        successful+=1
                    else:
                        errors.append("Nelze kopírovat položku - " + selected[0] + " do umístění - " + location  + " a přejmenovat ji na - " + r_new_name)
                        failed+=1
            else:
                errors.append("Neexistuje tato cesta - " + selected[0])
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
                                    digits_to_append = r_n_digit - len(str(counter))
                                    if digits_to_append<0: digits_to_append = 0
                                    new_name = str(counter)
                                    while digits_to_append>0:
                                        new_name = "0" + new_name
                                        digits_to_append-=1
                                    counter+=r_increment
                                    if r_new_name!="\\none\\":
                                        new_name+=r_new_name
                                    if r_file_type!="\\none\\":
                                        new_name+=r_file_type
                    case "after":
                                    if r_new_name!="\\none\\":
                                        new_name+=r_new_name
                                    digits_to_append = r_n_digit - len(str(counter))
                                    if digits_to_append<0: digits_to_append = 0
                                    new_name = str(counter)
                                    while digits_to_append>0:
                                        new_name = "0" + new_name
                                        digits_to_append-=1
                                    counter+=r_increment
                                    if r_file_type!="\\none\\":
                                        new_name+=r_file_type
                if os.path.exists(selected[i]):
                    if os.path.isfile(selected[i]):
                        if os.path.exists(location+"\\"+new_name):
                            errors.append("Položka - " + new_name + " již existuje v umístění - " + location + " , nelze kopírovati")
                            failed+=1
                        elif copy_file(selected[i], location+"\\"+new_name):
                            successful+=1
                        else:
                            errors.append("Nelze kopírovat položku - " + selected[i] + " do umístění - " + location + " a přejmenovat ji na - " + new_name)
                            failed+=1
                    if os.path.isdir(selected[i]):
                        if os.path.exists(location+"\\"+new_name):
                            errors.append("Složka - " + new_name + " již existuje v umístění - " + location + " , nelze kopírovati")
                            failed+=1
                        elif copy_entire_directory(selected[i], location+"\\"+new_name):
                            successful+=1
                        else:
                            errors.append("Nelze kopírovat položku - " + selected[i] + " do umístění - " + location  + " a přejmenovat ji na - " + new_name)
                            failed+=1
                else:
                    errors.append("Neexistuje tato cesta - " + selected[i])
        else:
            errors.append("coopyrename_advanced_but_one")
            return
    info.append("copyrename_successful")

def check_get_rows():
    global user_input, info, rows, errors, page
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
            rows = new_rows
            info.append("rows_success")
            page = 1

def do_next_previous():
    global location, info, errors, drives, distance, direction, page
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

def do_select_or_add(what):
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

def clear(): os.system('cls')

def refresh_all():
    global drives
    drives = get_list_of_drives()
    create_viewable()
    create_visible()

def main():
    global work, errors, info, table, location, direction, page, type_select
    refresh_all()
    clear()
    create_table()

    rprint(table)
    print_page()
    print_errors()
    print_info()
    if check_input(prompt.ask("[bold]Zadej příkaz [/bold](help)")):
        match user_input[0]:
            case "select": 
                if check_to_select():
                    check_validity_to_select()
                    do_select_or_add("select")
            case "rename":
                if check_to_rename("copy"):
                    do_rename()
            case "remove":
                do_remove()
            case "copy": 
                do_copy()
            case "move":
                do_move()
            case "up":
                if check_to_up():
                    go_up()
            case "search":
                print()
            case "sort": 
                print()
            case "showselect": 
                location = "select"
                info.append("showselect_success")
                page = 1
            case "copyrename":
                if check_to_rename("copyrename"):
                    do_copyrename()
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
                print_help()
            case "refresh":
                info.append("refreshed")
                return
            case "add":
                if check_to_select():
                    check_validity_to_select()
                    do_select_or_add("add")
            case "exit":
                work = False
            case "open":
                if check_to_open():
                    open()
            case "rows":
                check_get_rows()
            case "info":
                print_app_info()
            case "dirsize":
                if check_to_open():
                    get_dirsize()
            case "makedir":
                if check_new_dir_name():
                    make_dir()
                print()
            case _:
                errors.append("unknown_command")
   
while work:
    main()
rprint("[bold blue]Mějte se[/bold blue]")