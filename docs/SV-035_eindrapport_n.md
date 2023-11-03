
# SV-035 

# Implementatie van smart pump&treat 

 Ontwerp en toetsing op robuustheid 

Deelrapport II 

drs. R.A.A. Hetterschijt (TNO NITG) ir. F.J. Roelofsen (TNO NITG) ir. L.M.M. Bakker (Tauw B.V.) 

januari 2001 

Gouda, CUR/SKB 

## Stichting Kennisontwikkeling Kennisoverdracht Bodem 


**Auteursrechten** Alle rechten voorbehouden. Niets uit deze opgave mag worden verveelvoudigd, opgeslagen in een geautomatiseerd gegevensbestand of openbaar gemaakt, in enige vorm of op enige wijze, hetzij elektronisch, mechanisch, door fotokopieën, opnamen of op enige andere manier, zonder voorafgaande schriftelijke toestemming van CUR/SKB. Het is toegestaan overeenkomstig artikel 15a Auteurswet 1912 gegevens uit deze uitgave te citeren in artikelen, scripties en boeken mits de bron op duidelijke wijze wordt vermeld, alsmede de aanduiding van de maker, indien deze in de bron voorkomt, "©"Implementatie van smart pump&treat Deelrapport II, Ontwerp en toetsing op robuustheid", januari 2001, CUR/SKB, Gouda." 

**Aansprakelijkheid** CUR/SKB en degenen die aan deze publicatie hebben meegewerkt, hebben een zo groot mogelijke zorgvuldigheid betracht bij het samenstellen van deze uitgave. Nochtans moet de mogelijkheid niet worden uitgesloten dat er toch fouten en onvolledigheden in deze uitgave voorkomen. Ieder gebruik van deze uitgave en gegevens daaruit is geheel voor eigen risico van de gebruiker en CUR/SKB sluit, mede ten behoeve van al degenen die aan deze uitgave hebben meegewerkt, iedere aansprakelijkheid uit voor schade die mocht voortvloeien uit het gebruik van deze uitgave en de daarin opgenomen gegevens, tenzij de schade mocht voortvloeien uit opzet of grove schuld zijdens CUR/SKB en/of degenen die aan deze uitgave hebben meegewerkt. 


**Titel rapport CUR/SKB rapportnummer** Implementatie van smart pump&treat SV-035 Ontwerp en toetsing op robuustheid Deelrapport II **Project rapportnummer** SV-035 

**Auteur(s) Aantal bladzijden** drs. R.A.A. Hetterschijt **Rapport:** 54 ir. F.J. Roelofsen **Bijlagen:** 28 ir. L.M.M. Bakker 

**Uitvoerende organisatie(s) (Consortium)** Akzo Nobel Base Chemicals B.V. (ir. R.R. Saal, 020-4196163) TNO NITG (drs. R.A.A. Hetterschijt, 030-2564704) Tauw B.V. (ir. L.M.M. Bakker, 0570-699622) 

**Uitgever** CUR/SKB, Gouda 

**Samenvatting** Langzame nalevering van verontreinigingen vanuit zinklagen, slecht doorstroomde bodemlagen, organisch koolstof en kleimineralen beperkt de sanerende werking van pump&treat saneringen. In het RESTRISK project is aangetoond dat het onttrekken van geringe hoeveelheden grondwater afdoende is om de fysische en chemische processen die aan die nalevering ten grondslag liggen juist in stand te houden. Dit besef en daarop afgestemde onttrekkingsstrategie wordt smart pump&treat genoemd. Een hoge natuurlijke grondwaterstroming als drijvende kracht achter de verspreiding van verontreinigingen staat een brede toepassing van smart pump&treat in de weg. Door schoon grondwater om te leiden over de verontreinigde locatie wordt deze drijvende kracht weggenomen en kan smart pump&treat zonder verspreidingsrisico's worden geïmplementeerd. In feite wordt het saneringssysteem losgekoppeld van het beheerssysteem. Voor de locatie van Akzo Nobel betekent dit dat het saneringsdebiet gereduceerd wordt van 420 m^3 /dag naar 120 m^3 /dag. Hiertoe dient dan wel circa 650 m^3 /dag schoon grondwater te worden omgeleid. Dat dit in een significante besparing in de zuiveringskosten en daarmee saneringskosten resulteert is evident. Dit rapport doet verslag van het ontwerptraject voor het smart pump&treat systeem van Akzo Nobel, maar geeft ook algemene richtlijnen voor het ontwerp van zo'n systeem op een andere locatie. 

**Trefwoorden Gecontroleerde termen: Vrije trefwoorden:** in-situ bodemsanering, kosteneffectiviteit, pump&treat, verspreiding 

**Titel project Projectleiding** Implementatie van smart pump&treat Nederlands Instituut voor Toegepaste Geowetenschappen TNO (drs. R.A.A. Hetterschijt, tel. 030-2564704) 

Dit rapport is verkrijgbaar bij: CUR/SKB, Postbus 420, 2800 AK Gouda 

##### I 


##### II 


#### INHOUD 

##### SAMENVATTING V 

Hoofdstuk 1 INLEIDING 1 1.1 Kader 1 1.2 Probleem en doelstelling 1 1.3 Leeswijzer 2 

Hoofdstuk 2 GRONDSLAGEN VOOR DIMENSIONERING VAN SMART PUMP&TREAT3 2.1 Inleiding 3 2.2 Achtergronden van 'smart' pump&treat 3 2.3 Manipuleren van de grondwaterstroming 5 2.3.1 Principe 5 2.3.2 Dimensionering van het manipulatiesysteem 6 2.3.3 Dimensionering van het saneringssysteem 12 2.3.4 Vertaling naar locatiespecifiek ontwerp 14 2.4 Conclusies 15 

Hoofdstuk 3 ONTWERP 17 3.1 Inleiding 17 3.2 Ontwerpsystematiek 18 3.2.1 Methode en uitgangspunten 18 3.2.2 Opzet grondwatermodel 19 3.3 Geohydrologisch ontwerp manipulatie 25 3.4 Geohydrologisch ontwerp sanering 31 3.5 Sanerende werking 31 3.5.1 Opzet stoftransportmodel en doorbraakcurves 32 3.5.2 Resultaten 33 3.6 Effecten op de omgeving 35 3.6.1 Inleiding 35 3.6.2 Verdrogingsgevoelige vegetatie 36 3.6.3 Beïnvloeding beheerssysteem Budelco 37 3.6.4 Verstopping als praktisch knelpunt bij de implementatie van smart pump&treat 39 

Hoofdstuk 4 ROBUUSTHEID ONDER DYNAMISCHE OMSTANDIGHEDEN 41 4.1 Inleiding 41 4.2 Systeembeschrijving 41 4.2.1 Kwantificering van de dynamiek 42 4.2.2 Interpretatie 44 4.3 Bepaling van de 'lekterm' 47 4.4 Conclusies en aanbevelingen voor monitoring 48 

Hoofdstuk 5 CONCLUSIES EN AANBEVELINGEN 51 5.1 Conclusies 51 5.2 Aanbevelingen 52 

 LITERATUUR 53 

Bijlage A GEMETEN STOFCONCENTRATIES OP AKZO NOBEL TERREIN 

##### III 


Bijlage B BEHEERSCONTOUR 

Bijlage C VIJF REALISATIES KLEIDIKTE 

Bijlage D GRONDWATERAANVULLING OP HET AKZO NOBEL TERREIN 

Bijlage E STIJGHOOGTES ALS GEVOLG VAN MANIPULATIE EN SANERINGSSYSTEEM 

Bijlage F BEHEERSENDE WERKING SMART PUMP&TREAT SYSTEEM 

Bijlage G MODELINVOER VERONTREINIGINGSSITUATIE 

Bijlage H DOORBRAAKCURVEN TETRA, PER, CHLOROFORM EN CFK 

Bijlage I CONTOURKAARTEN VERDROGINGSSITUATIE 

Bijlage J OVERZICHT PERIODIEK GEMETEN STIJGHOOGTEN 

Bijlage K VERGELIJKING VAN HET TNO MODEL MET HET TAUW MODEL OP BASIS VAN STIJGHOOGTEN 

Bijlage L NEERSLAGEN VERDAMPINGSGEGEVENS, KNMI 

Bijlage M STROOMBANEN T.G.V. DYNAMICA IN NEERSLAG 

Bijlage N STROOMBANEN IN WORST CASE NEERSLAGSITUATIE 

##### IV 


#### SAMENVATTING 

 Implementatie van smart pump&treat 

_Kader_ Binnen het NOBIS-project Restrisk [Hetterschijt et al., 1998] is het concept 'smart pump&treat' uitgewerkt als kosteneffectief alternatief voor (stagnerende) grondwatersaneringen (zie figuur I-1). 

Fig. I-1. Niet-evenwichtssorptie als oorzaak van stagnatie. 

Verspreiding van verontreinigingen door hoge natuurlijke grondwaterstroming staat grootschalige implementatie van smart pump&treat in de weg. Omleiden van schoon grondwater over de verontreinigde locatie kan dit knelpunt ondervangen. In feite wordt zo de beheersing van de verontreiniging door een apart systeem van onttrekkingen en injectiepunten verzorgd (zie figuur I-2). 

_Doelstelling_ Dit project richt zich op het demonstreren van de werking en de robuustheid van het systeem op een voormalige locatie van Akzo Nobel om de bekendheid en het draagvlak voor deze oplossingsrichting te vergroten. In dit rapport wordt zowel een generieke evaluatie van het concept van omleiden en smart pump&treat uitgewerkt én de robuustheid van dit systeem voor de voormalige locatie van Akzo Nobel gedemonstreerd. Hiermee hopen wij voldoende handvatten te bieden voor toepassing van smart pump&treat in de praktijk. 

_Algemene bevindingen_ Door toepassing van een grondwater-manipulatiesysteem is het mogelijk de stijghoogtegradiënt tot 10% van de oorspronkelijke gradiënt te reduceren. De drijvende kracht achter de verspreiding wordt hiermee bijna volledig weggenomen. Het manipulatiesysteem bestaat dan bij voorkeur uit meerdere onttrekkingsputten stroomopwaarts en meerdere injectieputten stroomafwaarts van de verontreinigde locatie. Het aantal sets van onttrekking/infiltratieputten neemt toe wanneer ingespeeld moet worden op een sterk heterogene bodemopbouw (zoals bij de voormalige locatie van Akzo Nobel). Het saneringssysteem bestaat bij voorkeur uit meerdere onttrekkingsputten. Vanuit het oogpunt 'sanerende werking' zouden deze putten evenredig verspreid dienen te worden over de verontreiniging. Vanuit het oogpunt 'beheersing door een minimaal onttrekkingsdebiet' zouden 

##### V 


deze putten in het benedenstroomse deel van de verontreiniging geplaatst dienen te worden. Deze laatste, de beheersing met een minimaal debiet, is hier ook het maatgevende criterium. Op basis van de lengte en vorm (lengte/breedte) van de verontreiniging, de stijghoogtegradiënt ofwel verhang op de locatie en de transmissiviteit is een ruwe schatting te maken van het volume om te leiden schoon grondwater om smart pump&treat mogelijk te maken. 

 natural groundwater flow 

 treatment unit above the extraction well 

 contaminant dissolved 

 natural groundwater flow 

 pipeline 

Fig. I-2. Traditionele pump&treat (a) en smart pump&treat met omleiding van grondwater (b). 

_Ontwerp smart pump&treat voor voormalige locatie van Akzo Nobel_ Via een geautomatiseerde optimalisatie procedure gebaseerd op MODMAN [GeoTrans, 1992] en Lindo [Schrage, 1991] is een gecombineerd systeem ontworpen voor manipulatie van de grondwaterstand en sanering door smart pump&treat. De randvoorwaarde hierbij was dat de chloroform verontreiniging die maatgevend is voor de verspreiding, niet verder mag verspreiden. De optimalisatie van het systeem vond plaats door het saneringsdebiet te minimaliseren. De vrijheidsgraden bij de optimalisatie waren de plaats van manipulatieen saneringsputten en de debieten per put. Het systeem dat gevonden werd door deze optimalisatie bestaat uit 7 saneringsputten, waarvan er 5 in de tussenzandlaag staan en 2 in het watervoerend pakket gecombineerd met 10 manipulatielocaties (5 injectieen 5 onttrekkingslocaties), waarvan er 4 in de tussenzandlaag en 6 in het watervoerend pakket staan. Het totale saneringsdebiet bedraagt tussen de 113 en 137 m^3 /dag hetgeen 30 tot 35% is van het geschatte debiet (420 m^3 /dag) dat in de oorspronkelijke variant werd onttrokken en langs de zuivering moest worden geleid. Het debiet dat nodig is voor het manipuleren om verspreiding te beperken, bedraagt 570-670 m^3 /dag. Middels een eenvoudige transportmodellering is geschat dat het genoemde saneringssysteem 50 g tetrachloormethaan, 200 g chloroform, 200 g CFK112 en 20 g perchloorethyleen per dag verwijdert. 

##### VI 


_Robuustheid bij dynamiek_ Analyse van het stijghoogteverloop in de bodem gedurende 1 jaar laat zien dat er sprake is van dynamiek in het grondwatersysteem: stijghoogtegradiënten nemen toe en af en stromingsrichtingen veranderen. In de zomer en nazomer nemen de stijghoogtegradiënten op de locatie toe. Extra stijghoogtemetingen tonen aan dat kwel vanuit het kanaal ten zuiden van de locatie de dynamiek niet kan veroorzaken. In het 'worst case' geval waarbij een halfjaarlijkse natte periode (100% meer neerslag) 30 jaar aaneengesloten voortduurt, zijn de grondwaterverplaatsingen nog maar gering. Na een worst case periode van 6 jaar vallen de verplaatsingen nog juist binnen de marge van het ontwerp. Op basis hiervan wordt geconcludeerd dat seizoenale effecten een verwaarloosbare invloed hebben op het functioneren van het ontworpen systeem. De verontreiniging wordt beheerst en verplaatsingen zijn gering, zelfs in een 'worst case' situatie. Monitoring van stijghoogten na installatie moet continu inzicht geven in de stromingsrichtingen om vervolgens door inregeling van het systeem de beheersing van de verontreiniging continu te kunnen waarborgen. 

_Conclusies en aanbevelingen_ Aangetoond is dat het onttrekkingsdebiet **niet** bepalend is voor de sanerende werking [Hetterschijt en Te Stroet, 1998]. Het meest _efficiënte_ pump&treat saneringssysteem bestaat dan ook uit een verzameling van geringe onttrekkingen (10 m^3 /dag) verspreid over de verontreiniging, ook wel _smart_ pump&treat genoemd. 

Door schoon grondwater om te leiden over een verontreinigde locatie, het zogenaamde 'manipuleren' (stroomopwaarts onttrekken en stroomafwaarts injecteren), wordt de verontreiniging beheerst: manipulatie reduceert de stijghoogtegradiënt tot 10% van de oorspronkelijke gradiënt. De drijvende kracht achter de verspreiding wordt hiermee bijna volledig weggenomen. Dit maakt een veilige toepassing van smart pump&treat ook in goeddoorlatende watervoerende pakketten mogelijk, wanneer afbraak te gering is om verspreiding te beperken door geringe onttrekkingen in samenhang met natuurlijke afbraak. Geautomatiseerd optimaliseren van het manipulatieen saneringssysteem met MODMAN/Lindo maakt een objectieve en snelle keuze van de plaats van onttrekkingsen injectieputten en het debiet mogelijk. De verwachting bestaat, dat optimalisatie van pump&treat naar smart pump&treat een sterke reductie van het te behandelen volume grondwater tot gevolg heeft, waardoor zuiveringskosten een factor 3 tot 5 goedkoper worden. 

Aanbevolen wordt om aandacht te besteden aan puttenverstoppingproblematiek bij injectieputten van het manipulatiesysteem. Mogelijkheid tot injectie is namelijk een voorwaarde voor het toepassen van manipulatie. Daarnaast blijkt het ontwerpdebiet per put gevoelig voor onzekerheid als gevolg van bodemheterogeniteit. Dit is te ondervangen door het systeem bij installatie in te regelen op stijghoogtemetingen. Aanbevolen wordt hiervoor richtlijnen op te stellen. Ten slotte wordt aanbevolen te onderzoeken of vrachtverwijdering door het saneringssysteem in de optimalisatieprocedure kan worden opgenomen waar nu alleen naar debiet is geoptimaliseerd. 

##### VII 


##### VIII 


##### HOOFDSTUK 1 

#### INLEIDING 

1.1 **Kader** 

Binnen het NOBIS-project Restrisk [Hetterschijt en Te Stroet, 1998] is het concept 'smart pump&treat' uitgewerkt als ondervanging van stagnatie van grondwatersaneringen. Smart pump&treat behelst het saneren van bodem en grondwater door met een gering debiet grondwater te onttrekken, dit ter onderscheiding van traditionele pump&treat, waarbij relatief veel grondwater wordt onttrokken. De onderbouwing voor deze manier van saneren is de bevinding dat trage natuurlijke processen zoals diffusie, desorptie en oplossen van verontreinigingen de voortgang van een pump&treat sanering bepalen, niet de stroomsnelheid van het grondwater zoals voorheen wel werd verondersteld. Modelberekeningen toonden aan dat een sanering door middel van weinig grondwater onttrekken zeer effectief kan verlopen [Hetterschijt en Te Stroet, 1998]. Het behoeft weinig argumentatie dat een reductie van het te onttrekken verontreinigde grondwater in een aanzienlijke besparing op de saneringskosten resulteert (zuiveringskosten!). Een beperking voor de toepassing van dit concept is de verspreiding van verontreinigingen als gevolg van de natuurlijke stroming. Bij een grote natuurlijke grondwaterstroming lijkt een groot onttrekkingsdebiet noodzakelijk om de verontreiniging te beheersen, iets wat vanuit saneringsperspectief niet noodzakelijk is. Een methode om dit knelpunt te ondervangen is het 'omleiden' van schoon grondwater over de verontreinigde locatie. Hiermee wordt de drijvende kracht van de verspreiding weggenomen en kan de verontreinigingen toch door middel van smart pump&treat worden gesaneerd. Dit gecombineerde systeem van manipulatie van de grondwaterstroming en smart pump&treat kortweg smart pump&treat genoemd is als alternatieve aanpak voorgesteld aan Akzo Nobel voor de sanering van een met chloorfluorkoolwaterstoffen (cfk's) en gechloreerde koolwaterstoffen (ckw's) verontreinigde locatie in Weert. In het SKB-project waarvan dit rapport verslag doet, wordt dit concept op generieke wijze uitgewerkt en specifiek voor de genoemde voormalige locatie van Akzo Nobel. Het voor de Akzo Nobel locatie uitgewerkte concept zal daadwerkelijk geïnstalleerd worden, waarbij de prestatie van het systeem zal worden gemonitoord en geëvalueerd. Door het in een rapport bundelen van de uitwerking van generieke aspecten en de toepassing van het concept op de voormalige locatie van Akzo Nobel worden voldoende aanknopingspunten aangereikt voor het toepassen van dit concept op andere locaties. 

1.2 **Probleem en doelstelling** 

Verspreiding van verontreinigingen door hoge natuurlijke grondwaterstroming staat grootschalige implementatie van smart pump&treat in de weg. Omleiden van schoon grondwater over de verontreinigde locatie kan dit knelpunt ondervangen. In feite wordt zo de beheersing van de verontreiniging door een apart systeem van onttrekkingen en injectiepunten verzorgd. In een eerdere beknopte studie is de haalbaarheid van een dergelijk systeem op een voormalige locatie van Akzo Nobel onderzocht [Hetterschijt en Te Stroet, 1998]. Deze studie gaf echter geen handvatten voor het ontwerp van zo'n systeem op andere locaties. Bovendien was de haalbaarheidsstudie niet gericht op het vervaardigen van een gedetailleerd ontwerp voor de voormalige Akzo Nobel locatie, waardoor nog niet tot implementatie kon worden overgegaan. Het belang van het demonstreren van de werking en de robuustheid van het systeem op een locatie is het vergroten van de bekendheid en draagvlak voor deze oplossingsrichting als alternatief wanneer biologische in-situ sanering niet mogelijk of niet kosteneffectief is. Dit SKB project richt zich dan ook zowel op een generieke evaluatie van het concept van omleiden en smart pump&treat én op het demonstreren van de robuustheid van dit systeem voor 


de voormalige locatie van Akzo Nobel. Het smart pump&treat systeem voor de voormalige locatie van Akzo Nobel zal daartoe voorafgaand en tijdens installatie en operatie worden geëvalueerd op robuustheid. Met het combineren van de generieke uitwerking en een voorbeeld uit de praktijk hopen wij voldoende handvatten te bieden voor toepassing van dit saneringsconcept op andere verontreinigde locaties. 

