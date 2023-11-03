##    

##      

###### Deelresultaat 1 

###### Fase 1: Verkenningsen definitiefase 

###### SKB project: PP5304 

 (^) Versie 3  Opdrachtgever 

######  

 Gemeentewerken Rotterdam 9 juni 2006 


####    

**Titel** : R&B Rekenmodel 

 Nazorgkosten Bodemsanering 

**Projectnummer** : SKB project: PP5304 

**Documentnummer** : 

**Revisie** : Versie – 3 

**Datum** : 9 juni 2006 

**Auteur(s)** : drs. R.P. (Rob) Heijer Grontmij 

 Ing. C.A. (Kees) de Vette Ingenieursbureau Gemeentewerken Rotterdam F. (Floris) de Jong Validware 

**e-mail adres** : rob.heijer@grontmij.nl 

 ca.devette@gw.rotterdam.nl info@validware.com 

**Gecontroleerd** : Ir. J. M. P. (Joost) Martens Gemeentewerken Rotterdam / Beheer Buitenruimte 

**Paraaf gecontroleerd** : 

**Goedgekeurd** : 

**Paraaf goedgekeurd** : 

**Contact** : Ir. J. M. P. (Joost) Martens Gemeentewerken Rotterdam / Beheer Buitenruimte jmp.martens@gw.rotterdam.nl 


 

###     

1 Inleiding............................................................................................5 1.1 Algemeen .........................................................................................5 1.2 Doelstelling SKB-project ................................................................5 1.3 Fasering project................................................................................6 1.4 Inhoud en doelstelling van deze rapportage / leeswijzer...............6 

2 Wat doen we al? – De praktijk........................................................8 2.1 Inleiding............................................................................................8 2.2 Spreadsheetramingen nazorgkosten ...............................................8 2.3 RINAS (“IPO-model”) ....................................................................9 2.4 Risicomodel bij RINAS.................................................................11 2.5 ‘Quick scan’-methode risico’s ......................................................13 2.6 Samenvatting en analyse van de resultaten..................................15 

3 Wat doen we al? Andere ontwikkelingen in werkveld .............16 3.1 Inleiding..........................................................................................16 3.2 IPO-studie “Borgingsmogelijkheden nazorg bodemsanering”...16 3.3 ‘Rekenmodel’ Landsdekkend beeld .............................................17 3.4 Flexibele Emissie Beheersing (FEB)............................................18 3.5 QRA (Quantitative Risk Analyses) ..............................................19 3.6 Case Base Reasoning (CBR).........................................................20 3.7 Risman methode ............................................................................20 3.8 Medische sector .............................................................................26 3.9 Samenvatting en analyse van de resultaten..................................26 

4 Wat moet? – Wettelijke eisen en eisen door derden....................27 4.1 Inleiding..........................................................................................27 4.2 Landelijk en provinciaal beleid.....................................................27 4.3 Bedrijvenregeling ..........................................................................29 4.4 Verzekeraars...................................................................................30 4.5 Nazorgorganisaties ........................................................................30 4.6 Samenvatting van de resultaten ....................................................31 

5 Wat willen we? – Ontwerpwensen ...............................................32 5.1 Inleiding..........................................................................................32 5.2 Resultaten workshops....................................................................32 5.2.1 Workshop 1 ....................................................................................32 5.2.2 Workshop 2 ....................................................................................33 5.3 Enquete t.b.v. bepalen grootste discussiepunten..........................34 

6 “Wat gaan we bouwen?” – Definitiefase ...............................36 6.1 Inleiding..........................................................................................36 6.1.1 Algemeen .......................................................................................36 6.1.2 Werkwijze bouwfase .....................................................................36 6.1.3 Kosten realisatie programma van eisen........................................37 6.2 Functionele kenmerken .................................................................37 6.2.1 Algemeen .......................................................................................37 


 

6.2.2 Beheren gegevens ..........................................................................38 6.2.3 Basiskengetallen _(functionele eis 2, bijlage 1)_ ............................39 6.2.4 Prijspeilen _(eis 4, bijlage 1)_ ..........................................................42 6.2.5 Berekening doelvermogen ............................................................43 6.2.6 Berekening jaarbegroting ..............................................................43 6.2.7 Rapportages _(eis 9, bijlage 1)_ .......................................................44 6.2.8 Berekening gevoeligheidsanalyse _(eis 3, bijlage 1)_ ....................45 _6.2.9_ Vergelijkingen van ramingen _(eis 8, bijlage 1)_ ...........................46 6.2.10 Invoer risico ...................................................................................46 6.2.11 Export/import van ramingen _(eis 10, bijlage 1)_ ...........................46 6.2.12 Back-upfunctionaliteit ...................................................................46 6.2.13 Beheer ramingen ............................................................................46 6.2.14 Updatefunctionaliteit _(eis 11, bijlage 1)_ .......................................46 6.3 Technische kenmerken ..................................................................47 6.3.1 Programmeertaal............................................................................47 6.3.2 Technische architectuur.................................................................47 6.3.3 Relationele database ......................................................................49 6.3.4 Setupkit...........................................................................................49 6.3.5 Supportwebsite _(eis 11, bijlage 1)_ ................................................49 

7 “Wat moet verder nog gedaan worden?” .....................................51 


###     

**1.1 Algemeen** Als gevolg van het nieuwe bodembeleid (BEVER, Beleidsbrief Bodem, e.d.) blijven verontreinigingen langer in de bodem en blijven er na sanering meer restverontreinigingen in de bodem achter. De omvang van de (na)zorgtaak neemt de komende jaren hierdoor aanzienlijk toe. In de nieuwe Wbb is de nazorg wettelijk beter verankerd. Veel bevoegde gezagen en grote particulier saneerders zijn momenteel bezig zich te bezinnen hoe in bredere zin om te gaan met nazorg. 

Een vaak terugkomend knelpunt bij nazorg is de behoefte aan goede ramingen van de kosten en mogelijke financiële risico’s. Er bestaat op dit moment geen gestandaardiseerde en breed gedragen methode voor het bepalen en kwantificeren van de (na)zorgkosten en -risico’s van bodemsaneringen. Wel zijn er op ad hoc basis verschillende modellen (veelal voor eigen gebruik en deels ook voor andere typen nazorg) ontwikkeld, ieder met zijn eigen methode, opzet en specifieke doelstelling én specifieke manco’s. 

Het ontbreken van een goed en breed gedragen model voor kosten en risico’s leidt tot onjuiste en niet eenduidige inschattingen (zowel te laag als te hoog) van en discussies over de nazorgkosten. De gevolgen voor de praktijk kunnen zijn: in de afwegingsfase van het saneringsproces wordt een verkeerde variant gekozen, moeizame overnametrajecten van nazorglocaties doordat onzekerheden worden vertaald in (wellicht té) hoge premies, problemen bij het budgetteren van exploitatiekosten en stagnatie bij projecten / ontwikkelingen. Kortom; met een standaard rekenmodel kan een belangrijke slag worden geslagen bij de borging van de continuïteit en kwaliteit van nazorg van bodemsaneringen. 

**1.2 Doelstelling SKB-project** De doelstelling van dit SKB-project is een breed gedragen en vrij beschikbaar rekenmodel voor de nazorgkosten van bodemsaneringslocaties te maken. Met het rekenmodel kan een goede financiële basis voor nazorg worden gelegd en kunnen processen rondom bodemkwaliteit verder worden geoptimaliseerd. 

Vóórdat een dergelijk model kan worden opgesteld dient eerst een verkenning te worden uitgevoerd van de uitgangspunten en gewenste functionaliteiten van het model. Hierbij wordt niet alleen een overzicht gegenereerd 


van punten waarover consensus is maar ook van discussiepunten, oplossingsrichten en keuzen daarin voor deze discussiepunten en achtergronden van deze keuzen. De voorstudie resulteert daarmee in een overzicht van de ‘omgeving’ en het proces waar het rekenmodel zijn functie moet gaan vervullen. 

**1.3 Fasering project** Het project is gestart met een verkenning van en discussie over de uitgangspunten en functionaliteit van het te bouwen rekenmodel. Het streven is dat alle betrokken partijen zich hierin kunnen vinden. De weg ernaar toe is bepalend voor het draagvlak van het model. Met deze aanpak wordt de basis aan het begin van dit project gelegd in de eerste projectfase. Deze aanpak houdt ook in dat de invulling van de concrete activiteiten vooral voor de eerste projectfase kan plaatsvinden. De invulling van de latere fasen is afhankelijk van de resultaten van de eerste fase. In de tweede fase van het project wordt het rekenmodel gebouwd en getest. De derde fase is de verankeringsfase. Daarna start de beheerfase. 

Onderstaand is de fasering van het project zoals dat tot nu toe is uitgevoerd weergegeven. 

_Verkenningsfase_ : welke onderdelen van de kostenonderbouwing van nazorg zijn nu niet goed geregeld. Door middel van een enquête is bij alle consortiumleden en expertpanel gevraagd waar zij knelpunten ervaren. In bijlage 1 zijn de uitkomsten van de enquête in samengevatte vorm weergegeven. 

_Definitiefase_ : Door middel van twee workshops is in samenspraak met de consortiumleden de functionaliteit van het rekenmodel voor de nazorkosten vastgesteld. In hoofdstuk 5 staat in hoofdlijnen beschreven wat de uitkomsten zijn en in bijlage 2 is meer in detail weergegegeven wat de knelpunten zijn. Deze zijn door middel van een tweede enquête geïnventariseerd en naast de workshopresultaten gelegd. 

**1.4 Inhoud en doelstelling van deze rapportage / leeswijzer** In deze rapportage worden de resultaten van de eerste fase gepresenteerd. Deze bestaan uit:  _Wat doen we al?_ Inventarisatie van beschikbare basisinformatie: o De huidige praktijk van nazorgkosten ramen (hoofdstuk 2) o Raakvlakken met andere ontwikkelingen in het werkveld en andere werkvelden (hoofdstuk 3) De belangrijkste doelstelling van deze onderdelen is op een bewuste wijze gebruik te maken van beschikbare ervaring. 

 _Wat moet?_ – Wettelijke eisen en eisen door derden (hoofdstuk 4) De doelstelling van dit onderdeel is in beeld te brengen aan welke eisen het model moet voldoen.  _Wat willen we?_ – Ontwerpwensen en –eisen (hoofdstuk 5) De doelstelling van dit onderdeel is in beeld te brengen welke wensen de gebruikers hebben ten aanzien van functionaliteiten en mogelijkhe


den van het model. De resultaten van de twee workshops vormen voor deze paragraaf het uitgangspunt.  _Wat gaan we bouwen?_ – Definitiefase (hoofdstuk 6) De doelstelling van dit onderdeel is de resultaten van de voorgaande onderdelen te vertalen naar een concreet voorstel voor een te bouwen model.  _Wat moet er verder nog gedaan worden?_ – (hoofdstuk 7) Aangegeven wordt wat er naast de bouw van het model nog verder moet gebeuren. 


###       !" 

**2.1 Inleiding** In dit hoofdstuk wordt een inventarisatie gegeven van beschikbare informatie – toegespitst op de huidige praktijk van het ramen van nazorgkosten. Het betreft de resultaten van een ‘quick scan’. De inventarisatie beoogt daarmee niet compleet te zijn, maar een doorsnede van de huidige praktijk weer te geven met daarin de belangrijkste componenten. 

De belangrijkste doelstelling hiervan is op een bewuste wijze gebruik te maken van beschikbare ervaring. Per onderdeel komt het volgende aan bod: A. Omschrijving inhoud B. Reikwijdte C. Ervaringen en knelpunten bij gebruikers D. Bruikbaarheid voor rekenmodel E. Conclusies 

**2.2 Spreadsheetramingen nazorgkosten** 

_A. Omschrijving inhoud_ Bij ramingen van nazorgkosten wordt veel gebruik gemaakt van spreadsheets. Een spreadsheet is een ‘containerbegrip’ voor een veelvoud aan oplossingen die ‘digitaal zijn gemaakt’. De oplossingen die denkbaar zijn lopen uiteen van een ad-hoc opgestelde rekenstaat tot een gestandaardiseerd rekenmodel. 

_B. Reikwijdte_ De gebruikers hebben de mogelijkheid de raming naar eigen inzicht aan te passen en aan te vullen. Dat houdt in dat de spreadsheetramingen geen beperkingen hebben qua toepassingsgebied. Verschillende gebruikers hebben voor specifieke vraagstellingen eigen rekentools gebouwd en deze aan de spreadsheet gehangen. Denk hierbij aan overzichten van nazorgkosten per jaar uitgesplitst. 

_C. Ervaringen en knelpunten bij gebruikers_ Het belangrijkste knelpunt van een spreadsheetraming is gelijk ook zijn sterke kant: flexibiliteit. Door de (te) grote flexibiliteit is in te spelen op iedere situatie maar is het standaardiseren lastig en het garanderen van een standaardkwaliteit in de loop van de tijd en voor meerdere locaties een aandachtspunt. Door de flexibiliteit is een fout snel gemaakt en is het lastig aanpassingen adequaat en betrouwbaar te implementeren (vooral bij meerdere locaties). 


Voorts blijken in nazorgramingen bepaalde keuzen (denk aan levensduur voorzieningen, r/i-cijfer etc.) op meerdere plaatsen in de berekening terug te komen. Bij gebruikers is behoefte om gevolgen van dergelijke keuzen te beschouwen (gevoeligheidsanalyse). Dit vergt een gedegen en valide opzet van de spreadsheet zodat veranderingen in invoerparameters eenvoudig zijn te implementeren en rekenkundige resultaten in alle daaraan gerelateerde kostenposten op een juiste wijze worden doorgevoerd. Door de flexibiliteit is de neiging groot de raming voor iedere situatie of naar eigen wens aan te passen. Het is daarom niet goed mogelijk uniformiteit en kwaliteit te borgen. Veranderingen in inzicht in hoe een rekenmodel dient te worden opgesteld kan met nieuwe ervaringen veranderen. Aanpassingen van het model zijn echter niet altijd even snel door te voeren. Voorts kunnen verandering op verandering – indien deze niet professioneel worden geïmplementeerd – gevolgen hebben voor de betrouwbaarheid van het model. Dit geldt zeker indien deze veranderingen bij meerdere locaties worden doorgevoerd. 

_D. Bruikbaarheid voor rekenmodel_ Niet zozeer de spreadsheets zelf maar de filosofie achter de inhoud en opzet is van belang voor deze studie. Voor het opzetten van het rekenmodel (onderverdeling, wijze van rapporteren etc.) kan dan ook gebruik worden gemaakt van meerdere voorbeelden. Flexibiliteit wordt veelal gewaardeerd. Een aandachtspunt is de wijze waarop kwaliteit en uniformiteit kan worden geborgd. 

_E. Conclusies_ 

1. Spreadsheetramingen geven een praktische input voor de opzet van het     model 

2. Spreadsheetramingen zijn gezien de te grote mate van flexibiliteit min-     der geschikt om als standaard instrument te hanteren. 

3. Te grote flexibiliteit leidt tot inefficiëntie en verhoogde kans op kwali-     teitsverlies. 

**2.3 RINAS (“IPO-model”)** 

