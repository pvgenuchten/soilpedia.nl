# Voorspel je Verontreiniging! 

### Eindrapportage SKB-project PT4128 

### Definitief, 19 december 2005 



 Eindrapportage SKB-project PT04-128 3\60 

## Verantwoording 

**Titel** Voorspel je Verontreiniging! **Opdrachtgever** SKB **Projectleider** ir. M. (Marcus) van Zutphen **Auteur(s)** ir. M. (Marcus) van Zutphen, dr.ir.E.L. Wipfler, dr. ir. J.R. Valstar, drs. R.A.A. Hetterschijt en ir. L.M.M. Bakker 

**Projectnummer** 4334986 **Aantal pagina's** 60 (exclusief bijlagen) **Datum** 19 december 2005 **Handtekening** 

## Colofon 

Tauw bv Vestiging Rotterdam Rhijnspoor 209 Postbus 6 2900 AA Capelle aan den IJssel Telefoon (010) 288 61 00 Fax (010) 288 61 66 

Dit document is eigendom van de opdrachtgever en mag door hem worden gebruikt voor het doel waarvoor het is vervaardigd met inachtneming van de rechten die voortvloeien uit de wetgeving op het gebied van het intellectuele eigendom. De auteursrechten van dit document blijven berusten bij Tauw. Kwaliteit en verbetering van product en proces hebben bij Tauw hoge prioriteit. Tauw hanteert daartoe een managementsysteem dat is gecertificeerd dan wel geaccrediteerd volgens: 

- NEN-EN-ISO 9001. 



 Eindrapportage SKB-project PT04-128 5\60 

## Inhoud 

**Verantwoording en colofon** .......................................................................................................... **3** 

**Samenvatting ................................................................................................................................. 9** 

**1 Inleiding** ........................................................................................................................ **11** 

**2 Generieke beschrijving modellen** .............................................................................. **13** 

**3 Processen bij bodemverontreiniging** ........................................................................ **15** 

**4 De Wet bodembescherming als kader** ...................................................................... **17** 4.1 Faseringen in de Wbb ................................................................................................... **18** 4.2 Afperking van de verontreiniging ................................................................................... **18** 4.3 Bepaling van ernst en urgentie...................................................................................... **19** 4.4 Uitvoeren van een saneringsonderzoek ........................................................................ **19** 4.5 Het opstellen van het saneringsplan ............................................................................. **22** 4.6 Het uitvoeren van de sanering ...................................................................................... **23** 4.7 Het uitvoeren van de nazorg ......................................................................................... **23** 

**5 Beschrijving van de probleemstelling, doelstelling en gekozen oplossing** .......... **25** 5.1 Probleemstelling ............................................................................................................ **25** 5.2 Doelstelling .................................................................................................................... **25** 5.3 Gekozen oplossing(srichting) ........................................................................................ **26** 5.4 Deelnemers ................................................................................................................... **26** 

**6 Probleem-identificatie-proces** .................................................................................... **29** 6.1 Potentieel betrokkenen en hun wensen en eisen.......................................................... **29** 6.2 Waarom voor een numeriek model ............................................................................... **31** 6.2.1 Het overdragen van het conceptuele grondwaterstromingsmodel ................................ **31** 6.2.2 Het valideren van stoftransport ..................................................................................... **32** 6.3 Fysieke omstandigheden .............................................................................................. **33** 

**7 Conceptueel model** ..................................................................................................... **35** 

**8 Beschikbare data** ......................................................................................................... **37** 8.1 Welke data .................................................................................................................... **37** 


**6\60** Eindrapportage SKB-project PT04-128 

 8.2 Bruikbaarheid en betrouwbaarheid van data................................................................. 38 

 9 Numerieke modellering ............................................................................................... 41 9.1 Resultaten van het proces............................................................................................. 42 

 10 Proces voor de bepaling van aanvullende waarnemingen ...................................... 43 10.1 Geologie ........................................................................................................................ 43 10.2 Geohydrologie ............................................................................................................... 44 10.3 Stoftransport en afbraak ................................................................................................ 45 

 11 Modelleringsen interpretatieprocessen van de nieuwe gegevens ....................... 47 

 12 Bruikbaarheid van voorspellende waarde ................................................................ 49 

 13 Werkhandleiding Modelleer activiteiten .................................................................... 51 13.1 Het proces per Wbb-fase .............................................................................................. 51 13.2 Afperking van de verontreiniging ................................................................................... 53 13.2.1 Doel van de inzet van het model ................................................................................... 53 13.2.2 Benodigde informatie en mogelijke veldwerkzaamheden ............................................. 53 13.2.3 Mogelijke resultaten ...................................................................................................... 53 13.3 Bepaling van ernst en urgentie...................................................................................... 54 13.3.1 Doel van de inzet van het model ................................................................................... 54 13.3.2 Benodigde informatie en mogelijke veldwerkzaamheden ............................................. 54 13.3.3 Mogelijke resultaten ...................................................................................................... 54 13.4 Uitvoeren van een saneringsonderzoek ........................................................................ 54 13.4.1 Doel van de inzet van het numerieke model ................................................................. 54 13.4.2 Benodigde informatie en mogelijke veldwerkzaamheden ............................................. 55 13.4.3 Mogelijke resultaten ...................................................................................................... 55 13.5 Het opstellen van het saneringsplan ............................................................................. 56 13.5.1 Doel van de inzet van het numerieke model ................................................................. 56 13.5.2 Benodigde informatie en mogelijke veldwerkzaamheden ............................................. 56 13.5.3 Mogelijke resultaten ...................................................................................................... 56 13.6 Het uitvoeren van de sanering ...................................................................................... 56 13.6.1 Doel van de inzet van het numerieke model ................................................................. 56 13.6.2 Benodigde informatie en mogelijke veldwerkzaamheden ............................................. 57 13.6.3 Mogelijke resultaten ...................................................................................................... 57 13.7 Het uitvoeren van de nazorg ......................................................................................... 57 13.7.1 Doel van de inzet van het numerieke model ................................................................. 57 


 Eindrapportage SKB-project PT04-128 7\60 

13.7.2 Benodigde informatie en mogelijke veldwerkzaamheden ............................................. **57** 13.7.3 Mogelijke resultaten ...................................................................................................... **57** 

**14 Conclusies en Aanbevelingen** .................................................................................... **59** 



 Eindrapportage SKB-project PT04-128 9\60 

## Samenvatting 

In het SKB-project Voorspel je Verontreiniging is onderzocht of het mogelijk is om numerieke modellen op een zinvolle manier in te zetten voor het verklaren, begrijpen en voorspellen van gevallen van bodemverontreiniging. Aan de hand van 2 cases binnen en Shell terrein zijn door een denktank in drie brainstormsessies en tussenliggende velden modelleringwerkzaamheden verschillende aspecten en mogelijkheden voor de inzet van numerieke modellen en metingen geëvalueerd. De denktank bestond uit een brede selectie aan partijen die betrokken zijn bodemverontreinigingen. De verschillende personen waren afkomstig uit de volgende geledingen: 

- Probleembezitters 

- Terreineigenaren 

- Bevoegd gezagen 

- Aannemerij 

- Advies wereld 

- SKB, en 

- VROM 

Het bespreken binnen een breed gezelschap van de wensen en mogelijkheden voor de inzet van het model en de daaruit te verwachten resultaten blijkt zeer wenselijk voor een efficiënte uitvoering en een goede acceptatie door alle partijen. 

Uit het onderzoek blijkt dat het gebruik van numerieke modellen binnen de verschillende fases van het Wbb-traject nuttig kan zijn. De mate waarin het model ingezet kan worden verschilt per fase en is eveneens sterk afhankelijk van de wensen en de hoeveelheid en kwaliteit van de beschikbare veldgegevens. Voor toepassen van een model in elk van deze fases dient het een vergelijkbaar traject doorlopen te worden waarin er in een cyclisch proces een verfijning van het model wordt bereikt. 

In het project werd duidelijk dat voor effectief het inzetten van het numeriek model verschillende aspecten van de verontreinigingssituatie in verschillende stappen onderzocht en vastgesteld moeten worden. In volgorde van belangrijkheid zijn het: 

- De geologie 

- De geohydrologie 

- Het stoftransport en afbraakprocessen 

Daarnaast spelen natuurlijk de randvoorwaarden als de kwetsbaarheid van verschillende receptoren, de vereisten van de verschillende bevoegde gezagen en afspraken tussen verschillende partijen. 


**10\60** Eindrapportage SKB-project PT04-128 

 Uit de brainstormsessies is gebleken dat met de inzet van numerieke modellen en veldwerk het voor wat complexere verontreinigingssituaties moeilijk is om de relatie tussen de bron en de daaruit voortkomende pluim te voorspellen. Ook het voorspellen van het toekomstig verspreidingsgedrag van de huidige grondwaterverontreiniging is moeilijk, maar wel mogelijk gebleken. 

 Numerieke modellen zijn een nuttig gereedschap gebleken voor het kwantitatief doorrekenen van het verspreidingsgedrag van grondwaterverontreinigingen. De inzet is echter wel afhankelijk van de kennis en kunde van de persoon die het uitvoert en de kwaliteit en kwantiteit van de beschikbare gegevens in relatie tot de locatiespecifiek omstandigheden. 


 Eindrapportage SKB-project PT04-128 11\60 

## 1 Inleiding 

Voor u ligt de eindrapportage van het project Voorspel je verontreiniging! In Voorspel je Verontreiniging! is onderzocht of het mogelijk is om numerieke modellen op een zinvolle manier in te zetten om de relatie tussen de bron en pluim en daarmee het verspreidingsgedrag van de verontreiniging te voorspellen. 

Bodemverontreiniging is een probleem dat landsbreed zijn gelding doet. Bodembeleid is al jaren in ontwikkeling en nog steeds aan verandering onderhevig. De Wet bodembescherming (Wbb) vormt hiervoor het voornaamste wettelijke kader. In de Wbb is de verspreiding van de verontreiniging door de bodem geformuleerd als een van de belangrijkste redenen om een geval van bodemverontreiniging te onderzoeken en onacceptabele verspreidingsrisico’s ongedaan te maken. 

Binnen de uitvoering van het Nederlandse bodembeleid wordt uitgegaan van een relatie tussen de bron/kern van de verontreiniging en de pluim van verontreinigd grondwater. In vele projecten is onderzoek gedaan naar de relatie tussen de bron en de resulterende grondwaterverontreinigingen en naar de processen die het gedrag van de pluim bepalen. Hierbij kan ondermeer gedacht worden aan de Nobis Projecten gericht op Natuurlijke Afbraak van verschillende verontreinigende componenten. Uit praktijk ervaringen blijkt de relatie tussen de grondverontreiniging (de bron) en de grondwaterverontreiniging echter niet zo eenvoudig te bepalen als veelal voorgesteld. 

Aan de hand van 2 cases en drie brainstormsessies met stakeholders en experts is getracht een door allen gedragen visie op te stellen voor de zinvolle inzet van numerieke modellen voor het voorspellen van het gedrag van verontreinigingen. Als cases zijn twee deellocaties op het terrein van Shell gebruikt. Voor deze gevallen zijn de relaties tussen de bron en de pluim en de verspreidingsrisico's van de huidige verontreinigingssituatie niet eenvoudig vast te stellen. Voor deze twee deellocaties is een grote hoeveelheid gegevens over de bodem, de geohydrologie, de geochemie en de stofeigenschappen beschikbaar. Waar nodig heeft Shell op advies van het expert team additionele metingen laten uitvoeren. 

Door gebruik te maken van een denktank met experts en stakeholders (probleemeigenaar en bevoegd gezag), is onderzocht of met de numerieke modellen en een grote collectie aan onderzoeksgegevens een relatie tussen de bron en pluim kon worden gelegd. Indien de relatie met de beschikbare informatie niet goed kon worden vastgesteld, is inzichtelijk gemaakt waar leemten en onzekerheden zijn. 


