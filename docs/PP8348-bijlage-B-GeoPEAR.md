## Een oriënterende studie 

J. Lahr 

F. van den Berg 

**Alterra-rapport 1922, ISSN 1566-7197** 

# Uitspoelconcentraties en persistentie van 

# antibiotica in de bodem berekend met het 

# GeoPEARL 3.3.3 model 


Uitspoelconcentraties en persistentie van antibiotica in de bodem berekend met het GeoPEARL 3.3.3 model 


 2 Alterra-rapport 1922 

Dit onderzoek is gedaan in opdracht van het Ministerie van LNV, in het kader van het beleidsondersteunend onderzoek, programma Vitaal Landelijk Gebied, Thema Bodem (BO-01-002), en in opdracht van het Ministerie van VROM. Het onderzoek is uitgevoerd als onderdeel van het project ‘Antibiotica in de bodem’ van de Stichting Kennisontwikkeling en Kennisoverdracht Bodem (SKB) met als penvoerder adviesbureau Geofox-Lexmond. Projectcode BO-01-002-206 


### Uitspoelconcentraties en persistentie van antibiotica in de 

### bodem berekend met het GeoPEARL 3.3.3 model 

 Een oriënterende studie 

 J. Lahr F. van den Berg 

**Alterra-rapport 1922** 

**Alterra, Wageningen, 2009** 


 4 Alterra-rapport 1922 

REFERAAT 

Lahr, J. & F. van den Berg, 2009. _Uitspoelconcentraties en persistentie van antibiotica in de bodem berekend met het GeoPEARL 3.3.3 model. Een oriënterende studie_. Wageningen, Alterra, Alterra-rapport 1922. 29 blz.; 1 fig.; 5 tab.; 21 ref. 

Bij de milieubeoordeling van diergeneesmiddelen wordt door voor het afleiden van de lotgevallen in bodem en grondwater modelstudies voorgesteld. Recent is voor gewasbeschermingsmiddelen een nieuwe versie van het model GeoPEARL uitgebracht, v3.3.3. Hiermee kan men ook de persistentie in de toplaag van de bodem beoordelen. Er is een korte oriënterende studie uitgevoerd om na te gaan in hoeverre dit model ook kan worden gebruikt voor het modelleren van de lotgevallen van antibiotica. Hiertoe werden vier antibiotica geselecteerd: oxytetracycline, sulfamethoxazol, sulfadiazine en trimethoprim. De studie wijst uit dat GeoPEARL 3.3.3 in principe geschikt is voor diergeneesmiddelen, maar nog wel enkele aanpassingen behoeft. De bottleneck bij het gebruik van het model is het vinden van betrouwbare fysische en chemische eigenschappen voor diergeneesmiddelen. 

Trefwoorden: Antibiotica, Bodem, Uitspoeling, Persistentie, Model, GeoPEARL 

ISSN 1566-7197 