1.3 **Leeswijzer** 

Dit tweede deelrapport van het SKB-project bevat de resultaten van 'stap 1' zoals beschreven in het basisprojectplan (ontwerp omleiding en saneringssysteem). Het rapport is zodanig opgezet dat het na het opnemen van de resultaten van stap 2 (evaluatie) een volledig en beknopt eindrapport vormt. In hoofdstuk 2 zijn dan ook de resultaten van stap 0, principe en generieke aspecten van smart pump&treat met omleiding, samengevat. De resultaten van fase 0 zijn eerder meer uitgebreid gerapporteerd [Berendrecht, 1999] in een TNO rapport. In hoofdstuk 2 worden algemene richtlijnen gegeven voor het ontwerp van een gecombineerd systeem van omleiden en smart pump&treat. Het hoofdstuk is dan ook essentieel voor partijen die deze saneringsoplossing willen toepassen. In de volgende 2 hoofdstukken (3 en 4) wordt ingegaan op het specifieke ontwerp voor een voormalige locatie van Akzo Nobel. In hoofdstuk 3 zal het ontwerp van het omleidingssysteem en het saneringssysteem worden toegelicht, waarbij de ontwerpmethode, de werking van beide systemen en de effecten daarvan op de omgeving inzichtelijk worden gemaakt. In hoofdstuk 4 zal aandacht worden besteed aan de robuustheid van het ontworpen systeem onder dynamische omstandigheden. Hieruit volgen richtlijnen voor monitoring van het systeem om de robuustheid hiervan in de praktijk te evalueren. In hoofdstuk 5 worden conclusies en aanbevelingen samengevat. 


##### HOOFDSTUK 2 

#### GRONDSLAGEN VOOR DIMENSIONERING VAN SMART PUMP&TREAT 

2.1 **Inleiding** 

In dit rapport wordt verslag gedaan van de implementatie van smart pump&treat op een voormalige locatie van Akzo Nobel als kosteneffectief en milieuvriendelijk alternatief van een traditionele pump&treat. De aandacht gaat daarbij voornamelijk uit naar ontwerp en implementatie van het zogenaamde manipulatiesysteem dat smart pump&treat op de desbetreffende locatie mogelijk maakt. In dit hoofdstuk zal echter ook worden ingegaan op de achtergronden van smart pump&treat zelf. Tenslotte worden in dit hoofdstuk aanknopingspunten geboden voor het ontwerpen van smart pump&treat met manipulatie. 

2.2 **Achtergronden van 'smart' pump&treat** 

De 'traditionele' techniek voor het saneren van verontreinigde locaties is het doorspoelen van de bodem door grondwater te onttrekken (pump&treat), al dan niet in combinatie met het ontgraven van hot spots. In de jaren 80 werd duidelijk dat deze aanpak minder veelbelovend was dan in eerste instantie werd verwacht: vele grondwatersaneringen bleken te stagneren [Keeley, 1989; Haley et al., 1991]; [Freeze en Cherry, 1989]; [Mackey en Cherry, 1989]. Dit wil zeggen dat na een aanvankelijk snelle daling van de verontreinigingsconcentratie van het influent, de concentratie op een niveau blijft hangen dat boven het vooraf gestelde saneringsdoel ligt. De sanering duurt daardoor langer dan verwacht, waardoor de saneringskosten hoger uitvallen dan geraamd. Het onttrekken van grote volumes grondwater kan de sanering niet versnellen. Hetterschijt en Te Stroet [Hetterschijt en Te Stroet 1998] toonden aan dat een gering onttrekkingsdebiet van enkele kubieke meters per dag zelfs even effectief kan zijn als een debiet van honderden kubieke meters per dag. Wanneer hiermee bij het ontwerp van een pump&treat sanering rekening wordt gehouden, kan meer kosteneffectief worden gesaneerd. Een belangrijk voordeel hiervan is de enorme kostenbesparing op de zuivering van het onttrokken grondwater. Daarnaast zal door een lager onttrekkingsdebiet de verlaging van de grondwaterstand gering zijn wat in het kader van de verdrogingsproblematiek gunstig is. 

De oorzaak van de genoemde stagnatie is, dat het verloop van een pump&treat sanering wordt gelimiteerd door bepaalde niet-evenwichtsprocessen in de bodem. Van een dergelijk proces is sprake wanneer bijvoorbeeld slecht doorlatende lagen naast goed doorstroomde bodemlagen voorkomen (zie figuur 1). De verontreinigingen zijn in de loop der jaren in de lagen met geringe doorlatendheid gediffundeerd. Na een periode van grondwater onttrekken is de verontreiniging verwijderd uit de goed doorstroomde bodemlagen, ook wel mobiele zones genoemd. Er ontstaat nu een concentratiegradiënt tussen deze mobiele zones en de slecht doorlatende lagen, ook wel immobiele zones genoemd. Door deze gradiënt komen processen als diffusie en desorptie op gang. Deze processen kunnen echter niet worden versneld door de bodem te blijven doorspoelen, immers de concentratiegradiënt is al tot stand gekomen. Vaak werd de verwijdering van verontreiniging uit de mobiele zones als maatgevend voor de saneringsduur gesteld. Dit blijkt echter te optimistisch: als de verontreiniging uit de goed doorlatende lagen is verwijderd, blijven de immobiele zones langzaam naleveren. 

Niet-evenwichtsprocessen spelen zich ook op andere schaalniveaus af. Niet alleen op macroschaal maar ook op micro schaal: kleine deeltjes organische koolstof fungeren bijvoorbeeld ook als immobiele zones. De verontreinigingen moeten hierbij van de 'harde' kern van het koolstofdeeltje naar de rand diffunderen alvorens ze eenvoudiger desorberen en in het 


grondwater beschikbaar komen voor de onttrekking. Ook het oplossen van verontreiniging uit NAPL's (non-aqueous phase liquids) is zo'n niet-evenwichtsproces. 

Fig. 1. Niet-evenwichtssorptie als oorzaak van stagnatie. 

In het algemeen kan worden gesteld dat het naast elkaar voorkomen van mobiele en immobiele zones in de ondergrond niet-evenwichtsprocessen in de hand werken en daarmee stagnatie van pump&treat (en andere) saneringstechnieken. 

Het concept van _smart_ pump&treat houdt rekening met niet-evenwichtsprocessen. Het concept is ontwikkeld vanuit de gedachte dat bij optreden van niet-evenwichtsprocessen door intermitterend grondwater te onttrekken een zelfde resultaat kan worden verkregen als door continu te onttrekken [Griffioen en Hetterschijt, 1998]. Wanneer na een korte periode van onttrekken de verontreiniging uit de mobiele zones zijn verwijderd wordt de onttrekking stopgezet, deze heeft immers geen zin meer. Tijdens de 'rustperiode' blijft verontreiniging uit de immobiele zones naar de mobiele zones diffunderen. Na verloop van tijd is de concentratie in de goed doorstroomde lagen dermate toegenomen, dat het doorspoelen van de bodem weer de moeite loont. Door zo afwisselend korte perioden actief de goed doorstroomde zones te doorspoelen en vervolgens de natuurlijke processen te laten verlopen wordt hetzelfde saneringsresultaat behaald. Daarbij wordt echter veel minder grondwater onttrokken. 

In het kader van het NOBIS-project Restrisk is onderzoek gedaan naar de meest effectieve wijze van intermitterend saneren [Hetterschijt en Te Stroet, 1998]. Daarbij is gekeken naar de invloed van de frequentie van de pomp&pauze-cyclus, het onttrekkingsdebiet en de verhouding tussen de duur van de pompperiode en pauzes. Het verhogen van de frequentie had een verhoogde effectiviteit tot gevolg (meer massa werd verwijderd), terwijl evenveel grondwater werd onttrokken. Dit is toe te schrijven aan het feit dat de concentratiegradiënt tussen mobiele en immobiele zone bij een te lange pauze dermate is afgenomen, dat deze limiterend werd op de nalevering door diffusie en desorptie. De rustperiode dient dus niet zo lang te duren, dat de nalevering vanuit immobiele zones door diffusie en desorptie niet maximaal is. Het verhogen van het onttrekkingsdebiet resulteerde niet in een toename van de effectiviteit van de pump&treat sanering. Het gelijktijdig verhogen van de frequentie van de pomp&pauze cyclus en het gelijktijdig verlagen van het onttrekkingsdebiet zijn de belangrijkste optimalisaties die tot efficiency verbetering van 


intermitterend saneren leiden. Deze optimalisatie kan nog verder worden doorgevoerd door de duur van de pauze naar 0 dagen te verkorten en het debiet verregaand te verlagen. Deze resultaten worden bevestigd door Harvey [Harvey et al. 1994], die op een vergelijkbare wijze hebben aangetoond, dat continu onttrekken met een laag debiet efficiënter is dan intermitterend onttrekken. Resumerend wordt gesteld dat de grondwatersnelheid die door middel van het debiet wordt opgelegd, niet bepalend is voor de verwijdering van verontreiniging uit bodem en grondwater; deze dient aan te sluiten bij de snelheid van de massa-overdracht van de immobiele naar de mobiele zone om zo efficiënt mogelijk te saneren. In de praktijk betekent dit dat het onttrekken van enkele kubieke meters grondwater per dag voldoende doorstroming levert om effectief te saneren. 

2.3 **Manipuleren van de grondwaterstroming** 

2.3.1 _Principe_ Een knelpunt bij grootschalige implementatie van smart pump&treat sanering middels kleine onttrekkingen is de beheersing van de verontreiniging. Dit knelpunt wordt ondervonden wanneer de natuurlijke grondwaterstroming groot is en verspreiding van stoffen niet door natuurlijke afbraak (NA) wordt geremd. Voor het beheersen van de verontreiniging bij een hoge natuurlijke achtergrondstroming in een watervoerend pakket moet vele malen meer grondwater worden onttrokken dan voor de sanerende werking strikt noodzakelijk is. 

 natural groundwater flow 

 treatment unit above the extraction well 

 contaminant dissolved 

 natural groundwater flow 

 pipeline 

Fig. 2. Traditionele pump&treat (a) en smart pump&treat met omleiding van grondwater (b). 

Om in een situatie met een hoge achtergrondstroming en geringe mogelijkheden voor natuurlijke afbraak smart pump&treat toe te passen, is het opheffen van de natuurlijke grondwaterstroming 


ter plaatse van de locatie noodzakelijk. Dit kan door het grondwater dat bovenstrooms van de saneringslocatie komt aanstromen te onttrekken en dit benedenstrooms weer te injecteren. Door op deze manier schoon grondwater om te leiden, wordt de drijvende kracht van de verspreiding van de verontreiniging weggenomen. In figuur 2 is het verschil te zien tussen de traditionele pump&treat, waarbij de verontreiniging wordt beheerst door het onttrekken van 'vies' grondwater (rood) en smart pump&treat met omleiden van grondwater, waarbij wordt beheerst door het omleiden van 'schoon' grondwater (blauw). 

Het grote voordeel van het omleiden van grondwater om de verspreiding van verontreinigingen te voorkomen, is dat het grondwater dat wordt onttrokken schoon is en niet gezuiverd hoeft te worden. Het wegnemen van de natuurlijke grondwaterstroming op een verontreinigde locatie kan worden gecontroleerd aan de hand van het stijghoogteverloop op de locatie. Als gevolg van de natuurlijke grondwaterstroming vertoont de stijghoogte een verhang of gradiënt op de locatie. Het omleiden van grondwater heeft tot gevolg dat er geen stroming meer plaatsvindt op de locatie, waardoor het oorspronkelijke verhang van de stijghoogte wordt 'vlakgetrokken' (zie figuur 3). 

 omleiding door manipulatiesysteem 

 saneringssysteem 

 locatie 

 Q Q 

Fig. 3. Vlaktrekken van de stijghoogtegradiënt door middel van een grondwater manipulatiesysteem. 

Door het omleiden wordt het zwaartepunt van de beheersfunctie verplaatst van de onttrekkingsputten in de verontreiniging naar de onttrekkingsen infiltratieputten in schoon grondwater. 

2.3.2 _Dimensionering van het manipulatiesysteem_ De dimensionering van het manipulatiesysteem hangt af van verschillende factoren. Hierbij gaat het voornamelijk om omgevingsfactoren, zoals de grondwaterstroming, doorlatendheid van de ondergrond en omvang van de verontreiniging. Daarnaast spelen ook de eisen die aan het systeem worden gesteld mee. Voor het opstellen van dimensioneringsgrondslagen voor het manipulatiesysteem is inzicht in de invloed van genoemde factoren op de werking van het systeem noodzakelijk. 


Door Berendrecht [Berendrecht, 1999] is onderzoek gedaan naar de meest invloedshebbende factoren voor het manipulatieen saneringssysteem (zie ook paragraaf 2.3.3). Aan de hand van een 'referentieberekening' voor een fictieve verontreiniging met een oppervlak van 200 bij 100 meter in een watervoerend pakket met een transmissiviteit van 1000 m^2 /dag wordt in paragrafen 2.3.2 en 2.3.3 uitgelegd hoe het manipulatieen saneringssysteem er in algemene zin uit ziet. Deze paragrafen zijn bedoeld om inzicht te geven in het principe van beheersing van een verontreiniging door omleiden ofwel manipuleren van schoon grondwater. In paragraaf 2.3.4 wordt toegelicht hoe men aan de hand van de in paragrafen 2.3.2 en 2.3.3 gepresenteerde grafieken tot een eerste aanzet voor een locatiespecifiek ontwerp voor manipuleren kan komen. 

_Achtergrondstroming_ Afhankelijk van de natuurlijke stijghoogtegradiënt en de gewenste stijghoogtegradiënt op de locatie zal het debiet voor het manipuleren variëren. Wanneer de natuurlijke gradiënt sterk moet worden teruggebracht zal de capaciteit van het manipulatiesysteem ook groter moeten zijn dan wanneer deze 'gradiëntseis' kleiner is. De verhouding tussen de reductie van de gradiënt en het benodigde debiet is af te lezen uit figuur 4. 

In de figuur is duidelijk de toename van het benodigde manipulatiedebiet te zien bij toenemende reductie van de achtergrondstroming. Vooral wanneer de gradiënt wordt gereduceerd tot minder dan 10% van de oorspronkelijke gradiënt ( _ieis/i_ =0,1), neemt het benodigde debiet zeer sterk toe. Dit blijkt des te meer als men zich realiseert dat de relatieve gradiëntseis is uitgezet op logaritmische schaal. Ook neemt bij een gegeven gradiëntsreductie het benodigde manipulatiedebiet recht evenredig toe met de achtergrondstroming (dit zijn de verschillende curves). 

 0 

 200 

 400 

 600 

 800 

 1000 

 1200 

 1400 

 1600 

 1800 

 2000 

 0.001 0.01 0.1 1 

**i** (^) **eis /i (-) Q (m 3 /d)** (^) 1.00E-04 2.00E-04 4.00E-04 6.00E-04 8.00E-04 1.00E-03 Fig. 4. Relatie tussen de reductie van de achtergrondstroming en het benodigde manipulatiedebiet voor verschillende waarden van de achtergrondstroming. _Factor achtergrondstroming: Om dus bij een tweemaal zo hoge achtergrondstroming een zelfde reductie te creëren, is ook tweemaal zoveel manipulatiedebiet nodig. Aantal manipulatieputten_ 


In de referentiesituatie bestaat het manipulatiesysteem uit een _set_ van 2 putten die symmetrisch ten opzichte van de locatie zijn geplaatst. Bovenstrooms bevindt zich de onttrekkingsput en benedenstrooms de infiltratieput. Zo'n _set_ van een infiltratie én een onttrekkingsput wordt in de figuren en tekst verder kortweg 'één manipulatieput' genoemd. Door meerdere sets van manipulatieputten te gebruiken kan het benodigde _manipulatie_ debiet enorm worden gereduceerd. De reden is gelegen in het feit dat met meerdere putten het realiseren van een reductie van de gradiënt localer kan worden afgestemd met minder inspanning. Deze reductie ligt in de orde van enkele tientallen procenten en neemt toe bij toenemende strengheid van de gradiëntseis (zie figuur 5). Hierbij geldt wel dat het rendement van elke extra put afneemt. 

 0 

 0.1 

 0.2 

 0.3 

 0.4 

 0.5 

 0.6 

 0.7 

 0.8 

 0.9 

 1 

 0 0.1 0.2 0.3 0.4 0.5 0.6 

**i** (^) **eis/i (-) Q**^ **n /Q (-) 1** (^) 2 putten 3 putten 4 putten 5 putten Fig. 5. Verhouding tussen het manipulatiedebiet bij gebruik van meerdere putten en het debiet bij gebruik van één put. Om bijvoorbeeld de stijghoogtegradiënt met een factor 10 terug te brengen behoeft met 1 put extra reeds 40% minder onttrokken te worden. Door drie putten te gebruiken zal het totale debiet met 50% afnemen. De invloed van de derde put is dus aanzienlijk kleiner dan die van de tweede put. Tevens blijkt dat de invloed van een extra put groter wordt bij toenemende strengheid van de gradiëntseis. Een ander gevolg van het gebruik van meerdere putten is dat de gemiddelde afstand van de put tot de locatie afneemt waardoor de invloed op de stijghoogten in de omgeving vermindert. _Factor aantal putten: Een extra manipulatieput sorteert steeds minder effect._ De conclusie dat een extra manipulatieput steeds minder effect sorteert, is ook via een andere weg te verkrijgen. Daarbij wordt gekeken naar het gradiëntenveld op de locatie, zoals gerealiseerd door het manipulatiesysteem, en de eisen die aan de gradiënt gesteld worden. Als gevolg van het gebruik van meerdere putten, zal deze gradiëntseis exacter de randen van de locatie volgen. In figuur 6 is te zien dat bij gebruik van 5 putten, de beoogde gradiëntseis bijna geheel op de locatierand ligt. Hieruit kan worden geconcludeerd dat het in deze situatie nauwelijks meer zin heeft om nog meer putten bij te plaatsen. 


 -120 -100 -80 -60 -40 -20 0 20 40 60 80 100 120 -70 

 -50 

 -30 

 -10 

 10 

 30 

 50 

 70 

 x (m) 

 y (m) 

 2 putten 

 -120 -100 -80 -60 -40 -20 0 20 40 60 80 100 120 -70 

 -50 

 -30 

 -10 

 10 

 30 

 50 

 70 

 x (m) 

 y (m) 

 3 putten 

 -120 -100 -80 -60 -40 -20 0 20 40 60 80 100 120 -70 

 -50 

 -30 

 -10 

 10 

 30 

 50 

 70 

 x (m) 

 y (m) 

 4 putten 

 -120 -100 -80 -60 -40 -20 0 20 40 60 80 100 120 -70 

 -50 

 -30 

 -10 

 10 

 30 

 50 

 70 

 x (m) 

 y (m) 

 5 putten 

Fig. 6. Gradiëntenvelden bij gebruik van meerdere manipulatieputten. 

Om een indruk te geven van de putlocaties, zijn deze in figuur 7 voor de verschillende gradiëntseisen per plaatje en verschillend aantal putten in vier afzonderlijke plaatjes weergegeven. Hierin is duidelijk te zien dat bij een gegeven gradiëntseis de optimale putconfiguratie de vorm van een parabool heeft (voor meer dan 2 putten). Deze parabool neemt, bij toenemende strengheid van de gradiëntseis, toe in lengte en breedte. Zoals verwacht, blijkt in deze uniforme, homogene situatie het puttenveld dus hoofdzakelijk voor (onttrekkingen) en achter (infiltraties) de saneringslocatie te liggen. 

_Heterogeniteit van de ondergrond_ Een onzekere factor bij het ontwerp van een manipulatiesysteem is de mate van heterogeniteit van de ondergrond. Door het negeren van deze heterogeniteiten kunnen fouten in het uiteindelijke ontwerp van het manipulatiesysteem worden gemaakt. 