_A. Omschrijving inhoud_ Bij Koninklijk Besluit is op 1 april 1998 de Nazorgregeling van de Wet Milieubeheer in werking getreden voor stortplaatsen waar op of na 1 september 1996 afval is gestort. Op grond van deze wettelijke regeling dienen stortplaatsexploitanten een nazorgplan aan de provincie ter goedkeuring voor te leggen. Provincies worden verantwoordelijk voor de nazorg van deze stortplaatsen. Het IPO heeft voor de uitvoering van bovengenoemde regeling een checklist voor droge stortplaatsen en baggerspeciedepots opgesteld en ook het rekenmodel RINAS ontwikkeld(1). Bron: [http://www.nazorgstortplaatsen.nl/](http://www.nazorgstortplaatsen.nl/) en AltVAR(xii). 

_B. Reikwijdte_ Met het model is het doelvermogen (voorzienbare kosten, risicodekking) voor de nazorg voor een stortplaats te berekenen. Op basis van de berekening wordt het zgn. doelvermogen vastgesteld, dat is een totaal bedrag waarmee in eeuwigdurende nazorg kan worden voor


zien. In dit bedrag is een risico-opslag opgenomen, bedoeld om de kosten van niet-reguliere respons bij falen van de voorzieningen te dekken. Deze opslag kan worden berekend met het Risicomodel. Het doelvermogen omvat de volgende onderdelen:  algemeen (administratieve) informatie, aard en inhoud object, historie en kenbaarheid, locatieen omgevingsfactoren; 

 technische voorzieningen, exploitatie;  monitoring en controle;  onderhoud, periodieke vervangingen; 

 risico evaluatie, raming risico-opslag;  administratie en organisatie, rapportage en communicatie, apparaats

 kosten. 

_C. Ervaringen en knelpunten bij gebruikers_ Indien de opzet van het model wordt geprojecteerd op kostenramingen van bodemsaneringen zijn de volgende kanttekeningen erbij te plaatsen:  de algehele opzet, gebruikersvriendelijkheid en het werken volgens een vastgestelde – en als zodanig aangeboden – opzet met default kengetallen werkt over het algemeen efficiënt en prettig. 

 stortplaatsen doorgaans een minder grote kans maken op deelname aan veranderingen in ruimtelijke ontwikkelingen en daarmee een bestemmingswijziging zullen doormaken. Het kostenmodel is daarmee minder geschikt om op dergelijke ontwikkelingen te anticiperen.  Aan het model ligt ten grondslag dat een bij de start bestaande situatie onveranderd blijft, in aard (voorzieningen), mate van risicobeheersing (emissies, kwetsbaarheid), kwaliteit/intensiteit van onderhoud. Het is wel mogelijk om hier door middel van fasering nuances in aan te brengen. 

 Het voor inflatie gecorrigeerde prijspeil blijft onveranderd. 

_D. Bruikbaarheid voor rekenmodel_ De opzet van het IPO-rekenmodel is op onderdelen zeer bruikbaar (systematische opbouw, transparant, overzicht, gebruikswijze, eenheidstarieven, invoerwijze) maar op andere onderdelen juist niet geschikt (te veel toegespitst op één type IBC voor een heel specifieke situatie en daarmee te rigide voor het brede scala aan nazorglocaties waar R&B zich op richt, vanuit wettelijke regelingen zijn veel parameters vastgelegd). De wijze waarop het model beschikbaar is (als freeware downloadable van internet, [http://www.nazorgstortplaatsen.nl/)](http://www.nazorgstortplaatsen.nl/)) en support wordt gegeven (gratis helpdesk via internet) maakt het gebruik van het model laagdrempelig. 

_E. Conclusies_ 

1. De onder D genoemde positieve kenmerken van het model zijn zeer     bruikbaar voor het R&B-rekenmodel. 

2. Gezien de vereiste flexibiliteit (in kunnen spelen op specifieke situa-     ties) zal het rekenmodel nazorgkosten qua opzet en rigiditeit duidelijk     op dit punt moeten afwijken van het IPO-rekenmodel. 


**2.4 Risicomodel bij RINAS** 

_A. Omschrijving inhoud_ Het optreden van een ongewenste gebeurtenis kan leiden tot andere activiteiten dan de verwachte nazorgactiviteiten zoals die in een nazorgplan zijn beschreven en dus begroot. Het gaat dus niet om de normale bandbreedte in nazorgkosten. Het gaat om _gebeurtenissen die wel worden onderkend_ , maar waarvan het zodanig onzeker is of hiervoor ook maatregelen of voorzieningen getroffen moeten worden, dat er in een nazorgplan geen rekening mee kan worden gehouden. Dit wordt ondervangen door ze in een risicoanalyse op te nemen met een bepaalde kans van optreden. Het optreden van een ongewenste gebeurtenis leidt tot een situatie waarbij het milieu wordt bedreigd. Om de situatie vervolgens te herstellen, dienen kosten gemaakt te worden. Deze kosten worden hier verder ‘herstelkosten’ genoemd. 

_B. Reikwijdte_ De ongewenste gebeurtenissen kunnen gerelateerd zijn aan eigenschappen van de stortplaats zelf (vorm, stortmateriaal, voorzieningenniveau) en omgevingseigenschappen (bodemgesteldheid, geohydrologie). Ter berekening van het risicobedrag worden de volgende ongewenste gebeurtenissen onderscheiden (limitatief):  een grondwaterverontreiniging (3 typen): o een vroegtijdig gesignaleerde grondwaterverontreiniging zonder reeds aanwezige (geohydrologische) beheersmaatregelen; o een vroegtijdig gesignaleerde grondwaterverontreiniging met reeds aanwezige (geohydrologische) beheersmaatregelen; o een omvangrijke grondwaterverontreiniging (geen vroegtijdige signalering en geen aanwezige beheersmaatregelen). 

 een lokaal defect aan de bovenafdichting;  een vervroegde vervanging van de bovenafdichting. 

Naast deze gebeurtenissen zijn er mogelijk nog andere denkbaar. De hierboven genoemde ongewenste gebeurtenissen zullen echter als maat gelden voor de berekening van het risicobedrag. Ze worden in dit kader dan ook de ‘maatgevende gebeurtenissen’ genoemd. Het uiteindelijk te reserveren risicobedrag zal echter ook moeten worden aangewend om de gevolgen te herstellen van eventuele andere ongewenste gebeurtenissen. 

Naast de hierboven beschreven maatgevende gebeurtenissen, welke als voorzienbare risico’s beschouwd kunnen worden, kunnen ook _onvoorzienbare risico’s_ worden onderscheiden. Deze gebeurtenissen zijn _uitgesloten_ van verrekening in het risicobedrag. Ofwel omdat de hiermee gepaard gaande kosten onder een ander regime verhaald kunnen worden ofwel omdat het IPO van mening is dat de betreffende gebeurtenissen niet thuishoren bij de inschatting van het risicobedrag. Voorbeelden hiervan zijn het optreden van een aardbeving (schade zal worden gedekt door het Rijk) of een neerstortend vliegtuig (aansprakelijkheidsverzekering van een vliegtuigmaatschappij). 


De afleiding van het risicobedrag houdt in: het voorzien van ‘technisch’ falen (scenario’s), de reactie daarop, de kosten daarvan, kapitalisatie en gewogen sommatie met de waarschijnlijkheid van optreden als weegfactor. In het doelvermogen wordt de risico-opslag berekend met een probabilistisch model. 

**Probabilistische model** In de ‘probabilistische’ berekening van het risicobedrag worden met behulp van de Monte Carlo simulatietechniek faalgebeurtenissen heel vaak doorgerekend. Het technische systeem, faalkansen, faal gebeurtenissen en corrigerende maatregelen worden in detail van te voren uitgewerkt. Bij de simulatie worden telkens verschillende, maar op zich mogelijke waarden gebruikt voor kans, tijdstip en gevolg van falen. Met ingegeven kansverdelingen wordt telkens één uitkomst berekend, de duizenden uitkomsten samen geven inzicht in de verdeling van de mogelijke schadebedragen. Vervolgens wordt in die verdeling een (drempel)waarde als noodzakelijke reservering gekozen (95percentiel, een sterk door risicominnend of risicomijdend gedrag bepaalde, ‘politieke’ keuze). 

_C. Ervaringen en knelpunten bij gebruikers_ Omdat deze methode, net als de ‘quick scan’-methode (volgende paragraaf) gebaseerd is op dezelfde inschatting van faalkansen en corrigerende maatregelen ontlopen beide methoden elkaar niet zo. De probabilistische heeft als voordeel dat de uitkomst beter onderbouwd is en daarmee beter verdedigbaar. Het nadeel is dat de methode minder transparant is dan de ‘quick scan’-methode. De inschatting van de risico’s als zodanig blijft ‘mensenwerk’ en daarmee niet gebonden aan een vast omlijnd of universeel referentiekader. 

Het gebruik van het rekenmodel vraagt relatief veel aandacht, expertise en tijd. 

In de praktijk van stortplaatsen wordt er bij gebrek aan adequate input (ook door dé vakspecialisten in dit werkveld) nog al eens gebruik gemaakt van de mogelijkheid af te wijken van het voorschrift om RINAS te gebruiken door een vast risicopercentage als risicosom op te voeren in de nazorgkosten. Argumenten die hiervoor worden gebruikt zijn divers: de uitkomsten sluiten niet aan bij de beleving van de expert, de invoergegevens zijn van onvoldoende kwaliteit (‘rubbish-in-rubbish-out’), de uitkomsten van het rekenmodel zijn toch veelal punt van onderhandeling of een vast risicopercentage blijkt goed aan te sluiten bij de praktijk en beleving van de betrokkenen. 

_D. Bruikbaarheid voor rekenmodel_ Een rekenmodel als RINAS zou voor nazorg bodemsanering toepasbaar zijn. Hierbij zijn de volgende kanttekeningen te maken:  er is veel onderliggende informatie vereist die veelal niet beschikbaar is;  het toepassen van het model vraagt relatief veel aandacht, expertise en tijd;  door de voorgaande twee punten is het de vraag of het resultaat bruikbaar is; 


 In de praktijk is het werken met een risico-opslagpercentage, geschat door een expert, bevredigender;  Aan RINAS ligt ten grondslag dat een bij de start bestaande situatie onveranderd blijft, in aard (voorzieningen), mate van risicobeheersing (emissies, kwetsbaarheid), kwaliteit/intensiteit van onderhoud. Door middel van fasering kunnen nuances worden aangebracht. In de praktijk werkt dit minder goed.  RINAS werkt met een zeer beperkt aantal risicofactoren. Er is een beperkt aantal vastomlijnde faalscenario’s met interventiemaatregelen in RINAS geïmplementeerd. Nazorg bodemsanering heeft een veel bredere scope en daarmee een breder scala aan risicofactoren. De vraag is of al deze factoren in het model zijn te stoppen en of het model dan nog werkbaar en betrouwbaar is. Als voorbeeld kunnen niet-voorzienbare risico’s worden genoemd die zijn uitgesloten in het RINAS-model. Dit betreft de (financiële) gevolgen van ‘buitenissige’ gebeurtenissen met een kleine kans van optreden en grote gevolgschade, zoals aardbeving, overstroming of neerstortend vliegtuig. De naar kans gewogen verwachtingswaarde van deze scenario’s is klein, ze dragen zo weinig bij aan de totale risicoreservering. Als de gebeurtenis zich in werkelijkheid zou voordoen, kan de gevolgschade zodanig groot zijn dat de betrokken nazorgverantwoordelijke failliet gaat als gevolg van langdurig proces van schadevergoeding. 

_E. Conclusies_ 

1. RINAS heeft een te beperkte scope voor nazorg bodemsanering. 

2. RINAS is te complex voor de bodemsaneringpraktijk 

3. De complexiteit van RINAS wordt er niet beter op indien de scope     wordt verbreedt naar nazorg bodemsanering. 

4. In de praktijk blijkt een risicopercentage dat door een expert wordt     ingeschat niet onder te doen voor een uitkomst uit RINAS. 

5. Voor bijzondere dan wel complexe situaties kan een aanpak als met de     RINAS methode – aangevuld met bijzondere aspecten voor nazorg bo-     demsanering – een gewenste oplossing zijn. 

**2.5 ‘Quick scan’-methode risico’s** 

_A. Omschrijving inhoud_ Een in de praktijk nog al eens gebruikte methode voor de schatting van faalrisico’s is de ‘quick scan’-methode. Deze is gebaseerd op een ‘expert guess’. Een expert beschrijft het technische systeem, faalkansen, faal gebeurtenissen en corrigerende maatregelen. Ook kan een bandbreedte worden aangegeven. De noodzakelijke reservering volgt uit het naar kans gewogen sommeren van de gedisconteerde gevolgschaden voor alle onderkende scenario’s. Hiertoe wordt de volgende formule gehanteerd. 

 Faalrisico (p*  ) = kans op falen(p) X gevolgkosten (  ) 

Een voorbeeld van hoe deze in de praktijk wordt toegepast is in de onderstaande tabel opgenomen. 


**_Tabel 2.1: Praktijkvoorbeeld ‘quick scan’-methode_** 

**Gebeurtenis die tot falen van het systeem leidt** 

 Kans op voorkomen (expert guess) 

 Gevolgen gebeurtenis 

 Kosten (kans maal gevolg) 

Schermwand vertoont lekkage door fout bij installatie 

 0.05  500,000,(deels herplaatsen scherm) 

  25.000,

Schermwand sluit niet goed aan op natuurlijke onderafdichting 

 0.025  1.000.000,(deels herplaatsen scherm) 

  25.000,

Door ontwerpfout debiet te laag voor volledige beheersing 

 0.1  1.000.000,(grondwatersanering en aanpassen beheerssysteem) 

  100.000,

**Totale faalkosten verticale afscherming** 

  150.000,

_B. Reikwijdte_ Deze methode is breed toepasbaar. Ook in de rapportage ROSA(2)^ wordt van deze methode gebruik gemaakt om in de _afwegingsfase_ (saneringsonderzoek) de faalrisico’s inzichtelijk te maken. Deze methode wordt geclassificeerd als ‘complex’. Ook is er in deze rapportage sprake van een ‘eenvoudige uitwerking’ van de faalrisico’s en onzekerheden. In dat geval wordt aangegeven of het risico ‘hoog’, ’gemiddeld’ of ’laag’ is. 

_C. Ervaringen en knelpunten bij gebruikers_ De inschatting van de risico’s als zodanig blijft ‘mensenwerk’ en daarmee niet gebonden aan een vast omlijnd of universeel referentiekader. Omdat deze methode, net als een ‘Probabilistisch model’ gebaseerd is op hetzelfde ‘expert guess’ en dezelfde uitwerking van faalkansen en corrigerende maatregelen ontlopen beide methoden elkaar niet zo. De ‘quick scan’-methode is aantrekkelijk vanwege de kosten en eenvoud (transparantie). In de praktijk ontbreekt het echter aan een referentie voor wat betreft de volgende aspecten:  Welke risico’s dienen te worden meegenomen in de analyse?  Moet voor deze risico’s deze werkwijze worden gehanteerd of is er een andere, beter bruikbare methode, beschikbaar?  Hoe groot zijn deze risico’s?  Hoe dient met deze risico’s te worden omgegaan. 

Doordat het antwoord op een aantal van deze vragen niet gegeven kan worden neigen initiatiefnemers die geen nazorgverantwoordelijkheid wensen te dragen deze met alle lusten en lasten bij marktpartijen onder te brengen. Hierbij willen ‘onder druk van de markt’ nog wel eens te snel afspra


ken te worden gemaakt. De borging van de continuïteit en kwaliteit van de nazorg is hier niet mee gebaat. 

_D. Bruikbaarheid voor rekenmodel_ De methodiek is als zodanig eenvoudig toepasbaar. De resultaten van deze methode zijn eenvoudig in een rekenmodel in te voeren. 

_E. Conclusies_ De ‘quick scan’-methode is eenvoudig toepasbaar. De resultaten zijn – mits de basisgegevens goed zijn – geschikt om als input te gebruiken in een rekenmodel. De benodigde basisgegevens om het risicomodel goed te kunnen uitvoeren zijn niet in alle gevallen beschikbaar. De resultaten van de risicoanalyse zijn dan niet op voorhand goed. 

**2.6 Samenvatting en analyse van de resultaten** De meest gangbare wijze van ramen van nazorgkosten is met spreadsheet‘modellen’. De ervaring die hiermee is opgedaan is een prima basis voor het opstellen van een rekenmodel. Met het rekenmodel moet het belangrijkste euvel van spreadsheetramingen worden ondervangen; namelijk de te grote flexibiliteit. Door deze flexibiliteit is de robuustheid van dergelijke modellen betrekkelijk. Het IPO-rekenmodel is té specifiek voor een algemeen model voor nazorgkosten. Er zitten veel positieve kenmerken in en is daarmee een goede tegenhanger van het te flexibele spreadsheetmodel. Een combinatie van beide methoden zou mogelijk een oplossing bieden voor een model voor raming van nazorgkosten bodemsanering. 

Er zijn eenvoudige en complexe methoden beschikbaar om risico’s in te schatten. In beide gevallen is de betrouwbaarheid van de uitkomst afhankelijk van de input. De belangrijkste en meest kritische factor is de kans op voorkomen van faalkansen. Het model RINAS heeft een te beperkte scope en is te complex voor de doorsnee nazorglocatie. Met een veel eenvoudigere ‘quick-scan’-methode kan volgens experts een kwalitatief vergelijkbaar resultaat worden verkregen. Waar het echter aan ontbreekt, is een gedragen format voor de wijze waarop een dergelijk methode moet worden toegepast. Beide methoden zijn los van een rekenmodel nazorgkosten operationeel. De resultaten van deze methoden zijn eenvoudig in te voeren in een rekenmodel. 


### #     $   

###      

**3.1 Inleiding** In dit hoofdstuk wordt een inventarisatie gegeven van studies die op enige wijze een betekenis hebben voor het ramen van nazorgkosten. Het betreft de resultaten van een ‘quick scan’. De inventarisatie beoogt daarmee niet compleet te zijn, maar de belangrijkste studies weer te geven. 

De belangrijkste doelstelling hiervan is op een bewuste wijze gebruik te maken van beschikbare ervaring. Per onderdeel komt het volgende aan bod: A. Omschrijving inhoud B. Reikwijdte C. Betekenis voor rekenmodel D. Conclusies 

**3.2 IPO-studie “Borgingsmogelijkheden nazorg bodemsanering”** 

_A. Omschrijving inhoud_ In de IPO-studie “Borgingsmogelijkheden nazorg bodemsanering” (3)^ worden technische, organisatorische, financiële en juridische oplossingsrichtingen gegeven voor een aantal knelpunten. Het betreft knelpunten die ten tijde van het opstellen van de rapportage actueel waren. Doordat de studie enkel op specifieke knelpunten ingaat, vormt deze studie daarmee geen kookboek hoe nazorg aan te pakken of hoe nazorgkosten te bepalen. Voor de vraag hoe nazorg in algemene zin aan te pakken wordt verwezen naar documenten als de Richtlijn Bodem (http://www.bodemrichtlijn.nl). 

_B. Reikwijdte_ Wat betreft de financiële oplossingsrichtingen ligt de focus op de financiering van nazorg en is daarmee niet relevant voor R&B. 

_C. Betekenis voor rekenmodel_ De IPO-studie heeft voor het rekenmodel nazorgkosten geen directe betekenis. 

_D. Conclusies_ De IPO-studie heeft voor het rekenmodel nazorgkosten geen directe betekenis. 


**3.3 ‘Rekenmodel’ Landsdekkend beeld** 

_A. Omschrijving inhoud_ Het rapport Evaluatie Bodemsanering, Analyse landsdekkend beeld (4)^ gaat in op de meest waarschijnlijke omvang van de bodemverontreiniging in Nederland en de kosten van aanpak die daaraan nog zijn verbonden. Tevens wordt aandacht besteed aan de ontwikkeling van de bodemsaneringoperatie vanaf begin jaren ’80, in termen van bestede middelen en afgeronde saneringen en onderzoeken (paragraaf 5, blz. 47), ook wordt een vergelijking gemaakt van de gevonden resultaten op basis van het landsdekkend beeld en de verwachtingen uit interdepartementale beleidsevaluatie uit 1997. 

_B. Reikwijdte_ De belangrijkste bevindingen van deze rapportage voor de studie R&B liggen op het vlak van de belangrijkste doelgroep waarvoor het rekenmodel zou moeten worden ontworpen. 

_C. Betekenis voor rekenmodel_ De kosten van een homogene groep (zelfde type) gesaneerde locaties vertonen een min of meer ‘log-verdeling’. Zo maken circa 10% van de locaties een groot deel uit van de kosten. De achtergronden hiervan geeft de studie niet. Wel zijn er indicaties dat deze verdeling ook op nazorglocaties van toepassing is. Kijkend naar de praktijk hebben deze 10% van de locaties naar verwachting betrekking op locaties met een hoog risico-profiel (3). Dit betreft binnenstedelijke locaties met hoge endogene en exogene risico’s. Het gaat hierbij om risico’s die samenhangen met de aard en ernst van de verontreiniging (endogeen) en omgevingsrisico’s zoals geologische en geohydrologische omstandigheden, bedreigde objecten en saneringsvoorzieningen (exogeen). Voor deze locaties is de nazorg beter dan gemiddeld geregeld. Meer interessant is daarom de grote middenmoot van nazorglocaties die door hun aantal een grote aanspraak maken op bodemsaneringbudgetten. Het betreft de vaak meer eenvoudige gevallen die vanuit deze achtergrond geen speciale aandacht krijgen. Voor dergelijke gevallen zou een rekenmodel voor nazorgkosten een meerwaarde kunnen hebben. Gezien de aard van dergelijke locaties zou het rekenmodel laagdrempelig, met relatief weinig achtergrondkennis en eenvoudig te bedienen moeten zijn. 

_D. Conclusies_ Het rekenmodel zou zich vooral moeten richten op de,qua omvang en complexiteit, ‘middenmoot’ van nazorggevallen. De nazorg voor de complexe grote gevallen is veelal geregeld. Tijdens de workshops (zie bijlage 1 is geconcludeerd dat segmentering niet noodzakelijk is. Het model kan bij alle soorten situaties worden toegepast. 


**3.4 Flexibele Emissie Beheersing (FEB)** 

_A. Omschrijving inhoud_ De studie FEB(5)^ is voortgekomen uit een analyse van knelpunten die zich bij de uitvoering van nazorg van IBC-saneringen voordoen(6). 

_B. Reikwijdte_ FEB is een concept waarbij risico’s ten gevolge van verspreiding van verontreiniging niet worden gereduceerd door kostbare en soms overgedimensioneerde of zelfs onnodige maatregelen, maar beheersbaar worden gemaakt met een betrouwbaar monitoringssysteem. Bij FEB kan optimaal gebruik worden gemaakt van een gefaseerde besluitvorming van de aanpak, wat in veel gevallen leidt tot kostenbesparing. Een belangrijk element van FEB is het voldoende zekerheid bieden dat geen onaanvaardbare verspreiding optreedt. Om dit te bereiken worden enkele waarborgen geboden: er worden harde en toetsbare afspraken gemaakt over de grenzen van verspreiding, de verspreiding wordt gecontroleerd door een betrouwbaar monitoringssysteem en er is een interventiescenario beschikbaar om te kunnen worden uitgevoerd als de optredende verspreiding ontoelaatbaar dreigt te worden. Dit laatste kan het geval zijn als gevoelige objecten worden bedreigd of als blijkt dat het saneringsdoel, een stabiele eindsituatie, niet wordt bereikt. Met het FEB-concept kan de BEVER-gedachte om de bodem als reactorvat te gebruiken uitstekend in de praktijk worden gebracht. De beschikbare ruimte wordt ‘veilig’ gebruikt omdat toetsbare grenzen worden gesteld en bewaakt. Op ijkmomenten wordt de stand van zaken herbeoordeeld en wordt vastgesteld in hoeverre een stabiele eindsituatie met minimale nazorg nog binnen de gestelde randvoorwaarden haalbaar is. FEB biedt verder goede toetsingsmogelijkheden voor het bevoegd gezag en is een helder kader voor communicatie tussen alle betrokken partijen die gezamenlijk de randvoorwaarden vaststellen waarbinnen FEB wordt toegepast. 

_C. Betekenis voor rekenmodel_ Interessant voor R&B is een technisch antwoord op onzekerheden in mogelijk optredende verspreiding. Met het FEB-concept kan met een vooraf bepaalde zekerheid een ontoelaatbare verspreiding van verontreinigende stoffen tijdig worden aangetoond. Het is daarmee geen methode om risico’s inzichtelijk te maken maar om verspreidingsrisico’s hanteerbaar te maken. 

_D. Conclusies_ Door toepassing van het FEB-concept is met grotere betrouwbaarheid aan te geven hoe groot de restrisico’s van verspreiding zijn. Hiermee kan een betere onderbouwing worden gegeven van de risicopremie als onderdeel van het rekenmodel. 


**3.5 QRA (Quantitative Risk Analyses)** 

_A. Omschrijving inhoud_ QRA is beschreven in een NOBIS rapport (98-1-10, februari 2000) met de subtitel “ kwantitatieve risicoanalyse (QRA) ter ondersteuning van variantkeuze”. QRA is een methodiek waarmee een team van saneringsexperts en locatiedeskundigen de financiële risico’s van verschillende saneringsvarianten kunnen analyseren en kwantificeren. De belangrijkste risicofactoren kunnen worden geïdentificeerd. Onderzoek of speciale verzekeringsproducten mogelijk zijn zouden hierop afgestemd kunnen worden. De methodiek wordt ondersteund door een computerprogramma “DATA” (http://www.treeage.com). De methodiek geeft meer gedetailleerde informatie over de kosten van saneringsvarianten (inclusief beheertraject). Deze methodiek kan worden beschouwd als een verbijzondering die vooral zinvol kan zijn bij grotere en complexe projecten. 

De risico’s worden in vijf stappen geanalyseerd en gekwantificeerd: 

1. identificeren van faalgebeurtenissen per variant; 

2. ordening van gebeurtenissen tot faalscenario’s; 

3. toekennen van kansen aan faalgebeurtenissen; 

4. kwantificering van de gevolgen van faalgebeurtenissen; 

5. analyse van afweging van varianten. 

_B. Reikwijdte_ Deze stappen leveren een aantal producten op:  kosten kansencurven per variant, dit geeft de bandbreedte aan waarbinnen de kosten variëren;  tornadodiagram, deze geeft de volgorde weer van de omvang van de risico’s;  daarnaast zijn nog andere producten beschikbaar die niet nader zijn beschreven. 

_C. Betekenis voor rekenmodel_ De methodiek om vooral de risicokosten te identificeren en te kwantificeren heeft mogelijk meerwaarde voor risicoparagraaf van het rekenmodel. Nadeel van de QRA systematiek is dat een brede deskundigheid noodzakelijk is voor de toepassing hiervan. De systematiek wordt daarom niet algemeen toegepast. 

_D. Conclusies_ Door toepassing van het QRA-concept is met meer precisie aan te geven hoe groot de risicokosten zijn. Hiermee kan een betere onderbouwing worden gegeven van de risicopremie als onderdeel van het rekenmodel. De methodiek wordt door zijn complexiteit alleen in bijzondere gevallen toegepast. 


**3.6 Case Base Reasoning (CBR)** 

_A. Omschrijving inhoud_ In de afgelopen jaren is veel ervaring opgedaan met in-situ bodemsaneringen. Deze ervaring is meestal opgeslagen in de hoofden van uitvoerders en consultants of in slecht toegankelijke rapporten. Zij is daarom niet eenvoudig beschikbaar voor derden ter beoordeling van nieuwe bodemsaneringgevallen. Het project CBR^7 is opgezet om een systeem te creëren met behulp waarvan bestaande kennis over in-situ bodemsaneringen eenvoudig toegankelijk wordt. 

_B. Reikwijdte_ Het systeem bestaat uit een database (vooralsnog met ca. 100 afgeronde bodemsaneringgevallen) en een “reasoner”, met behulp waarvan in de database kan worden gezocht naar die afgeronde bodemsaneringsgevallen die een zo groot mogelijke overeenkomst vertonen met nieuwe bodemsaneringen. Op deze wijze kan optimaal worden geprofiteerd van reeds bestaande kennis over in-situ bodemsaneringen. Op basis van een zeer beperkt aantal karakteristieken kan tevens een schatting worden verkregen van de saneringsduur en de saneringskosten van nieuwe bodemsaneringgevallen. 

_C. Betekenis voor rekenmodel_ CBR geeft de mogelijkheid de risicokosten te identificeren en te kwantificeren en heeft daarmee mogelijk meerwaarde voor een risicomodule van het rekenmodel. De database is echter nagenoeg niet gevuld met actuele informatie. Nazorgervaring is daarom niet op deze wijze in te brengen in het R&B-project. 

_D. Conclusies_ Vooralsnog is CBR niet geschikt voor de risicoanalyse – en daarmee de risicomodule van het rekenmodel. 

_Aanbeveling_ Een database met nazorgervaringscijfers zal zeker een bijdrage leveren aan het op een hoger plan tillen van nazorg. Denk hierbij niet alleen aan de faalkansanalyse maar ook aan kostenbepalende parameters als de levensduur van kostenintensieve systeemonderdelen. 

**3.7 Risman methode** 

_A. Omschrijving inhoud_ Ook in de Grond-, Wegen Waterbouwsector is geregeld sprake van onvoorziene tegenvallers, schade, vertragingen, budgetoverschrijdingen en conflicten over wie daarvan de kosten moet dragen. Ze zijn bij veel bouwprojecten misschien niet helemaal te voorkomen, maar wel een stuk beter te beheersen met goed risicomanagement. Dit houdt in dat ze in eerste instantie moeten worden (h)erkend en in tweede instantie hanteerbaar moeten worden gemaakt (toebedeeld). Hier wordt de RISMAN-methode geregeld voor gebruikt. In de onderstaande figuur is deze methode schematisch weergegeven. De figuur laat 


zien dat risicomanagement een cyclisch leertraject is. Dit start met een risicoanalyse. De tweede stap is het benoemen van de beheersmaatregelen. Na de tweede sessie moet het uitvoeren van beheersmaatregelen, het evalueren van het effect hiervan en het actueel houden van de risicoanalyse deel gaan uitmaken van het denken van het projectteam, ofwel geïmplementeerd worden in de projectorganisatie 

_Figuur 4.1 Schematische weergave Risman-methode_ 

_B. Reikwijdte_ Risicomanagement kan in alle fasen van een project worden toegepast. Vaak wordt op overgangen van de ene naar de andere fase een nieuwe risicoanalyse uitgevoerd. Voor het ene project spelen misschien niet zozeer de faseovergangen een grote rol, maar kunnen beslismomenten die in de planning worden ingebracht worden aangegrepen voor een grondigere update van de risicoanalyse in vergelijking tot de normale actualisatie. 

_Figuur 4.2 Risman-methode toegepast in achtereenvolgde fasen in een project_ 

Risicomanagement wordt in dit werkveld niet gezien als een tovermiddel, maar in hoofdzaak als een manier van denken. De verantwoordelijkheid voor risico’s en de beheersing daarvan is een aandachtspunt voor het gehele projectteam met de projectmanager als eindverantwoordelijke. Hoe later deze bewustwording ontstaat, hoe meer risico’s zich reeds hebben voorgedaan of hoe beperkter de mogelijkheden tot bijsturing zijn geworden. Risi


comanagement heeft aandacht nodig en kost hierdoor tijd, maar de ervaring leert dat deze tijd wordt teruggewonnen door het beter (onderbouwd) kunnen stellen van prioriteiten. 

In de praktijk wordt doorgaans een onderscheid gemaakt in de volgende categorieën risico’s: 

 _Normale onzekerheden:_ deze vallen binnen de ‘dagelijkse’ werkzaamheden. Hiervoor wordt doorgaans een vaste post genomen volgens vastgestelde rekenregels (percentage van het onderdeel van het werk);  _Specifieke risico’s:_ dit zijn risico’s die buiten de reguliere, voorzienbare risico’s vallen. Hiervoor wordt doorgaans een bedrag gereserveerd op basis van een analyse van de kans op een afwijkende gebeurtenis maal de gevolgen daarvan. Een nadere toelichting op hoe in de praktijk met specifieke risico’s wordt omgegaan is onder deze opsomming van risico’s gegeven. 

 _Scope-risico’s:_ dit zijn risico’s die buiten de scope van het werk vallen en waarmee daarom binnen de contractvorming geen rekening hoeft te worden gehouden. 

Er zijn ruwweg twee methoden om specifieke risico’s te inventariseren en te kwantificeren: 

 _Grote risicobedragen:_ Hiervoor wordt nog al eens van een _‘Monte Carlo’-simulatie_ gebruik gemaakt. De uitkomst van de ‘Monte Carlo’simulatie is – zoals vaker bij modellen – afhankelijk van de input die erin wordt gestopt en daarmee afhankelijk van de kwaliteit van het betrokken adviesbureau. De basis voor de input van de simulatie wordt vaak gevormd door een tabel zoals op de volgende bladzijde opgesteld met de RISMANmethode. Deze tabel wordt ook voor het beheren en beheersen van risico’s (in een cyclisch proces) gebruikt. Voor het invullen van deze tabel wordt veelal een _‘risico-inventarisatiesessie’_ georganiseerd (grote projecten) waarbij met meerdere deelnemers het project wordt geanalyseerd op risico’s. Afhankelijk van de zwaarte van het project en het benodigde draagvlak kunnen hier bijvoorbeeld ook externe onafhankelijke deskundigen in zitten. In de ‘risicosessie’ wordt een _‘risicoregister’_ opgesteld met daarin de _risicoanalyse_. Uiteindelijk kan met de simulatie een _‘realistisch’ risicobedrag_ worden vastgesteld. Dat houdt in dat met een voorop _vastgestelde betrouwbaarheidsmarge_ het bedrag wordt vastgesteld. Hoe hoger het ‘zekerheidsniveau’ (zeker weten dat je met het risicobedrag de faalrisico’s kunt dekken) hoe groter het risicobedrag is. In de praktijk wordt veelal met een zelfde marge gewerkt die algemeen geaccepteerd is. Deze sessie(s) resulteert daarmee in het opstellen van een risicoregister dat als input dient voor projectkostenramingen in opeenvolgende projectfasen. Kostenen risicomanagement zijn hiermee onlosmakelijk met elkaar verbonden. In de volgende tekstbox wordt nader ingegaan op de ‘Monte Carlo’simulatie. 


 _Kleine risicobedragen:_ Hiervoor wordt doorgaans gewerkt met een _spreiding op de eenheidsprijs_ als verbijzondering van de stuksraming. Het schiften van risico’s (welke risico’s vallen in welke categorie) is maatwerk en daarmee per locatie verschillend. Deze schifting wordt afhankelijk van het project uitgevoerd op basis van een voorstel van de adviseur of in samenspraak tussen de adviseur en de opdrachtgever. Bij het beoordelen van de risico’s wordt vaak gebruik gemaakt van een _‘risico hitlist’_ (top-10 of top-20 met meest voorkomende risico’s) waarop de meest voorkomende risico’s in die specifieke sector zijn vermeld. Deze lijst is samengesteld op basis van ervaring. Het blijkt namelijk dat veel dezelfde risico’s steeds weer terugkomen. Deze lijst is daarmee voor een groot deel dekkend voor het project. Risico’s met een kans op voorkomen < 5% staan doorgaans niet op de hitlist. De gevolgen van de risico’s moeten bovendien ook klein zijn. 

De meest gebruikte rekenmethoden zijn SSK (Standaard Kostensystematiek Kostenramingen, publicatie 137 CROW) en PRI 2003 (Project Raming Infrastructuur, ECO RWS) Deze werkwijze kent grote parallellen met de werkwijze die ook wel wordt gevolgd in bodemsanering bij het inventariseren van risico’s. 


**Probabilistische kostprijsberekening (Monte-Carlo analyse)** De Monte-Carlo analyse is een probabilistische rekenmethodiek waarmee de kans wordt bepaald op overschrijding van de geraamde projectkosten. Dit door middel van het nemen van steekproeven tussen de vastgestelde L (laagste) waarde & U (uiterste) waarde. 

Resultaten die volgen uit deze analyse zijn: 

  Verwachtingswaarde (Mu) voor de totale projectkosten;  Bandbreedte rond de verwachtingswaarde (marge);  Top 10 van budgettaire risico’s in de raming;  Scheefte van de raming;  De variatiecoëfficiënt. 

Op basis van de verkregen informatie is het onder meer mogelijk om de trefzekerheid ten aanzien van geraamde projectkosten vast te stellen. Hierdoor kan een duidelijke bovengrens aan het projectbudget worden gesteld en kunnen gericht maatregelen worden getroffen om overschrijdingen van het projectbudget te voorkomen. Mede hierdoor neemt de vraag naar probabilistische (risico)ramingen steeds meer toe en wordt de projectkostenraming een steeds belangrijker instrument voor projectsturing en projectbeheersing. 


**Tabel ###** 

**Risico inventarisatie tabel RISMAN-methode** 

 Gevolg^ aspect 

 Beheersmaatregel 

 Restrisico 

 Stakeholder 

 Nr. 

 Cate-^ gorie 

 Risico omschrijving 

 Oorzaak 

 Gevolg 

 Kans 

 Tijd 

 Geld 

 Kwaliteit 

 Score 

 Risico aspect 

 Kans 

 Tijd 

 Geld 

 Kwaliteit 

 Score 


_C. Betekenis voor rekenmodel_ Door toepassing van de Risman-methode is met meer precisie aan te geven hoe groot de risicokosten zijn. Hiermee kan een betere onderbouwing worden gegeven van de risicopremie als onderdeel van het rekenmodel. De methodiek wordt gaat verder dan de ‘quick-scan’-methode maar biedt daarmee in verschillende stappen in de bodemsaneringsketen van een locatie mogelijkheden te sturen op risico’s. 

_D. Conclusies_ Door toepassing van de Risman-methode is met meer precisie aan te geven hoe groot de risicokosten zijn. Hiermee kan een betere onderbouwing worden gegeven van de risicopremie als onderdeel van het rekenmodel. De methodiek zal vooral op grotere meer complexe locaties zijn meerwaarde bewijzen. 

**3.8 Medische sector** Voor dit onderdeel zal in een latere fase nog invulling worden gegeven aan omgang met risico’s in de medische sector. Dit na interview van kennishouder op dit vlak 

**3.9 Samenvatting en analyse van de resultaten** Er zijn instrumenten beschikbaar voor de risicoanalyse. Daarmee zijn de kosten voor nazorgrisico’s beter te bepalen. Naarmate er meer inzicht is in de faalgebeurtenissen, kansen op voorkomen en gevolgen, zijn deze zinvol in te zetten. Al naar gelang de wensen en behoeften van de opdrachtgever kunnen deze, of elementen daaruit, worden toegepast. In de brainstormsessies kunnen hierin keuzen worden gemaakt. Het rekenmodel zou zich vooral moeten richten op de qua omvang en complexiteit ‘middenmoot’ van nazorggevallen. 


### %      " 

###     

###  

**4.1 Inleiding** In deze paragraaf wordt een kort overzicht gegeven van eisen die aan de berekening van nazorgkosten worden gesteld vanuit verschillende kaders. 

**4.2 Landelijk en provinciaal beleid** 

_A. Omschrijving inhoud_ In de _Circulaire Beoordeling en afstemming_ (viii)^ is in bijlage 6 een overzicht opgenomen met kostenposten die in een saneringsonderzoek dienen te worden opgenomen. Onder de verzamelpost nazorg staat – naast kwaliteits-, kwantiteitsmetingen en begeleiding en toezicht – vermeld ‘scenario bij falen van voorzieningen’. Er wordt niet verder in detail ingegaan op eisen die aan onderbouwing van nazorgkosten worden gesteld. 

In de Handleiding afwegingsproces saneringsdoelstelling (ix)^ worden geen nadere eisen gesteld aan kostenramingen van saneringen dan wel de nazorg. 

In _ROSA II_ (2)^ wordt aandacht besteed aan de relatie tussen saneringskosten en nazorgkosten in het kader van de afweging van saneringsvarianten. De saneringskosten worden conform de Wet Bodembescherming uitgesplitst in de volgende onderdelen: 

 _Stichtingskosten_ : de eenmalige kosten die voorafgaand aan de sanering en bij de start van de sanering (investeringskosten) worden gemaakt;  _Doorlopende kosten_ : kosten die gedurende de looptijd van de sanering zullen worden gemaakt (exclusief vervangingskosten). Hieronder vallen onderhoudskosten, instandhouden, kosten ten gevolge van energiegebruik en lozing op riool;  _Vervangingskosten_ : kosten die na enige tijd worden gemaakt om gehele (of aanzienlijke delen van) installaties of voorzieningen te vervangen;  _Overhead_ : de som van de uitvoeringskosten en de algemene kosten;  _Overige kosten_ : kosten die gemoeid zijn met schadeloosstelling van derden; 

De belangrijkste aandachtspunten bij saneringskosten zijn:  Pas op bij dubbeltelling van kosten bij vervangingsen stichtingskosten;  Neem de monitoringspeilbuizen mee bij vervangingskosten; 


  Het ‘fall-back’-scenario in de saneringskosten wordt meegenomen in het aspect faalrisico’s / onzekerheden;  Binnen RMK systematiek is het mogelijk om onzekerheden in verschillende posten en de saneringsduur mee te nemen. 

De belangrijkste aandachtspunten bij de saneringsduur inclusief nazorg zijn:  De duur van de sanering en nazorg wordt vrijwel altijd kwantitatief uitgedrukt en is vaak erg onzeker, er kan voor worden gekozen om een range aan te geven;  Voor natuurlijke afbraak wordt bij de bepaling van de saneringsduur de verwachte monitoringsperiode voor het bereiken van de beoogde saneringsdoelstelling genomen;  Bij beheersvarianten is de saneringsduur “eeuwig”, hiervoor wordt in de praktijk vaak langer dan 50 jaar aangegeven. 

De _Richtlijn Herstel en Beheer_ (http://www.bodemrichtlijn.nl) verwijst voor kostenposten op te nemen in een nazorgraming naar ‘Checklist nazorgplan, IPO, 1998. Voorts is een tabel opgenomen met belangrijke kostenposten en een zeer korte checklist met kostenposten op te nemen in de kostenraming. 

In het _Besluit financiële bepalingen bodemsanering_ (x) is het volgende aangegeven met betrekking tot de nazorgkosten. Gedeputeerde staten bepalen de hoogte van het bedrag waarvoor financiële zekerheid wordt gesteld op basis van de te verwachten kosten van sanering of nazorg na een periode van 5 jaar. Het bedrag kan op verzoek van degene die de zekerheid heeft gesteld tussentijds worden bijgesteld indien een deel van de maatregelen waarvoor zekerheid is gesteld, is uitgevoerd. 

Verder zou op _provinciaal niveau_ moeten zijn vastgelegd welke eisen er op saneringsplan niveau er aan nazorgramingen worden gesteld. Zo wordt in de PMV van provincie Utrecht melding onder ‘financiële gegevens’ gemaakt van:  Een begroting van de kosten van de sanering;  Een overzicht van financiële middelen ter dekking van de saneringskosten. 

In de bodemnota van provincie Zuid-Holland (xi)^ is sprake van “onzekerheden met betrekking tot de zorgkosten en eventuele kosten van het faalscenario”. Hierbij is niet verder expliciet gemaakt waarop wordt gedoeld. 

_B. Betekenis voor rekenmodel_ Er worden op hoofdlijnen handreikingen gegeven voor de inhoud van een raming van nazorgkosten. Ten behoeve van de financiële zekerheidstelling dient er in de rapportage van de nazorgkosten een knip te worden gemaakt na een periode van 5 jaar. 


Tussentijdse bijstellingen van de nazorgkosten moet met het model mogelijk zijn om desgewenst de financiële zekerheidstelling daaraan aan te passen. 

_C. Conclusies_ Eisen die vanuit landelijk beleid aan nazorgramingen worden gesteld beperken zich tot handreikingen voor kostenposten, inzichtelijk maken van de kosten vóór en na de eerste 5 jaar van de nazorg en de mogelijkheid de nazorgraming gaandeweg de uitvoering van de nazorg bij te stellen. 

**4.3 Bedrijvenregeling** 

_A. Omschrijving scope_ De aanpak van ernstige bodemverontreiniging op bedrijfsterreinen kan vanuit de Bedrijvenregeling worden gesubsidieerd. Dat kan op grond van zogenaamd interim-beleid, in de wandelgangen bekend als de Bedrijvenregeling bodemsanering. Het interim-beleid is nog niet wettelijk op rijksniveau verankerd, maar wordt op dit moment uitgevoerd op grond van een subsidieverordening van de gemeente of provincie. Daarin zijn afspraken van VROM, het ministerie van Economische Zaken, provincies en gemeenten met de werkgeversorganisaties VNO-NCW en MKB-Nederland uitgewerkt. De afspraken staan in het convenant Bodemsanering in gebruik zijnde en -blijvende bedrijfsterreinen. Op grond van een subsidieverordening kunnen eigenaren of erfpachters van bedrijfsterreinen al subsidie aanvragen voor het saneren van ernstig verontreinigde bodem. In januari 2006 is het Besluit financiële bepalingen bodemsanering in werking getreden. Dit besluit treedt in de plaats van de verordeningen. De wettelijke regeling past het interim-beleid aan. Zij versoepelt de eis dat 80% van de verontreiniging van vóór 1975 moet dateren. Dat betekent dat straks ieder bedrijf met een verontreiniging vóór 1975 onder voorwaarden gedeeltelijk voor subsidie in aanmerking komt. 

_B. Betekenis voor rekenmodel_ Voor de eisen die worden gesteld aan de financiële onderbouwing (voor zover deze betrekking hebben op de scope van dit rapport) wordt verwezen naar regelingen onder de Wbb. 

De bijdrage vanuit de Bedrijvenregeling wordt slechts één keer per geval van verontreiniging per onderneming gegeven. Om die reden komen de nazorgkosten enkel in aanmerking voor een bijdrage indien deze (in totaliteit of voor een bepaalde periode) in ééns door het bedrijf in kwestie worden afgeschreven. In de praktijk is het mogelijk om voor deze periode de nazorg bij derden neer te leggen tegen een vastgestelde afkoopsom. Deze laatste som komt – vaak samen met de investeringskosten – in aanmerking voor subsidie. Voor een dergelijke afkoop is inzicht in alle kosten – waaronder desgewenst ook de nazorgkosten – nodig waarvoor een bijdrage wordt gevraagd. 


_C. Conclusies_ De Bedrijvenregeling stelt geen inhoudelijke eisen aan de wijze waarop nazorgkosten dienen te worden geraamd. Daartoe wordt verwezen naar regelingen onder de Wbb. 

**4.4 Verzekeraars** 

_A. Omschrijving belang_ Voor verzekeraars is het in de huidige tijd niet realistisch om nazorg voor lange tijd te verzekeren. Het is wel mogelijk om voor een korte periode van 3 jaar een polis af te sluiten waarna tekens wordt beoordeeld of en hoe deze kan worden voortgezet. In de verzekering kunnen niet alle aspecten worden meegenomen, bijvoorbeeld de werking van damwanden op lange termijn is niet te verzekeren. 

_B. Betekenis voor rekenmodel_ Gezien de scope van de verzekeringsproducten – die qua tijd en dekking beperkt zijn – zijn er geen aanknopingspunten om in het rekenmodel nazorgkosten rekening te houden met eisen die verzekeraars stellen aan de raming van nazorgkosten. 

_C. Conclusies_ Zie onder B. hierboven. 

**4.5 Nazorgorganisaties** 

_A. Omschrijving raakvlak met rekenmodel_ Nazorgorganisaties zijn partijen die de nazorg al dan niet volledig afkopen. In het onderhandelingsproces van afkopen is inzicht in de nazorgkosten en risico’s vereist. Twee van deze organisaties zijn in het kader van deze inventarisatie geïnterviewd (Endanco en Bodemzorg). Bij één van de geïnterviewde nazorgorganisaties wordt voor wat betreft de inschatting van risico’s gebruik gemaakt van een ‘quick scan’-methode (zie ook paragraaf 2.5). 

_B. Betekenis voor rekenmodel_ In de praktijk zullen nazorgorganisaties – ongeacht of de aanbieder van een nazorglocatie zelf al een nazorgraming heeft opgesteld – altijd een begroting en risicoanalyse van de locatie maken. Vanuit die achtergrond is er geen behoefte aan een nieuw rekenmodel. Op basis van deze hercalculatie van de nazorgkosten gaat de nazorgorganisatie _in onderhandeling_ (er bestaat dus geen ‘universele’ nazorgraming) met de aanbieder van een nazorglocatie. Het rekenmodel zou ook als een checklist kunnen worden gezien in het proces van onderhandeling om te komen tot een afkoopsom. De rol die een nieuw rekenmodel in dit onderhandelingsproces ligt vooral in de wijze en snelheid waarmee dit proces kan worden doorlopen indien de aanbieder al zelf een gedegen en complete nazorgraming heeft opgesteld; het zal bijdragen aan wederzijds vertrouwen en het begrip om te komen tot een bepaalde afkoopsom. 


Nazorgorganisaties gebruiken veelal eigen kengetallen (kosten, levensduur voorzieningen, r/i-cijfer). Hierbij baseren ze zich onder meer op eigen ervaringscijfers en de eigen financiële situatie/kostenstructuur. Ze kijken hierbij met een schuin oog naar wat gebruikelijk is in het werkveld. Zo wordt het IPO-rekenmodel nog wel eens gebruikt in geval er geen ervaring is met bepaalde kengetallen (denk aan levensduur). Met het rekenmodel nazorgkosten zouden meer specifieke kengetallen aangereikt kunnen worden. 

De geïnterviewde nazorgorganisaties gaven aan een praktisch werkbare oplossing te hebben gevonden voor ‘het probleem r/i-cijfer’. Het is bekend dat de keuze van het r/i-cijfer op basis waarvan de kapitalisatie wordt uitgevoerd de meest maatgevende parameter is die de hoogte van de nazorgafkoop bepaald. In de praktijk gaan de geïnterviewde nazorgorganisaties ermee om door uit te gaan van een cijfer van 2,5% (of tussen 2% en 3%) als effectief rentepercentage. Een dergelijk cijfer is verdedigbaar vanuit de praktijk van pensioenfondsen die met een ‘gereserveerde beleggingsstrategie’ werken opdat de lange termijn waarde van de fondsen met grote zekerheid wordt gewaarborgd. Ook in het IPO-rekenmodel en in de Wet financiering decentrale overheden (Wet fido) wordt met een vergelijkbaar cijfer gewerkt. Door in het rekenmodel nazorg bodemsanering hierop aan te sluiten, wordt het draagvlak en acceptatie voor deze keuze verstevigd. 

_C. Conclusies_ Nazorgorganisatie hebben geen direct belang bij een rekenmodel nazorgkosten. Het indirecte belang bestaat eruit dat het voor deze organisatie eenvoudiger is om met partijen tot afstemming te komen over een afkoopbedrag van de nazorg op een locatie. Immers indien de probleembezitter zich ter dege bewust is van de nazorgkosten, zal hij op een andere wijze in het onderhandelingstraject met een nazorgorganisatie stappen dan als hij dat niet is. De keuzen die de geïnterviewde nazorgorganisaties hebben gemaakt met betrekking tot het te hanteren r/i cijfer verdient opvolging in het rekenmodel nazorgkosten bodemsanering. 

**4.6 Samenvatting van de resultaten** Vanuit verschillende kaders worden eisen gesteld aan de inhoud dan wel opzet van een rekenmodel nazorgkosten. Deze eisen zijn echter zeer beperkt. 

De keuzen die de geïnterviewde nazorgorganisaties hebben gemaakt met betrekking tot het te hanteren r/i cijfer verdient opvolging in het rekenmodel nazorgkosten bodemsanering. 


### &      '   

###  

**5.1 Inleiding** In twee workshops zijn door het consortium de uitgangspunten en de eisen van het rekenmodel vastgesteld. Daarmee is draagvlak gecreëerd voor de toepasbaarheid van het rekenmodel. In bijlage 1 zijn de uitkomsten van beide workshops nader uitgewerkt. 

**5.2 Resultaten workshops** 

5.2.1 Workshop 1 In de eerste workshop is gepeild waar het rekenmodel aan moet voldoen en wat het rekenmodel moet kunnen berekenen. Hierbij is geinventariseerd onder de consortiumleden voor welke doelen het rekenmodel ingezet zou kunnen gaan worden. Het gaat hierbij o.a. om de volgende onderwerpen: 

  Afwegen van sanerings-/beheervarianten;  Onderbouwen van nazorgraming;  Inzicht in toekomstig benodigde budgetten (jaargebonden);  Vroeg in beeld hebben van gekapitaliseerde kosten;  Inschatten van financiële risico’s;  Berekenen afkoop bedrag/ financiële garantstelling;  Uitvoeren gevoeligheidsanalyse kostenposten;  Nazorg beheerproces stroomlijnen. 

Discussiepunten die aan de orde zijn gekomen waren de volgende:  Moet er een model komen dat breed toepasbaar is of moet er per segment van de markt (volgens SKB project ALTVAR) een model worden ontwikkeld?  Hoe moeten we de risicokosten meenemen in het rekenmodel? 

Segmentering In de discussie over hoe een rekenmodel er uit zou moeten zien is met overgrote meerderheid vastgesteld dat segmentering zoals in eerdere studies (lit. 3 en xii) is voorgesteld voor de opzet van het rekenmodel geen consequenties heeft. Met andere woorden er kan met één opzet van het rekenmodel worden gewerkt voor alle typen locaties. 

   

                                


Risico’s Op basis van praktijkvoorbeelden is gekeken hoe bij grote infrastructurele werken omgegaan wordt met het kwantificeren van risico’s. Vervolgens is in de discussie naar voren gekomen dat bij nazorgprojecten op een minder intensief niveau behoefte is aan de inschatting van risico’s dan bij grote infrastructurele werken. In de laatste situatie is er vaak een specialist ingeschakeld die gedurende het gehele project adviseert over de risico’s en de hiermee samenhangende kosten (ter voorkoming van schade). In de discussie is ook naar voren gekomen dat bij bodemsanering en nazorg minder kennis, ervaring over risico’s beschikbaar is dan in de bouw. Het consortium heeft aangegeven dat er wel behoefte is om de risicokosten mee te nemen in het rekenmodel. 

Aandachtspunten Als aandachtspunten voor het vervolg zijn aangegeven:  Voorbeelden van risicobeoordeling/kwantificering verzamelen;  Meenemen van de aandachtspunten vanuit van bevoegd gezag (beschikking, handhaving);  Meenemen input van grootsaneerders, uitvoerende partijen; 

Tevens is een tweetal ontwikkelingen gesignaleerd die mogelijk op termijn van invloed kunnen zijn op het rekenmodel:  Loskoppelen van de bovenen ondergrond;  Toepassen van risicogerichte nazorg. 

5.2.2 Workshop 2 In de tweede workshop is dieper ingegaan op een systematiek om de nazorgrisico’s te kwantificeren (zie bijlage 3). Hiermee heeft het consortium ingestemd. Verder zijn de uitgangspunten van het rekenmodel uitgewerkt in functionele eisen die vervolgens door alle deelnemers zijn gewogen. Op basis hiervan zijn alle breed gedragen onderdelen opgenomen in het programma van eisen voor de bouw van het rekenmodel. 

In het programma van eisen is de volgende onderverdeling te maken:  _Eisen ter ondersteuning van de besluitvormingsfase:_ In de besluitvormingsfase (SO, SP) is nog onvoldoende zicht op de financiële kant van nazorg. Het wiel wordt nog te vaak opnieuw uitgevonden door het ontbreken van een vast referentiekader (opzet raming, wijze van gevoeligheidsanalyse). Een onderbouwde keuze zou bijdragen aan meer efficientie in de besluitvorming. O.a. o Onderbouwde kengetallen (eenheidsprijzen, levensduur voorzieningen, renteen inflatiecijfers) o Er moet een vergelijkingsmogelijkheid van de ramingen in zitten; o Gevoeligheidsanalyse m.b.t. rente en inflatie en de meest bepalende kostenposten; o .. 

       

         !"#$ %   %   

                 &  ' ( 


 _Eisen ter ondersteuning van de beheertaken van beheerders van nazorglocaties:_ In de praktijk blijkt hier nog onvoldoende ervaring mee te zijn opgedaan. De partijen zijn nog zoekend naar de juiste invulling daarvan en ervaring hoe derden dit oppakken. De behoeften spitsen zich toe op ondersteuning van de uitvoeringstaken zodat de nazorg beter is in te plannen en te budgetteren. O.a. o Bij rapportages moet een meerjaren begroting op locatieniveau en een clustering van locaties kunnen worden gemaakt. o Mogelijkheid contante-waarde berekening o .. 

 _Eisen met betrekking tot de gebruiksvriendelijkheid._ Het model moet logisch zijn opgebouwd, transparant, eenvoudig in gebruik, flexibel. O.a. o Prijspeilen moeten instelbaar zijn op locatieniveau en er moet overal indexering mogelijk zijn; o Exporteermogelijkheid naar MS-Excel; o Importeer/exporteermogelijkeid van kengetallen o Invoerdump voor later gebruik; o ... 

**5.3 Enquete t.b.v. bepalen grootste discussiepunten** Naar aanleiding van vragen van de SKB is als laatste stap van de verkenningsen definitiefase een enquete onder het consortium en expertpanel gehouden met als doel de belangrijkste discussiepunten voor het rekenmodel nazorgkosten bodemsanering boven water te krijgen. De resultaten van de enquete zijn uitgewerkt in bijlage 2. 

De belangrijkste discussiepunten zijn:  _Hoe om te gaan met ‘nazorgrisico’s’:_ In de eerste workshop is onderkend dat de risico’s van nazorg en de wijze waarop deze in het rekenmodel nazorgkosten terechtkomen uitgezocht moet worden. Een methodiek hiervoor is in de tweede workshop besproken en geaccordeerd. De resultaten van het doorlopen van de analyse van nazorgrisico’s bij een specifieke locatie zijn eenvoudig in te brengen in het rekenmodel. Dit zal met het uitwerken van een case in het vervolg van het project worden gedemonstreerd.  _De keuze van de toe te passen rente/inflatiecijfers:_ Alhoewel een geringe verhoging of verlaging van het r/i-cijfer leidt tot een substantieel andere bedrag voor de nazorg, lijkt er een goede oplossing voor te zijn. In paragraaf 4.5 is deze al aangegeven. Ook een door KIWA opgestelde concept richtlijn voor het afkopen van nazorglocaties sluit op deze lijn aan. Het ligt – mede op grond van inhoudelijke argumenten – voor de hand op deze keuze aan te sluiten. Het model zal toestaan om af te wijken van de standaard cijfers.  _Het bepalen van de kengetallen (prijzen, levensduur van voorzieningen):_ Binnen dit project zal gestart worden met het traject om te komen tot onderbouwde en algemeen gedragen kengetallen. Daartoe worden de 

    &  ' (           ( ) *+  $        #$ ,   , 

  )      

           &  ' (    &  ' (    &  ' (    &  ' (    &  ' (           ( ) *+  $        #$ ,   ,    &  ' (    &  ' (    &  ' (    &  ' ( 


op dit moment gebruikte kengetallen verzameld (rekenmodel nazorgkosten stortplaatsen, gegevens consortium, expertpanel en klankbordgroep, richtlijn herstel en beheer, etc. ). Tijdens het gebruik van het operationele model moet door het uitwisselen van ervaringscijfers de kwaliteit van de kengetallen steeds beter worden.  _Beleidmatige vragen_ : Discussies over het nazorgplan / de monitoringsstrategie (hoe vaak, welke parameters, wanneer mag men stoppen) vallen buiten de scope van dit project. Startpunt voor het rekenmodel is een uitgewerkt nazorgplan. Uiteraard kan het model wel gebruikt worden om de financiële consequenties van wijzigingen in de monitoringsstrategie (eerder stoppen, intensiveren, eerder/later vervangen van voorzieningen) te berekenen. 

De overige discussiepunten zullen vooral betrekking hebben op gebruikersniveau van het model (wijze van invoer en uitvoer, opzet van modulles, lay-out schermen). Hiertoe worden in het bouwproces van het model meerdere momenten ingelast om hierover binnen het consortium overeenstemming te krijgen. 

        


### ( )  *  +  

### !,, 

**6.1 Inleiding** 

6.1.1 Algemeen Dit hoofdstuk is een inhoudelijke uitwerking van het te realiseren programma van eisen voor het rekenmodel. In de paragrafen van dit hoofdstuk wordt ingegaan op de werkwijze in de bouwfase en wordt een indicatieve kostenraming vastgesteld. In volgende hoofdstukken passeren functionele en technische aspecten de revue. 

6.1.2 Werkwijze bouwfase In de bouwfase wordt uitgegaan van een stapsgewijze oplevering van tussenproducten. Per stap wordt in overleg met het op te richten projectteam bepaald wat er gebouwd gaat worden, wat de datum van oplevering is, en tegen welke kosten dit gerealiseerd wordt. 

Deze werkwijze beoogt dat:  geprofiteerd kan worden van voortschrijdend inzicht over de precieze inhoud van de functionaliteiten;  een tussentijdse herprioritering van te bouwen functionaliteiten kan plaatsvinden indien gewenst;  de ontwikkelaar op een lijn blijft met het projectteam;  het projectteam actief betrokken blijft bij de totstandkoming van de applicatie;  per stap de planning en het resterende budget worden geactualiseerd; 

Aan het eind van de onderzoeken bouwfase wordt een test van het complete systeem uitgevoerd. De test, die door de klankbordgroep wordt uitgevoerd, levert mogelijk nog aanpassingen op die zullen worden doorgevoerd. Door de systematiek van release en beoordeling van tussenproducten, is het aantal en de omvang van deze aanpassingen naar verwachting beperkt. 

Dit projectvoorstel kan tijdens de bouwfase worden bijgesteld in de volgende gevallen:  het projectteam komt door voortschrijdend inzicht tot andere ideeën over de functionaliteiten;  de ideeën over de functionaliteiten blijven onveranderd, maar de prioritering wijzigt;  bepaalde functionaliteiten kosten minder/meer tijd dan verwacht 


 zodat er meer/minder ruimte is om andere functionaliteiten te bouwen. 

6.1.3 Kosten realisatie programma van eisen Het totstand gekomen programma van eisen kan binnen het beschikbare budget voor de bouwfase worden uitgevoerd. Verder bijstellen van de prioriteiten is in dit stadium niet zinvol omdat de geraamde ontwikkelinspanning indicatief is en niet nodig omdat de stapsgewijze methodiek in de bouwfase rekening houdt met tussentijdse bijstelling van prioriteiten. 

Op basis van de gestelde prioriteiten die in hoofstuk 5 zijn uitgewerkt, wordt een naar het oordeel van het consortium doelmatige applicatie ontwikkeld, die beantwoordt aan de behoefte aan een krachtig maar eenvoudig bruikbaar en gestandaardiseerd hulpmiddel bij het opstellen van ramingen/begrotingen van nazorgprojecten. 

**6.2 Functionele kenmerken** 

6.2.1 Algemeen 

_6.2.1.1 Scope van het model_ Het model zal geschikt zijn om zowel eenvoudige als complexe ramingen/begrotingen op te stellen. Hoewel in principe gericht op gebruik voor “echte” nazorglocaties, zal het model ook ingezet kunnen worden voor bijvoorbeeld NAVOSof BSB-locaties. 

_6.2.1.2 Basisarchitectuur (functionele eis 1, bijlage 1)_ Een kostenmodel dat zowel geschikt is voor eenvoudige als complexe ramingen dient uit te gaan van een gemeenschappelijke basis die in alle soorten ramingen terugkomt. Geconstateerd kan worden dat een raming altijd bestaat uit kostenposten die ingedeeld zijn in een aantal rubrieken. Daarnaast kunnen rubrieken op hun beurt rubrieken bevatten. Voor eenvoudige saneringslocaties zijn wellicht 2 rubrieken en 10 kostenposten al voldoende. Voor complexe situaties kunnen tientallen rubrieken en honderden kostenposten worden ingevoerd. 

_6.2.1.3 Rubriek_ Functies van de rubriek:  Container om kostenposten aan toe te kennen;  Definiëren van aggregatieposten. Dit zijn posten waarvan de hoogte van het bedrag bepaald wordt door een rekenkundige bewerking op (een deel van) de kostenposten binnen de rubriek. Een percentage onvoorzien of een percentage voor directievoering bijvoorbeeld wordt dan berekend als een percentage maal het totaal van de kostenposten binnen de rubriek.  Definiëren van subtotalen. Indien men bijvoorbeeld voor een rubriek ‘Leeflaag’ niet losse kostenposten wil definiëren, maar eenvoudigweg wil invoeren “20.000 euro per jaar”, dan kan dit op rubrieksniveau worden ingevoerd.  Een bijzondere rubriek vormt de locatie. De locatie kan worden be


 schouwd als een hoofdrubriek, maar ook als een subrubriek, bijvoorbeeld in die gevallen waarbij men meerdere locaties wenst te clusteren. 

_6.2.1.4 Kostenpost_ Een kostenpost wordt gekenmerkt door tenminste de volgende eigenschappen:  Fasering: Een kostenpost kan in verschillende perioden verschillend gedefinieerd zijn _; (eisen 6,7, bijlage 1)_  Tijdspanne: de periode waarbinnen de kostenpost van toepassing is. De ingangsdatum van een kostenpost kan een vast moment zijn (kalenderjaar) of gerelateerd zijn aan het moment van aanvang nazorg (nazorgjaar). De einddatum kan daarnaast als optie “eeuwigdurend” hebben (feitelijk dus geen einddatum).  Frequentie: het aantal keer dat een kostenpost in een jaar voorkomt (of het aantal jaren tussen het optreden van een kostenpost).  Bedrag. Het bedrag kan een vast bedrag zijn, of worden uitgedrukt in een eenheidsprijs maal aantal eenheden. 

_6.2.1.5 Standaardmodules_ Het model zal voorzien in het gebruik van standaardmodules. Bijvoorbeeld een module “Monitoring”, die alle rubrieken en kostenposten bevat waarvan sprake is bij monitoring. De standaardmodules vormen een hulpmiddel om het skelet van de raming te construeren. De gebruiker kan op snelle en eenvoudige wijze een raming opbouwen door een of meerdere standaardmodules te kiezen. Vervolgens kan de gebruiker zelf nog bepaalde kostenposten/rubrieken verwijderen en/of juist andere toevoegen. 

6.2.2 Beheren gegevens 

_6.2.2.1 Beheer algemene gegevens_ Per raming kunnen een aantal algemene gegevens worden ingevoerd. Dit zijn in ieder geval NAW-gegevens van eigenaar en/of vergunninghouder en/of de opsteller van de raming. Daarnaast wordt in de bouwfase in overleg met het projectteam bepaald welke overige algemene gegevens zinvol zijn om op te nemen. Hierbij zal gekeken worden naar pakketten als GLOBIS en RINAS. 

Er wordt ook een vrije invoertabel toegevoegd waarin de gebruiker in de eerste kolom een kenmerk (bijvoorbeeld “tel. beheerder”) invoert en in de tweede kolom de waarde van dit kenmerk (bijvoorbeeld “06-112 223 44”). 

_6.2.2.2 Beheren kostenposten_ Het beheren van de kostenposten zal verlopen via één scherm dat dient te voldoen aan de volgende eisen: 1) Bieden van overzicht Het scherm geeft een overzicht van de hiërarchie van beschikbare rubrieken en kostenposten. 2) Geven van detailinformatie Het scherm toont per rubriek de details van de kostenposten. 


 3) Mogelijkheid tot bewerking Het scherm bevat een bewerkscherm waarmee de kostenposten en rubrieken bewerkt kunnen worden. 

Aan een dergelijk eisenpakket kan worden voldaan met de in bijlage 4 geschetste indeling. Links staat de hiërarchie van rubrieken en kostenposten, rechtsboven de details van alle kostenposten in de geselecteerde rubriek, en rechtsonderaan bewerkt de gebruiker de kostenpost (dit scherm is niet nader gedetailleerd). Een dergelijke indeling is gebaseerd op de schermlay-out van Microsoft Outlook. De hiërarchische structuur van mappen en e-mails is vergelijkbaar met die van rubrieken en kostenposten. Een dergelijke schermindeling is een gebruikersvriendelijke en herkenbare manier van gegevenspresentatie, die in veel applicaties in variaties terugkomt. 

_6.2.2.3 Beheren rubrieken_ Zoals in paragraaf 6.2.1.3 beschreven, vervult de rubriek een aantal functies. Als de gebruiker in het linkerscherm een rubriek selecteert, komt in het scherm rechtsonder een subscherm met eigenschappen van de rubriek te staan. Via dit scherm kan de invoer gepleegd worden die correspondeert met de in paragraaf 6.2.1.3 beschreven functies. Nieuwe rubrieken kunnen worden toegevoegd en bestaande verwijderd met een rechtermuisknopmenu in het linkerscherm, en via de knoppenbalk/menubalk. 

_6.2.2.4 Beheren kostenposten_ De in paragraaf 6.2.1.4 beschreven eigenschappen van een kostenpost kunnen worden bewerkt als de gebruiker in het linkerscherm of rechterbovenscherm een kostenpost selecteert. 

In aanvulling op de in paragraaf 6.2.1.4.beschreven eigenschappen, zal de mogelijkheid worden geboden om een kostenpost te linken aan een andere kostenpost. Hiermee kan de gebruiker geheugensteuntjes voor zichzelf vastleggen. Het ligt bijvoorbeeld voor de hand dat als de post “onderhoud hekwerk” vervalt omdat het hekwerk uit de raming wordt gehaald, dat dan ook de post “inspectie hekwerk” kan worden verwijderd. Om dergelijke relaties vast te leggen, kan een gebruiker kostenposten aan elkaar linken. Deze linking is vooral ter informatie aan de gebruiker: het systeem zal wel een signaal afgeven op het moment dat een gebruiker een bewerking doet op een kostenpost die relaties heeft met een andere kostenpost, maar grijpt niet inhoudelijk in door kostenposten te muteren. 

6.2.3 Basiskengetallen _(functionele eis 2, bijlage 1)_ 

_6.2.3.1 Omschrijving_ In het model wordt een functionaliteit gerealiseerd voor het invoeren, onderhouden en toepassen van basiskengetallen. De basiskengetallen hebben betrekking op levensduren van voorzieningen, prijzen en rente-en inflatiecijfers. Voor andere parameters wordt vooralsnog geen basiskengetallenfunctionaliteit gerealiseerd. 


_6.2.3.2 Beheer basiskengetallen_ Er wordt een scherm gebouwd waarmee de gebruiker een of meerdere sets van basiskengetallen kan beheren. Beheren betekent: nieuwe onderwerpen toevoegen, bestaande onderwerpen bewerken en bestaande onderwerpen verwijderen. 

De mogelijkheid van meerdere sets heeft als voordeel dat de gebruiker voor bepaalde ramingen een andere set kan gebruiken dan voor andere ramingen. 

Aan een set kan de gebruiker een of meerdere voorzieningen/kostenposten toekennen. Een basislijst met voorzieningen/kostenposten wordt bij de software meegeleverd maar kan door de gebruiker uitgebreid worden. Een voorziening/kostenpost uit de basislijst heeft een unieke ID dat bij iedere gebruiker hetzelfde is en een naam/omschrijving. Het ID dient om een voorziening/kostenpost uniek te identificeren, wat van pas komt bij de uitwisseling en vergelijking van kengetallen (zie paragraaf 6.2.3.4). Een door de gebruiker toegevoegde voorziening/kostenpost kent geen unieke ID. 

Per voorziening/kostenpost voert de gebruiker een ondergrens en bovengrens in voor de prijs in euro’s of de levensduur in jaren. Als de gebruiker niet wil werken met een onder-/bovengrens maar met een vaste waarde, voert hij in beide vakken hetzelfde getal in. Daarnaast kan per voorziening/kostenpost een opmerking ingevoerd worden. 

_6.2.3.3 Toepassing basiskengetallen_ In het scherm waar de kostenposten aan de ramingen worden toegevoegd, wordt een functie ingebouwd waarmee de gebruiker een basiskental kan selecteren. Door een basiskental te selecteren wordt de gemiddelde waarde van het basiskental ingevuld in het betreffende invoervak en wordt de kostenpost gelinkt aan een basiskental. Het linken betekent dat bij het invoervak een indicator komt te staan die aangeeft dat: 

 Het ingevulde getal afkomstig is uit een basiskental en niet is overruled door de gebruiker; of  Het ingevulde getal afkomstig is uit een basiskental en is overruled door de gebruiker; Daarnaast betekent het dat op het scherm ‘Beheer basiskengetallen’ bij een kental een indicator komt te staan die aangeeft dat het basiskental gebruikt wordt. Als een basiskental gebruikt wordt kan hij niet verwijderd worden. 

Hoe om moet worden gegaan met het bewerken van reeds gebruikte basiskengetallen wordt in de bouwfase met het projectteam besproken. 

_6.2.3.4 Uitwisselen basiskengetallen_ Er wordt een functionaliteit gebouwd waarmee gebruikers sets van basiskengetallen kunnen uitwisselen met elkaar. Bij de export kan de gebruiker een bestandsnaam en –locatie kiezen en een basiskengetallenset wegschrij


ven naar dit bestand. Bij import selecteert de gebruiker het basiskengetallenbestand dat geïmporteerd moet worden. Als een basiskengetallenset met eenzelfde naam/ID reeds voorkomt, krijgt de gebruiker de mogelijkheid om de bestaande basiskengetallenset uit te breiden/te overschrijven/toe te voegen onder nieuwe naam (exacte implementatie na overleg met het projectteam). 

De export/importfunctie kan ook gebruikt worden om via een centrale plaats (bijvoorbeeld de website) basiskengetallensets te distribueren en te verzamelen. Met verzamelen wordt bedoeld dat gebruikers op eigen initiatief of op verzoek van de beheersorganisatie, periodiek hun basiskengetallensets uploaden naar de website. 

_6.2.3.5 Actualiseren bestaande kengetallen_ De beheerorganisatie kan de verzamelde basiskengetallensets naast elkaar leggen. Doordat de basisvoorzieningenlijst werkt met unieke ID’s, kunnen de kengetallen die gebruikers in de loop der tijd hebben ingevoerd eenvoudig met elkaar worden vergeleken. Op basis van de vergelijking kan de beheerorganisatie besluiten om een nieuwe uitgave van de kengetallenlijst te distribueren via een downloadpagina op de website. 

_6.2.3.6 Toevoegen nieuwe kengetallen_ Daarnaast kan blijken dat gebruikers nieuwe voorzieningen/kostenposten met levensduurkengetallen geïntroduceerd hebben. Als dergelijke voorzieningen/kostenposten vaak voorkomen, kan de beheersorganisatie besluiten om een nieuw basiskental toe te voegen aan de basislijst (met naam en ID) en een levensduurkental en/of prijs toe te kennen aan deze voorziening/kostenpost. Deze exercitie vereist handwerk, omdat gebruikers niet allemaal dezelfde benaming zullen hanteren voor deze nieuw ingevoerde voorzieningen/kostenposten, en het systeem dus niet geautomatiseerd een lijstje van door gebruikers ingevulde kengetallen per nieuwe voorziening/kostenpost kan presenteren. 

_6.2.3.7 Export basiskengetallen bij export raming_ Omdat kostenposten uit ramingen gelinkt kunnen zijn aan een basiskental, dienen bij de export van ramingen naar een exportbestand de benodigde basiskengetallen meegeëxporteerd worden. Hierbij bestaan verschillende mogelijkheden:  De gebruiker kan de gerelateerde volledige basiskengetallenset(s) mee-exporteren;  De gebruiker kan alleen de gerelateerde basiskengetallen meeexporteren ;  De gebruiker kan ervoor kiezen dat de link wordt verbroken en de in de kostenposten opgenomen basiskengetallen worden geëxporteerd als ware het niet aan een basiskental gelinkte waarden. Welke van deze opties ondersteund gaan worden, wordt in de bouwfase vastgesteld in overleg met het projectteam. 


6.2.4 Prijspeilen _(eis 4, bijlage 1)_ 

_6.2.4.1 Invoer van kostenposten_ Alle kostenposten van een raming dienen te worden ingevoerd in hetzelfde prijspeil. Per raming kan de gebruiker opgeven wat het prijspeil is. Bij invoer van de kostenposten dient de gebruiker zich bewust te zijn van het prijspeil waarin de raming staat, vooral indien een raming die een paar jaar geleden is ingevoerd, moet worden geactualiseerd. 

_6.2.4.2 Omwerken prijspeilen_ De mogelijkheid zal worden geboden om prijzen om te rekenen naar een ander prijspeil. Hiertoe zal een beheerscherm worden gerealiseerd waar de gebruiker per kalenderjaar kan opgeven wat het indexeringspercentage was per 1 januari van dat kalenderjaar. Het aantal records dat kan worden aangemaakt is vrij. Als een gebruiker een raming in prijspeil 2002 wil omrekenen naar prijspeil 2005, dan zal hij tenminste indexcijfers voor de jaren 2003, 2004 en 2005 moeten invoeren alvorens het systeem een omrekening kan uitvoeren. Bij een omrekening worden alle bedragen van een raming met dezelfde factor gemuteerd; er wordt geen onderscheid gemaakt naar aard/categorie van een kostenpost. 

Het originele bedrag blijft niet behouden. Alvorens een prijspeilomrekening uit te voeren geeft het systeem hiervan een waarschuwing en biedt de optie om een back-up te maken van de raming in het huidige prijspeil. 


6.2.5 Berekening doelvermogen De doelvermogenberekening wordt uitgevoerd op basis van de volgende formule, die per kostenpost wordt doorgerekend: 

 ( 0 , 5 ) 

 ( 0 , 5 ) ( 1 ) 

 1 ts tp (^1 ) tu tp tu ts r 

 F K i      

     

Waarin: Ktp: ingevoerde kostenpost op t = tp [] Fts: benodigde omvang fonds op t=ts [] r: rente [aantal procent /100] i: inflatie [aantal procent /100] ts: kalenderjaar van start nazorg [kalenderjaar] tp: kalenderjaar prijspeil van de ingevoerde kostenposten [kalenderjaar] tu: kalenderjaar in nazorgfase waarin een uitgave aan een kostenpost [kalenderjaar] van toepassing is. De halfjaarscorrectie (+0,5) zorgt ervoor dat alle uitgaven in het midden van het uitgavejaar worden verondersteld. 

De som van deze individuele kostenposten (Fts) vormt het doelvermogen. 

De volgende uitgangspunten zijn aan de orde:  De nazorgfase gaat altijd in op 1 januari van een kalenderjaar;  Tijdspannes van kostenposten worden ingevoerd op jaarniveau (nazorgjaar of kalenderjaar);  Kostenposten die niet meer dan 1x per jaar voorkomen worden verondersteld te vallen halverwege het ingevoerde nazorg/kalenderjaar. Aangezien zowel nazorgjaren als kalenderjaren ingaan per 1 januari, valt een dergelijke post dus altijd op 1 juli van een kalenderjaar;  Van kostenposten die meer dan 1x per jaar voorkomen wordt eerst het jaarbedrag uitgerekend en vervolgens wordt ten behoeve van de kapitalisatie dit jaarbedrag beschouwd als een eenmalige uitgave op 1 juli van het jaar.  Kostenposten die geen einddatum kennen (eeuwigdurende kostenposten), worden berekend als kostenposten met een eindjaar van 1000 jaar.  Renteen inflatiepercentages kunnen separaat worden ingevoerd en worden vooralsnog per doelvermogenberekening als constanten beschouwd. 

6.2.6 Berekening jaarbegroting De jaarbegroting wordt berekend door (binnen een door te gebruiker in te voeren jarenrange) per jaar de kostenposten op te halen en door te rekenen op inflatiecorrectie. Net als bij de doelvermogenberekening geldt ook hier 


dat van kostenposten die meer dan 1x per jaar voorkomen eerst het jaarbedrag wordt berekend en vervolgens op dit jaarbedrag een inflatiecorrectie wordt uitgevoerd. 

6.2.7 Rapportages _(eis 9, bijlage 1)_ 

_6.2.7.1 Algemeen_ In het softwarepakket wordt een aantal standaardrapportages opgenomen. Hoewel het technisch mogelijk is om een rapportengeneratorfunctionaliteit in te bouwen wordt hiervan afgezien om de volgende redenen:  De ontwikkeling van een dergelijke functionaliteit kost dermate veel inspanning dat het een onevenredig beslag zou leggen op het beschikbare budget;  Ruime flexibiliteit beantwoordt niet aan de wens om uniformering te bereiken in de indeling en opmaak van kostenrapportages. Naast een keuze aan meest wenselijke rapportages zal het model de toevoeging van extra rapporten ondersteunen als maatwerk op verzoek. 

_6.2.7.2 Rapportage berekeningsresultaten_ De volgende typen rapporten worden gerealiseerd: 1) meerjarenbegroting 1 locatie (detailrapport en samengevat op rubrieksniveau); 2) meerjarenbegroting meerdere locaties (detailrapport en samengevat op rubrieksniveau); 3) contante-waardeberekening (detailrapport en samengevat op rubrieksniveau); 

 De tabelschema’s van deze formats zien er als volgt uit. 

 1) meerjarenbegroting voor 1 locatie 

 2) meerjarenbegroting voor meerdere locaties 


 3) contantewaardeberekening 

De rapportagefunctionaliteit wordt zodanig opgesteld dat op termijn eventuele nieuwe formats kunnen worden toegevoegd zonder dat een update van het hoofdprogramma nodig is. 

Op het scherm waarop de gebruiker het systeem de opdracht geeft om een rapportage te creëren, kan hij ook aangeven of hij de algemene gegevens (zie paragraaf 0) meegerapporteerd wil hebben. 

_6.2.7.3 Rapportage ruwe invoer_ Het doel van deze rapportage is het archiveren van ingevoerde data in het projectdossier. Mocht een volledige systeemcrash leiden tot het verlies van alle data, dan kunnen alle gegevens handmatig weer ingevoerd worden op basis van dit rapport. Het kan met het oog op (ISO)normeringen een vereiste zijn dat een rapport van ruwe invoer sec kan worden overlegd. 

_6.2.7.4 Technische implementatie (eis 10, bijlage 1)_ Alle rapportages worden als Microsoft Excel –bestand gecreëerd en opgeslagen op een bestandslocatie naar keuze. De gebruiker kan vervolgens deze bestanden afdrukken op de in Excel gebruikelijke wijze, archiveren of verder bewerken. 

6.2.8 Berekening gevoeligheidsanalyse _(eis 3, bijlage 1)_ De gevoeligheidsanalyse heeft tot doel om vast te stellen welke aspecten van de raming een belangrijke invloed hebben op de omvang van het doelvermogen. 

De gevoeligheidsanalyse zal zich tenminste richten op  invloed van wijziging van rente/inflatie op het doelvermogen;  overzicht van meest maatgevende kostenposten. 

Met het projectteam wordt in de bouwfase vastgesteld of daarnaast nog andere soorten gevoeligheidsanalyse (bandbreedte van termijnen, prijzen, frequenties) geïmplementeerd gaan worden. Dit zal afhangen van ruimte in budget en planning. 


_6.2.9_ Vergelijkingen van ramingen _(eis 8, bijlage 1)_ Voor bijvoorbeeld een afweging van saneringsvarianten is het handig om ramingen met elkaar te kunnen vergelijken. Er wordt een module gebouwd waarmee een gebruiker een aantal ramingen kan selecteren. De module zet de ramingen naast elkaar op het scherm en geeft door middel van kleuren/typografie/pictogrammen aan waarin ze verschillen. 

Indien ramingen in een verschillend prijspeil staan, zal het prijspeil omgerekend worden (zie ook paragraaf 6.2.4.2) 

6.2.10 Invoer risico In het model kan een risicobedrag worden opgenomen als toeslagpercentage en/of vast bedrag op rubrieks/ramingsniveau. De in te voeren percentages en/of bedragen worden door de gebruiker vastgesteld op basis van de voorgestelde marsroute, zie bijlage 3. De identificatie van risico’s en kwantificering tot kengetallen voor kans en gevolg en de daaruit volgende opslagpercentages of bedragen, vallen buiten de scope van dit projectvoorstel. 

6.2.11 Export/import van ramingen _(eis 10, bijlage 1)_ De gebruiker kan een raming exporteren naar een bestand. Dit bestand kan uitgewisseld worden tussen gebruikers van het softwarepakket. Een exportbestand bevat alle data die hoort bij een bepaalde raming. Bij het exporteren van ramingen dient de gebruiker te besluiten of gerelateerde levensduurkengetallen meegeëxporteerd moeten worden (zie paragraaf 6.2.3.7) 

6.2.12 Back-upfunctionaliteit De gebruiker kan een raming wegschrijven naar een back-upbestand. Bij een systeemcrash kan na inlezen van een dergelijk back-upbestand zonder verlies van data verder gewerkt worden aan de raming. Bij een back-up van een raming worden altijd alle gerelateerde levensduurkengetallen en algemene gegevens mee opgeslagen. 

6.2.13 Beheer ramingen Er wordt een functionaliteit geïmplementeerd waarmee de gebruiker ramingen kan dupliceren. Deze optie maakt het mogelijk om eenvoudig verschillende varianten van een raming op te stellen of een nieuwe raming te maken op basis van een bestaande. Tevens worden functionaliteiten voor het aanmaken van nieuwe ramingen en het verwijderen van bestaande ramingen geïmplementeerd. 

6.2.14 Updatefunctionaliteit _(eis 11, bijlage 1)_ In de applicatie wordt een functionaliteit ingebouwd waarmee de gebruiker automatisch of handmatig kan vaststellen of er programma-updates beschikbaar zijn. Deze functionaliteit wordt geïmplementeerd door contact te leggen met de supportwebsite. De applicatie doet een verzoek om informatie aan een service op de webserver. Deze service retourneert versieinformatie van de meest recente bestandsversies. De applicatie stelt ver


volgens vast of er programmaonderdelen beschikbaar zijn voor download. Als dat het geval is, krijgt de gebruiker de keuze om de updates te downloaden. Om de updatefunctionaliteit te laten werken moet de gebruiker beschikken over de benodigde internettoegangsrechten. Als alternatief kan ervoor worden gekozen om de bestanden handmatig te downloaden vanaf de website. 

**6.3 Technische kenmerken** 

6.3.1 Programmeertaal De applicatie wordt ontwikkeld in Microsoft.NET (spreek uit: “microsoft dot net). Microsoft.NET is sinds 2002 de nieuwe ontwikkelstandaard van Microsoft. Een aantal talen zijn beschikbaar binnen dit platform, waarvan de belangrijkste VB (Visual Basic) en C# (C-sharp) zijn. C# wordt beschouwd als de voorkeurstaal voor professionele applicaties en zal daarom worden ingezet voor onderhavig project. 

Met de keuze voor Microsoft.NET en programmeertaal C#, is gegarandeerd dat:  de applicatie volgens moderne en bewezen normen kan worden ontwikkeld (objectgeoriënteerd, n-tier-systematiek); 

 de applicatie tijden kostenefficiënt kan worden ontwikkeld door de toepasbare krachtige ontwikkelomgeving en -hulpmiddelen.  continuïteit van het pakket op lange termijn gewaarborgd is (Microsoft heeft zich gecommitteerd aan verdere doorontwikkeling van het .NETplatform);  een groot aantal marktpartijen in aanmerking komt voor het softwareonderhoud na oplevering (het .NET-platform wordt breed toegepast bij softwareontwikkelingbureaus). Microsoft.NET –applicaties draaien op computers met Windows 98 of hoger, zodat ook voor gebruikers met een systeem dat niet up to date is de applicatie beschikbaar zal zijn. 

6.3.2 Technische architectuur 

_6.3.2.1 Objectoriëntatie_ De applicatie wordt objectgeöriënteerd geprogrammeerd. Naast een groot aantal voordelen in de bouwfase (betrekking hebbend op onder andere de wijze van ontwerpen, programmeren en testmogelijkheden; het voert te ver om hier in dit stuk in detail op in te gaan) betekent dit ook dat het onderhoud (preventief/correctief/vernieuwend) aan de applicatie eenvoudiger is doordat de structuur zeer helder is vergeleken met een procedureel geprogrammeerde applicatie. Vrijwel alle professionele applicaties worden tegenwoordig objectgeoriënteerd geprogrammeerd. 

_6.3.2.2 Gelaagde systematiek_ De applicatie wordt in lagen opgebouwd volgens de zogenaamde _n-tier_ systematiek. Er zullen drie lagen ( _tiers_ ) worden onderscheiden: 


1. Persistance     Deze laag handelt de communicatie tussen de bussinesslogic en de on-     derliggende database af; 

2. Bussinesslogic     Deze laag bevat de applicatiespecifieke domeinobjecten en -routines     die de manipulaties met deze objecten uitvoeren. In deze laag zullen     bijvoorbeeld de verschillende kostencalculaties uitgevoerd worden. 

3. Userinterface     Dit zijn de invoerschermen, menu’s etc. die de communicatie tussen de     bussinesslogic en de gebruiker verzorgen. 

De belangrijkste voordelen van het realiseren van een gelaagde structuur zijn:  door de scheiding in lagen blijft het aantal taken dat een laag verzorgt beperkt en de taken die verricht worden zijn specifiek voor die laag. Dit heeft grote voordelen voor de onderhoudbaarheid van de applicatie op termijn. Het is bijvoorbeeld mogelijk om het onderhoud op de bussinesslogic te laten verrichten door een expert op dat gebied, terwijl een andere de userinterface onderhoudt; 

 voor de persistance-laag kan gebruik worden gemaakt van een standaard persistance framework. Door een in de praktijk bewezen persistance framework te gebruiken, kan de besteedbare ontwikkeltijd gericht worden op het programmeren van de applicatiespecifieke delen (de bussinesslogic en de userinterface). 

Door de bussinesslogic (het hart van de applicatie) volledig te scheiden van de andere twee lagen ontstaat de mogelijkheid om: 

 de applicatie ook als webapplicatie op het internet/bedrijfsintranet aan te bieden (extra userinterface bouwen; de bussinesslogic en persitancelaag blijven onveranderd); 

 de applicatie aan een andere database te koppelen (andere instellingen in het persistance framework; de bussinesslogic en userinterface blijven hetzelfde; Omdat hierbij steeds twee lagen van de applicatie onveranderd blijven, zijn de kosten van dergelijke uitbreidingen aanzienlijk lager dan bij herbouw. Hoewel deze uitbreidingen buiten de scope van dit projectvoorstel vallen, zijn ze illustratief voor de continuïteitsvoordelen die de n-tier systematiek met zich meebrengt. 

_6.3.2.3 Fysieke splitsing_ De scheiding van de applicatielogica in aparte lagen (zie paragraaf 6.3.2.2) komt tot uitdrukking in een splitsing van de applicatie in verschillende bestanden. De drie logische lagen worden ieder in een apart bestand opgeleverd. Dit heeft tot voordeel dat bij het verstrekken van updates alleen die bestanden hoeven te worden verstrekt, die ook daadwerkelijk aangepast zijn. De splitsing kan nog verder doorgevoerd worden, zodat ook bijvoorbeeld de taak “Creëren Rapportages” in een apart bestand wordt opgeleverd. Tot welk niveau de splitsing wordt doorgevoerd, wordt tijdens de bouwfase vastgesteld. 


6.3.3 Relationele database De data die door de gebruiker wordt ingevoerd en door de applicatie wordt getoond en bewerkt, wordt door de applicatie vastgelegd in een relationele database. De relationele databasesystemen die ondersteund zullen worden zijn: 1) Microsoft SQL Server (MS-SQL). Dit is een professioneel databasesysteem dat voldoet aan alle eisen voor de beoogde toepassing. Voor Microsoft SQL Server dient de gebruiker een licentie te hebben. 2) Microsoft database Desktop Engine (MSDE). Dit is een licentievrije versie van MS-SQL. Vanuit het oogpunt van toepasbaarheid voor de te bouwen applicatie, zijn de limitaties van de licentievrije versie niet beperkend. Alleen bij een groot aantal gebruikers op dezelfde MSDE-database, zal een lagere performance worden bereikt dan bij MS-SQL. 