Dit rapport is gratis te downloaden van [http://www.alterra.wur.nl](http://www.alterra.wur.nl) (ga naar ‘Alterra-rapporten’). Alterra verstrekt geen gedrukte exemplaren van rapporten. Gedrukte exemplaren zijn verkrijgbaar via een externe leverancier. Kijk hiervoor op [http://www.boomblad.nl/rapportenservice.](http://www.boomblad.nl/rapportenservice.) 

© 2009 Alterra Postbus 47; 6700 AA Wageningen; Nederland Tel.: (0317) 480700; fax: (0317) 419000; e-mail: info.alterra@wur.nl 

Niets uit deze uitgave mag worden verveelvoudigd en/of openbaar gemaakt door middel van druk, fotokopie, microfilm of op welke andere wijze ook zonder voorafgaande schriftelijke toestemming van Alterra. 

Alterra aanvaardt geen aansprakelijkheid voor eventuele schade voortvloeiend uit het gebruik van de resultaten van dit onderzoek of de toepassing van de adviezen. 

 [Alterra-rapport 1922/september/2009] 


#### Inhoud 

Woord vooraf 7 

Samenvatting 9 

1 Inleiding 11 

2 Methoden 13 2.1 Selectie antibiotica 13 2.2 Vrachten naar de bodem 13 2.3 Stofeigenschappen 15 2.4 GeoPEARL berekeningen 16 

3 Resultaten 19 3.1 Uitspoeling naar grondwater 19 3.2 Persistentie in bodem & poriewater 19 

4 Discussie & conclusies 21 

Literatuur 25 

Bijlage 1 Stofeigenschappen van geselecteerde antibiotica 27 Bijlage 2 Beschrijving van de uitgevoerde GeoPEARL 3.3.3 berekeningen 29 



Alterra-rapport 1922 7 

#### Woord vooraf 

Dit rapport is opgesteld in opdracht van het Ministerie van LNV, in het kader van het beleidsondersteunend onderzoek, programma Vitaal Landelijk Gebied, Thema Bodem (BO-01-002), en het Ministerie van VROM. Het onderzoek is uitgevoerd als onderdeel van het project ‘Antibiotica in de bodem’ van de Stichting Kennisontwikkeling en Kennisoverdracht Bodem met als penvoerder adviesbureau Geofox-Lexmond in Tilburg. De studie werd uitgevoerd door Dr. ir. Joost Lahr van Alterra, Wageningen UR (Centrum Ecosystemen), en Dr. Erik van den Berg van Alterra, Wageningen UR (Centrum Water en Klimaat). Contactpersonen namens het Ministerie van LNV waren Jan Huinink (Directie Kennis & Innovatie, Team Leefomgeving) en Johan de Jong (Directie Natuur, Landschap & Platteland). De contactpersonen bij het Ministerie van VROM waren Sybren Landman en Maartje Nelemans. Met dank aan Nico van den Brink van Alterra, Wageningen UR, en Ton van der Linden, RIVM, voor commentaar op de conceptversie. 



Alterra-rapport 1922 9 

#### Samenvatting 

Bij de milieubeoordeling van diergeneesmiddelen worden door de voor de registratie verantwoordelijke instanties voor het afleiden van de lotgevallen (gedrag en persistentie) in bodem en grondwater modelstudies voorgesteld. In Nederland zijn de afgelopen jaren modellen ontwikkeld waarmee men de uitspoeling van gewasbeschermingsmiddelen naar het grondwater kan beoordelen. Recent is voor dit doel een nieuwe versie van het model GeoPEARL 3.3.3 uitgebracht. Hiermee kan men ook de persistentie in de toplaag van de bodem beoordelen. Door Alterra is een korte oriënterende studie uitgevoerd om na te gaan in hoeverre dit model ook kan worden gebruikt voor het modelleren van de lotgevallen van antibiotica. De studie betrof het opzoeken en invoeren van gegevens en het doorrekenen van enkele scenario’s, maar nog geen validatie van de resultaten van de modelvoorspellingen door toetsing aan meetgegevens. 

Er werden op basis van hun gebruik in Nederland vier antibiotica geselecteerd: oxytetracycline, sulfamethoxazol, sulfadiazine en trimethoprim. Voor deze stoffen werden de fysische en chemische eigenschappen uit de literatuur verzameld voor invoer in het model. Het bleek voor deze stoffen en ook voor enkele andere diergeneesmiddelen lastig om goede gegevens te vinden in de openbare literatuur. Voor de modellering werd een aantal scenario’s opgesteld voor een voorjaarstoediening via mest aan maïsakkers. De scenario’s verschilden in realisme (realistisch versus een ‘worst case’) en in toedieningswijze (diepte van de toediening, inwerken versus injecteren). 

De berekende uitspoelconcentraties waren allen laag voor de realistische scenario’s. Oxytatracycline, sulfamethoxazol en sulfadiazine spoelen volgens de berekeningen niet uit, trimethoprim in een lage concentratie. Trimethoprim spoelt aanzienlijk meer uit onder extreme ‘worst case’ omstandigheden (langere halfwaardetijd, hoge vracht). De uitspoelconcentraties lagen bij het realistische scenario echter onder de Europese drempelconcentratie van 0.1 μg/L voor grondwater. 

Qua persistentie zijn met GeoPEARL de bodemen poriewater concentraties 2 jaar en 7 jaar na stoppen van een jaarlijkse toediening gedurende 20 jaar bepaald. Sulfamethoxazol en sulfadiazine komen na 2 jaar niet meer voor in de bodem en het poriewater. Oxytetracycline is persistenter en zou volgens de modelberekeningen na 2 jaar nog in de bodem aanwezig zijn maar niet in het poriewater. Trimethoprim, ten slotte, is van de stoffen het meest persistent. In de realistische scenario’s is deze stof 7 jaar na stoppen van de jaarlijkse toedieningen echter ook verdwenen uit de toplaag. 

Trimethoprim behoeft meer aandacht in risicoanalyses en bij monitoring. Het spoelt van de vier middelen het meeste uit en is persistent. Ook wordt het middel in combinatie met verschillende andere antibiotica gebruikt waardoor de totale vracht naar het milieu groter zal zijn dan op basis van het gebruik van één soort medicijn. 


10 Alterra-rapport 1922 

Voor alle berekende parameters geldt dat er geen grote verschillen waren tussen de drie doorgerekende realistische toedieningsscenario’s: inwerken over 5 cm, inwerken over 15 cm en injecteren op 15 cm. 

De uitkomst van de GeoPEARL berekeningen staat of valt met de beschikbaarheid van betrouwbare gegevens om in het model in te voeren. Op basis van deze studie mag echter geconcludeerd worden dat, indien er goede invoergegevens beschikbaar zijn, GeoPEARL in principe gebruikt kan worden voor het modelleren van de lotgevallen van diergeneesmiddelen ten behoeve van de risicobeoordeling voor registratiedoeleinden. Er kunnen verschillende relevante scenario’s voor diergeneesmiddelen worden doorgerekend. Het model zou in de toekomst kunnen worden ingezet bij het bepalen van gebieden met de hoogste risico’s (‘hot spots’), het ontwerpen van monitoringsprogramma’s en het afkleiden van vuistregels voor de toediening van de middelen aan de dieren en van mest aan de bodem. Het is echter wel nodig om voor diergeneesmiddelen de invoer en uitvoer van het model op een aantal punten aan te passen: 

  Invoer van het model o Er moet vóór het invoeren van gegevens in GeoPEARL met de lotgevallen van de diergeneesmiddelen in mestkelders rekening worden gehouden. o In principe zouden alleen berekeningen uitgevoerd moeten worden voor plots waar de middelen ook echt terecht komen. Hiertoe moet voor mest de koppeling met het gewas gedeeltelijk worden losgelaten en een extra kaart worden geconstrueerd met gebieden waar mest uit een bepaalde veehouderijsector uitgereden wordt.  Modelaanpassingen. o In het kader van realistische scenario’s voor mest zouden mestinjectie en ploegen in combinatie doorgerekend moeten kunnen worden.  Uitvoer van het model. o Uitvoer van de initiële concentraties (‘PECinitial’) in de toplaag van de bodem en het poriewater direct na toediening van mest. o Uitvoer van de ophoping in de toplaag van de bodem gedurende de toedieningsperiode van diergeneesmiddelen. 

Daarnaast is het belangrijk om de uitkomsten van het onderliggende PEARL model te toetsen middels onderzoek in het veld. 


Alterra-rapport 1922 11 

#### 1 Inleiding 

De afgelopen 10 jaar zijn in Europees en in mondiaal verband door respectievelijk de European Medicines Agency (EMEA) en de International Cooperation on Harmonisation of Technical Requirements for Registration of Veterinary Medicinal Products (VICH) richtlijnen opgesteld voor de risicobeoordeling van de milieueffecten van diergeneesmiddelen. De voorgestelde methodiek bestaat uit een Fase 1 en een Fase 2 (VICH, 2000, 2004). Fase 2 bestaat uit drie stappen of ‘tiers’, A, B en C, waarin steeds een nadere risicokarakterisering plaats vindt. Voor het afleiden van de lotgevallen (gedrag en persistentie) in het milieu worden hiertoe modelstudies voorgesteld (EMEA, 2006). Deze dienen zich te richten op de voorspelling van de milieuconcentraties (‘Predicted Environmental Concentrations’, PEC’s) in bodem, grondwater en oppervlaktewater. De VICH (2004) geeft hierbij expliciet aan dat de PECgrondwater moet worden afgeleid op een regionaal niveau. 

In Nederland wordt sinds 1988 gebruik gemaakt van een beslisboom om het risico van uitspoeling van bestrijdingsmiddelen naar het grondwater te kunnen beoordelen. De beoordeling heeft als criterium dat concentraties van werkzame stoffen en relevante metabolieten in het grondwater over een lange periode (20-60 jaar, afhankelijk van de toepassingsfrequentie) lager moeten zijn dan 0.1 μg dm-3^ , onder tenminste 90 % van het oppervlak waarop de stoffen worden gebruikt. Om deze concentraties te kunnen berekenen is het model GeoPEARL ontwikkeld (Tiktak et al., 2003, 2006). Daartoe zijn landsdekkende schematisaties gemaakt van o.a. bodemeigenschappen, landgebruik, meteorologie en drainagesystemen. 

Recent is een nieuwe versie van het model uitgebracht, GeoPEARL 3.3.3 (van den Berg et al., 2008). Hiermee kan men van gewasbeschermingsmiddelen ook de persistentie in de toplaag van de bodem beoordelen. GeoPEARL 3.3.3 is in principe ook te gebruiken voor andere stoffen die op het land terecht komen zoals antibiotica, maar daar is nog weinig studie naar gedaan. Om deze reden is door Alterra een korte oriënterende studie uitgevoerd om na te gaan in hoeverre GeoPEARL 3.3.3 kan worden gebruikt voor het modelleren van de lotgevallen van antibiotica in bodem en grondwater. 

Voor een beperkt aantal antibiotica zijn fysisch-chemische gegevens verzameld en aan verschillende toepassingsscenario’s onderworpen. Voor de scenario’s (vrachten naar de bodem) is gebruik worden gemaakt van de uitkomsten van de recente studie naar de risico’s van diergeneesmiddelen in het terrestrische milieu door het CML (Tamis et al., 2008). 

Het onderzoek is uitgevoerd als onderdeel van het project ‘Antibiotica in de bodem’ van de Stichting Kennisontwikkeling en Kennisoverdracht Bodem. De keuze van de stoffen is tevens afgestemd met de andere onderdelen van het project met name de metingen in bodem en grondwater zodat de uitkomsten van de GeoPEARL berekeningen met de resultaten van dit onderzoek vergeleken kunnen worden. 



Alterra-rapport 1922 13 

#### 2 Methoden 

##### 2.1 Selectie antibiotica 

De selectie van de meest geschikte antibiotica voor de studie heeft plaats gevonden aan de hand van de studie van Tamis et al. (2008) en screening van de beschikbare stofgegevens voor invoer in GeoPEARL. Tamis et al. (2008) combineerden voor verschillende sectoren van de veehouderij openbare gegevens over de toediening van antibiotica aan landbouwhuisdieren, de omvang van de veestapel en de hoeveelheden aan akkers toegediende mest. Op deze wijze werd een indruk gekregen van de potentiële vrachten antibiotica naar de bodem als gevolg van het gebruik bij kalveren en koeien in de wei, zeugen en biggen, vleesvarkens en pluimvee. De meest gebruikte antibiotica zijn volgens deze berekeningen: 

  Sulfamethoxazol  Sulfadiazine  Oxytetracycline  Doxycycline  Trimethoprim  Benzylpenicilline  Ampicilline  Amoxicilline  Flumequine 

Voor deze groep stoffen is op internet en wetenschappelijke publicaties uitgebreid gezocht naar de benodigde stofeigenschappen om in GeoPEARL in te voeren (zie §2.3). Het bleek dat deze gegevens voor de meeste stoffen zeer moeilijk te vinden waren. Uiteindelijk is voor slechts vier stoffen de benodigde minimuminformatie gevonden en ook bij deze gegevens zijn soms kanttekeningen te plaatsen (zie hoofdstuk 4). De vier stoffen waarmee de berekeningen konden worden uitgevoerd zijn oxytetracycline, sulfamethoxazol, sulfadiazine en trimethoprim. Het komt niet als een verrassing dat dit tevens enkele van de meest gebruikte, en dus ook meest bestudeerde, antibiotica uit de veehouderij betreft. 

##### 2.2 Vrachten naar de bodem 

In Tabel 1 is te zien hoe uit de gegevens in het rapport van Tamis et al. (2008) de via de mest toegediende oppervlaktedosis voor akkers wordt berekend. De hiervoor gebruikte formule luidt: 

 ( /. ) 1000 

 ( /. .) ( / ) ( /. )  

   Mestproductiekg kg jr 

 Doseringmg kg jr Vrachtkg ha Oppervlaktedosisg hajr mest dier 

 antibioticum dier mest antibioticum 


###### 14 

 Alterra-rapport 1922 

_Tabel 1. Berekening van de oppervlaktedoses antibiotica toegediend via dierlijke mest op basis van de gegevens van Tamis et al. (2008). De gegevens in de kolommen ‘GeoPEARLvoorjaar’ en ‘GeoPEARL worst case’ zijn als input gebruikt voor de modelberekeningen in het rapport._ 

 Dosering 

 Mestproductie 

 Concentratie mest 

 Voorjaarsvracht mest 

 Oppervlaktedosis 

 GeoPEARL 

 Jaarvracht mest 

 Oppervlaktedosis 

 GeoPEARL 

 (mg/kg dier.jr) 

 (kg/kg dier.jaar) 

 (mg/kg) 

 (kg/ha) 

 (g/ha) 

 voorjaar 

 (kg/ha) 

 (g/ha) 

 worst case 

 Oxytetracycline Kalveren & koeien 

 17.0 

 11.4 

 1.49 

 25000 

 37.3 

 90000 

 134.2 

 Vleesvarkens 

 103.4 

 5.2 

 19.88 

 30000 

 596.5 

 600 

 40000 

 795.4 

 800 

 Zeugen & biggen 

 116.4 

 6.2 

 18.77 

 30000 

 563.2 

 40000 

 751.0 

 Vleeskuikens 

 97.5 

 1.4 

 69.64 

 4500 

 313.4 

 Trimet(h)oprim/sulfamethoxazol(e) (1:5) Kalveren & koeien 

 16.3 

 11.4 

 1.43 

 25000 

 35.7 

 90000 

 128.7 

 Vleesvarkens 

 129.0 

 5.2 

 24.81 

 30000 

 744.2 

 120/620 

 40000 

 992.3 

 170/830 

 Zeugen & biggen 

 79.0 

 6.2 

 12.74 

 30000 

 382.3 

 40000 

 509.7 

 Vleeskuikens 

 0.0 

 1.4 

 0.00 

 4500 

 0.0 

 Trimet(h)oprim/sulfadiazine (1:5) Kalveren & koeien 

 0.0 

 11.4 

 0.00 

 25000 

 0.0 

 90000 

 0.0 

 Vleesvarkens 

 23.8 

 5.2 

 4.58 

 30000 

 137.3 

 40000 

 183.1 

 Zeugen & biggen 

 88.6 

 6.2 

 14.29 

 30000 

 428.7 

 70/360 

 40000 

 571.6 

 100/480 

 Vleeskuikens 

 0.0 

 1.4 

 0.00 

 4500 

 0.0 


Alterra-rapport 1922 15 

Bij de berekende vrachten kan onderscheid worden gemaakt tussen de voorjaarsvracht en de totale jaarvracht. De eerste wordt hier verder als het realistische scenario beschouwd omdat toediening van gier uit mestkelders meestal in het voorjaar plaatsvindt, de tweede als ‘worst case’ indien alle gier van een heel jaar in een keer wordt toegediend. 

De berekeningen in dit rapport zijn ook worst case doordat is gerekend met de hoogste oppervlaktedoses van de vier sectoren: vleesvarkens voor oxytetracycline, sulfamethoxazol en trimethoprim, en zeugen/biggen voor sulfadiazine (Tabel 1). Trimethoprim wordt gebruikt in combinatie met gesulfoneerde antibiotica. Voor trimethoprim is in het rapport verder gerekend met de vrachten die berekend zijn op basis van de 1:5 combinatie met sulfamethoxazol. Deze waren het grootst. 

##### 2.3 Stofeigenschappen 

De stofeigenschappen die nodig zijn voor berekeningen met GeoPEARL zijn: 

  De molecuulmassa (g)  De dampdruk, p (Pa) bij een referentie temperatuur  De oplosbaarheid in water, S (mg/L), bij een referentie temperatuur 

 De coëfficiënt voor sorptie aan organische stof in de bodem, K (^) om (L/d)  De halfwaardetijd van de (bio)degradatie in de bodem, DT 50 (d) De Kom-waarde werd voorafgaand aan de modelberekeningen omgerekend uit de Koc , de coëfficiënt voor sorptie aan organisch koolstof in de bodem, door de K (^) oc te vermenigvuldigen met 0.57 (Smit et al., 1997). In Bijlage 1 staan alle stofeigenschappen die op internet en in de literatuur gevonden zijn. Het was moeilijk de betrouwbaarheid van alle gegevens te verifiëren. In veel gevallen werd slechts één enkele waarde voor een bepaalde eigenschap achterhaald. Sommige gegevens waren sterk afwijkend van andere gegevens voor dezelfde parameters en dus mogelijk onbetrouwbaar. Dit soort data is niet meegenomen bij de modelberekeningen. In Bijlage 1 is door middel van een grijze arcering aangegeven welke gegevens uiteindelijk zijn gebruikt. Wanneer meerdere acceptabele waarden voor dezelfde parameters werden gevonden, is het geometrisch gemiddelde bepaald (het gemiddelde van de logaritmes van de waarden weer terug gerekend naar een gewoon getal). Indien gegevens in meerdere bronnen werden gevonden waren de waarden soms identiek, waardoor er een vermoeden was dat dezelfde initiële bron is gebruikt. In deze gevallen is de waarde slechts een maal meegeteld in de berekening van het gemiddelde. 


16 Alterra-rapport 1922 

##### 2.4 GeoPEARL berekeningen 

In Tabel 2 zijn de geselecteerde gegevens opgesomd die zijn gebruikt om in GeoPEARL een aantal verschillende scenario’s door te rekenen. Er is onderscheid gemaakt tussen een realistische toediening op basis van de voorjaarsgift die in de praktijk ook eenmalig is. Daarnaast is gerekend aan een ‘worst case’. Hiervoor is aangenomen dat de berekende totale jaarvrachten uit Tamis et al. (2008) in één enkele keer worden toegediend. Daarnaast is voor deze worst case ook gerekend met een langere halfwaardetijd voor de omzetting in grond. Voor oxytetracycline, sulfadiazine en trimethoprim zijn hiervoor de hoogste in de literatuur gevonden waarden gebruikt. Voor sulfamethoxazol werd maar één DT 50 gevonden en is voor de worst case gerekend met tien maal de gevonden waarde. 

_Tabel 2. Geselecteerde stofeigenschappen en vrachten naar de bodem voor vier veel in Nederland gebruikte veterinaire antibiotica die zijn ingevoerd in GeoPEARL 3.3.3 (zie Bijlage 1 voor een overzicht van alle gevonden gegevens en de geraadpleegde bronnen)._ Antibioticum Molecuulgewicht 

 Dampdruk (mPa) 

 Water oplosbaarheid (g/L) 

 Sorptiecoëfficiënt Koc (L/kg) 

 Realistisch Worst case 

 DT50 bodem (d) 

 Voorjaarsgift (g a.i./ha) 

 DT50 bodem (d) 

 Jaarvracht (g a.i./ha) 

Oxytetracycline 460.44 1.29× E-19 

 0.55 47932 28.2 600 180 800 

Sulfamethoxazol 253.28 2.49× E-04 

 0.42 181 2 620 20 830 

Sulfadiazine 250.28 3.13× E-04 

 0.077 80.7 1.6 360 28 480 

Trimethoprim* 290.32 1.32× E-03 

 0.4 123 51 120 100 170 

*vrachten als bij toediening in mengsel met sulfamethoxazol 

In GeoPEARL kan men een groot aantal variabelen instellen en keuzes maken met betrekking van het soort gewas, het tijdstip van toediening enzovoort. Er is voor deze oriënterende studie gekozen voor een aantal scenario’s met toediening in het voorjaar op maïsakkers. De meeste maïsakkers zijn gelegen op zandgronden (Figuur 1). Deze scenario’s komen overeen met toediening van varkensdrijfmest in Oost Nederland, waar ook het veldonderzoek van het SKB project ‘Antibiotica in de Bodem zich op richtte’. 

De volgende instellingen zijn gebruikt: 

  Aantal plots = 250 (default waarde in GeoPEARL)  Gewas = maïs  Toedieningsfrequentie = 1× per jaar  Toedieningsdatum = 15 april  Toplaag van de bodem = 5 cm (de bodemlaag waarover de concentraties worden berekend) 


Alterra-rapport 1922 17 

Met GeoPEARL zijn voor de vier antibiotica vier verschillende GeoPEARL scenario’s doorgerekend (zie ook Tabel 2 voor de doseringen en DT 50 -waarden voor de realistische en worst case scenario’s): 

  Realistisch, inwerken over 5 cm van de bodem  Worst case, inwerken over 5 cm van de bodem  Realistisch, inwerken over 15 cm van de bodem  Realistisch, injectie op 15 cm diepte in de bodem 

Met inwerken wordt bedoeld dat het middel, of in dit geval de mest met het antibioticum, wordt verdeeld over een bodemlaag met een bepaalde dikte. Inwerken over 5 cm komt overeen met oppervlakkig inploegen of frezen, over 15 cm met wat dieper inploegen (NB – de bodemconcentraties worden bij inwerken over 15 cm nog steeds berekend over de genoemde toplaag van 5 cm). Bij injectie wordt het middel op een bepaalde diepte in de bodem ingebracht. In de praktijk wordt drijfmest vaak geïnjecteerd en de bodem enkele dagen later geploegd. Ploegen na inwerken is met GeoPEARL niet te simuleren. 

De standaard uitvoer van GeoPEARL betstaat uit het 90-percentiel in de ruimte van de mediane uitspoelconcentratiewaarden in de tijd op 1 m diepte, d.w.z. in 90 van de 100 gevallen is de uitspoelconcentratie beneden deze waarde. De mediaan wordt berekend over 20 jaar. 

_Figuur 1. Maïspercelen (links) en zandgronden (rechts) in Nederland (kaarten uit GeoPEARL 3.3.3)._ 



Alterra-rapport 1922 19 

#### 3 Resultaten 

De originele uitdraaien met de GeoPEARL invoer en berekeningen worden gegeven in Bijlage 2. In de paragrafen hierna worden de resultaten voor uitspoeling en persistentie in de bodem samengevat en kort besproken. 

##### 3.1 Uitspoeling naar grondwater 

In Tabel 3 zijn de resultaten te zien van de uitspoelingsberekeningen met GeoPEARL. In de tabel is duidelijk te zien dat geen van de scenario’s leidt tot uitspoeling van oxytetracycline en sulfamethoxazol. In het geval van sulfadiazine wordt voor het worst case scenario een uitspoelconcentratie van 0,032 μg/L berekend. Dit is een lage waarde en de concentratie komt voornamelijk tot stand omdat in het worst case scenario een halfwaardetijd van 28 dagen werd gebruikt in plaats van de 1,6 d uit het realistische scenario. 

Voor trimethoprim leiden de realistische scenario’s tot een uitspoelconcentratie van 0,016-0,019 μg/L. Dit wordt veroorzaakt doordat deze stof volgens de verzamelde gegevens aanzienlijk persistenter is in de bodem dan de andere drie antibiotica, de DT 50 is met 51 dagen het langst. Ook Oxytetracycline heeft een wat langere halfwaardetijd (28 d), maar deze stof hecht weer veel sterker aan bodemdeeltjes dan de overige drie antibiotica (zie de Koc -waarde in Tabel 2). Het worst case scenario voor trimethoprim leidt tot een hoge uitspoelconcentratie van circa 0.64 μg/L. Dit is gebaseerd op een maximale DT 50 van 100 dagen. Bij de realistische scenario’s voor trimethoprim geven inwerken over 15 cm en injectie op 15 cm diepte een iets hogere uitspoelconcentratie dan inwerken over 5 cm. 

_Tabel 3. Met GeoPEARL 3.3.3 berekende uitspoelconcentraties van antibiotica op 1m diepte na toediening via mest aan de bodem. Concentraties in μg/L als 90-percentiel in de ruimte van de mediane waarden over 20 jaar._ Scenario Realistisch Inwerken 5cm 

 Worst case Inwerken 5cm 

 Realistisch Inwerken 15 cm 

 Realistisch Injectie 15 cm 

Oxytetracycline 0.000 0.000 0.000 0.000 Sulfamethoxazol 0.000 0.000 0.000 0.000 Sulfadiazine 0.000 0.032 0.000 0.000 Trimethoprim 0.016 0.636 0.019 0.019 

##### 3.2 Persistentie in bodem & poriewater 

De standaard uitvoer van GeoPEARL 3.3.3 voor de berekening van de persistentie in de bodem en het poriewater bestaat uit de concentraties in de bodem op basis van het ‘Community Recovery Principle’ (CRP) en het ‘Ecological Treshold Principle’ (ETP). Deze parameters betreffen de concentraties respectievelijk 2 jaar na de laatste 


20 Alterra-rapport 1922 

toediening en 7 jaar na de laatste toediening. De uitvoer van GeoPEARL bestaat verder uit het verloop van de CRP en ETP concentraties gedurende 365 dagen volgend op het moment van 2 respectievelijk 7 jaar na de laatste toediening. 

In Tabel 4 worden voor de vier antibiotica de concentraties in de bodem 2 jaar en 7 jaar na toediening gegeven, in Tabel 5 de bijbehorende poriewaterconcentraties. 

_Tabel 4. Met GeoPEARL 3.3.3 berekende totale concentraties van antibiotica in de toplaag van de bodem (bovenste 5 cm) na toediening van mest aan maïsakkers. Concentratie in μg/kg 2 jaar na laatste toediening en 7 jaar na laatste toediening._ Scenario Realistisch Inwerken 5cm 

 Worst case Inwerken 5cm 

 Realistisch Inwerken 15 cm 

 Realistisch Injectie 15 cm 2 jr. 7 jr. 2 jr. 7 jr. 2 jr. 7 jr. 2 jr. 7 jr. 

Oxytetracycline 0.249 0.000 279.3 15.52 0.231 0.000 0.231 0.000 Sulfamethoxazol 0.000 0.000 0.012 0.000 0.000 0.000 0.000 0.000 Sulfadiazine 0.000 0.000 0.072 0.000 0.000 0.000 0.000 0.000 Trimethoprim 0.670 0.000 8.091 0.020 0.654 0.000 0.613 0.000 

_Tabel 5. Met GeoPEARL 3.3.3 berekende totale concentratie van antibiotica in het poriewater van de toplaag van de bodem (bovenste 5 cm) na toediening van mest aan maïsakkers. Concentratie in μg/L 2 jaar na laatste toediening en 7 jaar na laatste toediening._ 

Scenario Realistisch Inwerken 5cm 

 Worst case Inwerken 5cm 

 Realistisch Inwerken 15 cm 

 Realistisch Injectie 15 cm 2 jr. 7 jr. 2 jr. 7 jr. 2 jr. 7 jr. 2 jr. 7 jr. 

Oxytetracycline 0.000 0.000 0.075 0.003 0.000 0.000 0.000 0.000 Sulfamethoxazol 0.000 0.000 0.001 0.000 0.000 0.000 0.000 0.000 Sulfadiazine 0.000 0.000 0.010 0.000 0.000 0.000 0.000 0.000 Trimethoprim 0.065 0.000 0.866 0.002 0.065 0.000 0.020 0.000 

Uit de tabellen blijkt dat de sulfaverbindingen sulfamethoxazol en sulfadiazine volgens de realistische scenario’s niet persistent zijn in de bodem en het poriewater. Zij zijn al na 2 jaar verdwenen. Onder het worst case scenario zouden zij na 2 jaar nog in lage concentraties (nanogram range) kunnen voorkomen maar na 7 jaar alsnog verdwenen zijn. 

Oxytetracycline is persistenter, met name in de bodem (Tabel 4), waarschijnlijk omdat het middel in vergelijking met de andere antibiotica sterk aan het organisch stof in de bodem hecht en dus minder uitspoelt. Het zou in het poriewater alleen onder worst case omstandigheden worden aangetroffen (Tabel 5). In het worst case scenario is de persistentie in de bodem ook veel groter (Tabel 4). 

Trimethoprim is eveneens persistenter dan de sulfaverbindingen. Onder het realistische scenario zou het na 2 jaar nog in zowel de bodem als het poriewater kunnen worden aangetroffen in lage concentraties (<1 μg/kg bodem, <1 μg/L poriewater). De verklaring is de relatief lange halfwaardetijd (51 d). Ook hier leidt het worst case scenario tot een veel grotere persistentie. 


Alterra-rapport 1922 21 

#### 4 Discussie & conclusies 

De met GeoPEARL 3.3.3 berekende uitspoelconcentraties (90-percentielen van de mediane waarden over 20 jaar) na toediening aan maïsakkers half april waren allen laag voor de realistische scenario’s (voorjaarsvracht en gemiddelde DT 50 uit de literatuur). Oxytatracycline, sulfamethoxazol en sulfadiazine zouden volgens de berekeningen niet uitspoelen, trimethoprim in een lage concentratie. Trimethoprim spoelt aanzienlijk meer uit onder ‘worst case’ omstandigheden (lange halfwaardetijd, hoge vracht). De uitspoelconcentraties lagen bij het realistische scenario echter onder de Europese drempelconcentratie van 0.1 μg/L voor grondwater waarboven een nadere risicoanalyse van grondwater zou moeten worden uitgevoerd (EMEA, 2006). Onder het worst case scenario kwam de concentratie voor trimethoprim als enige van de vier antibiotica wel boven de 0.1 μg/L uit. 

Om de persistentie te bepalen zijn met GeoPEARL de bodemen poriewater concentraties 2 jaar en 7 jaar na stoppen van een jaarlijkse toediening gedurende 20 jaar geschat. Sulfamethoxazol en sulfadiazine komen na 2 jaar niet meer voor in de bodem en het poriewater. Omdat deze stoffen ook al niet uitspoelen en een lage dampdruk hebben, kan worden geconcludeerd dat deze stoffen voornamelijk verdwijnen via afbraak in de bodem. Dit wordt gestaafd door een halfwaardetijd in de bodem van respectievelijk 2 dagen en 1,6 dagen. Oxytetracycline is persistenter en zou volgens de modelberekeningen na 2 jaar nog in de bodem aanwezig zijn maar niet in het poriewater. Dit valt te verklaren doordat oxytetracycline een langere halfwaardetijd heeft dan de twee gesulfoneerde antibiotica en zich van de vier stoffen het sterkst hecht aan het bodemmateriaal. Trimethoprim ten slotte is van de stoffen het meest persistent (DT 50 51 d). In de realistische scenario’s is deze stof 7 jaar na stoppen van de jaarlijkse toedieningen echter ook verdwenen uit de toplaag. 

Uit de berekeningen kwam trimethoprim, zoals gezegd, naar voren als de enige van de vier stoffen die uitspoelt en als meest persistent. Dit antibioticum behoeft daarom meer aandacht in risicoanalyses en bij monitoring, ook omdat het in combinatie met verschillende andere antibiotica wordt gebruikt. De totale emissie in het milieu kan dus groter zijn dan op basis van één soort medicijn te verwachten is. 

Voor alle berekende parameters geldt dat er geen grote verschillen waren tussen de drie doorgerekende realistische toedieningsscenario’s: inwerken over 5 cm, inwerken over 15 cm en injecteren op 15 cm. 

De uitkomst van de GeoPEARL berekeningen staat of valt met de beschikbaarheid van betrouwbare gegevens om in het model in te voeren. Voor de vier antibiotica in deze studie werd slechts een beperkte hoeveelheid gegevens gevonden in openbare bronnen, ondanks het feit dat het hier veel gebruikte middelen betreft. DT 50 waarden waren het moeilijkst te achterhalen en als er meerdere waarden beschikbaar waren, liepen deze soms sterk uiteen (zie de gegevens voor oxytetracycline en sulfadiazine in Bijlage 1). Ook Koc waarden voor hetzelfde antibioticum verschilden soms aanzienlijk 


22 Alterra-rapport 1922 

(sulfadiazine) en er is geen rekening gehouden met het feit dat de sorptie van sommige antibiotica pH-afhankelijk kan zijn. Gezien het sterke effect op de modelberekeningen, lijkt het vooral van belang dat de voor GeoPEARL gebruikte halfwaardetijden beter onderbouwd worden. Dit is op dit moment misschien wel de grootste bottleneck. 

Naast betrouwbare stofgegevens zijn ook de vrachten naar de bodem van groot belang. Voor deze studie zijn deze berekend op basis van de (gemiddeld) gebruikte doses per doeldier, de gemiddelde hoeveelheid mest die door deze dieren wordt geproduceerd en de gemiddelde vrachten mest die op de bodem worden gebracht. Met afbraak in de mestkelder gedurende het winterseizoen is bij gebrek aan gegevens geen rekening gehouden. Daarnaast is aangenomen dat alle maïsakkers in Nederland een mestgift met antibiotica uit een bepaalde veehouderijsector ontvangen. Dit zal in de praktijk niet het geval zijn. De resultaten van het ‘realistische’ scenario zijn om deze redenen al enigszins worst case en de uitkomsten voor het ‘worst case’ scenario moeten in dit licht misschien als een onrealistische ‘worst case’ worden beschouwd. Op basis van deze eerste berekeningen is echter wel aan te geven hoe de vier stoffen uit de studie onderling verschillen qua uitspoelgedrag en persistentie. 

Al met al zijn er genoeg redenen om de uitkomsten van deze oriënterende studie met voorzichtigheid te interpreteren. Dit ligt vooral aan de kwaliteit van de invoergegevens en minder aan het model zelf. De publiekelijk beschikbare gegevens ten aanzien van de stofeigenschappen waren niet goed te valideren en mogelijk van een wisselende kwaliteit. 

GeoPEARL 3.3.3 is een ‘state-of-the-art’, landsdekkend model dat gericht is op de berekening van doelgrootheden voor de registratie van gewasbeschermingsmiddelen. Het is echter minder geschikt voor het afleiden van locatiespecifieke lotgevallen. Dit soort berekeningen kan worden uitgevoerd met het gewone PEARL model waarmee gedetailleerd de lotgevallen op een specifieke locatie kunnen worden doorgerekend.. In dat geval is een profielbeschrijving nodig van de bodemhorizonten ter plekke: per bodemlaag organische stof, minerale samenstelling, vochtkarakteristieken, enz. Verder is per locatie informatie vereist over het sorptiegedrag en de omzettingssnelheid van een stof. Een alternatief is om een FOCUS grondwater scenario te kiezen (FOCUS, 2000) en dan met FOCUS-PEARL berekeningen uit te voeren voor diergeneesmiddelen. FOCUS scenario’s zijn ontwikkeld om op Europees niveau de uitspoeling van gewasbeschermingsmiddelen naar grondwater te berekenen. Hiervoor is een speciale versie van PEARL ontwikkeld. Van de 10 FOCUS scenario’s ligt het Hamburg scenario het dichtst bij Nederland, maar in de richtlijn van de EMEA (2006) voor risicoanalyse van diergeneesmiddelen wordt bijvoorbeeld het Okehampton scenario in Groot-Brittannië gesuggereerd. Voor de eerste tier beoordeling van gewasbeschermingsmiddelen wordt het Kremsmünster scenario gehanteerd. 

Op basis van deze studie kan geconcludeerd worden dat indien er goede informatie met betrekking tot de stofeigenschappen beschikbaar is, bijvoorbeeld de informatie van de fabrikanten zelf, GeoPEARL in de toekomst in principe gebruikt kan worden 


Alterra-rapport 1922 23 

voor het modelleren van de lotgevallen van diergeneesmiddelen ten behoeve van de risicobeoordeling voor registratiedoeleinden. Er kunnen namelijk verschillende relevante scenario’s voor diergeneesmiddelen mee worden doorgerekend. Verder kan het model worden ingezet bij het bepalen van gebieden met de hoogste risico’s (‘hot spots’) en bij het ontwerpen van monitoringsprogramma’s. Hiertoe is het eerst nog wel nodig om de invoer en de uitvoer van het model aan te passen op een aantal wezenlijke punten: 

  Invoer van het model o Er moet vóór het invoeren van gegevens in GeoPEARL met de lotgevallen van de diergeneesmiddelen in mestkelders rekening worden gehouden. o In principe zouden alleen berekeningen uitgevoerd moeten worden voor plots waar de middelen ook echt terecht komen. Hiertoe moet voor mest de koppeling met het gewas gedeeltelijk worden losgelaten en een extra kaart worden geconstrueerd met gebieden waar mest uit een bepaalde veehouderijsector uitgereden wordt.  Modelaanpassingen. o In het kader van realistische scenario’s voor mest zouden mestinjectie en ploegen in combinatie doorgerekend moeten kunnen worden.  Uitvoer van het model. o Uitvoer van de initiële concentraties (‘PECinitial’) in de toplaag van de bodem en het poriewater direct na toediening van mest. o Uitvoer van de ophoping in de toplaag van de bodem gedurende de toedieningsperiode van diergeneesmiddelen. 

Daarnaast is het belangrijk om de uitkomsten van het onderliggende PEARL model te toetsen middels onderzoek in het veld. 

Naast het gebruik voor registratiedoeleinden kunnen GeoPEARL en aanverwante modellen ook gebruikt worden voor het doorrekenen van verschillende scenario’s voor de boerenpraktijk en de dierenartsenpraktijk, bijvoorbeeld ten aanzien van de methoden van in de bodem brengen (zoals in dit rapport onderwerken versus injecteren), het tijdstip van toediening van mest aan de bodem en de keuze van minder milieuschadelijke diergeneesmiddelen indien er voor een aandoening meerdere middelen beschikbaar zijn. Met hulp van GeoPEARL kunnen dus vuistregels worden afgeleid om de ecologische risico’s van het gebruik van diergeneesmiddelen in de praktijk te reduceren. 



Alterra-rapport 1922 25 

#### Literatuur 

Berg, F. van den, A. Tiktak, J.G. Groenwold, D.W.G. van Kraalingen, A.M.A. van der Linden & J.J.T.I. Boesten. 2008. Documentation update for GeoPEARL_3.3.3. Wettelijke Onderzoekstaken Natuur & Milieu, Werkdocument nr. 103, Alterra, Wageningen UR/Planbureau voor de Leefomgeving, Wageningen/Bilthoven. 

Drillia, P., K. Stamatelatou & G. Lyberatos. 2005. Fate and mobility of pharmaceuticals in solid matrices. _Chemosphere_ 60: 1034-1044. 

EMEA. 2006. Guideline on environmental impact assessment for veterinary medicinal products in support of the VICH Guidelines GL6 and GL38. European Medicines Agency, Committee for Medicinal Products for Veterinary Use (CVMP), London. 

FOCUS. 2000. FOCUS groundwater scenarios in the EU review of active substances. Report of the FOCUS Groundwater Scenarios Workgroup, EC Document Reference SANCO/321/2000 rev. 2, Europese Unie, Brussel, 202 pp. 

Kay, P., P.A. Blackwell & A.B.A. Boxall. 2004. Fate of veterinary antibiotics in a macroporous tile drained clay soil. _Environmental Toxicology and Chemistry_ 23: 11361144. 

Kotzerke, A., S. Sharma, K. Schauss, H. Heuer, S. Thiele-Bruhn, K. Smalla, B.-M. Wilke & M. Schloter. 2008. Alterations in soil microbial activity and _N_ transformation processes due to sulfadiazine loads in pig-manure. _Environmental Pollution_ 153: 315-322. 

Lissemore, L., C. Hao, P. Yang, P.K. Sibley, S. Mabury & K.R. Solomon. An exposure assessment for selected pharmaceuticals within a watershed in Southern Ontario. _Chemosphere_ 64: 717-729. 

Rabølle, M. & N.H. Spliid. 2000. Sorption and mobility of metronidazole, olaquindox, oxytetracycline and tylosin in soil. _Chemosphere_ 40: 715-722. 

Smit, A.A.M.F.R., F. van den Berg & M. Leistra. 1997. Estimation method for the volatilisation of pesticides from fallow soils. Environmental Planning Bureau series 2, DLO Winand Staring Centre, Wageningen. 

Sukul, P. & M. Spitteler. 2006. Sulfonamides in the environment as veterinary drugs. _Reviews in Environmental Contamination and Toxicology_ 187: 67-101. 

Tamis, W.L.M., P.G.L. Klinkhamer, E. van der Meijden & J.A. van Veen. 2008. Potentiële effecten van diergeneesmiddelen op het terrestrische milieu in Nederland. 


26 Alterra-rapport 1922 

Thiele-Bruhn, S. 2003. Pharmaceutical antibiotic compounds in soils – a review. _Journal of Plant Nutrition and Soil Science_ 166: 145-167. 

Thiele-Bruhn, S. & M.-O. Aust. 2004. effects of pig slurry on the sorption of sulfonamide antibiotics in soil. _Archives of Environmental Contamination and Toxicology_ 47: 31-39. 

Tiktak, A., A.M.A. van der Linden & J.J.T.I. Boesten. 2003. The GeoPEARL model. Model description, applications and manual. RIVM rapport nr. 716601007/2003, RIVM/Alterra, Bilthoven/Wageningen. 

Tiktak, A., A.M.A. van der Linden, J.J.T.I. Boesten, R. Kruijne, D. van Kraalingen & F. van den Berg. 2006. The GeoPEARL model version 2.2.2. Part II. User guide and model description update. RIVM rapport nr. 716601008/2004-2006, Milieu en Natuur Planbureau/RIVM/Alterra, Bilthoven/Bilthoven/Wageningen. 

Tolls, J. 2001. Sorption of veterinary pharmaceuticals in soils: a review. _Environmental Science and Technology_ 35: 3397-3406. 

Topp, E, S.C. Monteiro, A. Beck, B.B. Coelho, A.B.A. Boxall, P.W. Duenk, S. Kleywegt, D.R. Lapen, M. Payne, L. Sabourin, H. Li & C.D. Metcalfe. 2008. Runoff of pharmaceuticals and personal care products following application of biosolids to an agricultural field. _Science of the Total Environment_ 396: 52-59. 

VICH (2000) Environmental impact assessment (EIAs) for veterinary medicinal products (VMPs) – Phase I. Rapport VICH GL6 (Ecotoxicity Phase I), June 2000, for implementation at Step 7, International Cooperation on Harmonisation of Technical Requirements for registration of Veterinary Medicinal Products (VICH), Brussel. 

VICH (2004) Environmental impact assessment (EIAs) for veterinary medicinal products (VMPs) – Phase II. Rapport VICH GL38 (Ecotoxicity Phase II), October 2004, for implementation at Step 7, International Cooperation on Harmonisation of Technical Requirements for Registration of Veterinary Medicinal Products (VICH), Brussel. 

Wehrhan, A., R. Kasteel, J. Simunek, J. Groeneweg & H. Vereecken. 2007. Transport of sulfadiazine in soil columns – experiments and modelling approaches. _Journal of Contaminant Hydrology_ 89: 107-135. 

Wightwick, A. & G. Allinson. 2008. Compilation of agrochemicals registered for use in Victoria and their physical-chemical properties. Report. The State of Victoria, Department of Primary Industries, Queenscliff, Victoria, Australië, 29 p. 


 Alterra-rapport 1922 

###### 27 

#### Bijlage 1 

#### Stofeigenschappen van geselecteerde antibiotica 

 Stofeigenschappen van geselecteerde antibiotica. De grijs gearceerde gegevens zijn gebruikt voor deGeoPEARL berekeningen.^ Pharmaceutical 

 CAS # 

 MW Source 

 Vp 

 T^ 

 Source 

 Solubility 

 T^ 

 Source 

 (°C) 

 (g/L) 

 (°C) 

 Oxytetracycline 

 79-57-2 

 460.44 Tolls 2001 

 1.29E-19mPa 

 Wightwick & Allinson 2008 

 0.3 

 Kay et al 2004 

 1 

 Tolls 2001 

 Sulfamethoxazole 

 723-46-6 

 253.28 Sukul & Spitteler 2006 

 1.87E-9 Torr 

 25 

 Sukul & Spitteler 2006 

 0.61 

 drugbank.ca 

 0.29 

 20 

 wildlifeinformation.org 

 Sulfadiazine 

 68-35-9 

 250.28 Sukul & Spitteler 2006 

 1.28E-10Torr 

 25 

 Sukul & Spitteler 2006 

 0.077 

 Sukul & Spitteler 2006 

 5.745E-6Pa 

 Wehrhan et al 2007 

 0.013-0.077 

 Wehrhan et al 2007 

 NR 

 Wightwick & Allinson 2008 

 0.077 

 Wightwick & Allinson 2008 

 Trimethoprim 

 738-70-5 

 290.32 Wightwick & Allinson 2008 

 9.88E-9 mmHg 

 25 

 Lissemore et al 2006 

 0.4 

 Lissemore et al 2006 

 1.32E-3 mPa 

 Wightwick & Allinson 2008 

 0.4 

 Wightwick & Allinson 2008 


###### 28 

 Alterra-rapport 1922 

Pharmaceutical 

CAS # 

Koc 

Source 

DT50 soil 

Source 

 (L/kg) 

 (d) 

 Oxytetracycline 

 79-57-2 

 42506 sandy loam soil 

 Rabølle & Spliid 2000 

 18.2 

 Kay et al 2004 

 47881 sandy soil 

 Rabølle & Spliid 2000 

 >180 soil + manure 

 Thiele-Bruhn 2003 

 93317 sandy loam soil 

 Rabølle & Spliid 2000 

 43.8 aer sediment slurry 

 Thiele-Bruhn 2003 

 27792 loamy sand soil 

 Rabølle & Spliid 2000 

 Sulfamethoxazole 

 723-46-6 

 4.44 at pH 7 

 Sukul & Spitteler 2006 

 2 

 Topp et al 2008 

 530 high OM 

 Drillia et al 2005 

 62 low OM 

 Drillia et al 2005 

 Sulfadiazine 

 68-35-9 

 124 silt loam 

 Thiele-Bruhn 2003 

 >28 manure/sludge 

 Thiele-Bruhn 2003 

 81 clay loam 

 Thiele-Bruhn 2003 

 1.6 man/sludge respiked 

 Thiele-Bruhn 2003 

 124 unfert. Soil 

 Thiele-Bruhn & Aust 2004 

 4<<32 sandy/silty 

 Kotzerke et al 2008 

 73.2 soil-slurry 

 Thiele-Bruhn & Aust 2004 

 37-126 

 Wightwick & Allinson 2008 

 4.95 at pH 7 

 Sukul & Spitteler 2006 

 Trimethoprim 

 738-70-5 

 205 sewage sludge 

 Thiele-Bruhn 2003 

 22-41 sewage sludge 

 Thiele-Bruhn 2003 

 74 soil 

 Wightwick & Allinson 2008 

 75-100 soil 

 Wightwick & Allinson 2008 


Alterra-rapport 1922 29 

#### Bijlage 2 Beschrijving van de uitgevoerde GeoPEARL 3.3.3 

#### berekeningen 

Asessment nr. Stof Scenario Toediening aan bodem 

5 Oxytetracycline Realistisch Inwerken in bovenste 5 cm 

6 Sulfamethoxazol Realistisch (^) Inwerken in bovenste 5 cm 7 Sulfadiazine Realistisch (^) Inwerken in bovenste 5 cm 8 Trimethoprim Realistisch Inwerken in bovenste 5 cm 10 Oxytetracycline Worst case (^) Inwerken in bovenste 5 cm 11 Sulfamethoxazol Worst case Inwerken in bovenste 5 cm 12 Sulfadiazine Worst case (^) Inwerken in bovenste 5 cm 13d Trimethoprim Worst case Inwerken in bovenste 5 cm 15 Oxytetracycline Realistisch Inwerken in bovenste 15 cm 16 Sulfamethoxazol Realistisch Inwerken in bovenste 15 cm 17 Sulfadiazine Realistisch (^) Inwerken in bovenste 15 cm 18 Trimethoprim Realistisch Inwerken in bovenste 15 cm 19 Oxytetracycline Realistisch Injecteren op 15 cm diepte 20 Sulfamethoxazol Realistisch (^) Injecteren op 15 cm diepte 21 Sulfadiazine Realistisch Injecteren op 15 cm diepte 22 Trimethoprim Realistisch (^) Injecteren op 15 cm diepte 


