Om na te gaan wat die invloed precies is, zijn voor dit deel van het onderzoek een aantal realisaties van een sterk heterogene ondergrond gesimuleerd waarmee de berekeningen zijn uitgevoerd. Uit de resultaten blijkt allereerst dat het uiteindelijke vereiste manipulatiedebiet in de heterogene situatie hoger is dan wanneer van een homogeen pakket wordt uitgegaan. Daarnaast zijn in sterk heterogene ondergronden meerdere manipulatieputten nodig om op de locatie aan de gestelde eis te voldoen. Dat is te verwachten, omdat er geldt dat hoe meer putten er worden gebruikt, des te localer er kan worden afgestemd op de gestelde eis. Eén set manipulatieputten is bij een sterk heterogene ondergrond dan ook niet in staat om 'in te spelen' op de ruimtelijke variaties. Wanneer er steeds meer putten worden gebruikt, nadert het totale benodigde debiet steeds meer tot dat wat in een situatie met homogene ondergrond nodig zou zijn. 


 -150 

 -100 

 -50 

 0 

 50 

 100 

 150 

 0 50 100 150 200 250 

 -150 

 -100 

 -50 

 0 

 50 

 100 

 150 

 0 50 100 150 200 250 

 -150 

 -100 

 -50 

 0 

 50 

 100 

 150 

 0 50 100 150 200 250 

 0.6 0.4 0.2 0.1 0.08 0.06 0.04 0.02 

 -150 

 -100 

 -50 

 0 

 50 

 100 

 150 

 0 50 100 150 200 250 

Fig. 7. Locaties van de manipulatieputten bij verschillende relatieve gradiëntseisen en verschillend aantal putten (2, 3, 4, en 5). 

Hoeveel manipulatieputten nodig zijn en waar deze putten moeten worden geplaatst, verschilt per gesimuleerde realisatie. Het totaal benodigde manipulatiedebiet neemt als gevolg van de heterogene ondergrond slechts enkele procenten toe ten opzichte van de homogene situatie, wanneer al meerdere putten worden toegepast. De verdeling van dit debiet over de putten verschilt echter wel sterk. 

 Factor heterogeniteit: Dit alles betekent dat onzekerheid in de opbouw van de ondergrond een grote invloed heeft op de juiste werking van het manipulatiesysteem. 

Op voorhand zijn de optimale putlocaties niet te voorspellen omdat de heterogeniteiten niet bekend zijn. In elke nieuwe situatie zal een optimalisatie moeten uitwijzen welke locaties de meest geschikte zijn. 

Vooruitlopend op het vervolg wordt al verwezen naar hoofdstuk 3. Hierin wordt een ontwerpsystematiek gepresenteerd die weet om te gaan met het genoemde probleem van 


heterogeniteit. Door een statistische benadering te volgen, blijkt het mogelijk te zijn om ondanks heterogeniteit toch een robuust systeem te ontwerpen. 

_Doorlatendheid van de ondergrond_ Naast de heterogeniteit van de ondergrond is ook het bepalen van de juiste doorlatendheid aan onzekerheden onderhevig. Deze onzekerheid heeft met name gevolgen voor de fluxen die door het systeem op de locatie zullen ontstaan. Als de werkelijke doorlatendheid hoger is dan de aangenomen doorlatendheid (onderschatting), zal de werkelijke gemanipuleerde flux hoger liggen dan de berekende flux. Het gevolg is dat er met teveel debiet wordt gemanipuleerd waardoor een groot deel van het verontreinigde grondwater vanaf de verontreinigingslocatie in het manipulatiesysteem terechtkomt. In het geval van een overschatting blijkt er een bepaalde marge te zijn waarbinnen er toch nog voldaan wordt aan de gestelde flux eis. Deze marge wordt kleiner naarmate de fluxeis strenger is. 

 Factor doorlatendheid: Een onjuiste inschatting van de doorlatendheid leidt er toe dat er verontreinigd grondwater in het manipulatiesysteem terecht kan komen. Een geringe onderschatting van de doorlatendheid is hierbij ongunstiger dan een overschatting. 

_Geometrie van de locatie_ Het onderzoek is uitgegaan van een rechthoekige locatie van 200x100 m. In werkelijkheid zijn er echter tal van locatieoppervlakten mogelijk. Naast bijna vierkante locaties kan er ook sprake zijn van in de richting van de stroming langgerekte locaties. Deze laatste doen zich voornamelijk voor in situaties waarin zich een verontreinigingspluim heeft ontwikkeld vanaf een bronlocatie. 

 0 

 200 

 400 

 600 

 800 

 1000 

 1200 

 1400 

 1600 

 1800 

 0.1 1 10 l/b (-) 

 Q (m 

 3 /d)^ ieis/I=0.1 ieis/I=0.2 ieis/I=0.4 

Fig. 8. Relatie tussen de geometrie van de locatie en het benodigde manipulatiedebiet voor verschillende gradiëntseisen. 

 Factor geometrie: Wanneer de lengte-breedte verhouding als uitgangspunt wordt genomen, blijkt de toename van het benodigde manipulatiedebiet het grootst te zijn wanneer de breedte groter wordt dan de lengte (zie figuur 8). 


Bij gelijkblijvende lengte-breedte verhouding neemt het manipulatiedebiet rechtevenredig toe met de lengte van de locatie. Deze constatering is van belang bij de vertaling van de resultaten uit deze studie naar praktijksituaties. Paragraaf 2.3.4 gaat hier nader op in. 

2.3.3 _Dimensionering van het saneringssysteem_ Deze paragraaf gaat in op de invloed die het manipulatiesysteem heeft op het saneringssysteem. Om tot het meest optimale _hydrologische_ ontwerp van het saneringssysteem te komen worden de locaties en debieten van de saneringsputten zodanig veranderd dat op de randen van de locatie de flux naar binnen is gericht (de verontreiniging wordt beheerst) en het totale saneringsdebiet minimaal is. De onderzochte generieke aspecten van het saneringssysteem hebben betrekking op de natuurlijke en gemanipuleerde achtergrondstroming en het aantal manipulatieen saneringsputten. 

_Mate van achtergrondstroming_ De hoogte van het benodigde saneringsdebiet wordt in sterke mate bepaald door zowel de mate van natuurlijke achtergrondstroming als de mate van gemanipuleerde achtergrondstroming. Hoe lager de achtergrondstroming wordt ten gevolge van manipulatie, des te lager het benodigde saneringsdebiet. Ten gevolge van de manipulatie kan het saneringsdebiet worden teruggebracht tot enkele procenten van het saneringsdebiet zoals dat nodig is in ongemanipuleerde stroming. Het saneringsdebiet neemt het sterkst af bij een kleine reductie van de achtergrondstroming zoals figuur 9 laat zien. 

 0 

 50 

 100 

 150 

 200 

 250 

 300 

 350 

 0.01 0.1 1 ieis/i (-) 

 Qsan 

 (m 

 3 /d) i=0.0005 i=0.0001 

Fig. 9. Invloed van gradiëntseis op saneringsdebiet voor verschillende maten van de achtergrondstroming. 

Globaal geldt dat voor een gradiëntseis die kleiner is dan 10% van de oorspronkelijke stijghoogtegradiënt, het saneringsdebiet nauwelijks meer afneemt. Praktisch betekent dit dat een extra manipulatie-inspanning geen evenredig saneringsrendement oplevert. 

 Factor achtergrondstroming: Evenals het manipulatiedebiet neemt het saneringsdebiet bij een gegeven gradiëntsreductie rechtevenredig toe met de mate van natuurlijke achtergrondstroming. 


Het systeem is ook gevoelig voor afwijkingen in het saneringsdebiet. Een te laag debiet zal er toe leiden dat een deel van de stroming de verontreinigingslocatie toch verlaat. De gevoeligheid voor deze fout neemt toe bij toenemende strengheid van de gradiëntsreductie die de manipulatieputten dienen te realiseren. Een kleinere gradiëntseis bevordert dus de robuustheid van het systeem. 

_Aantal saneringsputten_ Door meerdere putten te gebruiken kan het benodigde saneringsdebiet worden teruggebracht. Zoals figuur 10 laat zien, bedraagt deze reductie grofweg enkele tientallen procenten en hangt sterk af van de mate van gemanipuleerde stroming. 

 Factor aantal saneringsputten: Net als bij het manipulatiesysteem geldt ook hier dat de toegevoegde waarde van een extra saneringsput afneemt. 

Tot slot is in figuur 10 de totale uitstroom van de locatie aangegeven. Dit is het debiet dat na manipulatie en zonder saneringsputten de locatie verlaat. Het geldt dus als een ondergrens voor het benodigde saneringsdebiet. Slechts bij gebruik van zeer veel putten zal het saneringsdebiet dit uitstroomdebiet benaderen. 

 0 

 50 

 100 

 150 

 200 

 250 

 300 

 350 

 0.01 0.1 1 ieis/i (-) 

 Q 

 (msan 

 3 

**/d)** (^) 1 saneringsput 2 saneringsputten 3 saneringsputten 4 saneringsputten totale uitstroom Fig. 10. Invloed van aantal saneringsputten op totaal benodigde saneringsdebiet. _Aantal manipulatieputten_ In het voorgaande is al geconcludeerd dat door meerdere manipulatieputten te gebruiken het _manipulatie_ debiet sterk afneemt. Voor het _sanerings_ debiet heeft dit echter nadelige gevolgen in de gevallen waarin meer dan één manipulatieput wordt toegepast. Vanaf een bepaalde gradiëntsreductie blijkt namelijk het saneringsdebiet weer te moeten toenemen. Dit komt door de verandering van het stromingspatroon ter plaatse van de locatie dat ertoe leidt dat de locatie gedeeltelijk in het intrekgebied van de bovenstroomse manipulatieputten terecht zal komen. Hierdoor is er zowel op de bovenals benedenstroomse rand een uitgaande flux. Als gevolg hiervan moet dus de capaciteit van de saneringsputten worden verdeeld over de bovenen benedenstroomse rand. Deze 'gedwongen' configuratie geeft direct aan dat in deze situatie meerdere saneringsputten een gunstig effect hebben op de totale debiet. 


 Factor aantal manipulatieputten: Het manipulatiedebiet kan worden verminderd door meerdere putten te gebruiken, maar onder bepaalde omstandigheden neemt het saneringsdebiet juist toe. Dit is nadelig omdat het saneringsdebiet in de optimalisatie zwaarder weegt. Dit geldt echter voor een homogene bodem. 

Bij een heterogene bodem is de verhoogde flexibiliteit als gevolg van meerdere putten dermate gunstig, dat aangeraden wordt meerdere manipulatieputten te gebruiken. 

Nu de invloed van het aantal saneringsen manipulatieputten op het saneringsdebiet is beschreven, is ook de locatie van deze putten interessant. In eerste instantie zal een enkele saneringsput altijd aan de benedenstroomse zijde van de locatie worden geplaatst. Bij toenemende gradiëntsreductie verplaatst deze zich verder in de richting van de benedenstroomse rand. Zoals eerder in deze paragraaf is aangegeven, zal bij toename van het aantal manipulatieputten ook een aantal saneringsputten ter plaatse van de bovenstroomse rand nodig zijn. Algemeen kan worden gesteld dat voor kleine gradiëntsreducties de saneringsputten benedenstrooms moeten worden geplaatst. Bij grote gradiëntsreducties moeten de putten worden verspreid over zowel de benedenals de bovenstroomse rand van de locatie. 

2.3.4 _Vertaling naar locatiespecifiek ontwerp_ De resultaten uit dit hoofdstuk hebben een algemene geldigheid, waardoor de vertaling naar een locatiespecifiek ontwerp mogelijk is. Een schatting van het benodigde manipulatiedebiet kan namelijk volgens eenvoudige relaties worden bepaald uit de figuren 4 en 8. Een samenvatting hiervan is weergegeven in tabel 1 

Tabel 1. Nomogram voor het afleiden van benodigd manipulatiedebiet (m^3 /dag) bij ieis/i van 0,1 en een manipulatieput (set van infiltratie& onttrekkingsput). 

 l/b \ i 8.10-4^ 5.10-4^ 4.10-4^ 2.10-4^ 1.10-4 10 560 350 280 140 70 3 640 400 320 160 80 2 800 500 400 200 100 1 1120 700 560 280 140 

Het locatiespecifieke manipulatiedebiet kan worden bepaald door de lengte-breedte verhouding van de verontreinigingspluim te bepalen ( _l/b_ ) en de gradiënt van de natuurlijke grondwaterstroming ( _i_ ). Voor de voormalige locatie van Akzo Nobel (zie hoofdstukken 3 en 4) is deze verhouding 400 m/ 200 m = 2 hetgeen vergelijkbaar is met de referentiesituatie, de gradiënt is 8.10-4. Volgens tabel 1 is het benodigde manipulatiedebiet dan 800 m^3 /dag bij gebruik van één manipulatieput. De verontreinigingspluim op de voormalige locatie van Akzo Nobel is echter 400 m in plaats van 200 m zoals in de referentiesituatie. Hiervoor moet volgens paragraaf 2.3.2 worden gecorrigeerd door het in tabel 1 gevonden debiet te vermenigvuldigen met de verhouding tussen locatiespecifieke lengte (400 m) en de referentielengte (200 m), met een factor 2 dus. Het te manipuleren debiet zou dan 1600 m^3 /dag bedragen. Een laatste correctiefactor is die voor de transmissiviteit. Dit omdat de figuren waarop tabel 1 gebaseerd is, gerelateerd zijn aan een gradiënt in plaats van een waterflux. Bij een twee keer zo lage transmissiviteit zal een zelfde gradiënt tot een twee keer zo lage achtergrond flux leiden, waardoor ook twee keer zo weinig grondwater hoeft te worden omgeleid. De transmissiviteit voor de referentiesituatie bedraagt 1000 m^2 /dag. De transmissiviteit van de tussenzandlaag en het 


bovenste gedeelte van het watervoerend pakket op de voormalige locatie van Akzo Nobel bedraagt 400 m^2 /dag. Het manipulatiedebiet van 1600 m^2 /dag moet dan nog worden vermenigvuldigd met een factor van 0,4 (400/1000 m^2 /dag). Het manipulatiedebiet voor de voormalige Akzo Nobel locatie wordt dan geschat op 640 m^3 /dag. Dit komt goed overeen met het op grond van een grondig ontwerpproces berekende debiet van 670 m^3 /dag (zie hoofdstuk 4). Hierbij dient wel te worden opgemerkt dat bij het ontworpen systeem van meerdere sets van manipulatieputten gebruik wordt gemaakt, waardoor het te manipuleren debiet met ca. 40% kan afnemen (zie paragraaf 2.3.2). Indien hiervoor wordt gecorrigeerd zou de eerste schatting op basis van tabel 1 385 m^3 /dag bedragen. Dat het berekende debiet een stuk hoger is, is te verklaren door de heterogeniteit van de bodem op de voormalige locatie van Akzo Nobel. Berendrecht [Berendrecht, 1999] toont aan dat een heterogene bodemopbouw een toename van het manipulatiedebiet van 10% kan vergen en dat vlaktrekken van de stijghoogte met één set van manipulatieputten soms niet lukt doordat het niet in staat is 'in te spelen' op de ruimtelijke variaties. Resumerend geeft formule 1 de bepaling van een eerste schatting van een locatiespecifiek manipulatiedebiet uit tabel 1 weer: 

 man ref 

 locatie ref 

 locatie locatie lbi KD N 

##### KD 

 l 

 l Q = Q / ,∗ ∗ ∗ (1) 

waarin Qlocatie het locatiespecifieke manipulatiedebiet is, Ql/b,I het in tabel 2.1 opgezochte manipulatiedebiet bij gradiënt i en l/b, llocatie en lref de lengte van de verontreinigingspluim op de locatie en voor de referentie situatie (200 m) zijn, KDlocatie en KDref de transmissiviteit op de locatie en voor de referentiesituatie (1000 m^2 /dag) zijn en Nman een correctiefactor voor het aantal te plaatsen manipulatieputten (bijvoorbeeld 0,4 bij gebruik van 4 sets van putten in plaats van één). De waarde van Nman is af te lezen uit figuur 5 bij een gradiënteis van 0,1. Bij het gebruik van 4 manipulatieputten geldt een correctiefactor van 0,45. 

2.4 **Conclusies** 

Samenvattend zijn op basis van het gepresenteerde onderzoek conclusies te trekken gericht op de praktische toepassing van het concept _smart pump&treat_ : 

- Door toepassing van een grondwater-manipulatiesysteem is het vlaktrekken van de     stijghoogte tot 10% van de oorspronkelijke gradiënt mogelijk. 

- Een manipulatiesysteem bestaande uit één set manipulatieputten heeft bij een homogene     bodem de voorkeur vanwege de negatieve invloed van meerdere sets van putten op het     saneringsdebiet. 

- Bij een heterogene bodem biedt het manipuleren door middel van meerdere sets van putten     meer flexibiliteit, hetgeen zwaarder weegt dan het nadelig effect op het saneringsdebiet.     Deze situatie komt meer overeen met de praktijk, waardoor manipuleren door meerdere sets     van putten (4 à 5) wordt aanbevolen. 

- Een toenemend aantal extra manipulatie- of saneringsputten sorteert steeds minder effect. 

- Onder de gecreëerde omstandigheden kan het saneringssysteem volledig gericht zijn op het     saneren van de verontreiniging zelf. 

- Het gebruik van een extra saneringsput levert al een forse debietsreductie op waardoor de     uiteindelijke kosten van de zuiveringsstap sterk zullen afnemen. Meerdere saneringsputten     zijn ook voor het vergroten van de sanerende werking aan te bevelen. 

In de volgende hoofdstukken wordt aan de hand van de projectlocatie, een voormalige locatie van Akzo Nobel te Weert, het ontwerp voor een gemanipuleerde smart pump&treat gemaakt. 


Hierbij is nadrukkelijk gerekend met het voorkomen van heterogeniteiten in de ondergrond en het waarborgen van robuustheid onder dynamische omstandigheden. 


##### HOOFDSTUK 3 

#### ONTWERP 

3.1 **Inleiding** 

In voorgaand hoofdstuk is voor een generieke case het principe van beheersing van verontreinigd grondwater door 'omleiden' van _schoon_ grondwater toegelicht. In dit hoofdstuk zal worden ingegaan op knelpunten die ondervonden werden bij het ontwerp van een gecombineerd manipulatie en smart pump&treat systeem voor een voormalige locatie van Akzo Nobel, thans Honeywell (zie figuur 11). 

Fig. 11. Case: voormalige locatie van Akzo Nobel, thans locatie van Honeywell. 

Een overzicht van de verontreinigingssituatie wordt gegeven in bijlage A. In paragraaf 3.2.2. wordt de geohydrologie van de locatie beschreven. Voor een meer uitgebreide beschrijving van de verontreinigingssituatie dan hier gegeven wordt verwezen naar Bakker [Bakker, 1996]. Voorafgaand aan het tot stand komen van het ontwerp zoals beschreven in dit rapport, is door TNO [Te Stroet & Hetterschijt, 1998] een studie verricht naar haalbaarheid van de implementatie van grondwater-manipulatie voor de voormalige locatie van Akzo Nobel. Om te komen tot een ontwerp dat geschikt is voor het maken van een bestek en een gedetailleerde kostenraming, dienen een aantal aspecten nader te worden onderzocht: 

- Effect heterogeniteit van de ondergrond op robuustheid van het systeem. 

- Beperkte mogelijkheden voor het plaatsen van putten op en buiten het voormalige Akzo     Nobel terrein. 

- Effect van veranderingen in het hydrologisch systeem op de robuustheid van het systeem. 

- Sanerende werking van het smart pump&treat systeem. 


In dit hoofdstuk wordt het effect van bodemheterogeniteit en de beperkte mogelijkheid tot het plaatsen van putten op het ontwerp toegelicht. Dit zijn 'statische' ontwerp bepalende factoren. Hoofdstuk 4 zal nader worden ingaan op de robuustheid van het systeem onder dynamische condities. In dit hoofdstuk wordt het ontwerp van zowel het manipulatiesysteem als ook het saneringssysteem beschreven. De eerste stap in het ontwerpproces is gericht op het geohydrologisch beheersen van de verontreiniging, waarbij zo min mogelijk verontreinigd grondwater dient te worden onttrokken (zie paragraaf 3.2.1 voor de uitgangspunten). Het ontwerp is gedimensioneerd op de verontreinigingscontour met een maximale omvang zoals die in 1996 bekend was [Bakker, 1996], te weten de chloroformverontreiniging in het grondwater van de tussenzandlaag (zie bijlage B). Hoewel het 'geohydrologisch ontwerp' van zowel het manipulatiesysteem als het saneringssysteem gelijktijdig plaatsvond zijn de systemen in twee aparte paragrafen beschreven (resp. 3.3 en 3.4). De ontwerpsystematiek zelf is beschreven in paragraaf 3.2. In paragraaf 3.5 komt de sanerende werking van het saneringssysteem aan bod. Daarin zullen zowel de verwachte doorbraak van diverse 'hoofd'-verontreinigingen in de saneringsputten worden beschreven als ook de effectiviteit van de sanering. Tenslotte komen in paragraaf 3.6 de geohydrologische effecten van het gecombineerde systeem van omleiden en smart pump&treat op de omgeving aan de orde. Het gaat dan om de effecten op verdrogingsgevoelige vegetatie en op het beheerssysteem van het nabijgelegen Budelco. 

