


# cannot be a message "none"

initial_locales = ['cs', 'en']
initial_localization = {
    'cs' : {
        # error messages
        'no_input' : '[bold red]Nezadali jste žádný vstup[/bold red]',
        'select_bad_input' : '[bold red]Zadali jste špatný vstup pro funkci select[/bold red]',
        'unknown_command' : '[bold red]Zadali jste neznámý, nebo špatný příkaz[/bold red]',
        'open_bad_input' : '[bold red]Zadali jste špatný vstup pro funkci open[/bold red]',
        'file_does_not_exist' : '[bold red]Soubor či složka neexistuje[/bold red]',
        'permission_error' : '[bold red]Nemáte oprávnění k tomuto úkonu[/bold red]',
        'up_bad_input' : '[bold red]Zadali jste špatný vstup pro funkci up[/bold red]',
        'drive_does_not_exist' : '[bold red]Vámi zvolený disk neexistuje[/bold red]',
        'drive_bad_input' : '[bold red]Zadali jste špatný vstup pro funkci drive[/bold red]',
        'no_drive_no_root' : '[bold red]Není zvolen disk, nejde se proto dostat do jeho kořene[/bold red]',
        'no_select_in_roots' : '[bold red]Kořeny disků nelze označovat[/bold red]',
        'no_add_in_roots' : '[bold red]Kořeny disků nelze přidat k označeným[/bold red]',
        'open_nonexistent' : '[bold red]Nelze otevřít soubor či složku na indexu, který neexistuje[/bold red]',
        'invalid_index_of_select' : '[bold red]Zadali jste špatné ID, při spouštění posledního příkazu, tato ID jsou ignorována[/bold red]',
        'no_select_in_select' : '[bold red]Nemůžete si poznačit věci již poznačené[/bold red]',
        'rows_bad_input' : '[bold red]Zadali jste špatný vstup pro funkci rows[/bold red]',
        'next_bad_input' : '[bold red]Zadali jste špatný vstup pro funkci next[/bold red]',
        'previous_bad_input' : '[bold red]Zadali jste špatný vstup pro funkci previous[/bold red]',
        'nowhere_to_go_next' : '[bold red]Nelze otevřít další stranu, jelikož neexistuje[/bold red]',
        'nowhere_to_go_previous' : '[bold red]Nelze otevřít předchozí stranu, jelikož neexistuje[/bold red]',
        'no_up_in_root' : '[bold red]Nejde jít více nahoru, již jsme v rootu[/bold red]',
        'up_bad_input' : '[bold red]Zadali jste špatný vstup pro funkci up[/bold red]',
        'dirsize_nonexistent' : '[bold red]Zadali jste neexistující index, při zavolání funkce dirsize[/bold red]',
        'file_or_does_not_exist_dir_in_dirsize' : '[bold red]Nelze zjistit velikost pro položku na zadaném indexu[/bold red]',
        'dirsize_bad_input' : '[bold red]Zadali jste špatný vstup pro funkci dirsize[/bold red]',
        'remove_nothing_to_remove' : '[bold red]Není co bych smazal[/bold red]',
        'copy_nothing_to_copy' : '[bold red]Nejsou vybrány žádné položky ke kopírování[/bold red]',
        'copy_no_copy_in_select' : '[bold red]Nelze kopírovat do poznačených[/bold red]',
        'copy_no_copy_in_root' : '[bold red]Nelze kopírovat do kořene disků[/bold red]',
        'move_nothing_to_move' : '[bold red]Nejsou vybrány žádné položky k přesunutí[/bold red]',
        'move_no_move_in_select' : '[bold red]Nelze přesouvat do vyznačených[/bold red]',
        'move_no_move_in_root' : '[bold red]Nelze přesouvat do kořene disků[/bold red]',
        'make_dir_no_root' : '[bold red]Nelze vytvořit nový adresář v kořeni disků[/bold red]',
        'make_dir_no_select' : '[bold red]Nelze vytvořit nový adresář v seznamu poznačených[/bold red]',
        'make_dir_bad_input' : '[bold red]Zadali jste špatný vstup pro funkci makedir[/bold red]',
        'make_dir_failed' : '[bold red]Nelze vytvořit nový adresář[/bold red]',
        'rename_bad_input' : '[bold red]Zadali jste špatný vstup pro funkci rename[/bold red]',
        'rename_more_select_no_advanced' : '[bold red]Je vybráno více položek k přejmenování, ale nezadali jste rozšiřující parametry funkce rename[/bold red]',
        'rename_advanced_but_one' : '[bold red]Zadali jste rozšířené parametry funkce rename, ale máte zvolenou pouze jednu položku k přejmenování[/bold red]',
        'rename_nothing_to_rename' : '[bold red]Nejsou vybrány žádné položky k přejmenování[/bold red]',
        'copyrename_no_copy_in_select' : '[bold red]Nelze kopírovat (a přejmenovávat) do vyznačených[/bold red]',
        'copyrename_no_copy_in_root' : '[bold red]Nelze kopírovat (a přejmenovávat) do kořene disků[/bold red]',
        'copyrename_bad_input' : '[bold red]Zadali jste špatný vstup pro funkci copyrename[/bold red]',
        'copyrename_more_select_no_advanced' : '[bold red]Je vybráno více položek ke kopírování a přejmenování, ale nezadali jste rozšiřující parametry funkce copyrename[/bold red]',
        'copyrename_advanced_but_one' : '[bold red]Zadali jste rozšířené parametry funkce copyrename, ale máte zvolenou pouze jednu položku ke kopírování a přejmenování[/bold red]',
        'copyrename_nothing_to_copyrename' : '[bold red]Nejsou vybrány žádné položky ke kopírování a přejmenování[/bold red]',
        'search_bad_input' : '[bold red]Zadali jste špatný vstup pro funkci search[/bold red]',
        'move_no_move_in_search' : '[bold red]Ve vyhledaných položkách zkrátka nelze přesouvati[/bold red]',
        'copyrename_no_copy_in_search' : '[bold red]Ve vyhledaných položkách zkrátka nelze kopírovati s přejmenováním[/bold red]',
        'copy_no_copy_in_search' : '[bold red]Ve vyhledaných položkách zkrátka nelze kopírovati[/bold red]',
        'make_dir_no_search' : '[bold red]Nelze vytvořit složku ve vyhledaných položkách[/bold red]',
        'locale_bad_input' : '[bold red]Zadali jste špatný vstup pro funkci locale, nebo jste zadali neexistující lokalizaci.[/bold red]',
        'saveconfig_bad_input' : '[bold red]Zadali jste špatný vstup pro funkci saveconfig.[/bold red]',
        'sizeunit_bad_input' : '[bold red]Zadali jste špatný vstup pro funkci sizeunit.[/bold red]',
        '' : '',
        '' : '',
        '' : '',
        '' : '',
        # succes messages
        'select_success' : '[bold green]Soubory a složky úspěšně poznačeny[/bold green]',
        'open_dir_success' : '[bold green]Vybraná složka je otevřená[/bold green]',
        'open_file_success' : '[bold green]Vybraný soubor otevřen v externí aplikaci[/bold green]',
        'refreshed' : '[bold green]Je zaktualizováno[/bold green]',
        'up_success' : '[bold green]Posunuto výše[/bold green]',
        'root_success' : '[bold green]Jsme v kořeni disku[/bold green]',
        'roots_success' : '[bold green]Jsme v kořeni disků[/bold green]',
        'drive_success' : '[bold green]Zobrazen Vámi zvolený disk[/bold green]',
        'add_success' : '[bold green]Soubory a složky úspěšně přidány k poznačeným[/bold green]',
        'showselect_success' : '[bold green]Poznačené soubory a složky jsou zobrazeny[/bold green]',
        'unselect_success' : '[bold green]Zvolená poznačení jsou odznačena[/bold green]',
        'rows_success' : '[bold green]Maximální počet řádků tabulky výpisu úspěšně změněn[/bold green]',
        'next_success' : '[bold green]Zobrazen Vámi zvolený další list[/bold green]',
        'previous_success' : '[bold green]Zobrazen Vámi zvolený předchozí list[/bold green]',
        'dirsize_success' : '[bold green]Velikost složky na indexu [/bold green][bold blue]{}[/bold blue][bold green] je [/bold green][bold blue]{}[/bold blue][bold green] {}[/bold green]',
        'remove_successful' : '[bold green]Úspěšně odstraněno [/bold green][bold blue]{}[/bold blue][bold green] položek, selhalo odstraňování [/bold green][bold red]{}[/bold red][bold green] položek\nSeznam poznačených položek je smazán, jelikož položky neexistují[/bold green]',
        'remove_abort' : '[bold green]Odstraňování zrušeno[/bold green]',
        'copy_successful' : '[bold green]Úspěšně zkopírováno [/bold green][bold blue]{}[/bold blue][bold green] položek, selhalo kopírování [/bold green][bold red]{}[/bold red][bold green] položek[/bold green]',
        'make_dir_successful' : '[bold green]Nový adresář úspěšně vytvořen[/bold green]',
        'rename_successful' : '[bold green]Úspěšně přejmenováno [/bold green][bold blue]{}[/bold blue][bold green] položek, selhalo přejmenování [/bold green][bold red]{}[/bold red][bold green] položek[/bold green]',
        'copyrename_successful' : '[bold green]Úspěšně zkopírováno a přejmenováno [/bold green][bold blue]{}[/bold blue][bold green] položek, selhalo kopírování a přejmenování [/bold green][bold red]{}[/bold red][bold green] položek[/bold green]',
        'search_successful' : '[bold green]Výsledky vyhledávání[/bold green]',
        'locale_successful' : '[bold green]Lokalizace byla úspěšně změněna[/bold green]',
        'available_localization_loaded' : '[bold blue]Dostupné lokalizace byly načteny[/bold blue]',
        'cannot_load_localization' : '[bold red]Selhalo načítání existujících dodatkových lokalizací[/bold red]',
        'saveconfig_successful' : '[bold green]Nastavení ukládání konfigurace aplikace bylo úspěšně změněno.[/bold green]',
        'sizeunit_successful' : '[bold green]Nastavení jednotek velikosti bylo úspěšně změněno.[/bold green]',
        '' : '',
        '' : '',
        '' : '',
        '' : '',
        # other general
        'insert_cmd' : '[bold]Zadej příkaz [/bold](help)',
        'bye_message' : '[bold blue]Mějte se[/bold blue]',
        'remove_item_message' : '[bold red]Bude odstraněna položka - {}[/bold red]',
        'remove_confirm' : '[bold red]Opravdu chcete smazat {} položek??[/bold red]',
        'item_removed' : '[bold green]Smazána položka - [/bold green][bold blue]{}[/bold blue]',
        'unable_to_remove_item' : '[bold red]Nelze odstranit položku - {}[/bold red]',
        'nonexistent_path' : '[bold red]Neexistuje tato cesta - {}[/bold red]',
        'press_enter_to_hide' : 'Zmáčkněte Enter pro skrytí těchto informací:',
        'unable_to_copy_item' : '[bold red]Nelze kopírovat položku - {} do umístění - {}[/bold red]',
        'item_copied' : '[bold green]Zkopírována položka - [/bold green][bold blue]{}[/bold blue][bold green] - do umístění - [/bold green][bold blue]{}[/bold blue]',
        'copy_folder_already_exists' : '[bold red]Složka - {} již existuje v umístění - {} , nelze kopírovati[/bold red]',
        'copy_item_already_exists' : '[bold red]Položka - {} již existuje v umístění - {} , nelze kopírovati[/bold red]',
        'unable_to_move' : '[bold red]Nelze přesunout položku - {} do umístění - {}[/bold red]',
        'item_moved' : '[bold green]Přesunuta položka - [/bold green][bold blue]{}[/bold blue][bold green] - do umístění - [/bold green][bold blue]{}[/bold blue]',
        'unable_to_rename' : '[bold red]Nelze přejmenovat položku - {} na - {}[/bold red]',
        'item_renamed' : '[bold green]Přejmenována položka - [/bold green][bold blue]{}[/bold blue][bold green] - na - [/bold green][bold blue]{}[/bold blue]',
        'unable_to_copyrename_item' : '[bold red]Nelze kopírovat položku - {} do umístění - {} a přejmenovat ji na - {}[/bold red]',
        'item_copyrenamed' : '[bold green]Položka - [/bold green][bold blue]{}[/bold blue][bold green] - zkopírována a přejmenována - výsledek - [/bold green][bold blue]{}[/bold blue]',
        'searching_in' : ' [bold green]Vyhledáváme v umístění - [/bold green][bold blue]{}[/bold blue][bold green] - Pro ukončení vypněte program[/bold green]',
        'rights' : 'Práva',
        'modified' : 'Změněno',
        'created' : 'Vytvořeno',
        'size' : 'Velikost v {}',
        'file_or_folder_name' : 'Název souboru / složky',
        'id' : 'ID',
        'none_up' : '[bold yellow]Výpis seřazen dle základního zjištění vzestupně.[/bold yellow]',
        'none_down' : '[bold yellow]Výpis seřazen dle základního zjištění sestupně.[/bold yellow]',
        'name_up' : '[bold yellow]Výpis seřazen dle názvu položek vzestupně.[/bold yellow]',
        'name_down' : '[bold yellow]Výpis seřazen dle názvu položek sestupně.[/bold yellow]',
        'created_up' : '[bold yellow]Výpis seřazen dle času vytvoření položek vzestupně.[/bold yellow]',
        'created_down' : '[bold yellow]Výpis seřazen dle času vytvoření položek sestupně.[/bold yellow]',
        'size_up' : '[bold yellow]Výpis seřazen dle velikosti položek vzestupně.[/bold yellow]',
        'size_down' : '[bold yellow]Výpis seřazen dle velikosti položek sestupně.[/bold yellow]',
        'changed_up' : '[bold yellow]Výpis seřazen dle času poslední změny položek vzestupně.[/bold yellow]',
        'changed_down' : '[bold yellow]Výpis seřazen dle času poslední změny položek sestupně.[/bold yellow]',
        'list_info' : '[bold blue]Stránka {} z {}. Celkem {} souborů/složek/disků. Zobrazeno {}.[/bold blue]',
        'cannot_load' : '[bold blue]Nelze načíst nastavení aplikace, pokud chcete nastavení ukládat, použijte příkaz [/bold blue]saveconfig true',
        'load_successful' : '[bold blue]Úspěšně se načetlo nastavení aplikace[/bold blue]',
        'cannot_save' : '[bold red]Nelze uložit nastavení aplikace[/bold red]',
        'save_successful' : '[bold blue]Úspěšně se uložilo nastavení aplikace[/bold blue]',
        'not_saving' : '[bold blue]Nastavení aplikace se neukládá[/bold blue]',
        'print_locales' : '[bold green]Dostupné jazyky jsou : {}\nPokud chcete přidat další jazyky postupujte dle návodu ve wiki na githubové stránce projektu\nPokud chcete načítat dodatečné jazyky musíte mít zapnuto ukládání konfigurace.',
        '' : '',
        '' : '',
        '' : '',
        '' : '',
        '' : '',
        '' : '',
        '' : '',
        'app_info' : 
            '''
[bold green]----------------------------------------------------------------[/bold green]
[bold blue]Leek - the file manager[/bold blue]
[bold red]Pórek - správce souborů[/bold red]
[bold green]----------------------------------------------------------------[/bold green]
[bold cyan]verze: [/bold cyan][bold white]{}[/bold white]
[bold magenta]autor: [/bold magenta][bold white]{}[/bold white]
[bold green]vytvořeno: [/bold green][bold white]{}[/bold white]
[bold green]----------------------------------------------------------------[/bold green]
[bold magenta]Projektová stránka programu: [/bold magenta][bold blue]{}[/bold blue]
[bold yellow]Stránka projektu na Githubu: [/bold yellow][bold green]{}[/bold green]
[bold red]Tento program využívá Python {} a Rich {}[/bold red]
[bold magenta]Balení do exe souboru zajišťuje Pyinstaller {}[/bold magenta]
[bold blue]Komprimaci exe souboru zajišťuje UPX {}[/bold blue]
[bold green]Komprimaci zip archivů zase zajišťuje 7-zip {}[/bold green]
[bold blue]Velice děkuji všem tvůrcům projektů, jejichž práci využívám :smiley:[/bold blue]
[bold magenta]Pokud máte návrh na zlepšení programu, nové funkce,
změny, nebo jste našli chybu, tak neváhejte navštívit githubovou
stránku projektu a o své názory se podělit[/bold magenta]
[bold green]----------------------------------------------------------------[/bold green]
            ''',
        'app_info_leek_title' : 'Info o aplikaci Leek',
        'app_help_part_one' : 
            '''
Leek (pórek) je jednoduchý konzolový správce souborů ovládaný krátkými příkazy, jakožto každý správce souborů umí zobrazovat soubory, složky a základní informace o nich, veškeré zobrazování se děje na tabulkových listech, jejichž velikost si můžete sami upravit. Zároveň můžete volně mezi těmito listy přecházet. Soubory, disky a složky voláte dle jejich zobrazovaného ID. Leek je schopen volně přecházet mezi disky, vracet se zpět na root disku i na root celku. Zobrazení můžete kdykoli aktualizovat. Součástí leek je i jednoduché sledování chyb a úspěšných operací, které uživateli umožní se jednoduše vyznat ve výsledcích zadaných příkazů. V leeku si můžete poznačovat soubory pro budoucí práci s nimi, soubory poznačené si také můžete nechat zobrazit, nebo je odoznačovat. Leek samozřejmě umí soubory a složky přesouvat, přejmenovávat, kopírovat, kopírovat a přejmenovávat, mazat, vyhledávat v nich a zobrazení různě seřazovat. Leek využívá Python verze 3.10 a knihovnu rich, minimální verzí operačního systému Windows je Win 8 asi 64bit.
            ''',
        'app_help_part_two' : 
            '''
 - [bold blue]select [číslo/čísla oddělená mezerou/rozsah (tento parametr je volitelný)][/bold blue]
   - Odoznačí aktuální poznačené a poznačí si výběr, k označení se používá ID položek v aktuální lokaci, příklady parametrů ->
     - select |-> bez parametru označí všechny položky v aktualním adresáři
     - select 1 |-> označí položku s ID 1
     - select 1 2 3 7 8 9 |-> označí položky s napsanými ID
     - select 1 - 15 |-> označí položky z daného rozsahu
   - Veškeré duplicitní záznamy se ignorují, chybné a neexistující výběry zobrazí chybu.
 - [bold blue]add [číslo/čísla oddělená mezerou/rozsah (tento parametr je volitelný)][/bold blue]
   - Přidá k označeným vybrané, k označení se používá ID položek v aktuální lokaci, příklady parametrů ->
     - add |-> bez parametru přidá k označeným všechny položky v aktuálním adresáři
     - add 1 |-> přidá k označeným položku s ID 1
     - add 1 2 3 7 8 9 |-> přidá k označeným položky s napsanými ID
     - add 1 - 15 |-> přidá k označeným položky z daného rozsahu
   - Veškeré duplicitní záznamy se ignorují, chybné a neexistující výběry zobrazí chybu.
 - [bold blue]showselect[/bold blue]
   - Zobrazí seznam označených.
 - [bold blue]unselect [číslo/čísla oddělená mezerou/rozsah (tento parametr je volitelný)][/bold blue]
   - Odoznačí aktuální poznačené podle zadaného výběru, k odoznačení se používá ID položek v seznamu označených (zobrazte si je pomocí showselect), příklady parametrů ->
     - unselect |-> bez parametru odoznačí všechno označené v seznamu označených
     - unselect 1 |-> odoznačí položku s ID 1 v seznamu označených
     - unselect 1 2 3 7 8 9 |-> odoznačí položky s napsanými ID v seznamu označených
     - unselect 1 - 15 |-> odoznačí položky z daného rozsahu v seznamu označených
   - Veškeré duplicitní záznamy se ignorují, chybné a neexistující výběry zobrazí chybu.
 - [bold blue]root[/bold blue]
   - zobrazí kořen aktuálního adresáře.
 - [bold blue]roots[/bold blue]
   - zobrazí kořeny adresářů.
 - [bold blue]help[/bold blue]
   - zobrazí pomoc, kterou teď čtete, přece víte jak jste se sem dostali.
 - [bold blue]refresh[/bold blue]
   - přenačte zobrazení a disky, stejné jako když zadáte prázdný enter.
 - [bold blue]exit[/bold blue]
   - ukončí program.
 - [bold blue]info[/bold blue]
   - zobrazí informace o programu.
 - [bold blue]rows !číslo (povinný parametr)![/bold blue]
   - Nastaví počet řádků tabulky na číslo zadané v parametru, příklady parametrů ->
     - rows 20 |-> nastaví počet řádků na 20
   - Minimum řádků je 10, jakékoli menší číslo vyústí v chybu.
 - [bold blue]open !číslo (povinný parametr)![/bold blue]
   - Otevře soubor či složku na daném iD v aktuální lokaci, příklady parametrů ->
     - open 4 |-> otevře položku na ID 4 v aktuální lokaci
   - Pokud se jedná o soubor, tak bude otevřen ve výchozí aplikaci systému
   - Pokud jde o složku, tak do ní budete přesunuti.
   - Pokud zadáte neplatné ID, nebo dojde k chybě při zpracování, program vypíše chybové hlášení.
 - [bold blue]drive !znak disku (povinný parametr)![/bold blue]
   - Otevře disk daný znakem disku, příklady parametrů ->
     - drive f |-> otevře disk F:\\\\
   - Pokud zadáte něco jiného, než platný znak disku, tak to bude považováno za chybu.
 - [bold blue]up [číslo (tento parametr je volitelný)][/bold blue]
   - Přesune Vás o adresář výše, v případě zadání čísla Vás posune o tolik adresářů výše, kolik je dané číslo, příklady parametrů ->
     - up |-> posune Vás o jeden adresář výše
     - up 6 |-> posune Vás o 6 adresářů výše
   - Pokud zadáte číslo menší jak 1, tak se zobrazí chyba.
   - Pokud zadáte číslo větší, než kolikrát je možné jít výše, tak se program pokusí jít co nejvýše.
   - Pokud zadáte něco jiného nežli číslo, tak se zobrazí chyba.
 - [bold blue]next [číslo (tento parametr je volitelný)][/bold blue]
   - Pokud je více stran k zobrazení všech položek v aktuální lokaci, tak se můžete díky tomuto příkazu posunout na další stranu (+1), či o více stran podle čísla, které zadáte, příklady parametrů ->
     - next |-> posune Vás na další stranu (+1)
     - next 6 |-> posune Vás o 6 stran od aktuální strany (+6)
   - Pokud zadáte číslo menší jak 1, tak program ohlásí chybu
   - Pokud zadáte povel na přechod na stranu neexistující, tak se program pokusí k ní dostat co nejblíže a ohlásí chybu.
 - [bold blue]previous [číslo (tento parametr je volitelný)][/bold blue]
   - Pokud je více stran k zobrazení všech položek v aktuální lokaci, tak se můžete díky tomuto příkazu posunout na předchozí stranu (-1), či o více stran podle čísla, které zadáte, příklady parametrů ->
     - previous |-> posune Vás na předchozí stranu (-1)
     - previous 6 |-> posune Vás o 6 stran zpět od aktuální strany (-6)
   - Pokud zadáte číslo menší jak 1, tak program ohlásí chybu
   - Pokud zadáte povel na přechod na stranu neexistující, tak program se program pokusí k ní dostat co nejblíže a ohlásí chybu.
 - [bold blue]remove[/bold blue]
   - Smaže aktuální označené položky - soubory, složky i soubory a složky vnořené.
   - Pro smazání položek je nutné potvrzení.
   - Zjistí počet úspěšných a chybných odstranění a vypíše informace o výsledku příkazu.
 - [bold blue]copy[/bold blue]
   - Zkopíruje označené položky do aktuálního adresáře - soubory, složky i soubory a složky vnořené.
   - Zjistí počet úspěšných a chybných kopírovaní a vypíše informace o výsledku příkazu.
 - [bold blue]move[/bold blue]
   - Přesune označené položky do aktuálního adresáře - soubory, složky i soubory a složky vnořené.
   - Zjistí počet úspěšných a chybných přesunutí a vypíše informace o výsledku příkazu.
 - [bold blue]makedir !název (povinný parametr)![/bold blue]
   - Vytvoří v aktuálním adresáři nový adresář se zadaným názvem od uživatele, příklady parametrů ->
     - makedir NewFolder |-> vytvoří v aktuálním adresáři nový adresář s názvem NewFolder
   - Vypíše informace o výsledku provedení příkazu.
 - [bold blue]rename !nový_název (povinný parametr)! [!kde začátek_počítadla změna_počítadla minimální_počet_míst přípona_nebo_koncovka (polopovinné parametry)!][/bold blue]
   - Přejmenuje vybraný soubor či složku, nebo vybrané soubory či složky. Přejmenovává položky v seznamu poznačených.
   - Pokud je pouze jedna položka k přejmenování je povinný parametr pouze nový_název, jinak jsou povinné i další parametry.
   - nový_název - jedna část názvu, kde - after/before - pozice počítadla před či za novým_názvem, začátek_počítadla - startovní index
   - změna_počítadla - o jaké číslo se bude počítadlo pravidelně měnit, minimální_počet_míst - minimální počet míst počítadla, přípona_nebo_koncovka - název připojený ke konci nového názvu
   - Zjistí počet chybných a úspěšných přejmenování a vypíše výsledek příkazu a zda nedošlo k chybě, príklady parametrů ->
     - rename ahoj.txt |-> pokud pouze jeden soubor je vybrán tak bude přejmenován na název ahoj.txt
     - rename obrazek after 0 1 4 .jpg |-> všechny položky které jsou poznačené budou přejmenovány takto - obrazek0000.jpg, obrazek0001.jpg, ..........
 - [bold blue]copyrename !nový_název (povinný parametr)! [!kde začátek_počítadla změna_počítadla minimální_počet_míst přípona_nebo_koncovka (polopovinné parametry)!][/bold blue]
   - Zkopíruje a přejmenuje vybraný soubor či složku, nebo vybrané soubory či složky. Kopíruje a přejmenovává položky v seznamu poznačených do aktuálního adresáře.
   - Pokud je pouze jedna položka ke kopírování a přejmenování je povinný parametr pouze nový_název, jinak jsou povinné i další parametry.
   - nový_název - jedna část názvu, kde - after/before - pozice počítadla před či za novým_názvem, začátek_počítadla - startovní index
   - změna_počítadla - o jaké číslo se bude počítadlo pravidelně měnit, minimální_počet_míst - minimální počet míst počítadla, přípona_nebo_koncovka - název připojený ke konci nového názvu
   - Zjistí počet chybných a úspěšných kopírování a přejmenování a vypíše výsledek příkazu a zda nedošlo k chybě, príklady parametrů ->
     - copyrename ahoj.txt |-> pokud pouze jeden soubor je vybrán tak bude kopírován do aktuálního adresáře a přejmenován na název ahoj.txt
     - copyrename obrazek after 0 1 4 .jpg |-> všechny položky které jsou poznačené budou zkopírovány do aktuálního adresáře a přejmenovány takto - obrazek0000.jpg, obrazek0001.jpg, ..........
 - [bold blue]search !hledaný_výraz (povinný parametr)![/bold blue]
   - Vyhledá soubory či složky obsahující hledaný_výraz v aktuálním umístění a v jeho podadresářích
   - Průběžně informuje o vyhledávání, má kontrolu vstupu uživatele. Jako výsledek zobrazí seznam nalezených položek, příklady parametrů ->
   - search .txt |-> vyhledá všechny soubory v aktuálním adresáři a i v podadresářích obsahující .txt.
 - [bold blue]dirsize !číslo (povinný parametr)![/bold blue]
   - Zjistí a vypíše velikost zadané složky, příklady parametrů ->
     - dirsize 6  |-> zjistí a vypíše velikost adresáře na indexu číslo 6.
 - [bold blue]sort !dle_čeho_má_řadit vzestupně_sestupně (povinný parametr)![/bold blue]
   - Nastaví jakým způsobem se řadí a zobrazují zobrazené položky
   - dle_čeho_se_má_řadit - řazení dle jména - name, výchozí zobrazení - none, dle velikosti - size, dle času založení - created, dle času poslední úpravy - changed
   - vzestupně_sestupně - vzestupně - up, sestupně - down, příklady parametrů ->
     - sort name down - seřadí sestupně dle jmen. 
 - [bold blue]locales[/bold blue]
   - Zobrazí seznam všech dostupných vestavěných lokalizací a pokud máte povolené ukládání konfigurací, tak i všech dodatkových lokalizací.
   - Dodatkové lokalizace se mohou vložit do adresáře %APPDATA%(Roaming)/Leek/locales/ a to ve formátu jednotlivých dodatečných jazyků uložených
   - jako python dictionary ve tvaru {"locale_name" : {locale keys and data}} v souboru s názvem locale_name a příponou .llf - en.llf
   - Program nekontroluje správnost tvaru dodatkových lokalizací !!!!!!
   - Pro více informací navštivte projektové stránky programu.
 - [bold blue]locale !locale_name (povinný parametr)![/bold blue]
   - Změní lokalizaci programu do uvedeného jazyka, příklady parametrů ->
     - locale en |-> změní lokalizaci do jazyka se zkratkou en
   - V případě chybného zavolání, nebo zadání neexistující jazyka vypíše chybu.
- [bold blue]saveconfig !setting (povinný parametr)![/bold blue]
   - Nastaví zda se může ukládat nastavení programu pro použití při příštím startu, zapnutí zároveň umožňuje používat dodatečné lokalizace.
   - setting - true/false, program vždy ukládá nastavení při zavření pomocí příkazu exit, příklady parametrů ->
     - saveconfig true |-> nastavení se budou ukládat, dodatečné lokalizace jsou povoleny
   - V případě špatného vstupu funkce vypíše chybové hlášení.
- [bold blue]sizeunit !new_unit (povinný parametr)![/bold blue]
   - Nastaví jednotku velikosti dat v rámci celého programu
   - new_unit - B/KB/MB/GB/TB, příklady parametrů ->
     - sizeunit KB |-> nastaví jednotku zobrazování velikosti dat na KB
   - Jakýkoli jiný vstup něžli B/KB/MB/GB/TB je považován za chybu.
   - V případě zadání špatných parametrů funkce vypíše chybové hlášení.   
            ''',
        'app_help_leek_title' : 'Vítejte v podpoře programu Leek (no leak)',
        'app_help_command_list_leek_title' : 'Seznam příkazů a vysvětlení',
        'app_help_basic_title' : 'Základní informace',
        '' : '',
        '' : '',
        '' : '',
        '' : '',
        },
    'en' : {
        # error messages
        'no_input' : '[bold red]You gave no input[/bold red]',
        'select_bad_input' : '[bold red]Bad input given for command select[/bold red]',
        'unknown_command' : '[bold red]You gave wrong or unknown command[/bold red]',
        'open_bad_input' : '[bold red]Bad input given for command open[/bold red]',
        'file_does_not_exist' : '[bold red]File or folder doesn\'t exist[/bold red]',
        'permission_error' : '[bold red]You have insufficient permissions for this operation[/bold red]',
        'up_bad_input' : '[bold red]Bad input given for command up[/bold red]',
        'drive_does_not_exist' : '[bold red]The drive you choose is nonexistent[/bold red]',
        'drive_bad_input' : '[bold red]Bad input given for command drive[/bold red]',
        'no_drive_no_root' : '[bold red]No drive selected, so you can\'t get to it\'s root[/bold red]',
        'no_select_in_roots' : '[bold red]Roots of drives can\'t be selected[/bold red]',
        'no_add_in_roots' : '[bold red]Roots of drives can\'t be added to the selected list[/bold red]',
        'open_nonexistent' : '[bold red]Cannot open file or folder on a nonexistent index[/bold red]',
        'invalid_index_of_select' : '[bold red]You gave wrong IDs with your last command, these IDs will be ignored[/bold red]',
        'no_select_in_select' : '[bold red]Selected items can\'t be reselected[/bold red]',
        'rows_bad_input' : '[bold redBad input given for command rows[/bold red]',
        'next_bad_input' : '[bold red]Bad input given for command next[/bold red]',
        'previous_bad_input' : '[bold red]Bad input given for command previous[/bold red]',
        'nowhere_to_go_next' : '[bold red]There is no futher page to open[/bold red]',
        'nowhere_to_go_previous' : '[bold red]There is no previous page to open[/bold red]',
        'no_up_in_root' : '[bold red]We are in root, only sky is above us[/bold red]',
        'up_bad_input' : '[bold red]Bad input given for command up[/bold red]',
        'dirsize_nonexistent' : '[bold red]You gave a nonexistent index when you last called command dirsize[/bold red]',
        'file_or_does_not_exist_dir_in_dirsize' : '[bold red]Size of the specified folder or file cannot be estimated[/bold red]',
        'dirsize_bad_input' : '[bold red]Bad input given for command dirsize[/bold red]',
        'remove_nothing_to_remove' : '[bold red]Nothing left to remove[/bold red]',
        'copy_nothing_to_copy' : '[bold red]No items were selected for copy[/bold red]',
        'copy_no_copy_in_select' : '[bold red]You cannot copy into the selected list[/bold red]',
        'copy_no_copy_in_root' : '[bold red]Cannot copy into root of the file system[/bold red]',
        'move_nothing_to_move' : '[bold red]There are no items selected to be moved[/bold red]',
        'move_no_move_in_select' : '[bold red]You cannot move into the selected list[/bold red]',
        'move_no_move_in_root' : '[bold red]Cannot copy into root of the file system[/bold red]',
        'make_dir_no_root' : '[bold red]You can\'t make a new direcotory in the root of the file system[/bold red]',
        'make_dir_no_select' : '[bold red]New directory can\'t be created in the selected list[/bold red]',
        'make_dir_bad_input' : '[bold red]Bad input given for command makedir[/bold red]',
        'make_dir_failed' : '[bold red]Unable to create a new directory[/bold red]',
        'rename_bad_input' : '[bold red]Bad input given for command rename[/bold red]',
        'rename_more_select_no_advanced' : '[bold red]There are multiple items to be renamed, but you haven\'t inserted additional parametres for command rename.[/bold red]',
        'rename_advanced_but_one' : '[bold red]You have inserted additional parametres for command rename, but there is only one item to be renamed.[/bold red]',
        'rename_nothing_to_rename' : '[bold red]No items were selected to be renamed.[/bold red]',
        'copyrename_no_copy_in_select' : '[bold red]You can\'t copy-rename into the selected list[/bold red]',
        'copyrename_no_copy_in_root' : '[bold red]You can\'t copy-rename into the root of the file system.[/bold red]',
        'copyrename_bad_input' : '[bold red]Bad input given for command copyrename[/bold red]',
        'copyrename_more_select_no_advanced' : '[bold red]There are multiple items to be copy-renamed, but you haven\'t inserted additional parametres for command copyrename.[/bold red]',
        'copyrename_advanced_but_one' : '[bold red]You have inserted additional parametres for command copyrename, but there is only one item to be copy-renamed.[/bold red]',
        'copyrename_nothing_to_copyrename' : '[bold red]No items were selected to be copy-renamed.[/bold red]',
        'search_bad_input' : '[bold red]Bad input given for command search[/bold red]',
        'move_no_move_in_search' : '[bold red]You can\'t use move command in searched list.[/bold red]',
        'copyrename_no_copy_in_search' : '[bold red]You can\'t use copyrename command in searched list.[/bold red]',
        'copy_no_copy_in_search' : '[bold red]You can\'t use copy command in searched list.[/bold red]',
        'make_dir_no_search' : '[bold red]It isn\'t possible to create a new folder in searched list.[/bold red]',
        'locale_bad_input' : '[bold red]Bad input given for command locale, or you have inserted an unsupported localization.[/bold red]',
        'saveconfig_bad_input' : '[bold red]Bad input given for command saveconfig.[/bold red]',
        'sizeunit_bad_input' : '[bold red]Bad input given for command sizeunit.[/bold red]',
        '' : '',
        '' : '',
        '' : '',
        '' : '',
        # succes messages
        'select_success' : '[bold green]Files and folders were successfuly selected.[/bold green]',
        'open_dir_success' : '[bold green]The specified folder was opened.[/bold green]',
        'open_file_success' : '[bold green]The specified file was opened in external application.[/bold green]',
        'refreshed' : '[bold green]Interface was refreshed.[/bold green]',
        'up_success' : '[bold green]We are in the parent folder.[/bold green]',
        'root_success' : '[bold green]We are in the root of the drive.[/bold green]',
        'roots_success' : '[bold green]We are in the root of the file system.[/bold green]',
        'drive_success' : '[bold green]The specified drive is shown.[/bold green]',
        'add_success' : '[bold green]Files and folders were successfuly added to the selected list.[/bold green]',
        'showselect_success' : '[bold green]The list of selected files and folders is shown.[/bold green]',
        'unselect_success' : '[bold green]The specified selects were unselected.[/bold green]',
        'rows_success' : '[bold green]The maximum number of rows in the table successfuly changed.[/bold green]',
        'next_success' : '[bold green]The specified next page is shown.[/bold green]',
        'previous_success' : '[bold green]The specified previous page is shown.[/bold green]',
        'dirsize_success' : '[bold green]The size of the folder at index [/bold green][bold blue]{}[/bold blue][bold green] is [/bold green][bold blue]{}[/bold blue][bold green] {}[/bold green]',
        'remove_successful' : '[bold blue]{}[/bold blue][bold green] items were successfuly removed and [/bold green][bold red]{}[/bold red][bold green] failed to remove.\nThe selected list is empty now.[/bold green]',
        'remove_abort' : '[bold green]Delete operation aborted.[/bold green]',
        'copy_successful' : '[bold blue]{}[/bold blue][bold green] items were successfuly copied and [bold red]{}[/bold red][bold green] failed to copy.[/bold green]',
        'make_dir_successful' : '[bold green]New folder was successfuly created[/bold green]',
        'rename_successful' : '[bold blue]{}[/bold blue][bold green] items were successfuly renamed and [/bold green][bold red]{}[/bold red][bold green] items failed to rename.[/bold green]',
        'copyrename_successful' : '[bold blue]{}[/bold blue][bold green] items were successfuly copy-renamed and [/bold green][bold red]{}[/bold red][bold green] items failed to rename.[/bold green]',
        'search_successful' : '[bold green]Search reults are shown.[/bold green]',
        'locale_successful' : '[bold green]Localization was successfuly changed.[/bold green]',
        'available_localization_loaded' : '[bold blue]Available localizations were successfuly loaded.[/bold blue]',
        'cannot_load_localization' : '[bold red]Available additional localizations failed to load.[/bold red]',
        'saveconfig_successful' : '[bold green]The option whether to save configuration was successfuly changed.[/bold green]',
        'sizeunit_successful' : '[bold green]The units of size were successfuly changed.[/bold green]',
        '' : '',
        '' : '',
        '' : '',
        '' : '',
        # other general
        'insert_cmd' : '[bold]Insert command [/bold](help)',
        'bye_message' : '[bold blue]See you next time!![/bold blue]',
        'remove_item_message' : '[bold red]Item - {} will be deleted.[/bold red]',
        'remove_confirm' : '[bold red]Do you really wish to delete {} items??[/bold red]',
        'item_removed' : '[bold green]Item - [/bold green][bold blue]{}[/bold blue][bold green] was successfuly deleted.[/bold green]',
        'unable_to_remove_item' : '[bold red]Item - {} can\'t be deleted.[/bold red]',
        'nonexistent_path' : '[bold red]The specified path is nonexistent - {}[/bold red]',
        'press_enter_to_hide' : 'Press enter to hide this panel:',
        'unable_to_copy_item' : '[bold red]Item - {} can\'t be copied to location - {}[/bold red]',
        'item_copied' : '[bold green]Item - [/bold green][bold blue]{}[/bold blue][bold green] - was successfuly copied to location - [/bold green][bold blue]{}[/bold blue]',
        'copy_folder_already_exists' : '[bold red]Folder - {} already exists in location - {} , unable to copy.[/bold red]',
        'copy_item_already_exists' : '[bold red]File - {} already exists in location - {} , unable to copy.[/bold red]',
        'unable_to_move' : '[bold red]Unable to move item - {} to location - {}[/bold red]',
        'item_moved' : '[bold green]Item successfuly moved - [/bold green][bold blue]{}[/bold blue][bold green] - to location - [/bold green][bold blue]{}[/bold blue]',
        'unable_to_rename' : '[bold red]Item - {} can\'t be renamed to - {}[/bold red]',
        'item_renamed' : '[bold green]Item - [/bold green][bold blue]{}[/bold blue][bold green] - was successfuly renamed to - [/bold green][bold blue]{}[/bold blue]',
        'unable_to_copyrename_item' : '[bold red]Unable to copy item - {} to location - {} and rename it to - {}[/bold red]',
        'item_copyrenamed' : '[bold green]Item - [/bold green][bold blue]{}[/bold blue][bold green] - was successfuly copy-renamed to - [/bold green][bold blue]{}[/bold blue]',
        'searching_in' : ' [bold green]We search in - [/bold green][bold blue]{}[/bold blue][bold green] - If you want to exit, please close the application.[/bold green]',
        'rights' : 'Rights',
        'modified' : 'Modified',
        'created' : 'Created',
        'size' : 'Size in {}',
        'file_or_folder_name' : 'File or folder name',
        'id' : 'ID',
        'none_up' : '[bold yellow]Viewed items sorted without any criteria in ascending order.[/bold yellow]',
        'none_down' : '[bold yellow]Viewed items sorted without any criteria in descending order.[/bold yellow]',
        'name_up' : '[bold yellow]Viewed items sorted by name in ascending order.[/bold yellow]',
        'name_down' : '[bold yellow]Viewed items sorted by name in descending order.[/bold yellow]',
        'created_up' : '[bold yellow]Viewed items sorted by creation time in ascending order.[/bold yellow]',
        'created_down' : '[bold yellow]Viewed items sorted by creation time in descending order.[/bold yellow]',
        'size_up' : '[bold yellow]Viewed items sorted by size in ascending order.[/bold yellow]',
        'size_down' : '[bold yellow]Viewed items sorted by size in descending order.[/bold yellow]',
        'changed_up' : '[bold yellow]Viewed items sorted by last change time in ascending order.[/bold yellow]',
        'changed_down' : '[bold yellow]Viewed items sorted by last change time in descending order.[/bold yellow]',
        'list_info' : '[bold blue]Page {} of {}. There are {} files/folders/drives. Visible {}.[/bold blue]',
        'cannot_load' : '[bold blue]Unable to load application configuration, if you wish to save the configuration use command [/bold blue]saveconfig true',
        'load_successful' : '[bold blue]Configuration was successfuly loaded[/bold blue]',
        'cannot_save' : '[bold red]Unable to save the application configuration[/bold red]',
        'save_successful' : '[bold blue]Configuration was successfuly saved[/bold blue]',
        'not_saving' : '[bold blue]Configuration won\'t be saved[/bold blue]',
        'print_locales' : '[bold green]Available languages are : {}\nIf you wish to add more languages follow the steps in wiki on the github page of the program\nIf you wish to use additional languages you must have configuration saving turned on.',
        '' : '',
        '' : '',
        '' : '',
        '' : '',
        '' : '',
        '' : '',
        '' : '',
        'app_info' : 
            '''
[bold green]----------------------------------------------------------------[/bold green]
[bold blue]Leek - the file manager[/bold blue]
[bold green]----------------------------------------------------------------[/bold green]
[bold cyan]version: [/bold cyan][bold white]{}[/bold white]
[bold magenta]author: [/bold magenta][bold white]{}[/bold white]
[bold green]date: [/bold green][bold white]{}[/bold white]
[bold green]----------------------------------------------------------------[/bold green]
[bold magenta]Project webpage: [/bold magenta][bold blue]{}[/bold blue]
[bold yellow]Github webpage: [/bold yellow][bold green]{}[/bold green]
[bold red]This program uses Python {} and Rich {}[/bold red]
[bold magenta]Exe packaging provided by Pyinstaller {}[/bold magenta]
[bold blue]Exe file compression provided by UPX {}[/bold blue]
[bold green]ZIP archive compression provided by 7-zip {}[/bold green]
[bold blue]Many thanks to everybody, whose work I use in this project :smiley:[/bold blue]
[bold magenta]If you have a feature idea or request or you
have found any bugs please visit the github page of the
project and share your thoughts.[/bold magenta]
[bold green]----------------------------------------------------------------[/bold green]
            ''',
        'app_info_leek_title' : 'Leek information',
        'app_help_part_one' : 
            '''
Leek is a simple console file manager controled by short entered commands. As every other file manager it can view files, folders and basic information about them. Everything is viewed on table pages that have a changeable row size. You can also list through these pages. You manipulate with the files, folders and drives by their shown ID. Leek has a moderate subset of features commands that will allow you to copy, move, remove, rename, show and open the files and folders. Other features include direcotory creation, searching, sorting, simple configuration, an extensive built-in help and many other. In order to use most of these features and functions you need to select the files and folders you want to operate with. Leek uses Python and a Rich library for the console outputs, the target operating system is Windows. The minimial OS version is Windows 8 64 bit.
            ''',
        'app_help_part_two' : 
            '''
 - [bold blue]select [number/numbers separated by a space/range (optional parameter)][/bold blue]
   - Unselects currently selected and selects the desired items, IDs of the items in current location are used for the selection, possible input -> 
     - select |-> with no parametres specified all the items in current directory will be selected
     - select 1 |-> item with ID 1 will be selected
     - select 1 2 3 7 8 9 |-> items with shown IDs will be selected
     - select 1 - 15 |-> items in the given range of IDs will be selected
   - All duplicit IDs and records are ignored, faulty or nonexistent selection will raise an error.
 - [bold blue]add [number/numbers separated by a space/range (optional parameter)][/bold blue]
   - Adds the specified items by their respective IDs in current directory to the selection list, possible input ->
     - add |-> with no parametres specified all the items in current directory will be added to the selection list
     - add 1 |-> item with ID 1 will be added to the selection list
     - add 1 2 3 7 8 9 |-> items with the given IDs will be added to the selection list
     - add 1 - 15 |-> all the items in the given range of IDs will be added to the selection list
   - All duplicit IDs and records are ignored, faulty or nonexistent selection will raise an error.
 - [bold blue]showselect[/bold blue]
   - Shows the selected list.
 - [bold blue]unselect [number/numbers separated by a space/range (optional parameter)][/bold blue]
   -  Unselects the specified items by their respective IDs in the selection list from the selection list (To show these IDs please use command showselect), possible input ->
     - unselect |-> all the items in the selection list wil be unselected
     - unselect 1 |-> item with ID 1 in the selection list will be unselected
     - unselect 1 2 3 7 8 9 |-> items with the specified IDs from the selection list will be unselected 
     - unselect 1 - 15 |-> items in the given range of IDs will be unselected from the selection list
   - All duplicit IDs and records are ignored, faulty or nonexistent selection will raise an error.
 - [bold blue]root[/bold blue]
   - Shows the root of the current drive.
 - [bold blue]roots[/bold blue]
   - Shows the root of the file system.
 - [bold blue]help[/bold blue]
   - Shows the help of the program. Well I hope you know how you got here, don\'t you ?
 - [bold blue]refresh[/bold blue]
   - Refreshes the available drives and mainly refreshes the viewed table, pressing only enter has the same effect.
 - [bold blue]exit[/bold blue]
   - Exits the program and saves (if configured to save) the configuration.
 - [bold blue]info[/bold blue]
   - Information about the program will be shown.
 - [bold blue]rows !number (compulsory parameter)![/bold blue]
   - Sets the number of rows of the viewing table to the number specified in the parameter, possible input -> 
     - rows 20 |-> number of rows of the viewing table will be set to 20
   - Minimal ammount of rows is 10, if you input a lower number or input something different alltogether an error will be raised.
 - [bold blue]open !number (compulsory parameter)![/bold blue]
   - Opens the file or directory with the given ID (specified by the parameter) in the curent directory, possible input ->
     - open 4 |-> opens the item with ID 4 in the current folder
   - If the selected item is a file, it will be opend in the default system application for such file.
   - If the selected item is a folder, you will be redirected to it within leek.
   - If you input a faulty ID or some other error takes place, an error will be raised.
 - [bold blue]drive !drive letter (compulsory parameter)![/bold blue]
   - A drive with the specified letter will be opened within leek, possible input ->
     - drive f |-> drive F:\\\\ will be opened within leek
   - An error will be raised if you input something different than a valid drive letter.
 - [bold blue]up [number (optional parameter)][/bold blue]
   - You will be redirected to the parental folder, optional number will specify the count of jumps to parental folder the program will go, possible input ->
     - up |-> you will be redirected to the parental folder
     - up 6 |-> you will be redirected to the sixth parental folder from your current position
   - Inserted number smaller than 1 will result in an error.
   - Inserted number larger than the ammount of possible jumps to the parental folders will position you to the root of the file system.
   - An error will be raised if the optional parameter is something else than a number.
 - [bold blue]next [number (optional parameter)][/bold blue]
   - If there are multiple pages with items of the current folder, then you can use this command to flip to the next (+1) page or to a page in positive direction with an index of the current page + number, possible input ->
     - next |-> you will flip to the next page (+1).
     - next 6 |-> you will list through to the sixth page from the current one (+6).
   - An error will be raised, if the inputed optional number is smaller than 1.
   - If you try to list to a nonexistent page, the program will try to get as close to it in the positive direction and raises an error.
 - [bold blue]previous [number (optional parameter)][/bold blue]
   - If there are multiple pages with items of the current folder, then you can use this command to flip to the previous (-1) page or to a page in negative direction with an index of the current page - number, possible input ->
     - previous |-> you will flip to the previous page (-1).
     - previous 6 |-> you will list through to the sixth page from the current one (-6).
   - An error will be raised, if the inputed optional number is smaller than 1.
   - If you try to list to a nonexistent page, the program will try to get as close to it in the negative direction and raises an error.
 - [bold blue]remove[/bold blue]
   - All of the selected items - files, folders and subfiles and subfolders will be deleted. 
   - A confirmation is required to continue.
   - When the work is done it outputs the stats of how many deletions were successful or failed.
 - [bold blue]copy[/bold blue]
   - All of the selected items - files, folders and subfiles and subforlders will be copied to the current folder.
   - When the work is done it outputs the stats of how many copy actions were successful or failed.
 - [bold blue]move[/bold blue]
   - All of the selected items - files, folders and subfiles and subfolders will be moved to the current directory.
   - When the work is done it outputs the stats of how many move actions were successful or failed.
 - [bold blue]makedir !FolderName (compulsory parameter)![/bold blue]
   - Creates a new folder with the given name in the current directory, possible input ->
     - makedir NewFolder |-> creates a new folder with name NewFolder in the current directory
   - When the work is done it informs the user about the result of the command.
 - [bold blue]rename !new_name (compulsory parameter)! [!where counter_begin counter_increment minimal_number_of_digits extension (partly compulsory)!][/bold blue]
   - Renames the selected file or folder, or the selected files or folders. 
   - Use only one parameter if there is only one item to be renamed, otherwise you have to input the other parametres as well.
   - new_name - main part of the name or write |none| to leave it empty (or the new_name if there is only one item to be renamed), where - after/before - where to position the counter relative to new_name.
   - counter_begin - the number to start the counter with, counter_increment - the number that will be added to the counter with each item, minimal_number_of_digits - the minimal number of digits to be always shown, use 0 if you want the number to fit the counter.
   - extension - the ending part of the name of the file or the extension of the file, |none| - no extension, |base| - the current extension will be reused.
   - It prints out the information about what is being changed to what and when the work is done it informs about the result of the command, possible input ->
     - rename hi.txt |-> only one file to be renamed - it will be renamed to the specified name
     - rename picture after 0 1 4 |base| |-> all the selected items will be renamed like this nice_wall.jpg -> picture0001.jpg, nice_wall_2.png -> picture0002.png, ......
 - [bold blue]copyrename !nový_název (compulsory parameter)! [!kde začátek_počítadla změna_počítadla minimální_počet_míst přípona_nebo_koncovka (polopovinné parametry)!][/bold blue]
   - Copy-renames the selected file or folder, or the selected files or folders to the current directory. 
   - Use only one parameter if there is only one item to be copy-renamed, otherwise you have to input the other parametres as well.
   - new_name - main part of the name or write |none| to leave it empty (or the new_name if there is only one item to be copy-renamed), where - after/before - where to position the counter relative to new_name.
   - counter_begin - the number to start the counter with, counter_increment - the number that will be added to the counter with each item, minimal_number_of_digits - the minimal number of digits to be always shown, use 0 if you want the number to fit the counter.
   - extension - the ending part of the name of the file or the extension of the file, |none| - no extension, |base| - the current extension will be reused.
   - It prints out the information about what is being changed to what and when the work is done it informs about the result of the command, possible input ->
     - copyrename hi.txt |-> only one file to be copy-renamed - it will be copied to the current directory and renamed to the specified name
     - copyrename picture after 0 1 4 |base| |-> all the selected items will be copy-renamed like this nice_wall.jpg -> picture0001.jpg, nice_wall_2.png -> picture0002.png, ...... 
 - [bold blue]search !searched_term (compulsory parameter)![/bold blue]
   - Searches for items - files and folders with the searched term in their name in the current directory and subdirectories.
   - It regurarly informs about the search, you can\'t stop the command while it\'s processing, you have to close the program, possible input ->
   - search .txt |-> searches for files and folders in the current directory and it\'s subdirectories with term .txt in it\'s name
 - [bold blue]dirsize !number (compulsory parameter)![/bold blue]
   - Prints out the size of the specified folder (folder with the given ID), possible input ->
     - dirsize 6  |-> prints the size of the folder with ID 6
   - It raises an error in case of bad input or bad ID or prints a success message.
 - [bold blue]sort !sort_by asc_desc (compulsory parameter)![/bold blue]
   - Sets in which order the items are viewed.
   - sort_by - by name - name, by nothing - none, by size - size, by time of creation - created, by time of last change - changed
   - asc_desc - ascending - up, descending - down, possible input ->
     - sort name down - sorts by name in descending order 
 - [bold blue]locales[/bold blue]
   - Prints a list of all builtin localizations as well as installed additional ones if the saveconfig is set to true.
   - Additional localizations can be install to directory %APPDATA%(Roaming)/Leek/locales/. For each additional locale the format is
   - a text version of python dictionary in this format {"locale_name" : {locale keys and data}} in a file with name locale_name and extension .llf - en.llf
   - The correct format of the installed additional localizations is not checked !!!!!!
   - Please visit the project webpage for more information.
 - [bold blue]locale !locale_name (compulsory parameter)![/bold blue]
   - Application localization (language) will be changed to the selected language, possible input ->
     - locale en |-> localization will be changed to a language with shortcut en
   - The application raises an error in case of faulty input or when the specified locale is not supported (view locales), otherwise it informs about success.
- [bold blue]saveconfig !setting (compulsory parameter)![/bold blue]
   - Sets whether the application is alowed to save configuration for future use, if its turned on you can also use the additional localizations.
   - setting - true/false, configuration is always saved upon exit, possible input ->
     - saveconfig true |-> configuration will be saved from now on when you exit the application, additional localizations are alowed.
   - Confirutation is saved upon using command exit and when closing the window.
   - The program raises an error in case of bad input, it also outputs stats message.
- [bold blue]sizeunit !new_unit (compulsory parameter)![/bold blue]
   - Sets the unit of size for the scope of the whole application
   - new_unit - B/KB/MB/GB/TB, possible input ->
     - sizeunit KB |-> sets the unit of size to KB
   - Any other input than B/KB/MB/GB/TB will be ignored and considered as an error.
   - The command outputs error or success messgage depending on the result.
            ''',
        'app_help_leek_title' : 'Welcome, this is the support page of leek (no leak)',
        'app_help_command_list_leek_title' : 'List of commands and their description',
        'app_help_basic_title' : 'General information',
        '' : '',
        '' : '',
        '' : '',
        '' : '',
        }
    }