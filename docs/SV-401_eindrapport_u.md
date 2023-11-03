H. van Dokkum E. v.d. Hoek P. Middeldorp H. Rijnaarts F. Roelofsen N. de Rooij J. Smits S. Staps J. Valstar 

October 2003 

Gouda, SKB 

##### Stichting Kennisontwikkeling Kennisoverdracht Bodem 

## SV-401 

## NA Interface: 

## Natural Attenuation of oxidisable organic 

## pollutants at the Interface between 

## groundwater and surface water 

 Phase 1 


**Auteursrechten** Alle rechten voorbehouden. Niets uit deze opgave mag worden verveelvoudigd, opgeslagen in een geautomatiseerd gegevensbestand of openbaar gemaakt, in enige vorm of op enige wijze, hetzij elektronisch, mechanisch, door fotokopieën, opnamen of op enige andere manier, zonder voorafgaande schriftelijke toestemming van SKB. Het is toegestaan overeenkomstig artikel 15a Auteurswet 1912 gegevens uit deze uitgave te citeren in artikelen, scripties en boeken mits de bron op duidelijke wijze wordt vermeld, alsmede de aanduiding van de maker, indien deze in de bron voorkomt, "©"NA Interface: Natural Attenuation of oxidisable organic pollutants at the Interface between groundwater and surface water", oktober 2003, SKB, Gouda." 

**Aansprakelijkheid** SKB en degenen die aan deze publicatie hebben meegewerkt, hebben een zo groot mogelijke zorgvuldigheid betracht bij het samenstellen van deze uitgave. Nochtans moet de mogelijkheid niet worden uitgesloten dat er toch fouten en onvolledigheden in deze uitgave voorkomen. Ieder gebruik van deze uitgave en gegevens daaruit is geheel voor eigen risico van de gebruiker en SKB sluit, mede ten behoeve van al degenen die aan deze uitgave hebben meegewerkt, iedere aansprakelijkheid uit voor schade die mocht voortvloeien uit het gebruik van deze uitgave en de daarin opgenomen gegevens, tenzij de schade mocht voortvloeien uit opzet of grove schuld zijdens SKB en/of degenen die aan deze uitgave hebben meegewerkt. 

**Copyrights** All rights reserved. No part of this publication may be reproduced, stored in a retrieval system, or transmitted, in any form or by any means, electronic, mechanical, photocopying, recording and/or otherwise, without the prior written permission of SKB. It is allowed, in accordance with article 15a Netherlands Copyright Act 1912, to quote data from this publication in order to be used in articles, essays and books, unless the source of the quotation, and, insofar as this has been published, the name of the author, are clearly mentioned, "©"NA Interface: Natural Attenuation of oxidisable organic pollutants at the Interface between groundwater and surface water", October 2003, SKB, Gouda, The Netherlands." 

**Liability** SKB and all contributors to this publication have taken every possible care by the preparation of this publication. However, it can not be guaranteed that this publication is complete and/or free of faults. The use of this publication and data from this publication is entirely for the user's own risk and SKB hereby excludes any and all liability for any and all damage which may result from the use of this publication or data from this publication, except insofar as this damage is a result of intentional fault or gross negligence of SKB and/or the contributors. 


 I 

**Report title SKB report number** NA-Interface: Natural Attenuation of oxidisable organic SV-401 contaminants at the Interface between groundwater and surface water **Project report number** SV-401 

**Author(s) Number of pages** P. Middeldorp **Report:** 117 S. Staps **Appendices:** 6 H. Rijnaarts H. van Dokkum J. Smits J. Valstar N. de Rooij F. Roelofsen E. v.d. Hoek 

**Executive organisation(s) (Consortium)** TNO-MEP (P. Middeldorp, S. Staps, H. Rijnaarts, H. v. Dokkum, 055 5493493) TNO-NITG (J. Valstar, F. Roelofsen, 030 256 4707) WL | Delft Hydraulics (J. Smits, N. de Rooij, 015 285 8755) Geodelft (E. v.d. Hoek, 015 269 3500) 

**Publisher** SKB, Gouda 

**Abstract** The policy in soil remediation for mobile contaminants in the Netherlands consists of cost effective removal. There are strong indications that the interface between groundwater and surface water can play an important role in the natural degradation of organic contaminants (NA-interface). This is especially the case for mobile contaminants or degradation products that are persistent in anaerobic (subsurface) environments, but can be degraded more easily under oxidized environmental conditions (e.g. monochlorobenzene and the light mineral oil fraction). Three industrial sites were selected in The Netherlands. The project’s starting point is that the surface water is regarded as an object of risk and not as a reactor. On the basis of a previously developed conceptual model of the NA-interface processes, quantitative models describing these processes and the processes in the adjoining subsoil and surface water was performed using the following model codes CHARON and RT3D. Due to the relatively low resolution of the developed sampling method, the results of the measurements were considered not yet suitable to draw conclusions concerning the contribution of the NA-interface to removal processes. Therefore, the measured values were only used for boundary values for the models. Future research will focus on the quantification of biological degradation of contaminants in the interface. 

**Keywords Controlled terms Uncontrolled terms** biodegradation, chlorobenzene, groundwater interface, sediment models, surface water 

**Project title Projectmanagement** NA-Interface: Natural Attenuation of oxidisable TNO-MEP organic contaminants at the Interface between (Ing. J.J.M. Staps, 055 5493493) groundwater and surface water 

This report can be obtained by: SKB, PO Box 420, 2800 AK Gouda, The Netherlands Netherlands Centre for Soil Quality Management and Knowledge Transfer (SKB) 


 II 

**Titel rapport SKB rapportnummer** NA-grensvlak: Natuurlijke Afbraak van oxideerbare SV-401 organische verontreinigingen in het grensvlak tussen gronden oppervlaktewater **Project rapportnummer** SV-401 

**Auteur(s) Aantal bladzijden** P. Middeldorp **Rapport:** 117 S. Staps **Bijlagen:** 6 H. Rijnaarts H. van Dokkum J. Smits J. Valstar N. de Rooij F. Roelofsen E. v.d. Hoek 

**Uitvoerende organisatie(s) (Consortium)** TNO-MEP (P. Middeldorp, S. Staps, H. Rijnaarts, H. v. Dokkum, 055 5493493) TNO-NITG (J. Valstar, F. Roelofsen, 030 256 4707) WL | Delft Hydraulics (J. Smits, N. de Rooij, 015 285 8755) Geodelft (E. v.d. Hoek, 015 269 3500) 

**Uitgever** SKB, Gouda 

**Samenvatting** Het Nederlandse bodemsaneringsbeleid ten aanzien mobiele verontreinigingen richt zich op kosteneffectieve verwijdering. Er zijn sterke aanwijzingen dat het grensvlak tussen gronden oppervlaktewater een belangrijke rol kan spelen bij de natuurlijke afbraak van organische verontreinigingen (NA-grensvlak). Dit is met name het geval voor mobiele verontreinigingen of afbraakproducten die slecht afbreekbaar zijn in anaërobe milieu-omstandigheden, maar die beter kunnen worden afgebroken in geoxideerde milieus (bijvoorbeeld monochloorbenzeen en de lichte fractie van minerale olie). Het project is gericht op natuurlijke afbraakprocessen in het grensvlak van gronden oppervlaktewater. Als uitgangspunt is gehanteerd dat het oppervlaktewater wordt beschouwd als een bedreigd object. Drie Nederlandse locaties zijn geselecteerd voor het onderzoek. De grensvlakken op deze locaties betroffen twee getijdesystemen en een statisch systeem.Op basis van het ontwikkelde conceptueel model van de NA-grensvlakprocessen zijn deze processen en die in de ondergrond en het oppervlaktewater gemodelleerd door middel van de model codes CHARON en RT3D. Voor de grondwaterbemonstering in het grensvlak van gronden oppervlaktewater is een nieuwe methode ontwikkeld en toegepast. Vanwege de lage resolutie van deze bemonsteringsmethode waren de metingen nog niet voldoende geschikt om conclusies te trekken met betrekking tot de bijdrage van het NA-grensvlak aan het verwijderingsproces. Daarom zijn de gemeten waarden alleen gebruikt als grenswaarden voor de modellen. Vervolgonderzoek zal worden gericht op het kwantificeren van biologische afbraak van verontreinigingen in het grensvlak. 

**Trefwoorden Gecontroleerde termen Vrije trefwoorden** biologische afbraak, chloorbenzeen, grondwatermodellering, grensvlak, sediment chloorethenen, grondwater, modellen, oppervlaktewater 

**Titel project Projectleiding** NA-grensvlak: natuurlijke afbraak van oxideerbare TNO-MEP organische verontreinigingen in het grensvlak (Ing. J.J.M. Staps, 055 5493493) van gronden oppervlaktewater 

Dit rapport is verkrijgbaar bij: SKB, Postbus 420, 2800 AK Gouda 


 III 

###### INHOUD 

 SUMMARY..................................................................................... V 

 SAMENVATTING........................................................................ VIII 

Chapter 1 INTRODUCTION .......................................................................................... 1 

Chapter 2 PROBLEM DEFINITION............................................................................... 4 

Chapter 3 RESEARCH GOALS .................................................................................... 5 

Chapter 4 DIRECTIONS FOR SOLUTIONS ................................................................. 6 

Chapter 5 ACTIVITIES AND INTENDED RESULTS..................................................... 7 

Chapter 6 LITERATURE DATA AND PRELIMINARY EXPERIMENTS ........................ 8 6.1 Aerobic degradation of oxidisable organic pollutants ..................... 8 6.2 Determination of the rate constant for aerobic MCB degradation at the Solvay site........................................................ 8 

Chapter 7 CONCEPTUAL MODEL AND HYPOTHESIS BUILDING........................... 10 7.1 Approach from surface water to sediment ................................... 10 7.1.1 Methodology ................................................................................ 10 7.1.2 The natural system studied .......................................................... 12 7.2 Conceptual model from groundwater to sediment........................ 18 7.2.1 The system studied...................................................................... 18 7.2.2 Model used .................................................................................. 19 

Chapter 8 RESEARCH SITES .................................................................................... 21 8.1 Characteristics ............................................................................. 21 8.1.1 Listing essential characteristics.................................................... 21 8.1.2 BP site, Ghent, Belgium............................................................... 21 8.1.3 Shell Netherlands Refinery/Chemistry, Hoogvliet Rotterdam, The Netherlands .......................................................................... 21 8.1.4 Huntsman, Rotterdam Rozenburg, The Netherlands ................... 21 8.1.5 Solvay Pharmaceuticals, Amsterdam, The Netherlands .............. 21 8.1.6 LBC, Pernis, The Netherlands ..................................................... 22 8.2 Selection ...................................................................................... 22 8.3 Hypothesis NA-interface per site.................................................. 23 

Chapter 9 SAMPLING TOOLS.................................................................................... 24 9.1 Existing tools................................................................................ 24 9.1.1 Peeper ......................................................................................... 24 9.1.2 Environfilters ................................................................................ 24 9.2 Tools developed within the project............................................... 25 9.2.1 Multilevel sampling device ........................................................... 25 9.2.2 Control buckets ............................................................................ 25 


 IV 

Chapter 10 METHODOLOGY SITE INVESTIGATIONS ............................................... 27 10.1 Field measurements .................................................................... 27 10.2 Chemical analyses....................................................................... 27 10.2.1 Water samples ............................................................................. 27 10.2.2 Soil samples................................................................................. 28 10.3 Ecotoxicological investigations..................................................... 28 

Chapter 11 SITE INVESTIGATIONS ............................................................................ 33 11.1 Solvay site.................................................................................... 33 11.1.1 Geohydrological modelling........................................................... 33 11.1.2 Sampling methodology................................................................. 37 11.1.3 Results ......................................................................................... 38 11.1.4 Ecotoxicological assessment ....................................................... 41 11.2 LBC site ....................................................................................... 43 11.2.1 Geohydrological modelling........................................................... 43 11.2.2 Sampling methodology................................................................. 48 11.2.3 Results ......................................................................................... 48 11.2.4 Ecotoxicological assessment ....................................................... 50 11.3 Shell site ...................................................................................... 53 11.3.1 Geohydrological modelling........................................................... 53 

Chapter 12 MODEL INVESTIGATIONS........................................................................ 57 12.1 Approach model CHARON .......................................................... 57 12.1.1 Introduction .................................................................................. 57 12.1.2 Criteria for model formulation....................................................... 57 12.1.3 Description of CHARON............................................................... 59 12.1.4 Description of DELWAQ .............................................................. 64 12.1.5 Model investigations with CHARON............................................. 72 12.1.6 Model investigations with DELWAQ............................................. 79 12.1.7 Conclusions and discussion......................................................... 83 12.2 Approach model RT3D................................................................. 85 12.2.1 The chemical reaction model ....................................................... 85 12.2.2 Application of the model............................................................... 88 12.2.3 Conclusions and discussion....................................................... 107 

Chapter 13 GENERAL CONCLUSIONS PHASE 1 ..................................................... 108 

Chapter 14 RECOMMENDATIONS PHASE 1 ............................................................ 110 

 REFERENCES .......................................................................... 114 

Appendix A CONVERSION OF THE APPARENT BIODEGRADATION RATE CONSTANT FROM BATCH SYSTEMS TO WATER SATURATED SOIL 

Appendix B SITE CHARACTERISTICS FOR SITE EVALUATION 

Appendix C SOIL CORE SAMPLE ANALYSES 


 V 

###### SUMMARY 

 NA Interface: Natural Attenuation of oxidisable organic pollutants at the Interface between groundwater and surface water 

The policy in soil remediation in the Netherlands concerning mobile contaminants consists of cost effective removal strategies. This results often in active removal of the source of the contamination and treatment of the plume. In this approach, natural processes play an increasing role. Important aspects are objects of risk, which are often surface water systems like rivers, canals and harbours. In many situations, especially in river delta regions, the source area is situated close to the surface water, to which the plume moves and the groundwater is being discharged. The current situation is that relatively intensive and long lasting clean-up methods are used (e.g. pump and treat), to prevent any contamination from reaching the surface water. There are strong indications that the interface between groundwater and surface water can play an important role in the natural degradation of organic contaminants (NA-interface). This is especially the case for mobile contaminants or degradation products that are persistent in anaerobic (subsurface) environments, but can be degraded more easily under oxidized environmental conditions (e.g. monochlorobenzene, vinyl chloride, MTBE, light mineral oil fraction). Previous investigations have indicated indirectly that NA-interface processes contribute to a reduction of contaminant flux into surface water systems. Until now, no straightforward assessment and quantification of these processes have been performed. In the Netherlands, present water policy is oriented at zero emission towards surface water systems. Regulation based on maximum allowable contaminant influx into water systems is not yet available. 

An NA-interface project has been defined, focussed on NA-processes in the interface between groundwater and surface water. Three project phases are foreseen: respectively conceptual model and indicative measurements, optimisation modelling and increasing the number of industrial sites. 

This first project phase was carried out by TNO-MEP, TNO-NITG, WL|Delft Hydraulics and Delft Geotechnics. The aim was to gain more understanding of the occurrence of NA-interface processes and to quantify their contribution to emission reduction towards the surface water system. In case of a substantial contribution an additional aim was to promote application of NAinterface as part of a cost-effective integrated environmental management system for contaminated sites and surrounding water bodies. The project’s starting point is that the surface water is regarded as an object of risk. Thus, the interface should eliminate contaminants by natural occurring processes, thereby protecting the aquatic ecosystem. 

Three industrial sites in The Netherlands were selected for site investigations and for the development and application of high-resolution monitoring instruments and modelling procedures. The groundwater surface water interfaces at these sites can be divided into two tidal systems and one steady state system. A new tool was developed and applied for sampling groundwater with high resolution in the interface between groundwater and surface water. Also existing tools (monitoring wells, environfilters) were applied for measuring NA-interface gradients in the field. Using these tools, the NA-interface gradients for contaminants and macrochemical parameters were identified in the steady state interface system. Due to the low resolution of the sampling at the tidal interface system, the results of the measurements were considered not sufficiently reliable and suitable for drawing conclusions 


 VI 

concerning the occurrence of NA-interface processes. Therefore, the measured values were only used for boundary values to be introduced in the models. 

On the basis of the developed conceptual model of the NA-interface processes, quantitative models describing these processes and the processes in the adjoining subsoil and surface water was performed using the model codes CHARON, DELWAQ and RT3D. From the modelling it appeared that diffusion/dispersion alone gave a relatively large contribution to the decrease of the upwelling pollutant concentration at the sediment-water interface. The data obtained in the field on pollutant concentration profiles cannot be used to determine the biodegradation. Therefore, the degradation rate constants were determined in laboratory experiments. This was performed in batch tests for monochlorobenzene with sediment from the steady state system. 

Related to the interface, dispersivity reduces contaminant concentrations but not the contaminant flux, whereas biodegradation influences both contaminant flux and, relatively limited compared to dispersivity, contaminant concentrations. 

Modelling several scenarios for oxygen consumption of the sediment, dispersivity and biodegradation rate constants showed that the additional concentration decrease due to biodegradation is small compared to the concentrations in the upwelling groundwater at the lower boundary of the active sediment layer. Quite a different picture arises for the flux of micropollutants that enter the surface water through the sediment-water interface. Dispersion alone does not reduce the pollutant flux that is conveyed to the top sediment by groundwater. The models showed that the flux entering the surface water could be substantially reduced by biodegradation. Depending on the presence of favourable biodegradation conditions, the flux reduction percentage might be more than 95%. However, such optimal conditions are probably not present at most contaminated sites. The reduction percentage may be virtually equal to nil at very unfavourable conditions (e.g. high outflux rate) or when the maximal degradation rate is small. 

A crucial factor is the penetration depth of dissolved oxygen, since the degradation of the relevant pollutants requires oxygen. The penetration depth is maximal for sediments with low oxygen consumption, high dispersion and low upwelling groundwater velocity. The magnitude of the sediment oxygen consumption depends on several parameters, which vary over the seasons. A high upwelling velocity of groundwater is negative with respect to the degradation potential of the sediment-water interface, because this causes small residence times in the oxygen containing top layer. Moreover, the oxygen consumption may be raised by the presence of reduced substances such as ammonium, sulphide, iron(II) and methane in the groundwater. The presence of tidal movement of water enhances degradation when combined with a low net groundwater upwelling velocity and with adsorption. 

The interface between surface water and groundwater for non-tidal **_steady state flow systems_** is relatively thin. The estimates of the thickness of the interface vary between 1 mm and 1.5 cm for oxygen penetration depth. The decrease of the contaminant concentration when approaching the surface water is mainly due to dispersion. In **_tidal systems_** , a relatively thick interface may exist. It strongly depends on the amount of water that infiltrates during high tide. In the pilot study, the modelled thickness of the interfaces was approximately 2 – 6 cm. In such systems, biodegradation of micropollutants can be substantial if the pollutant strongly adsorbs to the soil material. Various measures can be considered to improve the influence on the NA-interface. These measures focus on enlargement of the residence time of the contaminants in the interface. In tidal systems, it is possible to cover the banks with a material that strongly retards the organic 


 VII 

contaminants to provide a better and prolonged mixing of aerobic water and the contaminant. In non-tidal systems, the surface water level can be changed periodically in order to obtain infiltration of aerobic water during part of the time. 

Research in phase 2 will focus on the quantification of biological degradation of contaminants in the interface, either in the laboratory or, preferentially, under field conditions. This will form the basis for determining a possible position of NA-interface processes within the framework of management systems for contaminated sites and for more cost-effective and sustainable remedial actions. 


 VIII 

###### SAMENVATTING 

 NA-Grensvlak: Natuurlijke Afbraak van oxideerbare organische verontreinigingen in het grensvlak tussen gronden oppervlaktewater 

Het Nederlandse bodemsaneringsbeleid ten aanzien van mobiele verontreinigingen richt zich op kosteneffectieve verwijdering. Dit resulteert vaak in actieve verwijdering van de verontreinigingsbron en behandeling van de -pluim. De laatste jaren neemt de rol van natuurlijke afbraakprocessen hierbij toe. Belangrijke aspecten zijn bedreigde objecten, welke vaak oppervlaktewatersystemen zijn, zoals rivieren, kanalen en havens. In veel situaties, met name bij rivierdelta’s, bevindt de verontreinigingsbron zich dicht bij het oppervlaktewater en verspreidt de pluim zich in die richting. Om te voorkomen dat verontreinigingen het oppervlaktewater bereiken worden relatief intensieve en langdurige saneringsmethoden toegepast (bijvoorbeeld _pump and treat_ ). 

Er zijn sterke aanwijzingen dat het grensvlak tussen gronden oppervlaktewater een belangrijke rol kan spelen bij de natuurlijke afbraak van organische verontreinigingen (NA-grensvlak). Dit is met name het geval voor mobiele verontreinigingen of afbraakproducten die slecht afbreekbaar zijn in anaërobe milieu-omstandigheden, maar die beter kunnen worden afgebroken in geoxideerde milieus (bijvoorbeeld monochloorbenzeen, vinylchloride, MTBE en de lichte fractie van minerale olie). Er zijn indirecte aanwijzingen uit voorgaand onderzoek dat NA-grensvlakprocessen bijdragen aan de reductie van de flux van verontreinigingen naar oppervlaktewatersystemen. Tot dusverre zijn deze processen echter nog niet aangetoond en gekwantificeerd. 

In Nederland is het huidige beleid met betrekking tot waterverontreiniging gericht op nul-emissie naar oppervlaktewatersystemen. Weten regelgeving, gebaseerd op maximaal toelaatbare influx van verontreinigingen naar watersystemen, is nog niet beschikbaar. 

Er is een NA-grensvlakproject gedefinieerd, gericht op natuurlijke afbraakprocessen in het grensvlak van gronden oppervlaktewater. Hierin zijn drie projectfasen voorzien: achtereenvolgens conceptueel model en indicatieve meting, optimalisering monitoring en uitbreiding aantal industriële locaties. Voorliggend rapport heeft betrekking op fase 1. Deze eerste projectfase is uitgevoerd door TNO-MEP, TNO-NITG, WL|Delft Hydraulics en Geodelft. Het doel was om inzicht te krijgen in het optreden van NA-grensvlakprocessen en om de bijdrage hiervan aan emissiereductie naar oppervlaktewater te kwantificeren. Indien er een substantiële bijdrage blijkt te zijn, is een aanvullende doelstelling het bevorderen van het toepassen van het NA-grensvlak als onderdeel van een kosten-effectief geïntegreerd milieu-management systeem voor verontreinigde locaties en watersystemen. 

Als uitgangspunt is gehanteerd dat het oppervlaktewater wordt beschouwd als een bedreigd object. Dit betekent dat het grensvlak het aquatisch ecosysteem dient te beschermen door verontreinigingen door middel van natuurlijke processen te verwijderen. 

Drie Nederlandse locaties zijn geselecteerd voor het onderzoek. De grensvlakken op deze locaties betroffen twee getijdesystemen en één statisch systeem. 

Voor de grondwaterbemonstering met hoge resolutie in het grensvlak van gronden oppervlaktewater is een nieuwe methode ontwikkeld en toegepast. Ook bestaande technieken (peilbuizen, milieufilters) werden toegepast om gradiënten in het NA-grensvlak in het veld te meten. Voor het statische systeem zijn gradiënten van verontreiniging en macroparameters vastgesteld. 


 IX 

Vanwege de lage resolutie van de bemonsteringsmethode waren de metingen in het getijdesysteem niet voldoende betrouwbaar en geschikt om conclusies te trekken met betrekking tot het NA-grensvlak. Daarom zijn deze gemeten waarden alleen gebruikt als grenswaarden voor de modellen. 

Op basis van het ontwikkelde conceptueel model van de NA-grensvlakprocessen zijn deze processen en die in de ondergrond en het oppervlaktewater gemodelleerd door middel van de modelcodes CHARON, DELWAQ en RT3D. 

De verkregen velddata van verontreinigingsgradiënten kunnen niet worden gebruikt om de biodegradatie vast te stellen. Daarom zijn afbraakconstantes bepaald in het laboratorium. Dit is uitgevoerd door middel van batch testen voor monochloorbenzeen met bodemmateriaal van het stationaire stysteem. 

Dispersiviteit beïnvloedt de concentraties van verontreinigingen, maar niet de verontreinigingsflux. Biodegradatie beïnvloedt zowel de verontreinigingsflux als, relatief beperkt ten opzichte van dispersiviteit, de concentraties van verontreinigingen. 

Modellering van verschillende scenario’s voor zuurstofconsumptie in het sediment, dispersiviteit en afbraakconstantes geeft aan dat de bijdrage van biodegradatie aan de concentratie-afname van verontreinigingen in het grensvlak klein is. 

Een heel ander beeld wordt verkregen voor de flux van verontreinigingen die door het grensvlak het oppervlaktewater bereikt. Dispersie alleen vermindert de verontreinigingsflux met het grondwater naar de bovenkant van het sediment niet. De modellen laten zien dat de flux naar het oppervlaktewater substantieel kan worden verminderd door biodegradatie. Afhankelijk van de milieu-omstandigheden kan de flux-reductie 95% of meer bedragen. 

Op de meeste verontreinigde locaties zijn zulke optimale omstandigheden echter niet waarschijnlijk; het reductiepercentage kan vrijwel nul zijn bij zeer ongunstige omstandigheden (bijvoorbeeld een hoge stroomsnelheid van het grondwater) of wanneer de afbraaksnelheid laag is. 

Omdat voor de afbraak van de beschouwde verontreinigingen zuurstof nodig is, is de penetratiediepte van opgelost zuurstof een bepalende factor. De penetratiediepte is maximaal voor sedimenten met een lage zuurstofconsumptie, hoge dispersiviteit en lage grondwaterstroomsnelheid. De mate van zuurstofconsumptie in het sediment is afhankelijk van verschillende parameters die variëren over de seizoenen. 

Een hoge grondwaterstroomsnelheid is nadelig met betrekking tot het afbraakpotentieel in het grensvlak, omdat dit korte verblijftijden veroorzaakt in de zuurstofhoudende toplaag. Bovendien kan de zuurstofconsumptie toenemen door de aanwezigheid van gereduceerde componenten, zoals ammonium, sulfide, ijzer(II) en methaan, in het grondwater. Getijde-invloed bevordert afbraak, evenals een lage grondwaterstroomsnelheid (kwel) en adsorptie. 

Het grensvlak tussen gronden oppervlaktewater in **statische systemen** is relatief dun. De schattingen voor de dikte van het grensvlak variëren van 1 mm tot 1,5 cm voor de zuurstofpenetratiediepte. De afname van concentraties van verontreinigingen in het grensvlak wordt hoofdzakelijk veroorzaakt door dispersie. 


 X 

In **getijdesystemen** kan een relatief dik grensvlak aanwezig zijn. Dit hangt sterk af van de hoeveelheid water die tijdens hoog tij infiltreert. In de _pilot study_ was de dikte van het grensvlak ongeveer 2 6 cm. In een dergelijk systeem kan een substantiële mate van biodegradatie van verontreinigingen optreden als de verontreiniging sterk aan bodemmateriaal adsorbeert. 

Voor het bevorderen van de invloed van het NA-grensvlak zijn diverse maatregelen denkbaar. Deze maatregelen richten zich op het vergroten van de verblijftijd van de verontreinigingen in het grensvlak. In **getijdesystemen** is het mogelijk om de oever te bedekken met materiaal, waaraan organische verontreinigingen adsorberen om daarmee een langere en betere menging van aëroob water met de verontreiniging te bevorderen. In **statische systemen** is een mogelijkheid om het niveau van het oppervlaktewater periodiek te wijzigen om daarmee tijdelijke infiltratie van aëroob grondwater te bewerkstelligen. 

Het onderzoek van fase 2 zal zich richten op het kwantificeren van biologische afbraak van verontreinigingen in het grensvlak. Dit kan plaatsvinden in het laboratorium of, bij voorkeur, in het veld. De resultaten zullen de basis vormen voor het vaststellen van de mogelijke positie van NAgrensvlakprocessen binnen het raamwerk van managementsystemen voor verontreinigde locaties en voor meer kosteneffectieve en duurzame saneringsmaatregelen. 


 CHAPTER 1 

###### INTRODUCTION 

Regarding the presence of polluted sites, the current soil policy in the Netherlands is that mobile pollutants shall be cost-effectively removed. The way, in which the source zone and the plume area can be most effectively treated, is crucial for the consideration of the remediation options. The current trend is the active removal of the pollutants from the source zone, combined with a plume treatment based on low intensity techniques, in which naturally occurring processes are becoming more and more important. In many cases, a consideration is made whether and how seriously a specified object is endangered. Such objects are often surface water systems, like rivers, canals and harbours. In many situations, particularly in the Netherlands being a river delta area abounding of water, the pollutant source is located at a relatively short distance from discharging surface water, causing the plume to move in the direction of that water body. Currently, in such occasions an intensive and long-lasting remediation and/or geohydrological control takes place in order to prevent the pollution from entering the surface water system (see figure 1). This practise is caused by the present water policy, oriented at zero emission towards surface water systems. Regulation based on maximum allowable contaminant influx into water systems is not yet available. 

 contaminated groundwater 

 surface water 

 interface 

 oxidisable organic contaminants 

 redox gradient 

Fig. 1. Cross-section of the pollutant plume, the reactive interface and the surface water. 

There are strong indications (a.o. based on the NOBISen SKB-research on the application of micro-aerobic degradation) that the interface between groundwater and surface water can play an important role in the natural attenuation (NA-interface) of organic pollutants [20, 21, 25, 37, 52]. Especially for mobile compounds that are persistent in an anaerobic soil environment but can be easily mineralised under more oxidised conditions, the NA-interface may be an important environment for biodegradation (see figure 2). These are compounds such as benzene, 


monochlorobenzene, vinyl chloride, the light aliphatic fraction of mineral oil, etc. Also, these can be degradation products of natural or stimulated _in situ_ processes. Despite the strong indications with respect to the presence of an NA-interface, sufficient proof for the actual presence and extent of natural attenuation at the mentioned interface has not yet been shown. 

 aerobicaerobic surface water 

 anaerobic groundwater 

 in flux of compounds recalcitrant under anaerobic conditions, including anaerobic biodegradation products of highly chlorinated compounds 

 H+, Cl-^ , CO 2 , H 2 O 

 aerobic biodegradation interface 

 interface 

 micro

 anaerobic groundwater 

 HO Cl Cl 

 (monochloro-benzene) (benzene) 

 (chlorophenol) 

 Cl 

 (vinylchloride) 

 (mobile aliphatics) 

Fig. 2. Schematic reproduction of the NA-interface process, in which the anaerobic (degradation) products are fully mineralised in the (micro-)aerobic interface. The principle of micro-aerobic degradation is also valid for non-chlorinated compounds like aniline, oil compounds, MTBE, etc. 

An NA-interface project as been defined, focussed on NA-processes in the interface between groundwater and surface water. Three project phases are foreseen: respectively conceptual model and indicative measurements, optimisation modelling and increasing the number of industrial sites. 

The research of phase 1, described in this report was carried out by TNO-MEP (leading partner) in co-operation with TNO-NITG, WL/Delft Hydraulics and GeoDelft. 

This project phase has been financed by the executive consortium and the following organisations: 

- Akzo Nobel Chemicals 

- British Petrol 

- Huntsman 

- Nerefco 

- Port of Rotterdam 

- Province of Limburg 

- Solvay Pharmaceuticals 

- Shell Netherlands Refinery/Chemistry 

- Shell Global Solutions 

- SKB 

- Delft Cluster. 


This NA-interface project phase was a cofinancing project for TNO in the EU FW5 project WELCOME (Water, Environment, Landscape Management at Contaminated Megasites). It was agreed with SKB and Delft Cluster that parts of this report are also reported within the framework of the WELCOME project. 


 CHAPTER 2 

###### PROBLEM DEFINITION 

Problem owners, confronted with pollution situations as mentioned above, need applicable extensive remediation measures as well as understanding of the role, which the interface between groundwater and surface water could possibly play. These are on the one hand site owners and port authorities, and on the other hand the entitled authorities and water managers. In the current situation, intensive and/or long-lasting remediation control measures have to be taken, resulting in relatively ineffective source zone measures, high costs, high use of raw materials and interference in natural systems. The expectation is that this will (partly) no longer be necessary when there is more understanding of the potential role of the NA-interface processes. Consequently, this may lead to a reduction of the amount of groundwater to be withdrawn (relation to dehydration problems). Integrating an NA-interface approach in a remediation has the advantage for the problem owner that the total execution of a remediation can become simpler and possibly less expensive. For the authorities it has the advantage that there will be a better integral solution. 


 CHAPTER 3 

###### RESEARCH GOALS 

The aim of this project phase is to get a better understanding of the natural attenuation processes in the interface between groundwater and surface water (NA-interface), in order deploy this knowledge in accordance with a functionally aimed and cost-effective manner for the control of polluted sites. The system definition of the NA-interface is the following: 

The NA-interface is the zone of the soil/surface water partition, in which a redox gradient ranges from strongly negative (methanogenic) to positive (aerobic). Considered are relatively mobile pollutants, such as benzene, monochlorobenzene, the light aliphatic fraction of mineral oil, etc., that are persistent under completely reduced (methanogenic) conditions, but that are biologically degradable with oxygen consumption, possibly also at low oxygen tensions (whether or not in the presence of nitrate and/or sulphate). 

The bottlenecks that have been defined are: 

- there is no understanding of the role of NA-interfaces, and the actual occurrence of the     expected processes; 

- there exist no specific monitoring tools and procedures; 

- there is no perception of the possibilities, boundary conditions and limitations of NA-interface     processes; 

- there is no acceptation by entitled authorities, and still insufficient basis for application in the     soil/water/environment management by site owners. 

To overcome these bottlenecks insight will be gained in: 

- the presence and extent of an interface (redox transition); 

- the dynamics of the interface, due to a) advective transport of water and chemicals resulting     from tidal changes and fluctuating groundwater tables, and b) the changing quality and the     sedimentation of particles (organic matter, sludge) from the overlaying water; 

- the extent of mixing due to tidal changes; 

- the residence time of the pollutant in the interface related to the biodegradation rate; 

- the influence of alternating oxidised and reduced conditions; 

- the dimension of the pollutant flux coming into the overlaying water, considering the     concentration gradient between groundwater and surface water. 

The starting point is that the surface water shall be considered an object to be protected and not to be used as “reactor vessel”. During an effective degradation at the interface, no shift of environmental problems occurs. The pollutant is eliminated through natural processes, thus protecting the aquatic ecosystem. It is expected that the research will be followed by phases focussing on monitoring optimization and extension of the number of industrial sites. 


 CHAPTER 4 

###### DIRECTIONS FOR SOLUTIONS 

To answer the aforementioned research question, the following research approach was used: 

- Demonstration of the occurrence of NA-interface processes, and the quantification of these     on at least two representative industrial sites; 

- The development of monitoring tools and procedures; 

- The determination of the boundary conditions within which NA-interface processes can     occur; 

- The investigation of the aquatic ecosystem to determine whether it is actually protected by     remediation options based on natural attenuation; 

- The fitting into the boundary conditions for water management (e.g. protection of the water     ecosystem), finally leading to a decision system that supports the appropriate application of     NA-interface and that will contribute to acceptation by both entitled authorities and site     owners. 

The underlying concept is the fact that the interface between soil and surface water plays an important role in the natural attenuation (NA-interface) of organic pollutants. Especially for those compounds that are mobile and persistent in anaerobic environments, the more oxidised interface may be an ideal environment for biodegradation. Roughly there are two distinct types of interfaces: 

- Interfaces with a large advective transport, like interfaces with tidal changes in harbours.     Many of the consortium members of this project possess a site at which such interfaces are     present; 

- Interfaces with a small or negligible advective transport, e.g. in rivers and canals. 

In both cases, processes, scale and therefore the measurement setup are different. In this project both types of interfaces have been studied. 