3.2 **Ontwerpsystematiek** 

3.2.1 _Methode en uitgangspunten_ Als belangrijkste ontwerpcriteria zijn de beheersing (1) van de verontreinigingen en de minimalisatie van het onttrekkingsdebiet (2) van verontreinigd grondwater dat onttrokken wordt, genoemd. Daarnaast werden in overleg binnen het consortium nog een aantal meer praktische ontwerpcriteria genoemd: 

- Een beperkt aantal sanerings- en omleidingsputten (maximaal 12 saneringsputten). 

- Optimaliseren naar sanerende werking saneringsputten. 

- Vracht verontreiniging naar zuivering minder dan 100 g/dag. 

- Beperking in mogelijke locaties voor sanerings- en omleidingsputten. 

- Manipulatiedebiet minder dan 1500 m^3 /dag. 

- Saneringsdebiet per put niet minder dan 8 m^3 /dag vanwege een ondergrens in de     pompcapaciteit. 

Het criterium 'beheersing verontreiniging' kan worden vertaald in de voorwaarde dat het grondwater op de uitgekarteerde contour van chloroform altijd naar het voormalige bedrijfsterrein van Akzo Nobel gericht dient te zijn. Aan deze voorwaarde kan worden voldaan door de natuurlijke grondwaterstroming om te leiden en door met saneringsputten grondwater te onttrekken. Dit moet met een minimaal debiet. Om aan de twee belangrijkste ontwerpcriteria te kunnen voldoen heeft het ontwerp via een bepaalde systematiek plaatsgevonden. Hierbij is gebruik gemaakt van de optimalisatieroutines MODMAN [GeoTrans, 1992] en LINDO [Schrage, 1991]. Met behulp van deze routines is het mogelijk om voor numerieke berekeningen de optimale oplossing te vinden uit een omvangrijke reeks mogelijke combinaties van aantal putten, putlocaties en putdebieten. Hiertoe dient het grondwaterprobleem getransformeerd te worden naar een optimalisatieprobleem. Deze transformatie kan worden uitgevoerd met behulp van MODMAN. Op basis van het locatiespecifieke grondwatermodel bepaalt MODMAN de responsiecurve van iedere potentiële onttrekking of injectie. Daarmee is in feite informatie aanwezig over de invloed van een put op een willekeurige locatie met een willekeurig debiet. De volgende stap in het ontwerpproces bestaat uit een optimalisatie van de alle responsiecurves onder de vooraf gestelde eisen. Hiervoor wordt de optimalisatieroutine LINDO gebruikt. Deze 


routine levert het optimale ontwerp in de vorm van putlocaties en de bijbehorende debieten. Een schema van de ontwerpsystematiek wordt in figuur 12 geschetst. 

 optimale debieten en LINDO bijbehorende kustlocaties 

 MODMAN OUTPUT 

 modflow input 

 Kustlocaties, Voorwaarden, modelfunctie simulaties = mogelijke kustlocaties + 1 

 MODFLOW 

 MODMAN INPUT 

Fig. 12. Stroomschema optimalisatie-procedure numeriek model. 

In paragraaf 3.3 en 3.4 wordt de invoer van MODMAN (putlocaties, voorwaarden en doelfunctie) voor respectievelijk het manipulatiesysteem en het saneringssysteem beschreven, evenals de resultaten van de optimalisatiestap met LINDO. Het model ofwel het 'gereedschap' waarmee MODMAN de invoer van LINDO genereert wordt beschreven in paragraaf 3.2.2. Van het berekende systeem wordt achteraf nagegaan of ook aan de andere ontwerpcriteria zoals het aantal putten, het manipulatiedebiet en de vracht naar de zuivering is voldaan. Uit enkele pre runs bleek namelijk al, dat met name het benodigde manipulatiedebiet en het aantal putten binnen de door Akzo Nobel gestelde randvoorwaarden zouden vallen. Voor optimalisatie op vrachtverwijdering is de huidige code MODMAN niet geschikt. Het ontwerp werd dan ook achteraf op dit criterium geëvalueerd door het effect van het ontworpen systeem op de verontreiniging met een stoftransportmodel door te rekenen. 

3.2.2 _Opzet grondwatermodel_ 

_Inleiding_ Uitgangspunt voor het grondwatermodel dat gebruikt is binnen deze studie, is de regionale en ter plekke van het voormalige Akzo Nobel terrein locale geohydrologische gebiedskennis van Tauw. Door Tauw is op basis van het NAtionaal GROndwater Model (NAGROM, module A61 1801-93, RIZA-TNO) een regionaal grondwatermodel vervaardigd in de analytische elementen code MLAEM [Strack, 1989]. In dit model is onder andere het beheerssysteem van Budelco opgenomen en is, ter onderscheiding van het NAGROM model, onder meer de deklaag en scheidende laag op 17 m –mv ingebracht. Daarnaast is het oppervlaktewatersysteem meer in detail ingebracht. De kennis uit dit model is door TNO verwerkt in een regionaal grondwatermodel in MODFLOW [McDonald & Harbaugh, 1988], verder het regionale model genoemd. Voor de berekeningen in deze studie is door TNO gebruik gemaakt van de modelcode MODFLOW die gebaseerd is op eindige differenties. Deze keuze voor MODFLOW was noodzakelijk om de optimalisatie met MODMAN mogelijk te maken. 


_Discretisatie_ In eerste instantie is een regionaal grondwatermodel opgezet, dat een lengte heeft van 4,9 km en een breedte van 4 km, waarvan de oppervlakte 19,6 km^2 bedraagt. De linkerbovenhoek van het modelnetwerk ligt op de RMD coördinaten x = 168250 en y = 363000. De grootte van de modelcellen neemt naar het interessegebied af van 100 naar 20 meter. Van dit regionale model is een uitsnede gemaakt, waarmee het manipulatieen saneringssysteem is ontworpen, verder het locale model genoemd. De oriëntatie van het locale model is circa 30º gedraaid ten opzichte van de oriëntatie van het regionale grondwatermodel, zodat de lengterichting van het model parallel aan de stromingsrichting van het grondwater over de locatie ligt. Het locale model heeft een lengte van 3 km en breedte van 2 km zodat de oppervlakte 6 km^2 bedraagt. De linkerbovenhoek van het modelnetwerk ligt op de RMD coördinaten x = 168400 en y = 360000. De grootte van de modelcellen neemt naar het interessegebied af van 100 naar 10 meter. 

_Geohydrologische schematisatie_ Zowel het regionale als locale model bestaat uit 4 lagen: een vijf meter dikke deklaag (modellaag 1) schermt het watervoerend pakket af (modellagen 3 en 4), dat tot ruim 100 meter beneden maaiveld doorloopt. Onder de deklaag bevindt zich een tussenzandlaag (modellaag 2) tot 17 m – mv. De tussenzandlaag wordt plaatselijk van het watervoerend pakket gescheiden door een enkele meters dikke scheidende laag, zie tabel 2 (gebaseerd op TNO Grondwaterkaart en gebiedskennis van Tauw). 

Tabel 2. Geohydrologische schematisatie. 

Regionaal diepte [m –mv] 

 Samenstelling Geohydrologische eenheid 

 Lokaal Diepte [m –mv] 

 Samenstelling 

0-5 Leemhoudend, fijn zand, leem 

 Deklaag 0,0-4,5 Fijn en matig grof zand, plaatselijk lemig 

 4,5-5,0 Lemig zand 

5-105 Fijne en grove grindhoudende zanden, plaatselijk kleilaagjes 

 5,0-17,0 Grof zand (tussenzandlaag) 

 Watervoerend pakket 

 17,0-20,0 Klei 

 >20,0 Grof zand, grindhoudend 

>105,0 Eerste scheidende laag 

Op basis van de TNO-grondwaterkaart en door geohydrologische gebiedskennis van Tauw [Bakker en Boode, 1997] is de in tabel 3 weergegeven parameterisatie van de modellagen gehanteerd. 

Een eerste testberekening met het locale grondwatermodel wees uit dat de vorm van het manipulatieen saneringssysteem sterk werd beïnvloed door de wijze waarop de kleilaag die de tussenzandlaag van het watervoerend pakket scheidt, wordt gemodelleerd. 


Tabel 3. Geohydrologische parameterisatie van de modellagen. 

 Laag Type Dikte [m] Weerstand [d] Transmissiviteit [m2/d] 1 Deklaag 5 5 2 Tussenzandlaag 12 150 

- Scheidende laag 3 1000-3000 - 3 Watervoerend pakket 10 - 260 4 Watervoerend pakket 70 - 1820 NB: dikte en weerstand van de scheidende laag zijn indicatief, deze variëren namelijk ruimtelijk. 

Beschikbare puntmetingen waren hiervoor geïnterpoleerd tot een ruimtelijk beeld van de kleilaag (zie figuur 13) Volgens dit beeld werd de kleilaag beschouwd als een continue laag over een afstand van honderden meters. Uit geostatistische analyse van alle bij Tauw en NITG beschikbare boringen (o.a. DINO) en mondeling overleg met de heer F. de Lange, geoloog bij NITG werd geconcludeerd, dat de continuïteit van de kleilaag minder groot is dan oorspronkelijk werd aangenomen. 

Fig. 13. Oorspronkelijke schematisatie kleilaag volgens regionaal model. 


Het kleivoorkomen in de boringen kan eerder geïnterpreteerd worden als in het gehele modelgebied voorkomende kleilenzen van beperkte afmetingen (eerder 100x100 m i.p.v. 1000x1000 m). De geringe afmetingen van deze kleilenzen ten opzichte van de dichtheid aan boringen, maakt het onmogelijk de lenzen met zekerheid uit te karteren. De robuustheid van het ontwerp van het manipulatieen saneringssysteem kan door deze onzekerheid negatief worden beïnvloed, als hiermee geen rekening wordt gehouden. Daarom is er voor gekozen om de onzekerheid over het voorkomen van de kleilaag in het ontwerpproces, dat wil zeggen in het locale grondwatermodel, mee te nemen door middel van geostatistische simulaties. Met deze methode is het mogelijk om op basis van puntmetingen een schatting te maken voor de waarde van een modelcel waar niet is gemeten. In dit specifieke geval gaat het om de dikte van de kleilaag die zich niet continu uitstrekt over het gebied. De simulatie is mogelijk omdat van de spreiding van de dikte ruimtelijke gegevens beschikbaar zijn in de vorm van boringen. Om uiteindelijk een waarde voor de weerstand van de laag te bepalen is naast de dikte ook een waarde voor de doorlatendheid nodig. Een simulatie hiervan is niet mogelijk omdat hierover geen ruimtelijke informatie beschikbaar is. In de weerstandsbepaling is daarom de doorlatendheid constant verondersteld. Een schatting van die dikte op een bepaald punt is mogelijk door rekening te houden met de ruimtelijke correlatie tussen de boringen. Met het programma GSLIB [Deutsch en Journel, 1998] is allereerst vastgesteld wat de ruimtelijke correlatie op basis van de aanwezige boring is in zowel de xals de y-richting. Hiervoor zijn 'variogrammen' gebruikt. Hieruit blijkt dat er globaal in de noord-zuid richting van een sterkere correlatie sprake is dan in de west-oost richting. Daarna zijn door het programma met de kennis uit de boringen vijf 'realisaties' van de kleilaag gegenereerd die allemaal een zelfde waarschijnlijkheid van voorkomen hebben. In elke realisaties bestaat de kleilaag nu niet meer uit een continue laag, maar is in een ruimtelijk veld van modelcellen een diktevariatie ingebracht op basis van de informatie uit de boringen. Een realisatie van de kleilaagdikte is weergegeven in figuur 14. Een totaaloverzicht van de vijf realisaties is opgenomen in bijlage C. 

Fig. 14. Realisatie van een in dikte variërende kleilaag op basis van geostatistiek. 


De realisatie in figuur 14 laat een bepaald 'geveegd' patroon zien. Dit komt overeen met de eerdere constatering dat de correlatie ten aanzien van de kleidikten niet in alle richtingen gelijk is. In de y-richting is deze hoger dan in de x-richting. Voor elk van deze vijf realisaties wordt met het Akzo-model een gemanipuleerde smart pump&treat systeem ontworpen. De weerstand als gevolg van de kleilaag tussen tussenzandlaag en watervoerend pakket is op basis van de geostatistische simulaties aangepast. 

_Grondwateraanvulling_ Zoals in het vorige hoofdstuk is uiteengezet is het concept van gemanipuleerde smart pump&treat systeem ontwikkeld ten behoeve van een minimalisering van het saneringsdebiet. Het manipulatiesysteem draagt ertoe bij dat het saneringssysteem zich volledig kan 'richten' op het saneren van de verontreiniging zelf. Het uiteindelijke saneringsdebiet moet gelijk zijn aan de hoeveelheid water die over de randen de saneringslocatie binnenkomt. Naast de grondwaterstromen die worden gecontroleerd door het manipulatiesysteem behoort hier ook de grondwateraanvulling. Omdat de achtergrondstroming wordt beheerst door manipulatie, zal het saneringsdebiet met name door de grondwateraanvulling worden bepaald. Een nauwkeurige schatting van deze aanvulling op de locatie is dan ook noodzakelijk om het saneringssysteem te dimensioneren. In het regionale model is de grondwateraanvulling in de vorm van neerslag over het hele gebied gemodelleerd als een constante flux van 0,7 mm per dag. In het locale model heeft hierop een fijnregeling plaatsgevonden ter plaatse van de locatie. Op dit terrein staan verschillende gebouwen waar tussendoor voornamelijk verharding aanwezig is. Langs deze verharding is drainage aanwezig die afwatert op het regenwaterriool. Ook het overgrote deel van de gebouwen is voorzien van regenwaterafvoer die aangesloten is op het riool. Op grond van de geschetste situatie is de conclusie getrokken, dat slechts een deel van het regenwater dat op de locatie valt ook werkelijk zal bijdragen aan de grondwateraanvulling. In het locale model is de hoeveelheid gemodelleerde grondwateraanvulling ter plaatse van de locatie dan ook verminderd. De aanvulling op een klein deel van het oppervlak waar gebouwen zijn gesitueerd, is teruggebracht naar 0 mm per dag. Op het resterende deel van de locatie is de neerslag van 0,7 mm per dag gehalveerde tot 0,35 mm per dag (zie bijlage D). 

_Onttrekkingen, oppervlaktewater en onderbemaling_ Volgens gegevens van Tauw zijn onttrekkingen van het beheerssysteem van Budelco ingevoerd in het regionale en locale grondwatermodel. Hierbij zijn de onttrekkingen volgens tabel 4 in het model ingebracht. Deze debieten zijn de mediane debieten die volgen uit een statistische analyse van de maandgemiddelde debieten over de perioden juli 1992 tot en met februari 1995. De onttrekking in het watervoerend pakket zijn proportioneel aan de dikte van de modellagen 3 en 4 verdeeld over de lagen die tezamen het watervoerend pakket representeren. 

Daarnaast is de Zuid-Willemsvaart ingevoerd, met een vast peil van 35,2 m +NAP en een infiltratieweerstand van 500 dagen. In het modelgebied komen enkele Peelen voor zoals het Rings-elven. Deze Peelen zijn ook ingevoerd door middel van een vast peil van 33,7 m +NAP en hebben een infiltratieweerstand van 3000 tot 4000 dagen. In het modelgebied komen ook enkele gebieden voor waar onderbemaling plaatsvindt, dit zijn de jarosiet bekkens van Budelco. Deze onderbemaling is in het regionale en locale model ingevoerd door middel van onttrekkingen in de modelcellen waar onderbemaling plaatsvindt. Het debiet van de onttrekkingen per cel is berekend uit het oppervlakte aandeel van die cel van het onderbemaalde gebied en de totale hoeveelheid grondwater die uitgemalen wordt. Gegevens over de hoeveelheid water die wordt uitgemalen uit deze gebieden is afkomstig van Tauw. In totaal gaat het om ongeveer 460 m^3 /dag, dat in deze gebieden wordt uitgemalen. 


Tabel 4. Onttrekkingen beheerssysteem Budelco. 

 x-coördinaat y-coördinaat Q [m3/dag] TZL 

 Q [m3/dag] WVP 170660 362027 238 170202 362013 228 169881 361978 298 169452 361706 312 169709 361113 111 169964 360830 111 169304 361752 430 169825 361897 519 170299 362062 427 170709 361933 413 170958 361488 249 171195 361044 352 

Daarnaast is de Zuid-Willemsvaart ingevoerd, met een vast peil van 35,2 m +NAP en een infiltratieweerstand van 500 dagen. In het modelgebied komen enkele Peelen voor zoals het Rings-elven. Deze Peelen zijn ook ingevoerd door middel van een vast peil van 33,7 m +NAP en hebben een infiltratieweerstand van 3000 tot 4000 dagen. In het modelgebied komen ook enkele gebieden voor waar onderbemaling plaatsvindt, dit zijn de jarosiet bekkens van Budelco. Deze onderbemaling is in het regionale en locale model ingevoerd door middel van onttrekkingen in de modelcellen waar onderbemaling plaatsvindt. Het debiet van de onttrekkingen per cel is berekend uit het oppervlakte aandeel van die cel van het onderbemaalde gebied en de totale hoeveelheid grondwater die uitgemalen wordt. Gegevens over de hoeveelheid water die wordt uitgemalen uit deze gebieden is afkomstig van Tauw. In totaal gaat het om ongeveer 460 m^3 /dag, dat in deze gebieden wordt uitgemalen. 

_Randvoorwaarden_ Naast drijvende krachten als grondwateraanvulling, onttrekkingen en onderbemaling dienen ook randvoorwaarden op de modelrand te worden gedefinieerd. De randvoorwaarden van het locale model zijn afkomstig uit het regionale grondwatermodel van TNO: de hiermee berekende stijghoogtes zijn als vaste stijghoogte op de rand van het locale model gedefinieerd. De randvoorwaarde van het regionale model van TNO zijn weer afkomstig uit het regionale model van Tauw [Bakker en Boode, 1997]. 

_Kalibratie en validatie_ Kalibratie van het regionale en locale grondwatermodel dat door TNO is opgezet behoort niet tot de scope van deze studie. Het regionale grondwatermodel van Tauw [Bakker en Boode, 1997] is echter wel op stijghoogtemetingen gekalibreerd en voor enkele momentopnamen stationair gevalideerd. De genormaliseerde verschillen tussen berekende en gemeten stijghoogte bedroeg volgens Tauw 0,15 m. Het regionale model van Tauw voldoet daarmee goed om de stijghoogte in het watervoerend pakket te voorspellen. Het regionale grondwatermodel van TNO is op betrouwbaarheid getoetst door de berekende stijghoogtes van het eerste watervoerend pakket te vergelijken met de volgens het Tauw model berekende stijghoogtes (zie bijlage K). Volgens de figuur in de bijlage komen de berekende stijghoogtes van de regionale modellen van Tauw en TNO buiten het voormalige Akzo Nobel terrein aardig overeen. Verschillen op het voormalige Akzo Nobel terrein zelf kunnen worden verklaard door de lokale verfijningen die in het TNO model zijn aangebracht. 


3.3 **Geohydrologisch ontwerp manipulatie** 

Zoals in paragraaf 3.2.1 is aangegeven kan door de optimalisatieroutines MODMAN en LINDO op objectieve wijze een gecombineerd manipulatiesysteem en saneringssysteem worden ontworpen, waarbij zo weinig mogelijk grondwater wordt onttrokken en de verspreiding wordt beheerst. 

Een van de belangrijkste ontwerpcriteria is het tegengaan van verspreiding van verontreinigingen. Dit criterium is in het optimalisatieproces opgenomen door als randvoorwaarde te stellen dat grondwaterstroming over de chloroformcontour zoals vastgesteld voor de tussenzandlaag altijd naar binnen gericht dient te zijn (zie figuur 15b). Deze randvoorwaarde wordt zowel in de tussenzandlaag als in de bovenste 10 meter van het watervoerend pakket opgelegd. 

## Qxy ≥ 0 

### iachtergrond 

### ieis 

##### Q Q Q 

Fig. 15. Randvoorwaarde voor verspreiding volgens gradiëntseis [a] en flux eis [b]. 