Zoals de naam al aangeeft, is MSDE primair bedoeld voor installatie op de desktop (de lokale pc), zodat iedere gebruiker zijn eigen database heeft. MS-SQL is primair bedoeld om geïnstalleerd te worden op een centrale server, waar meerdere computers toegang toe hebben. Het is echter ook mogelijk om een MSDE-database te delen met meerdere gebruikers en MS-SQL te installeren op een lokale pc voor gebruik door 1 persoon. 

Door middel van een configuratiescherm in de applicatie zal de gebruiker aangeven aan welke database geconnect moet worden. De gebruiker kan indien gewenst tussendoor wisselen van connectie, bijvoorbeeld om op een locale MSDE-database conceptramingen te bewerken, en op een centrale MS-SQLserver definitieve ramingen te plaatsen. 

Vanwege de toegepaste n-tier-systematiek met een aparte datalaag (zie paragraaf 0), is het op termijn mogelijk om een nieuwe datalaag toe te voegen die geschikt is om andere relationele databasesystemen (bijv. Oracle, MySQL) aan te spreken, zonder dat de overige applicatielagen aangepast hoeven te worden. 

6.3.4 Setupkit Om de installatie zo eenvoudig mogelijk te laten verlopen, wordt een setupkit gebouwd. Dit is een apart programma dat in ieder geval de volgende taken zal uitvoeren:  Installeren MSDE (optioneel);  Installeren applicatie (verplicht);  Uitvoeren databasescripts om de database te bouwen; 