At tidal interfaces, oxygen rich water will infiltrate the sediment at high tide and will therefore enhance the transport of oxygen into the sediment. The extent of penetration is dependent of the resistance of the sediment and the consumption of oxygen upon contact with the reduced solid phase. In stationary interfaces the oxygen penetration will be only a few mm or cm, since only diffusion and dispersion determine its transport. Without dispersion or non-equilibrium sorption, the oxygen and the pollution would never come into contact over a broad zone. Then, the only contact would be at a sharp interface. In reality, mixing does occur, making it possible for the pollutant to be degraded with oxygen. The extent of this mixing determines the degradation. 

The different bottlenecks will be tackled in consequent project phases. The first phase of the project is especially aimed at on the one hand a better understanding of the occurrence of NAinterface processes, and on the other hand a first concept of a measurement strategy, including the identification of possibly relevant monitoring tools. Based on progressive understanding, in the subsequent phases, the last two bottlenecks will be handled. In this project, insight will be gained in the natural degradation processes at the interface between groundwater and surface water. This knowledge will contribute to a functionally aimed and cost-effective way of management and control of polluted sites. Application may lead to less remediation efforts, and in the ultimate case to the prevention of the active remediation measures. 


 CHAPTER 5 

###### ACTIVITIES AND INTENDED RESULTS 

The project consists of three sub-phases. In the first sub-phase, the knowledge and experience, gained in other projects has been used to confine the research on the reactive interface. Initially, boundary conditions of the interface and the relevant parameters for the model were defined (conceptual model). Subsequent inspection of the participating sites has been carried out to make a selection of two sites for further research. An inventory of existing monitoring tools and the development and preliminary testing of new ones was also performed in this phase. During the second phase, the existing and newly developed monitoring tools have been installed and groundwater, surface water and solid phase samples have been taken to determine the parameters that were defined in the first phase of the project. Bioassays have been performed with (ground)water samples from upstream and downstream of the NA interface to determine whether the aquatic ecosystem is sufficiently protected by the natural attenuation processes occurring in the interface. 

Meanwhile, two different modelling approaches have been developed: 

- A **reactive transport model** for micro-pollutants, including geohydrology, geochemistry and     biochemistry; 

- A **model for macro(bio)chemistry of the sediment** , including mass transport, geochemisty,     and diagenesis with degradation of organic matter as the governing process. The measured data have been used to verify the models as much as possible and to produce different scenarios of pollutant emission reduction to the surface water at the investigated sites. 

The results of the monitoring and modelling activities have been tested against the main hypothesis of the project: _“Natural degradation in the reactive interface is involved in the attenuation of pollutants to such an extent that underestimation of this process often leads to an unnecessarily intensive remediation plan”._ 


 CHAPTER 6 

###### LITERATURE DATA AND PRELIMINARY EXPERIMENTS 

6.1 **Aerobic degradation of oxidisable organic pollutants** 

The aerobic degradation of mobile organic pollutants such as e.g. benzene, monochlorobenzene, vinyl chloride occurs relatively fast. In the anoxic groundwater, these compounds can either be inert (e.g. benzene, monochlorobenzene) or accumulated as a degradation product of other chemicals (e.g. _cis_ -dichloroethene, vinyl chloride, monochlorobenzene). The extent of degradation of these compounds at the oxic interface between groundwater and surface water depends, besides the residence time of the compound in the interface, largely on the specific degradation rate. The specific degradation rate is an intrinsic value to quantify the biodegradation independent on the pollutant concentration, which is typical for the degrading bacterial species. Hereby, it is assumed that no bacterial growth occurs, since the pollutant concentration is too low to support growth (see also appendix A). At the industrial sites under investigation in this project, the main pollutants that are expected to enter the interface are monochorobenzene, vinyl chloride and _cis_ -dichloroethene. These compounds are in principle well degradable under oxic conditions. However, whereas for MCB and VC degradation only oxygen is required [4, 13, 3234], the degradation _cis_ -DCE is generally a cometabolic degradation caused by unspecific methane monooxygenase enzymes from methanotrophic microorganisms [11, 12, 46]. Such unspecific reactions are generally slower than the specific oxidation reactions as for VC and MCB. Therefore, the kinetics of this degradation may be different. Moreover, _cis_ -DCE may not be degraded at all in the oxic interface when the main substrate for the monooxygenase enzymes (e.g. methane, phenol) is absent. However, the models used in this report work with different biodegradation scenarios, which are characterised by the choice of different first order rate constants. Therefore, the quantitative results of this modeling will give possible ranges of the contribution of biodegradation processes on the flux decrease in the NA-interface. It is expected that the biodegradation of _cis_ -DCE, despite its possibly different kinetics, will fit into this range. 

Values of aerobic first order degradation rate constants (k) for _cis_ -DC and VC were taken from the literature [49]. However, no rate constants were found in the literature for MCB. Therefore, these have been determined in the laboratory with sediment from the Solvay site (see next section). Since the rate constants we found in this study were considerably higher than values reported for comparable compounds (e.g. toluene), these values were also applied in one of the scenarios for the LBC case. 

6.2 **Determination of the rate constant for aerobic MCB degradation at the Solvay site** 

A literature search on the rate constants ( _k_ ) for the aerobic degradation of MCB, had no results. Therefore, it was decided to determine this rate constant for the Solvay site in laboratory batch experiments. In 200 ml serum flasks, 10 g of moist sediment were added to 150 ml of groundwater from the site. MCB was added to a concentration of 0.5 mg/L. The batches were incubated at 15°C on a shaker in the dark. The concentration of MCB was followed in time by taking headspace samples at different time intervals and analysis of this sample using gas chromatography with flame ionisation detection. The “apparent rate constant” (see appendix A) for the batch culture was calculated by assuming first order degradation kinetics: 

 C = Ce −^ kt 0 


where _C_ = concentration MCB (μg/L) _C_ 0 = concentration MCB at time zero (μg/L) _k_ = apparent first order rate constant (day-1) _t_ = time (days) 

Figure 3 shows the results of the batches with the highest and the lowest degradation rate and the fitted curves using the abovementioned equation. After 1.5 days about 80-100% of the MCB was degraded. The calculated apparent rate constants for the batch systems lay between 0.82 day-1^ and 3.58 day-1. The apparent rate constant k for the batch system was corrected for the sediment, which has lower water content than the batch system (appendix A). Thus, the rate constant for the sediment system was found to be between 16 and 70 day-1^ at 15°C. 

 y = 506,81e -3,5804x 

 0 

 100 

 200 

 300 

 400 

 500 

 600 

 0 0,5 1 1,5 2 Tim e (da ys) 

 M CB (μg/L) 

 y = 516,87e -0,8181x 

 0 

 100 

 200 

 300 

 400 

 500 

 600 

 0 0,5 1 1,5 2 Tim e (da ys) 

 M CB (μg/L) 

Fig. 3. Results from the batch degradation tests with Solvay sediment and MCB. The batches show the MCB concentration during time in the batches with the fastest (left) and the slowest (right) degradation. The formulas describe the equation of the black lines, indicating the closest fit to first order degradation kinetics. 


 CHAPTER 7 

###### CONCEPTUAL MODEL AND HYPOTHESIS BUILDING 

7.1 **Approach from surface water to sediment** 

7.1.1 _Methodology_ 

_Research approach_ The residence time and the degradation rate of the pollutants in the active sediment layer are strongly indicative for its degradation capacity. The residence time depends on various advection and dispersion processes and on adsorption of the pollutants. The degradation rate is very sensitive to the redox conditions, that vary over time and space. 

The degradation capacity can be expressed as the time averaged ratio of the pollutant flux from the sediment into the overlying water and the pollutant flux from the aquifer into the active sediment layer. Whether the degradation capacity is large enough to prevent toxic effects is to be judged on the basis of pollutant concentrations in the sediment and the overlying water. Consequently, the quantification and evaluation of the degradation capacity requires the application of models that provide both the fluxes and the concentrations of the pollutants in the sediment and the overlying water. 

Given the many uncertainties in and the site specificity of the conditions in the sediment, it was decided not to model a theoretical sediment and overlying water system. The models needed to be applied and verified for two contaminated test sites, which necessitated the execution of field measurement programmes. 

In view of the above, the research entailed the following activities: a. characterisation of the active sediment layer; b. formulation and selection of models that adequately describe redox-processes, transport processes and pollutant’s fate processes for both the sediment and the overlying water; c. development and operationalisation of the models; d. application of the models for the selected test sites; e. evaluation of the models and the sediment degradation capacity. 

The activities have been executed in two phases. Phase 1 concerned activities a and b, whereas phase 2 focussed on the remaining activities. Phase 1 also involved the selection of test sites and the assessment of the feasibility of the research. The sites selected are essentially different with respect to the presence or absence of tidal influence, the groundwater flow and pollutants. Delft Hydraulics has modelled two of the three cases, namely the Solvay and the LBC case. The modelling activities are given below. 

**a. Characterisation of the active sediment layer** The characterisation involved the identification of different, relevant types of redox interfaces, the relevant sediment diagenesis processes, the pollutant’s fate processes, and additional, relevant conditions. The identification was done in general and more in particular for the test sites, and leaned on Delft Hydraulics’ extensive expertise regarding water and sediment quality studies. From the start it was clear, that redox processes, transport processes, degradation and adsorption are important processes, and that spatial heterogeneity is important for the local modification of these processes. 


**b. Formulation and selection of models** Conceptual models were formulated for sediment diagenesis, redox-processes, transport processes and pollutant’s fate processes. It was decided that the overlying water was to be imposed on the models as a forcing function. Data provided by the field measurement programmes were used to refine the conceptual models. The selection of water and sediment quality modelling tools took the dedicated tools available at Delft Hydraulics as a starting point. These are CHARON [5-7], a chemical model for water and sediment quality, and DELWAQ [55, 56], a generic modelling framework for water and sediment quality. CHARON allows simulations of sediment diagenesis with a large extent of chemical and spatial detail. This model was to be used as research tool, mainly for the recognaissance and quantification of the redox sediment chemistry. DELWAQ was to be used for the integrated, scenario-type simulation of surface water and sediment systems including the fate of pollutants. 

**c. Development and operationalisation of the models** CHARON simulates sediment-water systems dynamically with an algorithm that calculates both slow processes and the chemical equilibrum. The chemical and physical system definition imposed on CHARON includes the most important sediment diagenesis processes. Among these processes are microbiological degradation of organic matter, nitrification, redox processes, methanogenesis, precipitation and dissolution of various iron minerals, and advective and dispersive mass transport (seepage, diffusion, bioirrigation and bioturbation). The dispersion and degradation of an organic micropollutant were added too. The 0.4 m thick sediment compartment was schematised with 25 layers, the thickness of which increases from 0.25 mm in the upper layer to 60 mm in the lower layer. Field measurement data of pore water concentration profiles and sediment composition were used as indicative values for the quantification of the initial composition of simulated water and sediment compartments as well as the water composition at the surface water and groundwater boundaries. The organic matter content of the sediment was quantified by means of an upper limit and a lower limit in order to reflect the possible range of conditions in the sediment and overlying water at the test sites. The values of process coefficients such as process rates were selected on the basis of the many calibrated applications of CHARON, which have been performed in the past. 

DELWAQ essentially deals with the same processes, but simulates them as slow processes in a much more parameterised way. The iron chemistry is not explicitly included. However, the simulation of micropollutants takes into account all important processes, including sorption. The sediment compartment was schematised with 14 layers, the thickness of which increases from 1 mm in the upper layer to 100 mm in the lower layer. 

The DELWAQ model was made operational after the completion of the application of CHARON. A recently improved new version of DELWAQ was applied, which allows the integrated simulation of water and sediment layers. DELWAQ was made to approximately reproduce the results of CHARON with respect to the consumption and penetration of oxygen in the sediment. The initialisation of the model was based on the same field data. The same degradation rates were applied for the micropollutants. Upper and lower limits of the rates for monochlorobenzene had been determined experimentally by TNO-MEP. The coefficients connected with additional processes such as sorption were quantified using available literature data. 

Both models used the constant groundwater seepage calculated for the two cases by TNO-NITG with a groundwater flow model as input. Test simulations with a conservative tracer showed the correctness of the models with respect to mass conservation and mass transport. 


**d. Application of the models** A calibration of process parameters on field data appeared not feasible because of the rather coarse vertical resolution of the available data. Moreover, the data concerned only two remote points in time. In view of this the path of dynamic year round simulations was abandoned. It was decided to perform steady state simulations only. All boundary conditions and forcing including the temperature were imposed on the models as time averaged conditions. Upper and lower limits for the sediment oxygen consumption were determined on the basis of upper and lower limits for the content and the degradation rate of organic matter in the sediment. Separate simulations for the minimal and the maximal oxygen consumption delivered: 

- the lower and the upper limit of the oxygen penetration depth; and 

- the maximal and the minimal degradation flux for the micropollutant. 

CHARON was applied for the Solvay and LBC case. The results for the degradation of micropollutants are indicative. The application of DELWAQ was restricted to the Solvay case, and delivered more precise data on the degradation of monochlorobenzene. 

**e. Evaluation of the models and the sediment degradation capacity** Models provide simplified representations of a natural system, implying that simulation results can never be better than approximate. Nevertheless, imperfect models are adequate when research questions can be answered to satisfaction. Potentially important aspects that have not been considered with the models as well uncertainties with respect to the input have been identified. The results and conclusions have been interpreted in view of uncertainties, simplifications and omissions. 

_Data requirements_ At the start of the research a list was made of the field data required for the calibration and the application of integrated water and sediment quality models. This list is attached as appendix B. 

_The cases studied and available data_ Delft Hydraulics modelled the Solvay and the LBC cases. These cases are described in chapter 8 of this report. 

A relatively extensive measurement programme was executed for the Solvay site. This programme provided data on sediment composition and the vertical concentration gradients of dissolved macrochemical substances and the pollutant. The measurement programme for the LBC site delivered rather crude data on gradients of substances in groundwater (see §11.3). These data do not meet the requirements for several reasons. The main cause is to be found in technical impediments. The detailed measurement of the composition of sediment and pore water in a vertical profile requires state-of-the-art techniques, the operation of which under field conditions is extremely troublesome. Only a subset of the parameters was actually measured at three points in time including the first trial survey. The vertical resolution was 1-2 cm. The consequence of this was that dynamic simulation with the models was abandoned. 

7.1.2 _The natural system studied_ 

_Water quality processes_ The quality of surface water results from an intricate interplay of numerous biochemical, chemical and physical processes. Since the simulation of water quality is not the purpose of the present study and is dealt with as a known boundary condition, only a very brief summary of water quality processes is given here. The organic matter in surface water arises from discharges of wastewater and from the primary production and mortality of phytoplankton (algae) and water plants. The assimilation of carbon 


dioxide by phytoplankton produces dissolved oxygen (DO). The production is more intense in nutrient (N, P) rich water, especially in highly eutrophic, shallow water systems. Dead organic matter often called detritus is mineralised by bacteria and settles on the sediment, where the decomposition continues. DO is consumed and carbon dioxide and nutrients (ammonium, phosphate) are released in the mineralisation process. The ammonium released is oxidised to nitrate in a microbial process called nitrification. DO exchanges with the atmosphere proportional to de degree of superor undersaturation [56]. All processes are highly dependent on temperature (directly) and solar radiation (indirectly), which implies diurnal and seasonal variation of process rates and concentrations. The seasonal differences may be large in moderate climates. The diurnal variation of the dissolved oxygen concentration may also be large in connection with primary production (assimilation) in eutrophic water systems. 

_Macro(bio)chemical processes in sediment_ The diagenesis of sediment in surface water is basically driven by the microbial decomposition of organic matter and the penetration of so-called electron acceptors in the active sediment layer [9, 27, 41-43]. Organic matter settles from the overlying water, into which it was discharged with wastewater, or in which it was produced by phytoplankton. The nature of the organic matter gradually changes during the decomposition process, which causes the decomposition rate to slow down. The organic residue changes into refractory humic material due to both biochemical and chemical polymerisation processes. Electron acceptors, like dissolved oxygen (DO), nitrate, manganese(IV), iron(III), sulphate and carbon dioxide, are required for the oxidation of organic matter. DO, nitrate and sulphate are obtained from the overlying water, whereas the other electron acceptors are mainly recycled in the sediment. The redox processes involved can be formulated as chemical reactions (figure 4). 

 800 

 600 

 400 

 200 

 0 

 -200 

 -400 

 Eh (mV) Energy yield (kJ/Mole CH2O) 

 Depth in sediments (CM) (high carbon flux sediments) 

 Eh 

 (mV) 

 Q_2846_M020308a 

###### (O2 

###### H2O) 

###### oxygen consumption 

 0.1 

###### (NO3 

###### N2) 

###### denitrification 

###### (MN(IV) 

###### MN(II)) 

###### manganese reduction 

###### (FE(III) 

###### FE(II)) 

###### iron reduction 

###### (SO4 

###### HS) 

###### sulfate reduction 

###### (CH2O 

###### CO2, CH4) 

###### methane formation 

 0.2 5 15 40 60 

Fig. 4. Sequence of redox reactions in surface sediments [38]. 

Bacteria cannot use the different electron acceptors simultaneously, because the energy gained from the reduction reactions is dependent on the redox potential. Moreover, bacteria species have specialised in using only one of the electron acceptors. Santchi _et al_. [38] presented the sequence of redox reactions in sediment according to figure 5. 


 Aerobic respiration: (CH 2 O)x(NH 3 )y(H 3 PO 4 )z + xO 2 + yH+^ → xCO 2 + yNH4+^ + zHPO42-^ + xH 2 O + (2+2z)H+ 

 Denitrification: 5(CH 2 O)x(NH 3 )y(H 3 PO 4 )z + 4xNO3-^ + (4x+5y)H+^ → 5xCO 2 + 5yNH4+^ + 5zHPO42-^ + 7xH 2 O + 10zH+^ + 2xN 2 

 Dissimilatory managenese reduction: (CH 2 O)x(NH 3 )y(H 3 PO 4 )z + 2xMnO 2 + (4x+y)H+^ → xCO 2 + yNH4+^ + zHPO42-^ + 3xH 2 O + (2+2z)H+^ + 2xMn2+ 

 Dissimilatory iron reduction: (CH 2 O)x(NH 3 )y(H 3 PO 4 )z + 4xFe(OH) 3 + (8x+y)H+^ → xCO 2 + yNH4+^ + zHPO42-^ + 11xH 2 O + (2+2z)H+^ + 4xFe2+ 

 Sulphate reduction: 2(CH 2 O)x(NH 3 )y(H 3 PO 4 )z + xSO42-^ + (x+2y)H+^ → 2xCO 2 + 2yNH4+^ + 2zHPO42-^ + 2xH 2 O + (2+4z)H+^ + xH 2 S 

 Methanogenesis: 2(CH 2 O)x(NH 3 )y(H 3 PO 4 ) + 2yH+^ → xCO 2 + 2yNH4+^ + 2zHPO42-^ + (4+4z)H+^ + xCH 4 

Fig. 5. Reaction equations for the microbial degradation of organic matter using various electron-acceptors (modified after [45, 54]). 

The redox potential decreases at the depletion of dissolved oxygen (DO) consumed in the aerobic degradation of organic matter. Denitrification only starts at the depletion of DO. Theoretically, the processes next in line after the depletion of nitrate are the reductions of manganese and iron. However, usually these processes concur with sulphate reduction due to low availability of dissolved manganese(IV) and iron(III), when the redox potential has gone down to approximately -200 mV. The (oxy)hydroxides of manganese and iron are highly insoluble. Finally, methanogenesis takes over when sulphate gets depleted at a redox potential of about 250 mV. Reduced substances are produced from nitrate, manganese(IV), iron(III), sulphide and carbon dioxide. The nitrogen produced from nitrate is released to the atmosphere. The manganese(II) and iron(II) precipitate as carbonate and sulphide minerals, that remain stable in the absence of oxygen. Reoxidation takes place at the deeper penetration of oxygen, or when through bioturbation reduced substances are mixed into the oxidised sediment top layer. Part of the reduced metal and sulphide ions does not precipitate, but diffuses upward and oxidises and precipitates quickly in the top layer. These are mainly chemical processes. The oxidation of methane is a biological process, which may proceed using DO or sulphate. Substantial quantities of methane may be released to the atmosphere, when the pore water has become saturated with methane. The reaction equations of the relevant (bio)chemical oxidation processes are presented in figure 6. 


 Oxidation of solutes with oxygen: NH4+^ + 2O 2 + 2OH-^ → NO3-^ + 3H 2 O 

 2Mn2+^ + O 2 + 4OH-^ → 2MnO 2 + 2H 2 O 

 4Fe2+^ + O 2 + 8OH-^ + 2H 2 O → 4Fe(OH) 3 

 H 2 S + 2O 2 + 2OH-^ → SO42-^ + 2H 2 O 

 CH 4 + 2O 2 → CO 2 + 2H 2 O 

 Oxidation of solutes with sulphate: CH 4 + SO42-^ → CO 2 + 2H 2 S + 2OH

 Oxidation of solids with oxygen: 2=S-Mn2+^ + O 2 + 2OH-^ → 2MnO 2 + 2=S-H 

 4=S-Fe2+^ + O 2 + 4OH-^ + 6H 2 O → 4Fe(OH) 3 + 4=S-H 

 FeS + 2O 2 → Fe2+^ + SO42

 2FeS 2 + 7O 2 + 2H 2 O → 2Fe2+^ + 4SO42-^ + 4H+ 

 Oxidation of iron with solids: MnO 2 + 2Fe2+^ + 2OH-^ + 2H 2 O → Mn2+^ + 2Fe(OH) 3 

 Oxidation of sulphide with solids: MnO 2 + H 2 S → Mn2+^ + S 0 + 2OH

 2Fe(OH) 3 + H 2 S → 2Fe2+^ + S 0 + 4OH-^ + 2H 2 O 

Fig. 6. Reaction equations for the secondary redox processes. =Sindicates a sorption site. (modified after [53, 54]). 

Ammonium is one of the by-products of the decomposition of organic matter. This substance diffuses upwards, is released into the overlying water or oxidised to nitrate. The process of nitrification is established by specialised bacterial species, and provide nitrate for denitrification. 

The aforementioned chain of processes leads to a very characteristic layer structure in the sediment [39, 40, 44, 53, 54]. Four sediment layers can be distinguished in the diagenetically active sediment, as is presented in figure 7. Additionally, a very thin meta-stable boundary layer exists that contains the detritus settled from the overlying water. From this boundary layer, detritus is incorporated in the sediment as the consequence of bioturbation and physical turbation. Only the sediment toplayer contains oxygen (d 1 ), whereas nitrate is present in both the toplayer and the second sediment layer (d 2 ). Together these layers form the oxidising layer (do), where metal (oxy)hydroxides are stable minerals. The third sediment layer still contains sulphate (d 3 ). All electron acceptors except carbon dioxide have been depleted in the fourth sediment layer (d 4 ). These two layers form the reducing sediment layer, where metal sulphides are stable minerals. 


 overlying water 

 d 

 boundary layer 

 o 

d (^) h dl d M3090 E000605b aerobic denitrifying oxidizing reducing **sediment** d (^1) d (^2) d (^3) d (^4) Fig. 7. The layer structure of sediment in relation to diagenetic processes. Denitrification proceeds mainly in the second layer. Sulphate reduction and methanogenesis proceed mainly in respectively the third and fourth layers. Due to macro-heterogeneity with respect to the availability of organic matter, porosity and chemical composition, these layers may not have the same thickness everywhere in the sediment. Moreover, due to micro-heterogeneity, the layers may be overlapping in the sense that reduction processes may occur in layers for which they are uncharacteristic. Denitrification and sulphate reduction may occur in anaerobic micro-pockets in the aerobic toplayer, whereas methanogenesis may proceed in sulphatedepleted micro-pockets in the sulphate-reducing layer [9]. The position and thickness of the layers is highly dependent on various transport processes. Advection in a direction perpendicular to the sediment-water interface may be caused by infiltration or seepage in connection with the predominant groundwater flow. Tidal motion may cause the alternation of infiltration and seepage. Dispersion at and below the sediment-water interface is caused by water flow along the sediment surface, resuspension-resettling, bioturbation, bioirrigation and molecular diffusion [41, 42]. Resuspension-resettling and bioturbation mainly affect solid substances, and cause a redistribution of organic matter and oxidised and reduced minerals in the sediment. The other transport processes affect only dissolved substances, and are responsible for the penetration of dissolved electron acceptors into the sediment. Short term and seasonal changes in temperature, water quality and organic matter settling cause diurnal and seasonal changes of the thickness of the layers [40]. In winter, the oxidising layer gets relatively thick due to slow decomposition of organic matter and high concentrations of DO 


and nitrate in the overlying water. In summer, the oxidising layer may virtually disappear when large quantities of organic matter are deposited at the sediment, and are decomposed quickly. The changing of forcing functions implies the diurnal and seasonal alternation of oxidising and reducing conditions in the middle zone of the active sediment layer. 

As mentioned above, the availability of organic matter and the penetration of electron acceptors drive sediment diagenesis and redox layer structure. These factors may be quite different for water systems in connection with differences in water quality (eutrophication), (ground)water flow and sediment composition. Extremes can be observed. Sandy sediment, that is poor in organic matter and that is subjected to alternating infiltration and seepage, will develop a thick oxidising layer (1-10 cm). On the contrary, silty sediment, that is rich in organic matter and has no significant water flow, will show a very thin oxidising layer (0.1-1 cm; [40]). However, all sediments may still have thick sulphate reducing layers especially in saline environments (10 cm or more; [53, 54]). 

_Processes concerning pollutants in water and sediment_ Organic pollutants in surface water are subjected to partitioning among dissolved and solid phases, settling, volatilisation, microbial degradation and transport [56]. Additional substance specific processes may be chemical hydrolysis and photochemical oxidation. Only partitioning, microbial degradation and hydrolysis may proceed in the sediment. Hydrolysis is probably not important for the pollutants considered in this study, since they are persistent at reducing conditions. 

Even mobile organic pollutants adsorb to some degree to particulate organic matter in water and sediment, including detritus and live phytoplankton. The adsorption and desorption of poorly sorbing substances are almost in equilibrium. The higher the organic content of sediment, the stronger adsorption may be. This may interfere with microbial degradation, because adsorbed pollutant is hardly available for degradation. On the other hand, adsorption prolongues the residence time of the pollutant in the sediment, which is favourable for degradation. 

Volatilisation is the release of a compound from surface water to the atmosphere. The rate of this process is proportional to the concentration in the water phase and the volatility of the compound. Both volatilisation and microbial degradation are highly temperature dependent, which means that these processes proceed at low rates in winter time. 

The microbial degradation of an organic pollutant is usually highly dependent on the redox potential. Some substances are only decomposed at reducing conditions, whereas the decomposition of other substances needs oxidising conditions or even the explicit presence of dissolved oxygen. Some substances need both types of conditions for the complete conversion into carbon dioxide. The decomposition may start at reducing conditions, whereas metabolites are further decomposed only at oxidising conditions. Some metabolites are more toxic to aquatic organisms than the mother substance. 

The extent of aerobic degradation of a pollutant in the sediment is dependent on the thickness of the aerobic or oxidising layer, the residence time of the pollutant in this layer, and the presence of a stable microbial population adapted to the decomposition of this pollutant. It is conceivable that such a stable population may not develop in certain sediment strata, due to diurnal and seasonal variation of the thickness of the redox layers as decribed in the previous section. Moreover, aerobic pollutant decomposing bacteria species may not colonise the anaerobic micropockets that persist in the aerobic layer. Bacteria will not be equally distributed in the sediment anyhow, because of vertical and horizontal heterogeneity regarding the availability of 


organic matter and nutrients. Finally, the activity of bacterial populations can also be disturbed by changes in salinity, which may occur in estuarine environments. 

The transport processes in the sediment have been discussed in the previous section, and are therefore skipped here. 

7.2 **Conceptual model from groundwater to sediment** 

7.2.1 _The system studied_ 

_Transport of groundwater contamination_ Groundwater contamination is often caused by the spill of a Non-Aqueous Phase Liquid (NAPL). This NAPL will form a floating layer on the groundwater if the density is lower than the density of water (LNAPL) or will sink in the groundwater until it is trapped on a less permeable layer when the density is higher than the density of the groundwater (DNAPL). From there the contaminants slowly dissolve into the groundwater. Groundwater flow is the dominant mechanism for the spreading of this dissolved contamination. Due to processes such as diffusion, dispersion, plumes will get larger and wider. Due to adsorption, the velocity of the average concentration may be less than the groundwater flow velocity and a further widening of the plume may occur. When the pure phase NAPL is not removed it will act as a continuous source for the plume until all mass has dissolved, but total dissolution is generally not reached within decades. Therefore contaminant plumes in groundwater are often characterised by a continuous source. 

_Biodegradation_ Another process that is important for groundwater contamination is biodegradation. Bacteria can degrade the contaminant into different substances that can be harmless or even be more toxic than the original contaminant (such as vinyl chloride, which is an intermediate product of PCE degradation). The degradation of groundwater contaminants is part of a redox reaction. The contaminants are often used as an electron donor while for instance oxygen acts as an electron acceptor. Oxygen is the strongest electron acceptor that is often encountered in natural groundwater systems. Other electron acceptors are only used if oxygen is depleted. The electron acceptors that are often encountered in groundwater systems are (in reducing strength): nitrate, iron(III) (s), sulphate and carbon dioxide (methanogenic bacteria). The reaction formulas with benzene as an example for the contaminant are given in the following reaction mechanisms. 

_Degradation by oxygen: C 6 H 6 + 7.5 O 2 → 6 CO 2 + 3 H 2 O_ 

_Degradation by nitrate: C 6 H 6 + 6 NO_ − 3 _+ 6 H+→ 6 CO 2 + 6H 2 O + 3N 2_ 

_Degradation by iron: C 6 H 6 + 30 Fe (OH) 3 + 60H+_^ _→ 6CO 2 + 78 H 2 O + 30 Fe2+_ 

_Degradation by sulphate: C 6 H 6 + 3.75 SO_^24 − _+ 7.5 H+_^ _→ 6CO 2 + 3H 2 O + 3.75 H 2 S_ 

_Degradation by methanogenesis: C 6 H 6 + 4.5 H 2 O → 2.25 CO 2 + 3.75 CH 4_ 

Some bacteria can also use oxidised contaminants such as PCE as an electron acceptor. However, this degradation pathway is not the target of this study. 

The reaction rate of the contaminants depends commonly on the concentration of the strongest electron acceptor and the concentration of the contaminants and also on the bacterial population. The bacterial population needs some time to grow when the circumstances become favourable. This last influence was experienced in the SKB-project “Ditribution of directly injected auxiliary substances” [28]. In this project, however, it is assumed that when the conditions for biodegradation are favourable, it is likely that they has been so already for a long period and 


bacterial populations are in a steady state. Due to the consumption of electron acceptors such as oxygen, the concentration of this electron acceptor may be depleted and degradation rates decrease. Depending on the type of contaminant, different electron acceptors (and different bacteria) may be used to continue the biodegradation (often at a lower degradation rate): or biodegradation may become negligible. 

_The NA-interface_ At the interface between groundwater and surface water, there is often a considerable change in chemical conditions, which may have a strong influence on the potential biodegradation. The region that will be addressed as the “NA-interface” is characterised by strong changes in physical and chemical properties. Aim of this study is to determine the capacity of biodegradation in this NA-interface. The key parameter to describe this capacity is the residence time of the contaminants with respect to the characteristic degradation time. This residence time depends strongly on the time-varying water fluxes, whereas the characteristic degradation time strongly depends on the time varying redox-conditions over the NA-interface. 

7.2.2 _Model used_ In principle, there are three important zones of which each has its own characteristic spatial and temporal scales: 

1. The surface water that is adjacent to the NA-interface. 

2. The soil compartment in which the transport of the groundwater and the dissolved     contaminants takes place. 

3. The transition zone. 

The model of WL/Delft Hydraulics studies the zone mentioned under 1. The zone mentioned under 2 is studied by TNO-NITG using a groundwater flow model. Both WL/Delft Hydraulics and TNO-NITG modelled the transition zone. 

_Modelling of the groundwater compartment_ In the first step, the large 3D-groundwater flow system has been modelled. First, the groundwater flow was modelled as a steady state system, using existing models that used the MODFLOW software [24] or Microfem [14]. The resulting groundwater fluxes in the vicinity of the NA-interface were used as input for the contaminant transport model. For the tidal influenced groundwater systems, the groundwater flow model is also calculated for the transient situation using the software MODFLOW. A few tidal periods were modelled by imposing the real time-varying surface water levels as a boundary condition. By obtaining the groundwater fluxes at the cells of the NA-interface over time, a first estimate of the extension of the mixing NA-interface in this tidal influenced system can be obtained. For the behaviour of the contaminants upstream of the mixing NA-interface, it can be assumed that the influence of the time varying groundwater velocities is negligible. 

The scale at which these processes are modelled is small enough to obtain detailed information about the groundwater flow in the vicinity of the NA-interface. If necessary, grid refinement or additional model layers were introduced. Results of this step were the spatial variability (fluxes through the bottom versus fluxes through the bank) of the water fluxes through the NA-interface. 

_Modelling of the biodegradation at the NA-interface_ For the biodegradation on the NA-interface the concentrations of all relevant chemicals are calculated using a 1D model. Hereto is streamtube in the direction of flow is selected out of the large-scale groundwater model. Fluxes and groundwater flow velocities are obtained from that large-scale groundwater model. The relevant chemicals are all chemicals that have a direct or indirect influence on the degradation rate of the contaminant. The waterfluxes in this model are known as they have been obtained by the model of the groundwater compartment. The boundary 


conditions with respect to the concentrations at the side of the groundwater compartments are obtained from field data. The concentrations at the surface water are obtained from field data as well. 

The 1-D transport model gives two important products: the extension of the interface layer described by the variation of the concentrations of the macrochemical parameters, which influence the degradation rates of the contaminants and the variation of the concentrations of the contaminants. The transport codes that have been studied for this project are the GT-model (Integrated Transport model; developed at TNO-NITG and KIWA [51]) and RT3D [3]. The GT-model is a combination of the transport software MT3D and the geochemical software PHREEQC. It has mainly been developed to compute the macrochemistry based on equilibrium reactions. The model can account for the precipitation of salts and complex adsorption behaviour in which for instance protons and heavy metals compete for the same sorption sites. It can handle kinetic formulations based on nitrification/denitrification, but introduction of other kinetic processes is not straightforward. RT3D is the reactive transport code, which has a few predefined modules for relatively simple degradation processes, that are based on zero or first order degradation or even Monod kinetics in which also bacteria populations are modelled as a state variable. The reactions are generally based on kinetic or total consumption of one of the species, so chemical equilibrium calculations are not implemented in RT3D. It has also a module in which a user can program all reaction equations he wants to incorporate. 

Due to this flexibility of RT3D, the fact that chemical equilibrium equations are not needed for the description of the redox-chemistry at the three field sites studied and the GT-model would have problems to introduce new kinetic reactions, it was chosen to apply RT3D for describing both the behaviour of the redox-chemistry and the micropollutants. It was chosen to model the macrochemistry and microchemistry simultaneously. In that case the biodegradation of the micropollutants have an influence on the redox-conditions and moreover the present version of RT3D cannot handle time dependent degradation constants, which would be needed for the tidal systems. 

**Important aspects** There are a few aspects that can play an important role in the modelling of this system: 

- The thickness and the composition of the active NA-interface are time dependent due to     sedimentation processes. The characteristic time of this process is relatively long. This     temporal variation is presently neglected within the model. 

- Besides the macro- and micro-chemical parameters that describe the redox conditions in the     interface layer, also temperature variations of the surface water and the water at the NA-     interface may play a role in the degradation capacity of the interface layer. This temporal     variation is presently neglected within the model. 

- Both the electric conductance and the temperature of the water in the NA-interface can act     as a tracer for monitoring of the water fluxes in the NA-interface. 


 CHAPTER 8 

###### RESEARCH SITES 

8.1 **Characteristics** 