**12\60** Eindrapportage SKB-project PT04-128 

 De eerste brainstormsessie is gehouden op 26 januari 2005. In de eerste brainstormsessie is de algemene doelstelling van het project en de verschillende rollen van de participanten aangegeven. Dit werd gevolgd door een toelichting op de eerste modelleringsactiviteiten voor de twee verontreinigde locaties (zie M001-4334986NEI-tsz-V01-NL, in te zien bij SKB). Naar aanleiding van de resultaten van deze sessie zijn verschillende werkzaamheden verricht. Deze zijn besproken in een tweede brainstormsessie welke is gehouden op 29 maart 2005. (zie M002-4334986MZU-kbo-V01-NL, in te zien bij SKB). In de derde brainstormsessie die heeft plaatsgevonden op 20 september 2005 zijn de laatste resultaten van het modelleerwerk en metingen gepresenteerd en besproken (zie M003-4334986MZU-kbo-V01-NL, in te zien bij SKB). Verder is er gesproken over de waarde van modelleren voor opdrachtgever, bevoegd gezag en anderen. In januari 2006 zullen de resultaten van het project op een generieke manier aan het publiek worden getoond tijdens een on-site dag. 

 Een overzicht van de twee cases, de werkwijze en het denkproces tijdens het SKB-project “Voorspel je Verontreiniging!” zijn weergegeven in het rapport "Voorspel je verontreiniging! Beschrijving cases". 

 Omdat de Wbb het wettelijke kader vormt voor het onderzoek naar het voorkomen en verspreidingsgedrag van verontreinigingen worden in hoofdstuk 2 de plaats en toepasbaarheid van modellen voor het voorspellen van verspreidingsrisico's binnen de verschillende fases binnen de Wbb beschreven. Voor elk van deze fases wordt in hoofdstuk 13 aangegeven wat een nuttige inzet van modellen voor het bepalen van de verspreidingsrisico's. 

 Het proces om tot een gedragen numeriek model te komen is in principe voor elk van de Wbbfases gelijk. Aan de hand van de doorlopen trajecten voor de twee verontreinigde locaties wordt een dergelijk proces beschreven. Elk van de processtappen worden in hoofdstuk 5 en de daaropvolgende hoofdstukken per stap uitgewerkt. Vervolgens leidt dit tot een werkhandleiding voor het voorspellen van verontreiniging met ondersteuning van modellen. 

 In deze rapportage worden verschillende termen ten aanzien van modellen gebruikt om eenduidigheid hierover te verschaffen, wordt in hoofdstuk 2 een toelichting gegeven op de verschillende modellen. Daarna volgt in hoofdstuk 3 een beschrijving van allerlei processen die een rol spelen bij de verspreiding van verontreinigingen door de ondergrond, en derhalve in modellen meegenomen kunnen worden. 


 Eindrapportage SKB-project PT04-128 13\60 

## 2 Generieke beschrijving modellen 

Modellen zijn een vereenvoudigde, schematische weergave van de werkelijkheid. Ze worden vaak gebruikt om een huidige waargenomen situatie te kunnen verklaren of om toekomstvoorspellingen te doen bij voorzetting van de autonome situatie of bij potentiële maatregelen. Er bestaan veel verschillende typen van modellen en in de praktijk blijken veel mensen onder het woord ‘model’ vaak maar een van deze modeltypes te bedoelen. Hieronder volgt een overzicht van de verschillende modeltypen die worden gebruikt bij het in beeld brengen, verklaren en voorspellen van het gedrag en voorkomen van gronden grondwaterverontreinigingen. 

Conceptueel model Een conceptueel model is een beschrijving van de relevante processen en fysieke parameters op een niet-kwantitatieve manier. Het belangrijkste, maar tevens het meest ongrijpbare conceptuele model is het gedachte model "het concept". Een ieder heeft een beeld van de situatie. Om dit concept aan anderen over te brengen kan het worden weergegeven in spraak, op "een sigaren kistje", in schema's etc. 

Op basis van een conceptueel model wordt vaak al een beeld gevormd hoe de situatie in elkaar steekt en worden beslissingen genomen om al dan niet extra metingen uit te voeren en zo ja welke. Indien er werkelijke kwantitatieve voorspellingen gedaan moeten worden zal het conceptuele model worden omgezet in een analytisch of numeriek model. 

Analytisch model In een analytisch model wordt de vergelijking of worden de vergelijkingen die een proces beschrijven opgelost, zodat op elke punt in de tijd en ruimte (0D tot en met 3D) een kwantitatieve waarde van de te bepalen toestandsvariabele bekend is. Analytische oplossingen kunnen vaak alleen gevonden worden onder bepaalde voorwaarden. De bodem moet veelal homogeen zijn, de processen niet te complex, etc. In dat geval is de oplossing vaak relatief snel en goedkoop te bepalen. 

Numeriek model Bij een numeriek model worden de processen in ruimte (0D tot en met 3D) en tijd gediscretiseerd: opgedeeld in ruimtelijke cellen en tijdstappen. De processen worden in elke cel per tijdstap doorgerekend. Hierdoor geeft het numeriek model slechts uitkomsten in een vooraf bepaald aantal modelcellen en voor een vooraf bepaald aantal tijdstappen. Deze modellen worden vrijwel altijd met een computer doorgerekend. Met behulp van numerieke modellen kunnen complexe processen in heterogene bodem meestal goed worden doorgerekend en benaderd. 


**14\60** Eindrapportage SKB-project PT04-128 

 De beperkende voorwaarde bij gronden grondwaterverontreinigingen is meestal niet de numerieke modelcode, maar de geringe kennis van de ondergrond (invoer parameters), de procesparameters en de keuze voor het achterliggende conceptuele model. Dit numerieke model wordt veelal als 'het model' gezien. 

 Screening tools Met behulp van screening tools kan snel worden onderzocht of sommige processen of saneringsmaatregelen kansrijk zijn. Hierbij wordt met behulp van een beperkte set veldgegevens een eenvoudig beslissingsmodel doorlopen. Als voorbeeld noemen we hier het zogenaamde ‘stoplichtenmodel’ om de potentie voor natuurlijke afbraak snel te bepalen. Deze screening tools geven echter vaak alleen een eerste indicatie en de uitkomsten dienen altijd te worden onderbouwd met aanvullende metingen en modelstudies, voordat er verdere beslissingen kunnen worden genomen. 

 In dit rapport wordt onder het woord model alle hierboven genoemde mogelijke modeltypen verstaan. Indien we een specifieke modeltype bedoelen zal deze expliciet worden genoemd. 


 Eindrapportage SKB-project PT04-128 15\60 

## 3 Processen bij bodemverontreiniging 

Bij grondwaterverontreiniging kunnen de verschillende processen van belang. Voor een uitgebreid overzicht verwijzen we naar vakboeken of naar rapportages van Nobis en SKB. 

Grondwaterstroming Grondwater stroomt door de ondergrond onder invloed van drukverschillen. Meestal is grondwater de enige vloeistof in de bodem. 

Stroming van andere vloeistoffen en gassen in de bodem Dit kan optreden bij de ontstaansgeschiedenis van een verontreiniging waarbij deze als puur product de bodem instroomt. Hierbij maken we onderscheid tussen Light Non-Aqeuous Phase Liquids (LNAPLs) en Dense Non-Aqeuous Phase Liquids (DNAPLs). LNAPLs hebben een lagere dichtheid dan water en blijven als een drijflaag op het grondwater drijven of zich onder invloed van grondwaterstandfluctuaties rond de grondwaterspiegel ophouden in poriën. DNAPLs hebben en hogere dichtheid dan water en zakken in de bodem weg totdat ze een ondoordringbare, slecht doorlatende laag tegen komen, waarop ze als zinklaag blijven liggen. Tijdens het neerwaartse transport vanaf het maaiveld zal er ook NAPL achterblijven in het centrale deel van de poriën; de zogenoemde residuaire verzadiging. Voor een verdere beschrijving van dit proces verwijzen we naar het Nobis-project DNAPLKAR. Bij een sanering worden er soms gassen het grondwater in gepompt (bijvoorbeeld bij persluchtinjectie of stoom gestimuleerde extractie) of kunnen gassen in-situ worden gevormd door natuurlijke processen die optreden (methaan vorming) of antropogene processen tijdens saneringen (bijvoorbeeld bij in-situ chemische oxidatie, stroom gestimuleerde extractie). Deze zullen veelal door het grondwater omhoog stromen. 

Oplossen/ neerslaan Vanuit een bronzone (drijflaag, zinklaag of residuaire verzadiging) lossen stoffen op in het grondwater. Dit proces is voor olie in detail beschreven in het SKB-project Modelcode olie. In de praktijk blijkt het uitermate lastig om detailgegevens over deze processen (hoeveel puur product is er aanwezig, wat is het contactoppervlak met het grondwater, etc.) te verkrijgen. Daarom valt dit proces (in dit rapport verder de bron-pluim-relatie genoemd ) veelal niet volledig te karakteriseren. Vaak wordt daarom de uitkomst van dit proces, de opgeloste concentratie net stroomafwaarts van de bron, als beginvoorwaarde van de pluimmodellering genomen. De voorspelling hoe lang het duurt tot dat de bron opdroogt is dan niet te maken. Het is ook mogelijk dat opgeloste stoffen neerslaan, omdat de concentratie hoger wordt dan de verzadigingsgraad. Een voorbeeld hierbij is het neerslaan van ijzer(III)-hydroxide, indien zuurstof wordt toegevoegd aan grondwater met een hoge ijzer(II)-concentratie. 


**16\60** Eindrapportage SKB-project PT04-128 

 Advectie Advectie is het proces waarbij de in het grondwater opgeloste verontreiniging meestroomt met het grondwater. Dit is veelal het primaire transportproces voor de opgeloste verontreinigingen. 

 Diffusie Diffusie wordt veroorzaakt door de willekeurige beweging van moleculen. Hierdoor is er een netto verspreiding van de verontreiniging van locaties met een hoge concentratie naar locaties met een lagere concentratie. Om zich dit proces goed voor te kunnen stellen, kan men denken aan het mengen van thee in een glas heet water. 

 Dispersie Dispersie treedt op bij advectie. Doordat het grondwater (en de daarin opgeloste moleculen van de verontreiniging) op de ene locatie sneller stroomt dan op een andere locatie, bv doordat de ene molecuul helemaal om een zandkorrel heen moet stromen en de andere rechtdoor gaat, wordt een verontreinigingspluim ook wijder en de maximumconcentratie lager. 

 Adsorptie/retardatie Adsorptie is het proces, waarbij een deel van de verontreiniging zich hecht aan de bodemdeeltjes. Dit deel van de verontreiniging verplaatst zich niet, zodat de gemiddelde snelheid van de verontreiniging lager wordt dan de stroomsnelheid van het grondwater. Bij aanname dat er continu evenwicht is tussen de geadsorbeerde concentratie en de opgeloste concentratie, kan adsorptie worden gemodelleerd door middel van retardatie, waarbij de retardatiefactor de verhouding is tussen de stroomsnelheden van het grondwater en van de verontreiniging. 

 Afbraak/chemische reacties Door natuurlijke of gestimuleerde afbraak of chemische reacties kunnen verontreinigingen omgezet worden in stoffen die ongevaarlijk, minder toxisch of zelfs nog toxischer zijn. Vaak kunnen deze afbraakproducten zelf ook nog verder afgebroken worden. Afbraak kan op verschillende manieren worden gemodelleerd, van eerste orde afbraak (mate van afbraak is lineair afhankelijk van de concentratie van de verontreiniging) tot complexe vergelijkingen waarbij de afbraak afhankelijk is van de verontreingingsconcentraties, de concentraties van redoxparameters, de bacteriepopulatie en concentraties van eventuele andere verontreinigingen. Bij deze berekeningen is het heikele punt altijd de afbraaksnelheid die omgevingspecifiek is. In de literatuur worden grote variaties voor afbraaksnelheden gevonden. 

 Vervluchtigen Vervluchtiging is de faseovergang van een verontreiniging opgelost in grondwater of als puur product naar de gasfase. Dit kan optreden indien de verontreiniging nabij de grondwaterspiegel is, doordat gas door de bodem stroomt tijdens een sanering (perslucht, ISCO), of door opwarming tijdens thermisch gestimuleerde extractie. 


 Eindrapportage SKB-project PT04-128 17\60 

## 4 De Wet bodembescherming als kader 

De 'Wet houdende regelen inzake bescherming van de bodem', beter bekend als de Wet bodembescherming (Wbb), vormt het wettelijk kader voor de aanpak van gevallen van historische bodemverontreiniging. Deze verontreinigen zijn opgetreden voor 1 januari 1987 en vormen in het algemeen de hoofdmoot van het aantal verontreinigingsgevallen. Voor de verontreinigingen ontstaan op of na deze datum geldt de Wet Milieubeheer waarin deze gevallen onder de zorgplicht vallen en dienen in principe zover dat redelijkerwijs geëist mag worden van de veroorzaker, volledig verwijderd en is de noodzaak voor het toepassen van een model veelal afwezig. Voor de aanpak van de historische gevallen en in enkele instanties de zorgplichtgevallen is het voor de bepaling van de mogelijk maatregelen veelal noodzakelijk een goed beeld te verkrijgen van de verspreidingsrisico's van de verontreiniging. Numerieke modellen voor het voorspellen van verontreinigingsrisico’s worden vrijwel alleen toegepast voor historische verontreinigingen. 

Sinds de invoering van de beleidsvernieuwing (Bever) als verwoord in Doorstart A5, 2001 en Van Trechter naar Zeef, spelen de verspreidingsrisico's een belangrijke rol bij de beoordeling van saneringsmaatregelen. Momenteel (2005) wordt er gewerkt aan een volgende beleidsvernieuwing waarin het gebruik van de bodem consequenter aan de mogelijkheden tot blootstelling aan en verspreiding van bodemverontreiniging wordt gekoppeld. Op basis van de blootstelling en de verspreidingsrisico's wordt bepaald of er maatregelen genomen moeten worden. Als de kans op blootstelling aan en verspreiding van bodemverontreiniging bij het aanwezige of voorgenomen bodemgebruik zo groot dat er sprake is van 'onacceptabele' risico's dienen er maatregelen te worden genomen, waardoor in ieder geval die onacceptabele risico's worden weggenomen. 