6.3.5 Supportwebsite _(eis 11, bijlage 1)_ De ondersteuning aan gebruikers zal verlopen via een daartoe te creëren website. 


De website zal voorzien in de volgende zaken:  Downloaden setupkit;  Downloaden/uploaden basiskengetallenlijsten (zie ook paragraaf 6.2.3.4)  Service voor geautomatiseerd downloaden programmaonderdelen vanuit de applicatie;  Handmatig downloaden updates programmaonderdelen;  Gebruikershandleiding;  Rubriek “Veelgestelde vragen”. 

Op termijn kan de website naar behoefte uitgebreid worden met bijvoorbeeld een discussieforum of een telefoonnummer voor telefonische ondersteuning, afhankelijk van de resultaten van een te houden evaluatie. 


- )      

###   + 

Naast de bouw van het rekenmodel zal in de volgende fase van het project ook aandacht worden besteed aan het verder uitwerken van “de Marsroute” voor het omgaan met risico’s en het vergroten van het draagvlak voor het rekenmodel. 

Omgaan met risico’s Tijdens de volgende fase van het project zal “de Marsroute” voor het omgaan met risico’s worden toegepast bij een case. Daarnaast zal worden bekeken of kennis vanuit andere SKB-projecten bv “Risicomanagement en contractvorming” en “Brownfields” nuttig kan worden toegepast. Verder zal ook de verzekeringswereld nog worden benaderd voor commentaar en advies bij het toepassen van “de Marsroute”. 