Door deze voorwaarde kan de chloroformcontour, die de maximale omvang van de verontreiniging van het voormalige Akzo Nobel terrein bepaalt, niet verder uitdijen. Deze _flux_ randvoorwaarde voor verspreiding wijkt af van eerder gehanteerde _gradiënts_ randvoorwaarde (i/ieis in hoofdstuk 2 en figuur 15a). De reductie van de gradiënt ten opzichte van de natuurlijke situatie is voor de Akzo case een minder bruikbaar optimalisatiecriterium vanwege de heterogeniteit van de kleilaag. De stijghoogte en daarmee de gradiënt in de tussenzandlaag kan lokaal binnen het te beheersen gebied sterk variëren als gevolg van deze heterogeniteit. Dit kan tot gevolg hebben, dat zeer veel grondwater moet worden rondgepompt en gesaneerd om de gradiënt in een deelgebiedje binnen de verontreiniginscontour te reduceren tot de voorafgestelde eis, terwijl deze eis voor het merendeel van het te beheersen gebied al is bereikt. In feite mag de verontreiniging zich binnen het verontreinigde gebied best verspreiden, zolang de maatgevende contour van chloroform maar niet verder uitdijt. In plaats van een strenge gradiëntseis voor het gehele verontreinigde gebied op te leggen, is nu gekozen voor een eis aan de stromingsrichting van het grondwater op de chloroformcontour. Deze eis is veel minder streng, waardoor het optimalisatieproces resulteert in een systeem dat voldoet aan de verspreidingseis bij een heterogene bodem en dat toch 'zuinig' met water is. 

In het optimalisatieproces worden verder een aantal (subjectieve) keuzes gemaakt die de objectiviteit van het ontwerpproces verminderen. Omdat het manipulatiesysteem gelijktijdig met het saneringssysteem wordt geoptimaliseerd middels LINDO, worden de gemaakte keuzes met betrekking tot het saneringsen manipulatiesysteem beide in deze paragraaf besproken. Het definitieve ontwerp van het saneringssysteem wordt echter in paragraaf 3.4. beschreven. 


De subjectieve keuzes die voorafgaand aan de optimalisatie zijn gemaakt, betreffen de toegestane locaties, waar het optimalisatieprogramma een manipulatie of saneringsput mag plaatsen, en weging van de optimalisatie tussen manipulatie en saneringssysteem. In figuur 16 worden de van tevoren vastgestelde locaties weergegeven waar manipulatieputten (zwart) en saneringsputten (rood) geplaatst mogen worden. 

Fig. 16. Mogelijke locaties voor manipulatie (zwart) en saneringsputten (rood). 

De mogelijke locaties van de putten zijn voor de tussenzandlaag en het watervoerend pakket gelijk. Er worden geen putten toegestaan in de deklaag. Het van tevoren beperken van het aantal mogelijke putlocaties heeft zowel een praktische als een rekentechnische reden. Binnen MODMAN kan voor maximaal 100 punten een responsiecurve worden berekend. Daarnaast neemt de rekentijd van de optimalisatie binnen LINDO drastisch toe met het aantal te beschouwen locaties. Om deze rekentechnische reden is besloten slechts 72 mogelijke locaties voor manipulatieputten toe te staan (36 per watervoerende laag) en 74 mogelijke locaties voor saneringsputten (38 per watervoerende laag). Daarnaast is er een praktische reden voor het beperken van mogelijke locaties voor putten: de voormalige locatie van Akzo Nobel is omringd door oppervlaktewater zoals de vennen en het kanaal. Plaatsing van putten is hier niet mogelijk, waarmee bij de optimalisatie expliciet is rekening gehouden door die locaties uit te sluiten. 

Uit figuur 16 blijkt dat de mogelijke locaties voor saneringsputten enigszins willekeurig verdeeld zijn over de chloroformverontreinigingspluim, waarbij locaties in het ven ten oosten van het terrein zijn uitgesloten. De verdeling van mogelijke locaties voor de manipulatieputten zijn minder willekeurig verdeeld. Bij de plaatsing is rekening gehouden met het feit dat zowel stroomopwaarts van de verontreiniging onttrekkingputten noodzakelijk zijn en stroomafwaarts injectieputten. Dit uit zich in een puntenwolk ten zuidwesten van de locatie en een ten noordoosten. De asymmetrie in de vorm van de puntenwolken is het gevolg van de beperkte plaatsingsmogelijkheden aan de noordkant van de locatie door de aanwezigheid van oppervlaktewater. Op basis van ervaringen opgedaan met de generieke analyse van omleiding (zie hoofdstuk 2) en de haalbaarheidsstudie werd verwacht dat injectieputten ten noordoosten van de locatie noodzakelijk waren. Deze 


dienden echter verder stroomafwaarts te worden geplaatst vanwege het vennengebied 'Ringselven'. 

Om inzicht te krijgen in het manipulatie en saneringsysteem is voorafgaand aan de uiteindelijke optimalisatie procedure twee keer geoptimaliseerd, waarbij de mogelijke locaties van manipulatieputten werd gevarieerd. Hiervoor werd een groot gebied grofmazig 'bedekt' met putlocaties (zie figuur 17). Uit de resultaten van deze optimalisatie bleek, dat ten zuidwesten van de locatie onttrekkingsputten voor manipulatie nodig waren op een afstand van 100 à 200 meter van de locatie. Ten noordoosten waren injectieputten voor manipulatie nodig. Opvallend was, dat de meest noordelijke putlocatie bij de optimalisaties telkens nodig was. 

Fig. 17. Eerste keuze mogelijke locaties manipulatie(zwart) en saneringssysteem (rood). 

Op basis van deze resultaten werd een kleiner gebied bepaald, waar putten geplaatst mochten worden (zie figuur 16). Door in een kleiner gebied evenveel locaties toe te staan, wordt de 'puntenwolk' dichter en kan een optimaler manipulatiesysteem worden gevonden. Uit de preoptimalisaties bleek dat telkens saneringsputten nabij de chloroformcontour nodig waren, vandaar dat hier de meeste locaties voor saneringsputten werden gekozen. Vanwege de randvoorwaarde aan het minimale saneringsdebiet per put (8 m^3 /dag, zie paragraaf 3.2.1) werd in een definitieve optimalisatieronde ook locaties voor saneringsputten midden in de verontreiniging toegestaan en minder putten op de rand. De gedachte was dat een paar putten met een hoger debiet de verontreiniging bijna even efficiënt zouden kunnen beheersen als meerdere putjes nabij de rand van de chloroformcontour. 

Een andere subjectieve keuze die voorafgaand aan de optimalisatie gemaakt dient te worden is de weging tussen de mate van minimalisatie van het manipulatiedebiet en het saneringsdebiet. Door het consortium werd op basis van de resultaten van de eerste optimalisatie ingeschat dat de manipulatiekosten minder sterk afhangen van het debiet dan de saneringskosten. Het minimaliseren van het saneringsdebiet werd daarom in de optimalisatie met LINDO zwaarder meegewogen dan het minimaliseren van het manipulatiedebiet. 


Hiertoe werd het systeem in optimalisatieronde 4 op twee manieren geoptimaliseerd, één keer waarbij het saneringsdebiet 10 keer zwaarder woog dan het manipulatiedebiet en één keer waarbij het 100 keer zwaarder woog. 

 30 40 50 60 70 80 90 100 110 120 

 20 30 40 50 60 70 80 90 100 110 120 

 man.sys. tzl man.sys. 1e wvp san.sys tzl. san sys 1e wvp 

 30 40 50 60 70 80 90 100 110 120 

 20 30 40 50 60 70 80 90 100 110 120 

 man.sys. tzl man.sys. 1e wvp san.sys tzl. san sys 1e wvp 

 30 40 50 60 70 80 90 100 110 120 

 20 30 40 50 60 70 80 90 100 110 120 

 man.sys. tzl man.sys. 1e wvp san.sys tzl. san sys 1e wvp 

 40 50 60 70 80 90 100 110 120 

 20 30 40 50 60 70 80 90 100 110 120 

 man.sys. tzl man.sys. 1e wvp san.sys tzl. san sys 1e wvp 

 30 40 50 60 70 80 90 100 110 120 

 20 30 40 50 60 70 80 90 100 110 120 

 man.sys. tzl man.sys. 1e wvp san.sys tzl. san sys 1e wvp 

 30 40 50 60 70 80 90 100 110 120 

 20 30 40 50 60 70 80 90 100 110 120 

 man.sys. tzl man.sys. 1e wvp san.sys tzl. san sys 1e wvp 

 30 40 50 60 70 80 90 100 110 120 

 20 30 40 50 60 70 80 90 100 110 120 

 man.sys. tzl man.sys. 1e wvp san.sys tzl. san sys 1e wvp 

 30 40 50 60 70 80 90 100 110 120 

 20 30 40 50 60 70 80 90 100 110 120 

 man.sys. tzl man.sys. 1e wvp san.sys tzl. san sys 1e wvp 

Fig. 18. Manipulatieen saneringssysteem na optimalisatie 5 voor vijf realisaties. 


Nadere analyse van het resulterende saneringssysteem leidde ertoe dat de plaats waar saneringsputten kunnen worden geplaatst verder werd ingeperkt en dat minimalisatie van het manipulatiedebiet in de optimalisatie werd losgelaten (zie paragraaf 3.4). Uit deze vijfde optimalisatieronde volgde een manipulatieen saneringssysteem per geologische variant zoals weergegeven in figuur 18. 

Zoals in paragraaf 3.2.2 al is uitgelegd wordt voor vijf verschillende geologische realisaties van de werkelijkheid een manipulatieen saneringssysteem ontworpen door optimalisatie. Op deze manier kan bij het ontwerp van het systeem al rekening worden gehouden met de invloed van de onzekerheid van de geologie op de betrouwbaarheid van het ontwerp. Uit optimalisatie 5 volgt dat het optimale manipulatie en saneringssysteem per realisatie verschilt wat betreft locatie van putten en het debiet per put. In werkelijkheid moet vooraf voor de locaties van de manipulatieen saneringsputten worden gekozen. Op basis van figuur 18 werd een manipulatieen saneringssysteem 'gekozen' door nu een beperkt aantal manipulatieen saneringsputten te selecteren die in zoveel mogelijk van de vijf geologische realisaties voorkomen. Deze putten zijn blijkbaar 'altijd' noodzakelijk voor een beheersing van de verontreiniging. Ook twee uitvoeringstechnische randvoorwaarden zijn meegenomen in de bepaling van het uiteindelijke systeem. Allereerst is afgezien van het plaatsen van manipulatieputten aan de overzijde van het kanaal vanwege de bereikbaarheid. Ten tweede diende het aantal onttrekkingsputten van het manipulatiesysteem even groot te zijn als het aantal infiltratieputten en het onttrekkingsdebiet even groot als het infiltratiedebiet. 

Het op basis van optimalisatieronde 5 gekozen manipulatieen saneringssysteem dat voldoet aan de uitgangspunten is weergegeven in figuur 19 (putnummers 1 t/m 27). 

Fig. 19. Het 'gekozen' manipulatieen saneringssysteem. 

Omdat de het gekozen systeem niet het optimale systeem is voor de afzonderlijke geologische realisaties, dient het gekozen systeem in een zesde optimalisatieronde opnieuw per realisatie te worden geoptimaliseerd. De plaats van de putten ligt dan vast, alleen het debiet per put kan 


worden aangepast. In tabel 5 worden de geoptimaliseerde debieten van het manipulatiesysteem en saneringssysteem per geologische realisatie opgesomd, waarbij ook het minimum, maximum en gemiddelde (avg) debiet is weergegeven. Een negatieve waarde duidt op een onttrekking en een positieve waarde betekent een debiet dat wordt geïnfiltreerd. 

Tabel 5. Injectieen onttrekkingsdebieten per geologische realisatie. 

Putnummer Laag x y Q r1 Q r2 Q r3 Q r4 Q r5 min avg max Manipulatie 4 TZL 170079 359418 -13 -6 -10 -6 -10 -13 5 TZL 170158 359438 -33 -28 -34 -35 -27 -27 -31 -35 6 TZL 170450 359802 13 0 0 7 13 7 TZL 170328 360214 33 34 34 35 37 33 35 37 1 WVP 169884 359482 -386 -423 -394 -360 -394 -360 -391 -423 2 WVP 169885 359585 -109 -31 -93 -113 -31 -87 -113 3 WVP 170008 359379 -121 -164 -97 -147 -142 -97 -134 -164 8 WVP 170480 359705 192 206 167 268 161 161 199 268 9 WVP Zie 6 Zie 6 58 34 55 29 48 29 45 58 10 WVP 170396 359921 366 378 360 323 327 323 351 378 Sanering 20 TZL 170046 359582 -20 -24 -21 -24 -18 0 -5 -12 22 TZL 170028 359698 -11 0 0 -12 -4 0 -11 -22 23 TZL 170208 359682 -14 -25 -10 0 -24 0 -15 -25 24 TZL 170296 359730 -11 -5 -14 -61 -20 -5 -22 -61 25 TZL 170285 359792 -20 -8 -22 0 -3 -18 -21 -24 26 WVP 170210 359637 -25 -21 -32 -23 -34 -14 -25 -35 27 WVP 170205 359771 -33 -35 -14 -17 -24 -21 -27 -34 min avg max san TZL -76 -62 -67 -97 -69 -62 -74 -97 san wvp -58 -56 -46 -40 -58 -40 -52 -58 totaal -134 -118 -113 -137 -127 manipuleren 662 652 616 655 573 573 632 662 NB: TZL is tussenzandlaag (5-12 m -mv), WVP is eerste 10 meter van het watervoerend pakket 

Uit tabel 5 blijkt dat het debiet per geologische realisatie aanzienlijk varieert per put (rijen in de tabel). Zo varieert het benodigde onttrekkingsdebiet uit put 2 afhankelijk van de werkelijke bodemopbouw tussen de 31 en 113 m^3 /dag. Via put 6 hoeft alleen in één van de vijf realisaties 13 m^3 /dag worden geïnfiltreerd, in de andere realisaties is de put niet nodig. Uit tabel 5 blijkt dat met name onttrekkingsput 1, in mindere mate ook 2 en 3, en injectieputten 8 en 10 van belang zijn voor het manipuleren. 

Het _totale_ manipulatiedebiet varieert per realisatie (rij 'manipuleren'). Volgens geologische variant 5 dient 573 m^3 /dag te worden omgeleid tegen 662 m^3 /dag bij variant 1. Gemiddeld genomen dient zo'n 632 m^3 /dag te worden omgeleid, de spreiding daaromheen bedraagt op basis van deze varianten zo'n 30 tot 60 m^3 /dag (zie grijze balk). De spreiding in het totale manipulatiedebiet is beduidend minder dan de spreiding in het debiet per put. Dit houdt in dat het systeem van meerdere putten het mogelijk maakt, in te spelen op de onzekerheid met betrekking tot het voorkomen van kleilenzen. Voorafgaand aan daadwerkelijke installatie maakt deze onzekerheid het echter niet mogelijk het debiet per put nauwkeurig te voorspellen. Dit debiet dient dus in de praktijk te worden ingeregeld. Hiervoor wordt in _toekomstig_ hoofdstuk 5 aanbevelingen gedaan. 


In bijlage E wordt het gecombineerde effect van het manipulatiesysteem en saneringssysteem op de stijghoogten in de verschillende modellagen weergegeven. 

3.4 **Geohydrologisch ontwerp sanering** 

Uit de optimalisatie met LINDO waarbij gebruik werd gemaakt van potentiële putlocaties zoals weergegeven in figuur 16 bleek, dat het saneringssysteem bestaat uit een tiental onttrekkingen, waarvan het debiet varieert van 1 tot 10 m^3 /dag verspreid over de randen van de chloroformcontour (zie figuur 18). In de praktijk blijken er volgens leverancier Grundfos echter geen onderwaterpompen te bestaan die minder dan 8 m^3 /dag kunnen onttrekken. Hierdoor werd een ondergrens gesteld aan het te onttrekken volume grondwater per mogelijke locatie van de saneringsputten. In eerste instantie werd deze beperking als extra randvoorwaarde in het optimalisatieproces meegenomen. Het optimalisatieproces werd hierdoor dermate complex dat er geen optimum kon worden gevonden, waarvoor door Schrage [Schrage, 1991] al wordt gewaarschuwd. Om te garanderen dat de optimalisatie zou resulteren in een saneringssysteem dat bestaat uit onttrekkingen van tenminste 8 m^3 /dag is het gebied waar saneringsputten geplaatst kunnen worden verkleind. Dit heeft tot gevolg dat er geen saneringsputten meer op de rand van de chloroformcontour geplaatst kunnen worden. De saneringsputten moeten dan meer onttrekken om verontreinigd grondwater binnen de chloroformcontour te houden. De locaties waar saneringsputten geplaatst kunnen worden zijn in rood weergegeven in figuur 16. In figuur 18 wordt het saneringssysteem voor de vijf realisaties weergegeven als resultaat van deze vijfde optimalisatie, waarbij in tabel 5 de onttrekkingsdebieten per saneringput voor de vijf realisaties zijn samengevat. Analoog aan het ontwerp van het manipulatiesysteem (zie paragraaf 3.3) wordt op basis van figuur 18 een saneringssysteem gekozen (zie figuur 19). Dit saneringssysteem wordt tegelijkertijd met het manipulatiesysteem in een zesde ronde geoptimaliseerd naar debiet. In tabel 5 wordt het debiet van de saneringsputten per realisatie per put en gesommeerd weergegeven. Uit tabel 5 blijkt, dat uit de tussenzandlaag door saneringsputten meer water moet worden onttrokken (62-97 m^3 /dag) om de verontreiniging te beheersen dan uit het ondiepe gedeelte van het eerste watervoerend pakket (40-58 m^3 /dag). Met name in de tussenzandlaag is de spreiding in het onttrekkingsdebiet per put over de 5 geologische realisatie groot. Putnummer 21 is in de laatste optimalisatie zelfs niet meegenomen omdat bij vorige optimalisaties maar in één realisatie een geringe hoeveelheid grondwater werd onttrokken. De verontreiniging wordt in de eerste 10 meter van het watervoerend pakket telkens met twee putten beheerst, te weten 26 en 27. De grondwaterstroming wordt in het watervoerend pakket minder sterk beïnvloed door de grilligheid van de kleilaag en de daarmee samenhangende onzekerheid. 

In bijlage F is de beheersende werking van het gecombineerde manipulatieen saneringssysteem (ook wel smart pump&treat systeem) voor de vijf geologische realisaties weergegeven. De figuur geeft de verplaatsing van fictieve verontreinigingsdeeltjes binnen de contour van de chloroformverontreiniging weer. Zo kan worden gecontroleerd of het definitieve ontwerp volgens de stationaire stromingssituatie voldoet aan de voorwaarde van geen verspreiding buiten het beheersgebied. Uit bijlage F blijkt dat, op twee plaatsen deeltjes ontsnappen. Het gaat dan om de voorste, stroomafwaartse grens van de chloroformverontreiniging en het uiterste zuidwest puntje van de chloroformverontreiniging. Deze geringe afwijking zal worden ondervangen door de uiteindelijke inregeling van het systeem zoals die op de locatie zal plaatsvinden. 

3.5 **Sanerende werking** 

Het ontwerp voor het saneringssysteem zoals dat er nu ligt, is gebaseerd op kwantitatieve randvoorwaarden zoals een minimaal saneringsdebiet en het invangen van al het grondwater uit 


de verontreiniging. De nu volgende paragrafen richten de aandacht op het verloop van de sanering zélf in termen van te zuiveren saneringsdebieten en het gedrag van de verontreiniging in de tijd. In paragraaf 3.5.1 wordt de vraag beantwoord welke stofconcentraties uiteindelijk te verwachten zijn in het zuiveringsinfluent. Dit wordt weergegeven door middel van doorbraakcurves waarin per onttrekkingsput het verloop van de vracht in de tijd wordt weergegeven. Op basis van die gegevens vindt het ontwerp en de dimensionering van de zuiveringsinstallaties plaats. 

3.5.1 _Opzet stoftransportmodel en doorbraakcurves_ Nu het geohydrologisch ontwerp van het manipulatie en saneringssysteem is gemaakt, kan de sanerende werking van het systeem worden bepaald. Hiertoe is met behulp van de stoftransport code MT3D [Zheng, 1992] de doorbraak van verschillende 'hoofd'verontreinigingen in de saneringsputten bepaald. Een schatting van de verontreinigingsvracht die doorbreekt in de saneringsputten is nodig voor het ontwerp van de zuiveringsinstallatie. In overleg met het consortium en Tebodin is besloten deze doorbraakcurves voor de vier hoofdverontreinigingen Tetrachloormethaan, Chloroform, CFK112 en Perchloorethyleen te berekenen. Hierbij is zowel de doorbraak per afzonderlijke saneringput bepaald als ook de totale vracht. 

