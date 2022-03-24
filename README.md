# leek
Leek (pórek) je jednoduchý konzolový správce souborů ovládaný krátkými příkazy, jakožto každý správce souborů umí zobrazovat soubory, složky a základní informace o nich, veškeré zobrazování se děje na tabulkových listech, jejichž velikost si můžete sami upravit. Zároveň můžete volně mezi těmito listy přecházet. Soubory, disky a složky voláte dle jejich zobrazovaného ID. Leek je schopen volně přecházet mezi disky, vracet se zpět na root disku i na root celku. Zobrazení můžete kdykoli aktualizovat. Součástí leek je i jednoduché sledování chyb a úspěšných operací, které uživateli umožní se jednoduše vyznat ve výsledcích zadaných příkazů. V leeku si můžete poznačovat soubory pro budoucí práci s nimi, soubory poznačené si také můžete nechat zobrazit, nebo je odoznačovat. Leek samozřejmě umí soubory a složky přesouvat," přejmenovávat, kopírovat, kopírovat a přejmenovávat, mazat, vyhledávat v nich a zobrazení různě seřazovat. Leek využívá Python verze 3.10 a knihovnu rich 11.2, minimální verzí operačního systému Windows je Win 8.

   - select [číslo/čísla oddělená mezerou/rozsah (tento parametr je volitelný)]
   - - Odoznačí aktuální poznačené a poznačí si výběr, k označení se používá ID položek v aktuální lokaci, příklady parametrů ->
   - - - select |-> bez parametru označí všechny položky v aktualním adresáři
   - - - select 1 |-> označí položku s ID 1
   - - - select 1 2 3 7 8 9 |-> označí položky s napsanými ID
   - - - select 1 - 15 |-> označí položky z daného rozsahu
   - - Veškeré duplicitní záznamy se ignorují, chybné a neexistující výběry zobrazí chybu.
   
   - add [číslo/čísla oddělená mezerou/rozsah (tento parametr je volitelný)]
   - - Přidá k označeným vybrané, k označení se používá ID položek v aktuální lokaci, příklady parametrů -> 
   - - - add |-> bez parametru přidá k označeným všechny položky v aktuálním adresáři
   - - - add 1 |-> přidá k označeným položku s ID 1
   - - - add 1 2 3 7 8 9 |-> přidá k označeným položky s napsanými ID
   - - - add 1 - 15 |-> přidá k označeným položky z daného rozsahu
   - - Veškeré duplicitní záznamy se ignorují, chybné a neexistující výběry zobrazí chybu.
   
   - showselect[/bold blue]
   - - Zobrazí seznam označených
   
   - unselect [číslo/čísla oddělená mezerou/rozsah (tento parametr je volitelný)]
   - - Odoznačí aktuální poznačené podle zadaného výběru, k odoznačení se používá ID položek v seznamu označených (zobrazte si je pomocí showselect), příklady parametrů ->
   - - - unselect |-> bez parametru odoznačí všechno označené v seznamu označených
   - - - unselect 1 |-> odoznačí položku s ID 1 v seznamu označených
   - - - unselect 1 2 3 7 8 9 |-> odoznačí položky s napsanými ID v seznamu označených
   - - - unselect 1 - 15 |-> odoznačí položky z daného rozsahu v seznamu označených
   - - Veškeré duplicitní záznamy se ignorují, chybné a neexistující výběry zobrazí chybu.
   
   - root - - zobrazí kořen aktuálního adresáře\n - [bold blue]roots[/bold blue]
   - - zobrazí kořeny adresářů
   
   - help
   - - zobrazí pomoc
   
   - refresh
   - - přenačte zobrazení a disky
   
   - exit
   - - ukončí program
   
   - info
   - - zobrazí informace o programu
   
   - rows !číslo (povinný parametr)!
   - - Nastaví počet řádků tabulky na číslo zadané v parametru, příklady parametrů ->
   - - - rows 20 |-> nastaví počet řádků na 20
   - - Minimum řádků je 10, jakékoli menší číslo vyústí v chybu
   
   - open !číslo (povinný parametr)!
   - - Otevře soubor či složku na daném iD v aktuální lokaci, příklady parametrů ->
   - - - open 4 |-> otevře položku na ID 4 v aktuální lokaci
   - - Pokud se jedná o soubor, tak bude otevřen ve výchozí aplikaci systému
   - - Pokud jde o složku, tak do ní budete přesunuti
   
   - drive !znak disku (povinný parametr)!
   - - Otevře disk daný znakem disku, příklady parametrů ->
   - - - drive f |-> otevře disk F:\\\\
   - - Pokud zadáte něco jiného, než platný znak disku, tak to bude považováno za chybu
   
   - up [číslo (tento parametr je volitelný)]
   - - Přesune Vás o adresář výše, v případě zadání čísla Vás posune o tolik adresářů výše, kolik je dané číslo, příklady parametrů ->
   - - - up |-> posune Vás o jeden adresář výše
   - - - up 6 |-> posune Vás o 6 adresářů výše
   - - Pokud zadáte číslo menší jak 1, tak se zobrazí chyba
   - - Pokud zadáte číslo větší, než kolikrát je možné jít výše, tak se program pokusí jít co nejvýše
   
   - next [číslo (tento parametr je volitelný)]
   - - Pokud je více stran k zobrazení všech položek v aktuální lokaci, tak se můžete díky tomuto příkazu posunout na další stranu, či o více stran podle čísla, které zadáte, příklady parametrů ->
   - - - next |-> posune Vás na další stranu
   - - - next 6 |-> posune Vás o 6 stran od začátku
   - - Pokud zadáte číslo menší jak 1, tak program ohlásí chybu
   - - Pokud zadáte povel na přechod na stranu neexistující, tak se program pokusí k ní dostat co nejblíže a ohlásí chybu
   
   - previous [číslo (tento parametr je volitelný)]
   - - Pokud je více stran k zobrazení všech položek v aktuální lokaci, tak se můžete díky tomuto příkazu posunout na předchozí stranu, či o více stran podle čísla, které zadáte, příklady parametrů ->
   - - - previous |-> posune Vás na předchozí stranu
   - - - previous 6 |-> posune Vás o 6 stran k začátku
   - - Pokud zadáte číslo menší jak 1, tak program ohlásí chybu
   - - Pokud zadáte povel na přecho na stranu neexistující, tak program se program pokusí k ní dostat co nejblíže a ohlásí chybu
   
   - remove
   - - Smaže aktuální označené položky - soubory, složky i soubory a složky vnořené.
   - - Zjistí počet úspěšných a chybných odstranění a vypíše informace o výsledku příkazu.
   
   - copy
   - - Zkopíruje označené položky do aktuálního adresáře - soubory, složky i soubory a složky vnořené.
   - - Zjistí počet úspěšných a chybných kopírovaní a vypíše informace o výsledku příkazu.
   
   - move
   - - Přesune označené položky do aktuálního adresáře - soubory, složky i soubory a složky vnořené.
   - - Zjistí počet úspěšných a chybných přesunutí a vypíše informace o výsledku příkazu.
   
   - makedir !název (povinný parametr)!
   - - Vytvoří v aktuálním adresáři nový adresář se zadaným názvem od uživatele, příklady parametrů ->
   - - - makedir NewFolder |-> vytvoří v aktuálním adresáři nový adresář s názvem NewFolder
   - - Vypíše informace o výsledku provedení příkazu.
   
   - rename !nový_název (povinný parametr)! [!kde začátek_počítadla změna_počítadla minimální_počet_míst přípona_nebo_koncovka (polovinné parametry)!]
   - - Přejmenuje vybraný soubor či složku, nebo vybrané soubory či složky. Přejmenovává položky v seznamu poznačených.
   - - Pokud je pouze jedna položka k přejmenování je povinný parametr pouze nový_název, jinak jsou povinné i další parametry.
   - - nový_název - jedna část názvu, kde - after/before - pozice počítadla před či za novým_názvem, začátek_počítadla - startovní index
   - - změna_počítadla - o jaké číslo se bude počítadlo pravidelně měnit, minimální_počet_míst - minimální počet míst počítadla, přípona_nebo_koncovka - název připojený ke konci nového názvu
   - - Zjistí počet chybných a úspěšných přejmenování a vypíše výsledek příkazu a zda nedošlo k chybě, príklady parametrů ->
   - - - rename ahoj.txt |-> pokud pouze jeden soubor je vybrán tak bude přejmenován na název ahoj.txt
   - - - rename obrazek after 0 1 4 .jpg |-> všechny položky které jsou poznačené budou přejmenovány takto - obrazek0000.jpg, obrazek0001.jpg, ..........
   - copyrename !nový_název (povinný parametr)! [!kde začátek_počítadla změna_počítadla minimální_počet_míst přípona_nebo_koncovka (polovinné parametry)!]
   
   - - Zkopíruje a přejmenuje vybraný soubor či složku, nebo vybrané soubory či složky. Kopíruje a přejmenovává položky v seznamu poznačených do aktuálního adresáře.
   - - Pokud je pouze jedna položka ke kopírování a přejmenování je povinný parametr pouze nový_název, jinak jsou povinné i další parametry.
   - - nový_název - jedna část názvu, kde - after/before - pozice počítadla před či za novým_názvem, začátek_počítadla - startovní index
   - - změna_počítadla - o jaké číslo se bude počítadlo pravidelně měnit, minimální_počet_míst - minimální počet míst počítadla, přípona_nebo_koncovka - název připojený ke konci nového názvu
   - - Zjistí počet chybných a úspěšných kopírování a přejmenování a vypíše výsledek příkazu a zda nedošlo k chybě, príklady parametrů ->
   - - - copyrename ahoj.txt |-> pokud pouze jeden soubor je vybrán tak bude kopírován do aktuálního adresáře a přejmenován na název ahoj.txt
   - - - copyrename obrazek after 0 1 4 .jpg |-> všechny položky které jsou poznačené budou zkopírovány do aktuálního adresáře a přejmenovány takto - obrazek0000.jpg, obrazek0001.jpg, ..........
  
   - search !hledaný_výraz (povinný parametr)!
   - - Vyhledá soubory či složky obsahující hledaný_výraz v aktuálním umístění a v jeho podadresářích, příklady parametrů ->
   - - Průběžně informuje o vyhledávání, má kontrolu vstupu uživatele. Jako výsledek zobrazí seznam nalezených položek
   - - - search .txt |-> vyhledá všechny soubory v aktuálním adresáři a i v podadresářích končící na .txt
  
   - sort !dle_čeho_má_řadit vzestupně_sestupně (povinný parametr)!
   - - Nastaví jakým způsobem se řadí a zobrazují zobrazené položky
   - - dle_čeho_se_má_řadit - řazení dle jména - name, výchozí zobrazení - none, dle velikosti - size, dle času založení - created, dle času poslední úpravy - changed
  - - vzestupně_sestupně - vzestupně - up, sestupně - down, příklady parametrů ->
  - - - sort name down - seřadí sestupně dle jmen