Vergroten draagvlak De leden van het consortium, expertpanel en klankbordgroep zullen intensief worden betrokken bij de bouw en het testen van het rekenmodel. Om te komen tot een goed werkend model met voldoende draagkracht zal verder aandacht besteed moeten worden aan het vergroten van het draagvlakbij de beslissers. Hierbij kan gedacht worden aan projectontwikkelaars, grondeigenaren, bestuurders of bevoegd gezag. Zij zullen naast de betrouwbaarheid van de raming behoefte hebben aan hoe het rekenmodel gebruikt kan worden in exploitatieberekeningen etc. Om hier nader invulling aan te geven dient in de volgende fase van het project, naast het bouwen van het model, ook een cross-over plaats te vinden naar een planeconoom die redeneert vanuit standpunt van grondeigenaar / projectontwikkelaar en een accountant die meer kijkt vanuit standpunt van bestuurder, die verantwoording af moet leggen over het uitgegeven geld. 



./$01 


#### "2    

De prioritering van de wensen voor het rekenmodel heeft in twee stappen plaatsgevonden. Hiervoor zijn, bij twee sessies, een twintigtal deelnemers vanuit consortium en expertpanel aanwezig geweest. In de eerste workshop van 25 oktober 2005 zijn de belangrijkste uitgangspunten van het rekenmodel besproken. De resultaten uit workshop 1 staan onderstaand beschreven. Onder het kopje workshop 2 staat het prioriteringsproces beschreven met een overzicht van de daadwerkelijke prioritering t.b.v. het rekenmodel. 