Het stoftransportmodel heeft een vergelijkbare discretisatie als het locale grondwatermodel dat in paragraaf 3.2.2 is toegelicht. In eerste instantie is het uit 4 modellagen opgebouwd, waarbij de celgroottes in stappen oplopen van 10 bij 10 meter tot 100 bij 100 meter. De porositeit van de bodemlagen is op 30% geschat. In het stoftransport model is geen rekening gehouden met het optreden van afbraak, wel met het optreden van sorptie. De gehanteerde sorptieparameters zoals distributiecoëfficiënt ofwel retardatie zijn per stof en modellaag weergegeven in tabel 6. De retardatie is berekend bij een bulkdichtheid van 1,6 g/cm3 en een organisch stofgehalte van 5% voor de deklaag (L1) en 0,15% voor de onderliggende watervoerende lagen (L2 t/m L4). Daarvoor is de distributiecoëfficiënt tussen organisch koolstof en water Koc bepaald uit de distributiecoëfficiënt tussen octanol en water Kow met log(Koc) = a*log(Kow) + b [Schwartzenbach en Westall, 1985], waarin a 0,72 is en b 0,49. 

Tabel 6. Sorptie parameters distributiecoëfficiënt en retardatie voor Tetra, Per, Chloroform en CFK112 volgens Sutherland [Sutherland, 1997]. 

 Stof Log Kow Koc Kd' [kg/m3] Kd R Per L1 2,42 171 8,55 45,6 46,6 L2 t/m L5 2,42 171 0,26 1,39 2,39 Tetra L1 2,35 152 7,60 40,5 41,5 L2 t/m L5 2,35 152 0,23 1,22 2,22 Chloroform L1 1,64 47 2,35 12,5 13,5 L2 t/m L5 1,64 47 0,07 0,37 1,37 CFK112 L1 1,57 42 2,10 11,2 12,2 L2 t/m L5 1,57 42 0,06 0,32 1,32 

Het concentratieverloop in de tijd is voor 4 stoffen afzonderlijk gesimuleerd, te weten: tetrachloormethaan ofwel Tetra, perchloorethyleen ofwel Per, chloroform en CFK. Daarbij is de huidige verontreinigingssituatie als uitgangssituatie voor de transportberekeningen genomen. 


Daartoe zijn de concentratiemetingen, verricht in het kader van het ander onderzoek [Bakker, 1996] en het saneringsonderzoek [Bakker en Boode, 1997], als puntmetingen opnieuw geïnterpreteerd. In bijlage A zijn de gemeten concentraties van de verschillende stoffen per modellaag weergegeven. Het overzicht laat zien dat verder naar de diepte de hoeveelheid gegevens afneemt en daarmee de zekerheid over de werkelijke verontreinigingssituatie. Met de beschikbare kennis is zijn de puntmetingen tot een ruimtelijk beeld van de verontreinigingen geïnterpoleerd (zie bijlage G). Kennis over het vroegere bedrijfsproces is bij deze interpretatie meegenomen. 

_Tetrachloormethaan (Tetra) als puur product_ Over het terrein verspreid liggen enkele 'hot spots' waarbinnen de stofconcentraties zeer hoog zijn. Op basis van historische gegevens mag worden aangenomen dat tetrachloormethaan op deze plaatsen als puur product in de ondergrond terecht is gekomen. Vooralsnog is aangenomen dat Tetra als puur product door dichtheidstroming tot op de kleilaag die de tussenzandlaag van het watervoerend pakket scheidt, terecht is gekomen. Het voorkomen van Tetra als puur product in het onderste deel van de tussenzandlaag is gesimuleerd door de concentratie op die plekken constant te houden. Het effect van puur product is immers een constante nalevering van verontreiniging. De concentratie zal vlak boven het puur product in de tijd niet afnemen. Om niet te veel massa in te brengen in het stoftransportmodel is de modellaag die de tussenzandlaag representeert op geknipt in een laagje van 1,5 meter dikte waarin puur product wordt gesimuleerd en een laag daarboven van 7,5 meter dik. De concentratie in de puur product zones werden gelijk gesteld aan de gemeten concentratie in de omgeving van de zones. Dit is meestal een orde grootte minder dan de oplosbaarheid van puur product. Toch is ervoor gekozen om de concentratie niet gelijk te stellen aan deze oplosbaarheid, omdat het puur product verspreid aanwezig is in de 1,5 meter dikke laag. In feite wordt een opgeschaalde, effectieve concentratie opgegeven. 

3.5.2 _Resultaten_ In bijlage H is de doorbraak van de verschillende verontreinigingen per saneringsput weergegeven voor een periode van 10 jaar vanaf het moment van opstarten. In figuur 20 wordt de totale vrachtverwijdering (mg/dag) voor de hoofdverontreinigingen Tetra, Per, chloroform en CFK weergegeven. In deze grafieken representeert elke gekleurde lijn de totale doorbraak voor één geologische variant. Uit deze figuur blijkt, dat de doorbraak bepaald wordt door Chloroform en CFK112, de bijdragen van Tetra en Per zijn beduidend minder. Verder blijkt de doorbraak van Chloroform en Per vrij stabiel over de periode van 10 jaar, dit in tegenstelling tot de doorbraak van Tetra en CFK112: de maximale doorbraak van Tetra vindt volgens de berekeningen pas enkele jaren plaats na het opstarten van het systeem. Bij CFK112 valt voor enkele geologische realisaties op, dat de doorbraak 5 tot 6 jaar na het opstarten van het systeem een orde grootte afneemt. Deze doorbraak wordt volledig bepaald door de doorbraakconcentraties in put 20 die vlak bij de verontreinigingskern ligt. Het grote debiet in verhouding met naastgelegen saneringsputten zorgt ervoor dat het overgrote deel van de verontreiniging door deze put wordt afgevangen. De piekverontreiniging blijkt na deze 5 tot 6 jaar voorbij te zijn. 


 CFK, tota a l 

 100 

 1000 

 10000 

 100000 

 1000000 

 0 2 4 6 8 10 

 tijd [ja re n] 

 mg/dag 

real1 real2 real3 (^) real4 real5 **Chloroform , totaal** 100 1000 10000 100000 1000000 0 2 4 6 8 1 **tijd [jare n] mg/dag** 0 real1 real2 real3 real4 real5 **PER totaal** 100 1000 10000 100000 0 2 4 6 8 10 **tijd [jaren] mg/dag** real1 real2 real3 real4 real5 **Te tra chloormethaa n, tota al** 100 1000 10000 100000 0 2 4 6 8 10 **tijd [jare n] mg/dag** real 1 real 2 real 3 real 4 real 5 Fig. 20. Doorbraakcurves (mg/dag) van Tetrachloormethaan en CFK112, Per en Chloroform. Uit de doorbraak van de verontreinigingen in de afzonderlijke putten (bijlage H) zijn enkele conclusies te trekken: 

- Bij nagenoeg iedere put bestaan er onderlinge verschillen tussen het stofvrachtverloop van     de vijf realisaties. 

- De saneringsputten pompen uiteenlopende stofvrachten op. Dit is enerzijds te verklaren uit     het feit dat sommige putten op een sterker vervuilde locatie staan en anderzijds doordat de     putdebieten verschillen. Een put met een groot debiet pompt daarmee ook een grotere     stofvracht omhoog. 

- De curven in de grafiek voor het totale verloop van de vrachten vertonen veel minder grote     onderlinge verschillen dan bij de individuele putten te zien was. Door de sommatie worden     over alle putten worden individuele uitschieters afgevlakt. 

- De vrachten die in de zes putten worden aangetroffen variëren sterk van grootte. De totale     vracht blijkt nagenoeg geheel te worden bepaald door drie of vier saneringsputten met hoge     stofvrachten. 

De maximale stofvrachten zoals die voorkomen in de totaalstroom richting de zuivering worden in tabel 7 weergegeven. Het getal dat vermeld staat geeft het maximum aan dat op grond van de 5 realisaties mag worden verwacht. 

Tabel 7. Maximale stofvracht in totaalstroom. 

 Stof Bovengrens stofvracht (mg/dag) Tetra Orde 50.000 Chloroform Orde 200.000 Cfk Orde 200.000 Per Orde 20.000 


_Betrouwbaarheid doorbraakcurves_ Bij het vervaardigen van het stoftransportmodel zijn enkele aannames gemaakt die de betrouwbaarheid van de berekeningen beïnvloeden. Afgezien van de betrouwbaarheid van de verontreinigingssituatie en het stromingsbeeld zoals die zijn ingevoerd in het model, gaat het dan om de vereenvoudiging van processen zoals sorptie en afbraak. Zoals in het begin van deze paragraaf is genoemd, is afbraak van verontreinigingen verwaarloosd. Dit is een sterke vereenvoudiging van de werkelijkheid. Het voorkomen van chloroform, een stof die geen deel uitmaakte van het productieproces en een afbraakproduct van Tetra is, wijst erop dat Tetra afbreekt. In het kader van het NOBIS-project Restrisk is door Hetterschijt en Te Stroet [Hetterschijt en Te Stroet, 1998] een schatting gegeven van de afbraaksnelheid van Tetra. De halfwaardetijd van Tetra werd door hen geschat op 10-14 jaar. Aangezien geen afbraakproducten van chloroform werden aangetroffen spraken Hetterschijt en Te Stroet [Hetterschijt en Te Stroet, 1998] de verwachting uit dat de sequentiële afbraak van Tetra stopt bij chloroform en niet verder verloopt via dichloromethaan en methylchloride naar onschadelijke eindproducten. Het ophopen van chloroform door afbraak van Tetra is niet meegenomen in deze transportmodellering. Hetterschijt en Te Stroet [Hetterschijt en Te Stroet, 1998] geven aan dat afbraak van Per, Tri en CFK's op deze locatie niet aannemelijk is. Het gevolg van het niet meenemen van afbraakterm is dat de doorbraak van chloroform daardoor wordt onderschat. Een andere vereenvoudiging betreft het sorptieproces van verontreinigingen aan de bodem. In deze studie is dit proces gemodelleerd als een evenwichtsproces, dat wil zeggen dat de uitwisseling van verontreinigingen tussen de bodem en het grondwater momentaan verloopt. Dit is een grove vereenvoudiging gezien het feit dat met name de deklaag veel organisch stof en leemlenzen bevat, die kunnen fungeren als immobiele zones (zie ook paragraaf 2.2). Het effect van deze vereenvoudiging is dat de doorbraak van stoffen in lage concentraties volgens het model later plaats vindt dan in werkelijkheid en dat de doorbraak volgens het model veel minder lang aanhoudt dan in werkelijkheid. Resumerend kan worden gesteld dat de vereenvoudiging van sorptieprocessen tot gevolg heeft dat de doorbraakcurves niet het daadwerkelijke saneringsverloop weergegeven. De maximale vracht die volgens het model doorbreekt, zal echter wel overeenkomen met de werkelijke maximale vracht. De doorbraakcurves zijn daarom wel bruikbaar voor het dimensioneren van de zuivering, waarvoor de transportmodellering onder andere bedoeld was. 

_Potentiële uitbreiding van het saneringssysteem_ In het ontwerpproces is rekening gehouden met de onzekerheid ten aanzien van de heterogeniteit van de ondergrond en is een automatische optimalisatieroutine gevolgd. Dit heeft geresulteerd in een saneringsen omleidingssysteem zoals in tabel 7 beschreven. Buiten deze systematiek om is voorgesteld om vier saneringsputten met een gezamenlijk debiet van 20 m^3 per dag aan het systeem toe te voegen vanwege capaciteitsruimte op de te plaatsen zuivering. De locaties van de putten, genummerd 28 t/m 31, is weergegeven in figuur 19 en komt voort uit de overweging dat naast de positie van de huidige saneringsputten, met name aan de randen van de verontreiniging, de extra putten gericht worden op de bronnen van de verontreiniging. 

3.6 **Effecten op de omgeving** 

3.6.1 _Inleiding_ Het systeem van manipulatieen saneringsputten is ontworpen voor de sanering van de voormalige locatie van Akzo Nobel. Het effect van dit systeem op de grondwatersituatie blijft echter niet beperkt tot de locatie zelf maar zal ook de grondwatersysteem in de omgeving beïnvloeden. In deze paragraaf wordt achtereenvolgens ingegaan op het effect van het 


ontworpen systeem op verdrogingsgevoelige vegetatie en op de beheersende werking van het beheersysteem van Budelco. 

3.6.2 _Verdrogingsgevoelige vegetatie_ Het grootste effect van het manipulatieen saneringssysteem op de freatische grondwaterstand is te verwachten van de putten van het manipulatiesysteem vanwege de grote capaciteit van deze putten. Dit effect is eenvoudig te bepalen door de berekende stijghoogten van voor de ingreep te vergelijken met de berekende stijghoogten ten gevolge van het puttensysteem. 

In figuur 21 is het gemiddelde effect rondom de locatie weergegeven. Verhogingen van de grondwaterstand zijn uitgedrukt in positieve waarden en verlagen in negatieve waarden. Aan deze figuur liggen effectberekeningen voor de vijf geologische realisaties ten grondslag, waarvan vervolgens het minimum, maximum en gemiddeld effect is bepaald (zie bijlage I). In de figuur is duidelijk de nul-contour te onderscheiden die de locatie ten noordoosten passeert. Stijgingen van de grondwaterstand treden op ten noordoosten van deze lijn en de dalingen aan de andere zijde. Zoals verwacht, zijn de veranderingen in de waterstand het grootst rond de putten die deel uit maken van het manipulatiesysteem. Voor de stijgingen geldt dat over een afstand van minder dan 250 meter rond de infiltratieputten de invloed is afgenomen tot 5 cm. Waterstanddalingen van 5 cm en groter treden op in een gebied rond de onttrekkingslocaties met een breedte van maximaal 300 meter. 

Fig. 21. Stijghoogteveranderingen ten opzichte van de oorspronkelijke situatie. 

Beeldbepalend voor de natuurlijke omgeving van het projectgebied zijn het heidelandschap en de grote vennen van De Hoort en Ringselven. Deze vennen grenzen nagenoeg direct aan de voormalige locatie van Akzo Nobel en strekken zich tot 3 kilometer naar het Noordwesten uit. De Loozerheide ligt op twee kilometer afstand noordelijk van de locatie. Binnen de genoemde gebieden zijn enkele deelgebieden te onderscheiden waarin hydrologisch gevoelige vegetaties voorkomen. Deze liggen met name in de periferie van het vennenen heidegebied, onder andere op enkele locaties ten westen van de voormalige locatie van Akzo Nobel. Naast verdroogde heide met daarin het Pijpestrootje, een freatofyt, komt volgens de ecohydrologische atlas 


[Provincie Limburg, 1997] in enkele nabijgelegen turfputten het Klein blaasjeskruid voor. Deze inventarisatie is gemaakt in 1990. Rond die tijd was er op het terrein een onttrekking actief van 1,5 miljoen m^3 /jaar. Na stopzetting ervan is de stijghoogte in het watervoerend pakket met ca. 1,0 m gestegen. 

Een belangrijk aandachtspunt in de effectenstudie betreft de optredende verlagingen. Zoals gezien treden verlagingen groter dan 5 cm met name op in een klein gebied direct rond de onttrekkingsputten. 

Bij deze effectberekening dient nog te worden opgemerkt dat deze is gebaseerd op basis van een stationaire situatie. Uit tijd-stijghoogtereeksen gemeten in de tussenzandlaag blijkt de natuurlijke schommeling in de freatische grondwaterstand alleen al anderhalve meter te bedragen (zie figuur 22). Ook in een meetreeks uit 1999 is een natuurlijke fluctuatie van ca. 0,5 m te ontdekken (zie figuur 25). 

 Verdrogingseffecten op de natuurlijke omgeving kunnen op grond van de berekeningen worden verwaarloosd. Een mogelijke uitzondering hierop is een gebied ten zuidwesten van de locatie. Binnen een oppervlakte van 500 bij 300 meter komen hier mogelijk turfputten met bovengenoemde gevoelige vegetatie voor. 

 Putnummer 57HP0074, lokatie 170.680 / 358.490 

 3100 

 3150 

 3200 

 3250 

 3300 

 3350 

 3400 

 01-Jan-8827-Oct-8823-Aug-8919-Jun-9015-Apr-9109-Feb-9205-Dec-9201-Oct-9328-Jul-9424-May-9519-Mar-9613-Jan-9709-Nov-9705-Sep-9802-Jul-99 

 datum 

 stijghoogte in cm t.o.v. NAP 

Fig. 22. Stijghoogteverloop in de tussenzandlaag (bron: OnLine GrondwaterArchief, OLGA). 

3.6.3 _Beïnvloeding beheerssysteem Budelco_ De effecten van het ontworpen smart pump&treat systeem op het beheerssysteem van Budelco zijn door Tauw berekend met een regionaal grondwater model in MLAEM dat ten grondslag ligt aan het door TNO opgezette regionale model. Hiervoor is gekozen omdat effecten in de vorm van verschillen in verlagingen en intrekgebieden inzichtelijk worden gemaakt. Door een ingreep als het smart pump&treat systeem voor de voormalige locatie van Akzo Nobel met hetzelfde model door te rekenen, als waarmee ook het beheersysteem van Budelco werd ontworpen, wordt vermeden dat verschillen als gevolg van wijze van modelleren (eindige differentie of analytische elementen) geïnterpreteerd worden als werkelijke effecten. Voor de gevoeligheidsanalyse zijn stroombaanberekeningen uitgevoerd met de meest kritische smart pump&treat variant van de vijf mogelijke systemen (zie tabel 7). Wanneer blijkt dat er in meest kritische situatie volledige beheersing van het Budelco-terrein plaatsvindt geldt dat tevens voor de andere varianten. Het selectiecriterium voor een sanering met het grootste negatieve effect op het Grondwater Beheerssysteem (GBS) van Budelco bestaat uit twee punten. Allereerst dient het 


saneringsdebiet minimaal te zijn. Ook dan is de onttrekking echter groter dan nul en is het effect op het GBS positief omdat de "natuurlijke achtergrondstroming" hierdoor afneemt; het GBS debiet mag zelfs kleiner zijn. Ten tweede dient het manipulatiedebiet, met netto debiet nul, maximaal te zijn. De infiltratiezijde van het manipulatiesysteem ligt namelijk nabij de bovenstroomse zijde van het Budelco-terrein. Deze infiltratie vergroot de "natuurlijke stroming" en daarmee in principe ook het benodigde beheersdebiet van het GBS. Op basis van deze selectiecriteria is gekozen voor een berekening met een combinatie van het manipulatiesysteem van realisatie 1 en het saneringssysteem behorend bij realisatie 4 (zie tabel 7) De berekende stroombanen zijn in figuur 23 weergegeven. 

Fig. 23. Stroombanen richting GBS zonder (a) en met (b) Akzo-Nobel onttrekking. 

Het Budelco-terrein is het in de figuur rood omlijnde complex. Bij de vergelijking van de stroombaanfiguren blijkt dat zowel met als zonder de Akzo Nobel-onttrekking er sprake is van 


volledige beheersing van het Budelco terrein door het GBS. Het infiltratiewater van het manipulatiesysteem van Akzo Nobel mondt grotendeels uit in de putten 15, 16 en 17, gelegen aan de oostzijde van het Budelco-terrein. Op basis van de uitgevoerde berekeningen zijn er dus geen relevante negatieve effecten op de werking van het GBS te verwachten. 

3.6.4 _Verstopping als praktisch knelpunt bij de implementatie van smart pump&treat_ In het in paragraaf 3.3 ontworpen smart pump&treat systeem is sprake van de omleiding van schoon grondwater. Een debiet van 650 m^3 /dag wordt bovenstrooms door manipulatieputten onttrokken en diezelfde hoeveelheid wordt benedenstrooms geïnfiltreerd. Uit de praktijk is bekend dat er een kans bestaat dat in de infiltratieputten verstopping optreedt. Het gevolg hiervan is dat het infiltratiedebiet waarop het systeem was ontworpen niet kan worden gerealiseerd. Het systeem zal daardoor in meerdere of mindere mate ontregelen, wat de betrouwbaarheid van de beheersing kan verminderen, indien geen maatregelen worden genomen om verstoppingen ongedaan te maken. 

Om dit praktische knelpunt te ondervangen is het van belang inzicht te krijgen in de kans op verstopping en aan te geven op welke wijze hiermee moet worden omgesprongen. In het kader van het NOBIS-project "implementatie beslissystematiek ontwerp en onderhoud van infiltratieen onttrekkingsmiddelen" is onderzoek verricht naar verstoppingsrisico's van het manipulatiesysteem voor de voormalige locatie van Akzo Nobel [Bakker e.a., 1999]. Een samenvatting uit dit onderzoek bestaande uit enkele conclusies wordt hieronder weergegeven. 