8.1.1 _Listing essential characteristics_ To come to the selection of suitable sites to study the NA-interface processes, we have listed the characteristics that should preferably known to fulfil the measuring and modelling needs. These characteristics concern the logistics for measurements, physical and chemical parameters in the pore water, the surface water and the sediment solid phase (see appendix B). Then, all candidate sites were visited to check this list for certain visual (logistic) characteristics and the availability of technical data, which are useful for the selection procedure. 

8.1.2 _BP site, Ghent, Belgium_ The site is situated alongside the channel Ghent-Terneuzen. BTEX and mineral oil migrate under the main road toward the channel, which is protected by a sheet pile. However, this sheet pile is not water-locked. The first 2.5 m of the bank surface is covered with concrete. Between the road and the bank are a crash barrier and some bushes. Concentrations of micro-pollutants are known, more parameters are listed in a report of the consultant. Two monitoring wells positioned in a straight line, perpendicular and close to the bank, show significantly decreasing benzene concentrations toward the bank. The groundwater table is 1.8 m-bgs. The top layer of 10 m consists of middle fine sand with a clay sheet at approximately 3 m-bgs. 

8.1.3 _Shell Netherlands Refinery/Chemistry, Hoogvliet Rotterdam, The Netherlands_ Data on soil and groundwater (hydrology, concentrations) are reported in several previous studies. In certain places, there is significant flux from an intermediate sand layer (ca. 7 m deep). A number of possible study sites have been selected on the basis of benzene concentrations that, upstream, exceed the Dutch intervention values. Accessibility of the bank is poor at most places because of overground pipelines. At most places, jetties are present, from which sediment and (ground)water samples can be taken. The groundwater table is at 1 m-bgs, and at the incline there is a drop to the surface water level. At some places loading and unloading of oil tankers takes place. The incline is covered with bricks. 

8.1.4 _Huntsman, Rotterdam Rozenburg, The Netherlands_ Data on soil and groundwater have been published in reference [37]. Data on aniline in the surface water are available (not on MCB). The monitoring well closest to the bank is situated ca. 40 m away from the incline. At the moment of visiting, it was therefore unclear whether any aniline or MCB would flow into the harbour. Later, new monitoring wells, situated close to the bank showed no increased concentrations of these compounds in the groundwater. The bank is vacant and its accessibility is good. A jetty is present from which sediment and (ground)water samples can be taken. A salt ship moors two times a week. Limewater and the effluent of the water purification plant is discharged in the harbour. The groundwater table is 1 m-bgs, and at the incline there is a drop to the surface water level. A ridge of rubble of about 1 m wide is flanking the down edge of the incline. The incline is covered with basalt bricks. 

8.1.5 _Solvay Pharmaceuticals, Amsterdam, The Netherlands_ Data on soil and groundwater quality have been reported by Delft Geotechnics [26]. The site is at three sides surrounded by the Noordzeekanaal. Part of it has been sold to Uniroyal and built-on. The remaining part is vacant. The site is confined by watertight sheet piles to prevent discharge 


of pollutants (MCB, VOCl). Around the sheet piles, a ridge of basalt/rubble was applied to strengthen the bank. Ships sail along, causing considerable alluvion. Pushing down part of the sheet pile resulted in strong erosion of the bank. Here, emergency enforcements have been placed (straw bales and clay). The pollution is mainly present in the in the upper sand layer of ca. 4 m. The groundwater table is less than 1 m-bgs and the flow direction is influenced by infiltration and withdrawal. Solvay has offered to dig a ditch inside the sheet piled area to facilitate the NAinterface project by creating and studying an artificial NA-interface. This generous offer was accepted and a research ditch of ca. 30 m wide and 4 m long was created at the south side of the site, where high concentrations of MCB occurred in the groundwater. Also, a hydrogen peroxide remediation was taking place at this location, resulting in aerobic groundwater conditions. For the NA-interface research, part of the hydrogen peroxide infiltration was switched off. The depth of the ditch could be varied by regulating the inlet of harbour water and the discharge of ditch water to the water purification plant. At this location, there were only data on micropollutants available, i.e. no macrochemical and redox data. These have been acquired after the ditch had been installed. 

8.1.6 _LBC, Pernis, The Netherlands_ The site is located in the Rotterdam harbour area, which has an open connection to the sea. Therefore, marine conditions prevail in the surface water and tidal water table fluctuations apply to this site. The quay consists of an incline of ca. 4 m deep. At the foot of the incline a rubble bar of half meter thickness covers the shore (figure 8). At the site, there is an efflux of _cis_ dichloroethene ( _cis_ -DCE) and VC toward the surface water. 

Fig. 8. View from the quay of site 2 on the shore (low tide) with the rubble bar. 

8.2 **Selection** 

Our aim was to select two sites for detailed study of the NA-interface processes. Several primary selection criteria were defined, which led to the final selection: 

1. There should be net drainage from groundwater to surface water; 

2. There should be a considerable (measurable) aerobically degradable pollutant flux potential     to the surface water; 

3. The interface should be accessible for detailed measurements. 

All sites fulfilled to criterion 1 (net drainage). However, Huntsman and Shell did not fulfil to criterion 2 (pollutant in interface). BP and Shell did not fulfil to criterion 3 (accessibility). 


The Solvay ditch and the LBC site fulfilled to all criteria, albeit that the LBC interface was covered with rubble and therefore possibly difficult to access. Therefore, these sites were selected for the measurement and modelling activities. On the request of Shell, modelling activities were also performed for this site. 

8.3 **Hypothesis NA-interface per site** 

The conceptual model, as described in the previous chapter, is generally valid for all three sites involved. The main difference between the sites is that the Solvay site has a static interface with a vertical influx of groundwater to the bottom of the ditch. Due to tidal influences, the interface of the LBCand Shell-site is dynamic. The influx at these sites is horizontal. At the Solvay and Shell site, monochlorobenzene is expected to be degraded when the contaminated groundwater passes the interface. At the LBC site, trichloroethene is being degraded in the anaerobic groundwater heading to the interface, whereas _cis_ -DCE and vinylchloride are expected to be degraded in the interface. 

Further details are given in chapter 7 (Conceptual model and hypothesis building) and previous paragraphs of chapter 8. 


 CHAPTER 9 

###### SAMPLING TOOLS 

9.1 **Existing tools** 

The search for existing devices that can be used for the sampling of the NA-interface resulted in different potentially suitable tools, which will be described here. 

9.1.1 _Peeper_ This system consists of a rectangular PVC plate with horizontally cut out slots of ca. 40 ml each (lower slots contain 80 ml each). These slots are situated at defined distances from each other. The slots are covered on both sides of the plate with a hydrophilic membrane (Versapor) and subsequently covered with another PVC plate with openings at the height of the slots (see figure 9). Both sides of each slot are connected to PVC/PE tubing, through which they are filled with demineralised water. The bottom of the system has a sharp edge, which facilitates pushing the system into the sediment. Once placed in the sediment, the system needs to equilibrate with the surrounding pore liquid in the sediment. When the system is equilibrated, samples are taken by pushing out the liquid from the slots with nitrogen gas. The resolution of this system is 1 cm. This system has been used for the research at the Solvay site. 

Fig. 9. Side view of the peeper system, ready for use. 

9.1.2 _Environfilters_ The Environfilter allows groundwater sampling from depths down to more than 70 metres, depending on soil resistance, without disturbing the chemical composition of the soil. It consists of a loose cone point on which a filter has been fitted as well as a synthetic riser tube. The whole apparatus is pressed into the ground in a closed state with standard CPT-equipment. Once it has reached the sampling depth, the rod string is retracted to expose the filter to the groundwater. The rod string is expelled completely leaving only the cpt-point and riser tube in the 


soil. During retraction the borehole is effectively sealed under controlled conditions by an environmentally harmless grout, thus preventing oxygen penetration. The Environfilter is made of HDPE and has a standard filter length of 80 cm and a PTFE riser tube with a diameter of 10/12 mm. In this particular project the filter length was only 4 cm and the riser tube had a diameter of 2/4 mm. 

9.2 **Tools developed within the project** 

9.2.1 _Multilevel sampling device_ The system is composed of a hollow tube (ca. 30 cm diameter) that is pushed in the sediment of the ditch. The water level in the ditch has to be kept low, so that the soil inside of the tube can be excavated. At defined distances from the top of the tube, special filter tubes are pushed horizontally through pre-drilled holes from inside the tube into the sediment (figure 10). Each filter tube is separately connected to tubing, which is led to the bank of the ditch. The tubing of all filter tubes is clustered and wrapped into a protective sleeve. Samples can be taken by connecting the tubing to syringes. To prevent the influence of the extraction zone of one filter tube on another close by, the filter tubes of successive depths are placed in a horizontal angle of 45° of each other. To prevent taking samples of the preferential water flow along the main tube, the basis of the filter tubes consists of 3 cm “blind” material At each depth, two filter tubes are placed (duplicates) one in an opposite direction to the other. The exact depths can be preset according to the expected thickness of the NA-interface. The resolution of this system is also 1 cm. 

Fig. 10. Top view of the main tube, inserted into the sediment. The small filter tubes are pushed from inside into the sediment. 

9.2.2 _Control buckets_ In order to determine the quality of the seepage water without that it is being mixed with surface water, at the Solvay site buckets (diameter ca. 20 cm, height ca. 15 cm) containing small holes at the top, were place upside down over the sediment. The content of the buckets can be analysed 


through tubing, connecting the bucket with the bank (figure 11). Since there is very little mixing in these buckets, the contents of the buckets became anaerobic and thus, no oxygen could penetrate into the sediment interface. Therefore, these devices were used to simulate the absence of a NA-interface as defined before in this report. 

#### anaerobic sediment 

#### groundwater 

#### interface interface 

aerobic surface water (^) sample tubing **anaerobic interface** 

#### anaerobic sediment 

#### groundwater 

#### interface interface 

aerobic surface water (^) sample tubing **anaerobic interface** Fig. 11. Schematic picture of a control bucket. 


 CHAPTER 10 

###### METHODOLOGY SITE INVESTIGATIONS 

10.1 **Field measurements** 

For the field measurements, several were devices available. 

- OTD diver 

- Soil core sampler 

- Flow-through cells (oxygen, redox) 

10.2 **Chemical analyses** 

10.2.1 _Water samples_ Water samples were taken from the multilevel samplers, environment filters, control buckets and peepers. They were analysed for the following parameters: 

_pH_ The pH of each sample was measured directly in the field, using a portable pH electrode and pH/mV-meter. 

_MCB_ A sample of 2 ml was added to 20 ml vials containing 6 ml distilled water and ca. 10 mg/L HgCl 2. MCB was measured in the headspace of these vials after heating the vial to 80°C, using gas chromatography connected with a mass selective detector GC-MSD. 

_Nitrate, sulphate_ Samples of ca. 1.5-2 ml were collected in Eppendorf tubes, which contained 20 μl of a 1g/L HgCl 2 stock solution. In the laboratory, these samples were diluted to the appropriate concentration and analysed with high performance liquid chromatography (HPLC) with an ion exchange column and a conductivity detector (Dionex). 

_Metals_ Samples of 2 ml were collected in tubes, which contained ca. 50 μl of concentrated HNO 3 , and analysed with atomic absorption spectrometry (flame-AAS). 

_Sulphide_ Samples of 2 ml were fixed with 0.25 ml of a 1 M ZnCl solution. Sulphide was measured spectrophotometrically according to the Dutch standard method NEN6608. 

_COD_ 1-2 ml of sample was added to tubes from a Dr. Lange LCK 314 COD analysis kit, which were then vigorously shaken. In the laboratory, the tubes were heated in a heating block and the extinction was analysed at 435 nm. 

_Ammonium_ Samples of 2 ml were collected in tubes, which contained ca. 50 μl of concentrated H 2 SO 4 , and after dilution analysed with high performance liquid chromatography (HPLC) with an ion exchange column and a conductivity detector (Dionex). 


10.2.2 _Soil samples_ The soil core samples were defrosted in a polyethelene glove box, which was constantly flushed with N 2. After defrosting the cores, the samples were transferred into a glove box kept under nitrogen atmosphere. In the glove box, the sediment was carefully pushed out the stainless steel casing. The cores were sliced in four parts: 0-3 cm, 3-6 cm, 6-11 cm, and 11-16 cm from the sediment surface. These subsamples were analysed for the following parameters. 

_X-ray fluorescence analysis (XRF)_ A 10-g subsample was ground and subsequently pressed with wax into pressed-powder tablets. The samples were ground using a Tungsten-carbide mill in an automated grindingand pressing machine. The tablets were analysed for major and trace elements by X-ray spectroscopy, using an ARL9400 spectrometer with a Rh tube, with full matrix correction for major elements (SiO2, TiO2, Al2O3, Fe 2 O 3 , MnO, MgO, CaO, Na 2 O, K 2 O, P 2 O 5 , S) and Compton scatter method for trace elements (As, Co, Cr, Cu, Ni, Pb, V, Zn, Ba, Ga, Nb, Rb, Sr, Y, Zr). The XRF was calibrated using approximately 100 certified geological reference samples. 

_Total C and N_ Total N en total C were determined with a Carlo Erba NA 1500 NCS elemental analyser. 

_Thermogravimetric analysis_ Water content, organic matter, carbonate and loss of ignition at 1000 °C were analysed with a LECO Thermogravimetric Analyzer 601. The analyses are performed by automatically measuring the weight loss of a sample during stepwise heating. The temperatures were set to 105 °C for water content, 450 °C for organic matter, 800 °C for carbonate and 1000 °C for remaining claybound water. 

_MCB_ An internal standard (toluene) was added to the subsamples, which were subsequently extracted with methanol. The methanol was analysed for MCB by using GC-MSD. 

_Acid-volatile sulphide (AVS)_ AVS analysis was analysed according the method described by Van den Berg [50] and Henneke [15] with slight modifications. Ca. 1 gram of sediment was transferred to the reaction vessel in an argon-filled glove bag. The reaction vessel was weighed and then attached to the argon-purged analysis train. Samples were acidified with 10 ml 6M HCl for 1 hr at room temperature. Resultant H 2 S was flushed from the reaction vessel and trapped in a 1M NaOH solution. H 2 S concentrations were determined colorimeterically as described in reference [1]. 

10.3 **Ecotoxicological investigations** 

One of the most important preconditions for implementation of Natural Attenuation as solution for contaminated sites is that the water ecosystem may not be adversely affected by the groundwater contaminants. Most likely, remediation solutions that do not protect the water ecosystem or even regard the water compartment as "reactor", are not acceptable to the appropriate local authorities such as Rijkswaterstaat. Therefore, it is very important to investigate whether the NA interface reduces concentrations of potentially toxic substances to acceptable levels. For many well-known substances, these levels have been defined. The MTR (Maximum Tolerable Risk level) is the concentration that protects 95% of the species in the aquatic ecosystem. MTR's for water and sediment are listed in reference [2]. Procedures exist to derive indicative MTR's (i-MTRs) from ecotoxicity data for substances for which no MTR has been established yet. A first indication of the risk of a substance for the aquatic ecosystem can be obtained by comparing the measured or modelled concentrations of the substance in water and 


sediment to the corresponding MTR. This "generic assessment" was executed for both the Solvay and the LBC site. 

However, in this case, this generic assessment yields only a rough estimate of the actual risk for the aquatic and sediment ecosystem. Reasons for this are: 

- The bioavailable concentration of the substance may not be equal to the calculated or     measured concentration, because of sorption or speciation; 

- Degradation products (metabolites) may be produced. The degradation products are often     not taken into account in risk assessments, and in many cases no ecotoxicity data is     available for these substances. Metabolites may be less toxic or more toxic than the parent     compound. 

- The combined effect of more than one toxic substance (mixture) is difficult to predict. The     combined effect may be stronger (synergism) or less strong (antagonism) than the expected     combined effect of the individual substances. 

- Finally, and important in this specific case: the composition of the pollution is not always     known, and substances whose existence is not expected, may not me analysed and therefor     not be included in the risk assessment, which will underestimate the actual risk. 

Because of these reasons, bioassays have been executed as well for the Solvay and LBC site. The principle of a bioassay is that water (or sediment) is collected in the field and taken to the lab, where organisms are exposed to this water under controlled conditions. After a certain period of time (e.g., 96 h), the mortality (or other endpoint) is registered. The advantage of bioassays is that they respond to all toxic substances in the sample, and bioavailability and combination effects are taken into account. The disadvantage is that it is difficult to link observed effects with specific substances. 

A point of attention is the oxygen concentration in the samples. Samples of groundwater one both sides of the suspected NA interface were analysed, as well as samples of surface water. Some of these samples are (most likely) anaerobic, some have (very) low oxygen concentrations, and surface water samples are aerobic. We used standard (aerobic) toxicity tests for the bioassays, of which the individual wells where covered with foil. This means that some oxygen has entered the samples during the execution of the test (which may cause breakdown of the substances), and it means that the low oxygen concentration may have affected some of the test organisms. However, these tests are more representative for assessing the actual risk for the aquatic ecosystem than anaerobic bioassays. The test results represent the situation that the groundwater enters the surface water, and aquatic animals are exposed to this water. However, some care should be taken when interpreting the results. 

Three tests were used, covering three different trophic levels: 

- Microtox Basis Test (Bacteria); 

- Rotox Test (Rotifer); 

- Thamnotox Test (Crustacean). The tests are described in the following sections. 

All tests were executed in two replicates. The sample is classified as “toxic”, when a significant difference between the blank and the highest concentration (most cases: undiluted sample) was observed. This difference is determined by STOWA [48] (see table 1). 


Table 1. Criteria for toxicity [48]. 

 Test Difference (%) between blanc and sample that is significant at n=2 replicates Microtox test 60-70 Rotox test 40-45 Thamnotox test 40-45 * 

* Comparable to Rotox; Brils (pers. comm.) 

No additional classification (e.g., very toxic, slightly toxic) was used. 

Two series of tests were executed: 

- In the first series (samples taken on April 23 2002 by De Straat and TNO-MEP, dept. MBT);     four samples from the Solvay site and three samples from the LBC-site were tested in all     three tests. 

- On September 24 2002, a second series was tested (samples taken on August 30 2002, by     TNO-MEP, dept. MBT), to verify the results of the first series: four samples from the Solvay     site and three samples from the LBC-site. The samples were stored at 5º C before analysis.     Only the Microtox test was executed. 

EC 50 s were calculated for the Thamnotox and Rotox tests after plotting the calculated percent mortalities on a log concentration / % mortality sheet. This procedure is described in reference [29]. 

To determine the validity of the tests, environmental parameters (pH, salinity, ammonia, sulphide) were analysed in the samples. This was not possible in the first test series, due to the limited volume of the samples. The analysis protocols are described in table 2. 

Table 2. The analysis protocols used in the ecotoxicologic studies. 

 Parameter pH Salinity Ammonia Sulphide Protocol ER-001 ER-003 Merck testkit TNO draft protocol Remarks WTW pH meter WTW oxicalc kit number 14752 Spectrophotometric 

**Microtox Basic Test** The principle of the Microtox Basic test is based on the direct exposure of the bio-luminescence bacteria _Vibrio fisheri_ with the water sample. In the Microtox test the toxicity of a sample is determined by measuring the bioluminescence of the bacte-ria Vibrio fisheri. The bioluminescence is a measure for the respiration of the bac-teria and is based on a biochemical reaction. Inhibition of the respiration by toxic substances will result in a reduction of the bioluminescence. The decrease in bio-luminescence is a measure for the toxicity of the sample. 

The sample is pre-treated and a dilution series is made. The samples are incubated during 10 minutes at 15 ºC. Bacteria are pre-treated and put in the samples. After incubation the samples are measured with a Microtox 500. The method is described in the standard protocol for Microtox Solid Phase, from RIKZ (National Institute for Coastal and Marine Management), which has been adapted for Microtox Basic Test. Difference between the two tests is that for the Solid Phase test a sediment sample is used, for the Basic Test a water sample is used [36]. 

**Rotox Test** In freshwater and coastal marine environments rotifers play a major role in several important ecological processes. As filter-feeds on phytoplankton and bacteria, rotifers exert substantial 


grazing pressure that at times exceeds the grazing pressure of the larger crustacean zooplankton. In addition to their important ecological role in aquatic communities, rotifers are attractive organisms for toxicological studies because an extensive database exists on the basic biology of this group. The rotifer life cycle is well defined and the fac-tors regulating it are reasonably well understood. Rotifers in the genus Brachionus are particularly useful for environmental toxicology because of their rapid repro-duction, short generation times, sensitivity and the commercial availability of dor-mant eggs (cysts). Brachionus have a cosmopolitan distribution that spans six con-tinents and are ecological important members of many aquatic communities im-pacted by pollution. The rotifer _Brachionus calyciflorus_ (figure12) is used in the Rotox test. 

A 24 hour LC 50 bioassay is performed in a multiwell test plate using neonates of the freshwater rotifer Brachionus calicyflorus which are hatched from cysts prior to the test. The sensitivity of Brachionus calyciflorus compares favourably with that of many in-vertebrates currently used in aquatic toxicology. The Rotox test is highly standardised, each Rotoxkit containing standard test materials, concentrated salt solutions and reference cysts. The repeatability of the toxicity test is therefore high. The complete protocol is described in “Rotoxkit F; Rotifer Toxicity Screening Test for Freshwater; Standard Operational Procedure” [30]. 

Fig. 12. Rotifer _Brachionus calicyflorus_ (From reference [47]). 

A dilution series 100 % 50 % 25% 12.5 % and 6.25 % of the sample is prepared by the serial dilution procedure. A parafilm strip was put over the test plate, after filling the plates. The plate was incubated at 25 ºC in darkness, for 24 hours. After 24 hours each well is checked for dead and living rotifers. The organisms are considered dead if they do not exhibit any movement in 5 seconds of observation. 

**Thamnotox test** Freshwater anostracans, often called fairy shrimp, are one of the many groups of aquatic crustaceans; fairy shrimp are typical inhabitants of temporary, predator-poor aquatic environments, which dry out periodically, or show striking changes in the water level. Survival during adverse periods is ensured by the production of resting eggs, called cysts. When the 


habitat becomes favourable again, the cysts hatch, and give rise to nauplii that rapidly grow out to adults, ensuring the next active generation. Investigations have led to the development of a simple and cost-effective acute bioassay with the nauplii of the fairy shrimp species _Thamnocephalus platyurus_. Live test organisms can be hatched “on demand” from cysts. The 24 hour LC 50 bioassay is performed in a multiwell test plate using instar II-III larvae of the fairy shrimp _Thamnocephalus platyurus_ (figure 13), which are hatched from cysts prior to the test. Each Thamnotoxkit contains standard test materials, concentrated salt solutions and reference cysts. The repeatability of the toxicity test is therefore high. 

Fig. 13. Fairy shrimp Thamnocephalus platyurus. 

A dilution series 100 % 50 % 25% 12.5 % and 6.25 % of the sample was prepared by the serial dilution procedure. A parafilm strip was put over the test plate, after filling the plates. The plate was incubated at 25 ºC in darkness, for 24 hours. After 24 hours each well was checked for dead and living larvae. The organisms are considered dead if they do not exhibit any movement in 10 seconds of observation. The complete protocol is described in “Thamnotoxkit F; Crustacean Toxicity Screening Test for Freshwater; Standard Operational Procedure” [31]. 


 CHAPTER 11 

###### SITE INVESTIGATIONS 

11.1 **Solvay site** 

11.1.1 _Geohydrological modelling_ 

**Introduction** The Solvay site is located in the Amsterdam Harbour area on a peninsula that is about 750 x 300 m. The site is surrodunded by the Noordzeekanaal in the north and by the Carel Reijnierszhaven in the south. On this location a ditch was constructed for test purposes for the NA-interface project. This ditch has a length of 25 and a width of +/4m. It is located in the centre approximately 50 m from the surface water. An overview of the Solvay location and a schematic position of the ditch are shown in figure 14. 

Fig. 14. Location of Solvay as well as location of the test ditch. 

The Ditch is located on a rather contaminated area where MCB concentrations up to 15 mg/l were measured in the past. For the site a remediation program was developed. One of the measures is the installation of sheet piling around the location to prevent the contamination from spreading to the harbour and the deep groundwater. The sheet piling covers almost 90 % of the site boundaries. An extra sheet piling is drilled perpendicular to the harbours and divides the location in the fallow area (with ditch) and the area with factory buildings. 

**Groundwater model Solvay** The objective of this modelling activity is to calculate the groundwater flux that passes the NAinterface in order to simulate the biochemical processes that take place. The groundwater model for the Solvay site is developed in two steps. First a ‘regional’ model is set up for the harbour area around Solvay covering 2000x1500 m. The model results were used as boundary conditions for the second and smaller model covering just the Solvay peninsula. Information for both models was taken from previous reports on the site [26]. 


_Geological layering_ The geological layering at Solvay is as follows. 

1. Antropogenic sandy layer This layer has a thickness of 3 to 6 m and lies on top. The deepest position of this layer is found at NAP –7m while the surface has an average level of NAP +1 m. In some parts of the terrain (north-west and south-east) this layer contains more clay and on a local scale some clay lenses are found. These lenses are formed during the construction of this layer. 

2. Clay layer (Duinkerke formation) Below the antropogenic layer a clay layer is located. Field data shows that the thickness of this specific layer can fluctuate throughout the site from 1 m central south to 16 m northeast depending on the position of a former channel. 

3. Sandy layer (Duinkerke formation) Under the confining layer a thick sandy formation (channel deposit) is found containing clay lenses on a local scale. This layer is considered the lower boundary of both groundwater models. 

From this point the explanation of the groundwater model set-up is focused on the second and most detailed model. 

Based on the available information a groundwater model is set up for the phreatic layer containing the antropogenic layer and the first low-permeable layer. To be able to model the groundwater system around the ditch with the NA-interface in detail, the first layer is split up in 12 sub-layers. Because the compositions of the antropogenic layer varies in space (sand, sand/clay and clay) also different hydrological parameters are defined. The geohydrological parameters for the modelled layer types are given in table 3. 

Table 3. Hydrological parameters for geological layers used in the model. 

 Geological layer Hydraulic conductivity (m/day) 

 Anisotropie ratio conductivity: Horizontal / vertical 

1. Antropogenic layer 

- Sand 4.4 1 

- Sand/clay 2.2 2 

- Clay 0.44 10 

2. Confining layer 0.001 1 

_Boundary conditions_ The model boundaries are defined by the water level in the harbour, at the west boundary by the phreatic head and at the bottom by the head of the sandy layer below the confining layer. In the model the sheet piling has a resistance of 1000 days. The recharge is estimated at 1 mm/day. 

_Groundwater system around the NA-interface_ The groundwater system around the ditch with the NA-interface is complex because of the interaction with the aforementioned remediation system. This system originally consists of a number of drains systematically installed throughout the area. Figure 15 shows the location of the ditch and 8 surrounding drain locations supported by gridlines. More drains are installed at equal distances. They were used for geohydrological isolation and remediation of contaminant sources and plumes. At present, only a selection of drains is used for remediation (figure 15). In the drain just above the ditch, hydrogen peroxide is infiltrated (+) to stimulate biological 


degradation of a MCB source. Surrounding drains stimulate groundwater transport by draining (-) groundwater. 

Fig. 15. Location of the NA-interface ditch (top) and surrounding drains (bottom). 

A pump in the ditch is used to maintain a constant water level, causing a certain groundwater flux flowing towards the ditch. The incoming flux contains contamination that passes the NAinterface. Pumping harbour water into the system refreshes the water in the ditch. Several wells are installed on the site (figure 15) for measurements of groundwater heads and contaminant concentrations. During the test phase the water level in the ditch was fixed at NAP –0.55 m. 

**Model results** During the test phase (started in January 2002) the peroxide remediation could not be switched off, thus the remediation is part of the simulation. The field operator passed data about infiltration and drainage fluxes. In figure 16 the calculated heads and streamlines are shown. The heads show a typical convex pattern between the surface water at the north and the south. East of the sheet piling a high phreatic head is calculated because of a higher resistance of the low-permeable layer as well as the surrounding sheet piling. The streamlines represent the flowpaths of the infiltrated H 2 O 2 -water in the direction of the remediation drains and the north part of the ditch. According to the results, a small part (10%) of the H 2 O 2 can seep out in the ditch if not degraded in time. So the effect of H 2 O 2 or decomposition products on the NA-interface depends on the degradation rate. 


Fig. 16. Calculated heads (top) and pathlines (bottom). 

Model results of the stationary were compared with measured heads on 8 locations. Some of the points show a rather good fit (+/0.15 m) while others are off more than 0.5 m. Some mismatch may be expected because of the lack of information on local heterogeneity, location of clay lenses and hydrological parameters. Larger effects can be caused by the remediation system. From consultations with the field operator it is found that some drains are leaking causing lower heads in the direct vicinity. 

Based on the model results a range of seepage fluxes through the NA-interface at the streambed of the ditch is defined: Low : 20 mm/day Mean : 70 mm/day High : 120 mm/day 

During the field test data is collected on the water volumes pumped into and out of the ditch. The water budget for the ditch easily gives an estimation of total seepage volume. Together with the 


seepage area it gives an impression of the seepage flux for 1 m 2 of NA-interface. The results are in range of the fluxes given above. These fluxes are used as boundary conditions for the detailed fate and transport calculations within the NA-interface. 

11.1.2 _Sampling methodology_ At the Solvay site, a NA-interface of millimetres to centimetres was expected. Therefore, highresolution devices had to be used here. At this site, two multilevel samplers were installed, two peepers and three control buckets (figure 17). For sediment oxygen measurements, an OTD diver was applied. 

_Water samples_ At the Solvay site, samples for analytical measurements were taken from both installed multilevel samplers using 5 and 10 ml syringes. The first 5 ml of sample was considered as “dead volume” from the tubing and was discarded. The following 10 ml of sample was divided over different vials for the appropriate analyses. All samples were stored cool and dark until analysis in the laboratory. This procedure has been performed in two sampling rounds, one in April and one in August 2002. Water samples of 40 ml were taken from the peepers. These samples were used for the ecotoxicity tests. 

_Soil samples_ In August 2002, two core samples were taken from the upper 30 cm of the ditch sediment. Directly after sampling, the cores were closed with paraffin and subsequently frozen at –80°C with solid carbon dioxide. The samples were transported to the laboratory for analysis. 

 multilevel sampling devices 

 peepers 

 anaerobic control compartments 

 multilevel sampling devices 

 peepers 

 anaerobic control compartments 

 multilevel sampling devices 

 peepers 

 anaerobic control compartments 

Fig. 17. Multilevel samples, peepers and control buckets installed at the sediment surface of the (temporarily emptied) Solvay ditch. 


11.1.3 _Results_ 

_Water samples, round 1, April 2002_ The MLSDs and the three anaerobic control compartments were sampled. In the samples from the anaerobic control compartments, only MCB was determined. 

The results of the analyses of the MLSDs are shown in figure 18. The MCB concentration at 22 cm depth varies largely. The highest concentration is in the range of 16 mg/L. The concentrations closer to the groundwater-surface water interface clearly decrease to a zero level in the surface water. MCB concentrations measured in the anaerobic control compartments were all around 15 mg/L. This shows that they are good negative controls in relation with NA-interface degradation processes. 

The pH shows a trend of high alkalinity (pH near 9) in the surface water, declining to around pH 7 in the sediment. The metals Fe, Ca and Mn show clear concentration peaks at 4 cm depth. This can be explained by the accumulation of these metals at the point were they are oxidised and precipitate. Samples from this depth were clearly yellow, indicating that the sample contained part of the (colloid) iron precipitates. 