Omdat op basis van ondermeer de verspreidingsrisico's maatregelen moeten worden genomen die soms zeer ingrijpend zijn qua uitvoering en kosten is een goede inschatting van de verspreidingsrisico's zeer wenselijk. Ook dient de bepaling van de verspreidingsrisico's door alle stakeholders geaccepteerd te worden om het draagvlak van de juiste maatregelen mogelijk te maken en te implementeren. Het proces waarin de verspreidingsrisico's worden bepaald is complex en omvat verschillende fases. Ook zal in het kader van de Wbb een aantal fases doorlopen moeten worden om tot een voor alle partijen acceptabele situatie te komen. 


**18\60** Eindrapportage SKB-project PT04-128 

### 4.1 Faseringen in de Wbb 

 Binnen de Wbb is het noodzakelijk om nadat een helder beeld verkregen is van de verontreinigingssituatie een uitspraak te doen over de ernst en urgentie van de situatie. Afhankelijk van de ernst en urgentie zal de verontreiniging, in bron en pluim gebieden, aangepakt moeten worden met verschillende technieken en over verschillende tijdsperioden. Door de vele jaren sinds het ontstaan van de verontreiniging, de mogelijkheden binnen de Wbb om de verontreiniging over een langere tijd te saneren en de grote variatie in oplossingsmogelijkheden, is het gebruik van numerieke modellen voor het voorspellen van de verontreiniging gemeengoed. 

 Binnen het Wbb-traject dat doorlopen moet worden om een historische verontreiniging aan te pakken zijn verschillende fasen te onderkennen. Het traject omvat het gehele proces van het in beeld brengen van de verontreiniging tot en met de nazorg van een sanering. De onderscheidde fases zijn: 

1. Karakterisering van de verontreinigingssituatie 

2. Bepaling van ernst en urgentie 

3. Uitvoeren van een saneringsonderzoek 

4. Het opstellen van het saneringsplan 

5. Het uitvoeren van de sanering 

 en na evaluatie bij restverontreiniging 

6. Het opzetten van een nazorgplan en het uitvoeren van de nazorg 

 In de navolgende paragrafen wordt het doel van elk van deze fases beschreven. De mogelijkheden voor het gebruik van een numeriek model, de benodigde informatie en de mogelijke resultaten van een dergelijke inzet worden in hoofdstuk 13 Werkhandleiding Modelleer activiteiten beschreven. 

### 4.2 Afperking van de verontreiniging 

 De "karakterisatiefase" is geen fase als beschreven binnen het Wbb. Het is een fase waarin een goed beeld zal worden verkregen van de verontreinigingssituatie door het uitvoeren van verschillende typen onderzoek. Hieronder vallen ondermeer het historisch onderzoek, het oriënterend onderzoek, het verkennend onderzoek en het naderonderzoek. Door middel van de inspanningen die verricht worden in deze fase wordt in het reguliere proces een meer bekend over: 

- De ontstaansgeschiedenis van de verontreiniging 

- De in de bodem aanwezige verontreiniging(en 

- De verticale en laterale verspreiding van de verontreiniging 


 Eindrapportage SKB-project PT04-128 19\60 

Daarnaast kan in specifieke gevallen meer bekend worden over: 

- De bodemopbouw en ruimtelijk variatie hierin 

- De globale geohydrologische situatie 

- Wat de mogelijke receptoren zijn 

- Wie de betrokkenen zijn 

- Wat de toekomstplannen voor de locatie zijn In deze fase wordt de basis gelegd van het conceptueel model van de verontreinigingssituatie en wordt middels de eerste onderzoeken het conceptuele model verbeterd. 

### 4.3 Bepaling van ernst en urgentie 

In deze fase wordt op basis van de verontreinigingssituatie een beoordeling in het kader van ernst en urgentie uitgevoerd. De beoordeling van de ernst is op basis van de omvang van de verontreinigingscontour: de horizontale en verticale interventiewaarde contour. Daarnaast dient inzicht te zijn in de omvang van de streefwaarde contour .De beoordeling van de urgentie is op basis van risico's. De drie vormen van risico's zijn humane risico's, ecologische risico's en verspreidingsrisico's. De beoordeling van de ernst en urgentie wordt naar het zich doet aanzien ergens in 2006 aangepast. Deze aanpassing zal voornamelijk invloed hebben op de bepaling van de urgentie met de verspreidingsrisico’s in het bijzonder. 

In de huidige Wbb wordt voor niet urgente gevallen van bodemverontreiniging ook geen tijdstipbepaling voor aanvang van sanering opgesteld. De noodzaak voor uitvoering van de vervolgstappen is niet direct aanwezig. Voor urgente gevallen van bodemverontreiniging wel, aangezien hieraan wel een tijdstipbepaling voor aanvang van sanering wordt gesteld (afhankelijk van mate van urgentie). De ernst en urgentie bepaling wordt altijd door het bevoegd gezag vastgelegd in een beschikking. 

### 4.4 Uitvoeren van een saneringsonderzoek 

Als de verontreinigingssituatie als urgent is beoordeeld, is het opstellen van een saneringsplan noodzakelijk (hierop dient het bevoegd gezag weer een beschikking af te geven) alvorens met een eventuele sanering kan worden gestart. Zeker voor meer complexe verontreinigingssituaties is het aan te bevelen om een saneringonderzoek uit te voeren. Een saneringsonderzoek heeft in de huidige Wbb geen wettelijke status. 

In juni 1997 heeft het Kabinet een standpunt ingenomen over de vernieuwing van het bodemsaneringsbeleid. Een belangrijk onderdeel hiervan is een nieuwe saneringsdoelstelling: “functiegericht en kosteneffectief saneren” voor historische gevallen van bodemverontreiniging. Voor functiegericht en kosteneffectief saneren gelden een aantal strategische doelstellingen. Deze saneringsdoelstellingen zijn beschreven in het rapport “Van Trechter Naar Zeef, afwegingsproces saneringsdoelstelling” (SDU, oktober 1999). 


**20\60** Eindrapportage SKB-project PT04-128 

 Ten aanzien van de (mobiele) verontreinigingen in de ondergrond geldt als algemene doelstelling “het bereiken van een stabiele eindsituatie binnen 30 jaar”. Er is sprake van een stabiele eindsituatie indien er: 

- Geen verdere verspreiding van de verontreiniging optreedt 

- Geen risico’s (humaan en ecologisch) aanwezig zijn 

- Geen kwetsbare objecten worden bedreigd 

- Geen verstoring van de stabiele eindsituatie door voorzienbare ontwikkelingen     optreedt 

 Het begrip “stabiele eindsituatie” is nader uitgewerkt in het eindrapport project “Doorstart A5” (werkwijze voor beslissingen over de aanpak van verontreinigingen in de ondergrond van 2 juli 2001). Het afwegingsproces is weergegeven in de zogenaamde landelijke saneringsladder. 


 Eindrapportage SKB-project PT04-128 21\60 

Het huidig functionele bodemsaneringsbeleid volgens BEVER is gericht op het bereiken van een trede 1 (multifunctioneel saneren (MF), geen nazorg en restverontreinigingen) op de saneringsladder. Hiervan mag onderbouwd mag worden afgeweken op basis van technische haalbaarheid, kosteneffectiviteit, gebruiksfunctie, rendement etc. De sanering dient veelal te leiden tot doel waarbij de bodem geschikt is voor het gebruik en het wegnemen van risico’s. Indien onderbouwd kan worden afgeweken van trede 1, dient gestreefd te worden naar trede 2 of een trede 3, afhankelijk van de omvang van de restverontreiniging. Trede 4 en trede 5 hebben betrekking op een IBC-variant (Isoleren, Beheersen en Controleren). Met een IBC-variant zal alleen worden ingestemd indien een stabiele eindsituatie (trede 2 of 3) niet haalbaar wordt geacht. 

Het saneringsonderzoek heeft tot doel om de mogelijke saneringstechnieken voor de aanpak van de verontreinigingssituatie op een heldere en goed onderbouwde wijze met elkaar te vergelijken. Een MF-variant (of maximaal haalbare variant) dient in het saneringsonderzoek veelal als referentie te worden meegenomen. Indien ook een functionele variant mogelijk moeizaam haalbaar is, kan een IBC-variant ook worden betrokken in de afweging. Op basis van deze vergelijking zal, in samenspraak met de betrokkenen, door de probleembezitter de voorkeursvariant worden geselecteerd. Zaken die voor het bereiken van deze doelstelling voor ogen gehouden dienen te worden, zijn: 

- Concretiseren van de strategische saneringsdoelstellingen (bodem geschikt     maken voor gebruik en wegnemen risico’s), rekening houdend met eisen en     wensen stakeholders 

- Bepalen van haalbare saneringstechnieken 

- Inzicht geven in de baten en lasten van de verschillende     saneringstechnieken1) 

- Inzicht geven in het verspreidingsgedrag van de restverontreiniging na     sanering bij verschillende varianten 

- Inzicht geven in de risico’s van de saneringsvarianten en mogelijke     faalscenario’s 

- Bepalen van de meest haalbare, handhaafbare en kosteneffectieve aanpak,     die ook door de meest belangrijke partijen gedragen wordt 

- Basis bieden voor het saneringsplan. 

Ten aanzien van het afwegen van de baten en lasten van de verschillende saneringstechnieken kan het volgende opgemerkt worden: In het kader van een tweetal SKB projecten, ROSA I en ROSA II, Robuuste Saneringsafweging is een afwegingssystematiek ontwikkeld waarbij op kwantitatieve wijze de verschillende saneringsvarianten met elkaar worden vergeleken op baten en lasten. 


**22\60** Eindrapportage SKB-project PT04-128 

 Hierbij is een vaste set aan afwegingsaspecten benoemd namelijk: Baten: risicoreductie, herstel gebruiksmogelijkheden, pluimgedrag, verwijderde vracht, afname aansprakelijkheid Lasten: saneringskosten, saneringsduur en nazorg, faalrisico’s, belasting andere milieucompartimenten. Mede op basis van deze afweging zal met de meest belangrijke partijen de voorkeursvariant worden bepaald, welke in het saneringsplan nader zal worden uitgewerkt. 

 Zeker bij complexe verontreinigingssituaties is het voorafgaand aan het saneringsonderzoek opstellen van een modellering (2D of 3D) van groot belang. Op basis van een goed gevuld, gekalibreerd en onderbouwd model kunnen reeds keuzes gemaakt worden welke technieken mogelijk van toepassing kunnen zijn of niet. Een dergelijk model is derhalve zeer belangrijk voor het maken van een goed onderbouwde (voorkeurs)variant. 

### 4.5 Het opstellen van het saneringsplan 

 De variant die geselecteerd is in de saneringsonderzoeksfase dient nader uitgewerkt te worden. Doel van het saneringsplan is dan ook het op dusdanig gedetailleerd niveau beschrijven van de geselecteerde saneringsvariant zodat met alle betrokken partijen overeenstemming kan worden bereikt. Technisch inhoudelijk dient hierbij gedacht te worden aan de positionering van de onttrekkingsfilters, de monitoringspunten, het te onttrekken debiet per bodemlaag en per filter etc. 

 Tevens dienen eventuele monitoring en/of nazorg beschreven te worden alsmede een terugvalscenario voor het geval de variant uiteindelijk niet of onvoldoende blijkt te functioneren. Ook dient het saneringsplan als basis voor een op te stellen werkomschrijving of bestek en dient het te voldoen aan zowel het beleid als de lokaal geldende provinciale milieuverordening (PMV). Het saneringsplan dient als basis voor de uit te voeren sanering waarop door het bevoegd gezag beschikking zal worden verleend. 

 Belangrijk aspect in het saneringsplan is het beschrijven van de saneringsdoelstelling (kan eventueel ook al worden gedaan na het afwegingsproces in de saneringsonderzoeksfase). De saneringsdoelstelling wordt opgesplitst in 2-delen, namelijk: 

1. Eisen ten aanzien van de minimale doelstelling 

- Wegnemen onacceptabele risico’s voor receptoren, en/of het geschikt     maken van de bodem voor de functie 

- Afgesproken pluimgedrag, en daarmee de mate van zorg (actief, registratie     of nazorg) waarvoor is gekozen 

2. Een verwachting of streven ten aanzien van de restconcentratie,     vrachtverwijdering of saneringsduur. 


 Eindrapportage SKB-project PT04-128 23\60 

### 4.6 Het uitvoeren van de sanering 