In het onderzoek worden de verstoppingsrisico's beoordeeld op basis van de eigenschappen van het grondwater uit de tussenzandlaag en het watervoerend pakket. Uitgaande van mogelijke oorzaken van verstopping zijn enkele basisgegevens geïnterpreteerd die betrekking hebben op de lokale hydrologie en de bodemen grondwatersamenstelling. 

_Accumulatie van deeltjes_ Dit risico kon voor de locatie niet geëvalueerd worden omdat geen membraanfilterindex is bepaald wat een maat voor het aantal zwevende deeltjes. De relatief hoge doorlatendheid in genoemde bodemlagen wijst op grof materiaal met een klein gehalte aan fijne fractie. Dit zou kunnen wijzen op een laag risico. 

_Fysisch-chemische neerslagen_ Grondwateranalyses in beide bodemlagen geven aan dat ijzer en mangaan de kritische waarden overschrijden. Dit betekent dat bij elk contact met zuurstof neerslagen gevormd kunnen worden. De gemeten zuurstofgehaltes in ondiep grondwater zijn laag en omdat dezelfde lage waarden in diep grondwater gemeten worden, is het waarschijnlijk dat zuurstof afwezig is. Allerlei waarnemingen ondersteunen dit: hoge ijzer (II) gehaltes, methaanvorming, sulfaatreductie en negatieve tot lage positieve waarden voor de redoxpotentiaal. Dit betekent dat er geen verstopping door ijzer of mangaan zal optreden zolang de bovenzijde van het putfilter voldoende diep is gesteld. Een risico ontstaat bij het (gedeeltelijk) aantrekken van ondiep grondwater en bij het inlekken van zuurstof in het systeem. 

_Biologisch-chemische neerslagen_ Methaan is een product van anaërobe afbraak van organische verontreinigingen en wordt in hoge gehaltes aangetroffen in de infiltratie zone. Methaan kan bij oxidatie met zuurstof tot biologische verstopping leiden. Naast methaan kunnen ook hoge sulfaatconcentraties kritisch zijn indien er sulfaatreductie optreedt. Hoewel sulfide niet is bemonsterd, spreken de boorbeschrijvingen over de geur van rotte eieren, wat een indicatie is voor H 2 S. Gevormd sulfide zal voor een groot deel vastgelegd worden als onoplosbaar metaalsulfide. 

_Accumulatie van gassen_ 


Het grondwater bevat geringe gehaltes aan vrij kooldioxide. Wanneer het systeem op overdruk wordt gehouden zijn de risico's op gaslogging nihil. 

Uit het onderzoek komt de aanbeveling dat voor het waarborgen van een ongestoorde werking van onttrekkingsen retourmiddelen een goed opgestelde meeten maatregelenprogramma nodig is. Het programma, gebaseerd op analyse van betrouwbare gegevens en diagnose van verstopping, is een cyclisch proces dat continu gemonitoord dient te worden. Alleen op deze wijze kunnen juiste acties tijdig genomen worden. 

Uit bovenstaande blijkt dat actieve monitoring een kritisch onderdeel is. In fase 2 wordt om die reden een monitoringsen actiestrategie ontwikkeld speciaal gericht op het signaleren en verhelpen van deze verstoppingsrisico's. Daarnaast dient bij het technisch ontwerp rekening gehouden te worden met regeneratietechnieken als het terugspoelen van de putten. 


##### HOOFDSTUK 4 

#### ROBUUSTHEID ONDER DYNAMISCHE OMSTANDIGHEDEN 

4.1 **Inleiding** 

Zowel het manipulatiesysteem als het saneringssysteem zijn ontworpen uitgaande van stationaire omstandigheden. In werkelijkheid zullen zich echter veranderingen voordoen in het hydrologische systeem op een zekere tijden ruimteschaal. Te denken valt aan seizoensinvloeden of een afwisseling tussen droge en natte jaren. Hierdoor kunnen de stijghoogten en daarmee stroomsnelheden en stromingsrichtingen variëren. Afhankelijk van de grootte van deze variaties bestaat de mogelijkheid dat een deel van de verontreiniging aan het saneringssysteem ontsnapt of 'weglekt'. Daarom is het van belang om na te gaan of de invloed van de dynamiek van het grondwatersysteem dusdanig is dat een dergelijke lek ook werkelijk optreedt. Zo niet dan is het systeem robuust genoeg. Als het wel het geval blijkt te zijn, is dit aanleiding voor een gerichte monitoring mogelijk in combinatie met tussentijdse bijstellingen van het systeem. Dit hoofdstuk beschrijft deze analyse in een aantal stappen. De tweede paragraaf wordt allereerst de dynamiek vanuit gemeten stijghoogten gekwantificeerd. Om vervolgens de gevolgen van die dynamiek voor de beheersing van de verontreiniging te kunnen bepalen zijn stromingsberekeningen uitgevoerd. Deze worden in paragraaf 4.3 toegelicht. Tot slot volgen in paragraaf 4.4 de conclusies aangevuld met aanbevelingen voor de opzet van een monitoringsnetwerk. 

4.2 **Systeembeschrijving** 

Om inzicht te krijgen in de dynamiek zoals die zich voordoet op de voormalige locatie van Akzo Nobel zijn stijghoogtemetingen uitgevoerd in zowel het watervoerend pakket als de tussenzandlaag. Deze hebben plaatsgevonden over een periode van 10 maanden (27 april 199928 januari 2000) met tijdstappen van een half uur. In zowel de tussenzandlaag als het watervoerend pakket zijn op vier locaties metingen verzameld gebruikmakend van in totaal vijf peilbuizen. Bij drie peilbuizen zijn namelijk metingen in zowel de tussenzandlaag als het watervoerend pakket uitgevoerd. In figuur 24 staan deze vijf locaties aangegeven. 


Fig. 24. Positie van de 8 meetpunten (4 per laag) op 5 locaties. 

Het verloop van de stijghoogte van een van de meetpunten in de tussenzandlaag is in figuur 25 weergegeven. Het maximale verschil over de gemeten periode bedraagt bijna 50 cm en komt overeen met het beeld dat de andere meetlocaties vertonen. In de figuur is duidelijk een dalend en stijgend verloop in de stijghoogte te ontdekken wat mogelijk wijst op een seizoensafhankelijke variatie veroorzaakt door een droge en natte periode. 

 3350 

 3360 

 3370 

 3380 

 3390 

 3400 

 3410 

 3420 

 27-Apr-9917-May-9906-Jun-9926-Jun-9916-Jul-9905-Aug-9925-Aug-9914-Sep-9904-Oct-9924-Oct-9913-Nov-9903-Dec-9923-Dec-9912-Jan-00 

 Datum 

 stijghoogte in cm t.o.v. NAP 

Fig. 25. Stijghoogteverloop in een meetpunt in de tussenzandlaag. 

4.2.1 _Kwantificering van de dynamiek_ Met behulp van de stijghoogtemetingen in de tijd is het mogelijk om de dynamiek van de grondwaterstand te kwantificeren. Wanneer de grondwaterstand rond de locatie vereenvoudigd wordt tot een vlak, betekent dynamiek in feite de wijze waarop dat vlak in de tijd kantelt. De nieuwe helling en de richting van de helling zijn indicatoren voor veranderingen in zowel de stroomsnelheden als de stroomrichtingen ter plaatse. De helling wordt uitgedrukt in de stijghoogtegradiënt terwijl de richting waarin de gradiënt afneemt overeen komt met de stromingsrichting van het grondwater. Kwantificering van de gradiënt en de richting is mogelijk door per tijdstap het dan voorkomende stijghoogtevlak te bepalen. 

De ligging van een stijghoogtevlak is te bepalen wanneer er drie in een zelfde laag gemeten stijghoogten bekend zijn. Zoals figuur 26 laat zien zijn er per laag echter vier meetpunten beschikbaar zodat het stijghoogtevlak kan worden bepaald door met de kleinste-kwadratenmethode een vlak door de 4 stijghoogten te 'fitten'. Op elk tijdstip kunnen zo de stijghoogtegradiënt en de stromingsrichting op de locatie worden bepaald. De resultaten hiervan voor zowel de tussenzandlaag als het watervoerend pakket zijn weergegeven in figuur 26. De richting van de stroming is gedefinieerd als hoek in het RMD coördinatenstelsel ofwel ten opzichte van het oosten. 

De schommeling in de grafieken, met name te zien in het richtingsverloop in het watervoerend pakket, wordt veroorzaakt doordat kleine variaties in de stijghoogtemetingen over een korte afstand de geringe gradiënt en stromingsrichting toch sterk beïnvloeden. 

De resultaten laten zien dat er zeker sprake is van dynamiek. In het gradiëntverloop voor de tussenzandlaag is een duidelijke toename gedurende de zomerperiode te zien die enkele maanden aanhoudt. Deze toename bedraagt ongeveer 50% ten opzichte van de gradiënt tijdens de winterperiode. In die zelfde periode lijkt de stromingsrichting zich enkele graden richting het 


oosten te verplaatsen. In het watervoeren pakket is de invloed van de dynamiek ook terug te vinden. De gradiënt loopt daar op van 0,02 tot 0,04 cm/m. Vanwege deze geringe helling over de korte afstand tussen de meetpunten (maximaal 200 m) zijn de invloeden van kleine veranderingen in stijghoogten aanleiding tot sterke richtingsveranderingen van het vlak. Dit verschijnsel is duidelijk in figuur 26a terug te zien. 

 Stromingsrichting van 2 stijghoogtevlakken in de tijd 

 0 

 10 

 20 

 30 

 40 

 50 

 60 

 70 

 80 

 90 

 27-Apr-9917-May-996-Jun-9926-Jun-9916-Jul-995-Aug-9925-Aug-9914-Sep-994-Oct-9924-Oct-9913-Nov-993-Dec-9923-Dec-9912-Jan-00 

 Datum 

 Hoek in graden 

 tussenzandlaag watervoerend pakket 

 Gradienten voor 2 stijghoogtevlakken in de tijd 

 0.00 

 0.02 

 0.04 

 0.06 

 0.08 

 0.10 

 0.12 

 0.14 

 0.16 

 0.18 

 0.20 

 0.22 

 0.24 

 27-Apr-9917-May-996-Jun-9926-Jun-9916-Jul-995-Aug-9925-Aug-9914-Sep-994-Oct-9924-Oct-9913-Nov-993-Dec-9923-Dec-9912-Jan-00 

 Datum 

 gradient [cm/m] 

 tussenzandlaag watervoerend pakket 

Fig. 26. Verloop van stijghoogtevlak in de tijd; stromingsrichting [a] en gradiënt [b]. 

Naast bovengenoemde divermetingen hebben er gedurende een jaar 8 meetronden plaatsgevonden waarin handmatig de stijghoogten in ongeveer 20 peilbuizen zijn bepaald (voor peilbuislocaties zie figuur 27). Omdat het hier om meer dan 4 meetpunten gaat is de ligging van het stijghoogtevlak met een grotere nauwkeurigheid te bepalen. Een overzicht van de stijghoogten gedurende de meest complete meetronden is bijlage J weergegeven. Berekeningen van de stijghoogtevlakkken door deze punten leveren zowel de stromingsrichting als de bijbehorende stijghoogtegradiënt op (zie tabel 8). 


Tabel 8. Stijghoogtegradiënten en stromingsrichtingen op de locatie. 

 tussenzandlaag watervoerend pakket datum meetronde 

 stromingsrichting (graden) 

 gradiënt (m/m) 

 stromingsrichting (graden) 

 gradiënt (m/m) 21-04-99 52 0.0013 4 0.00026 27-04-99 81 0.0015 21 0.00021 28-07-99 48 0.0015 51 0.00051 15-10-99 31 0.00037 28-10-99 46 0.0018 21 0.00035 28-01-00 56 0.0014 25 0.00031 

Deze waarden laten een nagenoeg zelfde verloop zien in vergelijking met de continue divermetingen. Zo nemen de gradiënten in de tussenzandlaag in de zomer en de maanden daarna toe. De waarden van zowel de gradiënten als de stromingsrichtingen hebben gelijke orde van grootte vergeleken met de divermetingen. De berekeningen op basis van meer metingen leiden niet tot sterk afwijkende resultaten. Het gradiëntverloop in figuur 26 is daarmee redelijk nauwkeurig. 

Fig. 27. Peilbuizen gebruikt voor handmatige meetronden. 

4.2.2 _Interpretatie_ Een volgende stap is het verklaren van het gradiëntverloop en met name de gradiënttoename in de zomerperiode. Op basis van die verklaring is de dynamiek in het grondwatermodel in te brengen. De veronderstelling is, dat het kanaal ten zuiden van de locatie de stijghoogte op de locatie beïnvloedt wat leidt tot het waargenomen gradiëntverloop. Het peil in het kanaal (35,20 m + NAP) is hoger dan de stijghoogten in de omliggende pakketten waardoor kwel in de richting van de locatie optreedt. In de zomerperiode zullen de waterstanden dichtbij het kanaal door de aanvoer van kwel minder sterk dalen dan verder van het kanaal af. Dit verschil levert de gradiëntstoename over de locatie op. 


Om te onderzoeken of het kanaal het veronderstelde effect heeft, is met het ontwikkelde TNO model een gevoeligheidsanalyse uitgevoerd. Deze analyse is gericht op de vraag of de hogere gradiënten, zoals die uit de metingen naar voren komen, te realiseren zijn door de infiltratieweerstand van het kanaal aan te passen. In de analyse is de infiltratieweerstand in een aantal stappen teruggebracht van de oorspronkelijke 500 dagen naar 50 en zelfs naar 10 dagen. Op basis van de modelresultaten zijn de gradiënten en de stromingsrichtingen bepaald die laten zien dat de gemeten hoge gradiënten, oplopend tot rond de 0,002 m/m, zeker te bereiken zijn. Het is dus mogelijk om door middel van een weerstandsverlaging van het kanaal de hoge gradiënten te realiseren. Dergelijke lage infiltratieweerstanden lijken bijna onrealistisch en het zou betekenen dat het model op dit punt niet juist is. 

Om op basis van metingen te kunnen vaststellen of de grondwaterstand werkelijk aan het kanaal 'hangt' zijn 3 extra peilbuizen langs het kanaal geplaatst. De ligging van de oorspronkelijke verzameling meetpunten geeft namelijk niet volledige zekerheid omtrent de gradiënten en bijbehorende richtingen. Dit komt omdat de punten relatief ver verwijderd liggen van het kanaal en de oriëntatie voornamelijk evenwijdig aan het kanaal is. Uit de nieuwe meetronden blijkt dat de stijghoogten in de drie extra punten niet hoger zijn dan op de locatie zoals verwacht maar juist lager (zie figuur 28). Op basis van deze resultaten wordt geconcludeerd dat het niet mogelijk is dat het kanaal de waterstanden rond de locatie beïnvloedt om daarmee de dynamiek te veroorzaken. 

Fig. 28. Positie van extra meetpunten (genummerd), inclusief stijghoogten. 

Een tweede mogelijke verklaring voor de waargenomen dynamiek is gelegen in de neerslag. Wanneer kan worden aangetoond dat er een duidelijke relatie is tussen het neerslagverloop, of beter de grondwateraanvulling, en het stijghoogteverloop is dat een sterke aanwijzing. Door de neerslag te variëren kan de dynamiek dan ook in de modelberekeningen worden ingebracht. 


Wanneer de relatie niet kan worden gelegd zijn meerjarige trend of de vertragende werking van berging in het gebied mogelijke verklaringen. 

De relatie tussen de grondwateraanvulling en het stijghoogteverloop is zichtbaar te maken door in een grafiek zowel het gemeten als het berekende stijghoogteverloop uit te zetten. Uitgaande van een gemeten stijghoogte op tijdstip 0 is het verdere verloop te bepalen door per tijdstap een positieve dan wel een negatieve grondwateraanvulling te verrekenen. De werkelijke grondwateraanvulling is eenvoudig benaderd op basis van KNMI gegevens over neerslag en verdamping (zie bijlage L). Zijdelingse toeof afstroming en stroming naar het watervoerende pakket zijn in de analyse niet meegenomen. Grondwateraanvulling is de neerslag over een periode minus de verdamping. Voor de bepaling van de bijbehorende stijghoogteverandering is een 'berging'-parameter nodig. Deze is niet constant in de tijd en hangt onder andere af van de porositeit van de bodem en van de bergingsmogelijkheden in de onverzadigde zone. Toch wordt er een constante waarde voor deze parameter bepaald door deze steeds aan te passen totdat er een goede 'fit' met het gemeten verloop ontstaat. Voor de periode van april 1999 tot januari 2000 is op die manier het stijghoogteverloop geschat. Figuur 29 geeft in een figuur zowel het gemeten als het berekende stijghoogteverloop weer. 

 Stijghoogteverloop in de tussenzandlaag 

 3350 

 3355 

 3360 

 3365 

 3370 

 3375 

 3380 

 3385 

 3390 

 3395 

 3400 

 07/03/99 04/04/9902/05/99 30/05/99 27/06/9925/07/99 22/08/99 19/09/99 17/10/9914/11/99 12/12/99 09/01/00 

 datum 

 stijghoogte in cm 

 divermeting berekening 

Fig. 29. Gemeten en berekende grondwaterstand. 

De figuur laat duidelijk zien dat de stijghoogten in de tussenzandlaag direct worden beïnvloedt door de neerslag. Een piek in het berekende verloop vindt vrijwel direct plaats met een piek in het werkelijk gemeten verloop. Dat de gemeten piek rond augustus ver boven het berekende verloop uitsteekt kan te maken hebben met lage bergingsmogelijkheden in die periode. Op basis van deze analyse is een sterke relatie tussen de neerslag en de stijghoogte in de tussenzandlaag aangetoond. 

In het algemeen wordt dynamisch gedrag in het grondwater veroorzaakt door dynamiek in de drijvende krachten van het grondwatersysteem. Voorbeelden hiervan zijn de infiltratie vanuit het kanaal, de grondwateraanvulling maar ook de achtergrondstroming. Er is als vastgesteld dat de infiltratie vanuit het kanaal niet de oorzaak van de dynamiek is. Ook dynamiek in de achtergrondstroming in het watervoerend pakket lijkt niet de oorzaak te zijn van de grotere gradiënten in de tussenzandlaag. Het dynamisch verloop van de tussenzandlaag en het 


watervoerend pakket zou in dat geval op de voormalige locatie van Akzo Nobel nagenoeg gelijk moeten zijn. De conclusie luidt dat de dynamiek, die uit de gemeten stijghoogten is afgeleid, alleen te verklaren is door veranderingen in de neerslag. Tot welke gevolgen dit leidt voor de beheersing van de verontreiniging komt in de volgende paragraaf aan de orde. 

4.3 **Bepaling van de 'lekterm'** 

In de vorige paragraaf is gesteld dat de variatie in de grondwateraanvulling te gebruiken is voor het inbrengen van de waargenomen dynamica in het grondwatermodel. De meest eenvoudige manier om neerslagvariatie over een jaar te vertalen is het opdelen in een natte en een droge periode. Bij de modelberekeningen voor de stationaire situatie is uitgegaan van een gemiddelde neerslag van 0,7 mm/dag wat neerkomt op 255 mm per jaar. 

In een eerste analyse is de neerslag in de natte periode met 25% vermeerderd tot 0,88 mm/dag en in de droge periode met 25% verminderd tot 0,53 mm/dag. Het effect van deze wijzigingen is per periode afzonderlijk bekeken. Elk scenario is hiervoor als stationaire situatie gemodelleerd, namelijk bij een netto neerslag van 0,88 mm/dag (nat) en 0,53 mm/dag ('droog'). Het effect van deze wijzigingen op het verloop van stroombanen vanuit de verontreiniging is in bijlage M weergegeven. 

De resultaten laten zien dat bij de modellering met minder neerslag de verontreiniging voor een tweetal realisaties wordt beheerst, zowel in de tussenzandlaag als in het watervoerend pakket (niet weergegeven). Omdat de neerslag is verlaagd, zal het intrekgebied van het ontworpen saneringssysteem zich vergroten waardoor de verontreiniging door het onttrekkingssysteem ruimschoots wordt ingevangen. Permanent meer neerslag heeft tot gevolg dat in de tussenzandlaag de verontreiniging wordt beheerst. Alleen in het watervoerend pakket lekt op een termijn van 80 jaar de verontreiniging over een smal grensdeel weg. De termijn waarop dit plaatsvindt is vrij lang. Verwacht wordt dat bij een halfjaarlijkse afwisseling met de droge periode, waarin de stroombanen meer naar binnen gericht zijn, de verontreiniging binnen de contour blijft. 