**Resultaten Workshop 1** 

De onderwerpen die zijn behandeld in de workshop zijn onderstreept en per onderwerp kort behandeld. 

Segmentering Er is gekeken naar mogelijke segmenteringen van nazorg op basis van de resultaten van het IPO rapport BO 19 en het SKB-project AltVAR. Daarbij kwamen aan de orde: 

- Actieve en passieve nazorg ; 

- Dynamische en statische locaties; 

- Nazorg door overheid of derden; 

- Hoog risico of laag risico; 

- Soort locatie: WBB, stortplaats, bouwstofconstructie; 

- Nazorgpakketten (registratie, monitoring, actieve isolatie); 

- Locale of gebiedsgerichte aanpak; 

- Stedelijk gebied of landelijk gebied. 

Aan het eind van de dag was de conclusie dat het niet noodzakelijk is om in het kader van dit project te kiezen voor een bepaald segment. Het rekenmodel kan voor alle mogelijke segmenten worden gebruikt, de (reken)techniek is namelijk voor alle locaties dezelfde. De verschillen in de segmenten zitten in de hoeveelheid nazorgmaatregelen die moeten worden meegenomen en de mogelijke risico’s. 

Doelen van het model Vervolgens is geïnventariseerd waar men het rekenmodel voor wil gaan gebruiken: 

- afweging saneringsvarianten, onderbouwde nazorgraming; 

- maken afweging voor vooral kleine en middelgrote gevallen; 

- inzicht toekomstig benodigde budgetten; 

- inzicht jaargebonden budgetten en gekapitaliseerd; 

- gevoeligheidsanalyse kostenposten; 


- onderbouwen eigen aanbieding; 

- berekening bedrijvenregeling; 

- als basis voor financiële garantstelling; 

- optimale keuze doorsaneren versus nazorg; 

- inschatting financiële risico’s; 

- inzicht risico’s (juridisch, omgeving); 

- berekenen bedrag afkoop, overnemen beschikking; 

- gemeenschappelijke basis, stroomlijnen proces, ramen van risico’s; 

Kostenbeheersing / risicomanagement AT Osborne verzorgde een presentatie over de verschillen in kostenbeheersing en risicomanagement bij utiliteitsbouw en bij infrastructuurprojecten. Aandachtspunten waren: 

- Is de scope (pve) van het project duidelijk of gevoelig voor verande-     ringen; 

- Wel of geen gedragen kostenmodel beschikbaar; 

- Hoeveelheid beschikbare ervaringscijfers; 

- Beschikbaarheid kostenexpertise. NB: De beschikbare kennis over de beheerkosten van utiliteitsbouw en infrastructuurprojecten is veel geringer dan de kennis over de bouwkosten. 