Dit is voor de praktijk de belangrijkste fase: de risico's en verontreiniging worden gemitigeerd. Tijdens de uitvoering van de saneringsmaatregelen worden de geplande werkzaamheden uitgevoerd en wordt duidelijk of de werkelijkheid zo is zoals verwacht. In het algemeen zal de werkelijkheid anders zijn dan gedacht en zal op basis van de veldwaarnemingen en de interpretatie hiervan duidelijk worden of, en zo ja welke aanpassingen nodig zijn. Voor de interpretatie en de selectie van aanpassingen kan een numeriek model toegepast worden. Ook kan het model gebruikt worden om de voorspelde waarden te toetsen. 

### 4.7 Het uitvoeren van de nazorg 

De nazorg fase is een fase binnen de saneringsaanpak waarin in het algemeen weinig veranderingen horen op te treden. Na afronding van de voornaamste saneringsmaatregelen is het de verwachting dat de verontreiniging gesaneerd is tot de doelstelling en dat middels nazorg de restverontreiniging gemonitord wordt. 

Veel van de werkzaamheden in deze fase zullen bestaan uit het periodiek bemonsteren van peilbuizen en het analyseren van het bemonsterde grondwater. De interpretatie van de waarnemingen dienen periodiek geëvalueerd en geïnterpreteerd te worden. Een numeriek model kan hiervoor een welkom of zelfs essentieel hulpmiddel zijn. 


**24\60** Eindrapportage SKB-project PT04-128 


 Eindrapportage SKB-project PT04-128 25\60 

## 5 Beschrijving van de probleemstelling, doelstelling 

## en gekozen oplossing 

### 5.1 Probleemstelling 

Het verspreidingsgedrag van een verontreiniging vormt veelal de aanleiding voor het uitvoeren van saneringsmaatregelen. Voor het bepalen en voorspellen van de verspreidingsrisico's is geen door alle stakeholders aanvaarde manier voorhanden. Een van de meest gebruikte middelen om de verspreidingsrisico's te bepalen is het opstellen van een numeriek model van de verontreiniging op basis van beschikbare gegevens over de bodemopbouw, geohydrologie en verontreinigingscondities. Hiermee wordt een voorspelling gedaan van de verspreiding. 

Eén door alle stakeholders aanvaarde eisen aan een dergelijk numeriek grondwaterstromingsmodel, ontbreekt. Verschillende partijen hebben andere verwachtingen ten aanzien van de waarde, nauwkeurigheid en bruikbaarheid van een vastgestelde relatie tussen de bron en de pluim en de voorspelling van het pluimgedrag. 

Door het ontbreken van eenduidige eisen maken dat foutieve keuzes en eisen ten aanzien van saneringsmaatregelen genomen kunnen worden. Daarnaast kan een niet gedeeld beeld van de mogelijkheden en onmogelijkheden en toepasbaarheid van numerieke en analytische modellen onder verschillende omstandigheden tot conflicten leiden tussen verschillende stakeholders:. Ook kan het niet delen van hetzelfde beeld aan mogelijkheden en onmogelijkheden leiden tot onbegrip wat soms kan leiden tot wantrouwen. Dit leidt veelal tot vertraging van de werkzaamheden. 

### 5.2 Doelstelling 

De doelstelling van het aanleunproject was om te achterhalen of met de huidige kennis en technieken een betrouwbare voorspelling gemaakt kan worden van de verspreidingsrisico’s van complexe bodemverontreiniging die door alle stakeholders aanvaard wordt. Hierbij was vooral de betrokkenheid van partijen als het bevoegde gezag en mogelijke buren van belang. 

Voor alle betrokkenen werd inzichtelijk gemaakt wat de meerwaarde van het numerieke model is binnen de verschillende fases van Wbb-traject. Daarbij dienden de (on)mogelijkheden van een model voor iedereen zichtbaar gemaakt worden. 


**26\60** Eindrapportage SKB-project PT04-128 

### 5.3 Gekozen oplossing(srichting) 

 Op basis van de reeds beschikbare informatie en modellen is in een cyclisch proces nagegaan in hoeverre het op een algemeen gedragen wijze de relatie tussen de grondverontreinigingen en de grondwaterverontreinigingen en de verspreidingsrisico's voor twee verontreinigingsituaties kunnen worden gelegd. De cases betroffen twee gescheiden gevallen van grondwaterverontreiniging: één met benzeen en één met furfural beide gelegen op het terrein van Shell. Voor het vaststellen van de relatie tussen de bron en de pluim, de verspreidingsrisico's en de 'waardebepaling' van de voor is waren en zouden komen, is alleen gebruik gemaakt van de gangbare (onderzoeks)technieken. 

 De drie brainstormsessies met de betrokken stakeholders en experts met elk een verschillende achtergrond heeft ervoor zorg gedragen dat een breed pallet aan visies en de mogelijke scenario's zijn doorlopen. In verschillende ronden zijn de modelleerwerkzaamheden uitgevoerd om inzicht te krijgen in het proces om tot een goede waardeschatting te komen van de modelvoorspellingen. 

### 5.4 Deelnemers 

 In de onderstaande tabel is een overzicht gegeven van alle betrokkenen bij het project en de rol die zij in het project vertegenwoordigen. 

 Bedrijf Contactpersoon Rol in project Rolf Hetterschijt Consortiumlid / Eindgebruiker / Voorzitter Denktank Shell Nederland Raffinaderij bv Arie Hoek Consortiumlid / Eindgebruiker Minke de Vries Consortiumlid / Eindgebruiker Laurent Bakker Consortiumlid /Penvoerder Tauw bv Marcus van Zutphen Consortiumlid / Projectleider Louise Wipfler Consortiumlid TNO NITG Johan Valstar Consortiumlid / Modelleur Havenbedrijf Rotterdam Willem van Hattem Consortiumlid / Eindgebruiker Royal Haskoning/GT Timo Heimovaara Panellid Denktank Royal Haskoning Jan Taat Panellid Denktank Rijkswaterstaat Pim Neefjes Panellid Denktank DCMR Milieudienst Rijnmond Jan Nieuwenhuizen Panellid Denktank Ministerie van VROM Miech de Steenwinkel Panellid Denktank 


 Eindrapportage SKB-project PT04-128 27\60 

**Bedrijf Contactpersoon Rol in project** 

SKB Han de kreuk Panellid Denktank / SKB-vertegenwoordiger 

Oranjewoud Alex Meertens Uitvoering bodemonderzoek/ Deelname aan denktank 

Grontmij Doite Schaap Uitvoering bodemonderzoek/ Deelname aan denktank 



 Eindrapportage SKB-project PT04-128 29\60 

## 6 Probleem-identificatie-proces 

Het probleem identificatie proces bestaat uit twee delen. Ten eerste, dient er een globaal beeld te zijn van de verontreiniging, kwetsbaarheden en risico's en ten tweede moet er inzicht zijn in het maatschappelijke krachtenveld, de (potentieel) betrokkenen, hun rol en de wensen en eisen. Zowel het globale beeld als het maatschappelijke krachtenveld bepalen de mate van detail waarmee het conceptuele model, dat ten grondslag zal liggen aan elke aanpak van een verontreinigingsgeval, moet worden onderbouwd. Wat is een accuraat genoeg beeld? Wat zijn de geplande maatregelen? Wat zijn de verschillende hypotheses, de belangen, de te beschermen objecten, en de te onderzoeken saneringsdoelstellingen die onderzocht moeten worden? 

Het doel en de toepassing van het model van de verontreinigingssituatie dienen voorafgaand aan de werkzaamheden geïnventariseerd te worden om de onderzoeksinspanningen te bepalen. Vooraf moet duidelijk worden gesteld welke vragen het model moet kunnen beantwoorden voor de wensen en eisen van de maatschappelijk betrokkenen. Aan de hand hiervan zal een keuze voor het model gemaakt worden. Hierbij zal gedacht moeten worden aan: welke model-code, de modelopzet, de te modelleren processen, de te hanteren wensen en randvoorwaarden en het schaalniveau van de modellering. Daarna zal geïnventariseerd moeten worden wat de beschikbare gegevens zijn en indien nodig, zullen reeds voorafgaand aan de modellering aanvullende gegevens vergaard moeten worden. In paragraaf 6.1 wordt een overzicht gegeven van de betrokkenen die invloed hebben op de aanpak van de sanering. In de daaropvolgende paragraaf wordt nader ingegaan op het onderscheid tussen een conceptueel model en een numeriek model. Als laatste worden in dit hoofdstuk de fysieke omstandigheden die het conceptueel model vormen toegelicht. 

### 6.1 Potentieel betrokkenen en hun wensen en eisen 

Om tot een gedragen aanpak van een geval van bodemverontreiniging te komen is het noodzakelijk de verschillende betrokkenen te identificeren. Voor de twee cases is een inventarisatie gemaakt. In de onderstaande tabel is in de eerste kolom een overzicht gegeven van verschillende potentieel betrokkenen. In de tweede kolom zijn verschillende documenten en mogelijke formaliseringen die ten grondslag kunnen liggen aan de wensen en eisen van de betrokkenen. 


**30\60** Eindrapportage SKB-project PT04-128 

 Tabel 6.1 Overzicht van potenieel betrokkenen en de mogelijke achtergronden van hun wensen en eisen 

 Terreineigenaren Beheersplannen, contracten en saneringsplicht veroorzaker Terreingebruikers Bedrijfspolicy’s / Locatiebeheersplannen Bevoegde gezagen WBB , toetser en handhaver; Wvo toetser en handhaver. Buren Belangen van buren (overlast, zorg) Vorige eigenaren Overdracht verantwoordelijkheden Contractdocumenten overname terreingebruik Aannemers en adviseurs Ontwerp en en uitvoering saneringen Derden Afspraken/contracten met derden 

 Naast de betrokkenen gelden vanzelf sprekend de bedrijfs-policy's, weten regelgeving, wensen en eisen van de buren (Rijkswaterstaat (RWS) voor de havens en terreineigenaren van aanliggende terreinen) en de potentiële receptoren als het oppervlaktewater en kwetsbare gebieden in de omgeving. Gezamenlijk bepalen zij het maatschappelijke kader voor de toetsing van de bruikbaarheid van het model. Dit met name ten aanzien van de verwachte waarde, de nauwkeurigheid en de bruikbaarheid van de vastgestelde relatie tussen bron en pluim en de voorspellende waarde hiervan. 

 Voor de onderhavige saneringslocaties zijn de betrokkenen: 

 Shell die als terreingebruiker en veroorzaker van de verontreiniging een saneringsverplichting. 

 Het bevoegd gezag voor beide saneringslocaties zijn de Gemeente Rotterdam in het kader van de Wbb en Rijkswaterstaat in het kader van de Wet verontreiniging oppervlaktewateren (Wvo). De DCMR Milieudienst Rijnmond voert de taken van als bevoegd gezag en handhaver namens de gemeente Rotterdam uit. 

 Het Havenbedrijf Rotterdam is eigenaar van het terrein. 

 De buren zijn momenteel nog niet betrokken bij de beoordeling van het model en de noodzakelijk maatregelen. 

 Bij het opstellen van het model zijn de adviseurs en modelleurs betrokken geweest om invulling en sturing te geven aan het opstellen van zowel het conceptuele als het numerieke model. 


 Eindrapportage SKB-project PT04-128 31\60 

In het onderstaande figuur is de inbedding van de modellering binnen de verschillende deelgebieden. Het meest brede maatschappelijke kader wordt gevormd door de (inter)nationale wetgeving, gevolgd door de beschikbare geaccepteerde locatiebeheersplannen en bedrijfspolicies. Op een meer lokaal niveau gelden de afspraken met en eisen van de buren en anderen ten aanzien van de verontreiniging. De meest specifieke voorwaarden zijn gelegen in de locatie specifieke omstandigheden: de fysieke werkelijkheid en de eigenschappen van de verontreiniging. 

 Figuur 6.1 Overzicht van de verschillende niveaus van invloed 

### 6.2 Waarom voor een numeriek model 

De keuze voor het maken van een numeriek model kan verschillende achtergronden hebben. Deze achtergronden zijn veelal gelegen in de vraag wat beoogd wordt met het model maar het gebruik voor het maken van voorspellingen van de verspreidingsrisico's onder de huidige en/of gemodificeerde condities zal hier vrijwel altijd een onderdeel van vormen. Allerlei partijen die betrokken zijn bij een geval van verontreinigd grondwater kunnen een numeriek model wensen met verschillende doelen voor ogen. Voordat besloten wordt een model te maken dient een gezamenlijk doel vast gesteld te worden. Of dienen de doelstellingen van de betrokkenen binnen het concept van het op te stellen model te passen. 

De belangrijkste redenen worden in de paragrafen kort beschreven. 

**6.2.1 Het overdragen van het conceptuele grondwaterstromingsmodel** Een numeriek model kan zeer goed gebruikt worden om de gevormde denkbeelden (conceptueel model) over de geohydrologische en verontreinigingssituatie over te dragen en kwantitatief te onderbouwen. Een numeriek model maakt het mogelijk om de gevormde denkbeelden van het conceptuele model helder over te brengen op anderen. 

 Wetgeving, Locatiebeheerplannen, Bedrijfs-policy 

 Buren en afspraken derden 

 Historie Geologie Stofeigenschappen et cetera 