Op basis van de KNMI gegevens blijkt de gekozen neerslagverdeling (+/25%) nog aan de lage kant te zijn. De netto neerslag voor de beide periodes is bepaald uit de neerslag en de verdamping. Na omrekening van de Makking verdamping naar de Pennman verdamping (factor 1,25) en rekening houdend met een gewasfactor voor de winter en de zomer, respectievelijk 0,6 en 0,8, volgt het neerslagverlies. Deze analyse levert allereerst op dat voor de winterperiode een netto neerslag van 1,4 mm/dag geldt. Vergeleken met de oorspronkelijke waarde van 0,7 mm/dag is dat een toename van 100%! In de zomer is er nauwelijks sprake van netto neerslag. 

Modelberekeningen voor het worst case scenario waarbij het 30 jaar lang achtereen winter is (neerslag 1,4 mm/dag) laten zien wat het effect is op stroombanen vanuit de verontreiniging. In bijlage N zijn de resultaten weergegeven. 

Het is vanzelfsprekend dat onder deze omstandigheden deeltjes vanuit de beheerscontour ontsnappen. De afstanden die worden afgelegd zijn echter gering. Zo ontsnapt er zelfs na 30 jaar nagenoeg geen verontreiniging in de tussenzandlaag. Stroombanen in het watervoeren pakket komen duidelijk verder maar ook daar zijn de afstanden in deze worst case benadering gering. De verplaatsingen gedurende 6 jaar aaneengesloten worst case perioden bedragen orde grote meters (zie figuur 30). 


Fig. 30. Detail van locatie inclusief beheerscontour op kritieke positie met stroombanen gedurende 6 jaar. 

Dit komt overeen met de marge die bij de bepaling van de beheerscontour is aangehouden. In werkelijkheid zullen de geringe, naar buiten gerichte verplaatsingen gedurende de winter worden gecompenseerd tijdens de zomer. Over de lange termijn zullen de verplaatsingen dan ook naar binnen zijn gericht. 

4.4 **Conclusies en aanbevelingen voor monitoring** 

Uitgaande van de analyse in de vorige paragraaf is de conclusie dat de seizoenale effecten een verwaarloosbare invloed hebben op het functioneren van het ontworpen systeem. De verontreiniging wordt beheerst en verplaatsingen zijn gering, zelfs in de worst case situatie. 

De volgende fase in het project richt zich met name op het ontwerp en het beheer van het monitoringsnetwerk voor de locatie. De bovengenoemde conclusie heeft ook gevolgen voor het ontwerp van het monitoringsnetwerk. Omdat het effect van de dynamica op het systeem valt te verwaarlozen hoeft er ook bij het ontwerp van de monitoring geen rekening mee te worden gehouden. Het ontwerp kan volledig op de stationaire situatie worden gebaseerd. Dit houdt onder ander in dat de meetfrequentie laag kan zijn, mogelijk eens per kwartaal, zodat een jaargemiddelde stijghoogtegradiënt nog redelijk goed te bepalen valt. 

_Aanbevelingen_ Uitgangspunt voor de beheersing van de verontreiniging is dat op de rand, ter plaatse van de beheerscontour, de stroming naar binnen gericht moet zijn. Om deze stromingsrichting vast te stellen is monitoring van de stijghoogte aan weerszijden van de rand nodig. Monitoringspunten komen op basis hiervan paarsbewijs langs de beheerscontour te liggen. Het wordt aanbevolen om nader onderzoek te verrichten naar de nauwkeurigheid van deze metingen. Bij de bepaling van stromingsrichtingen gaat het om het meten van kleine stijghoogteverschillen die nog geringer worden wanneer de afstanden tussen de meetpunten afneemt. Belangrijk aandachtspunt bij het ontwerp van het monitoringsnetwerk is het bestaan van kritische locaties of gebieden waar de kans op het weglekken van verontreiniging groot is. Op basis van de resultaten in bijlage M en N betreft dit met name de zuidoost zijde van de locatie. 

Informatie die bij de monitoring vrijkomt is ook interessant voor het aanbrengen van verbeteringen in het gebruikte grondwatermodel. Het gaat hierbij met name om de geohydrologische parameters van de ondergrond. De meest interessante monitoringsperiode hiervoor is de tijd tussen het aanzetten van de eerste pomp en het moment waarop het volledige 


systeem werkt en de grondwaterstand zich heeft ingesteld. Het aansluitend uitvoeren van een tijdsafhankelijk modellering over die periode, in feite een extra kalibratieronde, levert de extra gegevens over de ondergrond. Hiervoor is continue stijghoogtemetingen tijdens deze eerste monitoringsfase nodig in tegenstelling tot laagfrequente metingen in de tweede fase. Het aantal meetpunten en de locaties in de eerste fase kan afwijken van die van het netwerk voor de lange termijn monitoring. In de eerst fase zullen de monitoringspunten met name georiënteerd worden ten opzichte van de infiltratieen onttrekkingspunten. 

De belangrijkste meetgrootheid voor monitoring is de stijghoogte in de verschillende pakketten. Het uitvoeren van kostbare concentratiemetingen geeft in eerste instantie niet meer zicht op de beheersende werking van het systeem dan stijghoogtemetingen. Wel ontstaat er een beter beeld van de werkelijke verontreinigingssituatie. 



##### HOOFDSTUK 5 

#### CONCLUSIES EN AANBEVELINGEN 

5.1 **Conclusies** 

_Motivatie_ 

- De aanleiding voor dit specifieke SKB-project was de in het NOBIS-project Restrisk     getrokken conclusie dat het onttrekkingsdebiet **niet** bepalend is voor de sanerende werking     en daarmee de duur van een pump&treat sanering. 

- De duur van een pump&treat sanering wordt dan ook vaak sterk onderschat. 

- Het meest efficiënte pump&treat saneringssysteem bestaat dan ook uit een verzameling van     geringe onttrekkingen (1-10 m^3 /dag) verspreid over de verontreiniging, ook wel smart     pump&treat genoemd. 

- Door schoon grondwater om te leiden over een verontreinigde locatie (stroomopwaarts     onttrekken en stroomafwaarts injecteren) wordt de verontreiniging beheerst. Dit maakt een     veilige toepassing van smart pump&treat ook in goeddoorlatende watervoerende pakketten     mogelijk, wanneer afbraak te gering is om verspreiding te beperken met geringe     onttrekkingen. 

- Omleiden is veelal bij toepassing van smart pump&treat in watervoerende lagen     noodzakelijk. 

- De verwachting bestaat, dat optimalisatie van pump&treat naar smart pump&treat een sterke     reductie van het te behandelen volume grondwater tot gevolg heeft, waardoor     zuiveringskosten een factor 3 tot 5 goedkoper worden. 

_Algemene ontwerp richtlijnen voor omleiden of 'manipuleren' van grondwater_ 

- Door toepassing van een grondwater-manipulatiesysteem is het mogelijk de     stijghoogtegradiënt tot 10% van de oorspronkelijke gradiënt te reduceren. De drijvende     kracht achter de verspreiding wordt hiermee bijna volledig weggenomen. 

- Het manipulatiesysteem bestaat bij voorkeur uit twee à drie onttrekkingsputten     stroomopwaarts en twee à drie injectieputten stroomafwaarts van de verontreinigde locatie.     Meerdere 'sets' van putten zijn nodig, wanneer ingespeeld moet worden op een sterk     heterogene bodemopbouw (zoals bij de voormalige locatie van Akzo Nobel). 

- Het saneringssysteem bestaat bij voorkeur uit 4 tot 6 onttrekkingsputten. Vanuit het oogpunt     'sanerende werking' zouden deze putten evenredig verspreid dienen te worden over de     verontreiniging. Vanuit het oogpunt 'beheersing door een minimaal onttrekkingsdebiet'     zouden deze putten in het benedenstroomse deel van de verontreiniging geplaatst dienen te     worden. Vaak is beheersing met minimaal debiet het maatgevende criterium. 

- Op basis van de lengte en vorm (lengte/breedte) van de verontreiniging, de     stijghoogtegradiënt ofwel verhang op de locatie en de transmissiviteit is een ruwe schatting     te maken van het volume om te leiden schoon grondwater om smart pump&treat mogelijk te     maken. 

- Voor de voormalige locatie van Akzo Nobel dient 570-670 m^3 /dag schoon grondwater te     worden omgeleid en 115 m^3 /dag verontreinigd grondwater te worden onttrokken. Dit is een     30% van het oorspronkelijk saneringsdebiet. 

_Ontwerp methode 'optimalisatie met MODMAN/Lindo'_ 

- Geautomatiseerd optimaliseren van het manipulatie- en saneringssysteem met MODMAN/     Lindo maakt een objectieve en snelle keuze van de plaats van onttrekkings- en injectieputten     en het debiet mogelijk. 


_Robuustheid bij toepassing in de praktijk_ 

- Seizoenale effecten hebben een verwaarloosbare invloed op het functioneren van het     ontworpen systeem. De verontreiniging wordt beheerst en verplaatsingen zijn gering, zelfs in     een langdurige worst case situatie. 

- Continue monitoring van de stijghoogte tijdens de opstartfase van het systeem, het     inschakelen van de putten, levert informatie waarmee het grondwatermodel sterk kan worden     verbeterd. 

- Laag frequente monitoring van stijghoogten tijdens de saneringsfase op strategische locaties     maakt aansturing van het smart pump&treat systeem mogelijk. 

5.2 **Aanbevelingen** 

Aanbevolen wordt om aandacht te besteden aan verstoppingproblematiek bij injectieputten van het manipulatiesysteem. Mogelijkheid tot injectie is namelijk een voorwaarde voor het toepassen van manipulatie. Daarnaast blijkt het ontwerpdebiet per put gevoelig voor onzekerheid als gevolg van bodemheterogeniteit. Dit is te ondervangen door het systeem bij installatie in te regelen op stijghoogtemetingen. Aanbevolen wordt hiervoor richtlijnen op te stellen. Ten slotte wordt aanbevolen te onderzoeken of vrachtverwijdering door het saneringssysteem in de optimalisatieprocedure kan worden opgenomen. 


#### LITERATUUR 

Bakker, L.M.M., (1996); Aanvullend nader onderzoek voormalig bedrijfsterrein Akzo Nobel te Weert, Tauw rapport nr. R3447073.T02/LMB, Deventer. 

Bakker, L.M.M., Beek, C.G.E.M. van, Vasak, L., Nieuwaal, A., Stefess, G.C., December 1999; Implementatie beslissystematiek ontwerp en onderhoud van infiltratieen onttrekkingsmiddelen, CUR/NOBIS 98-1-08, Gouda. 

Bakker, L.M.M., Boode, J., (1997); Saneringsplan voormalig bedrijfsterrein Akzo Nobel te Weert, Tauw rapport nr. R3447030.T02, Deventer. 

Berendrecht, W.L., (1999); Generieke aspekten van gemanipuleerde smart pump-and-treat sanering, TNO rapport nr. NITG 99-241-B, Delft. 

Deutsch, C.V., Journel, A.G., (1998); GSLIB: geostatistical software library and user's guide, 2nd edition, Oxford University Press, Oxford. 

Freeze R.A., Cherry J.A., (1989); What Has Gone Wrong? _Ground Water vol. 27(4)_ , 458-464. 

GeoTrans, Inc. (1992); MODMAN: An optimization module for MODFLOW, version 2.1, Documentation and user's guide. 

Griffioen, J., Hetterschijt, R.A.A., (1998); On diffusive Mass-Transfer Limitations in Relation to Remediation of Polluted Groundwater Systems, _6 th_^ _International FZK/TNO Conference on Contaminated Soil_ , Edinborough, UK. 

Haley J.L., Hanson B., Enfiedl C., Glass J., (1991); Evaluating the effectiveness of Groundwater Extraction Systems, _Groundwater Monitoring Rev. vol. 11(1)_ , 119-124. 

Harvey F.C., Haggerty R., Gorelick, M.S., (1994); Aquifer remediation: A method for estimating mass transfer rate co-efficients and an evaluation of pulsed pumping, _Wat. Resour. Res. vol. 30(7),_ 1979-1991. 

Hetterschijt, R.A.A., Te Stroet, C.B.M., (1998); RestRisk –verspreiding en risico's van restconcentraties in bodem en grondwater, Fase 2, deelrapport I: Slimmer saneren met pump&treat; Onzekerheden en pompstrategieën, CUR/NOBIS 95-2-11, Gouda. 

Hetterschijt, R.A.A. en Te Stroet, C.B.M., (1998); RestRisk –verspreiding en risico's van restconcentraties in bodem en grondwater, Fase 2, deelrapport III: Natuurlijke afbraak en verspreiding, TNO rapport nr. NITG 98-115-A, Delft. 

Keeley, J.F., (1989); Performance Evaluation of Pump & Treat Remediations, _Superfund Issue Paper,_ EPA/540/8-89/005, R.S. Kerr Environmental Research Lab., Ada OK, 14 pp. 

Mackey, D.M., Cherry, J.A., (1989); Groundwater Contamination: Pump-and-Treat Remediation, _Environ. Sci. Technol. 23(6),_ 630-636. 

McDonald, M.G., Harbaugh, A.W., (1988); A Modular Three-dimensional Finite Difference Groundwater Flow Model, U.S. Geological Survey, U.S.A. 


Provincie Limburg (1997); Ecohydrologische Atlas Limburg. 

Schrage, L. (1991); LINDO: an optimization modeling system, 4th edition, The Scientific Press, San Francisco. 

Stroet, C.B.M. Te, Hetterschijt, R.A.A., (1998); Haalbaarheidsonderzoek naar extensieve grondwatersanering van het Akzo bedrijventerrein te Weert, TNO rapport nr. NITG-98-140-A, Delft. 

Strack, O.D.L., (1989); Multi-layer aquifer modelling using the analytical element method, _Proc. 4 th_^ _Int. Conf. On the use of models to find working solutions to groundwater problems_ , National Well Association, Dublin, Ohio, USA. 

Sutherland, S.S., (1997); Remediation Engineering: design concepts, ISBN 1-56670-137-6, CRC press Inc, U.S.A. 

Schwartzenbach, R.P., Westall, J.C., (1985); Sorption of hydroophobic trace organic compounds on groundwatersystems. _Water Sci.Soc.Am_. J. 51, 876-884. 

Zheng, C., (1992); MT3D: a modular three-dimensional transport model Version 1.5, Documentation and user's guide. 


##### BIJLAGE A 

#### GEMETEN STOFCONCENTRATIES OP AKZO NOBEL TERREIN 


##### BIJLAGE B 

#### BEHEERSCONTOUR 


##### BIJLAGE C 

#### VIJF REALISATIES KLEIDIKTE 


##### BIJLAGE D 

#### GRONDWATERAANVULLING OP HET AKZO NOBEL TERREIN 


##### BIJLAGE E 

#### STIJGHOOGTES ALS GEVOLG VAN MANIPULATIE EN SANERINGSSYSTEEM 


##### BIJLAGE F 

#### BEHEERSENDE WERKING SMART PUMP&TREAT SYSTEEM 


##### BIJLAGE G 

#### MODELINVOER VERONTREINIGINGSSITUATIE 


##### BIJLAGE H 

#### DOORBRAAKCURVEN TETRA, PER, CHLOROFORM EN CFK 


##### BIJLAGE I 

#### CONTOURKAARTEN VERDROGINGSSITUATIE 


##### BIJLAGE J 

#### OVERZICHT PERIODIEK GEMETEN STIJGHOOGTEN 


tussenzandlaag 

watervoerend pakket 

 datum 

 21/04/99 

 27/04/99 

 28/07/99 

 28/10/99 

 28/01/00 

 21/04/99 

 27/04/99 

 28/07/99 

 15/10/99 

 28/10/99 

 28/01/00 

 putnr.^72 

 33.90 

-^ 

 33.64 

 33.62 

 33.84 

-^ 

-^ 

-^ 

-^ 

-^ 

- 

 73 

-^ 

 33.73 

 33.52 

 33.54 

 33.74 

-^ 

-^ 

-^ 

-^ 

-^ 

- 

 101 

-^ 

 33.75 

 33.55 

 33.60 

 33.82 

-^ 

-^ 

-^ 

-^ 

-^ 

- 

 102 

-^ 

-^ 

 33.53 

 33.58 

 33.75 

-^ 

-^ 

-^ 

-^ 

-^ 

- 

 112 

 33.91 

 33.85 

 33.62 

 33.66 

 33.86 

-^ 

-^ 

-^ 

-^ 

-^ 

- 

 113 

 33.96 

-^ 

 33.66 

 33.69 

 33.90 

-^ 

-^ 

-^ 

-^ 

-^ 

- 

 208 

 34.30 

-^ 

-^ 

-^ 

-^ 

 33.45 

-^ 

-^ 

-^ 

-^ 

- 

 210 

 34.43 

-^ 

-^ 

 34.11 

-^ 

 33.46 

-^ 

 33.09 

-^ 

 32.82 

- 

 211 

 33.95 

-^ 

 33.67 

 33.70 

-^ 

 33.45 

-^ 

 32.86 

-^ 

 32.83 

- 

 212 

 33.53 

-^ 

-^ 

-^ 

-^ 

-^ 

-^ 

-^ 

-^ 

-^ 

- 

 302 

-^ 

-^ 

 33.65 

 33.68 

 33.88 

-^ 

-^ 

-^ 

-^ 

-^ 

- 

 1011 

 33.80 

-^ 

 33.49 

 33.50 

 33.74 

-^ 

-^ 

 33.01 

-^ 

-^ 

- 

 1021 

 33.76 

-^ 

 33.43 

 33.46 

 33.70 

 33.41 

-^ 

 32.77 

-^ 

 32.74 

 33.24 

 1031 

 33.91 

 33.85 

 33.62 

 33.65 

 33.86 

-^ 

-^ 

-^ 

-^ 

-^ 

- 

 1051 

-^ 

 33.60 

 33.31 

 33.32 

 33.59 

-^ 

 33.31 

 32.75 

-^ 

 32.71 

 33.22 

 1101 

 33.57 

 33.50 

 33.13 

 33.12 

 33.46 

 33.37 

 33.30 

 32.72 

 32.73 

 32.68 

 33.18 

 1201 

 33.50 

-^ 

 33.00 

 32.97 

 33.36 

 33.36 

-^ 

 32.71 

-^ 

 32.66 

 33.17 

 II^ 

 33.72 

 33.65 

 33.42 

 33.46 

 33.67 

 33.41 

 33.33 

 32.76 

-^ 

 32.73 

 33.24 

 A^ 

-^ 

-^ 

-^ 

-^ 

-^ 

 33.40 

-^ 

-^ 

 32.82 

 32.76 

 33.28 

 B^ 

-^ 

-^ 

-^ 

-^ 

-^ 

 33.43 

-^ 

 32.79 

 32.80 

 32.76 

 33.27 

 C 

-^ 

-^ 

-^ 

-^ 

-^ 

 33.38 

-^ 

 32.74 

 32.75 

 32.70 

 33.21 

 D 

-^ 

-^ 

-^ 

-^ 

-^ 

 33.37 

 33.31 

 32.73 

 32.75 

 32.69 

 33.21 

 E^ 

-^ 

-^ 

-^ 

-^ 

-^ 

 33.43 

 33.36 

 32.79 

 32.83 

 32.76 

 33.28 

 Bij deze bijlage is ook een serie figuren gevoegd (formaat A3) waarin met een kleurverdeling de gemeten stijghoogten op de plattegrond van de locatie zijn ingevuld. 


##### BIJLAGE K 

#### VERGELIJKING VAN HET TNO MODEL MET HET TAUW MODEL 

#### OP BASIS VAN STIJGHOOGTEN 

Stijghoogtecontouren berekend met het Tauw model (continu) en met het TNO model (onderbroken) 


##### BIJLAGE L 

#### NEERSLAGEN VERDAMPINGSGEGEVENS, KNMI 

 Neerslag en verdamping per week van maart '99 tot januari '00 (locatie Ell, stationsnummer 377) 

 -30 

 -20 

 -10 

 0 

 10 

 20 

 30 

 40 

 50 

 07/03/9921/03/9904/04/9918/04/9902/05/9916/05/9930/05/9913/06/9927/06/9911/07/9925/07/9908/08/9922/08/9905/09/9919/09/9903/10/9917/10/9931/10/9914/11/9928/11/9912/12/9926/12/9909/01/0023/01/00 

 datum 

**neerslag in mm (per week)**^ neerslag verdamping 


##### BIJLAGE M 

#### STROOMBANEN T.G.V. DYNAMICA IN NEERSLAG 


##### BIJLAGE N 

#### STROOMBANEN IN WORST CASE NEERSLAGSITUATIE 