Vervolgens is bekeken hoe dat voor bodemsanering / nazorg is: einddoel is duidelijk, de weg ernaar toe niet, geen gedragen kostenmodel, weinig ervaringscijfers en kostenexpertise. Dit betekent dat een groot deel van de kosten vallen onder reserveringen en onvoorzien. 

Daarna werd ter illustratie ingegaan op risicomanagement bij enkele grote projecten (HSL-Zuid, Gottharttunnel, Betuweroute). Conclusie: bij dit soort projecten wordt intensief op risico gestuurd. 

Dit onderdeel van de workshop is na de workshop mede als basis gebruik voor de uitwerking van hoe om te gaan met nazorgrisico’s (zie bijlage 3 ). 

Onderstaande aandachtspunten zijn aan het eind van de workshop door de deelnemers genoemd als aandachtspunt voor vervolgtraject. Tevens zijn enkele relevante ontwikkelingen benoemd: 

- Ervaringen met RINAS-model, voorbeelden van risicobeoordeling     verzamelen; 

- Mening bevoegd gezag (beschikking, handhaving); 

- Input van grootsaneerders / uitvoerend bedrijfsleven; 

- Ontwikkeling: Loskoppeling boven- en ondergrond; 

- Ontwikkeling: Risicogerichte nazorg. 

Functies en aandachtspunten voor het model: De resultaten van de eerste workshop over de functies en aandachtspunten voor het model zijn verwerkt en deels verder uitgewerkt in een discussienotitie voor de 2e^ workshop. 


 Resultaten workshop 2 

 Tijdens de workshop van 23 november is gestemd over welke functionele eisen gesteld moeten worden aan een rekenmodel nazorgkosten. Samengevat zijn de volgende randvoorwaarden en wensen geformuleerd ten aanzien van het te bouwen rekenmodel: o Algemene acceptatie, gevalideerd en checklist-based; o Bruikbaar in zo vroeg mogelijk onderzoeksstadium en zeker bij afweging saneringsvarianten; o Gebruiksvriendelijk, logisch, inzichtelijk en eenvoudig; o Flexibel, maar wel uniform (overal toepasbaar); o Kapitalisatieberekening en budgetraming (te koppelen aan meerjarenplanning); o Onderbouwde en geaccepteerde kengetallen, maar ook maatwerk mogelijk; o Eenheidsprijzen orde van grootte en bandbreedtes; o Gevoeligheidsanalyse; o Meenemen risicokosten (+ inhoudelijke discussie hierover nodig, wat wel, wat niet). 

 In onderstaande tabel staan de resultaten van de stemming weergegeven in aantallen plussen (wel nodig) en minnen (niet nodig). Cursief: opmerkingen vanuit het consortium. 

**FUNCTIONELE EISEN (blad 1)** 

 1 Basisarchitectuur +2  Opm: fasering kostenposten in de tijd 2 Kengetallen  Levensduren +7  prijzen +1  In software bijgeleverd +4  door gebruiker in te voegen +3 3 Gevoeligheidsanalyse  rente en inflatie +7  prijzen  bepalende kosten +6  levensduur^ +2 

   

 Opm: looptijd, kosten per item of rubriek, frequenties, aantallen. Default+Bandbreedte 4 Prijspeilen bij invoer  instelbaar per ingevoerde prijs +1 -2 instelbaar op locatieniveau +4 -2 5 Prijspeilen omwerking +2  overall indexering +3 indexering differentieerbaar 


  r en i separaat +2 6 Invoer datum aanvang nazorg  kalenderjaar +7 (uitg. per 1 juli) maand  

**FUNCTIONELE EISEN (blad 2)** 

 7 Datums kostenposten  Vast (kalenderjaar) +2  t.o.v. aanvang nazorg (nazorgjaar) +4  t.o.v. andere kostenpost +1   signalering koppelingen +3 8 Vergelijkingen ramingen +4       9 Rapportages  zelf definieerbaar +4 -3    meerjarenbegroting 1 locatie +8  meerjarenbegroting n locaties +7 contante-waardeberekening +6 variantenanalyse +1  meerjarenbegroting: inzicht frequenties +2   samenvatting op hoofdposten +3  invoer dump (ISO)^ +5  invoer dump voor latere invoer +2          


  

 Tijdens de workshop is tevens de marsroute met betrekking tot het meenemen van de risicokosten in het model aan de consortiumleden voorgelegd. De marsroute zoals deze in dit rapport (Bijlage 3) is beschreven is unaniem als bruikbaar instrument geaccepteerd. 

**OVERIGE EISEN** 

 User interface    

10 Technische eisen 

   export MS Excel +8   export MS Access   export Word   export ...   export + import kengetallen +3 

   

 extern, om default aan te passen (jaarlijks) +4   autorisatieniveaus -3 

   

 (beheerder: aanpassen kengetal

_len)_ (^) +3   11 Handleiding/support  website _(voor IT-aspecten)_ +8   digitaal document (word/pdf) +1   papieren document -3  12 Formele validatie +3 -2      


"2     

**Inleiding** 

In het kader van de ontwikkeling van het rekenmodel voor nazorgkosten is onder consortium en expertleden een enquête gehouden. Doel van de enquête was meer inzicht te krijgen in de knelpunten die worden ervaren op het gebied van de werkelijke nazorgkosten versus de geraamde kosten. Van de 17 leden hebben er 12 gereageerd. 

**Resultaten enquête** 

**1. Door welke knelpunten loopt u vast bij het bepalen van de kos- ten van een nazorgproject.** 

Vooral het identificeren en kwantificeren van risico’s wordt als knelpunt ervaren. Direct daarna komt de vraag hoe je eigenlijk om moet gaan met langjarige projecten en hoe je daarvoor op een algemeen geaccepteerde wijze een kostenraming kunt maken (aspecten als wijze van kapitalisatie en budgetvorming). Knelpunten die minder vaak worden genoemd zijn het gebrek aan onderbouwde kengetallen en het feit dat er vaak te weinig bekend is over een locatie (bijvoorbeeld geohydrologie of specifieke stofeigenschappen) om een goed nazorgprogramma te kunnen ontwerpen en daarvan de kosten te kunnen ramen. Wat hoort er minimaal in zo’n nazorgprogramma thuis en wat zijn optionele onderdelen? 

**2. Wat is de belangrijkste oorzaak van discussies over nazorgkos- ten en hoe vaak komt het voor dat nazorgprojecten significant stagne- ren of worden afgeblazen.** 

De discussie gaat vaak over het nut en noodzaak van bepaalde nazorgactiviteiten. Welke activiteiten neem je wel mee en welke niet? Nauw hiermee verbonden is de behoefte aan algemeen geaccepteerde kengetallen voor levensduren, frequenties en eenheidsprijzen van activiteiten. Onzekerheid en onenigheid over mee te nemen risico’s speelt ook hier een belangrijke rol. 

Dit alles hangt direct samen met de benodigde financiële middelen, die vaak als (te) hoog worden ervaren. Als er weinig tot geen discussie is over de hoogte van de nazorgkosten blijft nog wel de vraag over wie het beheer over een nazorgbudget moet krijgen. Partijen hebben nogal eens tegengestelde belangen. 

**3. Hoe vaak komt het voor dat de hoogte van de nazorgkosten de reden is dat niet tot nazorg wordt over gegaan. En wat zijn de belang- rijkste gevolgen.** 

Hierover is men het niet eens. Enkele respondenten zeggen dat dit vaak voorkomt en anderen zeggen juist dat het niet zo zeer om de hoogte van de kosten gaat, maar meer om de vraag hoe een budget beheerd moet worden. 


De meeste respondenten hebben hiermee echter geen ervaring en/of hebben er geen mening over. 

**4. Hoe vaak komt het voor dat de methode waarop de kosten be- rekend worden een breekpunt is waardoor nazorgproject geen door- gang vindt (of met grote stagnatie).** 

Idem als vraag 3. 

**5. Hoeveel procent wijkt de raming van de nazorgkosten van een second opinion gemiddeld af van de originele raming. Wat is hiervan de belangrijkste oorzaak?** 

Ook hier zeggen de meeste respondenten dat ze er geen kijk op hebben. Het gevoel zegt dat er grote verschillen kunnen bestaan, afhankelijk van de (on)afhankelijkheid van de adviseurs en de wijze waarop wordt omgegaan met risico’s. 

**6. Wat zijn volgens u de drie belangrijkste redenen van het niet doorgaan van een nazorgvariant, in volgorde van belangrijkheid.** 

De belangrijkste redenen zijn: Risico’s zijn onduidelijk of te groot: 7 keer genoemd Gebruiksbeperkingen zijn ongewenst: 3 keer genoemd Waardevermindering / smet op de locatie: 3 keer genoemd Men komt er financieel niet uit: 3 keer genoemd 

Onenigheid over de methodiek van kostenberekening wordt hier slechts één keer genoemd. 

Enkele respondenten wijzen op de rol van het bevoegd gezag: enerzijds kan die een nazorgvariant afkeuren, maar anderzijds komt het ook voor dat een nazorgprogramma doodbloedt omdat er niet wordt gehandhaafd. Wijzigingen in weten regelgeving spelen een rol. Het komt ook voor dat er na een beperkt aantal meetrondes al besloten wordt dat er geen verdere nazorg meer nodig is. Daarbij komt nog dat een deel van de nazorglocaties weinig ruimtelijke dynamiek heeft en de uitvoering van nazorg daardoor als niet urgent wordt beschouwd. 

**7. Wat zijn in de lopende nazorgpraktijk de drie belangrijkste kostenfactoren, in volgorde van belangrijkheid.** 

Monitoring (bemonstering en analyses) en personele kosten (coördinatie, interpretatie, rapportage) worden het meest genoemd. Periodieke vervanging van voorzieningen en aanpassingen en onderhoud aan voorzieningen komen daarna. 


Minder vaak worden genoemd: risicokosten, onttrekking/lozing en zuivering van grondwater en de keuze van de rente en inflatie cijfers. 

**8. Waar kunnen nog knelpunten optreden in het bouwtraject van het model.** 

Onenigheid over de keuze voor bepaalde kengetallen (frequenties en eenheidsprijzen) en de wijze van risicocalculatie worden beschouwd als de grootste beren op de weg. Factoren die daarnaast worden genoemd zijn: geldgebrek, te weinig draagvlak, conflicten over te hanteren rente en inflatie cijfers, te veel kostenposten/perfectionisme, bepaalde functionaliteiten blijken lastig in te bouwen. 

**9. Welke 5 functionaliteiten van het rekenmodel – zoals dat nu is**     **beoogd – zijn voor u het meest van belang en om welke reden.** 

Contante waarde berekening: 6 keer genoemd Meerjarenbegroting van een locatie: 5 keer genoemd Kengetallen levensduren: 4 keer genoemd Kengetallen in software bijgeleverd: 4 keer genoemd Gevoeligheidsanalyse rente en inflatie: 4 keer genoemd Gevoeligheidsanalyse bepalende kosten: 4 keer genoemd Meerjarenbegroting van meerdere locaties: 2 keer genoemd Kunnen vergelijken van ramingen: 2 keer genoemd Datum kostenpost t.o.v. aanvang nazorg: 1 keer genoemd 

De belangrijkste redenen die leiden tot stagnatie van nazorgprojecten in relatie tot de kostenbepaling van nazorg zijn:  Volgens veel mensen is er vaak sprake van een overschatting van de nazorgkosten, omdat er te veel aspecten worden meegenomen in de kostenraming;  Het is vaak moeilijk om een algemeen geaccepteerde opzet van een budgetfinaciering te realiseren. Hierbij is ook de onderbouwing van de kapitalisatie vaak een knelpunt (er zijn te weinig kengetallen om een betrouwbare meerjarenraming te maken);  Als er door meerdere partijen kosten worden berekend zullen, door verschil van inzicht en verschil van belangen, de verschillen in de ramingen al snel 10 >30% bedragen. Hierdoor onstaat vaak een gevecht om de hoogte van het nazorgbedrag. Mogelijk zijn hier zaken ook met andere afspraken dicht te leggen. Dit vergt echter vaak een intensiever traject waarbij draagvlak noodzakelijk is van alle partijen.  Het rekenmodel staat of valt bij goede betrouwbare kengetallen, deze onderbouwde kengetallen ontbreken nu vaak. Hierdoor is onderlinge vergelijkbaarheid beperkt en is draagvlak snel verdwenen  De risico’s bij nazorgvariant zijn niet geidentificeerd en gekwantificeerd, waardoor onduidelijkheid bestaat en besluiten uitblijven;  Het is opvallend dat bij de meest bepalende kostenfactoren niemand de risicokosten (vervangen materialen etc.) noemd, maar 

       

               . )       %%/#$ /,)   /,)#$ /,)  


 wel monitoring en personele kosten (misschien duidt dit op de mogelijkheid dat de nazorgrisico’s bij veel locaties helemaal niet zo groot zijn in tegenstelling tot het algemene beeld. Dit beeld wordt misschien gekleurd door enkele grote gevallen).  Waardevermindering (psychologisch) en gebruiksbeperking (is feitelijk ook een waardevermindering) zijn de belangrijkste negatieve aspecten van nazorg die kunnen leiden tot niet doorgaan van nazorgvariant. Het is echter lastig om deze factoren te kwantificeren, waardoor dit nu vaak een gevoelskwestie blijft.  Het beheren en inzetten van een nazorgbudget is problematisch als er sprake is van meerdere partijen die financiering moeten regelen. Iedere partij gaat vanuit eigen positie onderhandelen over de hoogte van de bedragen en vaak ook vanuit verschillende financieringskaders;  Als belangrijk aandachtspunt voor de kwantificering van nazorgkosten met rekenmodel is genoemd dat er voldoende draagvlak moet zijn voor de toepassing van het model. 

Conclusie van de bovenstaande bevindingen is dat de meeste aspecten meegenomen worden in de functionaliteit van het rekenmodel en de risicobenadering. De zaken die nog opgepakt moeten worden zijn:  Hoe gaan we om met waardevermindering a.g.v. gevoelsmatige aspecten (hoe te kwantificeren);  Hoe realiseren we binnen afzienbare tijd een redelijke set onderbouwde kengetallen, die door alle partijen worden geaccepteerd. Transparantie is hierbij maatgevend;  Hoe zit het met het overschatten van de nazorgkosten in relatie tot de risico’s. Het lijkt er op dat in de maatgevende kosten de risicokosten vaak een ondergeschikte rol spelen; Niet alle risico’s en gebruiksbeperkingen etc. zijn te voorzien of te vangen in een kostenmodel. Hiervoor is het nodig dat er goede afspraken worden gemaakt tussen betrokken partijen hoe om te gaan met de belangrijkste risico’s, situaties etc. Dit zijn zaken die moeilijk te kwantificeren zijn. Dit gaat vaak over wie kan waarvoor verantwoordelijk zijn (vanuit verschillende rollen: eigenaar, gebruiker etc.). 

       

         . )       %%/#$ /,)   /,)#$ /,)  

       

       %%/ 

   ¶ 


"#23  4 5   

Bij de bepaling van de totale nazorgzorgkosten bij bodemsaneringen hoort veelal een opslag te worden opgenomen ter dekking van risico’s ofwel ongewenste gebeurtenissen. Het optreden van een ongewenste gebeurtenis kan leiden tot andere activiteiten dan de verwachte nazorgactiviteiten zoals die in een nazorgplan zijn beschreven en dus begroot. Het gaat dus niet om de normale bandbreedte in nazorgkosten. Het gaat om gebeurtenissen die wel worden onderkend, maar waarvan het zodanig onzeker is of hiervoor ook maatregelen of voorzieningen getroffen moeten worden, dat er in een nazorgplan geen rekening mee kan worden gehouden. 

In deze paragraaf wordt een marsroute voorgesteld voor het omgaan met risico’s bij de raming van nazorgkosten van bodemsaneringen met het te bouwen rekenmodel. Omdat dit een betrekkelijk fundamentele keuze is voor de opzet van het rekenmodel is dit onderwerp relatief uitgebreid uitgewerkt en besproken in de tweede brainstormsessie. 

**Probleemstelling** Uit de studie AltVAR(xii)^ blijkt dat we de lange termijn risico’s niet (voldoende objectief) kunnen kwantificeren. Dit leidt tot belemmeringen in de nazorgmarkt in het algemeen en tot stagnatie van overdracht van nazorgverplichtingen in het bijzonder. De huidige (IPO-) modellen voor de berekening van nazorgkosten en – risico’s voldoen goed voor Wm-stortplaatsen (dat wil zeggen voor goed gedefinieerde IBC-systemen), maar bieden geen oplossing voor meer complexe situaties. Dit komt doordat de technische risico’s moeilijk zijn te bepalen en te kwantificeren; niet-technische risico’s een veel grotere rol lijken te spelen. 

Deze situatie rond risico’s leidt tot stagnatie van nazorg; er wordt op een niet-eigenlijke wijze omgegaan met risico’s. Door een marsroute voor risico’s te ontwikkelen kan mogelijk deze stagnatie worden opgeheven.  Deze marsroute bestaat uit 5 stappen. Voordat deze marsroute wordt behandeld, wordt onderstaand kort ingegaan op de te beschouwen risico’s.  **Wat voor risico’s?** Over wat voor risico’s praten we? In de studie AltVAR(xii)^ zijn de volgende risicogroepen onderscheiden. A. Technische risico’s bijvoorbeeld als gevolg van bronpluimmaatregelen, het falen van systemen of tegenvallende prognoses van verspreiding B. Juridische risico’s bijvoorbeeld als gevolg van al dan niet terechte claims door derden 


C. Functionele risico’s bijvoorbeeld als gevolg van oneigenlijk gebruik van de locatie (door derden of de reguliere gebruiker) D. Omgevingsrisico’s bijvoorbeeld als gevolg van invloeden of (ruimtelijke) ontwikkelingen op of vanuit omgeving E. Bestuurlijk-juridische risico’s bijvoorbeeld als gevolg van wijzigingen in weten regelgeving of besluiten door de overheid F. Economische risico’s bijvoorbeeld als gevolg van wijzigingen in het beleggingsklimaat of tegenvallende economische ontwikkelingen waardoor druk op het nazorgbudget komt te staan 

In de studie AltVAR wordt meer uitgebreid op de risico’s ingegaan. Tevens wordt aangegeven welke risico’s geringe, matige of omvangrijke financiële gevolgen hebben. 

Het optreden van een ongewenste gebeurtenis (risico) leidt tot een situatie waarbij het milieu wordt bedreigd. Om de situatie vervolgens te herstellen, dienen kosten gemaakt te worden. Deze kosten worden ook wel ‘herstelkosten’ genoemd.  **Hoe marsroute gebruiken?** Onderstaand wordt een marsroute gegeven die kan worden gevolgd om risico’s bij nazorg bodemsanering hanteerbaar te maken. Deze marsroute kan niet alleen worden gebruikt om in de voorbereidingsfase (SO, SP of NZ-plan) tot een risicoreductie te komen (dan is meer sprake van rsiscomanagement) maar ook om ze in onderhandelingsposities bespreekbaar te maken. Immers, er zijn meerdere oplossingen mogelijk om risico’s op te vangen. Het zal blijken dat het niet altijd loont om risico’s bij derden onder te brengen. Ze horen – liefst – te liggen bij de partij die het beste de risico’s in de praktijk beheersbaar kan maken. In geval van onderhandelingsposities verdient het de voorkeur onderstaande stappenplan in een open en transparant proces te doorlopen. Hierdoor worden niet voor de hand liggende toewijzingen van risico’s en te hoge afkoopsommen voorkomen. Op verschillende punten in de marsroute is aangegeven op welke wijze de risico’s op een praktische wijze contant kunnen worden gemaakt; met andere woorden, hoe ze in het rekenmodel nazorgkosten bodemsanering kunnen worden meegenomen.  **Marsroute hanteren risico’s nazorg bodemsanering** Bij het ontwikkelen van deze marsroute is gebruik gemaakt van ervaringen die in andere werkvelden zijn opgedaan met vergelijkbare problematiek (utiliteitsbouw en civiele techniek). De marsroute bestaat uit de volgende stappen: A. Risico-identificatie B. Prioritering van de risico’s C. Schiften van risico’s D. Uitsluiten van risico’s E. Contant maken van risico’s  