**32\60** Eindrapportage SKB-project PT04-128 

 Om deze overdracht goed mogelijk te maken is het noodzakelijk een goed beeld van de geologie en geohydrologie te hebben. Daarnaast dient voor de overdracht een juiste keuze van het model gemaakt te worden. Zo kan gekozen worden uit een grote selectie aan modellen: 1 Dimensionale, 2 Dimensionale modellen (zowel in het horizontale als verticale uitvoering), 3 Dimensionale waarbij verschillende bodemlagen ingebracht kunnen worden, en natuurlijk kunnen al deze modellen stationair of tijdsafhankelijk zijn. 

 In dit type model zijn met name de geologische en geohydrologische schematisatie en parameters het belangrijkste. De bodemopbouw, de stijghoogten metingen en de variaties in de grondwaterstanden en onttrekkingsmiddelen in de omgeving vormen samen met de randvoorwaarden voor het model de voornaamste invoerparameters. 

 6.2.2 Het valideren van stoftransport Het meenemen van stoftransport in het numerieke model is veelal wenselijk om aan te tonen dat de gevonden geohydrologische beschrijving op basis van de geologische en geohydrologische gegevens ook kan voorspellen hoe de huidige verontreiniging zich heeft gevormd. De verontreiniging kan dienen als een soort tracer in het geohydrologische systeem. 

 Om stoftransport goed op te kunnen nemen in het numerieke model zijn naast de benodigde input gegevens uit de vorige paragraaf ook gegevens over de concentraties, retardatie, diffusie en dispersie van de verontreiniging in de ondergrond nodig. 

 Het opstellen van een dergelijk model kan alleen plaatsvinden nadat een goed geohydrologisch model is opgesteld. Dit komt om dat stoftransport voor het overgrote deel bepaald wordt door advectief transport: transport met het grondwater. 

 Het kwantitatief onderbouwen van het stoftransport kan zeer goed helpen met het vaststellen waar de grondwaterverontreiniging zich heen beweegt en wat de verspreidingsrisico's hiervan zijn. Zo kan bijvoorbeeld duidelijk worden of verontreinigd grondwater zich in de richting van kwetsbare receptoren stroomt en of bijvoorbeeld terreingrenzen worden overschreden. 

 Een andere belangrijke eigenschap van een stoftransportmodel is de mogelijkheid om massafluxen aan verontreinigingen te bepalen: de hoeveelheid verontreiniging dat per tijdseenheid een bepaald doorstroom oppervlak doorstroomt. 


 Eindrapportage SKB-project PT04-128 33\60 

Een andere belangrijke eigenschap van een stoftransportmodel is de mogelijkheid om massafluxen aan verontreinigingen te bepalen: de hoeveelheid verontreiniging dat per tijdseenheid een bepaald doorstroom oppervlak doorstroomt. 

### 6.3 Fysieke omstandigheden 

Fysieke omstandigheden die het conceptuele model vormen van de verontreiniging en die effect hebben op de onderzoeksinspanning zijn bijvoorbeeld: 

- Beschikbaarheid historische gegevens 

- Bodemeigenschappen/geohydrologie/geologie 

- Stofeigenschappen (mobiliteit, oplosbaarheid, dichtheid, toxiciteit potentie voor     natuurlijke afbraak etc) 

- Receptoren 

- Saneringsmaatregelen 

Bij aanvang van het uitwerken van de bron-pluim relatie bestaat er over het algemeen al een globaal beeld van de verontreinigingssituatie. Men is op de hoogte van de historie van de verontreiniging (tankplaat, calamiteit etc), er zijn monitoringsgegevens aanwezig en vanuit de grondwaterkaart van Nederland is er een regionaal stromingsbeeld aanwezig. Terreininspectie, luchtfoto's en gesprekken met betrokkenen geven inzicht in de mogelijke bedreigde objecten. 

Op basis van deze en andere beschikbare gegevens wordt het eerste conceptuele model opgesteld. Zoals aangegeven in paragraaf 6.2 zal afhankelijk van de gekozen vraagstelling nagegaan moeten worden of het 1e conceptuele model voldoende is om vragen te beantwoorden. 

 In het kader van het project was bij de Benzeen-locatie de grondwaterstroming en een gedeeltelijk stoftransport in het model verwerkt. Omdat niet de volledige vorming van de grondwaterverontreiniging met het numeriek model achterhaald kon worden, kan niet worden gesteld dat het gehele stoftransport in het model verwerkt was. Met het model was het wel goed mogelijk om de aangetroffen concentraties in het grondwater naar de toekomst te kunnen extrapoleren en in combinatie met de grondwaterstroming was het mogelijk om een flux te bepalen. Deze flux is bepaald over het doorstroomoppervlak dat gelegen was direct onder de terreingrens met de haven. 


**34\60** Eindrapportage SKB-project PT04-128 


 Eindrapportage SKB-project PT04-128 35\60 

## 7 Conceptueel model 

Bij het aangaan van onderzoekswerkzaamheden naar de ernst en aard van mogelijke verspreiding van verontreiniging dienen verschillende aspecten vooraf helder geformuleerd te worden. Hierbij dient allereerst een conceptueel model van de situatie opgesteld te worden. In dit conceptuele model dienen potentiële bronnen, de mogelijke transportroutes en de mogelijke receptoren geïdentificeerd te worden. Daarnaast dienen kritische punten als terreingrenzen, kadastrale perceelsgrenzen, en overgangen in geologie (bijvoorbeeld breukvlakken en randen van geologische eenheden als kleilagen en leemlenzen) in kaart te worden gebracht. 

Voorbeeld van mogelijke scenario’s die geverifieerd moeten worden: 

Op basis van het conceptuele model wordt de data verzameld en geïnventariseerd. Veelal wordt het conceptuele model vertaald naar een numeriek model. Het conceptuele model wordt continu bijgesteld gedurende het proces door nieuwe informatie Belangrijk is dat alle belangrijke mogelijke aspecten die van invloed zijn op de bron-pluim ontwikkeling in het model worden opgenomen zijn. Voorbeelden van invloeden zijn dijklichamen, leidingstraten, voorkeursstromen en verspreiding van verontreiniging via het riool. Maar ook de aanwezigheid van drijfen zaklagen. Met de inzet van de denktank is dit voor de beschouwde cases uitvoerig gebeurd. 

 Overwegingen over de Furfural verontreiniging tijdens 1 ste^ brainstormsessie: 

- ‘Mogelijk is oorspronkelijk sprake geweest van één spill waarna er (plaatselijk)     afbraak is opgetreden. Dit zou het voorkomen van de losse     verontreinigingsvlekken zonder duidelijke bron kunnen verklaren;’ 

- ‘het verontreinigingsbeeld geeft weer dat er mogelijk sprake is van preferente     stroombanen;’ Overwegingen over de Benzeen verontreiniging tijdens 1ste^ brainstormsessie 

- ‘de oorspronkelijke bronnen van de benzeenverontreiniging in de ophooglaag zijn     grotendeels al opgelost zodat er daar nu lage concentraties of zelfs geen     benzeen wordt gemeten.’ 

- Historisch gezien is er geen directe aanleiding de benzeenverontreiniging te     relateren aan de op de locatie uitgevoerde activiteiten (te weten vorige eigenaar,     batch kraker, VC-fabriek, tankpark, waterzuivering); 

- Verspreidingsbeeld van de verontreiniging sluit verspreiding via het riool uit. 


**36\60** Eindrapportage SKB-project PT04-128 

 Voorbeeld van het in kaart brengen van invloeden en de bijbehorende afwegingen. 

 Voor het de furfurallocatie is onderzocht of de voormalige dijklichamen een storende werking hadden op de verspreiding van de verontreiniging. De ligging en mogelijk vormen van voorkomen bleek dat deze dijklichamen is in het numerieke model onderzocht. 

 Uiteindelijk bleek deze aanname ten aanzien van het grondwaterstromingspatroon niet significant beïnvloed wordt door deze dijklichamen. Het conceptuele model waarin deze dijklichamen aanwezig waren kon door het verwerken van dit conceptuele model in een numeriek model, ontkracht worden. 


 Eindrapportage SKB-project PT04-128 37\60 

## 8 Beschikbare data 

De beschikbare data vormen samen met het conceptuele model en het doel van de numerieke modelleerwerkzaamheden de basis van de grondwatermodellering. De beschikbare data dienen vergaard te worden uit zo veel mogelijk betrouwbare (instituten, dossiers, veldmetingen) en mogelijk minder betrouwbare bronnen (overlevering, suggestieve meldingen, inschattingen). Hierna dienen deze geordend en beoordeeld te worden op bruikbaarheid en betrouwbaarheid. 

### 8.1 Welke data 

Op basis van het voorlopige conceptuele model moet in kaart worden gebracht welke harde en zachte data beschikbaar zijn. Dit gaat om data op het gebied van: 

- Bodemopbouw en geohydrologie 

- Oppervlaktewater 

- Bodemgebruik op de locatie 

- Historische gegevens 

- Verontreinigingssituatie (opgelost product/ drijflaag-zaklaagbepaling) 

- Geochemische processen waaronder oplosbaarheid en sorptie 

- Afbraakproducten en -processen Met harde data wordt bedoeld kwantitatieve gegevens zoals stijghoogten en concentraties. Onder zachte data wordt bijvoorbeeld verstaan verhalen van terreingebruikers over de historie van het terrein, de aanwezigheid van afbraakproducten (niet gekwantificeerd). Met behulp van de data dient het conceptuele model te worden geverifieerd en kunnen soms mogelijke scenario’s worden uitgesloten. Voor de numerieke modellering zijn vervolgens kwantitatieve gegevens nodig. Al gedurende het verzamelen van de data wordt het conceptuele model aangepast aan de nieuwe bevindingen. 

Voorbeeld beschikbare gegevens en bruikbaarheid van de gegevens: 


**38\60** Eindrapportage SKB-project PT04-128 

### 8.2 Bruikbaarheid en betrouwbaarheid van data 

 De beoordeling op betrouwbaarheid en bruikbaarheid zijn van groot belang voor de beoordeling van het eindresultaat. Bij alle modellen geldt nog altijd de uitspraak "rubbish in = rubbish out". Bij de beoordeling van de bruikbaarheid en betrouwbaarheid kunnen verschillende criteria gebruikt worden. Hieronder is een kort, niet volledig lijstje met criteria: 

- Representatief voor het gebied. De gegevens moeten op dusdanig     schaalniveau zijn dat het aansluit bij het gewenste schaalniveau van het     numerieke model om de vraagstelling te beantwoorden. Dit betekent dat     wanneer alleen regionale grondwatergegevens aanwezig zijn de mate van     betrouwbaarheid van het numerieke model (dat op lokale schaal is     gedetailleerd) laag is. De schaal van het numerieke model wordt vervolgens     weer bepaald door de schaal van de verontreiniging en de complexiteit van de     ondergrond/ geohydrologie voor zover bekend 

- Grondwaterstanden gemeten ten opzichte van een vast punt 

- Data van meting grondwaterstanden goed vastgelegd en bij voorkeur veel     metingen op dezelfde dag om verstoringen door fluctuaties als gevolg van     bijvoorbeeld getijde te voorkomen 

- Boorbeschrijvingen zijn van kwalitatief goede boringen (geen avegaar- of     spoel-boringen) om zo een beter beeld van de bodemopbouw te verkrijgen 

 Voor de situatie op het terrein van Shell is een semi-regionaal grondwaterstromingsmodel beschikbaar. Dit model is in het verleden opgesteld op basis van de toen beschikbare boorprofielen, sonderingen en kennis over de bodemopbouw. Dit model heeft een mate van detail die toegesneden was op de locatie als geheel, maar dit is voor detail onderdelen als de twee onderhavige verontreinigingsituaties een te grote mate van onnauwkeurigheid. Uit het model zijn wel de algemene grondwaterstromingsrichting, de grondwaterstromingsnelheid en de verschillende laagdikten te halen. Maar deze zijn natuurlijk niet locatie specifiek in beeld gebracht. Bij aanvang van de werkzaamheden van dit project zijn naast het model ook andere gegevens beschikbaar als bijvoorbeeld de mogelijke bronlocatie op het Shell terrein en daarbuiten en de verschillende meetpunten voor grondwaterstanden en grondwatermonstername. 

 Resultaat 1ste brainstormsessie benzeenverontreiniging: ‘’Er is een tritium/helium bepaling uitgevoerd ter vaststelling van de ouderdom van het water. Aan de hand van de meetresultaten is gebleken dat het regionaal geohydrologische model, dat vooralsnog op de locatie werd toegepast, niet van toepassing is op dit gedeelte van het Shell-terrein. Het infiltratiewater verplaatst zich 6x zo langzaam dan in het model wordt geschetst’’. 


 Eindrapportage SKB-project PT04-128 39\60 