The sulphate concentrations are relatively low in the deeper sediment (10-40 mg/L. However, a sharp increase (up to ca. 500 mg/L) in the sulphate concentration occurs around 3 cm depth. Here, the oxidation of sulphide at the interface has caused the increase of the sulphate concentration. Nitrate is present at only very low levels. There are only a few samples with detectable levels at 0 and 1 cm depth. COD measurements do not show a clear trend over depth. Unfortunately, no reliable data could be obtained from the ammonium analyses. For another important parameter, oxygen, the sample volumes were too small. This parameter was measured by using a diver containing an oxygen sensor. The device needs further improvements regarding stabilization time and resolution. 


 Phosphate (mg/L) 0 2 4 6 8 10 12 14 

 Depth relative to sediment surface (cm) 

 -20 

 -10 

 0 

 10 

 Ca-total (mg/L) 0 100 200 300 400 

 Depth relative to sediment surface (cm) 

 -20 

 -10 

 0 

 10 

 Sulphate (mg/L) 0 100 200 300 400 500 

 Depth relative to sediment surface (cm) 

 -20 

 -10 

 0 

 10 

 Mn-total (mg/L) 0 2 4 6 8 10 12 14 

 Depth relative to sediment surface (cm) 

 -20 

 -10 

 0 

 10 

 COD (mg/L) 0 50 100 150 200 

 Depth relative to sediment surface (cm) 

 -20 

 -10 

 0 

 10 

 pH 6 7 8 9 

 Depth relative to sediment surface (cm) 

 -20 

 -10 

 0 

 10 

 Nitrate (mg/L) 0 1 2 3 4 5 6 7 

 Depth relative to sediment surface (cm) 

 -20 

 -10 

 0 

 10 

 MCB (mg/L) 0 2 4 6 8 10 12 14 16 

 Depth relative to sediment surface (cm) 

 -20 

 -10 

 0 

 10 

 Fe-total (mg/L) 0 100 200 300 400 

 Depth relative to sediment surface (cm) 

 -20 

 -10 

 0 

 10 

 Phosphate (mg/L) 0 2 4 6 8 10 12 14 

 Depth relative to sediment surface (cm) 

 -20 

 -10 

 0 

 10 

 Ca-total (mg/L) 0 100 200 300 400 

 Depth relative to sediment surface (cm) 

 -20 

 -10 

 0 

 10 

 Sulphate (mg/L) 0 100 200 300 400 500 

 Depth relative to sediment surface (cm) 

 -20 

 -10 

 0 

 10 

 Mn-total (mg/L) 0 2 4 6 8 10 12 14 

 Depth relative to sediment surface (cm) 

 -20 

 -10 

 0 

 10 

 COD (mg/L) 0 50 100 150 200 

 Depth relative to sediment surface (cm) 

 -20 

 -10 

 0 

 10 

 pH 6 7 8 9 

 Depth relative to sediment surface (cm) 

 -20 

 -10 

 0 

 10 

 Nitrate (mg/L) 0 1 2 3 4 5 6 7 

 Depth relative to sediment surface (cm) 

 -20 

 -10 

 0 

 10 

 MCB (mg/L) 0 2 4 6 8 10 12 14 16 

 Depth relative to sediment surface (cm) 

 -20 

 -10 

 0 

 10 

 Fe-total (mg/L) 0 100 200 300 400 

 Depth relative to sediment surface (cm) 

 -20 

 -10 

 0 

 10 

Fig. 18. Results of the chemical analyses for sampling round 1, April 2002. The red and black symbols indicate the concentrations measured in the Northand Southside multisamplers respectively. The blue symbols in the MCB graph indicate the concentrations in the control buckets. 

_Water samples round 2, August 2002_ Samples were taken from the multilevel samplers en the three anaerobic control buckets. The results are shown in figure 19. Ammonium was not found in the samples form the multilevel sampler (<5 mg/L). However, in de control buckets high ammonium concentrations were found. This might be due to nitrate reduction and ammonium accumulation in the anaerobic buckets. 


 Phosphate (mg/L) 0 2 4 6 8 10 12 14 

 Depth relative to sediment surface (cm) 

 -20 

 -10 

 0 

 10 

 Ca-total (mg/L) 0 50 100 150 200 250 300 

 Depth relative to sediment surface (cm) 

 -20 

 -10 

 0 

 10 

 Sulphate (mg/L) 0 100 200 300 400 500 

 Depth relative to sediment surface (cm) 

 -20 

 -10 

 0 

 10 

 COD (mg/L) 0 25 50 75 

 Depth relative to sediment surface (cm) 

 -20 

 -10 

 0 

 10 

 pH 6 7 8 9 

 Depth relative to sediment surface (cm) 

 -20 

 -10 

 0 

 10 

 Nitrate (mg/L) 0 1 2 

 Depth relative to sediment surface (cm) 

 -20 

 -10 

 0 

 10 

 MCB (μg/L) 0 500 1000 1500 2000 2500 3000 

 Depth relative to sediment surface (cm) 

 -20 

 -10 

 0 

 10 

 Fe-total (mg/L) 0 20 40 60 80 100 

 Depth relative to sediment surface (cm) 

 -20 

 -10 

 0 

 10 

 Phosphate (mg/L) 0 2 4 6 8 10 12 14 

 Depth relative to sediment surface (cm) 

 -20 

 -10 

 0 

 10 

 Ca-total (mg/L) 0 50 100 150 200 250 300 

 Depth relative to sediment surface (cm) 

 -20 

 -10 

 0 

 10 

 Sulphate (mg/L) 0 100 200 300 400 500 

 Depth relative to sediment surface (cm) 

 -20 

 -10 

 0 

 10 

 COD (mg/L) 0 25 50 75 

 Depth relative to sediment surface (cm) 

 -20 

 -10 

 0 

 10 

 pH 6 7 8 9 

 Depth relative to sediment surface (cm) 

 -20 

 -10 

 0 

 10 

 Nitrate (mg/L) 0 1 2 

 Depth relative to sediment surface (cm) 

 -20 

 -10 

 0 

 10 

 MCB (μg/L) 0 500 1000 1500 2000 2500 3000 

 Depth relative to sediment surface (cm) 

 -20 

 -10 

 0 

 10 

 Fe-total (mg/L) 0 20 40 60 80 100 

 Depth relative to sediment surface (cm) 

 -20 

 -10 

 0 

 10 

Fig. 19. Results of the chemical analyses for sampling round 2, august 2002. The red and black symbols indicate the concentrations measured in the Northand Southside multisamplers respectively. The blue symbols indicate the concentrations measured in the control buckets. 

_Soil core samples_ The results for the soil core sample slices are listed in appendix C. Also here, a gradient of the monochlorobenzene concentration from a high concentrations at 40 cm depth to a lower concentration in the slice containing the upper centimeters of the sediment. 

**Interpretation** 

The sulphate and total iron data from the multilevel sampler clearly show the occurrence of a anaerobic-aerobic transition of the redox chemistry. This NA-interface is located within the upper 2-3 centimeters of the sediment. A more precise estimation of the interface cannot be made with the used equipment, as the highest resolution was 1 cm in this case. Also, oxygen measurements using an OTD diver attached to a probing aparatus showed the absence of oxygen at 2 cm below the sediment surface. 

Also the monochlorobenzene data show a sharp concentration decrease towards the sediment surface. At a first glance, this may indicate the presence of biodegradation of this pollutant in the NA-interface. However, the modelling activities (that will be discussed in the next chapter) have shown that also diffusion/dispersion contributes largely to the attenuation of the monochlorobenzene concentration in the upper part of the sediment. It was concluded that the 


resolution of the monochlorobenzene measurements is not high enough to tell biodegradation from these physical attenuation processes. 

11.1.4 _Ecotoxicological assessment_ 

_Generic assessment_ The main pollutant at the Solvay site is monochlorobenzene (MCB). The maximum concentrations that were measured in the sampling rounds of April and August are listed in table 4, together with the MTR (Maximum Tolerable Risk level, the Dutch environmental quality standard) for surface water. The concentration in the April sampling round is high, ca. 23 times the MTR. Should this concentration occur in surface water, it is likely to cause effects on aquatic organisms. A review of toxicity data learns that especially fish are sensitive to MCB, followed by crustaceans. Algae are much less sensitive to MCB. However, it should be remembered that the concentration was measured at a depth of 45 cm below the sediment surface, and that concentration in shallow sediment samples are below detection limit. The concentrations in the August test series were lower, with a maximum of ca. 4 times MTR. 

Table 4. Expected concentrations of some typical pollutants, compared to MTR's. 

 Substance Highest concentration April 2002 (μg/L) 

 Highest concentration August 2002 (μg/L) 

 MTR (μg/L) Monochlorobenzene 15564 2650 690 

**Bioassays** The results of the two test series are presented in tables 5 and 6. The samples Noord, Midden and Zuid in the first test series were collected in the "reversed bucket" sampling devices, which were placed on top of the sediment. The hypothesis was that these samples would represent the groundwater after passage through the NA interface. However, measurements have shown that the sampling devices disturb the interface, and the water seeping from the sediment is anaerobic. Therefore, the samples are probably representative of the (anaerobic) groundwater below the interface. The "peeper" sample was collected using a Peeper sampling device, at a depth of 30 cm below the sediment surface, which is presumed to be well below the NA interface. However, the sample bottle that we received was not entirely filled and contained some air, and it is likely that the sample has been aerated during the transport and handling. 

The results show that the (probably anaerobic) samples Midden and Zuid are toxic in the Microtox and Thamnotox test, and the sample Noord is toxic only in the Microtox test. The (probably aerated) Peeper sample is not toxic. 

Table 5. Results of the bioassays in the first test series. EC 50 is the calculated dilution (% of sample in test medium) that yields an effect in 50% of the wells. A '-' means no EC50 could be calculated. N.a. means that the undiluted sample was not tested. “*” indicates a significant effect. 

 Microtox test Rotox test Thamnotox test 

Sample EC (^50) (% sample) Effect undiluted sample (%) EC 50 (% sample) Effect undiluted sample (%) EC 50 (%) Effect undiluted sample (%) Noord 6.0* n.a. 2.4 13 Midden 1.6* n.a. 3.3 57 96* Zuid 0.80* n.a. 18 7.8 100* Peeper 74 n.a. 21 10 


In the second test series, samples from the Peeper were collected at increasing depths (P-1 above the NA interface; P-10 well below the interface). The samples were not toxic in the Microtox test (table 6). 

Table 6. Results of the bioassays in the second test series. EC 50 is the calculated dilution (% of sample in test medium) that yields an effect in 50% of the wells. A '-' means no EC 50 could be calculated. 

 Microtox test Sample characteristics 

Sample EC (^50) (% sample) pH (-) Sulphide (mg/L S) Salinity ( 0 / 00 ) Ammonia (mg/L N) P-1 (stimulation) 8.02 < d.l. 2.5 < 4 P-2 (stimulation) 7.16 < d.l. 4.3 < 4 P-10 > 100% 6.60 < d.l. 4.6 10.5 Surface water (stimulation) 6.56 < d.l. 5 < 4 **Interpretation** In the first test series, the bioassays of the samples that are assumed to be anaerobic are toxic to the test species, and the samples that are assumed to be aerobic are less toxic or not toxic. The MCB concentrations in the deeper sediment (45 cm below sediment surface) and the control buckets were high (16 mg/L and 15 mg/L, respectively). This is a likely cause of the observed toxicity. The toxicity of MCB to the _Vibrio fisheri_ (Microtox test) is known from literature: EC 50 values of 9,400 (5 minutes), 11,260 (30 minutes) and 20,000 μg/L (10 minutes) are reported (source: IUCLID database), and STOWA reports a lower EC 50 of 990 μg/L (15 minutes) [48]. The concentration in the peeper sample, which was not toxic, is lower: several hundred μg/L at 30 cm depth. The second test series does not show toxicity. On August 30 2002, concentration gradients were measured at the Solvay location. MCB showed a strong decrease, from ca. 2400 μg/L below the NA interface, to < 16 μg/L in the upper layers of the sediment. The concentration in the "reversed buckets" was ca. 2200-2700 μg/L. Based on these concentrations it can be assumed that the concentration MCB in the samples P1 and P2 was low (< 100 μg/L). The concentration in P-10 is not known, but depending on the depth of the sample (30 cm below sediment surface) MCB concentrations of several hundred μg/L are expected. Therefore, MCB seems a likely explanation for the observed toxicity in the samples. Oxygen could in theory also be an explanation, as toxicity coincides with anaerobic samples. Low oxygen concentrations may have caused adverse effects to the (aerobic) test species. Microtox and Rotox should only be executed on samples with O 2 > 3 mg/L [48]. However, toxicity was observed even in highly diluted samples (EC 50 up to 0.80%, i.e. < 1% sample in > 90% medium). Therefore, it may be assumed that the oxygen concentration in the mixture of sample and medium, which was actually tested, was sufficient. Oxygen is therefore not a likely explanation. For a valid Rotox test, the salinity should be < 3 0 / 00 [48]. Therefore, the salinity of the samples (up to 5 0 / 00 in the second test series) could affect the test species. However, because of the low EC 50 (up to 2%), the dilution argument that was made for oxygen also holds true for salinity. Salinity is not critical for the Microtox test. It is remarkable that stimulation of _Vibrio fisheri_ occurred in the second test series. This phenomenon has been observed before, in a test with high sulphate concentrations (2300 mg/L SiO 4 ) [48]. 


The following conclusions can be drawn from the ecotoxicological assessment: 

- The concentrations of pollutants in the anaerobic groundwater at the Solvay site are higher     than the environmental quality standards (MTR) for surface water. At the Solvay site, the     MCB concentration is 4 to 23 times the MTR; 

- The measured concentrations in the surface water are smaller than the MTR for surface     water. At the Solvay site, the MCB concentration is reduced to << 0.1 * MTR; 

- At the Solvay-site, processes at the NA interface seem the main cause for the reduction of     the hazard. 

- The bioassays at the Solvay-site indicate that the deeper groundwater is toxic, due to the     high MCB concentration. Passage through the NA interface can lead to reduction of the     ecotoxicity from toxic to non-toxic. 

11.2 **LBC site** 

11.2.1 _Geohydrological modelling_ The groundwater flow at the groundwater surface water interface at the LBC-site is complex. The surface water is affected by tidal influences. To describe the temporal behaviour of the groundwater flow in the vicinity of the interface a 2-D model of a cross-section perpendicular to the 3rd^ Petroleumhaven has been made. This model is based on data that were obtained from a 3-D steady state groundwater flow model made with Microfem [8]. 

An overview of the cross-section near the harbour is shown in figure 20. 

Fig. 20. Location and overview of the modelled cross-section (horizontal distance and vertical elevations are estimated using all data available and are not always exact). 

The groundsurface in the vicinity of the NA-interface is characterised by bank containment construction. The land surface is at 4.5 m +NAP. The first slope consists out of basalt and goes down to a small horizontal plain. The elevation of this plain is estimated to be 0.05 m-NAP. The horizontal plain consists out of rubble and is approximately 0.5 m thick and 2.6 m wide. At the harbour site after the edge the rubble slopes down with a 1:3 slope to the bottom of the harbour. During high tide (average 1.22 m+NAP) the horizontal plain is flooded, whereas during low tide (0.60 m –NAP) the small plain (top of the rubble) falls completely dry. 


The model parameters and boundary conditions are obtained from a steady state model that was developed for the LBC-site [8] and site experience obtained during monitoring (De Straat, personal communication) and are discussed below. 

**Geological layering:** The geological layering is as follows: 

1. Antropogenic sandy layer     The top layer consists of a antropogenic sand aquifer of about 5 m thickness. The top of the     aquifer is about 4.5 m +NAP. 

2. Clay layer (Westland Formation)     Underneath the top layer, a clay layer is present. In most of the site this layer is     approximately 5 m thick. However in the direct vicinity of the site there are several indications     that this layer is less thick. First of all, the diver measurements at the monitoring wells 700 –     703 show a clear influence of the tide, which would be impossible if they were located in the     clay layer. During installation the recovery of the wells were found similar to wells in the     underlying Holocene sandy layer. Cone penetration test data at nearby locations showed that     the clay layer is approximately between 0.0 and 0.5 m-NAP. 

3. Holocene sand (Westland Formation)     This layer consists of coarse to fine sand (meander deposits) with occasional small isolated     clay deposits. It is found approximately between 5 and 17 m-NAP, but in the vicinity of the     monitoring site its top is found at approximately 0.0 m NAP. 

4. Holocene peat and clay (Westland Formation)     This low-permebility layer consists out of three deposits. On top a clay layer (Calais     formation), underlain by a peat layer (in Dutch called “basisveen”). Below is a pleistocene     loam layer. In total this layer is about 3 m thick (17-20 m-NAP), but in a large part of the site     this layer is absent. At the location that is considered in this study this layer is mostly absent. 

5. Pleistocene sand (Kreftenheye Formation)     This layer consists of fluvial coarse sand with a high permeability. Its thickness is     approximately 10m. 

6. Pleistocene clay (Kedichem-Tegelen Formation)     This low-permeable clay layer is 30 to 40 m thick and is considered to be the hydrological     base of the model. 

The geohydrologic parameters for the modelled layers are given in table 7. 

Table 7. Hydrological parameters for geological layers used in the model. 

 Geological layer Hydraulic conductivity (m/day) 

 Transmissivity (m 2 /day) 

 Vertical resistance (days) 1 Antropogenic layer 0.4 phreatic aquifer 2 Holocene clay 0.00014 3500 3 Holocene sand horizontal 2 vertical 0.2 

 39 78 

 5 Pleistocene sand 80 800 


**Recharge** The recharge in the steady state model of De Straat is spatially variable depending on the land use. In the area of interest it varies between 0.3 and 1.0 mm/day. In the 2D-model of the crosssection the recharge was choosen the spatial averaged value of a small zone around the crosssection (0.8 mm/day). 

**Harbour** The harbour has been modelled using the river package of MODFLOW. Each cell that has its center within the soil is modelled as an active cell. Each cell that has it center in the surface water is modelled as an inactive cell. Active cells at the land surface-water boundary have boundary conditions in which the flux towards the river depends on the difference between groundwater head and river stage and a river resistance. That resistance is the actual distance between the cell center and the bank divided by the conductivity. An overview of the active and inactive cell and cells with river boundaries are given in figure 21. 

Fig. 21. Overview of active and inactive cells. 

The stages in the harbour are influenced by the tide. To model this effect the surface water stage is modelled using the following equation: 

 h = 0. 31 + 0. 91 sin( 2 π t / 12. 5 ( hour )) 

where _h_ is the river stage and _t_ is the time in hours. 

**Boundary conditions** For the upstream boundary a constant head condition is used. The constant heads are equal to the head estimates obtained by the steady state model of De Straat. At the downstream boundary near the harbour only the head in the lower aquifer is fixed. This value is estimated on head measurements in this aquifer. At the other aquifers the boundary is determined by interaction with the surface water using the river package of MODFLOW. The constant head values are given in table 8. 


Table 8. Constant head boundary conditions. 

 Aquifer Upstream boundary Downstream boundary antropogenic layer 3.5 Holocene sand 0.734 Pleistocene sand 0.508 0.504 

**Storage coefficient and specific yield** The storage coefficients for all layers were set at 0.001; a similar value was the average value found for the Holocene sand at the nearby site of Shell Pernis. The storage coefficient account for additional water storage when the soil matrix is compressed due to a higher water pressure. 

The specific yield is set at 0.2 which is a reasonable value for the effective storage capacity of sand (water volume between saturation and field capacity). The specific yield accounts for the additional storage if the water table rises. 

**Model results** The predicted heads at the monitoring wells are shown in figure 22. 

Fig. 22. Modelled and measured heads at monitoring wells (water level in m NAP related to time in hours). 

The reference elevation of the monitored head was not measured. The elevation of the measured heads in figure 22 was estimated. The model prediction at the locations of well 701 and 702 is good. The main difference is caused by the fact that the tide is is not a perfect sinusoical function but low tide lasts longer than high tide. The model prediction at well 700 is less good. The measurements show a clear cuttoff at around 5 cm +NAP. Below this level, the measured heads show no tidal influence. This effect is likely due to the fact that a certain high conductivity connection with the harbour falls dry and the surrounding area is less permeable and dampens the tidal influence strongly. Unfortunately there is no physical proof to support this hypothesis. 

**Flowlines** Flow lines starting at the monitoring wells have been calculated using the model code MODPATH. The resulting flow lines that start at the outer ends of the monitoring screen are shown in figure 23. 

 -0.4 

 -0.2 

 0 

 0.2 

 0.4 

 0.6 

 0.8 

 1 

 1.2 

 1.4 

 0 5 10 15 20 25 

 model measurement 701 measurement 702 

 -0.2 

 0 

 0.2 

 0.4 

 0.6 

 0.8 

 1 

 1.2 

 0 5 10 15 20 25 

 model measurement 700 


Fig. 23. Calculated streamlines of particles starting at top and bottom of the screen of the monitoring wells (depth in m+NAP; x-coordinate in m). 

The particles started at the outer ends of screens representing monitoring wells are all flowing into the direction of the horizontal plain that falls dry during low tide. The influence of the tide is relatively small. The changes in solute position during one tidal period are in the order of a few centimeters at maximum. 

The particles should officially continue until the horizontal plain at 0.5 m-NAP, but they do not which is the result of a shortcoming of the MOPATH-code. Particles are stopped whenever the particle reaches a cell with a strong sink (all fluxes at the cell boundary are directed inwards except for the river upwelling flux). As the pathlines are almost vertical when they reach the sink (plain at 0.6 m -NAP is the bottom of the cells with the sinks, it is very likely the remaining part of the pathline will be almost entirely vertical. 

**Fluxes** The fluxes that are obtained from the model are given in figure 24. It is clear that the fluxes are also strongly influence by the tide. At all locations, water flows into the aquifer during part of the tidal period. The strongest fluxes are in the direct vicinity of the bottom of the upper slope. The remarkable behaviour of the flux at the bottom of the upper slope at the end of low tide (~ 0.4 days) is due to the fact that the surface water elevation falls just below the horizontal plain and the drainage level of the surface water becomes equal to the elevation of horizontal plain. During high tide the water flows approximately 0.1 m into the aquifer assuming a porosity of 0.3. This value is obtained by dividing the area under the positive fluxes by the porosity. 


 -0.400 

 -0.300 

 -0.200 

 -0.100 

 0.000 

 0.100 

 0.200 

 0.300 

 0.000 0.100 0.200 0.300 0.400 0.500 0.600 time (day) 

 fluxes (m/day) 

 at bottom upper slope 1.3 m from slope 2.6 m from slope 

Fig. 24. Fluxes during tidal period at LBC site at 3 locations (positive flux is flux from surface water into aquifer). 

11.2.2 _Sampling methodology_ Based on the flowpaths shown in figure 25, six environfilters (see section 9.1.2) were placed at different depths and different distances from the foot of the incline, in and under the rubble layer at the LBC site (figure 25). 

 envirofilters (depth) 1.1 m0.9 m 0.5 m0.2 m 

 incline 

 rubble layer 

 envirofilters (depth) 1.1 m0.9 m 0.5 m0.2 m 

 incline 

 rubble layer 

Fig. 25. Position and sampling depth of the environfilters, installed at the LBC site. 

11.2.3 _Results_ The results of the environfilters sampling at the LBC site are shown below. In the figures, the environfilters have been grouped in two series of 3 filters, which can be considered to yield samples from different places in one flowpath. Figure 26 represents the results of the macroparameter measurements. In the series MF5/MF1/MF2 an increase of the oxygen concentration was found from 0.27 at 90 cm below surface to 1.85 mg/L at 20 cm below surface, while the surface water contained 9.20 mg/L O2. Also the pH and the conductivity increased toward the surface. The measured redox potentials do not differ significantly, except for the 


surface water (higher potential). The COD in the surface water is about 7 times lower than in the environfilters. In the series MF6/MF4/MF3, too little data are available on oxygen, pH and redox potential. The values that are available are comparable to those of the other series at the same depth. 

 MF1 MF2 

 MF3 

 MF5 

 MF6 MF4 

 OE 2 0.44 mg/l ECh^ -158 mV1420 μS/cm pH 6.87 COD 104 mg/l 

 OE 2 n.g. ECh^ n.g.1500 μS/cm pH n.g. COD 156 mg/l 

 OE 2 n.g. ECh^ n.g.n.g. pH n.g. COD 122 mg/l 

 OE 2 0.27 mg/l ECh^ -153 mV1520 μS/cm pH 6.83 COD 50 mg/l 

 OE 2 n.g. ECh^ n.g.n.g. pH n.g. COD 162 mg/l 

 OE 2 1.85 mg/l ECh^ -110 mV3300 μS/cm pH 8.03 COD 156 mg/l 

 OE 2 9.20 mg/l ECh^ +101 mV4320 μS/cm pHCOD 8.1919 mg/l 

 Oppervlaktewater 

 milieufilters 1.1 m 0.9 m 0.5 m 0.2 m 

 talud 

 puinberm 

 MF1 MF2 

 MF3 

 MF5 

 MF6 MF4 

 OE 2 0.44 mg/l ECh^ -158 mV1420 μS/cm pH 6.87 COD 104 mg/l 

 OE 2 n.m. ECh^ n.m.1500 μS/cm pH n.m. COD 156 mg/l 

 OE 2 n.m. ECh^ n.m.n.m. pH n.m. COD 122 mg/l 

 OE 2 0.27 mg/l ECh^ -153 mV1520 μS/cm pH 6.83 COD 50 mg/l 

 OE 2 n.m. ECh^ n.m.n.m. pH n.m. COD 162 mg/l 

 OE 2 1.85 mg/l ECh^ -110 mV3300 μS/cm pH 8.03 COD 156 mg/l 

 OE 2 9.20 mg/l ECh^ +101 mV4320 μS/cm pHCOD 8.1919 mg/l 

 Surface water 

 milieufilters 1.1 m 0.9 m 0.5 m 0.2 m 

 talud 

 puinberm 

 Envirofilters (depth) 1.1 m 0.9 m 0.5 m 0.2 m 

 incline 

 rubble layer 

 MF1 MF2 

 MF3 

 MF5 

 MF6 MF4 

 OE 2 0.44 mg/l ECh^ -158 mV1420 μS/cm pH 6.87 COD 104 mg/l 

 OE 2 n.g. ECh^ n.g.1500 μS/cm pH n.g. COD 156 mg/l 

 OE 2 n.g. ECh^ n.g.n.g. pH n.g. COD 122 mg/l 

 OE 2 0.27 mg/l ECh^ -153 mV1520 μS/cm pH 6.83 COD 50 mg/l 

 OE 2 n.g. ECh^ n.g.n.g. pH n.g. COD 162 mg/l 

 OE 2 1.85 mg/l ECh^ -110 mV3300 μS/cm pH 8.03 COD 156 mg/l 

 OE 2 9.20 mg/l ECh^ +101 mV4320 μS/cm pHCOD 8.1919 mg/l 

 Oppervlaktewater 

 milieufilters 1.1 m 0.9 m 0.5 m 0.2 m 

 talud 

 puinberm 

 milieufilters 1.1 m 0.9 m 0.5 m 0.2 m 

 talud 

 puinberm 

 MF1 MF2 

 MF3 

 MF5 

 MF6 MF4 

 OE 2 0.44 mg/l ECh^ -158 mV1420 μS/cm pH 6.87 COD 104 mg/l 

 OE 2 n.m. ECh^ n.m.1500 μS/cm pH n.m. COD 156 mg/l 

 OE 2 n.m. ECh^ n.m.n.m. pH n.m. COD 122 mg/l 

 OE 2 0.27 mg/l ECh^ -153 mV1520 μS/cm pH 6.83 COD 50 mg/l 

 OE 2 n.m. ECh^ n.m.n.m. pH n.m. COD 162 mg/l 

 OE 2 1.85 mg/l ECh^ -110 mV3300 μS/cm pH 8.03 COD 156 mg/l 

 OE 2 9.20 mg/l ECh^ +101 mV4320 μS/cm pHCOD 8.1919 mg/l 

 Surface water 

 milieufilters 1.1 m 0.9 m 0.5 m 0.2 m 

 talud 

 puinberm 

 Envirofilters (depth) 1.1 m 0.9 m 0.5 m 0.2 m 

 incline 

 rubble layer 

Fig. 26. Concentration of different macroparameters measured in the environfilters. 

Figure 27 represents the results of the micropollutant measurements. Contrary to earlier measurements in nearby monitoring wells, very low concentrations of _cis_ -DCE and VC were found in the environfilters. In both series, the concentrations of _cis_ -DCE and VC are too low to indicate a decrease in concentration towards the surface. 

 MF1 MF2 

 MF3 

 MF5 

 MF6 MF4 

 cis-DCE <5 μg/l VCEtheen <2.5 μg/l<14 μg/l Ethaan 413 μg/l 

 cis-DCE <5 μg/l VCEtheen <2.5 μg/l<14 μg/l Ethaan 195 μg/l 

 cis-DCE <5 μg/l VCEtheen <2.5 μg/l69 μg/l Ethaan 3387 μg/l 

 cis-DCEVC <5 μg/l<2.5 μg/l EtheenEthaan 52 μg/l1876 μg/l 

 cis-DCEVC 22 μg/l<2.5 μg/l EtheenEthaan <14 μg/l125 μg/l 

 cis-DCEVC 11 μg/l<2.5 μg/l EtheenEthaan <14 μg/l112 μg/l 

 cis-DCEVC <5 μg/l<2.5 μg/l EtheenEthaan <14 μg/l<15 μg/l 

 Oppervlaktewater 

 milieufilters 1.1 m 0.9 m0.5 m 0.2 m 

 talud 

 puinberm 

 MF1 MF2 

 MF3 

 MF5 

 MF6 MF4 

 cis-DCE <5 μg/l VCEtheen <2.5 μg/l<14 μg/l Ethaan 413 μg/l 

 cis-DCE <5 μg/l VCEtheen <2.5 μg/l<14 μg/l Ethaan 195 μg/l 

 cis-DCE <5 μg/l VCEtheen <2.5 μg/l69 μg/l Ethaan 3387 μg/l 

 cis-DCEVC <2.5 μg/l<5 μg/l 

EtheenEthaan (^) 1876 μg/l52 μg/l cis-DCEVC <2.5 μg/l22 μg/l EtheenEthaan <14 μg/l125 μg/l cis-DCEVC <2.5 μg/l11 μg/l EtheenEthaan <14 μg/l112 μg/l cis-DCEVC <2.5 μg/l<5 μg/l EtheenEthaan <14 μg/l<15 μg/l Surface water **milieufilters 1.1 m 0.9 m 0.5 m 0.2 m talud puinberm Envirofilters (depth) 1.1 m 0.9 m 0.5 m 0.2 m incline rubble layer** MF1 MF2 MF3 MF5 MF6 MF4 cis-DCE <5 μg/l VCEtheen <2.5 μg/l<14 μg/l Ethaan 413 μg/l cis-DCE <5 μg/l VCEtheen <2.5 μg/l<14 μg/l Ethaan 195 μg/l cis-DCE <5 μg/l VCEtheen <2.5 μg/l69 μg/l Ethaan 3387 μg/l cis-DCEVC <5 μg/l<2.5 μg/l EtheenEthaan 52 μg/l1876 μg/l cis-DCEVC 22 μg/l<2.5 μg/l EtheenEthaan <14 μg/l125 μg/l cis-DCEVC 11 μg/l<2.5 μg/l EtheenEthaan <14 μg/l112 μg/l cis-DCEVC <5 μg/l<2.5 μg/l EtheenEthaan <14 μg/l<15 μg/l Oppervlaktewater **milieufilters 1.1 m 0.9 m0.5 m 0.2 m talud puinberm milieufilters 1.1 m 0.9 m0.5 m 0.2 m talud puinberm** MF1 MF2 MF3 MF5 MF6 MF4 cis-DCE <5 μg/l VCEtheen <2.5 μg/l<14 μg/l Ethaan 413 μg/l cis-DCE <5 μg/l VCEtheen <2.5 μg/l<14 μg/l Ethaan 195 μg/l cis-DCE <5 μg/l VCEtheen <2.5 μg/l69 μg/l Ethaan 3387 μg/l cis-DCEVC <2.5 μg/l<5 μg/l EtheenEthaan (^) 1876 μg/l52 μg/l cis-DCEVC <2.5 μg/l22 μg/l EtheenEthaan <14 μg/l125 μg/l cis-DCEVC <2.5 μg/l11 μg/l EtheenEthaan <14 μg/l112 μg/l cis-DCEVC <2.5 μg/l<5 μg/l EtheenEthaan <14 μg/l<15 μg/l Surface water **milieufilters 1.1 m 0.9 m 0.5 m 0.2 m talud puinberm Envirofilters (depth) 1.1 m 0.9 m 0.5 m 0.2 m incline rubble layer** Fig. 27. Concentration of micropollutants measured in the environfilters. 


11.2.4 _Ecotoxicological assessment_ 

_Generic assessment_ To obtain a first indication of the hazard of the groundwater for the aquatic ecosystem, measured concentrations of typical substances are compared to MTRs. After the start of the project, the concentrations of table 9 were measured during the indicative sampling round. 

Table 9. Concentrations of some typical pollutants, compared to MTRs (indicative sampling round). Concentrations that exceed the MTR are printed in bold style. 

 Substance Expected concentration (μg/L) 

 MTR (μg/L) cis -1,2-Dichloroethene 7300 6100 Vinyl chloride 500 820 Tetrachloroethene 30 330 Trichloroethene 60 2400 Benzene 5 240 Toluene 7 730 Ethylbenzene 100 370 Xylenes 10 380 

The highest environmental risk is posed by _cis_ -DCE and its breakdown product vinyl chloride: The PEC/PNEC ratios are 1,2 and 0,6 respectively. Acute toxicity is not to be expected at these concentrations. Breakdown of dichloroethene to vinyl chloride may increase the risk, due to the much higher (7 times) toxicity of vinyl chloride. The aromatic benzene, toluene, ethylbenzene and xylene are more toxic than vinyl chloride, but the concentrations are much lower. All substances are highly volatile, and evaporation will occur soon after substances enter the surface water. 

During phase 1.1 and 1.2 of the project, measurements were carried out (tables 10 and 11). The concentrations of _cis_ -DCE and vinyl chloride in the second sampling round are much lower than in the indicative sampling round. The concentrations of the organic pollutants are all well below the MTR. Arsenic exceeds the MTR with a factor 2 6 (sample 701). 

Table 10. Concentrations of typical pollutants at the LBC-site (in μg/L) [8], in comparison to MTRs. Concentrations exceeding the MTR are printed in bold. n.a. = not analysed. 

 Substance Sample 700 (μg/L) 

 Sample 701 (μg/L) 

 Sample 703 (μg/L) 

 MTR (μg/L) Arsenic 45 160 84 25 Total BTEX 1.8 18 2.1 240-730 Volatile aromatics 1.8 18 1.8 cis -Dichloroethene 95 11 0.48 6100 Vinyl chloride 270 57 1.4 820 Ethene 110 580 94 8500 Ethane n.a. n.a. n.a. 


Table 11. Concentrations of typical pollutants at the LBC-site (in μg/L), measured in the groundwater by TNO-MEP in phase 1.2 of the project. The MTR is shown for comparison. 

 Substance Sample 1 (μg/L) 

 Sample 4 (μg/L) 

 Sample 6 (μg/L) 

 MTR (μg/L) Arsenic n.a. n.a. n.a. 25 Total BTEX n.a. n.a. n.a. 240-730 Volatile aromatics n.a. n.a. n.a. cis -Dichloroethene 22 < 5 < 5 6100 Vinyl chloride < 2.5 < 2.5 < 2.5 820 Ethene < 14 < 14 69 8500 Ethane 125 413 3387 

**Bioassays** The results of the two test series are shown in tables 12 and 13. The sample volumes in the first test series were too small to analyse some chemical characteristics of the sample (pH, salinity, ammonia) that are necessary to determine if the test is valid. In the second series, the volumes were sufficient to carry out the analyses (table 13). 

Table 12. Results of the bioassays in the first test series. EC 50 is the calculated dilution (% of sample in test medium) that yields an effect in 50% of the wells. A '-' means that no EC 50 could be calculated. 

 Microtox test Rotox test Thamnotox test 

Sample EC (^50) (%) Mortality undiluted sample (%) EC 50 (%) Mortality undiluted sample (%) EC 50 (%) Mortality undiluted sample (%) 700 16 n.a. 0 6.7 701 78 n.a. 0 91 60 703 21 n.a. 3 25 Table 13. Results of the bioassays in the second test series. EC 50 is the calculated dilution (% of sample in test medium) yielding an effect in 50% of the wells. '-' means that no EC 50 could be calculated. D.l. = detection limit. Microtox test Sample characteristics Sample EC (^50) (%) Mortality undiluted sample (%) pH (-) Salinity ( 0 / 00 ) Sulphide (mg/L S) Ammonia (mg N/L) 1 9.6 n.a. 7.35 0.8 0.323 < 4 4 71 n.a. 6.49 0.7 0.078 6.2 6 68 n.a. 6.35 0.7 < d.l.^5 Surface water 

- n.a. 6.47 2.1 < d.l.^ < 4 

In the first test series, the samples 700 and 703 show effect in the Microtox test, and the sample 701 in the Thamnotox test. The samples were taken at a depth of 0.7 m. 

The samples in the second test series cannot be compared directly to the first series, because different sampling systems were installed. The depth of the three samples increases, from 1 (0.5 m) via 4 (0.9 m) to 6 (1.1 m). Measured from the quayside to the water, the first sample is 1, followed by 6 and by 4. All three samples are toxic in the Microtox test, but sample 1 is more 


toxic than the other two. The surface water sample in the second test series shows no effect in the Microtox test. 

**Interpretation** At the LBC-site, the exact position of the NA interface is not (yet) located. In the first test series, the samples were selected on the hypothesis that the NA interface is located near 701. Sample 701 shows no effect in the Microtox test, but is toxic in the Thamnotox test. Clearly, the composition of the sample is different from the other two (700 and 703), which show toxicity in the Microtox test. The chemical measurements show that arsenic, BTEX, ethane and volatile aromatics have their peak value at 701. Arsenic exceeds the MTR value. No toxicity data for arsenic in the Thamnotox test is available in literature. Samples 700 and 703 differ in composition, and it is therefore not possible to pinpoint one substance as cause of the observed toxicity in the Microtox test. The concentrations of the measured substances are all below the reported EC 50 for Microtox (see table 14). The toxicity in the Microtox test was confirmed in the second test series (despite the fact that the locations are slightly different). The concentrations of organic pollutants seem too low to explain the observed effects in the Microtox test (see table 13). Arsenic (exceeds MTR) is not a likely explanation, because the highest concentration coincides with the smallest effect (sample 701). Besides, the EC 50 values for the Microtox and Rotox tests are much higher (see table 14). Low oxygen concentrations are not likely, because there were no effects in the Thamnotox and Rotox tests, which have a longer exposure time. However, oxygen cannot be ruled out as cause. Possible explanations for the observed toxicity are: 

- Dissolved sulphide in the samples. Microtox is especially sensitive to sulphide. The highest     toxicity in the second test series coincides with the highest measured sulphide concentration. 

- Other chemicals than the ones that were analysed. 

Table 14. Expected concentrations of some typical contaminants, compared to the toxicity of the substance in the Mircrotoxand Rotox tests. 

 Substance Microtox (μg/L) 

 Rotox (μg/L) Arsenic 4900 (15 min EC 50 ) [22] 12100 (LC 50 , 24h) [48] cis -1,2-Dichloroethene 905,000 [35] Vinyl chloride Tetrachloroethene 4,180 (5 min EC 20 ) [19] 120,000 (5 min EC 20 ) [35] 

- 

 Trichloroethene 42,750 (5 min EC 20 ) [19] 176,000 [35] 

- 

 Benzene Toluene 17,000 (5 min EC 20 ) [19] 19,700 [35] 

- 

 Ethylbenzene 9,680 [35] Xylenes 16,000 (5 min EC 20 ) [19] 9,200* (15 min EC 50 ) [16] 16,000 [35] 

- 

_* m_ -xylene 

The following conclusions can be drawn from the ecotoxicological assessment: 

- The concentrations of pollutants in the anaerobic groundwater at LBC site are higher than the     environmental quality standards (MTR) for surface water. At the LBC-site the greatest hazard     is posed by _cis_ -DCE (1-2 times MTR) and vinyl chloride (< MTR, but higher concentrations     can be reached due to breakdown of _cis_ -DCE). 

- The measured concentrations in the groundwater that passed the NA interface, are smaller     than the MTR for surface water. At the LBC-site the concentrations of organic pollutants are 


 all well below MTR. At the LBC-site however, arsenic at relatively high concentrations (2-6 times MTR) is present. 

- At the LBC-site, the reason for the relatively low measured concentrations is less clear     (possibly, spatial heterogeneity of the groundwater pollution). 

- The bioassays at the LBC-site show the groundwater of all three samples is toxic to one or     more test species. The toxicity cannot be explained by the organochlorine contaminants that     have been analysed. 

- At the LBC-site, other substances are likely to play a role in the observed toxicity. Possible     candidates are arsenic, or sulphide, or other organochlorine pollutants, or degradation     products. 

11.3 **Shell site** 

11.3.1 _Geohydrological modelling_ 

_Introduction_ The NA-interface site provided by Shell is located at Shell Pernis Rotterdam at the harbour named 1e^ Petroleumhaven. At 10 m-bgs, a sandy layer is in contact with the harbour. In geohydrological terms the harbour system is mainly draining water from this layer. In the harbour there is a tide with an amplitude of 0.7 m. Contamination within the influenced zone around the harbour will eventually flow into the harbour while water from distant parts flow vertically towards the deeper aquifers. In the past, the Shell Pernis site as a whole was subject of a geohydrological study [17]. For that purpose a groundwater model was set up that is used in this NA-interface study. This groundwater model was used to calculate the boundary conditions of a more detailed model that zoomed in on the area containing the NA-interface. Figure 28 shows part of the Shell site and the area of the detailed model. The NA-interface is located on the west quay situated on the 1st^ Petroleumhaven. 

Fig. 28. Position of the NA-interface location. 


_Groundwater model Shell_ Basis of the model activity is the calibrated groundwater model for the Shell Pernis location covering 205 km 2 containing model cells of 18x18 m in the centre. The model was used for calculations on a stationary basis. The second and more detailed model for the NA study covers only 0.55 km 2 with cells of 2x2 meter in the vicinity of the NA-interface. Because of the important influence of the tide in the harbour on the processes at the NA-interface this model is developed as a non-stationary model. 

_Geological layering_ Next to the Shell Pernis site one of the other NA-interfaces sites is located: the LBC location. For that reason both locations show a rather similar geohydrology. 

The surface of Shell Pernis has a level of about NAP + 5m. On top we find a sandy antropogenic layer with a thickness of a few meters and a permeable structure. Below that layer a Holocene topayer is found with a thickness of approximately 20m consisting of clayey deposits. Within this layer sandy permeable channel deposits are found that can be grouped in two channel systems. The upper system is part of the younger Duinkerken formation while the deeper and older system is part of Calais formation. The patterns of these systems show irregularity in thickness and extension. Below this layer there is the first main aquifer of about 10m thick with a high permeability. 

The expected NA-interface is located on the interface of the upper channel deposit and the harbour at approximately 10m below the surface level. Because of this depth, the layer is considered confined. 

_Set up of the groundwater model_ In the groundwater model this profile is translated into a model concept of four layers. The details of the Shell Pernis model is described in the report mentioned earlier. It explains the process of calibration of the geohydrological parameters using more than 50 head measurements. These calibrated parameters are used by the development of the small-scale groundwater model to calculate the processes at NA-interface. Also the boundary conditions and information about the local recharge, resistance of sheet piling and the existence of drainage systems is copied. From this point the explanation of the groundwater model is focused on this second and more detailed model. Figure 29 shows the heads and streamlines calculated with the detailed model in a stationary situation. 


Fig. 29. Calculated heads and streamlines for the layer containing the NA-interface. 

_Modelling the tidal influence_ The stages in the harbour are influenced by the tide. The tide is modelled using a mean stage of NAP + 0.35 m, an amplitude of 0.70 m and a period of 12.5 hours. Calculations with the model are performed with the non-stationary model using time steps of 1 hour. For every time step a new stage in the harbour is calculated. 

To be able to model a non-stationary time series of heads and fluxes, an additional model parameter is used: the storage coefficient. This parameter represents the ability of a layer to store an additional amount of water when the water pressure increases. The storage in a phreatic layer is high in comparison to the storage in a confined layer. The consequence can be illustrated by the influence of tidal effects on groundwater heads. In a phreatic layer, the effect of the tide is dimmed out within a short distance (several meters) while the head in a confined layer can react over more than 100 meter. The additional volume of water that is stored within the aquifer during a tidal period determines the temporal variation of the groundwater fluxes. 

_Storage coefficient_ It is important to get realistic values for the storage coefficient because it has effect on the estimation of the flux passing the NA-interface over time. An estimation of the coefficient is based on field measurements of heads in the confined layer. There is a relation between the storage coefficient and the distance at which the dimmed tidal effects are still measured. The expression of this analytical formula is given by: 

 a 

 df = exp− x × π 

 = × S s 

 a T kD 


with: _df_ dim factor of the tidal amplitude (-) _x_ : distance towards the open water (m) _kD_ : transmissivity of the confined layer (m 2 .day-1) _T_ : tidal period (day) 

_S_ (^) _s_ : specific storage coefficient (1/m) For the estimation of S (^) s 11 series of measured heads were analysed. The series were used in a previous study and were taken on several locations on Shell Pernis [18]. Figure 30 shows the results of the calculations. Some locations do not give an estimation of S (^) s because there the confining layer is absent. The results show some differences with a mean estimation of just below 1.10-3^ (1/m). For further calculation with the model the value of 7.10-4^ (1/m) is used. Fig. 30. Estimated Specific storage coefficient based on field measurements. 


 CHAPTER 12 

###### MODEL INVESTIGATIONS 

12.1 **Approach model CHARON** 

12.1.1 _Introduction_ Models are needed for the simulation of sediment diagenesis and pollutant degradation. The diagenesis model delivers the macrochemical conditions such as the dissolved oxygen gradient in the sediment to the pollutant model. Both models may be integrated into one modelling framework or may be operated off-line. 

The selection of appropriate models was based on the perspective that eventually a routinely applicable, comprehensive as well as generic model will be needed for site-specific assessment of the degradation of organic micropollutants. Such a model should facilitate the integrated simulation of water and sediment quality in surface water systems, and should describe all relevant water quality processes including primary production of phytoplankton. However, a highly detailed chemical model is needed in the current stage of research, as was pointed out by model criteria for the selection and formulation of models derived from the description of the natural system in chapter 3 (see the next section). 

In order to satisfy the criteria best, it was decided to use two different models, which were selected and constructed from modelling tools available at Delft Hydraulics: aquatic chemistry model CHARON [5-7] and generic water quality model DELWAQ [55, 56]. These models are very different with regard to concepts and process formulations. In contrast with CHARON, DELWAQ describes only the main macrochemical processes in an approximate way. However, DELWAQ simulates pollutant processes in much more detail. Consequently, CHARON is used as a research tool, whereas DELWAQ will eventually be the operational model for “scenario” simulations. 

CHARON was used to simulate sediment diagenesis in order to obtain accurate gradients of important macrochemical components such as dissolved oxygen. This model was also used to perform a recognaissance with respect to the effects and importance of the degradation and the dispersive dilution of monochlorbenzene. In the next stage DELWAQ was made to reproduce the macrochemical gradients delivered by CHARON. Subsequently, monochlor-benzene was simulated with DELWAQ in a more comprehensive way. 

The models have been curtailed to fit the essential processes in the sediment. The water column was basically dealt with as a constant boundary condition. Both criteria and models are described in the following sections. 

12.1.2 _Criteria for model formulation_ The criteria for formulation of the modelling framework for sediment diagenesis and pollutant degradation are summarised below. These criteria were formulated in view of both the need of a comprehensive water and sediment quality model and a dedicated model for sediment diagenesis. 


_Water quality related criteria:_ 

- Organic matter in various fractions, the settling fluxes of organic matter and water quality     (DO, nitrate, sulphate, ammonium) is imposed as forcing functions. 

- The model allows dynamic simulation of partitioning (adsorption), settling, microbial     degradation and volatilisation of pollutants. 

_Sediment diagenesis related criteria:_ 

- Organic matter in various fractions, electron-acceptors (DO, nitrate, sulphate, iron, etc.),     ammonium, sulphide and methane can be simulated dynamically according to a 1-D vertical     schematisation of the sediment. Substances as iron may currently only be modelled with the     detailed chemical model CHARON. 

- The simulation of the thickness of the various redox layers is accurate by means of     discretisation of the sediment in thin layers (≥ 0.25 mm). 

- Vertical advective transport (infiltration, seepage) and dispersive transport (bioturbation of     solids, and dispersion of dissolved substances by bioirrigation, flow induced turbulence and     molecular diffusion) are included, taking into acount both diurnal (tide) and seasonal     variation. 

- The effects of micro-heterogeneity with respect to redox conditions can be taken into     account. (This is done in DELWAQ by overlapping of the consumption of various     electronacceptors. CHARON provides the option of a 2-D schematisation of the sediment. It     was decided not to study the possible effects of micro-heterogeneity in this stage of     research.) 

- The effects of macro-heterogeneity can be studied with by performing several simulations     with different sediment compositions and porosities. (This was done in as far as necessary to     establish ranges for the penetration of dissolved oxygen into the sediment.) 

_Pollutant’s fate related criteria:_ 

- The partitioning and the microbial degradation of pollutants are simulated dynamically     according to a 1-D vertical schematisation of the sediment. 

- The stimulation and inhibition of microbial degradation depending on the redox conditions,     that is to say the presence of DO, nitrate and/or sulphate is included in the model. 

- The model delivers the pollutant fluxes into the sediment and the overlying water and the     resulting pollutant concentrations in water and sediment in the form of time series. 

- The effects of micro-heterogeneity with respect to microbial degradation can be taken into     account. (As mentioned above, it was decided not to study the possible effects of micro-     heterogeneity in the current research.) 

- The adaption of pollutant degrading bacteria to alternating oxidising and reducing conditions     (lagging effect), the effects of changing salinity on microbial degradation, as well as the fate     of metabolites of pollutants can be included. (It was decided not to study these aspects in     this stage of research.) 

_Pragmatic criteria:_ 

- Those processes and process details that cause second order effects with respect to redox     gradients can be neglected, in view of the present recognaissance study. 

- In the case of the use more than one model, models are mutually consistent with respect to     the driving processes, the degradation of organic matter and the consumption of electron-     acceptors in particular. 

- The efforts needed to extend the existing modelling tools to meet the above criteria, to     produce input and output, and to perform simulations are minimal. 

- The output of the hydrological model of TNO-NITG can be used as input. 

- The presence of shore reinforcement in the form of layers of loosely packed stones or stone     blankets can be taken into account by means of confining the simulations to the uncovered 


 sediment area, and correcting mass flow according to the percentage of sediment covered with stones. 

12.1.3 _Description of CHARON_ 

_The main features_ CHARON is a flexible modelling framework for the dynamic, 0-3D simulation of aquatic (bio)chemical and geochemical problems [5-7]. It combines equilibrium chemistry with slow processes and mass transport (advection and diffusion). The equilibria are calculated on the basis of the mass conservation and mass action laws. The latter states that the chemical system strives for minimisation of the Gibbs free energy. The mass fluxes caused by slow processes can be calculated with various temperature dependent kinetic formulations. The mass exchanges between solid, fluid and gas can be modelled as equilibrium or as slow processes. Fluxes between atmosphere and surface water are generally considered as slow processes, whereas precipitation and dissolution of CaCO 3 is mostly considered as an equilibrium process. The chemical system to be simulated can be composed by the user by means of the definition of substances and components. The latter are the basic combinations of atoms, out of which the molecules of all substances in the model can be built. The user can choose the nature and the number of substances freely. The number of substances is only limited by the acceptable computational burden. CHARON has been used successfully many times for the simulation of layered systems, such as sediment and soil/groundwater systems, in particular for the diagenesis of sediment in aquatic surface water driven by the microbial decomposition of organic matter. All relevant redox, precipitation and adsorption processes can be taken into account. 

_The applied model_ The version of CHARON used is the 1D version. The model contains the active sediment compartment and the overlying surface water compartment. This system is schematised as a column with an horizontal area of 1 m 2 , consisting of one water layer and 25 sediment layers. The total depth of the sediment modelled is 40 cm. It is assumed that below this depth no gradients are present. The uppermost layers are 0.25 mm thick. The thickness increases more or less exponentially with increasing depth, whereas the lower layer 6 cm thick. The model has a boundary below the lowest sediment layer for the upwelling groundwater and an inflow boundary for the surface water. In order to impose a constant water quality as boundary condition the residence time of the water compartment was set at 1 day, the depth of this compartment at 4 meter. The sediment has a lower boundary at the deepest segment (the groundwater), with a constant seepage flow in the Solvay case, and a time-dependent seepage and infiltration flow in the LBC case. 

CHARON simulates the organic and inorganic species, solid and dissolved, which influence the macrochemical system, like pH, redox, oxygen, etc. In the sediment especially the CaCO 3 , the different solid iron species like pyrite (FeS 2 ), siderite (FeCO 3 ) and amorphous iron hydroxide (FeOOH), and the adsorption complex (CEC) are important. Advection and diffusion/dispersion is possible for the liquid phase as well as for the solid phase. The numerical solution of the advection dispersion problem is done in an implicit way, where both dissolved and solid transports are included, as well as the linearisation of the chemistry. If the chemistry is not linear enough within a time step (e.g. a solid substance completely dissolves and does not buffer the system anymore), the time step is reduced automatically to follow the non-linear part of the chemistry. 

Choosing the right initialisation, boundary conditions and process parameters (decay coefficients etc.) is a complicated task. Questions arise such as: What is the infiltration depth of oxygen against an upwelling reduced water? So when the flow field became available, with the intrusion 


velocity of the pollutant in the sediment, the first try out started, to get some feeling for the sensitivity of the model for the initialisation, boundary conditions, etc. 

Processes as diffusion/dispersion and decay determine the concentration profile of an upwelling pollutant at the sediment-water interface. From the results of previous modelling of the sediment water interface with regard to oxygen, phosphorus and nitrogen, the input of the model was determined. It appeared that diffusion/dispersion alone gave a large contribution to the lowering of the concentration of the upwelling pollutant at the sediment-water interface. This phenomenon can also be illustrated with a formula, which gives the relation between the concentration profile and the flow velocity and diffusion dispersion: 

 vx D Cx C C C ./ 2 (^12 )exp = + − − (12.1) 

where: _Cx_ is the concentration at depth x; _C_ 2 is the boundary concentration at the bottom of the column; _C_ 1 is the boundary at the top of the column; _v_ is the flow velocity; _D_ is the diffusion dispersion. 

Assuming a residence time of 1 day for the surface water and a depth of the water of 4 meter, we can calculate the concentration in the surface water. The mass of pollutant transported to the surface water per m 2 of sediment water interface equals the concentration in the groundwater times the seepage flow velocity. For the Solvay site the seepage flow velocity is 0.07 m/day. With a dimensionless concentration of 1 for the pollutant this gives a mass flux of 0.07 units/day. With a residence time of 1 day and a depth of 4 meter, 4 m 3 of water have to transport 0.07 units of pollutant each day, or the concentration will be 0.07/4 = 0.0175 units/m 3 (or 1.75% of the inflowing concentration). For the LBC site the net upwelling flow is only 0.005 m/day, so the net flux is only 0.005 units/day and the outflow concentration will be 0.005/4 = 0.00125 units/m 3. 

Figure 31 shows the profile for the case of molecular diffusion only, calculated with the model and calculated with formula 12.1. From this picture it is clear (Note the logarithmic distance axis) that a large dilution occurs in the uppermost 1 mm, where the concentration goes down from about 50% of the original concentration to about 15% of this concentration. Deviations between the numerical and analytical results are determined by numerical dispersion of the model. 


 concentration profiles 

 0.0000 

 0.1000 

 0.2000 

 0.3000 

 0.4000 

 0.5000 

 0.6000 

 0.7000 

 0.8000 

 0.9000 

 1.0000 

 0.0001 0.001 0.01 0.1 1 depth(meter) 

 concentration 

 Profile numerical model, diffusion profile analytical solution diffusion profile analytical solution(diffusion*10) 

Fig. 31. Concentration profile (mg/l) due to diffusion/dispersion, comparison analytical and numerical. Dept is displayed on a logarithmic scale. 

Unfortunately it is impossible to measure such a profile in the field over such short distances. In the field the diffusion/dispersion will be higher. The figure gives also the profile with a higher diffusion/dispersion. An increase with a factor of 10 will lead to a shift of the profile: the 50% concentration goes down from 1 mm to 1 cm depth, and the concentration in top of the profile goes down to 2.6%. 

So the conclusion was drawn that we probably cannot use the data obtained in the field on pollutant concentration profiles to calibrate the decay. The concentration gradient is mainly determined by dispersion, whereas the vertical resolution with which concentrations are measured is too coarse. Since the field data cannot be used to calibrate the decay coefficients it was decided to determine decay coefficients in laboratory experiments. This was done by TNOMEP (see § 6.2). 

From the first model runs it also became clear that the amount of decay of pollutant in the sediment is very dependent on the infiltration depth of oxygen, assuming that decay is only possible under the presence of oxygen. No data were available to accurately describe oxygen concentration profiles for the Solvay site. For the Solvay case it was shown by measurements that the oxygen penetration was less than 2 cm. 

For LBC there were 3 measurements in the sediment, however 2 of them were smaller than 1 mg/litre and values below 1 mg/liter are mostly considered to be unreliable. 

The oxygen profiles are determined by the oxygen consumption in the sediment in combination with the flow field and diffusion/dispersion. Finally some other substances contribute to the oxygen profile like reduction of oxidators and oxidation of reductors (see chapter 3). The driving force on the oxygen consumption is the decay of organic material in the sediment. 

Organic material finds its origin from loads from industries and/or households, but also as a result of primary production in the surface water. In the sediment also other processes contribute to the 


result of the oxygen profile like oxidation of reduced compounds from the deeper layers in the sediment, like methane and iron sulfides and reduction of oxidised compounds like nitrate, sulphate and iron hydroxides. For an accurate description of all these processes a lot of information has to be available, in a detailed scale in the depth. 

The data is limited to the solid phase for the Solvay case. From these data it was concluded that the solid material mainly consists of sandy material (81% SiO 2 ) and some feldspars or clay material (3.5 till 5% of Al 2 O 3 ) and a little bit of CaCO 3 (about 6%). The measurements showed rather low values for organic matter (between 0.3 and 0.5%) and iron (0.5% of Fe 2 O 3 ). This is probably caused by the fact that the research ditch was relatively recently excavated (summer 2001). Since the origin of the organic material in this rather young sediment was unknown, it was difficult to determine an appropriate decomposition rate. For that reason we decided to set the input parameters in such a way that we did get a realistic range of the oxygen consumption rate. This was done by: 

- varying initial organic matter content in the sediment: between 0.1 and 0.4% total dry weight,     equally divided between fast and slow decaying material; 

- by varying decomposition rate: between 0.01 and 0.04 d -1^ for the fast decaying organic     matter and between .001 and .004 d -1^ for the slowly decaying part of the organic matter. 

In all cases the flux of organic material from the surface water to the sediment was chosen in such a way that the amount of organic material in the sediment is more or less constant, in agreement with the steady state assumptions. 

Note: the oxygen consumption is not an input parameter, but is calculated by the model as result of decay of organic material and all other redox processes. Six scenarios’s for oxygen consumption rates were set up. The final calculated consumption rates vary from 0.44 till 4.85 grams of O 2 /m 2 /day. The value of 4.85 is rather high; the value of .44 is a very low value. The oxygen penetration depth is also dependent on the diffusion/dispersion factor (and of course on the vertical flow in the sediment). Two diffusion dispersion profiles were used, one with a factor 5 times molecular diffusion at top of the profile and molecular at the bottom of the profile, and one with 15 time molecular at top of the profile and 3 times molecular at the bottom of the profile (bioirrigation, modeling experience). 

Since no time dependent information was available, combined with the fact that we already were using oxygen consumption rate scenarios, we also decided to do steady state calculations. In that case we are independent of initialisations, which is a tedious task. This implies that we run the model for such a period that under constant boundary conditions we do not observe any changes (in time) in calculated profiles. For the LBC site the lower boundary is a cycle of infiltration and seepage flows, so not constant in time. This also implies that no constant profile develops but that we get a so called “steady limit cycle”, the profile changes in time but repeats itself each flow period. 

All processes, which can influence the redox profile, are taken into account. But since we only modelled a steady state profile some of them are not important, like the reactions with solid iron minerals: pyrite (reduced) and iron hydroxide (oxidised). These reactions influence the time dependent penetration depth of substances like O 2 and NO3-, but are not important for a steady state profile. We also did not model adsorption of the pollutant. In the steady state the dissolved profile is independent of any adsorption processes. With adsorption it takes more time to reach the steady state profile. 

Several processes are temperature dependent, since we only modelled one steady state profile; the temperature was set at 11o^ Celsius, which is the average temperature in the sediment. 


The decay of pollutant is dependent on the oxygen concentration in the sediment. We used the next formula for the first order decay rate of the pollutant: 

 Rateact = Ratesat ( oxygact / oxygsat ) (12.2) 

where: _Rateact_ is the actual applied decay rate; _Ratesat_ is the measured decay rate at oxygen saturation; _Oxygact_ is the actual O 2 concentration; _Oxygsat_ is the saturation concentration. 

This formula results in a linear decrease of rate of decay with a decrease in percentage of oxygen saturation and zero decay in the absence of oxygen. 

_Model input_ The model was run for all cases for 25 days, which is the time needed to get at a steady state with regard to the oxygen and pollutant profile in the sediment. Since we did calculate a steady state profile under different oxygen consumption scenarios, a lot of the necessary initialisation choices and parameters settings are not decisive any more if they only influence the non steady state behaviour, which for instance is the case for the iron chemistry. The conversion of iron hydroxide to pyrite and reversely, flattens the variation in oxygen penetration depth, which normally occurs during the season, mainly because of the temperature dependency of the decay of organic material. 

The following settings were used: 

- The surfacewater is assumed to be in equilibrium with the atmosphere with regard to O 2 and     CO 2. 

- The boundary condition for the surface water is saturated with O 2. 

The boundary condition for the surface water for NO (^) 3-^ was set 0.32 mgN/l (Denitrification in the sediment is equivalent to an oxygen flux to the sediment). 

- The boundary condition for the groundwater is zero oxygen, but without reduced components     (like CH 4 ). 

- The boundary for the pollutant in the groundwater is 1 (mass unit/m^3 ). 

- The temperature is constant in time and depth, 11 °C. 

- We used four decay rates for the pollutant: 

- 0/day, which gives the reference for no decay of pollutant; 

- 0.3/day, which is about the literature value for a lot of these pollutants; 

- 12/day and 53/day, which are the temperature corrected values for values found in the     batch experiments from TNO/MEP. 

- We assumed no decay of pollutants in the surface water. 

- We used two diffusion/dispersion profiles: one with a factor 5 times molecular diffusion at top     of the profile and molecular at the bottom of the profile, and one with 15 time molecular at top     of the profile and 3 times molecular at the bottom of the profile. 

- All other chemicals were set at fresh water values for the Solvay case and the lower     boundary for the LBC case, while the surface water for the LBC case was set at seawater     levels. But in the present calculations these values have no influence on the steady state     profiles for oxygen and the pollutant. 

- The upwelling velocity in the Solvay case is 0.07 m/day, for the LBC case we used the     middle scenario (1.3 m on horizontal plan) with a period of 0.5208 days divided into 12     intervals of 0.0434 day with the highest upwelling velocity of 0.124 m/day and the highest     downwelling velocity of 0.105 m/day. The mean velocity is upwelling with 0.005 m/day. 


12.1.4 _Description of DELWAQ_ 

_The main features_ DELWAQ [55, 56] is a flexible modelling framework for the dynamic, 0-3D simulation of water and sediment quality. Eutrophication, oxygen/BOD and pollution issues are among the many water quality problems that have been studied using this modelling framework. DELWAQ combines slow physical and (bio)chemical processes and mass transport (advection and diffusion) on the basis of mass conservation. (Near) equilibrium processes can be taken into account by means of equilibrium partitioning or very fast process kinetics. The process rates can be calculated with various temperature dependent kinetic formulations. The mass exchange between atmosphere and water and between solids and water are also taken into account. The substances to be simulated are chosen from a predefined list, but this puts no limit to the number of micropollutants that can be simulated. The process formulations are selected from a predefined set of process routines, but if desirable new routines can be added easily because of DELWAQ’s modular structure. DELWAQ has been used successfully in a great variety of modelling studies concerning water quality of all kinds of surface water systems. 

_The applied model Overview of substances and processes_ The DELWAQ-version applied is known as DELWAQ-G [42]. The simulated substances are particulate and dissolved organic matter (C, N, P), dissolved oxygen, nitrate, ammonium, sulphate, dissolved sulphide, particulate sulphide, methane and an organic micropollutant. Particulate organic matter is described with three fractions, each having a different decomposition rate. The water and sediment quality processes included in the model are: 

- Decomposition of organic matter (DECFAST, DECSLOW, DECREFR, DECDOC); 

- Consumption of electron acceptors oxygen, nitrate, sulphate and production of methane at     the mineralisation of organic matter (CONSELAC); 

- Nitrification (NITRIF_NH4); 

- Oxidation of sulphide (OXIDSUD); 

- Precipitation and dissolution of sulphide (PRECSUL, SPECSUD); 

- Oxidation of methane (OXIDCH4); 

- Ebullition of methane (EBULCH4); 

- Volatilisation of methane (VOLATCH4, SATURCH4); 

- Reaeration of dissolved oxygen (REAROXY, SATUROXY); 

- Degradation of the micropollutant (LOS_WK_OMP); and 

- Partitioning (sorption) of the micropollutants among water and organic matter     (PARTWK_OMP). 

The rates of these processes are generally temperature dependent according to: 

 k = k^20 × kt ( T −^20 ) (12.3) 

with: _k_ = proces rate (g.m^3 .d) _kt_ = temperature coefficient (-) _T_ = temperature ( oC) 

The mass transport processes implemented in DELWAQ-G concern: 

- advection of particulate substances by burial and digging; 

- advection of dissolved substances by seepage; 

- dispersion of particulate substances by bioturbation; and, 

- dispersion of dissolved substances by bio-irrigation and diffusion. 


_Formulations for macrochemical processes_ The background and the kinetics of the macrochemical processes are extensively described in reference [42]. A brief summary is presented below for most of the processes. No attention is paid to the volatilisation and reaeration processes, because they do not effectively affect the overlying water concentrations since the composition of the water column is a forcing function. The decomposition of dead organic matter (detritus) is described as the serial mineralisation and conversion of four fractions. Each mineralisation flux has a proportional conversion flux. Mineralisation implies the release of ammonium and phosphate. The mineralisation rate has been formulated as the following first-order kinetic process: 

 Rmin = fel × facc × kmin × Cx (12.4) 

with: _Cx_ = organic carbon, nitrogen or phosphorus concentration (g C/N/P.m -3) _facc_ = acceleration factor for nutrient stripping (-) _fel_ = limiting factor for electron acceptors (-) _kmin_ = first-order mineralisation rate (d-1) 

The consumption of the electron-acceptors and methanogenesis are coupled to the mineralisation of organic matter. The relative contributions of the electron-acceptors oxygen (OXY), nitrate (NO 3 ), sulphate (SO 4 ) and carbon dioxide depend on Michaelis-Menten kinetics for limitation and inhibition. Carbon dioxide is not included in the model. However, for methanogenesis, the consumption of carbon dioxide is equal to the production of methane (CH 4 ). The formulations are as follows: 

   

    

  + × 

 × − + × 

 = − − 

 − φ 1 1 φ 

 1 1 i i 

 i i i 

 i 

_i_ (^) _Ce Ksi Ce Ce Ksl Ce fli_ (12.5) 

# ∑ 

 = 

 = 

= (^) _in i i i i fli frli fli_ 1 (12.6) _Rcns_ (^) _i_ = _ai_ × _frlii_ × _Rtm in_ (12.7) with: _ai_ = stochiometric reaction constant of electron-acceptor i (g EA.g C-1) or of methane (g C.g C-1) _Cei_ = concentration of electron-acceptor i (g EA.m-3) _fli_ (^) _i_ = limitation and inhibition function for electron-acceptor i _frli_ (^) _i_ = fraction of the organic matter degradation process connected with consumption of electron-acceptor i _Ksl_ (^) _i_ = half-saturation concentration of electron-acceptor i for limitation (g EA.m-3) _Ksi_ (^) _i-1_ = half-saturation concentration of electron-acceptor i-1 for inhibition (g EA.m -3) _Rcns_ (^) _i_ = consumption rate of electron-acceptor i (g EA.m -3.day-1) or production rate of methane (g C.m-3.day-1) _Rtmin_ = total mineralisation rate of organic matter (g C.m-3.day-1) φ = porosity (-) _i_ = index for the electron-acceptor or methane (n=4 in the current implementation) The sum of fractions _frli_ (^) _i_ is equal to one. The reduction of oxygen is of course only subjected to a limitation function, methanogenesis only to an inhibition function. This approach allows the overlap of all reduction processes in each layer at the same time. 


Ammonium (NH 4 ) is converted into nitrate (NO 3 ) by means of nitrification. The rate can be characterised with: 

   

    

  × + ×  

    

  × + 

 = × Ksox Cox 

 Cox Ksam Cam 

 Cam R knit φ φ 

 (12.8) 

with: _Cam_ = dissolved nutrient concentration, ammonium or nitrate (g N.m-3) _Cox_ = dissolved oxygen concentration (g O 2 .m -3) _knit_ = kinetic constant (g N.m-3.day-1) _Ksam_ = half saturation constant for ammonium (g N.m-3) _Ksox_ = half saturation constant for oxygen (g O 2 .m -3) _R_ = rate of nitrification or denitrification (g N.m-3.day-1) 

The sulphide oxidation rate is formulated as follows: 

 φ φ φ ×  

    

  ×  

    

  = × 

 Csud Cox Roxi koxi (12.9) 

with: _Csud_ = total dissolved sulphide concentration (g S.m -3) _koxi_ = pseudo second-order sulphide oxidation rate (g O2-1.m 3 .d) _Roxi_ = rate of sulphide oxidation (g S.m-3.d-1) 

The precipitation of sulphide (SUD) and the dissolution of particulate sulphide (SUP) is described with: 

 Rprc = 32000 × kprc ×( Csd − Csde )× φ if Csd ≥ Cdse (12.10) 

 Rdis = 32000 × kdis ×( Csde − Csd )× φ if Csd < Cdse (12.11) 

with: _Csd_ = dissolved free sulphide concentration (mole.l -3) _Csde_ = equilibrium dissolved free sulphide concentration (mole.l -3) _kdis_ = dissolution reaction rate (d-1) _kprc_ = precipitation rate (d-1) _Rdis_ = rate of dissolution (g S.m-3.d-1) _Rprc_ = rate of precipitation (g S.m-3.d-1) 

Equations 12.10-11 require the free dissolved sulphide concentration, which is calculated from the simulated total dissolved sulphide concentration (SUD) and the chemical equilibrium between S 2-^ , HS -^ and H 2 S. The calculations need the pH and two equilibrium constants as input parameters. 

Microbial methane oxidation with dissolved oxygen is modelled with: 

   

    

  × + ×  

    

  × + 

 = × Ksox Cox 

 Cox Ksch Cch 

 Roxi koxi Cch 4 φ 4 φ 

(^4) (12.12) 


with: _Cch_ 4 = dissolved methane concentration (g C.m -3) _koxi_ = Michaelis-Menten rate for oxidation with dissolved oxygen (g C.m -3.d-1) _Ksch_ 4 = half saturation constant for methane consumption (g C.m -3) _Ksox_ = half saturation constant for dissolved oxygen consumption (g O 2 .m -3) _Roxi_ = methane oxidation rate with DO (g C.m-3.d-1) 

A similar relation describes the oxidation with sulphate. This process does not occur when the dissolved oxygen concentration is above a certain critical value. 

The ebullition of methane (CH 4 ) is formulated as the total removal of methane produced in excess of saturation, which is a function of water depth and sediment temperature. The methane ebullition flux follows from: 

   

    

  ∆ 

 − = × t 

 Cch Cch s Rebu f 

 4 / φ 4 (12.13) 

with: _Cch_ 4 _s_ = methane saturation concentration (g C.m -3) _f_ = scaling factor (-) Rebu = rate of methane ebullition (g C.m-3.d-1) ∆ _T_ = time step in DELWAQ (day) 

_Formulations for mass transport_ The formulations of the transport processes are described in detail in reference [42]. A brief discription is given here for upwelling and dispersion. Burial and digging do not occur in the applied model. Upwelling and downwelling are both called seepage. The seepage advective flux is: 

 φ 

 vd fd C 

_Fadv_ (^) _d_ × × = (12.14) with: C = bulk concentration of a substance (g.m-3) _Fadv_ (^) _d_ = dissolved advection flux (g.m-2.day-1) _fd_ = dissolved fraction of a substance (-) _vd_ = volumetric seepage velocity (m.day-1) Bioturbation by benthic organisms causes the dispersion of particulate substances. The pertinent dispersion flux is approximated with: 

#### ( ) 

#### ( ( ) ( )) 

#### ( 1 2 ) 

 1 1 , 1 2 1 1 /^1122 /^12 L L 

 fp C fp C 

_Fdis_ (^) _p max Dp_ + × − − × − = − − × × φ φ φ φ (12.15) with: _Dp_ = particulate dispersion coefficient (m 2 .day-1) _Fdis_ (^) _p_ = particulate dispersion flux (g.m-2.day-1) _fp_ = particulate fraction of a substance (-) _L_ = half dispersion length (m) indexes 1 and 2 refer to two adjacent segments. 


Benthic organisms also cause bio-irrigation, the dispersion of dissolved substances. The pertinent dispersion flux follows from: 

#### ( ) 

#### ( ) 

#### ( 1 2 ) 

 1 ,^211 /^122 /^2 L L 

 fd C fd C 

_Fdis_ (^) _d min Dd_ + × − × = × × φ φ φ φ (12.16) with: _Dd_ = diffusion or dispersion coefficient (m 2 .day-1) _Fdis_ (^) _d_ = dissolved dispersion flux (g.m-2.day-1) _fd_ = dissolved fraction of a substance (-) The above transport processe have been implemented in DELWAQ-G on the basis of the conservation of porosity. _Formulations for micropollutant processes_ The formulations of the micropollutants processes are described in reference [42]. The essentials of the formulations are dealt with below. For reasons mentioned above no attention is paid to volatilisation. The degradation rate for a specific compartment is equal to: _R_ deg = _k_ 1 deg× _fr_ deg× _Cmpt_ (12.17) with: _Cmpt_ = total micropollutant concentration (g.m-3) _fr_ deg = fraction subjected to degradation (-) _k_ 1deg = first order degradation rate (d-1) _R_ deg = degradation rate (g.m-3.d-1) The degradation rate is equal to the rate for oxidising conditions when the dissolved oxgen concentration exceeds a certain low critical value. Otherwise, it obtains the rate for reducing conditions. The fraction subjected to degradation is in this case equal to the freely dissolved micropollutant fraction. The partitioning of the micropollutant is computed with: 

#### Kppoc ( Cpoc Xdoc Cdoc ) Kpalg Calg 

 fdf + × + × + × 

 = φ 

 φ (12.18) 

#### ( ) 

#### Kppoc ( Cpoc Xdoc Cdoc ) Kpalg Calg 

 Kppoc Xdoc Cdoc fdoc fdf × + × + × 

 × × = 1 − × (12.19) 

#### ( ) 

#### Kppoc ( Cpoc Xdoc Cdoc ) Kpalg Calg 

 Kppoc Cpoc fpoc fdf × + × + × 

 × = 1 − × (12.20) 

### fal g = ( 1 − fdf − fdoc − fpoc ) (12.21) 

with: _Calg/poc/doc_ = concentration of algae biomass, dead particulate organic matter matter, and dissolved organic matter (g C.m-3b) _falg/poc/doc_ = fraction of a micropollutant adsorbed to algae, dissolved organic matter, dead particulate organic matter (-) _fdf_ = freely dissolved fraction of a micropollutant (-) _Kpalg/poc_ = partition coefficient for algae and dead particulate organic matter (m 3 w.g C-1) _Xdoc_ = adsorption efficiency of DOC relative to POC (-) 


Algae biomass is not included in the applied model. The fractions of the dissolved and adsorbed species add up to one, whereas _falg_ is equal to zero. 

_Model input_ DELWAQ has been applied for the Solvay case only. The geometrical, hydrological and water quality boundary conditions are basically the same as in the simulations with CHARON. Yet, some differences exist that mainly relate to the differences between the models. 

The Solvay case concerns a 4 m deep water layer overlying a 0.4 m thick sandy sediment layer. The layer has a constant porosity of 0.5 and a low organic matter content of approximately 0.4% dry matter. The sediment layer consists of 19 sublayers, thin at the top and thick at the bottom (6x1, 5x2, 2x4, 2x30, 2x50, 2x100 mm). The water layer acted as a forcing function. A constant overlying water quality was imposed by means of flushing with water of a constant composition. The effective residence time of the water column was 1 day only. An upwelling flow of 0.07 m per day is imposed on the lower boundary of the sediment layer. 

Table presents the concentrations imposed on both the overlying water and the pore water in the lower sediment boundary. All concentrations are bulk concentrations, which means that the pore water concentrations are in fact two times as high at porosity 0.5. 

Table 15. Concentrations imposed on the boundaries. 

 Substance Overlying water Concentration (g.m -3^ ) 

 Sediment boundary Concentration (g.m -3^ ) 

 Organic micropollutant (monochlorobenzene) Dissolved oxygen (OXY) Nitrate N (NO 3 ) Ammonium N (NH4) Sulphate S (SO 4 ) Dissolved sulphide (SUD) Precipitated sulphide (SUP) Methane C (CH 4 ) Fast dec. part. organic matter C (POC1) Slowly dec. part. organic matter C (POC2) Refr. part. organic matter C (POC3) Refr. dissolved organic matter C (DOC) Fast dec. part. organic matter N (PON1) Slowly dec. part. organic matter N (PON2) Refr. part. organic matter N (PON3) Refr. dissolved organic matter N (DON) Particulate inorganic matter (IM1) 

 0.0 10.56 0.32 0.5 150.0 0.0 0.0 0.0 3.0 1.5 0.5 5.0 0.48 0.24 0.08 0.25 1.0 

 1.25 0.0 0.0 0.0 50.0 0.0 0.0 0.0 10.0 40.0 1950.0 5.0 3.2 12.8 304.0 0.2 1300000.0 


Table 16. Input parameters for the decomposition of organic matter, electron-acceptor consumption and methanogenesis in DELWAQ-G. 

 Name Process / Definition of parameter Value Units Decomposition of organic matter 

 ku_dFdec20 kl_dFdec20 ku_dSdec20 kl_dSdec20 ku_dprdec20 kl_DOCdec2 0 a_dNpr a_dPpr b_dts b_dtpr b_dtdr 

 max. first-order min. rate fast decomp. detr. at 20 o^ C max. first-order min. rate slow dec. detr. at 20 o^ C min. first-order min. rate fast decomp. detr. at 20 o^ C min. first-order min. rate slow dec. detr. at 20 o^ C first-order min. rate part. refractory detr. at 20 o^ C first-order min. rate diss. refractory detr. at 20 o^ C stoch. constant nitrogen in refractory detritus stoch. constant phosphorus in refractory detritus conv. fraction fast dec. detr. into slow dec. detr. conv. fraction slow dec. detr. into part. refr. detr. conv. fraction slow dec. detr. into diss. refr. detr. 

 0.02 0.02 0.002 0.002 0.0002 0.0002 0.03 0.003 1.0 0.4 0.04 

 d -1 d -1 d -1 d -1 d -1 d -1 g N.g C-1 g P.g C-1 

- 

- 

- 

 Consumption of electron-acceptors, methanogenesis 

 CoxRedInh CoxMetInh CniMetInb KsOxCon KsNiDen KsSuRed KsOxDenInh KsNiRedInh KsSuMetInh 

 critical diss. oxygen conc. inhibition of sulphate red. critical diss. oxygen conc. inhib. of methanogenesis critical nitrate conc. inhibition of methanogenesis half saturation constant for oxygen limitation half saturation constant for nitrate limitation half saturation constant for sulphate limitation half sat. const. for DO inhibition of denitrification half sat. const. for nitrate inhib. of sulph. reduction half sat. const. for sulphate inhib. of methanogenesis 

 0.2 0.02 0.1 2.0 2.0 2.0 0.2 0.2 0.2 

 g O 2 .m -3 g O 2 .m -3 g N.m -3 g O 2 .m -3 g N.m -3 g S.m -3 g O 2 .m -3 g N.m -3 g S.m -3 

The process coefficients used are presented in tables 16-18. The temperature dependencies of the process rates (input values for 20 oC) have been omitted from these tables. The temperature coefficients are 1.047 for organic matter decomposition and 1.07 for all other processes. A constant temperature of 11 oC was imposed on the model. 

The coefficients were estimated on the basis past DELWAQ simulations for the eutrophication of surface water systems. Little effort was made to calibrate the coefficients for the redox, precipitation and dissolution processes. This is justified considering the fact that the simulation concerns the steady state situation. The steady state penetration of oxygen into the sediment is practically independent of the rates of these processes. 


Table 17. Input parameters for the processes of ammonium, sulphide and methane in DELWAQ-G. 

 Name Process / Definition of parameter Value Units Nitrification 

 RcNit20 KsAmNit KsOxNit 

 MM nitrification rate half saturation constant for ammonium limitation half saturation constant for oxygen limitation 

 50.0 0.5 1.0 

 gN.m -3^ .d -1 gO 2 .m -3 gN.m -3 

 Oxidation, precip., dissolution, speciation of sulphide 

 CoxSUD RcSox20 DisSEqFeS RcDisS20 RcPrecS20 pKhs pKh2s pH 

 critical dissolved oxygen concentration pseudo second-order sulphide oxidation rate at 20 o^ C eq. dis. free sulphide conc. for amorph. iron sulphide dissolution reaction rate precipitation reaction rate neg. log. of eq. constant for HS-^ (see directives!) neg. log. of eq. constant for H 2 S (see directives!) acidity 

 0.0 25.0 10 -9 10 6 10 6 -14.0 -7.1 7.5 

 gO 2 .m -3 

gO (^) 2-1^ .m 3 .d -1 mole.l-1 d -1 d -1 -log(l.mole -1^ ) -log(l.mole -1^ ) 

- 

 Oxidation of methane 

 CoxMet CsuMet RcMetOx20 RcMetSu20 KsMet KsOxMet KsSuMet 

 critical DO concentration for methane oxidation critical sulphate concentration for methane oxidation MM-rate for methane oxid. with oxygen at 20 o^ C MM-rate for methane oxid. with sulphate at 20 o^ C half saturation constant for methane consumption half saturation constant for DO consumption half saturation constant for sulphate consumption 

 2.0 0.0 1.0 1.0 0.5 1.0 1.0 

 gO 2 .m -3 gS.m -3 gC.m -3^ .d -1 gC.m -3^ .d -1 gC.m -3 gO 2 .m -3 gS.m -3 

Table 18. Input parameters for the processes of the organic micropollutant (monochlorobenzene). 

 Name Process / Definition of parameter Value Units Degradation 

 RcDegOOM P RcDegROM P CoxPart 

 first-order degr. rate at oxid. cond. And at 20 oC first-order degr. rate at red. cond. and at 20 oC critical dissolved oxygen concentration 

 100.0 0.0 0.25 

 d -1 d -1 g.m -3^ b 

 Partitioning (sorption) 

 lKpocOMP XDOCOMP 

 partition coefficient for POC adsorption efficiency of DOC relative to POC 

 2.5 0.2 

(^10) log (L.kg C(^1) ) 

- 

The settling of particulate organic matter is established in the model by means of a settling velocity of 0.033 m.day -1. This velocity is small but yet realistic for the net settling of organic detritus. It was selected in order to achieve a rather low sediment oxygen demand of approximately 0.44 g.m -2.day-1, the lower estimate used in the simulations with CHARON. In 


order to maintain a constant porosity the settling velocity of particulate inorganic matter was set to zero. The dispersion of particulate and dissolved substances is established by the turbation activity of benthic organisms. The bioturbation dispersion coefficient for particulate matter varies linearly over depth from 1.5 to 0.5 10 -6^ m 2 .day-1. The bio-irrigation dispersion coefficient for dissolved substances varies varies linearly over depth from 15.0 to 5.0 10 -4^ m 2 .day-1. This is approximately 15 to 5 times the molecular diffusion coefficient. The higher values are imposed at the sedimentwater interface. 

The composition of the sediment was initialised in the following way. A simulation was made for a period of at least two years. The sediment composition resulting at the end of a simulation was imposed on the model as initial condition. This procedure was repeated until steady state was achieved. 

12.1.5 _Model investigations with CHARON_ 

_Dissolved oxygen penetration and pollutant degradation_ The steady state profiles for the Solvay case are the concentrations calculated at the end of a simulation period of 25 days. In the LBC case we get a steady limit cycle. We get the highest concentration of pollutant at the highest upwelling velocity and the lowest concentration of pollutant at the highest downwelling velocity. The presented concentrations will be the average of those last two calculated. Only the simulation results for oxygen and the micropollutant pollutant are presented. 

Table 19 contains a summary of all results. It presents data for 6 different values of oxygen consumption (in grams O 2 /m 2 /day) and four different cases: Solvay and LBC, with low and high diffusion/dispersion. It contains 5 parts: 

- The first part gives the penetration depth of O 2 in mm; 

- The second part gives the percentage of pollutant in the uppermost layer with decay not     occurring; 

- The other three parts give the extra contribution to the lowering of the uppermost     concentration as a result of decay also in percentage. 

In order to assist the interpretation of table 19 we provide the following example. With the oxygen use of 0.44 grams/m 2 /day the penetration depth of oxygen in the Solvay case with high dispersion is 10.0 mm (part 1 of the table). Without decay the concentration in the uppermost layer is 2.9 percent of the incoming concentration (part 2 of the table). If we have a decay of 12/day this concentration will diminish further with 18.5 percent, or the contribution of decay to the diminishing of the flux will be 18.5 percent (part 4 of the table). 

It is obvious that low oxygen consumption results in a higher penetration depth for oxygen and hence a higher contribution of the decay of the pollutant. It is also obvious that without decay there is a considerable reduction in concentration of the pollutant in the top of the sediment profile. The concentration decrease is larger in the LBC case than in the Solvay case. In the LBC case the cycling of upwelling and downwelling gives an extra contribution to dispersion, while also in the LBC case the net upwelling flow and hence the net mass transport of pollutant per unit time is much lower. As a result diffusion/dispersion has “more time” to lower the concentration. 


Table 19. Results for oxygen and pollutant for all cases. 

**Part1** Oxygen penetration depth (mm) Oxygen use Solvay High Disp Solvay Low Disp LBC High Disp LBC Low Disp 0.44 10.0 4.8 36.0 26.0 0.88 8.0 2.5 26.0 18.5 1.22 6.3 2.5 18.5 13.5 1.76 4.8 1.8 18.5 13.5 2.42 3.5 1.3 13.5 8.0 4.85 1.8 0.6 8.0 4.8 

**Part2** Decay=0 Percent concentration upper layer of sediment Oxygen use Solvay High Disp Solvay Low Disp LBC High Disp LBC Low Disp 0.44 2.9 5.0 0.4 0.5 0.88 2.9 5.0 0.4 0.5 1.22 2.9 5.0 0.4 0.5 1.76 2.9 5.0 0.4 0.5 2.42 2.9 5.0 0.4 0.5 4.85 2.9 5.0 0.4 0.5 

**Part3** Decay=0.3/day Percent contribution of decay in diminishing flux Oxygen use Solvay High Disp Solvay Low Disp LBC High Disp LBC Low Disp 0.44 0.5 0.2 4.4 2.6 0.88 0.3 0.1 1.4 0.8 1.22 0.2 0.1 0.8 0.4 

1.76 0.1 0.0 0.6 0.4 2.42 0.1 0.0 0.3 0.2 4.85 0.0 0.0 0.3 0.2 

**Part4** Decay=12/day Percent contribution of decay in diminishing flux Oxygen use Solvay High Disp Solvay Low Disp LBC High Disp LBC Low Disp 0.44 18.5 8.8 70.0 50.5 0.88 11.0 4.7 38.0 22.9 

1.22 7.4 2.9 22.3 12.6 1.76 5.2 2.1 17.1 10.7 2.42 3.2 1.2 9.9 5.9 4.85 1.2 0.4 4.1 3.0 

**Part5** Decay=53/day Percent contribution of decay in diminishing flux Oxygen use Solvay High Disp Solvay Low Disp LBC High Disp LBC Low Disp 

0.44 54.5 31.5 95.6 84.4 0.88 37.5 18.4 74.0 50.3 1.22 27.2 11.9 53.4 30.5 1.76 20.2 8.6 43.8 26.1 2.42 13.1 5.2 28.7 16.1 4.85 5.0 1.8 13.8 8.9 


Figure 32 gives the results for the Solvay case with low oxygen consumption and high diffusion dispersion, for the no-decay calculation, the 12/day and the 53/day decay calculation. This is the case where the contribution of the decay is the largest of all calculations for Solvay (54.5% for the 53/day calculation). 

 Solvay, decay=0/day,decay=12/day;decay=53/day, oxyg = .44, high dispersion 

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

 0.0001 0.001 0.01 0.1 1 depth (meter) 

 concentration 

 pollutant no decay pollutant decay = 53/day pollutant decay = 12/day oxygen high dispersion 

Fig. 32. Pollutant and oxygen profiles (mg/l) for Solvay at the lowest oxygen consumption. Dept on a logarithmic scale. 

 Solvay, decay=0/day,decay=12/day;decay=53/day, oxyg = .44, high dispersion 

 0.01 

 0.1 

 1 0.0001 0.001 0.01 0.1 1 

 depth (meter) 

 concentration pollutant no decay pollutant decay = 53/day pollutant decay = 12/day oxygen high dispersion 

Fig. 33. Pollutant and oxygen profiles (mg/l) for Solvay at the lowest oxygen consumption. Both concentration and depth on a log scale. 


 Solvay, decay=0/day,decay=12/day;decay=53/day, oxyg =1.76, high dispersion 

 0.01 

 0.1 

 1 0.0001 0.001 0.01 0.1 1 

 depth (meter) 

 concentration pollutant no decay pollutant decay = 53/day pollutant decay = 12/day oxygen high dispersion 

Fig. 34. Pollutant and oxygen profiles (mg/l) for Solvay at the a “reasonable” oxygen consumption rate of 1.76 grams of O 2 /m 2 /day. Both concentration and depth on a log scale. 

 LBC, decay=0/day,decay=12/day;decay=53/day, oxyg = .44, high dispersion 

 0.0001 

 0.001 

 0.01 

 0.1 

 1 0.0001 0.001 0.01 0.1 1 

 depth (meter) 

 concentration 

 pollutant no decay pollutant decay = 53/day pollutant decay = 12/day oxygen high dispersion 

Fig. 35. Pollutant and oxygen profiles for LBC at the a low oxygen consumption rate of 0.44 grams of O 2 /m 2 /day. Both concentrations and depth on a log scale. 

To clarify even further what the differences between the concentrations are at top of the profile, the figure can also be given with a logarithmic concentration axis as is given in figure 33. For comparison we also give the results for a higher oxygen consumption rate of 1.76 grams of O 2 /m 2 /day, which is still a reasonably low value (figure 34). Finally, we present the results for the LBC case with the highest contribution of decay in figure 35. 

_Sensitivity analysis_ At the assessment of the simulations presented above it was concluded that the assumption of a steady state profile for oxygen in the LBC case was not correct from a theoretical point of view. 


The oxygen front goes up and down in the profile with the tidal movement, whereas in the case of retardation of the pollutant the movement of the pollutant front lags behind. This gives potentially higher possibilities for oxidation of the pollutant. However, the movement of the oxygen front gives also possibilities for iron reduction and oxidation. So we made a sensitivity analysis in a simple case to study this phenomenon. 

The simple case is a column of 1 m 2 with 25 segments; each segment is 2 mm thick. So the whole column is 5 cm thick. There is during a half day an upwelling flow of 0.04 m 3 and during a half day a downwelling flow of 0.02 m 3. On the upperside we have a boundary with saturated oxygen and zero pollutant. On the lower side the boundary for the pollutant has a concentration of 1 mass unit and zero oxygen. This implies that the flux of pollutant at the lower boundary equals 1.0(M/m^3 ) * 0.04(m 3 /day) = 0.04 M/day during a half day of upwelling or 0.02 M/day for the whole day. The decay rate of organic matter is set at such a rate that in the whole column there is an oxygen consumption of 0.4 grams/m 2 /day. 

We performed simulations for 8 scenarios. We used two adsorptions for the pollutant, a high adsorption where there is 10 times as much pollutant in the solid phase as in the liquid phase (per unit of total volume) and a low adsorption where this ratio is 1. We used two disffusion/dispersion rates: a zero diffusion/dispersion and a diffusion dispersion over the whole profile of .0004 m 2 /day. With zero diffusion/dispersion the tidal cycle is divided over 40 steps, with diffusion/dispersion it is divided over 500 steps. Two of the scenarios concern iron: one without iron and one with 0.3% iron, initialised as FeOOH (oxidised form) but with the possibility to convert it to FeS (reduced form). All calculations were made for a period of 20 days in order to establish the steady limit cycle. 

Figure 36-39 present the scenario results for the calculated fluxes. The two cases without dispersion and without iron (the first two bars in the graph) are different because of the higher adsorption in the second case. Figure 37 gives the oxygen concentrations for the upper 9 segments. 

 COMPARISON OF FLUXES 

 0 

 10 

 20 

 30 

 40 

 50 

 60 

 no disp,low adsorption,no Fe 

 no disp,high adsorption,no Fe 

 with disp,low adsorption,no Fe 

 with disp,high adsorption,no Fe 

 no disp,low adsorption,with Fe 

 no disp,high adsorption,with Fe 

 with disp,low adsorption,with Fe 

 with disp,high adsorption,with Fe 

 percentage flux 

Fig. 36. Percentage of flux to the surface water for 8 different scenarios. 


 oxygen in scen no dispersion, no iron, high adsorption 

 0 

 0.05 

 0.1 

 0.15 

 0.2 

 0.25 

 0.3 

 0.35 

 0 5 10 15 20 25 30 35 40 45 cycle number 

 concentration (mol.m3) 

 SEG-1 SEG-2SEG-3 SEG-4SEG-5 SEG-6 SEG-7SEG-8 SEG-9 

Fig. 37. Oxygen concentrations during a tide for the upper 9 segments. 

 NO DISPERSION NO IRON 

 0.000 

 0.100 

 0.200 

 0.300 

 0.400 

 0.500 

 0.600 

 0.700 

 0.800 

 0.900 

 1.000 

 getij_1getij_3getij_5getij_7getij_9getij_11getij_13getij_15getij_17getij_19getij_21getij_23getij_25getij_27getij_29getij_31getij_33getij_35getij_37getij_39getij_41 TIME 

 CONC 

(^) lage K (1/1) Hoge K(10/1) Fig. 38. Pollutant concentration in the upper segment during the tidal cycle (without dispersion). 


 DISPERSION NO IRON 

 0.000 

 0.010 

 0.020 

 0.030 

 0.040 

 0.050 

 0.060 

 0.070 

 0.080 

 0.090 

 0.100 

 getij_1getij_15getij_29getij_43getij_57getij_71getij_85getij_99getij_113getij_127getij_141getij_155getij_169getij_183getij_197getij_211getij_225getij_239getij_253getij_267getij_281getij_295getij_309getij_323getij_337getij_351getij_365getij_379getij_393getij_407getij_421getij_435getij_449getij_463getij_477getij_491 TIME 

 CONC 

 lage K (1/1) Hoge K(10/1) 

Fig. 39. Pollutant concentrations in the upper segment during the tidal cycle (with dispersion). 

_The simulation without diffusion/dispersion_ The effect of the tidal cycle in the case of adsorption is clear. During downwelling the oxygen front penetrates almost with the advective velocity (only retarded with the oxygen consumption at that depth by decaying organic matter at that time). De pollutant front also goes downward, but with a velocity with is smaller: the downwelling velocity divided by the retardation. So the adsorbing downwelling front is passed by the oxygen front, and decay of the pollutant will occur. From the picture of the oxygen front it is clear that only during downwelling the decay will occur, there is no oxygen in the profile during upwelling, which also means that probably a lot of reduced substances will be transported to the surface water during upwelling, without contributing to the oxygen consumption of the sediment. This implies that on the average during the tidal cycle the penetration of oxygen is more effective in degrading the pollutant. 

_The simulation with diffusion/dispersion_ The differences occurring with diffusion/dispersion will occur for both the pollutant and oxygen in the liquid phase, but since most of the pollutant is in the solid phase, the pollutant behaviour is less dependent on the diffusion/dispersion than the oxygen behaviour. Through diffusion/dispersion both the oxyen transfer from the surface water to the sediment as well as the flux of the pollutant to the surface water will be higher. However, the concentrations will be lower. Because of the lower concentration the decay of the pollutant will be lower. The net difference in flux to the surface water between the cases with and without adsorption will be less than in the case with only advective flow. 

_The simulation with iron_ The effect of iron is that it changes the oxygen profiles considerably. During downwelling oxygen meets the reduced solid iron, which becomes oxidised. During upwelling the reduced substances meet the oxidised iron, which will be reduced. The net effect is that the difference in oxygen penetration between the downwelling tide and the upwelling tide becomes much less than without iron. A similar conclusion holds for the front of reduced substances. 

_Conclusion_ Although we did find differences in fluxes for the adsorbing and non-adsorbing pollutant, this sensitivity analysis shows that the differences become marginal due to dispersion and redox reactions with iron. Therefore, the conclusions drawn earlier in this paragraph are valid. 


12.1.6 _Model investigations with DELWAQ_ The objectives of the investigations with the water and sediment quality model DELWAQ were: 

- To show that the model can reproduce the dissolved oxygen penetration in the sediment,     calculated with the chemical model CHARON as a result of sediment diagenesis; 

- To determine the concentration gradient of the organic micropollutant monochloro-benzene     in the sediment and its flux into the overlying water on the basis of more detailed process     formulations. 

Regarding the micropollutant processes DELWAQ differs from CHARON in two respects. Partitioning (sorption) is included and the degradation rate is maximal when the dissolved oxygen concentration exceeds a low critical value (0.25 g.m -3). No degradation occurs below this oxygen concentration. This implies that the effective degradation rate is higher in DELWAQ. The results produced with DELWAQ are used to shed more light on the potential of the sediment for the degradation of organic micropollutants such as monochlorobenzene. 

As opposed to CHARON DELWAQ has been applied only for one scenario for the Solvay case. Other scenarios as well the other case could have been reproduced too, but this would not have produced more information. The scenario selected is the one with high dispersion and low sediment oxygen demand, which guarantees maximal penetration of oxygen into the sediment. DELWAQ was made to reproduce the results of CHARON with respect to oxygen penetration for a steady state situation. The lower estimate of the sediment oxygen demand (0.44 g.m -2.day-1) was reproduced by imposing an equivalent organic matter settling flux. The decompostion rates of the organic matter were estimated on the basis of past DELWAQ applications. 

Figures 40 41 show the overlapping vertical concentration profiles in the pore water of the sediment for dissolved oxygen, nitrate, sulphate, sulphide and ammonium, respectively with a linear and a logarithmic depth scale. Using a log scale stretches the profiles near the sediment water interface, which facilitates interpretation. Figure 41 indicates that the oxygen penetration depth is a little over 1 cm. DELWAQ reproduces the oxygen penetration calculated with CHARON. 

The nitrate concentration has a maximum and the ammonium concentration a minimum due to nitrification in the oxygen-containing layer. Dissolved sulphide peaks at the depth where sulphate reduction is maximal. Due to oxidation the sulphide concentration obtains a low value near to the sediment-water interface. Methane and precipitated sulphide are not shown because these substances are not present. The high sulphate concentrations prevent methanogenesis. The dissolved sulphide concentration is not high enough to induce precipitation in the model. 


 0.00 

 0.50 

 1.00 

 1.50 

 2.00 

 2.50 

 0.0 5.0 10.0 15.0 20.0 25.0 30.0 35.0 40.0 Sediment depth (cm) 

 Concentration (mg/l) 

 NH4 NO3 SO4 (*0.01) SUD OXY (*0.1) 

Fig. 40. The pore water concentrations (g.m-3) of dissolved oxygen, nitrate, sulphate, dissolved sulphide and ammonium simulated with DELWAQ-G in a steady state. Depth is displayed on a linear scale. 

 0.00 

 0.50 

 1.00 

 1.50 

 2.00 

 2.50 

 0.0 0.1 1.0 10.0 100.0 Sediment depth (log cm) 

 Concentration (mg/l) 

 NH4 NO3 SO4 (*0.01) SUD OXY (*0.1) 

Fig. 41. The pore water concentrations (g.m-3) of dissolved oxygen, nitrate, sulphate, dissolved sulphide and ammonium simulated with DELWAQ-G in a steady state. Depth is displayed on a log scale. 

The vertical separation of the consumption of electron-acceptors and methanogenesis appears from figure 42, also on the basis of a log scale. The vertical sequence of processes is in agreement with the scientific description of sediment diagenesis presented in chapter 3. A rather thin toplayer contains oxygen since it is consumed in the decomposition of organic matter. Nitrate is depleted mainly just below this layer due to denitrification. Sulphate reduction starts at the depth where the oxygen concentration approaches zero. Methanogesis does not proceed due to high sulphate concentrations. It was shown that in the model methanogenesis starts at neardepletion of sulphate [42]. 


 0.00 

 0.10 

 0.20 

 0.30 

 0.40 

 0.50 

 0.60 

 0.70 

 0.80 

 0.90 

 1.00 

 0.0 0.1 1.0 10.0 100.0 Sediment depth (log cm) 

 Fraction (-) 

 FrOx FrNi FrSu FrMet 

Fig. 42. The fractional contributions of oxygen consumption, denitrification, sulphate reduction and methanogesis simulated with DELWAQ-G in a steady state. Depth is displayed on a log scale. 

The concentrations of the organic matter fractions are displayed in figure 43. High organic matter concentrations occur near the sediment-water interface due to the settling of organic matter from the water column. The decomposition causes the depletion of POC1 and POC2 at greater depth. 

 0 

 500 

 1000 

 1500 

 2000 

 2500 

 0.0 5.0 10.0 15.0 20.0 25.0 30.0 35.0 40.0 Sediment depth (cm) 

 Concentration (mg/l) 

 POC1 POC2 POC3 

Fig. 43. The sediment concentrations (g.m-3) of the partciculate organic matter fractions simulated with DELWAQ-G in a steady state. Depth is displayed on a linear scale. 


 0.0 

 0.5 

 1.0 

 1.5 

 2.0 

 2.5 

 3.0 

 3.5 

 4.0 

 0.0 5.0 10.0 15.0 20.0 25.0 30.0 35.0 40.0 Sediment depth (cm) 

 Concentration OMP (mg/l) 

 0.0 

 1.0 

 2.0 

 3.0 

 4.0 

 5.0 

 6.0 

 7.0 

 8.0 

 Concentration OXY (mg/l) 

 OMP decay 53/day OMP no decay OXY 

Fig. 44. The pore water concentrations of the micropollutant and dissolved oxygen (g.m -3) simulated with DELWAQ-G in a steady state. Depth is displayed on a linear scale. 

Figures 44-45 display the predicted dissolved concentrations of the micropollutant for fast degradation (53 day-1) and for no degradation at all. The predicted gradients resemble those produced with CHARON. However, in the absence of degradation the decrease of the concentration at the sediment-water interface to 20% of the concentration in the upwelling groundwater is less than predicted by CHARON. A part of the difference is connected with the coarser schematisation of the sediment, a toplayer of 1 mm in DELWAQ versus a toplayer of 0.25 mm in CHARON. The difference is also due to a difference in porosity The DELWAQ model has a porosity of 0.5, CHARON a porosity of 0.8. The effects of a smaller porosity are a higher effective upwelling velocity (smaller residence time) and a smaller dispersive flux at the sediment-ware interface. 

 0.0 

 0.5 

 1.0 

 1.5 

 2.0 

 2.5 

 3.0 

 3.5 

 4.0 

 0.0 0.1 1.0 10.0 100.0 Sediment depth (log cm) 

 Concentration OMP (mg/l) 

 0.0 

 1.0 

 2.0 

 3.0 

 4.0 

 5.0 

 6.0 

 7.0 

 8.0 

 Concentration OXY (mg/l) 

 OMP decay 53/day OMP no decay OXY 

Fig. 45. The pore water concentrations of the micropollutant and dissolved oxygen (g.m -3) simulated with DELWAQ-G in a steady state. Depth is displayed on a logarithmic scale. 


With degradation, the concentration decrease is also less for DELWAQ than for CHARON. The micropollutant concentration at the sediment-water interface is 4 % of the concen-tration in the upwelling groundwater. However, the decrease of the micropollutant flux into the overlying water is higher in DELWAQ. This is due to the higher effective degradation rate. The flux of micropollutant into the overlying water is reduced with 80% compared to 55% in the case of CHARON. 

The fractions of dissolved and adsorbed micropollutant can be seen in figure 46. Slightly over 50% is adsorbed to particulate organic matter. At a porosity of 0.5 this implies that the bulk concentration of the micropollutant is a little higher than the pore water concentration. Near the sediment-water interface the fraction adsorbed to POC is higher due to the higher POC concentration. The fraction adsorbed to dissolved organic matter is negligibly small in connection with a rather low partition coefficient and a low DOC concentration. 

 0.0 

 0.2 

 0.4 

 0.6 

 0.8 

 1.0 

 0.00 5.00 10.00 15.00 20.00 25.00 30.00 35.00 40.00 Sediment depth ( cm) 

 Concentration OMP (mg/l) 

 Fraction OMP Dissolved Fraction OMP ads. to DOC Fraction OMP ads. to POC 

Fig. 46. The fractions of dissolved and adsorbed micropollutant simulated with DELWAQ-G in a steady state. Depth is displayed on a linear scale. 

12.1.7 _Conclusions and discussion_ The development of CHARON and DELWAQ started around 1980. Since then these models have been applied for many different studies concerning sediment diagenesis, sediment-water exchange of substances and water quality. This delivered a generic system definition and generic values for the process coefficients. Although due to a lack of detailed field data it was not possible to calibrate and verify the models in the current research, it is felt that the applied models are adequate for the assessment of the pollutant degradation potential of the sediment in surface water systems. The models are reliable enough to approximately simulate the penetration of oxygen in surface water sediment. In view of the lack of detailed data it was decided to consider lower and upper estimates of the sediment oxygen demand instead of the actual demand. The original plan to perform dynamic simulations was abandoned. Instead the models were applied for representative steady states. The simulations show that the steady state oxygen penetration depth at 11 oC is between 0.001 to 0.01 m at the absence of tides such as in the case of the Solvay site. When the overlying water is subjected to tides, being the case at the LBC site, the steady state oxygen penetration depth may be substantially larger. Depths of 0.020.04 m are predicted. 


The main uncertainties in the models concern the degradation of organic pollutants. Scanning of the scientific literature usually delivers quite a wide range for the field degradation rate of an organic micropollutant [23]. The conditions required for efficient degradation in the sediment as well as the degradation rate under specific field conditions are poorly known for most micropollutants. The quantitative effects of seasonal differences and spatial heterogeneity in sediment composition are yet to be unravelled. The same goes for the impact of intermittent oxidising and reducing conditions on the activity of bacteria species responsible for pollutant degradation. 

TNO-MEP measured the degradation rate of monochlorobenzene in diluted sediment by means of batch experiments. The observed first order degradation rates are between 16 and 70 day -1^ at a temperature of 15 oC. Such high rates might be overestimations for the degradation rate in the sediment at field conditions. Literature data referring to surface water point at a rate less than 1 day-1^ [23]. However, bacterial activity in the top sediment is generally much higher than in the water column. In our modelling practice the exchange of substances between sediment and 

water, we found rates as high as 100 day-1^ for the nitrification of ammonia (the oxidation of NH (^3) to NO3-) in the top sediment, whereas surface water has rates in the order of 0.1 day-1. These coefficients have been verified against field data. Groundwater flow originating from contaminated soil conveys organic micropollutants to the sediment in a nearby surface water system. The models were used to quantify the degradation and the concentration profiles of pollutants in the top sediment. The simulations have shown that dispersion alone establishes strongly decreased concentrations of pollutants at the sedimentwater interface, assuming that (very) low pollutant concentrations prevail in the overlying water. This assumption is correct when: 

- the surface area of the water body is large compared to the area in which the upwelling of     contaminated groundwater occurs; and/or 

- the residence time in the water body is small. 

The degradation of a pollutant may cause the further decrease of the concentrations at the sediment-water interface. This additional decrease may be substantial compared to the concentrations at the interface that are caused by dispersion alone. The additional decrease is small compared to the concentrations in the upwelling groundwater at the lower boundary of the active sediment layer. Yet, the pollutant concentration at the sediment-water interface might be smaller than 0.1% of the concentration in the upwelling groundwater at conditions favourable to degradation. 

Quite a different picture arises for the flux of micropollutant that enters the surface water through the sediment-water interface. Dispersion alone does not reduce the pollutant flux that is conveyed to the top sediment by groundwater. The models showed that the flux entering the surface water might be reduced substantially because of degradation. Depending on the presence of conditions favourable to degradation and the magnitude of the maximal degradation rate the reduction percentage might be larger than 95%. However, such optimal conditions will not be met in most contaminated sites. The reduction percentage may be virtually equal to nil at (very) unfavourable conditions or when the maximal degradation rate is small. 

A crucial factor is the penetration depth of dissolved oxygen, since the degradation of the relevant pollutants requires oxygen. The penetration depth is maximal for sediments with low oxygen consumption, high dispersion and small upwelling velocity. This velocity is a function of the gradient of the groundwater pressure (potential), which might be manipulated in order to maximise degradation. The magnitude of the sediment oxygen consumption depends mainly on the organic matter settling flux in the overlying water, which in turn depends on the trophic status 


of the water body. The presence and activity of benthic organisms determine the magnitude of the dispersion coefficient. Driven by light incidence and temperature all these parameters vary over the seasons. 

It is now evident that sediments with a low organic matter content and a well developed benthic community have a relatively high potential for the degradation of pollutants. Sediments with a high organic matter content may have no degradation potential whatsoever. Sediment in water bodies is rather inhomogeneous, meaning that the oxygen consumption rate and the activity of benthic organisms vary substantially from spot to spot. This causes the variation of the concentration and the flux of a pollutant in the horizontal plane. Consequently, local toxicity may be higher or lower than on average. 

A high upwelling velocity of groundwater such as in the Solvay case is negative with respect to the degradation potential of the sediment-water interface, because this causes small residence times in the oxygen containing toplayer. Moreover, the oxygen consumption may be raised by the presence in groundwater of reduced substances such as ammonium, sulphide, iron(II) and methane. This aspect was not paid due attention, because too few data were available to quantify the composition of the groundwater. Therefore, the oxygen penetration depth may be overestimated in the present simulations. 

The presence of tidal movement of water such as in the LBC case enhances degradation when combined with a low net groundwater upwelling velocity and with adsorption. The additional degradation at the occurrence of adsorption is relatively small. 

12.2 **Approach model RT3D** 

12.2.1 _The chemical reaction model_ The behaviour of the macro-chemistry and the biodegradation of the micropollutants are modelled simultaneously. The processes that are considered are advection, molecular diffusion, dispersion, retardation, biodegradation and all relevant redox-reactions. All these processes will be discussed below: 

- Advection     Advection is the transport of the solutes that is being transported with the average     groundwater flow velocity. At the location of Solvay the Darcy groundwater flow velocity is 7     cm/day. At the site of LBC the estimated Darcy groundwater flow velocity fluctuates between     -12.4 (upwelling) and 10.5 (infiltrating) cm/day. At the Shell-site, the estimated Darcy     groundwater flow velocity fluctuates between –10.8 (upwelling) and 3.6 (infiltrating) cm/day. 

- Diffusion     Diffusion is the spreading of the contaminant due to irregular Brownian motion of the     molecules. At sharp concentration gradients diffusion makes the plume wider and longer and     the high concentrations decrease. The diffusion coefficient that is used for all species is 8.6     10 -5^ m 2 /day. 

- Dispersion     Dispersion is a phenomenon that has the same effect as diffusions, but is caused by     variation in the flow velocity of the groundwater and its solutes through the porous medium.     Longitudinal dispersion is the dispersion in the direction of the groundwater flow. The     dispersion coefficient is normally obtained by the product of the Darcy flow velocity and the     longitudinal dispersivity. The longitudinal dispersivity has been obtained for many field and     laboratory studies and is commonly a function of the travel distance [10]. For travel distances 


 that are of interest in this study, the scale of the interface, which is at maximum estimated to be 10 cm, the longitudinal dispersivity reported is approximately 1 cm [10], although the field data show a significant variation. It is expected that the value of the dispersivity has a strong influence on the model results and therefore it is decided to make two model runs with longitudinal dispersivities of 1 cm and 1 mm respectively. 

- Retardation/adsorption     Adsorption of species on the soil material makes the average flow velocity of the species     lower than that of the groundwater. Organic contaminants do commonly adsorb to the     organic fraction of the soil. In groundwater contamination studies, it is commonly assumed     that there is equilibrium between the adsorbed mass and the dissolved mass of the organic     contaminants as the time scale of the flow velocity is often large compared to the time scale     of adsorption process.     For steady state flow situations, the influence of equilibrium adsorption does not play a role if     one is only interested in the steady state profile of the solutes.     For tidal systems, the influence of equilibrium adsorption is important. Due to the slower     movement of the organic contaminant with respect to oxygen, their plumes will mix during the     period of infiltration and will increase the biodegradation. It is uncertain if the sorption process     reaches ‘equilibrium’ during the tidal period, but this assumption will be made during the     calculations. If full equilibrium adsorption does not occur, it has two consequences. During     the upwelling period of the tide, the adsorbing micropollutant can pass the interface within     one tidal period, giving it less time to biodegrade and passing the interface zone when there     is little oxygen around. The second consequence is that an adsorbed contaminant molecule     that desorbs during the infiltration period of the tide comes into an oxygen rich environment,     but has only a short time to biodegrade before it reaches the surface water. Altogether the     consequence of not reaching adsorption equilibrium is unfavourable.     The retardation factors for DCE and VC at the LBC–site are 6.2 and 1.15 respectively. These     values are based on an organic matter content of 0.4% and 10 log octanol water number of     2.71 for DCE and 1.2 for VC. At the Shell site the retardation factor for monochlorobenzene     is 7.2 based on the same organic matter content and a 10 log octanol water number of 2.81. 

- Redox–reactions     In the vicinity of the surface water a number of redox reactions are likely to take place, such     as the reaction of iron(II), sulphide and methane with oxygen or nitrate, degradation of     organic matter in the subsurface and nitrification. 

- Oxidation of iron, sulphide or methane     Iron(II) is being oxidised when it is present simultaneously with oxygen. In that case iron(III)     is being formed which is likely to precipitate. This chemical reaction is very quick. In the     model it is assumed that when iron(II) and oxygen are present within a cell, they will react     until either all iron(II) or oxygen is depleted. When there is still iron(II), it will react with nitrate.     The denitrification part of this reaction is kinetically limited and is assumed to have a     degradation constant of 100 per day for the degradation of nitrate. Oxidation of sulphide and     methane can be handled in a similar way. However, field data of sulphide (for 2 sites) and     methane (on all sites) were not available and this oxidation process has not been modelled in     order to compare the behaviour of the three sites more easily. 

- Degradation of organic matter     In case of the degradation of organic matter, it is assumed that the organic matter cannot be     depleted as due to sedimentation in the surface water, new organic matter is supplied. It is     assumed that degradation of organic matter only takes place when oxygen is available. The     reaction equation for depletion of oxygen is: 


 [ ] 

 [ ] [. .] 

 [ ] 2 

 2 ,.. 

 2 2 

(^2) _K O O k om dt dO O_ = − _O om_ • • + (12.22) Where [O 2 ] is the concentration of oxygen; k (^) O2,o.m. is the second order degradation rate coefficient; [o.m.] is the sediment concentration of organic matter and K (^) O2 is the half saturation constant of oxygen. This relation is shown in figure 47. 0 0.2 0.4 0.6 0.8 1 1.2 0 2 4 6 8 10 12 **oxygen concentration (mg/l)** Fig. 47. Relation between degradation rate and oxygen concentration. This equation offers the possibility to make the degradation rate insensitive to the oxygen concentration when the concentration of oxygen becomes very high and other aspects may become more sensitive. A literature review showed that the half saturation constant of oxygen shows a large variation. For the calculations, a value of 0.4 _mg/l_ is used and during the sensitivity analyses a value of 2.0 _mg/l_ is used. The second order degradation rate constant is set at 5000 _per day_ and 300 _per day_ to get similar values for the oxygen consumption as obtained by Delft Hydraulics (0.44 g/m 2 _/ day_ and 4.85 g/m 2 _/ day_ for scenarios with low and high values respectively). The concentration of organic matter is set to unity in the soil and set to zero in the surface water. _Nitrification_ Nitrification takes place if ammonium and oxygen react to form nitrate, H+^ and water. The consumption of oxygen in this process is: [ ] [ ] [ ] [ ] 2 (^2) , , 3 2 2 (^2 332) _K O O k Y NH dt dO O_ = − _O NH_ ⋅ _NH O_ ⋅ ⋅ + (12.23) The consumption of ammonium is: [ ] [ ] [ ] [ ] 2 2 , 3 3 2 (^2 3) _K O O k NH dt dNH O_ = − _O NH_ ⋅ ⋅ + (12.24) 


The production rate of nitrate is: 

 [ ] 

 [ ] [ ] [ ] 2 

 2 , , 3 

 3 2 

(^2 333) _K O k Y NH O dt dNO NH NO O_ = + _O NH_ ⋅ −⋅ ⋅ + − (12.25) In these equations, the yield coefficient Y (^) species 1, species 2 between two species is the ratio of the mass of the second species that is consumed or produced and the mass of the first species that is consumed. The yield coefficient between ammonium and oxygen is 1.9 and the yield coefficient between ammonium and nitrate is 3.6. The degradation rate parameter is chosen to be 100 per day. _Biodegradation_ Biodegradation of the organic contaminants, monochlorobenzene, DCE and VC, is assumed to take place when oxygen is present. Degradation of the organic contaminant is modelled by the following equation: [ ] [ ] [. .] [ ] 2 2 ,.. .., 2 2 (^2 2) _K O O k Y OC dt dO O_ = − _O OC_ ⋅ _OCO_ ⋅ ⋅ + (12.26) [ ] [. .] [. .] [ ] 2 2 , .. 2 (^2) _K O k OC O dt dOC O_ = − _O OC_ ⋅ ⋅ + (12.27' For the degradation of monochlorobenzene the degradation rate constant k (^) O2,O.C. is varied for a high and a low value. The high value is 57 per day. This value is equal to the maximum value obtained by the laboratory experiment of 76 per day and corrected for temperature influence (multiplication factor of 0.75). The low value of the degradation rate constant k (^) O2,O.C. is 12 per day, which is derived in a similar way from the low value obtained from the laboratory experiment of 16 per day. Degradation of monochlorobenzene consuming other electron acceptors, such as nitrate, iron(III), sulphate does not take place. The degradation rates of DCE and VC have not been measured during then laboratory experiments. As a first estimate, the same values as for monochlorobenzene are applied. The abovementioned reactions have been modelled using the software RT3D [3]. 12.2.2 _Application of the model_ The model will be applied to the three sites selected for this project: the Solvay-site, the LBC-site and the site at Shell-Pernis. **Solvay-site (steady state flow, no tidal movement)** For the Solvay site a vertical 1D-model has been built. The smallest cell sizes are 0.25 _mm_ close to the surface water. The horizontal area of the cell is 1 _m_^2. The surface water has been modelled as the most downstream cell an additional inward flux of 4 _m_^3 _/day_. The same cell has also the only outflow condition of the model. The most upstream cell has an inward flux of 0.07 _m_^3 _/day_. The concentrations of all species are given in table 20. 


Table 20. Concentrations at inward water fluxes. 

 Concentration at groundwater boundary (mg/l) 

 Concentration at surface water boundary (mg/l) oxygen 0 14 nitrate 0 1 iron(II) 9.0 0 sulphate 390 404 monochlorobenzene 1.7 0 ammonium 0 0 

For this situation different model scenarios have been computed. Table 21 gives an overview of these scenarios. 

Table 21. Overview of model scenarios of the Solvay-site. 

 Scenario nr 

 Longitudinal dispersivity (m) 

 Degradation rate coefficient of organic fraction (per day) 

 Degradation rate coefficient of monochlorobenzene (per day) 

 Half saturation oxygen (mg/l) 

 Concentration iron(II), ammonium 

 1 0.01 300 57 0.4 normal 2 0.01 300 12 and 0 0.4 normal 3 0.01 5000 57 0.4 normal 4 0.001 300 57 0.4 normal 5 0.001 5000 57 2.0 normal 6 0.001 300 57 0.4 0 

_Scenario 1: high dispersivity; low organic matter degradation rate and high monochlorobenzene degradation rates_ 

Figure 48 shows the steady state profile of the various species for scenario 1. 

 0.01 

 0.1 

 1 

 10 

 100 

 1000 

 0.0001 0.001 0.01 0.1 1 distance (m) 

 oxygen nitrate iron (II+) sulphate monochlorobenzene nitrate iron total sulphate monochlorobenzene 

Fig. 48. Profile of species distribution at the Solvay-site for scenario 1 (solid lines show the model results; squares show the measurement values; white-filled squares show measurements that were below the detection limit). 


From this figure, it is clear that the oxidation of iron(II) has a strong impact on the surface watergroundwater interface. Below approximately 1 cm, all oxygen has been consumed for the oxidation of iron and organic matter. For species that do not react, the interface would extend to approximately 3 cm, which can be seen from the monochlorobenzene profile. The concentration of monochlorobenzene reduces to 0.041 mg/l when approaching the surface water boundary. This is a reduction of 97.6% compared with the upstream groundwater concentration. Only part of this reduction is caused by biodegradation. Diffusion and dispersion cause the other part. These contributions will be separated in scenario 2 when the profiles for monochlorobenzene are computed in case no degradation of monochlorobenzene takes place. For comparison the measured values of various species have also been plotted within the figure. These values show a large variation, which makes it hard to compare them to the model results. Moreover, the main action in the model predictions occurs within a 1 _cm_ interval next to the surface water boundary, which unfortunately has very little data. 

_Scenario 2: high dispersivity; low organic matter degradation rate and low and zero monochlorobenzene degradation rates_ 

Figure 49 shows the steady state profile of the monochlorobenzene for high, low and zero degradation. 

 0.01 

 0.1 

 1 

 10 

 0.0001 0.001 0.01 0.1 1 distance (m) 

 no degradation Low degradation high degradation 

Fig. 49. Profile of oxygen and monochlorobenzene for high, low and zero degradation rate coefficients. 

It is clear that the influence of biodegradation on the decline of the monochlorobenzene concentration near the surface water boundary is limited. The monochlorobenzene concentration in the cell closest to the surface water is 0.041 mg/l for the high, 0.057 mg/l for the low and 0.068 mg/l for the zero monochlorobenzene degradation rate coefficient. Biodegradation reduces the concentration values by 40% for the high degradation rate coefficient. 

_Scenario 3: high dispersivity; high organic matter degradation rate and high monochlorobenzene degradation rate_ 

Figure 50 shows the steady state profile of the various species for scenario 3. 


 0.01 

 0.1 

 1 

 10 

 100 

 1000 

 0.0001 0.001 0.01 0.1 1 distance (m) 

 oxygen nitrate iron (II+) sulphate monochlorobenzene nitrate iron total sulphate monochlorobenzene 

Fig. 50. Profile of species distribution at the Solvay-site for scenario 3 with high degradation rate for organic matter. 

In this scenario, the oxygen enters the first 4 mm of the aquifer. The concentration of monochlorobenzene before it reaches the surface water is 0.060 mg/l. Its reduction is again a combined influence of dispersion/diffusion and biodegradation. The reduction of the total load of monochlorobenzene to the surface water in this scenario is 20%. 

_Scenario 4: low dispersivity; low organic matter degradation rate and high monochlorobenzene degradation rate_ 

Figure 51 shows the steady state profile of the various species for scenario 4. 

 0.01 

 0.1 

 1 

 10 

 100 

 1000 

 0.0001 0.001 0.01 0.1 1 distance (m) 

 oxygen nitrate iron (II+) sulphate monochlorobenzene nitrate iron total sulphate monochlorobenzene 

Fig. 51. Profile of species distribution at the Solvay-site for scenario 4. 


In this scenario, the interface of oxygen and iron(II) is at approximately 2 mm from the surface water boundary. The interface of the non-reacting species continues up to 5 mm from the surface water boundary. The concentration of monochlorobenzene in the cell closest to the surface water is 0.18 mg/l. In this scenario, the reduction of the monochlorobenzene concentration at the interface is much smaller compared to the model with the higher dispersivity. Comparison with additional model results showed that the influence of biodegradation on the reduction of the load of monochlorobenzene to the surface water in this scenario is 16%. 

_Scenario 5: high dispersivity; high organic matter degradation rate and low monochlorobenzene degradation rate and high half saturation constant for oxygen_ 

Figure 52 shows the steady state profile of the various species for scenario 5. 

 0.01 

 0.1 

 1 

 10 

 100 

 1000 

 0.0001 0.001 0.01 0.1 1 distance (m) 

 oxygen nitrate iron (II+) sulphate monochlorobenzene nitrate iron total sulphate monochlorobenzene 

Fig. 52. Profile of species distribution at the Solvay-site for scenario 5 with a high half saturation constant for oxygen. 

In this scenario, the oxygen enters the first 1 cm of the aquifer. The concentration of monochlorobenzene before it reaches the surface water is 0.045 mg/l. The reduction is again a combined influence of dispersion/diffusion and biodegradation. The reduction of the total load of monochlorobenzene to the surface water in this scenario is 33%. 

_Scenario 6: high dispersivity; high organic matter degradation rate and high monochlorobenzene degradation rate, no consumption of oxygen for iron(II) oxidation_ 

Figure 53 shows the steady state profile of the various species for scenario 6. 


 0.01 

 0.1 

 1 

 10 

 100 

 1000 

 0.0001 0.001 0.01 0.1 1 distance (m) 

 oxygen nitrate sulphate monochlorobenzene nitrate iron total sulphate monochlorobenzene 

Fig. 53. Profile of species distribution at the Solvay-site for scenario 6 without influence of iron(II). 

In this scenario, the oxygen enters the first 1.0 cm of the aquifer before its concentration decreased to its half saturation constant of 0.4 mg/l. After 1.5 cm only 0.01 mg/l of oxygen is present. The concentration of monochlorobenzene before it reaches the surface water is 0.034 mg/l. Its reduction is again a combined influence of dispersion/diffusion and biodegradation. The reduction of the total load of monochlorobenzene to the surface water in this scenario is 55%. 

The results of all these scenarios are summarised in table 22. 

Table 22. Summary of model results of Solvay-site. 

 Scenario nr description 

 Infiltration length of oxygen (mm) 

 Concentration of monochlorobenz ene before reaching the surface water boundary (mg/l) 

 Reduction of load of monochlorobenzene to the surface water 1 reference situation 10 0.041 40% 2 low degradation rate of monochlorobenzene 

 10 0.057 16% 

 3 high degradation rate of organic matter 

 4 0.060 20% 

 4 low dispersivity 2 0.18 16% 5 high half saturation constant of oxygen 

 10 0.045 33% 

 6 no oxygen consumption by iron oxidation 

 15 0.034 55% 

**LBC-site** The tidal system of the LBC-site has been modelled with a vertical 1-dimensional model of 0.20 m long with cell lengths of 1 mm each. This model represents an averaged streamline. The influence of the temporal varying flow velocity in directions perpendicular to the temporal averaged velocity direction is neglected. The boundary conditions for the outer cells are prescribed time-varying fluxes that were obtained with the flow model for the streamtube at 1.30 m on the horizontal plain. An overview of these fluxes during a single tidal period is given in figure 54. 


 -0.150 

 -0.100 

 -0.050 

 0.000 

 0.050 

 0.100 

 0.150 

 0.000 0.100 0.200 0.300 0.400 0.500 0.600 time (day) 

 fluxes (m/day) 

Fig. 54. Modelled fluxes during the tidal period. 

The concentrations of all relevant species of the infiltrating water are given in table 23. 

Table 23. Concentration infiltrating water at boundary fluxes. 

 Concentration at surface water boundary (mg/l) 

 Concentration at groundwater boundary (mg/l) Oxygen 9.2 0 Nitrate 9.8 0 iron(II) 0 35 Sulphate 167 153 ammonium 0 9.5 cis -DCE 0 0.022 VC 0 0.022 

These values were obtained from the field data. Macroparameters for groundwater boundary have been averaged, while the maximum measured concentration of _cis_ -DCE was used. VC was not detected during the fieldwork, but in order to make a comparison between the behaviour of _cis_ -DCE and VC, the VC-value is set equal the values of _cis_ -DCE. 

For this situation different model scenarios have been computed. Table 24 gives an overview of these scenarios. 

Table 24. Overview of model scenarios of the LBC-site. 

 Scenario nr. 

 Longitudinal dispersivity (m) 

 Degradation rate coefficient of organic fraction (per day) 

 Degradation rate coefficient of cis DCE and VC (per day) 

 Half saturation oxygen (mg/l) 

 Concentration iron(II), ammonium 

 1 0.01 300 57 0.4 normal 2 0.01 300 12 and 0 0.4 normal 3 0.01 5000 57 0.4 normal 4 0.001 300 57 0.4 normal 5 0.001 5000 57 2.0 normal 6 0.001 300 57 0.4 0 


_Scenario 1: high dispersivity; low organic matter degradation rate and high monochlorobenzene degradation rate_ 

The breakthrough curves of _cis_ -DCE and VC for the reference situation are shown in figure 55 and figure 56. 

 1.E-04 

 1.E-03 

 1.E-02 

 1.E-01 

 0 1 2 3 4 5 6 7 8 9 time (days) 

 80 mm 70 mm 60 mm 50 mm 40 mm 30 mm 20 mm 10 mm 5 mm 0 mm 

 distance to surface water 

Fig. 55. Breakthrough curves for _cis_ -DCE for scenario 1 (reference situation). 

 1.E-05 

 1.E-04 

 1.E-03 

 1.E-02 

 1.E-01 

 0 1 2 3 4 5 6 7 8 9 time (days) 

 80 mm 70 mm 60 mm 50 mm 40 mm 30 mm 20 mm 10 mm 5 mm 0 mm 

 distance to surface water 

Fig. 56. Breakthrough curves for VC for scenario 1 (reference situation). 

For both breakthrough curves it holds that they are approaching a steady state cycle. This can be seen that after 7 days the cycles resemble each other. After that time, the initial concentration condition has no influence anymore on the model results. For _cis_ -DCE the reduction of the concentration before reaching the surface water is considerable. The maximum concentration during the cycle is 5.7 _μg/l_. That is a reduction of 74% within the interface due to biodegradation and dispersion. The reduction of the total load of _cis_ -DCE that reaches the surface water has also been computed and is 62%. For VC the maximum concentration during the cycles that reaches the surface water is 9.2 _μg/l_. This means a concentration reduction 58%. The reduction of the total load of VC that reaches the 


surface water is 39%. The only reason for the difference in behaviour is the retardation as all model parameters for _cis_ -DCE and VC are equal. Due to the stronger retardation of _cis_ -DCE its plume mixes better with the oxygen plume, which results in a faster biodegradation. 

_Scenario 2: high dispersivity; low organic matter degradation rate and low and zero monochlorobenzene degradation rates_ 

The breakthrough curves of _cis_ -DCE and VC for this scenario are shown in figure 57 and figure 58. 

 1.E-04 

 1.E-03 

 1.E-02 

 1.E-01 

 0 1 2 3 4 5 6 7 8 9 time (days) 

 80 mm 70 mm 60 mm 50 mm 40 mm 30 mm 20 mm 10 mm 5 mm 0 mm 

 distance to surface water 

Fig. 57. Breakthrough curves for _cis_ -DCE for scenario 2 (low degradation rate coefficient for _cis_ -DCE and VC). 

 1.E-04 

 1.E-03 

 1.E-02 

 1.E-01 

 0 1 2 3 4 5 6 7 8 9 time (days) 

 80 mm 70 mm 60 mm 50 mm 40 mm 30 mm 20 mm 10 mm 5 mm 0 mm 

 distance to surface water 

Fig. 58. Breakthrough curves for VC for scenario 2 (low degradation rate coefficient for _cis_ DCE and VC). 


The maximum concentration in the groundwater that reaches the surface water is 7.8 μg/l for _cis_ DCE and 9.8 μg/l for VC. Due to the lower degradation rates the reduction of the contaminant concentration before reaching the surface water reduced from 74% to 64% for _cis_ -DCE and from 58% to 55% for VC. The reduction of the total load that reaches the surface water is 48% for _cis_ DCE and 35% for VC. 

_Scenario 3: high dispersivity; high organic matter degradation rate and high monochlorobenzene degradation rate_ 

The breakthrough curves of _cis_ -DCE and VC for this scenario are shown in figure 59 and figure 60. 

 1.E-03 

 1.E-02 

 1.E-01 

 0 1 2 3 4 5 6 7 8 9 time (days) 

 80 mm 70 mm 60 mm 50 mm 40 mm 30 mm 20 mm 10 mm 5 mm 0 mm 

 distance to surface water 

Fig. 59. Breakthrough curves for _cis_ -DCE for scenario 3 (low degradation rate coefficient for organic matter). 

 1.E-04 

 1.E-03 

 1.E-02 

 1.E-01 

 0 1 2 3 4 5 6 7 8 9 time (days) 

 80 mm 70 mm 60 mm 50 mm 40 mm 30 mm 20 mm 10 mm 5 mm 0 mm 

 distance to surface water 

Fig. 60. Breakthrough curves for VC for scenario 3 (low degradation rate coefficient for organic matter). 


The maximum concentration in the groundwater that reaches the surface water is 8.2 _μg/l_ for _cis_ DCE and 9.8 _μg/l_ for VC. The reduction of the total load that reaches the surface water is 46% for _cis_ -DCE and 35% for VC. 

_Scenario 4: low dispersivity; low organic matter degradation rate and high monochlorobenzene degradation rate_ 

The breakthrough curves of _cis_ -DCE and VC in case the longitudinal dispersivity is decreased to 1 mm are shown in figure 61 and figure 62. 

 1.E-05 

 1.E-04 

 1.E-03 

 1.E-02 

 1.E-01 

 0 1 2 3 4 5 6 7 8 9 time (days) 

 80 mm 70 mm 60 mm 50 mm 40 mm 30 mm 25 mm 20 mm 15 mm 10 mm 5 mm 0 mm 

 distance to surface water 

Fig. 61. Breakthrough curves for _cis_ -DCE for scenario 4 (low dispersivity). 

 1.E-11 

 1.E-10 

 1.E-09 

 1.E-08 

 1.E-07 

 1.E-06 

 1.E-05 

 1.E-04 

 1.E-03 

 1.E-02 

 1.E-01 

 0 1 2 3 4 5 6 7 8 9 time (days) 

 80 mm 70 mm 60 mm 50 mm 40 mm 30 mm 25 mm 20 mm 15 mm 10 mm 5 mm 0 mm 

 distance to surface water 

Fig. 62. Breakthrough curves for VC for scenario 4 (low dispersivity). 

The maximum concentration in the groundwater that reaches the surface water is 4.6 μg/l for _cis_ DCE and 16 μg/l for VC. Due to the lower dispersivity, the reduction in the contaminant concentration before reaching the surface water increased from 74% to 79% for _cis_ -DCE and decreased from 58% to 27% for VC. The reduction of the total load that reaches the surface 


water is 70% for _cis_ -DCE and 8% for VC. The influence of the dispersivity on the reduction of the VC-concentration is largest as for VC dispersion is more crucial for the mixing with the oxygen plume than it is for _cis_ -DCE which also mixes good due to the stronger retardation. 

_Scenario 5: high dispersivity; high organic matter degradation rate and low monochlorobenzene degradation rate and high half saturation constant for oxygen_ 

Figure 63 and figure 64 show the breakthrough curves of _cis_ -DCE and VC in case the half saturation constant for oxygen is increased to 2 mg/l (scenario 5). 

 1.E-04 

 1.E-03 

 1.E-02 

 1.E-01 

 0 1 2 3 4 5 6 7 8 9 time (days) 

 concentration (mg/l) 

 80 mm 70 mm 60 mm 50 mm 40 mm 30 mm 20 mm 10 mm 5 mm 0 mm 

 distance to surface water 

Fig. 63. Breakthrough curves for _cis_ -DCE for scenario 5 with a high half saturation constant for oxygen. 

 1.E-05 

 1.E-04 

 1.E-03 

 1.E-02 

 1.E-01 

 0 1 2 3 4 5 6 7 8 9 time (days) 

 concentration (mg/l) 

 80 mm 70 mm 60 mm 50 mm 40 mm 30 mm 20 mm 10 mm 5 mm 0 mm 

 distance to surface water 

Fig. 64. Breakthrough curves for VC for scenario 5 with a high half saturation constant for oxygen. 


The maximum concentration in the groundwater that reaches the surface water is 5.7 μg/l for _cis_ DCE and 9.2 μg/l for VC. The reduction of the total load that reaches the surface water is 62% for _cis_ -DCE and 39% for VC. 

_Scenario 6: high dispersivity; high organic matter degradation rate and high monochlorobenzene degradation rate, no consumption of oxygen for iron(II) and ammonium oxidation_ 

Figure 65 and figure 66 show the breakthrough curves of _cis_ -DCE and VC in case no oxygen is consumed by iron(II) and ammonium (scenario 6). 

 1.E-04 

 1.E-03 

 1.E-02 

 1.E-01 

 0 1 2 3 4 5 6 7 8 9 time (days) 

 concentration (mg/l) 

 80 mm 70 mm 60 mm 50 mm 40 mm 30 mm 20 mm 10 mm 5 mm 0 mm 

 distance to surface water 

Fig. 65. Breakthrough curves for _cis_ -DCE for scenario 6 with no influence of iron(II) and ammonium. 

 1.E-05 

 1.E-04 

 1.E-03 

 1.E-02 

 1.E-01 

 0 1 2 3 4 5 6 7 8 9 time (days) 

 concentration (mg/l) 

 80 mm 70 mm 60 mm 50 mm 40 mm 30 mm 20 mm 10 mm 5 mm 0 mm 

 distance to surface water 

Fig. 66. Breakthrough curves for VC for scenario 6 with no influence of iron(II) and ammonium. 

The maximum concentration in the groundwater that reaches the surface water is 4.7 μg/l for _cis_ DCE and 8.4 μg/l for VC. The reduction of the total load that reaches the surface water is 69% for _cis_ -DCE and 44% for VC. 


The results of all these scenarios are summarised in table 25. 

Table 25. Summary of model results of LBC-site. 

 Maximum concentration of contaminant before reaching the surface water boundary (μg/l) 

 Reduction of load of contaminant to the surface water 

 Scenario description 

 cis DCE VC cis -DCE VC 1 reference situation 5.7 9.2 62% 39% 2 low degradation rate of monochlorobenzene 

 7.9 9.8 48% 35% 

 3 high degradation rate of organic matter 

 8.2 9.8 46% 35% 

 4 low dispersivity 4.6 16 70% 8% 5 high half saturation constant of oxygen 

 5.7 9.2 62% 39% 

 6 no oxygen consumption by iron and ammonium oxidation 

 4.7 8.4 69% 44% 

**Shell-site** 

The tidal system of the Shell-site has been modelled with the same model set up as the LBCsite: a vertical 1-dimensional model of 0.20 m long with cell lengths of 1 mm each. The boundary conditions for the outer cells are prescribed time-varying fluxes that were obtained with the groundwater flow model. An overview of these fluxes during a single tidal period is given in figure 67. 

 -120 

 -100 

 -80 

 -60 

 -40 

 -20 

 0 

 20 

 40 

 60 

 0 0.1 0.2 0.3 0.4 0.5 0.6 

 time (days) 

 flux 

Fig. 67. Modelled fluxes during the tidal period. 

The concentrations of all relevant species of the infiltrating water are given in table 26. 


Table 26. Concentration infiltrating water at boundary fluxes. 

 Concentration at surface water boundary (mg/l) 

 Concentration at groundwater boundary (mg/l) oxygen 10 0 nitrate 13 0.04 iron(II) 0 52 sulphate 57 9.2 ammonium 0 9.5 Monochlorobenzene 0 0.1 

Most of these values were obtained from the field data. Ammonium had not been analysed and the same values are used as for the LBC-site. The oxygen concentration at the groundwater boundary was set at zero, as the officially reported concentration was 0.476 mg/l, which is probably erroneous, as the groundwater seems anaerobic. Monochlorobenzene has not reached the NA-interface yet and an imaginary value is used. 

For this situation different model scenarios have been computed. Table 27 gives an overview of these scenarios. 

Table 27. Overview of model scenarios of the Shell-site. 

 Scenario nr 

 Longitudinal dispersivity (m) 

 Degradation rate coefficient of organic fraction (per day) 

 Degradation rate coefficient of monochlorobenzene (per day) 

 Half saturation oxygen (mg/l) 

 Concentration iron (II+), ammonium 

 1 0.01 300 57 0.4 normal 2 0.01 300 12 and 0 0.4 normal 3 0.01 5000 57 0.4 normal 4 0.001 300 57 0.4 normal 5 0.001 5000 57 2.0 normal 6 0.001 300 57 0.4 0 

_Scenario 1: high dispersivity; low organic matter degradation rate and high monochlorobenzene degradation rate_ 

The breakthrough curves of monochlorobenzene for the reference situation are shown in figure 68. 


 0.E+00 

 1.E-02 

 2.E-02 

 3.E-02 

 4.E-02 

 5.E-02 

 6.E-02 

 7.E-02 

 8.E-02 

 9.E-02 

 1.E-01 

 0 1 2 3 4 5 6 7 8 9 time (days) 

 20 mm 16 mm 12 mm 8 mm 4 mm 2 mm 0 mm 

 distance to surface water 

Fig. 68. Breakthrough curves for monochlorobenzene for scenario 1 (reference situation). 

For the breakthrough curve it holds that it approaches a steady state cycle. For monochlorobenzene the reduction of the concentration before reaching the surface water is considerable. The maximum concentration during the cycle is 89 μg/l. That is a reduction of 10% within the interface. The reduction of the total load of monochlorobenzene that reaches the surface water is 4.5%. 

_Scenario 2: high dispersivity; low organic matter degradation rate and low and zero monochlorobenzene degradation rates_ 

The breakthrough curves of monochlorobenzene for this scenario are shown in figure 69. 

 0.E+00 

 1.E-02 

 2.E-02 

 3.E-02 

 4.E-02 

 5.E-02 

 6.E-02 

 7.E-02 

 8.E-02 

 9.E-02 

 1.E-01 

 0 1 2 3 4 5 6 7 8 9 time (days) 

 20 mm 16 mm 12 mm 8 mm 4 mm 2 mm 0 mm 

 distance to surface water 

Fig. 69. Breakthrough curves for monochlorobenzene for scenario 2 (low degradation rate coefficient for monochlorobenzene). 


The maximum concentration in the groundwater that reaches the surface water is 90 _μg/l_ for monochlorobenzene. The reduction of the total load of monochlorobenzene that reaches the surface water is 2.7%. 

_Scenario 3: high dispersivity; high organic matter degradation rate and high monochlorobenzene degradation rate_ 

The breakthrough curves of monochlorobenzene for this scenario are shown in figure 70. 

 0.E+00 

 1.E-02 

 2.E-02 

 3.E-02 

 4.E-02 

 5.E-02 

 6.E-02 

 7.E-02 

 8.E-02 

 9.E-02 

 1.E-01 

 0 1 2 3 4 5 6 7 8 9 time (days) 

 20 mm 16 mm 12 mm 8 mm 4 mm 2 mm 0 mm 

 distance to surface water 

Fig. 70. Breakthrough curves for monochlorobenzene for scenario 3 (low degradation rate coefficient for organic matter). 

The maximum concentration in the groundwater that reaches the surface water is 90 μg/l for monochlorobenzene. The reduction of the total load of monochlorobenzene that reaches the surface water is 3.9%. 

_Scenario 4: low dispersivity; low organic matter degradation rate and high monochlorobenzene degradation rate_ 

The breakthrough curves of monochlorobenzene in case the longitudinal dispersivity is decreased to 1 mm are shown in figure 71. 


 0.E+00 

 1.E-02 

 2.E-02 

 3.E-02 

 4.E-02 

 5.E-02 

 6.E-02 

 7.E-02 

 8.E-02 

 9.E-02 

 1.E-01 

 0 1 2 3 4 5 6 7 8 9 time (days) 

 20 mm 16 mm 12 mm 8 mm 4 mm 2 mm 0 mm 

 distance to surface water 

Fig. 71. Breakthrough curves for monochlorobenzene for scenario 4 (low dispersivity). 

The maximum concentration in the groundwater that reaches the surface water is 95 μg/l for monochlorobenzene. The reduction of the total load of monochlorobenzene that reaches the surface water is 18%. 

_Scenario 5: high dispersivity; high organic matter degradation rate and low monochlorobenzene degradation rate and high half saturation constant for oxygen_ 

Figure 72 shows the breakthrough curves of monochlorobenzene for this scenario. 

 0.E+00 

 1.E-02 

 2.E-02 

 3.E-02 

 4.E-02 

 5.E-02 

 6.E-02 

 7.E-02 

 8.E-02 

 9.E-02 

 1.E-01 

 0 1 2 3 4 5 6 7 8 9 time (days) 

 concentration (mg/l) 

 20 mm 16 mm 12 mm 8 mm 4 mm 2 mm 0 mm 

 distance to surface water 

Fig. 72. Breakthrough curves for monochlorobenzene for scenario 5 with a high half saturation constant for oxygen. 

In this scenario, the maximum monochlorobenzene concentration in the groundwater that reaches the surface water is 90 μg/l. The reduction of the total load of monochlorobenzene that reaches the surface water is 3.7%. 


_Scenario 6: high dispersivity; high organic matter degradation rate and high monochlorobenzene degradation rate, no consumption of oxygen for iron(II) and ammonium oxidation_ 

Figure 73 shows the breakthrough curves of monochlorobenzene for this scenario. 

 0.E+00 

 1.E-02 

 2.E-02 

 3.E-02 

 4.E-02 

 5.E-02 

 6.E-02 

 7.E-02 

 8.E-02 

 9.E-02 

 1.E-01 

 0 1 2 3 4 5 6 7 8 9 time (days) 

 concentration (mg/l) 

 20 mm 16 mm 12 mm 8 mm 4 mm 2 mm 0 mm 

 distance to surface water 

Fig. 73. Breakthrough curves for monochlorobenzene for scenario 6 with no influence of iron(II) and ammonium. 

The maximum monochlorobenzene concentration in the groundwater that reaches the surface water is 78 μg/l. The reduction of the total load of monochlorobenzene that reaches the surface water is 27%. 

The results of all these scenarios are summarised in table 28. 

Table 28. Summary of model results of Shell-site. 

 Scenario nr description 

 Maximum concentration of monochlorobenzene before reaching the surface water boundary (μg/l) 

 Reduction of load of monochlorobenzene to the surface water 

 1 reference situation 89 4.5% 2 low degradation rate of monochlorobenzene 

 90 2.7% 

 3 high degradation rate of organic matter 

 90 3.9% 

 4 low dispersivity 95 18% 5 high half saturation constant of oxygen 

 90 3.7% 

 6 no oxygen consumption by iron and ammonium oxidation 

 78 27% 

The calculated biodegradation at the Shell site is relatively low. The reason for this low biodegradation is that due to the low infiltrating rate compared to the upwelling rate, the residence time of monochlorobenzene in the interface zone is relatively short. The infiltration and upwelling rate have been determined using a storage coefficient of 7 10 -4^ 1/m_._ This value has been derived from field data, which showed a large variation. Using a different value for the storage coefficient can give quite different results. 


12.2.3 _Conclusions and discussion_ The influence of the interface between groundwater and surface water acts quite different for steady state flow systems and tidal systems with infiltration during part of the tidal period. Therefore for both situations conclusions are drawn separately. 

_Steady state flow systems_ 

- The interface between surface water and groundwater for steady state flow systems is very     thin. For the pilot that was modelled in this project, the estimates of the thickness of the     interface vary between 1 mm and 1.5 cm for oxygen and nitrate up to 3 cm for non-reacting     species. The parameters that strongly influence the thickness of the interface are the     groundwater flow upwelling rate, the longitudinal dispersivity and the macro-chemistry of the     groundwater; as at the study site most oxygen and nitrate that enters the aquifer is     consumed by oxidation of iron(II). 

- The decrease of the contaminant concentration when approaching the surface water is     mainly due to dispersion. For the model run with a relative high dispersivity, the     monochlorobenzene concentration before reaching the surface water decreased with 97%.     This reduction strongly depends on the longitudinal dispersivity and the ratio between the     groundwater upwelling rate and the dilution rate in the surface water. The total load of the     contaminant to the surface water is reduced much less as the total load is the combination of     the advective flux (flow velocity times concentration) and the dispersive and diffusive flux     (concentration gradient times the dispersion/diffusion coefficient). 

- According to the model results the contribution of biodegradation to the decrease in     monochlorobenzene concentration can be up to 55% under favourable model assumptions. 

_Tidal systems_ 

- In tidal systems, a relatively thick chemical interface may exist. It strongly depends on the     amount of water that infiltrates during the rise of the tide. In the pilot study at the LBC-site,     the modelled thickness of the interface is approximately 6 cm. At the Shell-site, the modelled     thickness of the interface is approximately 2 cm. 

- Biodegradation of the micropollutants can be very large if the pollutant strongly adsorbs to     the soil material. In that case, the infiltrating oxygen plume and the retarded plume of the     pollutant mix strongly, which gives a good condition for biodegradation. At the LBC-site, the     surface water load of _cis_ -DCE decreased 70% under the most favourable model     assumptions. For the hardly retarded plume of VC, the conditions are less favourable and     only a decrease of 44% has been obtained using the most optimal model assumptions. At     the Shell-site, the surface water load of monochlorobenzene decreased 27% under the most     favourable model assumptions. The situation may be more favourable if more water infiltrates     during the rising tide than was assumed in the model. 


 CHAPTER 13 

###### GENERAL CONCLUSIONS PHASE 1 

_Monitoring devices_ 

A new tool (Multi Level Sampler) was developed for sampling groundwater at small distances in the interface between groundwater and surface water. Together with existing tools (monitoring wells, environfilters, peepers) it has been applied for measuring NA-interface gradients in the field. The new developed tool made it possible to prove the occurrence of NA-interface gradients for both contaminants (e.g., monochlorobenzene) and macro parameters. The order of detail, however, was not sufficient for determining the contribution of biodegradation apart from processes like dilution and dispersion. 

Several methods were applied for the determination of the oxygen penetration depth. Some of them were limited by the sampling technique. The application of a diver with an oxygen sensor led to results that were still too rough (because of the resolution in distance and the time needed for stabilisation). 

_Modelling of NA-interface processes_ 

Related to the interface, dispersivity influences contaminant concentrations and not contaminant flux, whereas biodegradation influences both contaminant flux and, relatively limited compared to dispersivity, contaminant concentrations. 

The degradation of a pollutant will cause decrease of the concentrations at the sediment-water interface. The additional decrease is small compared to the concentrations in the up welling groundwater at the lower boundary of the active sediment layer. Yet, the pollutant concentration at the sediment-water interface might be smaller than 0.1% of the concentration in the up welling groundwater at conditions favourable to degradation. 

Quite a different picture arises for the flux of micro pollutant that enters the surface water through the sediment-water interface. Dispersion alone does not reduce the pollutant flux that is conveyed to the top sediment by groundwater. The models showed that the flux entering the surface water may be reduced substantially because of degradation. Depending on the presence of conditions favourable to degradation and the magnitude of the maximal degradation rate the reduction percentage might be larger than 95%. However, such optimal conditions will not be met in most contaminated sites. The reduction percentage may be virtually equal to nil at (very) unfavourable conditions or when the maximal degradation rate is small. 

A crucial factor is the penetration depth of dissolved oxygen, since the degradation of the relevant pollutants requires oxygen. The penetration depth is maximal for sediments with low oxygen consumption, high dispersion and small up welling velocity. The magnitude of the sediment oxygen consumption depends on several parameters, which vary over the seasons. 

A high up welling velocity of groundwater is negative with respect to the degradation potential of the sediment-water interface, because this causes small residence times in the oxygen containing top layer. Moreover, the oxygen consumption may be raised by the presence in groundwater of reduced substances such as ammonium, sulphide, iron(II) and methane. 


Tidal water table fluctuations enhance degradation when combined with a low net groundwater up welling velocity and with adsorption. The additional degradation effect of adsorption strongly depends on the residence time of the contaminant in the interface. This residence time depends on the magnitude of adsorption and the ratio of the net groundwater flux and the volume of water that infiltrates during a tidal period. 

The influence of the interface between groundwater and surface water acts quite different for steady state flow systems and tidal systems with infiltration during part of the tidal period. 

Steady state flow systems: 

- The interface between surface water and groundwater for steady state flow systems is very     thin. For the pilot that was modelled in this project, the estimates of the thickness of the     interface vary between 1 mm and 1.5 cm for oxygen and nitrate up to 3 cm for non-reacting     species. 

- The decrease of the contaminant concentration when approaching the surface water is     mainly due to dispersion. 

- According to the model results the contribution of biodegradation to the decrease in     monochlorobenzene concentration can be up to 55% under favourable model assumptions. 

Tidal systems: 

- In tidal systems, a relatively thick chemical interface may exist. It strongly depends on the     amount of water that infiltrates during the rise of the tide. In the pilot study the modelled     thicknesses of the interfaces were approximately 2 - 6 cm. 

- Biodegradation of the micro pollutants can be very extensive if the pollutant strongly adsorbs     to the soil material. In that case, the infiltrating oxygen plume and the retarded plume of the     pollutant mix strongly, which gives a good condition for biodegradation. 

In this project the modelling has been executed using two different point of views: one focussing on the surface water and the interface and one focussing on the groundwater and interface. Differences between these viewpoints concern the choice of model parameters, which are based on experiences from both back grounds. The processes that are used in both modelling approaches are the same: 

- advection, diffusion, dispersion, adsorption and instantaneous and 

- kinetically limited (bio)chemical reactions. 

The conclusions drawn from both modelling excercises are similar, even though a difference exists in the opinions on the importance of adsorption in tidal systems. For future modelling the key issue is to obtain better estimates for the model parameters. These are likely to be obtained from inverse modelling using adequate measurements. Moreover it is important to validate the models. Once the better estimates of the model parameters are known the choice of the model software is basically irrelevant as long as all important processes and key interactions between the processes are incorporated. 

_Ecotoxicological assessment_ The fact that the groundwater samples are either anaerobic or micro-aerobic, while the risk must be assessed for the aerobic water and sediment ecosystems, posed a methodological problem: both anaerobic (effect of low oxygen concentrations) and aerobic (ecologically not relevant) bioassays are not quite suitable. However, the bioassays still show that toxicity testing has an added value to a concentration-based hazard assessment. 


 CHAPTER 14 

###### RECOMMENDATIONS PHASE 1 

_Quantification of bioremediation_ 

The first step for future research is to determine the occurrence and contribution of biological degradation of contaminants in the interface, either in the laboratory or, preferentially, under field conditions. After it has been proved that the biological removal of contaminants in the interface can be substantial, it should be investigated which site characteristics are favorable for the occurrence of beneficial removal processes. This can be achieved by investigating a larger number of sites, varying in both interface and contaminant characteristics. 

The ultimate challenge for future research will be to quantify the contaminant removal in the interface and the inflow of contaminants to the surface water under field conditions. Therefore it is necessary to develop a sampling tool for seepage water, which does not influence the interface and prevents this water from dilution and dispersion with the surface water 1. The tool should be applicable at a great number of sites in order to determine the composition of the seepage water under field conditions. 

Since the oxygen penetration is a very crucial parameter for NA-interface processes, a tool should be developed for measuring the oxygen concentrations with a resolution order of millimeters. Developing the tool from microelectrodes or oxygen diver equipment is expected to have the best chances. 

_Modelling: further details and validation_ 

The model reconnaissance has pointed out that the combination of dispersion and degradation of a pollutant may have large effects on the concentrations at the sediment-water interface. The pollutant flux from the sediment into the overlying water will be reduced, but not to a negligibly low level. Low but detectable concentrations will prevail at the interface, even when the concentration in the surface water is extremely low. The question is whether the seasonally varying concentrations of a pollutant and its metabolites in sediment and water are acceptable from a toxicological point of view. Finding the answer to that question should be the ultimate aim of further research. The next step is to find out if concentrations lower than toxicological standard concentrations can be achieved at all, and if this is the case, what conditions have to be met, regarding the penetration depth of oxygen in sediment. 

So far the research has focused on the simplified simulation of steady state conditions at an average ambient temperature, mainly because of a lack of sufficiently detailed field data. The effects of oxygen penetration in the sediment have been analyzed for upper and lower limits of the sediment oxygen demand. However, the activity of bacteria and higher benthic organisms is highly temperature dependent. It is high in summer and low in winter. The effects of seasonal variation should be studied, which requires both measurements and dynamic, integrated simulations of water and sediment quality. Dynamic models need to be calibrated and verified on the basis of detailed measurement data. Besides monochlorobenzene, other relevant pollutants should be studied as well. 

(^1) A relatively new tool that is currently being developed for determining the fate of contaminants and degradation products is the quantification of stable isotope fractionation. 


_Laband field research_ 

For some measurements in the sediment-water interface under field conditions, large impediments would have to be overcome. Therefore, future research should be an optimal combination of field and laboratory experiments. Well-controlled lab experiments with sediment-water interface systems may provide sufficiently frequent measurements with high vertical resolution. The parameters measured should cover at least the most essential data, such as dissolved oxygen profiles. Field experiments should then be designed and used to verify that the lab experiments are representative for the field. 

Due attention is to be paid to the measurement of the composition of upwelling groundwater, a highly important boundary condition for the models. This must include both the concentrations of pollutants as well as the concentrations of substances that affect the sediment oxygen demand (NH4+, NO3-, SO42-, S 2-, Fe2+, CH 4 ). 

Besides seasonality a number of other potentially important aspects have not yet been considered with the models such as the fate of toxic metabolites of the micro pollutants. Future modeling would also have to study the effects on pollutant concentrations and fluxes of: 

- Vertical and horizontal heterogeneity; 

- Intermittently oxidizing and reducing conditions; 

- Degradation concurrent with denitrification and sulphate reduction. 

The determination of the degradation rate in relation to the second and third aspects requires additional batchor through flow experiments. For tidal systems, the impact of the interface between groundwater and surface water seems favourable under specific conditions: infiltration of water during the rise of the tide in combination with a retarded contaminant. In order to validate the model results, it is essential to obtain relevant measurements, which means time series of concentration measurements of contaminants, oxygen, electrical conductivity values, temperature, etc. The position of these measurements should be very precise with an accuracy of approximately 1 cm. Moreover, the time before the monitoring well or the sensor is in equilibrium should be short compared to the tidal period. Considering this complexity of such a monitoring system, it is to be considered to study the phenomena of the NA-interface in tidal systems using laboratory experiments. Information about the thickness of the chemical interface can be obtained using divers. 

_Enhanced natural attenuation at the interface_ 

In case the influence of the NA-interface on the biodegradation is not large enough to reduce the contaminant concentration to an acceptable level, various measures can be considered to improve the influence on the NA-interface. These measures focus on enlargement of the residence time of the contaminants in the interface. In tidal systems, it is possible to cover the banks with a material that strongly retards the organic contaminants to provide a better and prolonged mixing of aerobic water and the contaminant. In non-tidal systems, at some sites it will be possible to change the surface water level periodically in order to obtain infiltration of aerobic water during part of the time. In both situations, it will be beneficial if the net upwelling groundwater flow velocity is reduced to create larger residence times in the interface zone. 

_Exotoxicological aspects_ For future research, it is recommended to keep paying attention to ecotoxicological aspects, because the protection of the surface water is an important prerequisite for any acceptable solution. 


The ecotoxicological assessment can be greatly improved with the following issues: 

- Identification of the source of the observed toxicity. It is important for the Solvay location to     confirm that MCB is responsible for the observed effects, and is interesting for LBC to     distinguish between metals (arsenic) and organics. 

- Field research: When a natural site is studied, where a NA interface is active (e.g., LBC-site),     the actual effects of the seeping groundwater (after passage through the NA interface) can     be studied by comparing the sediment invertebrate community to a reference location. This     may help to quantify the effect of the natural attenuation solution. 

- A final way to proceed is to start a discussion with the relevant authorities, to develop a     strategy for assessing the ecological risk for the aquatic ecosystem from groundwater inflow. 

_Water Policy aspects_ 

New methods need to be developed to adressthe issues mentioned above. This is especially important for new, Water Framework Directory driven, assessment of the quality of surface water and sediment systems. 

**Continuation plan Phase 2** The primary goal for the research in Phase 2 is the quantification of natural attenuation processes in the groundwater / surface water interface. This will be carried out at both laboratoryand field scale. 

The project plan includes the following activities: 

1. To determine the contaminant mass balance in an interface model on bench scale and, to     quantify natural attenuation in the interface system. 

2. Because the extent of degradation is strongly dependent on the oxygen penetration from the     surface water to the interface: to develop a field measurement tool for the determination of     the oxygen penetration depth in the interface on a millimeter scale. 

3. To develop and apply on field scale a sampling method for seepage water from the interface,     without disturbing the natural interface and without mixing the seepage water and the surface     water. The method can be used to quantify the contaminant flux from ground- to surface     water at different sites. 

4. To generate suffiently detailed data from laboratory research for validating the computer     models applied in the previous research phase. 

These activities are necessary for quantification and validation of the results of the previous phase. 

The results of the proposed project plan are (numbers according to the activities mentioned above): 

1. The quantified contribution of natural degradation processes in the interface between ground-     and surface water. 

2. A tool for the determination of the oxygen penetration depth in the interface on a millimeter     scale. 

3. A sampling method for seepage water from an interface. This is a tool for determining the     seepage water quality at different sites. This quality is the base for the risk assessment for     the surface water and discussions with the Water Boards. 

4. Data for validating the computer models for removal processes that were developed in the     previous phase. 


On a longer term, research activities for further tuning are: 

- Tidal influences (on laboratory scale) 

- Simultaneous degradation of contaminants and denitrification and sulphate reduction 

- Seasonal influences (less activity at lower temperatures) 

- Monitoring: 

- at more sites 

- of more contaminant types 

- Intermittent oxidative and reductive conditions 

- Heterogeneity 


###### REFERENCES 

[1] Allen HE, Fu G, Boothman W, DiToro DM & Mahony JD (1991) Determination of AVS and selected SEM in Sediment. Report nr.EPA 821-R-91-100, US Environmental Protection Agency. 

[2] CIW (2000) Normen voor het waterbeheer. Achtergronddocument 4e Nota Waterhuishouding CIW. 

[3] Clement (1997) RT3D, A modular computer code for simulating reactive multi-species transport in 3-dimensional groundwater systems. Pacific Northwest National Laboratory, PNNL 11720. 

[4] Davis JW & Carpenter CL (1990) Aerobic biodegradation of vinyl chloride in groundwater samples. Appl. Environ. Microbiol. 56: 3878-3880. 

[5] De Rooij NM (1980) A chemical model to describe nutrient dynamics in lakes. Pages 139149 in J. Barrica and L. Mur (eds), Hypertrophic ecosystems. Dr. W. Junk B.V. Publishers, The Hague, the Netherlands. 

[6] De Rooij NM (1991) HADES: Development and tentative simulations (in Dutch). Research report nr.T584, WL | Delft Hydraulics. 

[7] De Rooij NM & Kroot MPJM (1991) Mathematical simulation of biochemical processes in natural waters by the chemical model CHARON. Model documentation nr.R1310-10, WL | Delft Hydraulics. 

[8] DeStraat (2000) Geohydrologische onderbouwing beheersmaatregel;en Oude Maasweg 4 (LBC) te Rotterdam (in Dutch, concept version). Report nr.B99A0118, De Straat Milieuadviseurs B.V. 

[9] DiToro DM (2001). Sediment Flux Modeling. John Wiley & Sons, Inc., New York. 

[10] Gelhar LW, Welty C & Rehfeldt KR (1992) A critical review of data on field-scale dispersion in aquifers. Water Resources Research 28: 1955-1974. 

[11] Gerritse J, Renard V, Visser J & Gottschal JC (1995) Complete degradation of tetrachloroethene by combining anaerobic dechlorinating and aerobic methanotrophic enrichment cultures. Appl. Microbiol. Biotechnol. 43: 920-928. 

[12] Halden K & Chase HA (1991) Methanotrophs for clean-up of polluted aquifers. Water Sci. Technol. 24: 9-17. 

[13] Hartmans S & Debont JAM (1992) Aerobic vinyl chloride metabolism in _Mycobacterium aurum_ L1. Appl. Environ. Microbiol. 58: 1220-1226. 

[14] Hemker CJ & Nijsten GJ (1997). Groundwater flow modeling using Micro-fem Version 3.1. Hemker, Amsterdam. 


[15] Henneke E, Luther III GW & De Lange GJ (1991) Determination of inorganic sulfur speciation with polarographic techniques some preliminary-results for recent hypersaline anoxic sediments. Marine Geology 100: 115-123. 

[16] Hermens J, Busser F, Leeuwangh P & Musch A (1985) Quantitative structure-activity relationships and mixture toxicity of organic chemicals in _Photobacterium phosphoreum_ : the Microtox test. Ecotoxicol. Environ. Saf. 9: 17-25. 

[17] Hetterschijt RAAea (2000) Kwetsbaarheidskaarten als basis voor monitoring en sanering op het Shell Pernis terrein. TNO-report, TNO-NITG. 

[18] IWACO (2002) Werkzaamheden ten behoeve van ijking grondwatermodel Pernis. Report nr.19975a0.100, IWACO. 

[19] Kaiser KLE & Devillers J (1994). Ecotoxicity of chemicals to _Photobacterium phosphoreum_. Gordon and Breach Science Publishers, Amsterdam. 879 pp. 

[20] Langenhoff A, Elissen H, Rijnaarts H, Pijls C, Alphenaar A, Boode J, te Stroet C & van Zutphen M (2000) Bioremediatie van HCH locaties; Eindrapportage fase 1. nr.CR 99/445, TNO-MEP, Apeldoorn. 

[21] Langenhoff AAM, Staps S, Rijnaarts H, Praamstra T, Heijnen M & Vis P (2001) Feasibility study of a "Biological Fence"at the site of Shell Netherlands Refinery. TNO-report nr.R2001/314, TNO, Apeldoorn. 

[22] Maas JL, Naber A & Botterweg J (1994) Toxiciteit en mutageniteit van acht industriële effluenten voor zoetwaterorganismen. Vergelijking van de gevoeligheid van zoeten zoutwaterorganismen. RIZA-Werkdocument nr.93.171X, RWS. 

[23] Mackay D, Shiu WY & Ma KC (1992). Monoaromatic Hydrocarbons, Chlorobenzenes and PCBs. Illustrated handbook of physical-chemical properties and environmental fate for organic chemicals, vol. 1. Lewis Publishers, London. 

[24] McDonald MD & Harbaugh AW (1988). A modular three-dimensional finite-difference flow model. Techniques in water resources investigations of the U.S. Geological Survey, vol. 6. 586 pp. 

[25] Middeldorp PJM, Staps JJM, Visser-Westerweele EPC, Mol JJW, Rijnaarts HHM & Cerneaz KL (2002) Bitterfeld: Bioremediation of regional contaminated aquifers. Phase 2001 Interim report. TNO-report nr.R 2002/390, TNO-MEP, Apeldoorn, The Netherlands. 

[26] Mulder GJ & Weststrate F (2000) Report nr.CO-387050/15, Delft Geotechnics, Delft. 

[27] Nolte AJ, Van Gils JAG, Icke J & Smits JGC (2001) Sediment-water exchange of substances. Comparison of 4 sediment modules. Research report nr.Z2846, WL | Delft Hydraulics. 

[28] Opdam HJWY, Valstar JR & E. TB (2002) Distribution of directly injection of auxiliary substances (in Dutch). SKB-report nr.SV-065, SKB, Gouda, The Netherlands. 


[29] Peltier WH & Weber CI (1985) Methods for measuring the acute toxicity of effluents to freshwater and marine organisms. EPA report nr.600/485-013, U.S. Environmental Protection Agency, Cincinnati, OH. 

[30] Persoone G & Snell TW (1998) ROTOXKIT F; Rotifer Toxicity Screening Test for Freshwater. Standard Operational Procedure University of Ghent, Ghent, Belgium. 

[31] Persoone G & Snell TW (1998) Thamnotoxkit F; Crustacean Toxicity Screening Test for Freshwater. Standard Operational Procedure University of Ghent, Ghent, Belgium. 

[32] Pettigrew CA, Haigler BE & Spain JC (1991) Simultaneous biodegradation of chlorobenzene and toluene by a _Pseudomonas_ strain. Appl. Environ. Microbiol. 57: 157-162. 

[33] Phelps TJ, Malachowsky K, Schram RM & White DC (1991) Aerobic mineralization of vinyl chloride by a bacterium of the order Actinomycetales. Appl. Environ. Microbiol. 57: 12521254. 

[34] Reineke W & Knackmuss H-J (1984) Microbial metabolism of haloaromatics: Isolation and properties of a chlorobenzene-degrading bacterium. Appl. Environ. Microbiol. 47: 395-402. 

[35] Richardson MS & Gangolli S eds. (1992-1996) The dictionary of substances and their effects. The Royal Society of Chemistry, Cambridge. 

[36] RIKZ (1999) Sediment Toxiciteitstest met Microtox Solid Phase. Standaardvoorschrift nr.SPECIE-02, Rijksinstituut voor Kust en Zee. 

[37] Roovers CPAC (1998) In situ remediation of soil contaminated with monochlorobenzene and aniline. Summary report nr.NOBIS 96-1-10, CUR/NOBIS, Gouda, The Netherlands. 

[38] Santschi P, Höhener P, Benoit G & Buchholtz-ten Brink M (1990) Chemical processes at the sediment interface. Mar. Chem. 30: 269-315. 

[39] Smits JGC (1991) Switch, a model for sediment-water exchange of nutrients; Part 1: Formulation; Part 2: Calibration/Application for Lake Veluwe. Research report nr.T542/T584, WL | Delft Hydraulics, 

[40] Smits JGC (1994) Switch, a model for sediment-water exchange of nutrients; Part 3: Reformulation and recalibration for Lake Veluwe. Research report nr.T584, WL | Delft Hydraulics. 

[41] Smits JGC (2002) Sediment-water exchange of substances, Diagenesis modelling, Phase 

2. Research report nr.Q2935.30, WL | Delft Hydraulics. 

[42] Smits JGC (2002) Sediment-water exchange of substances, Diagenesis modelling, Phase 

3. Research report nr.Q2935.30, WL | Delft Hydraulics. 

[43] Smits JGC & Icke J (2001) Sediment-water exchange of substances. Model and knowlegde development, Phase 1 (in Dutch). Research report nr.Z2845.31, WL | Delft Hydraulics. 


[44] Smits JGC & Van der Molen DT (1993) Application of SWITCH, a model for sedimentwater exchange of nutrients, to Lake Veluwe in the Netherlands. Hydrobiologia 253: 281300. 

[45] Soetaert K, Herman PMJ & Middelburg JJ (1996) A model of early diagenetic processes from the shelf to abyssal depth. Geochim. Cosmochim. Acta 60: 1019-1040. 

[46] Speitel GE & Closmann FB (1991) Chlorinated solvent biodegradation by methanotrophs in unsaturated soils. J. Environ. Eng.ASCE 117: 541-548. 

[47] Starkweather PL & Kellar PE (1987) Combined influences of particulate and dissolved factors in the toxicity of _Microcystis aeruginosa_ (NCR-SS-170) to the rotifer _Brachionus calyciflorus_. Hydrobiologia 147: 375-378. 

[48] STOWA (1997). Keuzesysteem en praktijktoetsing. Biomonitoringtechnieken voor bestrijdingsmiddelen en zware metalen in watersystemen, vol. 2. Stichting Toegepast Onderzoek Waterbeheer, ISBN 90.74476.90.2. 

[49] Suarez MP & Rifai HS (1999) Biodegradation rates for fuel hydrocarbons and chlorinated solvents in groundwater. Bioremed. J. 3: 337-362. 

[50] Van den Berg GA, Loch JPG, Van der Heijdt LM & Zwolsman JJG (1998) Vertical distribution of acid-volatile sulfide and simultaneously extracted metals in a recent sedimentation area of the river Meuse in The Netherlands. Environ. Toxicol. Chem. 17: 758-763. 

[51] Van der Grift B, Griffioen J & Beekman W (2002) Manual for the Integrated Transport Model for Groundwater quality version 2.2 (in Dutch). TNO-report nr. NITG-01-164-B, TNO-NITG, Utrecht. 

[52] Van Heiningen WNM, Nipshagen AAM, Griffioen J, Veltkamp AG, Langenhoff AAM & Rijnaarts HHM (1999) Intrinsic and enhanced biodegradation of benzene in strongly reduced aquifers. Pages 481-485 in B. C. Alleman and A. Leeson (eds), In situ bioremediation of petroleum hydrocarbon and other organic compounds. The fifth international in situ and on site bioremediation symposium. Battelle Press, San Diego. 

[53] Wang Y & Van Cappellen P (1996) A multicomponent reactive transport model of early diagenesis: Application to redox cycling in coastal marine sediments. Geochim. Cosmochim. Acta 60: 2993-3014. 

[54] Wijsman JWM, Herman PMJ, Middelburg JJ & Soetaert K (2001) A model for early diagenetic processes in sediments of the continental shelf of the Black Sea. Est. Coast. Shelf Sci. in press. 

[55] WL|Delft_Hydraulics (1995) DELWAQ 4.2, User's manual. 

[56] WL|Delft_Hydraulics (2000) Technical Reference Manual for DELWAQ. 


 APPENDIX A 

###### CONVERSION OF THE APPARENT BIODEGRADATION RATE CONSTANT FROM 

###### BATCH SYSTEMS TO WATER SATURATED SOIL 

The degradation rate at a given biomass concentration is 

###### X 

###### dt 

###### dC 

###### v = 

_v_ = degradation rate (mol.s-1.kg-1) C = concentration (mol.m -3) _t_ = time (s) X = biomass concentration (kg/m 3 ) 

Michaelis-Menten kinetics for biodegradation: 

###### K C 

###### v C 

###### v 

 s 

 m 

###### + 

###### ⋅ 

###### = 

_v_ (^) _m =_ max. degradation rate (mol.s-1.kg-1) _K_ (^) _s_ = half-saturation constant (mol.m-3) Combining the two equations yields 

###### K C 

###### v X C 

###### dt 

###### dC 

 s 

 m 

###### + 

###### ⋅ ⋅ 

###### = 

C<<K (^) m, therefore, first order degradation kinetics apply 

###### k X C 

###### K 

###### v X C 

###### dt 

###### dC 

 s 

###### = m^ ⋅ ⋅ = ⋅ ⋅ 

_k_ = first order degradation rate constant (= _v_ (^) _m/K_ (^) _s_ ) (s -1) The term _k.X_ is here defined as the “apparent first order degradation rate constant” _k_ (^) _app_ , which is _k_ corrected for the biomass concentration. This constant enables to calculate the first order degradation rate constant ( _k_ (^) _app_ ) for a soil system without knowing the exact biomass concentration. Using the _k_ (^) _app_ , then _s m_ 

###### K 

###### v X 

###### k 

###### ⋅ 

###### app,microorganism= 


Provided sufficient mixing the following assumption holds: 

_k_ app, microorganism = _k_ app, batch 

Without transport limitation: 

 app batch batch 

 soil 

###### app soil X k 

###### X 

_k_ (^) , = ⋅ , _app batch sbatch batch_ 

###### app soil sm k 

###### V 

_k_ (^) , , 

##### , =((^1 −θ)ρ )⋅ 

θ = porosity of the soil (m^3 /m 3 ) ρ _s_ = density of the solid phase of the soil (kg/m^3 ) 

_V_ (^) _batch_ = total volume of the batch (m^3 ) _ms,batch_ = mass of the solid phase in the batch (kg) Derivation: 

###### V 

###### f m 

###### X s 

###### ⋅ 

###### = 

 (assumption: 99% of the biomass attached to the solid phase of the soil) 

 f = factor for biomass density on the slid phase (-/-) 

soil: _s s s s_ 

###### V 

###### m 

##### =φ ⋅ρ =( 1 −θ) ρ 

##### Xsoil = f ( 1 − θ ) ρ s 

batch: _batch_ 

 s sbatch 

###### V 

###### m 

###### V 

_m_ (^) , 

###### = 

 s batch 

 batch s 

 batch 

 sbatch 

 s batch 

 soil 

###### m 

###### V 

###### V 

###### m 

###### f 

###### f 

###### X 

###### X 

 , , 

###### ( 1 ) 

###### ( 1 ) 

###### = − ⋅ 

###### − 

##### = θ ρ 

##### θ ρ 

= conversion factor for the apparent biodegradation rate constant batch ⇒ soil, without transport limitation 


 APPENDIX B 

###### SITE CHARACTERISTICS FOR SITE EVALUATION 

**Logistics** − Accessibility of the site − Special safety regulations − Accessibility of the bank with ballast car − Presence of structures from which samples can be taken − Information on quay/bank construction − Original dredging depth − Dredging frequency − Draught of ships and frequency of mooring − Last depth soundings 

**Sediment cq. pore water parameters Unit** − Particle size distribution − Porosity -/− Water content g/kg DM − Clay content % DM − Sand content (fraction > 63μ) % DM − Organic matter content % DM − COD g O 2 /kg DM − pH -− Redox potential mV − Oxygen content mg O 2 /l − Chloride mg/L − Conductivity μS/cm − DOC mg C/l − Sulphate* mg S/l − Dissolved sulphide* mg S/l − Precipitated sulfide* mg S/l − Total-N mg/l − Total reactive iron-Fe(OOH) g Fe/kg DM − Total reactive iron-Fe 2 S g Fe/kg DM − Mn2+(aq)* mg Mn/l − Total reactive manganese* g Mn/kg DM − Total-P* mg P/l − Ortho-phosphate-P* mg P/l − Alkalinity* mg HCO 3 /l − Dissolved calcium* mg Ca/l − Calcite* g/kg DM − Micro-pollutants μg/l & μg/kg DM 


**Mass transport parameters Unit** − Water depth m − Tidal movement m − Flow rate surface water m/s − Seepage velocity mm/day − Flow rate groundwater m/year − Sediment growth velocity cm/year 

**Surface water parameters Unit** − Temperature °C − pH -− Suspended solids mg/l − Redox potential mV − Oxygen content mg O 2 /l − Chloride mg/l − Conductivity μS/cm − Total-N mg/l − Kjeldahl-N mg/l − Ammonium-N mg/l − Nitrate-N mg/l − Sulphate mg/l − Algae content μg chlorofyl/l − COD mg O 2 /l − BOD* mg O 2 /l − DOC* mg C/l − POC* mg C/l − Total-P* mg P/l − Ortho-phosphate-P* mg P/l − Dissolved silicate* mg Si/l − Secchi-depth* m − Alkalinity* mg HCO 3 /l − Dissolved calcium* mg Ca/l − Total iron* mg Fe/l − Total manganese* mg Mn/l − Micro-pollutants μg/l 


 APPENDIX C 

###### SOIL CORE SAMPLE ANALYSES 


 Core samples taken from the Solvay ditch, August 2002 

**Depth from cm 0 3 6 11** 

**until cm 3 6 11 16** 

Remark total core length is 30 cm Description middle fine sand with shell residues, grey with black stripes SiO2 (%) 81 81 81 81 Al2O3 (%) 3,6 3,9 3,9 4,0 TiO2 (%) 0,1 0,1 0,1 0,1 Fe2O3 (%) 0,5 0,5 0,5 0,6 MnO (%) 0,016 0,015 0,017 0,016 CaO (%) 3,3 3,5 3,7 3,3 MgO (%) 0,3 0,3 0,3 0,3 Na2O (%) 1,0 1,1 1,1 1,1 K2O (%) 1,2 1,3 1,3 1,3 P2O5 (%) 0,028 0,030 0,031 0,032 S (%) 0,040 0,051 0,037 0,038 Sum (%) 92 92 92 92 As mg/kg 1,4 2,9 2,0 2,4 Cu mg/kg 11 4,2 4,9 6,6 Pb mg/kg 11 8,7 9,9 11 Zn mg/kg 17 20 18 16 Ni mg/kg 5,8 6,7 6,1 7,3 Cr mg/kg 19 19 24 19 V mg/kg 15 15 16 16 Sn mg/kg 0,000 1,9 1,5 7,4 Sr mg/kg 120 123 131 123 Ba mg/kg 236 252 247 271 Rb mg/kg 42 43 44 45 Ga mg/kg 4,6 4,8 4,3 4,5 Zr mg/kg 90 99 87 90 Nb mg/kg 3,5 3,4 3,9 3,3 Y mg/kg 8,0 8,7 9,1 8,2 Sc mg/kg 2,9 4,1 2,8 4,8 La mg/kg 9,2 8,0 8,2 7,1 Nd mg/kg 5,7 7,7 14 11 Th mg/kg 3,3 4,1 2,7 0,000 U mg/kg 2,0 0,8 1,4 1,3 S-AVS (wet sediment) μmol/g 3,7 4,1 2,8 3,8 water content % 21 18 21 24 N (Kjeldahl) % 0,003 0,004 0,003 0,006 Total C % 0,7 1,0 1,0 0,8 weightloss between 105 and 450 % 0,4 0,3 0,3 0,5 weightloss between 450 and 550 % 0,2 0,2 0,2 0,3 weightloss between 550 and 800 % 3,0 3,2 3,1 2,9 weightloss between 800 and 1000 % 0,051 0,047 0,039 0,047 organic matter % 0,4 0,3 0,3 0,5 CaCO3 XRF % 5,9 6,2 6,6 5,9 MCB μg/kg d.w. 226 381 822 2111 