**Stap A – Risico-identificatie** De basis voor het bespreekbaar en hanteerbaar maken van risico’s vormt een risicoanalyse; liefst zodanig dat dit een open en transparante communicatie op dit punt mogelijk maakt. Allereerst dienen de risico’s te worden geïdentificeerd – liefst gerubriceerd naar de zes hiervoor genoemde typen risico. Hiervoor zou gebruik kunnen worden gemaakt van bijvoorbeeld:  een checklist of shortlist van de 20 meest voorkomende risico’s per type nazorg: deze bestaat nog niet maar zou aan de hand van de typologie van bijvoorbeeld het rapport IPO BO-19 “Borgingsmogelijkheden nazorg Bodemsanering” (Grontmij, MMG Advies, 2005) kunnen worden opgesteld. In deze rapportage is tevens een ‘ranking’ aangegeven met de mate waarin een bepaald type sanering gevoelig is voor een bepaalde boringmogelijkheid;  een evaluatie van een deskundige; 

 een ervaringsdatabase: een dergelijke database is niet beschikbaar maar zou een waardevolle bijdrage aan de identificatie van risico’s (en kans op voorkomen) kunnen opleveren;  ‘praten met collega’s’: een dagdeel de locatie ‘doorakkeren’ met collega’s levert vaak al een goede dekking van de risico’s op;  Een ‘achterkant sigarendoos’ analyse: met een quick scan is door een ervaren deskundige wellicht al een groot deel van de risico’s inzichtelijk te krijgen.  **Stap B – Prioritering van de risico’s** Als eenmaal de risico’s zijn geïdentificeerd kan worden overgegaan tot het prioriteren van de risico’s. Een instrument om dit in te vullen is door de risico’s te positioneren in de risicomatrix. In deze matrix krijgen de risico’s een plaats naar gelang hun kans van voorkomen en de gevolgen. Onderstaand is ter illustratie een dergelijke matrix gegeven. Het rapport IPO BO-19 geeft een aanzet om tot prioritering van de risico’s te geven. Het rapport is echter niet dekkend voor alle mogelijke voorkomende risico’s. 


        

             

     

         

              _c_   

Bij het nader invullen van deze matrix kan van het volgende stappenplan gebruik worden gemaakt: 

 _Identificatie_ van wat mis kan gaan (zie stap A) (zowel technisch als niet-technisch);  Wat zijn de _gevolgen_ (respons) van het systeem en wat zijn compenserende / corrigerende maatregelen;  Wat zijn de _kosten_ van de compenserende / corrigerende maatregelen;  Wat zijn de verdisconteerde kosten van de compenserende / corrigerende maatregelen, rekening houdend met het _moment_ waarop het systeem faalt;  Wat is de _kans_ dat het systeem faalt en verwerk dit in de verdisconteerde kosten van de compenserende / corrigerende maatregelen. 

**Stap C – Schiften van risico’s** Als eenmaal de risico’s in beeld zijn gebracht kan een eerste schifting worden toegepast. Dit gebeurt aan de hand van de vier verschillende vakken I t/m IV in de risicomatrix. 

_Vak I (kans klein – effect klein)_ Risico’s die in dit vak van risicomatrix staan behoren tot het ‘normaal risico’ van een project. Denk hierbij aan bijvoorbeeld: de kans dat een peilbuis van een omvangrijk monitoringsmeetnet door vandalisme voortijdig dient te worden vervangen. Deze risico’s zijn niet maatgevend. Extra aandacht hieraan besteden is niet productief, verwart de discussie over risico’s en leidt de aandacht af van risico’s die wel van belang zijn om nader aandacht te geven. 

Een wijze om deze risico’s hanteerbaar te maken – en die doorgaans al wordt gehanteerd in contracten – is door deze in de normale ‘winst / risico’-post op te nemen van het werk. 

_Vak II (kans groot – effect klein)_ Risico’s die in dit vak van risicomatrix staan worden mogelijk veroorzaakt door een ‘gevoelig’ nazorgsysteem. 

I (^) II III (^) IV 


Denk hierbij aan bijvoorbeeld: de kans dat een peilbuis van een omvangrijk monitoringsmeetnet door vandalisme regelmatig dient te worden vervangen. Deze risico’s zijn niet maatgevend. Extra aandacht hieraan besteden is tot op zekere hoogte – voor wat betreft het risicoprofiel van de nazorglocatie – niet productief; immers de gevolgen zijn klein en daarmee niet maatgevend voor het totale risicobedrag. 

Het is een overweging waard een ‘kansreductie’ (zie figuur 2) toe te passen waardoor het risico van vak II naar vak I zal verschuiven. De kosten van deze reductie dient in verhouding te staan met de gevolgen. Veelal zal deze kansreductie leiden tot een meer robuuste nazorg maar niet tot een significant andere kosten voor de nazorg in totaliteit. In aansluiting op het voorbeeld kan de desbetreffende peilbuis op een minder ‘gevoelige’ locatie worden geplaatst of worden voorzien van een vandalismebestendige behuizing. 

Als niet voor een kansreductie wordt gekozen, kunnen de risico’s uit vak II hanteerbaar worden gemaakt door op de specifieke kostenposten met grote kans en klein effect een geringe risico-opslag toe te passen. Hiertoe kan worden volstaan met een vooraf vastgesteld opslagpercentage (op basis van bijvoorbeeld een vuistregel, checklist of ervaringscijfers). Het is niet de moeite waard (in relatie tot de andere vakken) om hier veel langer bij stil te staan.  _Vak III (kans klein – effect groot)_ Risico’s die in dit vak van risicomatrix staan zijn de moeite waard om nader te beschouwen. Denk hierbij aan bijvoorbeeld: de kans dat een grondwaterverontreiniging ontstaat door een tegenvallende nalevering van de bron. Deze risico’s kunnen maatgevend zijn. Extra aandacht hieraan besteden is 

- voor wat betreft het risicoprofiel van de nazorglocatie – productief; im- mers de gevolgen zijn groot en daarmee mogelijk maatgevend voor het totale risicobedrag. Er zijn meerdere oplossingen om met deze risico’s om te gaan:  Gevolgreductie;  Risicobepaling;  Verzekeren. 

Het is een overweging waard een ‘gevolgreductie’ (zie figuur 2) toe te passen waardoor het risico van vak III naar vak I zal verschuiven. De kosten van deze reductie dient in verhouding te staan tot de gevolgen. Veelal zal deze gevolgreductie leiden tot een meer robuuste nazorg maar niet tot significant andere kosten voor de nazorg in totaliteit. In aansluiting op het voorbeeld kan een monitoringssysteem met een vooraf bepaalde betrouwbaarheid (FEB-systematiek) worden toegepast of het interceptiesysteem voor de nog te ontwikkelen grondwaterpluim vast worden aangelegd waarmee snel kan worden ingegrepen. 


Als niet voor een gevolgreductie wordt gekozen, kunnen de risico’s uit vak III hanteerbaar worden gemaakt door een ‘risicobepaling’: per ongewenste gebeurtenis de kans op optreden te bepalen en de kosten van de gevolgen (risico = kans x gevolg). Hiertoe kan niet worden volstaan met een vooraf vastgesteld opslagpercentage (op basis van bijvoorbeeld een vuistregel, checklist of ervaringscijfers); immers de gevolgen kunnen maatgevend zijn. De analyse van de kans en gevolgen is werk voor deskundigen. Mogelijk dat wel gebruik kan worden gemaakt van vuistregels – in aansluiting op het voorbeeld – voor wat betreft de kosten van een grondwatersanering van een bepaalde omvang. 

Indien een statistisch onderbouwde waarde voor het risicobedrag is gewenst kan deze worden bepaald met een probabilistisch model. Zo kan met bijvoorbeeld 95% betrouwbaarheid de hoogte van het te reserveren risicobedrag worden vastgesteld. Voor meer achtergronden zie het tekstblok op blz 9. Er zijn in de markt productenbeschikbaar om het probabilistische model te implementeren (denk aan het risico-model bij RINAS of “Crystal Ball”). Vóórdat hierin een verdiepingsslag wordt gemaakt dient eerst te worden aangegeven of het überhaupt wenselijk is een statistisch onderbouwde waarde voor het risicobedrag te bepalen. Hierbij spelen meerdere aspecten een rol als bruikbaarheid in de praktijk, waarde van de uitkomsten, complexiteit van de methodiek, alternatieven. 

                    ! "    #          $  %   &  '    ( #) %*     % #    #                  %  +   #              ,              '     +     %  *#             * #    #     $   -$   . / 01          ! "    *      2                  (     #       )  Ook valt te overwegen om het risico te verzekeren bij een externe partij (verzekeraar). De risicopremie kan worden ingebracht in de kostenraming van de nazorgkosten. 

_Vak IV (kans groot – effect groot)_ In principe kan net als bij vak III het risico worden vastgesteld ( _risico = kans x gevolg_ ). Aangezien dit veelal tot onacceptabele risico’s leidt, zal men al snel tot de conclusie komen dat risico’s die in dit vak van risicomatrix staan eigenlijk niet zouden mogen voorkomen; niet alleen uit oogpunt van bestendigheid van de technische oplossing maar ook uit oogpunt van bestendigheid van de beheerorganisatie. 


Ze verdienen zonder meer bijzondere aandacht omdat ze maatgevend zijn. 

Er zijn meerdere oplossingen om met deze risico’s om te gaan.  Aanpassing van de nazorgmaatregelen: een ‘gevolgreductie’ én ‘kansreductie’ toepassen. Dit zal al snel kosteneffectief blijken te zijn. Het risico zal naar de vakken I, II of III moeten verschuiven. Voor de wijze waarop vervolgens met het restrisico wordt omgegaan wordt verwezen naar wat onder het desbetreffende vak is aangegeven.  Bewust het risico nemen en garantstelling voor een terugvalscenario regelen. Deze aanpak zal een wezenlijk onderdeel van de beschikking zijn. In het SKB-project FEB(5)^ is een werkwijze ontwikkeld om deze aanpak procesmatig hanteerbaar te maken. 

 Onderbrengen van het risico bij een externe partij (verzekeraar). De risicopremie kan worden ingebracht in de kostenraming van de nazorgkosten.  Uitsluiten (zie verderop).  Als dit alles niet mogelijk is: treffen van aanvullende sanerende maatregelen resulterend in een meer nazorgloze situatie en reductie van de risico’s.          

             

     

         

            _Figuur 2 Kansreductie en gevolgreductie_ 

**Stap D Uitsluiten risico’s** Naast de in stap C beschreven gebeurtenissen, welke als voorzienbare risico’s beschouwd kunnen worden, kunnen ook onvoorzienbare risico’s worden onderscheiden. 

Indien deze gebeurtenissen liggen binnen de scope van de nazorg – of afkoopsom – kunnen deze worden uitgesloten van verrekening in het risicobedrag. Ofwel omdat de hiermee gepaard gaande kosten onder een ander regime verhaald kunnen worden ofwel omdat dat de betreffende gebeurtenissen niet thuishoren bij de inschatting van het risicobedrag. Voorbeelden hiervan zijn het optreden van een aardbeving (schade zal worden gedekt door het Rijk) of een neerstortend vliegtuig (aansprakelijkheidsverzekering van een vliegtuigmaatschappij). Indien onvoorzienbare risico’s toch binnen de afkoopsom van de nazorgkosten dienen te worden opgenomen, zal het in de praktijk neerkomen op maatwerk en – in geval van een mogelijke overdracht – onderhandeling tussen de partijen die de overdracht van de nazorg willen overeenkomen. Dergelijk maatwerk valt buiten de scope van deze marsroute. 

 Maatregel met gevolgreductie Maatregel met kansreductie 


Ook voor voorzienbare risico’s uit vak IV kan worden overwogen deze uit te sluiten en niet mee te nemen in de kostenraming. In geval van overdracht van de nazorg vallen dergelijke risico’s buiten de afkoopsom en blijven ze liggen bij de geadresseerde van de beschikking op de nazorg. Redenen om voor een dergelijke aanpak te kiezen zijn bijvoorbeeld. 

 Het afkoopbedrag is dermate hoog dat de initiatiefnemer het risico liever bij zich houdt;  De risico’s zijn niet beheersbaar door de partij die wordt gevraagd ze over te nemen. Risico’s zijn het best beheersbaar bij partijen die de mogelijkheid hebben ze te beïnvloeden en er qua logistiek, positie of expertise redelijkerwijs verantwoordelijkheid voor kunnen nemen. 

Door op een transparante wijze onderling over deze risico’s te praten, kan een voor de betrokken partijen een gunstige allocatie van risico’s mogelijk worden gemaakt. Belangen en posities van betrokken partijen kunnen mede bepalend zijn voor de wijze waarop de risico’s worden geallokeerd. 

**Stap E Contant maken risico** In stap C is aangegeven op welke wijze risico’s contant kunnen gemaakt. In figuur 3 is samengevat _de wijze waarop risico’s in een rekenmodel nazorgkosten bodemsanering kunnen worden ingebracht_. In de figuur is ervan uitgegaan dat maatregelen als kanen gevolgreductie of het treffen van aanvullende sanerende maatregelen al zijn doorgevoerd.          

     $        3   %  

           *          *      &  #  *#              4     (5 2 )  6        7  0    8%     0  6 %      %                1      7  

  9     6 %      %                /  %                '     (      ) 

 _Figuur 3 Wijze van contact maken van risico_ 


**Risicoanalyses in de praktijk** Er is nog weinig ervaring in de praktijk met het analyseren van risico’s van nazorglocaties en het contant maken daarvan. Een uitzondering daarop vormt de aanpak van grote locaties. De kennis van risicoanalyse is veelal zeer beperkt. Daardoor wordt het omgaan met risico's als lastig en bedreigend ervaren. De toepassing van ‘lastige modellen’(denk aan RINAS) maakt deze discussie er niet eenvoudiger op, maar geeft wel enige houvast. 

De blinde vlek bij het uitvoeren van risicoanalyses is het ontbreken van (praktijk)ervaring. Hiervoor zijn de volgende redenen aan te geven: 

1. Er is in de praktijk nog onvoldoende ervaring opgedaan met de risico- aspecten van nazorg. 

2. Opgedane ervaring wordt niet op een systematische wijze vastgelegd en voor derden beschikbaar gesteld. 

3. Bepaalde risico’s hebben zich in de praktijk nog niet voorgedaan. Zo is bijvoorbeeld de vervangingstermijn van stalen damwanden als onder- deel van een IBC-systeem in geen van de geïnstalleerde systemen in Ne- derland nog verstreken. 

4. Er is geen onderzoek uitgevoerd (dan wel bij de auteur bekend) met betrekking tot de levensduur van systeemonderdelen. 

Een risicoanalyse is van bijzonder belang in geval sprake is van een afkoopsituatie. In geval van afkopen van risico’s zijn de uitkomsten van een risicoanalyse niet heiligmakend. De uitkomsten van een dergelijke analyse zullen hooguit een uitgangspunt vormen van onderhandelingen in het overnametraject. Het is daarom niet functioneel te streven ‘het enige en juiste risicobedrag’ te kunnen berekenen. 

Een aantal risico’s is lastig te benoemen. Denk hierbij aan bijvoorbeeld economische en bestuurlijk-juridische risico’s. In voorkomende gevallen zal bewust voor een meer kostbare nazorgloze oplossing worden gekozen of deze door het bevoegd gezag worden vereist. 

In situaties dat sprake is van afkoop van nazorgrisico’s zullen deze risico’s: 

1. door aanvullende maatregelen worden verkleind. Denk hierbij naast technische oplossingen ook aan meer toezicht door derden of door (semi) publieke (overheids)organen. 


2. worden uitgesloten door de partij die de nazorg overneemt. Dan is echter geen sprake van volledige overname van de nazorgverantwoorde- lijkheid. 

3. door een niet kwantitatief onderbouwde hoge afkoopsom worden ver- disconteerd. 

4. Worden verdisconteerd met minder risicovolle nazorglocaties in de nazorgportefeuille van de nazorgorganisatie. 

Een mogelijke oplossing voor het met meer vertrouwen omgaan van risico’s bij nazorglocaties, is het uitwerken en beschikbaar stellen van een aantal karakteristieke voorbeelden. Deze kunnen als sjabloon worden gehanteerd voor de analyse van risico’s op andere locaties. Hierin schuilt wel het gevaar dat deze voorbeelden te veel als standaard worden gezien. Op basis van de uitgewerkte karakteristieke voorbeelden zou daarom moeten worden beoordeeld in hoeverre deze voldoende generiek zijn voor toepassing in algemene zin. 



 74 

#####  

##### "%2 

##### 64 

##### ) 

#####  

#####  

#####   

##### + 

#####  

#####  


"&2, 

(^1) [http://www.nazorgstortplaatsen.nl/](http://www.nazorgstortplaatsen.nl/) (^2) ROSA, Praktijkdocument voor het maken van keuzes bij mobiele verontreinigingen, SKB, september 2004. (^3) “Borgingsmogelijkheden nazorg bodemsanering”, Grontmij en MMG Advies bv, IPO, BO-19, 2005-09-12 (^4) Evaluatie Bodemsanering, Analyse landsdekkend beeld, 3B Bureau Bodem en milieubeleid, 24 augustus 2005 (^5) Handleiding Flexibele Emissiebeheersing, CUR/NOBIS, 97-2-01 / 981-02, GeoDelft en Grontmij, april 2000 (^6) IBC en nazorg door Flexibele Emissie Beheersing, eindrapport, CO-370130/150, november 1997 (^7) “Case Based Reasoning, hidden soil knowledge unveiled; Learning from finished in-situ remediation projects”, SKB, SV-613, 2004 viii (^) Circulaire Saneringsregeling Wet Bodembescherming, Beoordeling en afstemming, 19 december 1997 ix (^) Handleiding afwegingsproces saneringsdoelstelling, SDU, 2000 x Besluit financiële bepalingen bodemsanering. Artikel 39 van het Besluit van 15 december 2005, uitvoering financiële bepalingen WBB (staatsblad 2005, 681), hoofdstuk 6: financiële zekerheid xi (^) Gezamenlijk Bodemsaneringsbeleid Den Haag, Dordrecht, Leiden, Rotterdam, Schiedam, Zuid-Holland, provincie Zuid-Holland, 2003 xii (^) Allocatie van lange termijn Verantwoordelijkheid, Aansprakelijkheid en (Rest)risico’s, SKB, juni, 2005 