- Dekkingsgraad van de boringen en sonderingen zijn in overeenstemming met     de mate van heterogeniteit van de ondergrond. Een heel heterogeen gebied     kan niet in beeld gebracht worden met een grote onderlinge afstand tussen de     filters. Een homogene zandgrond daarentegen wel. 

- Concentratiemetingen zijn op alle relevante componenten 

- Concentratiemetingen zijn betrouwbaar? Indien hierover twijfels zijn kan het     mogelijk getoetst worden door her-bemonstering en (her)analyse. 

- Gehalten aan verontreiniging in de grond zijn betrouwbaar bepaald (gebruik     van steekbussen voor vluchtige verbindingen etc.). 

- Gehalten zijn representatief voor de verschillende bodemlagen; indien er     binnen en bodemlaag een groot concentratieverloop (te verwachten) is, dient     de filterstelling van de peilbuis bekend te zijn en dient dit gegeven in de     interpretatie te worden meegenomen. 

- De verontreiniging moet zo mogelijk zijn afgeperkt voor grond en grondwater     waarbij beide gehalten of concentraties. Grond bepaald veelal de bronzone en     het grondwater met name de pluim. 

- de bronnen moeten zo goed mogelijk zijn geïdentificeerd en afgeperkt 


**40\60** Eindrapportage SKB-project PT04-128 


 Eindrapportage SKB-project PT04-128 41\60 

## 9 Numerieke modellering 

Een vergelijking tussen het oorspronkelijke conceptuele model en de veldgegevens geeft inzicht in de betrouwbaarheid van het conceptuele model ter representatie van de werkelijkheid. Met behulp van het numerieke model kan het conceptuele model worden gekwantificeerd, fysische en chemische processen inzichtelijk worden gemaakt en de gevoeligheid voor de verschillende parameters inzichtelijk worden gemaakt. Ook eventuele conceptuele inconsistenties komen naar boven en daarnaast eventuele fouten die bij het meten zijn opgetreden. Het numerieke model wordt gekalibreerd aan de data om vervolgens toekomstige ontwikkelingen te kunnen voorspellen. Tijdens het numeriek modelleren wordt de loop “conceptueel model-data-numeriek model” een aantal maal doorlopen. Het numerieke model kan worden ingezet om verschillende scenario’s door te rekenen en op die manier bepaalde mogelijke scenario’s uit te sluiten. Of, wanneer dat niet mogelijk is, de verschillende scenario’s allen te toetsen aan criteria die zijn opgelegd door het maatschappelijke kader. Bijvoorbeeld het overschrijden van de terreingrens; wanneer dat in alle mogelijke gevallen niet gebeurt, is er voldoende antwoord op de gestelde vraag, maar is er nog geen volledige zekerheid omtrent het gedrag van de verontreiniging. Ook kunnen numerieke modelscenario’s worden gebruikt om een meetstrategie te vinden, waarin deze scenario’s kunnen worden gevalideerd. 

Belangrijk bij de interpretatie van de gegevens is het bewustzijn van de beperkingen van het model en de data. Het model blijft een simplificatie van de werkelijkheid. Van de harde gegevens moet daarom de betrouwbaarheid worden ingeschat en ook de betekenis voor de modellering (gevoeligheid). Daarnaast geldt dat vrijwel elke meting zeer lokaal is of slechts een waarneming op één tijdstip. Ruimtelijk en temporele variabiliteit zal altijd een grote invloed hebben op toepasbaarheid van gegevens. Hier komt toch het fingerspitzengefuhl van de modelleur kijken. 

Voor de data geldt dat wanneer er weinig en onbetrouwbare data beschikbaar zijn, dan kan het model nog zo geavanceerd zijn, het resultaat zal geen tot weinig betekenis hebben omdat het model niet goed gekalibreerd of gevalideerd kan worden. Onbetrouwbare data leveren veelal onbetrouwbare modelresultaten. 

 Toetsen conceptueel model met numeriek model 1 ste^ brainstorm sessie (furfuralverontreiniging): 

- Drie modelvarianten zijn ontwikkeld om de mogelijke invloed van de dijk op de     grondwaterstroming te bepalen en ook om te bepalen of met stijghoogtemetingen     deze varianten zijn te valideren / uit te sluiten. 


**42\60** Eindrapportage SKB-project PT04-128 

### 9.1 Resultaten van het proces 

 Het blijkt dat het belangrijk is eerst de geohydrologische situatie goed in de vingers te hebben. Zolang dat niet het geval is, is het vaak niet efficiënt het model uit te breiden met stoftransport en afbraak. Het beeld dat bij de verschillende denktankleden aanwezig was van het gebruik van modellen is in de loop van het project gewijzigd! 

 Voor het voorspellen van transport kunnen eenvoudige als complexe modelcodes worden ingezet. Hierbij valt te denken tot eenvoudige stroombaanberekeningen tot geavanceerde stoftransportcodes met redoxafhankelijke afbraak. Veelal is een stroombaanberekening bruikbaar om relevante vragen te beantwoorden (komt de stromingsrichting van de pluim overeen met de gemeten pluim? Wat is de reistijd tot een bepaalde locatie, zodat de afbraakconstanten bepaald kunnen worden? 

 Algemeen kan worden gesteld dat een geavanceerd model ondersteund met beperkte data een schijnnauwkeurigheid suggereert. Dit kan leiden tot verkeerde conclusies. 

 Bij de furfuralverontreiniging was het doel voor de tweede brainstormsessie om te kijken of de dijk een grote invloed op de grondwaterstroming kan hebben. De hypothese was dat er een sterke voorkeurstroming ontstaat zodat op de terreingrens slechts zeer lokaal een pluim doorbreekt. Aansluitend is voor de volledigheid ook een stoftransportberekening met afbraak gedaan, maar de meerwaarde van deze berekeningen was zeer beperkt. 


 Eindrapportage SKB-project PT04-128 43\60 

## 10 Proces voor de bepaling van aanvullende 

## waarnemingen 

Uit het proces van modelleren en het kalibreren van het numerieke model komen nieuwe vragen naar boven. Een goede fit blijkt bijvoorbeeld alleen mogelijk wanneer een aantal aannames worden gedaan betreffende: 

- Geologie/geohydrologie 

- Bronlocatie en aanvangstijd van de verontreiniging. 

Deze aannames of hypothesen moeten op hun beurt weer getoetst worden. 

Het belang van toetsing van deze hypothesen wordt bepaald door het verwachtte risico van falen en de reactie van belanghebbenden (maatschappelijk kader). 

Uit het doorlopen proces voor beide cases kwam een voorkeursvolgorde voor investeringen in het verwerven van nieuwe data. Deze gegevensverzameling richtte zich op het vergaren van gegevens over drie essentiële onderdelen voor een conceptueel model en daarmee voor een stoftransport model: de geologie, de geohydrologie en het stoftransport en afbraak. In de navolgende paragraaf worden deze onderdelen besproken. 

### 10.1 Geologie 

Voor de geologie dienen allereerst historische gegevens te worden opgezocht evenals DINOen ReGIS informatie en algemene geologische en bodemeigenschappen. Daarna volgen boringen met een goede boorbeschrijving (pulsboring, handboring, gestoken monsters) en sonderingen. 

 2 de^ brainstormsessie furfuralverontreiniging: ‘’De k-waarde is op 2,5 m/dag gesteld. De ophooglaag is maximaal 4 m. Dit levert een transmissiviteit (kD) op van maximaal 10 m 2 /dag. Dit is een vrij hoge transmissiviteit welke waarschijnlijk niet overeenkomt met de werkelijkheid. Wanneer deze lager (kD-waarde 1 m/dag) wordt gebruikt, stroomt het water sneller de diepte in. Dit geeft mogelijk ook een beeld dat beter overeenkomt met de furfuralpluim.’’ 

 Er is vervolgens besloten een aantal pompproeven uit te voeren. Door problemen tijdens de uitvoering hiervan is uiteindelijk besloten de pompproeven te vervangen door slugtests. De slugtest hebben helaas in vergelijking met pompproeven een beperktere invloedstraal. Het aantal metingen is daarom groter dan het aantal als gepland voor de pompproeven. De resultaten zijn gebruikt voor het bepalen van de variatie in doorlatendheid over het terrein. 


**44\60** Eindrapportage SKB-project PT04-128 

 Deze dienen natuurlijk op de locatie zelf en indien nodig in de nabije omgeving uitgevoerd te worden om een locatiespecifiek beeld van de situatie te verkrijgen. Bij de positionering van deze boringen is het van belang om een goed locatiedekkend beeld te verkrijgen. Ook zal het aantal afgestemd moeten zijn op de lithologie en de eigenschappen van de verontreiniging. Zo zal in een groot homogeen zandpakket met een eenvoudige verontreiniging aan alleen opgeloste componenten het aantal boringen of sonderingen aanzienlijk beperkter kunnen zijn dan voor en heterogeen of gestuwd pakket waarin DNAPL-migratie mogelijk heeft opgetreden. Dit omdat voor het laatste geval de verspreiding van de verontreiniging sterk zal afhangen van de aanwezigheid van voorkeursbanen. 

 Ook kan de bodem door middel van georadar of seismiek beter in beeld gebracht worden. Het voordeel van deze technieken is dat zij een 2-dimensionaal of semi-3-dimensionaal beeld van de bodem kunnen verschaffen. De onderscheidende kwaliteit van deze metingen is minder accuraat dan dat van een boring of een sondering, maar door het vlak dat verkend wordt, kan essentiële informatie over de continuïteit van lagen en lenzen en aanwezigheid van storende lagen verkregen worden die uit verticale lijnmetingen als boringen en sondering niet gehaald kunnen worden. 

### 10.2 Geohydrologie 

 Voor de geohydrologische karakterisatie geldt als basis het (grond-)waterpeilbeheer in het modelgebied en de Grondwaterkaart van Nederland. In het veld kunnen achtereenvolgens naar voorkeur de volgende metingen worden verricht: 

- Grondwaterstanden 

- Verspreidingscontouren 

- Doorlatendheidstesten     − pompproeven     − slugtests     − zeefkrommen 

- Inschatting effectieve neerslag op basis van veldinspectie 

- Tracer-testen voor de bepaling van     − grondwaterstromingssnelheid en -richting     − ouderdomsbepaling 

 Hierbij dient opgemerkt te worden dat het peilen van een groot aantal peilbuizen op een (droge) dag veelal de voorkeur geniet. Het meerdere malen uitvoeren van dergelijke metingen is relatief beperkt qua kosten en geeft een goed inzicht in de temporele geohydrologische fluctuaties. De verspreidingscontouren op basis van de concentraties in het grondwater geven met name inzicht in de langjarig-emiddelde stromingsrichting(en) van het grondwater van de afgelopen tijd. 


 Eindrapportage SKB-project PT04-128 45\60 

Onder invloed van recente wijzigingen in de geohydrologische situatie zoals het aanof uitzetten van pompen, maatregelen die invloed hebben op de grondwateraanvulling, herstelof beschadiging van rioolsystemen. 

De doorlatendheidstesten genereren bruikbare informatie over de permeabiliteit van de bodem. De voorkeur gaat uit naar pompproeven vanwege de grotere invloedsstraal en betrouwbaarheid van de meting. Slugtesten geven indicatieve waarden rondom de peilbuis. Zeefkrommen geven slechts zeer indicatieve waarden. 

Tracertesten waarbij tracers aan het grondwater worden toegevoegd worden niet vaak toegepast vanwege de lange duur en veelal hoge kosten. Zij kunnen wel goede informatie geven over de stromingssnelheid en richting. Tracertesten voor de ouderdomsbepaling van het grondwater zijn veelal relatief beperkt qua doorlooptijd en kosten en kunnen daarnaast zeer waardevol zijn. 

### 10.3 Stoftransport en afbraak 

Voor verbetering van de modellering van het stoftransport kan achtereenvolgens het volgende bepaald worden: 

- Stofeigenschappen (oplosbaarheid, sorptiegedrag, dichtheid, toxiciteit, afbraak     parameters en -routes, dochterproducten, etc.) 

- Drijflaagbemonstering en analyse 

- Afbraakproces     − Identificatie van dochterproducten     − Isotopenonderzoek voor vaststelling van biologische omzetting     − Bepaling van aanwezigheid van benodigde micro-organismen 

- Redox omstandigheden     − Eh     − Zuurstofconcentratie     − Methaanconcentratie     − Sulfaat, Fe2+, Fe 3+, Nitraat, etc. 

- Afbraakonderzoek voor snelheidsbepalingen     − Laboratoriumtesten     − Veldmetingen 

- Adsorptieparameters 

- Dispersie en diffusieparameters 

Op basis van deze bevindingen zal het numerieke model aangepast worden en zal het conceptuele model geverifieerd en zo nodig aangepast worden. Het bepalen van het stofgedrag en de redox-condities in het veld geeft ook veel inzicht in de grondwaterstroming en bodemopbouw. 


**46\60** Eindrapportage SKB-project PT04-128 

 Zo zal verontreiniging zich niet tegen of haaks op de grondwaterstromingsrichting verplaatsen en geven Ec-waarden of redox-potentialen aan of er bijvoorbeeld een zoet-zout grensvlak is en of er bijvoorbeeld koolstofbronnen als veen in de ondergrond aanwezig zijn. 

 De interactie tussen de geohydrologische beschrijving en het stoftransport en de afbraak processen kan een verfijning van het geohydrologisch model mogelijk maken. 


 Eindrapportage SKB-project PT04-128 47\60 

## 11 Modelleringsen interpretatieprocessen van de 

## nieuwe gegevens 

Nadat er nieuwe metingen en/of nieuwe modelberekeningen zijn uitgevoerd, dient de modelleur de metingen en de modelberekeningen samen te interpreteren. Dat kan aan de hand van de volgende drie vragen 

**1 Vallen de waarnemingen binnen de onzekerheidsmarge van het model?** Indien het antwoord op deze vraag positief is, kan met behulp van het aanpassen van de modelparameters een goede fit van de metingen worden verkregen. 

Indien het antwoord op deze vraag negatief is, zijn er twee mogelijkheden: 

1. Het modelconcept moet worden bijgesteld. 

2. De onzekerheid van de modelparameters was groter dan vooraf ingeschat? 

**2 Wat vertellen de metingen en de modelvoorspellingen over het werkelijke probleem?** Het is mogelijk dat de metingen moeilijk zijn te verklaren met behulp van het model, zonder heel veel ad-hoc aannamen te doen. In sommige gevallen kan deze informatie wel worden gebruikt om de grootte van het werkelijke probleem te bepalen en is een gedetailleerd stromingmodel overbodig. Zo zou het bijvoorbeeld kunnen dat aangetoond wordt dat het veronderstelde probleem eigenlijk geen probleem is. 

 Een voorbeeld van de benzeenlocatie: Bij de benzeenverontreiniging hadden we na de 2 de^ brainstormsessies geen idee waar de werkelijke bronnen van de verontreinigingen lagen. Het uitvoeren van extra metingen om dit nader te bepalen zou zeer kostbaar zijn. Echter door het bepalen van de benzeenflux naar de haven door de berekende grondwaterfluxen te vermenigvuldigen met de gemeten concentratie bleek de vracht naar het oppervlaktewater zodanig laag, dat de probleemeigenaar en bevoegd gezag vonden dat eventuele saneringskosten niet in verhouding zouden staan tot het rendement. Het modelleren van de werkelijke relatie tussen bronzone en pluim was in dit geval niet mogelijk, maar ook niet nodig. 


**48\60** Eindrapportage SKB-project PT04-128 

 3 Hoe verkleinen we de onzekerheid van de modelvoorspelling? Indien de onzekerheid van de modelvoorspelling gemaakt was, door meerdere modelvarianten door te rekenen, kan deze onzekerheid verkleind worden door alle modelvarianten te kalibreren op de metingen. In gevallen waar geen expliciete berekening van de modelonzekerheden is uitgevoerd, dient dit model ook gekalibreerd te worden op de metingen. Een expliciete maat voor de grootte van de onzekerheid is dan niet voor handen, maar de mate waarin het model de relevante processen goed beschrijft, geeft een indicatie hoe betrouwbaar het model is. In dit geval dient de modelleur zich af te vragen of de metingen voldoende eenduidige informatie geven over de processen die bepalend zijn voor het probleem dat hij onderzoekt. 

 Indien bijvoorbeeld metingen een goed beeld geven van de afname van concentratie stroomafwaarts door natuurlijke afbraak (bijvoorbeeld door het ontstaan van afbraakproducten of een verschuiving in de isotopenverhouding), zal het model (dat goed gefit is) een betrouwbaar beeld geven voor de afname van de concentraties stroomafwaarts. Het is goed mogelijk dat het model de verontreinigingsflux niet goed weergeeft doordat de grondwatersnelheid onzeker is. De modelleur weet dan de betrouwbaarheid van het model voor de afname van de concentratie stroomafwaarts groot is, maar dat de betrouwbaarheid wat betreft de verontreinigingsflux minder groot is. 


 Eindrapportage SKB-project PT04-128 49\60 

## 12 Bruikbaarheid van voorspellende waarde 

Op basis van de modelresultaten worden veelal beslissingen genomen ten aanzien van de verontreiniging: wel of niet saneren en zo ja, op wat voor manier en waar richten de maatregelen zich op (de bron, de pluim, isolatie etc. etc.). Als het goed is, is het mogelijk om aan de hand van het model te voorspellen wat zal geschieden in verschillende scenario's. De waarde van deze voorspellingen dienen, gezien de grote (financiële) effecten die zij kunnen hebben, goed in beeld gebracht te zijn. 

Algemeen kan gesteld worden dat van de voorspellende waarde afhankelijk is van de kwaliteit van het proces dat doorlopen is. De belangrijkste uitgangspunten en randvoorwaarden zijn het vooraf helder formuleren van het doel van de modellering en de hypotheses ten aanzien van de processen bij het opstellen van conceptuele model. Een belangrijk criterium ten aanzien van de bruikbaarheid van het model en daarmee de voorspellende waarde is de mate waarin het model de huidige situatie kan verklaren. Hierbij dient bijvoorbeeld de huidige verontreinigingscontour verklaart te kunnen worden op basis van een verontreiniging ten tijde van haar ontstaan en de met het model berekende verspreiding. 

Om het model met de huidige situatie te kunnen vergelijken is het natuurlijk noodzakelijk dat er voldoende gegevens over de huidige situatie beschikbaar zijn. Hierbij dient natuurlijk gedacht te worden aan de stijghoogten, concentratiemetingen. 

Ook de gevoeligheid van het model dient voor zover dat noodzakelijk is geverifieerd te worden. Als vele aannamen noodzakelijk zijn geweest, dient inzichtelijk te zijn wat de impact hiervan is op de mogelijke uitkomsten van de modellering. 

Om na te gaan of het numerieke model een voldoende bruikbaar resultaat heeft opgeleverd kan worden nagegaan wat de waarde is die de betrokken partijen hieraan hechten. Een van de voorbeelden hiervan is de beperking aan monitoringsinspanningen die worden toegestaan door bijvoorbeeld het bevoegd gezag of de terreinbeheerder omdat op basis van het model de ontwikkelingen van de verspreidingsrisico's van de verontreiniging helder gemaakt zijn. Indien een partij hier onvoldoende vertrouwen in heeft zal de monitoring door middel van grondwatermonstername en analyses noodzakelijker geacht worden. 

Ook is het zeer wel mogelijk dat bij een betrouwbaar model er tijdens de sanering minder monitoring noodzakelijk geacht worden om de voortgang te controleren. Een verbeterd beeld van het verspreidingsgedrag leidt tot een meer gerichte, en dus effectievere, monitoring. 


**50\60** Eindrapportage SKB-project PT04-128 

 Voor het bevoegde gezag ligt het ten grondslag aan de mogelijkheid de monitoringinspanning te reduceren. Voor saneerders kan het model worden gebruikt om de loop van een sanering te duiden en eventuele additionele metingen te baseren op het model. 

 Bruikbaarheid van de voorspellende waarde tijdens het project 

 Het is lastig hier eenduidige conclusies te trekken. In beide doorlopen cases bleek het lastig de geohydrologie en de verspreiding van de verontreiniging voldoende in de vingers te krijgen. 

 Voor de benzeenlocatie was de voorspellende waarde ondanks de relatief beperkte nauwkeurigheid van het model zeer bruikbaar. Ondanks dat met het model de herkomst van de huidige verontreinigingssituatie niet kon worden beschreven, wat het model betrouwbaar genoeg om te kunnen voorspellen wat, binnen acceptabele marges, de te verwachten flux aan opgeloste verontreiniging is dat zich via de tussen-zand-laag de terreingrens passeert. Op basis van deze voorspelling gaf het bevoegd gezag voor het oppervlaktewater aan in dit specifieke geval hiermee geen problemen te hebben met natuurlijke lozing op oppervlaktewater en derhalve geen actieve maatregelen te vereisen. Op basis hiervan en de ligging zeer nabij het oppervlaktewater werd het ook voor het bevoegd gezag in het kader van de Wbb niet noodzakelijk geacht sanerende maatregelen vanuit de Wbb te verlangen. Hierdoor konden actieve saneringsmaatregelen onderbouwd achterwegen gelaten worden. 

 Voor de furfurallocatie is het geohydrologische beeld gedurende het project sterk veranderd. Nieuwe metingen die het conceptuele beeld onderbouwen zijn nog niet uitgevoerd en zullen in het kader van dit project niet meer worden uitgevoerd. Echter, het was wel mogelijk bepaalde maatschappelijke vragen voldoende te beantwoorden en daarnaast leverde de modelleersessie nieuwe inzichten op. Als gevolg van de modelleersessie zal de focus nu op de diepere ondergrond gericht zijn, omdat is gebleken dat het merendeel van het freatisch grondwater in verticale richting via de tussenzandlaag en het watervoerend pakket het terrein verlaat. 


 Eindrapportage SKB-project PT04-128 51\60 

## 13 Werkhandleiding Modelleer activiteiten 

### 13.1 Het proces per Wbb-fase 

Voor elke fase die voor een verontreinigingsgeval wordt doorlopen in het kader van de Wbb, kan een vergelijkbaar proces doorlopen worden om tot een voor die fase gewenst resultaat te komen. In het project Voorspel je Verontreiniging! werd het proces doorlopen voor de Wbb-karakterisatiefase doorlopen voor de Furfural-locatie en, zij het heel snel, werden voor de Benzeen-locatiede de Wbb-karakterisatie-, Wbb-ernst&urgente en Wbb-SO-fase doorlopen. 

De beschrijving van de verschillende processtappen die al dan niet cyclisch doorlopen worden zijn weergegeven in de onderstaande figuur. De modelleerwerkzaamheden die doorlopen moeten worden voor elk van deze stappen zijn in de voorgaande hoofdstukken behandeld. 

Wat de doelstelling is van elk van de Wbb-fases is beschreven in hoofdstuk 2. Welk doel de modelleerwerkzaamheden in elk van deze fases kan hebben, wat de benodigde informatie is voor het modelleren van de situatie en wat de mogelijke resultaten van de modelleerwerkzaamheden zijn wordt in paragrafen 13.2 tot 13.7 beschreven. 


**52\60** Eindrapportage SKB-project PT04-128 

 Probleem identificatie/ identificatie maatschappelijk kader 

 Conceptueel model 

 Model toetsen aan de hand van additionele waarnemingen 

 Beschikbare data 

 Numeriek/analytisch model 

 Aanpassen conceptuele model totdat numerieke model en data overeenstemmen 

 model is in staat huidige situatie te beschrijven en voorspellingen dusdanig te doen dat ze voldoen aan de eisen van alle betrokkenen bij het project (eindgebruiker, bevoegde gezagen, etc. ) 


 Eindrapportage SKB-project PT04-128 53\60 

### 13.2 Afperking van de verontreiniging 

**13.2.1 Doel van de inzet van het model** In deze fase is het doel van het model om te komen tot een efficiënte monstername om het verontreinigingsprobleem nader te karakteriseren. 

In de beginfase van het onderzoek, als er slechts een eerste gedachte ten aanzien van de verontreinigingsituatie is, is de inzet van een numeriek model niet efficiënt en zal het conceptuele model in de vorm van een schematisatie praktischer zijn. Met behulp van het model wordt het mogelijk inzicht te krijgen waar te meten. In de loop van deze fase zal meer informatie beschikbaar komen over de verschillende elementen in de ondergrond (bodemgesteldheid, geohydrologie en verontreinigingssituatie). Indien voldoende informatie beschikbaar is, kan een numeriek model opgesteld worden om deze informatie beter te kunnen ontsluiten. 

**13.2.2 Benodigde informatie en mogelijke veldwerkzaamheden** De benodigde informatie bestaat uit gegevens die iets zeggen over: 

- De stromingsrichting van de pluim in horizontale en verticale richting, zoals de     bodemopbouw, stijghoogtemetingen, doorlatendheden (zowel horizontaal als     verticaal), onttrekkingsgegevens, drainagegegevens. 

- De mogelijke ligging en kenmerken van de bron(nen): Is de bron puur     product?, zo ja is het een LNAPL of een DNAPL? 

**13.2.3 Mogelijke resultaten** Het resultaat van het model is in deze fase een karakterisatie/afperkingstrategie die onderbouwd is door inzicht over het gedrag van de pluim, zoals de stromingsrichting en de ligging van de bronzones. 

Zo kan op basis van een numerieke model worden bepaald waar, welke aanvullende gegevens hiaten in het conceptuele model het meest efficiënt kunnen aanvullen. Hierbij kan gedacht worden aan de locaties voor boringen, peilbuizen (en concentratiebepalingen van gronden grondwatermonsters). Ook kan bijvoorbeeld gedacht worden aan locaties voor doorlatenheidstesten voor kD-waarde bepaling en het uitvoeren van georadar voor het in beeld brengen van de laterale continuïteit van bodemlagen om de heterogeniteit van de bodemlagen te bepalen. 

De verkregen informatie zal weer verwerkt worden in het conceptuele en numerieke model, waardoor een verbeterd inzicht van de situatie zal worden bewerkstelligd. 


**54\60** Eindrapportage SKB-project PT04-128 

### 13.3 Bepaling van ernst en urgentie 

 13.3.1 Doel van de inzet van het model Met het model zullen in deze fase de verspreidingsrisico’s worden berekend. Mogelijk kan in deze fase een eenvoudig analytisch model al toereikend zijn. 

 13.3.2 Benodigde informatie en mogelijke veldwerkzaamheden De benodigde informatie bestaat uit gegevens die iets zeggen over: 

- De grondwaterstroomsnelheid, zoals het hydraulische verhang en de     doorlatendheden, inclusief allerlei verstoringen hierin, zoals bijvoorbeeld     zandpalen. 

- De adsorptie van de verontreiniging aan de bodem, zoals het organische     stofgehalte voor organische verontreinigingen en de cation exchange capacity     en samenstelling van het grondwater voor zware metalen en de adsorptie     gerelateerde stofeigenschappen van de verontreiniging zoals het octanol-     water getal. 

- De afbraak van de verontreiniging, zoals de redoxomstandigheden en     informatie over de afbraaksnelheid van de verontreiniging. Voor de laatste twee aspecten geldt dat deze informatie alleen nodig is indien de processen adsorptie en/of afbraak als relevant worden beschouwd en niet vooraf duidelijk is dat deze processen een verwaarloosbare invloed hebben op de verspreiding van de verontreiniging. 

 13.3.3 Mogelijke resultaten De resultaten van het model zijn in deze fase: 

- Voorspelling van de groei van de omvang van de verontreiniging bij voorkeur     inclusief onzekerheidsmarges. 

- Indien nog niet genoeg informatie voor handen is, kan een meetstrategie om     de relevante resterende informatie in handen te krijgen worden opgesteld. Met     het model kan dan worden bepaald welke metingen onderscheidende     informatie bevatten om de benodigde gegevens af te leiden. 

### 13.4 Uitvoeren van een saneringsonderzoek 

 13.4.1 Doel van de inzet van het numerieke model In deze fase zal het numerieke model gebruikt worden om de effecten van de verschillende saneringsvarianten door te rekenen of deze varianten zelfs te dimensioneren. Daarnaast zal ook een afweging gemaakt moeten worden (bijvoorbeeld conform ROSA) over welke trede op de saneringsladder gekozen kan worden met welke maatregel of combinatie van maatregelen. 


 Eindrapportage SKB-project PT04-128 55\60 

Afhankelijk van de verontreinigingsituatie en de saneringsmogelijkheden zal een onderbouwde keuzen van de mogelijk haalbare trede op de saneringsladder (BEVER) gemaakt moeten worden. Hiervoor zal in deze en ook in de volgende fases veelal een numeriek model nodig zijn. 

Een andere vorm dat de gebruikelijke numerieke modellen zijn de zogenaamde _screening tools_. _Screening tools_ zijn eenvoudig numerieke modellen, veelal _spread sheets_ waarmee met beperkte invoergegevens op hoofdlijnen een eerste indruk van de bepaald proces kan worden verkregen. Als op basis van een dergelijke _screening_ de mogelijkheid lijkt te bestaan dat de techniek of het proces op zou kunnen treden, kan overwogen worden dit nader te onderzoeken met een gedegen modellering. _Screening tools_ zijn uitdrukkelijk niet geschikt om gebruikt te worden om voorspellingen mee te doen of om ontwerpen nader vorm te geven of budgetten te ramen. 

Het toepassen van _screening tools_ in de fases dat nog onvoldoende kennis aanwezig is om een gedegen numeriek model op te zetten is wel mogelijk. Bij het gebruik van _screening tools_ dient de significante beperkingen van deze _tools_ altijd zeer goed aangegeven te worden. 

**13.4.2 Benodigde informatie en mogelijke veldwerkzaamheden** De benodigde gegevens hangen in dit geval nauw samen met de gekozen saneringsvarianten. Alle locatiespecifieke invloeden op de processen die in de saneringsvarianten een rol spelen moeten worden gekarakteriseerd. Een voorbeeld hierbij is de aanwezigheid van redoxcomponenten in de bodem en het grondwater indien gestimuleerde afbraak een saneringsvariant is. De mate van benodigd detail van deze gegevens moet worden afgestemd om de juiste keuze te kunnen maken tijdens de afweging van de saneringsvarianten. 

**13.4.3 Mogelijke resultaten** De resultaten van het model in deze fase zijn: 

- Een voorspelling van het gedrag van de verontreiniging tijdens de     saneringsvarianten. 

- Dimensionering van de verschillende saneringsvarianten. 

- De faalkansen van de verschillende saneringsvarianten. 

- Overige effecten van de saneringsvarianten die van invloed zijn op de     afweging van de saneringsvarianten, zoals bijvoorbeeld     grondwaterstandsverlagingen, zettingen. 


**56\60** Eindrapportage SKB-project PT04-128 

### 13.5 Het opstellen van het saneringsplan 

 13.5.1 Doel van de inzet van het numerieke model Het doorrekenen, ontwerpen en optimaliseren van de gekozen saneringsvariant en het optimaliseren van de monitoring tijdens de sanering. Hierbij is het in veel gevallen ook noodzakelijk om de stabiliteit van de grondwaterverontreinigingspluim aan te tonen en hiervoor een meetprotocol op te stellen. Een numeriek grondwaterstromingsmodel kan daarbij helpen. 

 13.5.2 Benodigde informatie en mogelijke veldwerkzaamheden De benodigde informatie hangt hier uiteraard sterk af van de gekozen saneringsvariant. Het is goed mogelijk dat de benodigde gegevens voor een optimaal ontwerp pas te achterhalen zijn op het moment dat een sanering wordt uitgevoerd. In dat geval is het wenselijk om tijdens de uitvoering van de sanering het ontwerp bij te kunnen stellen of om als onderdeel van de sanering een veld-pilot uit te voeren. Deze pilot dient gedimensioneerd, gemonitord en geëvalueerd te worden. Vervolgens worden de resultaten gebruikt om een full-scale ontwerp te dimensioneren. 

 Verder kunnen aanvullende metingen als doorlatendheden, pompproeven gebruikt worden voor het verfijnen van het conceptueel beeld en daarmee een betere dimensionering mogelijk te maken. 

 13.5.3 Mogelijke resultaten De resultaten van het numerieke model in deze fase zijn: 

- Een voorspelling van het gedrag van de verontreiniging tijdens de gekozen     saneringsvariant. 

- Optimalisatie van de gekozen saneringsvariant. 

- Het ontwerp van de pilot en de calibratie/validatie van de pilot met de     monitoringsgegevens. 

- De faalkansen en –mechanismen van de gekozen saneringsvariant. 

- Een efficiënte monitoringsstrategie om de werking van de saneringsvariant     aan te tonen of faalmechanismen tijdig te ontdekken. 

### 13.6 Het uitvoeren van de sanering 

 13.6.1 Doel van de inzet van het numerieke model Het numerieke model kan worden ingezet om de veldwaarnemingen voortkomend uit de monitoring van de saneringsvariant te verklaren en om op afwijkingen van de voorspelling gepast te kunnen reageren en indien noodzakelijk bij te sturen. Ook kan het model goed gebruikt worden voor het opvolgen van de saneringswerkzaamheden. Hierbij kan gedacht worden aan peilverlagingen, veranderingen (hopelijk afname) van concentraties, grondwaterstromingssnelheden en wijzigingen in bijvoorbeeld redox-condities. 


 Eindrapportage SKB-project PT04-128 57\60 

Daarnaast kan het model ook gebruikt worden om na te gaan of externe effecten van de sanering, zoals peilverlaging volgens verwachting verlopen en eventueel om te bepalen welke aanvullende maatregelen mogelijk zijn om deze effecten te verkleinen. 

**13.6.2 Benodigde informatie en mogelijke veldwerkzaamheden** De benodigde informatie bestaat uit gegevens die het proces van de saneringsvariant direct of indirect beschrijven, zoals concentratieveranderingen van de verontreiniging, concentratieverloop van het opgepompte grondwater, concentraties van afbraakproducten bij gestimuleerde afbraak, temperatuur bij stoominjectie, etc. 

Ook is informatie over externe effecten van de sanering zoals peilverlagingen in de omgeving en informatie of mogelijke faalmechanismen van de sanering van belang. 

**13.6.3 Mogelijke resultaten** De resultaten van het model in deze fase zijn: 

- De validatie dat de sanering volgens planning verloopt of niet. 

- Bijsturing van de sanering op basis van de nieuwe gegevens en calibratie van     het model. 

- Het dimensioneren van extra inspanning om ongewenste externe effecten     tegen te gaan. 

### 13.7 Het uitvoeren van de nazorg 

**13.7.1 Doel van de inzet van het numerieke model** Het controleren of de metingen tijdens de nazorg volgens verwachting zijn of dat de voorspelling van de situatie na afloop van de sanering aanpassing behoeft en eventueel het aanpassen van de monitoringsstrategie tijdens de nazorg. 

**13.7.2 Benodigde informatie en mogelijke veldwerkzaamheden** De benodigde informatie bestaat hier uit de monitoringsdata tijdens de nazorg. Dit zal veelal de periodieke bemonstering van de verontreinigingsconcentraties en grondwaterstanden zijn. 

**13.7.3 Mogelijke resultaten** De resultaten van het model in deze fase zijn: 

- De validatie of de sanering de gewenste doelen behaald heeft. 

- Een gekalibreerd model op basis van de monitoring van de nazorg en     aangepaste voorspellingen over de te verwachten verspreiding van de     restverontreiniging. Een onderbouwd ontwerp voor de aanpassing van de monitoring tijdens de nazorg. 


**58\60** Eindrapportage SKB-project PT04-128 


 Eindrapportage SKB-project PT04-128 59\60 

## 14 Conclusies en Aanbevelingen 

Het gebruik van modellen is nuttig tijdens alle fasen van de Wbb. In de karakterisatiefase zal veelal een eenvoudig conceptueel model volstaan. In de loop van het onderzoek zal meer data bekend worden en zal het model veel gedetailleerder worden en zal er veelal een numeriek model toegepast worden. De mate van detail van het model moet worden afgestemd aan de vraagstelling, de wensen van de verschillende stakeholders en de hoeveelheid aanwezige data. 

Indien er te weinig data aanwezig is om een betrouwbaar model te maken, dienen er extra metingen te worden uitgevoerd. Om deze metingen te optimaliseren is model ook nuttig. Gedacht kan dan worden aan een conceptueel model voor een eerste indruk of aan een numeriek model om op basis van een meer gedetailleerd beeld aanvullende metingen uit te voeren. Als voorbeeld kunnen modellen die gebaseerd zijn op verschillende hypothesen, met een numeriek model worden doorberekend en kunnen daarmee metingen geselecteerd worden die onderscheidend zijn voor de verschillende hypothesen. 

In een verspreidingsituatie dienen eerst de geologie en geohydrologie goed in kaart te worden gebracht. Pas als deze goed bekend is en de stromingsrichting van de pluim (zowel in horizontale als verticale richting) vastligt, kan een stoftransportmodel worden gebouwd en metingen voor bijvoorbeeld afbraak gericht worden uitgevoerd. Het toepassen van screening tools in de fases dat nog onvoldoende kennis aanwezig is om een gedegen numeriek model op te zetten is wel mogelijk. Bij het gebruik van screening tools dient de significante beperkingen van deze tools altijd zeer goed aangegeven te worden. 

Voor de beoordeling van de noodzaak van maatregelen en de het maken van de keuze voor saneringsmaatregelen op basis van de saneringsladder is een kwantitatieve beoordeling noodzakelijk en daarom is het toepassen van een numeriek model in veel gevallen vrijwel noodzakelijk. 

Alle mogelijke invloeden op de verontreinigingssituatie dienen in kaart te worden gebracht en te worden geselecteerd op de invloed op de verspreiding van de verontreiniging. Een snelle inschatting van het belang van de verschillende invloeden is hiervoor een voorwaarde. Dit kan deels door inzicht en deels door het doorrekenen van verschillende modelhypothesen. Dit kan door gebruik te maken van de expertise van senior modelleurs/ adviseurs. 


**60\60** Eindrapportage SKB-project PT04-128 

 Er zijn vele meetmethoden en modellen beschikbaar om het verspreidingsgedrag van verontreiniging in kaart te brengen. Echter, uit het doorlopen proces voor de twee geselecteerde cases blijkt het nog steeds lastig om de grondwaterstroming en het stoftransport en reactief gedrag goed in de vingers te krijgen. De cyclus meten-modelleren-aanpassen conceptueel model geeft wel een goed handvat om dit in de praktijk te doen. 


