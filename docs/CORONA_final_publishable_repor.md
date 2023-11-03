## CONFIDENCE IN FORECASTING OF NATURAL ATTENUATION AS A RISK-BASED 

## GROUNDWATER REMEDIATION STRATEGY 

# CORONA C onfidence in f OR ecasting O f N atural A ttenuation 

# A research project principally funded by the European Union within the 5th 

# Framework Programme under contract EVK1-2001-00087 

# Final report 

# October 2005 

# D.N. Lerner, P. Bjerg, J. Datel, A. Gargini, P. Gratwohl, C. Holliger, P. Morgan, 

# T. Ptak, R. Schotting, H. Slenders, S.F. Thornton 


In bibliographies, this report should be cited as: 

 Lerner D.N., Bjerg P., Datel J., Gargini A., Gratwohl P., Holliger C., Morgan P., Ptak T., Schotting R., Slenders H., Thornton S.F., 2005. CORONA Confidence in forecasting of natural attenuation as a risk-based groundwater remediation strategy, Final report of the EU research project EVK12001-00087. University of Sheffield, UK. 25 pages. Available from http://www.shef.ac.uk/corona. 

© University of Sheffield, 2005, all rights reserved. This publication may be reproduced, stored in a retrieval system, and transmitted in its entirety. However no part less than the whole of this publication may be reproduced, stored in a retrieval system, or transmitted by any means, electronic, mechanical, photocopying, recording or otherwise, without the prior permission of the University of Sheffield. 


### EXECUTIVE SUMMARY 

There are hundreds of thousands of sites in Europe where groundwater is polluted, often by manufactured organic chemicals. Unfortunately the pollutants are technically difficult to remove and so the cost of engineered clean up can be high, often higher than the value of the land. A risk-based approach to managing groundwater pollution is becoming widely accepted in Europe because it targets resources to those sites where human health or the environment are at significant risk of harm. Risk assessment enables us to take account of the natural processes, collectively known as natural attenuation, which reduce the concentrations of pollutants. Biodegradation, in which native bacteria consume the pollutants as food, is usually the most important attenuation process. A good understanding of the transport and fate of pollutants is required to make predictions of future behaviour and generate confidence in risk assessment. 

The outcomes of the CORONA project will increase confidence in assessment and forecasting of natural attenuation through the following: 

1. We have strengthened the scientific understanding of natural attenuation by studying a range of real     polluted sites, using field investigations, laboratory studies and computer simulation. All of the sites     had complex pollution problems, with mixtures of pollutants, poorly known histories and a variety of     groundwater flow conditions. We were able to go beyond the usual qualitative assessment, and     provide quantitative descriptions of the transport and fate of the pollutants. As these descriptions are     published in the scientific literature they will enable practitioners to translate our findings to other     difficult sites. 

2. We have provided robust engineering tools for the assessment and quantification of natural     attenuation, and made these publicly available. One tool is a numerical model which can be tailored to     suit the chemistry, geology and history of particular sites. A second tool is a simple spreadsheet-based     method of predicting the length of pollution plumes, using a minimum of expensive data. It is based on     a new conceptual model of how plumes behave, and includes a new mathematical solution. These are     supported by guidance documents which explain how quantitative assessment of natural attenuation     can be carried out. 

3. We have promoted the use of these tools in the end-user community of contaminated site owners,     regulators and their advisors through a website and a series of short courses. Further courses will be     held after the end of the project, and the engineering tools and guidance documents will remain     available through the project website. 

In addition to these scientific and technical outcomes, the project has initiated new research collaborations in Europe and beyond, and contributed to the training of 10 new research scientists to PhD level. Overall, CORONA will make a significant improvement in the economy and environment of the European Union. 

 i 


(BLANK) 

 ii 


### CONTENTS 

Executive summary.........................................................................................................................................i 

(blank)............................................................................................................................................................ii 

Contents........................................................................................................................................................ iii 

TABLES AND FIGURES............................................................................................................................... iii 

Project summary ............................................................................................................................................1 

 Background: why natural attenuation is important .....................................................................................1 

 Activities in the CORONA project ..............................................................................................................1 

 Key research advances .............................................................................................................................3 

 High resolution multilevel sampling .......................................................................................................3 

 Microbiological degradation processes in a heterogeneous plume in the Netherlands .........................6 

 Reoxidation at the upstream end of a hydrocarbon plume, Hnevice, Czech Republic ..........................9 

 Natural attenuation in changing flows at the NIT site, Italy..................................................................10 

 Ammonium and phenol plume at Rexco site, Mansfield, UK ...............................................................12 

 Sjoelund site, Denmark .......................................................................................................................13 

 Laboratory microbiology ......................................................................................................................15 

 Laboratory plume model......................................................................................................................16 

 Numerical model development and use ..............................................................................................17 

 CoronaScreen and guidance...............................................................................................................19 

 CORONA knowledge exchange ..............................................................................................................21 

 Research impacts and benefits to society ...............................................................................................23 

 Take up of CORONA principles...........................................................................................................23 

Acknowledgements......................................................................................................................................23 

Publications..................................................................................................................................................24 

The CORONA Consortium and contact details ............................................................................................25 

### TABLES AND FIGURES 

Table 1 Summary of the field sites investigated in CORONA........................................................................3 

Table 2 Prediction of normalized toluene breakthrough concentrations for nine different polymer tubing materials. Measured for a bundle type MLS with 15 m tubing length, 4 mm tubing diameter and low flow sampling at 100 ml/min. C/C0 is the concentration at the exit of tube as a proportion of concentration in sample. ..........................................................................................................................................................5 

 iii 


Figure 1 Conceptual sketch of the CORONA principle. Fringe oxidised plumes are controlled by the counter fluxes of oxidants and pollutants (lower right). The rate of degradation of pollutants that are degraded within the plume is controlled by the diffusion-controlled availability of electron donors/acceptors (middle left). ...................................................................................................................................................2 

Figure 2 Numerical simulation example of a reactive plume fringe zone at field scale. The steady state ammonium plume (top) clearly reflects the supply of oxygen from the top of the aquifer in recharge (middle) and its consumption during the nitrification process. The environment for the growth and survival of microbe populations is restricted to a very narrow zone, where the concentration gradients of oxygen and ammonium overlap (bottom) (courtesy of U. Maier, University of Tuebingen). ..............................................4 

Figure 3 Theoretical maximum vertical resolution of two bundle-type MLS systems: point sampler (PS) and line sampler (LS) plotted vs. aquifer porosity (ne)..........................................................................................6 

Figure 4 Conceptual model of the plume at the Brabant site. ........................................................................7 

Figure 5 Molecular analyses of sediment samples showing _Dehalococcoides etheogenes_ is only present in or near the biobarrier......................................................................................................................................7 

Figure 6 Stable isotope fractionation along the flow path at Brabant ............................................................8 

Figure 7 Degradation products in monitoring wells along flow path ...............................................................8 

Figure 8 Locations of the reactive zones at the Hnevice site. Groundwater flow is from left to right, see text for further explanation. ...................................................................................................................................9 

Figure 9 Effects of the transient flow field on ethylbenzene concentrations. Simulations were made using MT3D during a flood event (left picture) and during baseflow recession (right picture); contour levels range from 1 mmol/l (red) to 1e-6 mmol/l (light blue); the blue rectangle is the area with the MLSs grid. ..............11 

Figure 10 Molecular microbiological analyses of groundwater samples from Rexco demonstrating the presence of anammox bacteria. PCR with specific primers showed the presence of anammox bacteria in samples of boreholes BH102 and BH101. Lanes 1 – 9: BH102samples of 18 – 26 m depths; lanes 10 – 14: BH101 samples of 16 – 20 m depths; + is the positive control, M is the molecular size marker. .................13 

Figure 11 Conceptual model of the contamination as well as results of selected parameters from two multilevel samplers. .............................................................................................................................................14 

Figure 12 Specific degraders and degradation potential (expressed as evolved radioactively labelled CO 2 in the microcosms) across the fringe 50 metre down gradient from the landfill................................................15 

Figure 13 Schematic drawing of the laboratory plume experiment...............................................................17 

Figure 14 Transverse dispersion coefficients plotted against the Peclet number, together with experimental results of other studies and fitted equations.................................................................................................18 

Figure 15 Simulated chloride plume at the CORONA field site Sjoelund. ...................................................19 

Figure 16 Opening view of CoronaScreen performance assessment model................................................20 

Figure 17 Example output from CoronaScreen, showing estimates of plume length. ..................................21 

Figure 18 Organisation of knowledge exchange between CORONA and external parties...........................22 

 iv 


### PROJECT SUMMARY 

### Background: why natural attenuation is important 

There are hundreds of thousands of sites in Europe where groundwater is polluted. The sites are of many types, from large petrochemical plants, through manufacturing sites, to petrol stations with leaking underground storage tanks. The pollution at these sites is often manufactured organic chemicals which are potentially hazardous to human health and the environment. Unfortunately the pollutants are technically difficult to remove and so the cost of engineered clean-up can be high, often higher than the value of the land. 

A risk-based approach to managing groundwater pollution is being widely accepted in Europe. Under this approach, each site is assessed to decide if the pollution is likely to cause harm or whether, by the time it has travelled along the pathway in the aquifer to arrive at the receptor, concentrations will be below harmful levels. Concentrations can be reduced during travel through the aquifer by several natural processes, collectively known as natural attenuation. Biodegradation, in which native bacteria consume the pollutants as food, is usually the most important attenuation process. Even where risk assessment is not accepted by regulators, natural attenuation is often accepted as a strategy for remediating groundwater pollution, usually in association with long term monitoring. For both risk assessment and monitored natural attenuation, a good understanding of the transport and fate of the pollutants is required to have confidence in predictions of future behaviour. 

The evolution of many pollution plumes is difficult to predict because of the lack of information on ground conditions, the complexity of the pollutant mixtures, and our poor understanding of the microbiological processes involved in biodegradation. These problems have often reduced confidence in natural attenuation as a strategy, and restricted its use to simpler problems such as petrol spills. The guidelines that are available to help practitioners are generally concerned to demonstrate whether natural attenuation is occurring, rather than predicting its extent and the likely length of the pollution plume. Most risk assessment tools take a very simplistic view of biodegradation, and use predictive equations that are no longer considered appropriate. 

With this background, the CORONA project set out to increase confidence in assessment and forecasting of natural attenuation by achieving the following goals: 

1. Strengthening the scientific basis which supports the use of natural attenuation as a risk assessment     tool; 

2. Providing simple but robust engineering tools for assessment and quantification of natural attenuation     as a remedial approach for groundwater pollution; 

3. Promoting the use of these tools in the end-user community of problem holders, regulators and     advisors. 

### Activities in the CORONA project 

The project started from a new conceptual model of the biodegradation behaviour of pollution plumes groundwater, derived from an earlier study of the Four Ashes site^1 , as illustrated in Figure 1. 

(^1) D. N. Lerner, S. F. Thornton, M. J. Spence, S. A. Banwart, S. H. Bottrell, J. J. Higgo, H. E. H. Mallinson, R. W. Pickup, G. M. Williams, 2000. Ineffective natural attenuation of degradable organic compounds in groundwater. _Ground Water_ , **38** (6), 922-928. NOTE: publications generated by the CORONA project are given at the end of this report, references in the footnotes are to other work, or un-refereed publications from CORONA. 


### Source Pathway Target 

 Groundwater flow 

 Concentration 

 Depth O 2 NO^3 

 e-donoror Pollutant e-acceptor 

 groundwater flow 

 slow non equilibrium mixing 

 Mixing and anaerobic degradation in the internal corona 

 Contaminant flux across control plane 

 Mixing and aerobic degradation in the fringe corona 

**Figure 1 Conceptual sketch of the CORONA principle.** Fringe oxidised plumes are controlled by the counter fluxes of oxidants and pollutants (lower right). The rate of degradation of pollutants that are degraded within the plume is controlled by the diffusion-controlled availability of electron donors/acceptors (middle left). 

This model implies that high-resolution sampling across the plume, especially at the fringe in most cases, will be very helpful in deducing biodegradation behaviour. As the required resolution is not available from commercially available samplers, a significant effort in the project was on designing and testing new sampling systems for these applications. 

The bulk of the project’s resources were used on investigating and understanding several case studies (Table 1). All of these were real sites, where site owners gave us access to carry out complementary investigations to the work of their consultants. 

These sites had their own complexities, as outlined in Table 1. To complement the field studies, microbiology and biodegradation behaviour was studied in the laboratory, particularly for the Brabant and Sjoelund sites. Interpretation and quantification of processes at each field site was completed by building numerical models which drew all the data into unified interpretations. The software used for modelling was first validated by testing against a plume constructed in a laboratory sand tank. Through this process of understanding and quantifying the fate and transport at these sites, we have been able to deepen the scientific basis for the use of natural attenuation, our first goal. 

Three mathematical models were developed to estimate the length of pollution plumes, based on the CORONA conceptual model; these were built into an easy-to-use spreadsheet called CoronaScreen. This is accompanied by manuals for the software, and a guidance document to explain how natural attenuation can be assessed in the field and quantified with the new models. These simple but robust engineering tools were tested by practitioners outside the project, before being made available for free download from the project website; these activities fulfil our second goal. 


**Site Characteristics Key issues** 

Brabant, The Netherlands 

 Chlorinated solvent pollution in complex sand, peat, silt and clay sequence 

 Is there significant attenuation of chlorinated solvents and their daughter products? 

Four Ashes, UK Phenolic pollutants in sandstone aquifer 

 Previous studies at this site led to the CORONA hypothesis, and new data from the site was used to test the CoronaScreen model 

Hnevice, Czech Republic 

 Petroleum hydrocarbons in very permeable sandy gravel aquifer 

 Reoxidation at the upstream margin of a shrinking plume 

NIT, Italy Petroleum hydrocarbons including styrene in an alluvial aquifer with imposed hydraulic boundaries 

 The effects of changing hydraulic conditions on natural attenuation 

Rexco, UK Mixed ammonium and phenol pollutants in a sandstone aquifer 

 Biodegradation of ammonium in competition with organic compounds; effects of sorption by cation exchange on transport 

Sjoelund, Denmark Phenoxy acid pesticides within a landfill leachate plume, in an alluvial aquifer 

 Biodegradation of a trace pollutant within a matrix of other oxygen-consuming pollutants 

**Table 1 Summary of the field sites investigated in CORONA** 

Site knowledge exchange groups, which brought together the researchers with those interested in the site, were established for all sites. The CORONA tools and concepts were promoted at a range of meetings and conferences, and especially through courses on natural attenuation and CoronaScreen. A course has been made available on the project website together with papers, the guidance document and other material on natural attenuation, fulfilling the third goal of the project of promoting the use of natural attenuation and the CORONA tools. 

### Key research advances 

**_High resolution multilevel sampling_** 

One of the major restraints on the widespread use of MNA in Europe is the uncertainty in assessing field conditions, and so CORONA invested significant resources in devising and installing better sampling systems^2. 

The most significant mass-removal process during natural attenuation is biodegradation. The CORONA hypothesis is that certain zones, often in the fringes of a plume, offer enhanced conditions for biodegradation. Here, microbes, nutrients, contaminants and electron donors or acceptors are found together in the required ratios. These zones often have rapid degradation rates and contribute significantly to the overall reduction of contaminant mass within the entire plume. In contrast to their significance, the spatial extent of these highly reactive zones is quite small, compared to the volume of the whole plume, and is furthermore characterised by steep concentration gradients (Figure 2). These gradients generally cannot be detected using standard monitoring procedures and tools. 

(^2) Piepenbrink et al. 2003 (CORONA deliverable D7 ‘Technical report LAG/01/2003/0883’). 


 distance [m] 

 elevation [m] 

(^00 20 40 60 80 100 120) 0.5 1 1.5 2 1.00E-02c1 4.64E-03 2.15E-03 1.00E-03 4.64E-04 2.15E-04 1.00E-04 4.64E-05 2.15E-05 1.00E-05 **ammonium [g/l]** (^) **W1 W2 W3 W4 distance [m] elevation [m]** (^00 20 40 60 80 100 120) 0.5 1 1.5 (^2) EA1 1.00E-02 4.64E-03 2.15E-03 1.00E-03 4.64E-04 2.15E-04 1.00E-04 4.64E-05 **oxygen [g/l]** (^) **W1 W2 W3 W4 distance [m] elevation [m]** (^00 20 40 60 80 100 120) 0.5 1 1.5 (^2) 2.19E-02M1 2.07E-02 1.95E-02 1.84E-02 1.72E-02 1.60E-02 1.48E-02 1.36E-02 1.24E-02 1.12E-02 

#### microbe population [g/l] 

 W1 W2^ W3^ W4 

**Figure 2 Numerical simulation example of a reactive plume fringe zone at field scale.** The steady state ammonium plume (top) clearly reflects the supply of oxygen from the top of the aquifer in recharge (middle) and its consumption during the nitrification process. The environment for the growth and survival of microbe populations is restricted to a very narrow zone, where the concentration gradients of oxygen and ammonium overlap (bottom) (courtesy of U. Maier, University of Tuebingen). 

As Figure 2 indicates, multilevel sampling (MLS) with a high resolution of the order of 0.1 m or less, is essential for field investigation of natural attenuation processes within the reactive fringes. As there are no suitable commercial systems presently available to fulfil these requirements, all sampling systems that were installed within the CORONA project were custom made for each site. 

To achieve the goals of high resolution MLS, the sampling requirements at an individual site have to be defined carefully at first. Here, a fundamental aid is to work with a ‘standardised’ procedure based on a site questionnaire concerning the following issues: general site properties, aquifer properties and hydrogeology, groundwater properties and hydrogeochemistry, contamination, and existing monitoring wells. The information can be used to design a site-specific ‘ideal’ multilevel sampling system, which is: (a) made of materials and using pumping methods that do not influence the target parameters to be measured and that withstand the site-specific chemical environment, (b) able to avoid or get rid of stagnant well water, and (c) capable of sampling from the required depth and resolution. 

Some of the major problems identified and resolved during CORONA in achieving the goals of unbiased, level accurate high resolution MLS were as follows: 

 (a) The total sampled volume, which is composed of the sample volume itself, plus the volume of the stagnant water within the sampling system. This has to be removed before sampling, and 


 may finally limit the sampling resolution by its zone of influence as shown in Figure 3. The primary solution to this problem is to stop using many of the standard sampling protocols (DIN, EPA, ...) which demand huge groundwater volumes for every single compound to be analyzed. In CORONA, small diameter inertial-lift pumps and miniature gas-lift pumps were designed to provide minimum volume, high quality samples with minimal disturbance. 

 (b) The material of the sampling well, tubes and pumps may change the physico-chemical properties of the sample. In the example in Table 2, the measured concentrations are biased by sorptive losses taking into account partitioning coefficients, intra-polymeric diffusion coefficients and tube-surface to tube-volume ratios. Simple laboratory protocols were designed in CORONA to test materials in advance to inform the choices made for field installations. 

 (c) The costs of installing MLSs, particularly if multiple boreholes have to be drilled to reach and separate different depths. For unconsolidated aquifers, a direct-push methodology and associated tools were developed and tested under field conditions. For consolidated aquifers, a high resolution bundled piezometer was shown to be successful in the field. 

 Polymer C/C 0 

 PTFE (Polytetrafluoroethene) 0.94 

 PA-DK (Polyamide, brand used in DK) 0.94 

 XDPE(High density polyethylene, Waterra) 0.67 

 PA (Polyamide) 0.65 

 HDPE-USFD (High density polyethylene) 0.53 

 LDPE (Low density polyethylene) 0.47 

 PU (Polyurethane) 0.42 

 PVC (Polyvinyl chloride) 0.18 

 SI (Silicone) 0.07 

**Table 2 Prediction of normalized toluene breakthrough concentrations for nine different polymer tubing materials.** Measured for a bundle type MLS with 15 m tubing length, 4 mm tubing diameter and low flow sampling at 100 ml/min. C/C0 is the concentration at the exit of tube as a proportion of concentration in sample. 

In summary, high resolution, multi-level sampling was shown to be both feasible and cost effective at a range of sites with different geology and pollutant conditions. 


 Line-Sampler (screen 5 cm) vs. Point-Sampler 

 0.00 

 5.00 

 10.00 

 15.00 

 20.00 

 25.00 

 30.00 

 35.00 

 40.00 

 45.00 

 50.00 

 0.00 0.05 0.10 0.15 0.20 0.25 0.30 0.35 0.40 

 ne [-] 

 theoretically closest sampling intervall [cm] 

 LS 1Liter PS 1Liter LS 0.1Liter PS 0.1Liter LS 0.01Liter PS 0.01 Liter 

**Figure 3 Theoretical maximum vertical resolution of two bundle-type MLS systems: point sampler (PS) and line sampler (LS) plotted vs. aquifer porosity (ne).** 

**_Microbiological degradation processes in a heterogeneous plume in the Netherlands_** 

Soil and groundwater at the site of a metal workshop in the province of Brabant are contaminated mainly with cis-dichloroethene (cisDCE), vinyl chloride (VC) and 1,1-dichloroethane (DCA). The source of the contaminants is located underneath a large production facility, and source removal is not possible. The sources are located in the top soil layers that consist of a complex sequence of sand, peat, silt and clay. Contaminants reach the underlying sandy aquifer at a depth of 30 mbgl (metres below ground level), and the plume in the aquifer roughly has a length of 1000 m, between 40 and 60 mbgl. A bioscreen or biologically activated zone was created between 10 and 20 mbgl to stop the outflow of contaminants from the source to the plume in the aquifer. Model simulations with RT3D have suggested that the plume will fade away within 60-80 years, but there were uncertainties. Therefore the objective of the study was to investigate the occurrence, rates and locations of NA. The conceptual model of Brabant site is presented in Figure 4. It is assumed that in the aquifer distinct zones or spots exist (internal coronas) where either or both reductive and oxidative processes take place. The occurrence of these zones was investigated with high resolution sampling. 

The plume was investigated with 6 MLSs placed to 60-80 mbgl for high resolution sampling of soil and groundwater. The MLSs were placed to create a control plane perpendicular to the flow direction. The plume is “fingered” and has preferential paths. 

Groundwater chemistry, soil chemistry and redox status did not show optimal conditions for biodegradation. The soil samples were subjected to microcosm studies and molecular analyses for dechlorinating bacteria ( _Dehalococcoïdes ethenogenes_ , DE). Only after extended periods of time (>1 year) was some activity noted in the microcosms. For significant degradation, the microcosms needed the addition of DE. This agreed with the molecular analyses of the original sediments as presented in Figure 5. DE was not detected in the samples from the plume (Figure 5 MF4, MF 6). Only a groundwater sample from a 


monitoring well 100 m downstream of the bioscreen (C48) contained significant levels of DE. The strong increase of ethene in this monitoring well since the erection of the bioscreen strongly suggests that this is a result of the enhancement in the bioscreen, and the outflow of microbial activity. 

**Figure 4 Conceptual model of the plume at the Brabant site.** 

The chemical and microbial analyses offered little firm evidence for NA. Stronger evidence was found in the stable isotope analyses, supported with the increase of degradation products along the central flow path (see Figure 6 and Figure 7). A stable isotope shift from -20 to +3‰ means that the relative amount of the 

(^13) C atom in cisDCE has increased significantly as a result of microbiological degradation. Bacteria prefer to degrade 12 C molecules over 13 C molecules, thus changing the 12 C:^13 C ratio of the remaining compound. The initial decrease of VC composition (from -28 to -33‰) corresponds with its production from cisDCE with a high 12 C content. II-1 II-2 II-3 (^) C 48 30m bgl 

#### Positive 

#### controls 

#### M F4, M F6, 

#### C 50 7 en 15 m 

#### N egative 

#### control 

#### Bio s cr e e n 

#### 1 0 0 m 

#### d o w n s t r e a m 

II-1 II-2 II-3 (^) C 48 30m bgl 

#### Positive 

#### controls 

#### M F4, M F6, 

#### C 50 7 en 15 m 

#### N egative 

#### control 

#### Bio s cr e e n 

#### 1 0 0 m 

#### d o w n s t r e a m 

**Figure 5 Molecular analyses of sediment samples showing** **_Dehalococcoides etheogenes_** **is only present in or near the biobarrier** 


 Fractioning along flowpath 

 -40,00 

 -30,00 

 -20,00 

 -10,00 

 0,00 

 10,00 

 0 200 400 600 800 

 distance from source (m) 

 d 13C fractio n in g 

 VC d13C 

 cis-1,2 dichloroethylene d13C 

**Figure 6 Stable isotope fractionation along the flow path at Brabant** 

 0% 

 10% 

 20% 

 30% 

 40% 

 50% 

 60% 

 70% 

 80% 

 90% 

 100% 

 C40 I I -1 NOB 2 M LS3 M LS6 

 E T H V C c DCE 

**Figure 7 Degradation products in monitoring wells along flow path** 

Overall, the studies at Brabant showed: 

- Natural attenuation does occur in the plume, but could only be confirmed with stable isotopes in     combination with the relative increase of the products VC and ethene. 

- Although the conditions in the aquifer are sub-optimal, the introduction of just _Dehalococcoïdes_     _ethenogenes_ in the microcosms increased degradation rates. 

- Microbial activity in the aquifer is currently very low. The low (and improved) detection limits of     direct microbial methods such as microcosms and molecular techniques are critical to detecting     activity in this plume. 

- The microbial activity of the bioscreen seems to have migrated into the plume and should reduce     plume life. 

- The low indigenous microbial activity together with bacterial migration from the bioscreen is     estimated to lead to a plume life of 40-60 years. 

- The MLSs proved to be a very efficient tool for characterising a cross section of this irregular     plume. 


**_Reoxidation at the upstream end of a hydrocarbon plume, Hnevice, Czech Republic_** 

The research site Hnevice has been seriously contaminated by petroleum hydrocarbons since the 1940s. The Quaternary aquifer is composed of very permeable sandy gravel, with hydraulic conductivities from 10 -3^ to 10-4^ m.s-1. The water flow rate is about 1 m d-1^ and the water level is 4-6 mbgl. The objective of research at this site was to understand the redox processes at the upstream end of a hydrocarbon plume, particularly the reoxidation processes occurring as the plume shrinks in size. 

Five MLSs and 12 piezometers were installed upstream of and in the rear of the plume, where ambient ground water containing high concentrations of electron acceptors enter the contaminated area. Based on groundwater and solid phase geochemistry, a conceptual model with four different geochemical zones was developed (Figure 8). A full sequence of redox zones (sometimes overlapping) were identified with degradation processes occurred in vertically thin zones (up to mm). Zone I is the background unpolluted aquifer, with aerobic groundwater and an absence of reduced species in significant concentrations. Zone II is situated in the plume core with methanogenic, sulphateand iron-reducing conditions accompanied by ankerite and kutnahorite precipitates and significant depletion of the oxidation capacity of the aquifer. Coating of iron oxide surfaces with reduced iron phases in Zone II appears to limit iron reduction and makes sulphate reduction and methanogenesis occur in the presence of bio-available Fe(III). Zone III is a mixing (corona) zone, situated at the fringe of the plume with high biodegradation rates, nitrate, manganese and iron reducing conditions and Fe(III) precipitates. In Zone IV Fe(II), mineral reoxidation (with e.g. psilomelane and cornelite present) is typical. 

**Figure 8 Locations of the reactive zones at the Hnevice site.** Groundwater flow is from left to right, see text for further explanation. 

The reactive transport code PHT3D was used to confirm the major features of the geochemical evolution at the site. In the study, the multicomponent hydrocarbon mixture found at the site was approximated by one reactive component – toluene – and a non-reactive residual mass. The dissolution of toluene from this 2component mixture was calculated by Raoult’s Law. The degradation of toluene in the dissolved phase generated carbon and hydrogen which in turn triggered geochemical changes including the precipitation of siderite and FeS. 

The simulations showed a gradual retreat of the free phase plume, accompanied by moving, sharp interfaces between oxygen, nitrate and ferrihydrite consuming zones. In contrast, there was an overlap between the ferrihydrite and the sulphate consuming zones. The results indicated enrichment with secondary ferrihydrite due to the re-oxidation of dissolved ferrous iron at the lower plume fringe. The model demonstrates the important role of the vertical transverse dispersivity in the evolution of the redox processes and natural attenuation. Higher values increased the rate of biodegradation, resulted in low 


concentrations of dissolved iron and less precipitation, and increased the thickness of the secondary ferrihydrite precipitation zone below the plume. 

The former free phase zone (Zone IV) can severely limit the penetration of electron acceptors into the contaminant plume because the re-oxidation of precipitates may consume a significant part of the oxidation capacity of groundwater and recharge entering the plume. Electron balance calculations based on the rate constants obtained from the plume calibration indicated that about 95.5 % of electron acceptors reach the free phase plume and only about 4.5 % are consumed in the re-oxidation zone. However, the electron acceptor consumption is very sensitive to rate constant values, for example, rates higher by a factor of 10^3 only allow about 58.2 % of EA reach the free phase plume. This has serious implications for the attenuation potential at many sites, increasing the time until the aquifer returns to fully aerobic conditions. 

Two tracer experiments with MTBE and bromide provided dispersivity values in the longitudinal and vertical transverse directions. Longitudinal dispersivity is relatively small (10 cm). Vertical transverse dispersivity is very high compared to literature values (about 6 mm) and also higher than in well-controlled tank experiment media. This may be explained by the high content of gravel (average 60%, diameters up to 8 cm), which produces very large vertical spreading. 

In summary, the Hnevice site shows: 

- Natural attenuation by oxidation of hydrocarbons will generally created a zone of reduced minerals     in the aquifer. 

- This reduced zone will become a significant sink for oxidants entering the plume and will slow     down completion of biodegradation of the hydrocarbon contaminants. 

**_Natural attenuation in changing flows at the NIT site, Italy_** 

The NIT site is an oil refinery and chemical processing plant with significant petroleum hydrocarbon contamination, including large LNAPL (light non-aqueous phase liquid) pools. The site hydrogeology is complicated in that groundwater heads and flow directions are controlled by interactions with a river, a canal and a hydraulic barrier where groundwater is pumped to control groundwater pollution. 

The objectives of the field study at NIT were (1) to determine if natural attenuation was occurring, and what type of monitoring was required to observe it, (2) to quantify fringe and core processes using MLS data and simulation techniques. 

Ten MLSs with 0.5 m resolution were installed, using a numerical model of groundwater flow patterns to determine the optimum locations. Four rounds of sampling were performed, with additional data provided by the Environmental National Agency from 22 long screen wells. 

Changes in concentration were observed which were linked with seasonal variations in hydraulic conditions (Figure 9). Changing heads in pumping wells and water levels in the canals bounding the site were seen to cause variable flow velocities and directions. These are likely to increase natural attenuation by increasing mixing of the contaminants with uncontaminated groundwater. However the fluctuating water table creates a smeared zone by raising and lowering the LNAPL pools, which generates pulses in contaminant concentration. As result, the behaviour of the aquifer system is really complex to monitor and more than 3 MLS were needed to find a flow line. 

Natural attenuation was detected, principally through the use of stable isotopic analysis, with δ^18 O and δ^13 C of dissolved inorganic carbon showing an accumulation of biogenic products along a flow line. Hydrochemical results from the MLSs confirmed these results, but the standard long-screened wells were not able to provide useful information on dispersivity and redox zonation, which are key factors in NA assessment. Analysing the NAPL composition identified a significant amount of sulphate was present, and 


δ^32 S measurements showed that it was an electron acceptor in biodegradation. This finding improved the conceptual model, in which every source of electron donor and acceptor must be taken into account to quantify the natural attenuation potential. 

If the high concentrations found in the plume’s core were inhibitory to bacteria, they would slow the rate of biodegradation, particularly for the anaerobic respiration processes occurring in the core. Laboratory microcosms were used to assess inhibition of degradation by the contaminant mixture. The laboratory experiments confirmed that the degradation rate decreases when contaminant concentration is high, and that each compound has its own degradation rate. 

**Figure 9 Effects of the transient flow field on ethylbenzene concentrations.** Simulations were made using MT3D during a flood event (left picture) and during baseflow recession (right picture); contour levels range from 1 mmol/l (red) to 1e-6 mmol/l (light blue); the blue rectangle is the area with the MLSs grid. 

 Using a site-specific version of PHT3D, the conceptual model of processes at the site was confirmed by simulating the field observations. This included (1) inhibition by the substrate, (2) a sulphate source in the LNAPL, and (3) movement of the LNAPL pool with the movements of water table. This enabled us to quantify the overall natural attenuation behaviour. 

 Overall, the study of the NIT site showed: 

- The site-specific characteristics of the site (e.g. hydraulic boundaries in space and time, sources     of electron acceptors) must be taken into account, even if the site has fairly common pollutants     such as petroleum hydrocarbons. 

- Contaminants can be inhibitory to bacterial processes and slow the core biodegradation processes     significantly. 

- Conventional sampling systems are not sufficient to reveal the complexities of plume behaviour     and must be supplemented with MLSs. 


**_Ammonium and phenol plume at Rexco site, Mansfield, UK_** 

Rexco, near Mansfield in the UK, was the site of a coal gasification plant from 1935 to 1969. Serious pollution of groundwater in the underlying Permo-Triassic sandstone aquifer arose from the spillage of wash water from the process from 1955 onwards. The water contained, amongst other chemicals, 10-20 g/l of ammonium and ~15 g/l of phenol. The objectives of the study were (1) to understand the processes of phenol degradation and test the hypothesis that the phenol pollution had naturally attenuated, (2) to understand the mechanisms and estimate the amount of ammonium degradation, and (3) to quantify the sorption of ammonium and hence the retardation of its movement with groundwater. 

Two new high resolution MLSs were installed to complement the 10 MLSs and 30 other boreholes already existing on site; these were used to measure vertical profiles of groundwater chemistry and microbiology through the ammonium plume. Ammonium oxidation was studied in microcosms. Extensive reactive transport modelling was undertaken using PHT3D^3. 

From the numerical modelling of the plumes, which was validated by field data, the phenol plume was shown to have completely biodegraded. This occurred within 20 years of the end of the source input. Sulphate was present in high concentrations in the source, and this electron acceptor accounted for ~64% of the phenol degradation by the end of the source input, with fringe processes accounting for a further 20% of the degradation. Without the sulphate in the source, the phenol would still be present at high concentrations, as the supply of electron acceptors through fringe processes would be much slower. At this site, the supply of fringe electron acceptors for phenol degradation is reduced by two factors, the reoxidation of the reduced aquifer materials and the continuing oxidation of the ammonium plume. 

Field data from the MLSs and laboratory microcosms showed that ammonium is oxidised to nitrate at the fringe of the plume and so will, eventually, be naturally attenuated. Molecular analysis of groundwater samples showed that aerobic as well as anaerobic ammonium-oxidizing bacteria were present (Figure 10). The latter bacteria use nitrite as an electron acceptor to oxidise ammonium and to form N 2. This is an exciting discovery, since these so-called anammox bacteria have never been reported in groundwater before. In some samples, they accounted for 25% of all eubacteria present. We were not successful at incubating them in microcosms and demonstrating the anammox process was occurring. Understanding their role and implications for other such plumes will require further research. If the anammox process does occur in the aquifer, it could significantly shorten the life of the plume, as the products of aerobic ammonium oxidation can assist in removing more ammonium. 

Sorption by cation exchange was shown to be a major but complex factor in the fate and transport of ammonium. Sorption could not be adequately represented by a linear isotherm, as the effective linear partition coefficient varied from 0.07 to 1.5 over the evolution of the plume. The higher values apply to the later history of the plume, reducing the effective velocity of the ammonium to low values, and helping to reduce risk to downstream receptors. After 45 years of the plume’s life to date, about 88% of the ammonium was sorbed to the aquifer, and 1.5% had oxidised to nitrate. 

(^3) Haerens, B., 2004. Reactive transport modelling of a groundwater contamination from a former coking plant. PhD thesis, Hydrogeology and Engineering Geology, Fac. Of Sciences. KU Leuven, Belgium. 


## BH102 BH101 

## M 1 2 3 4 5 6 7 8 9 10 11 12 13 14 + M 

**Figure 10 Molecular microbiological analyses of groundwater samples from Rexco demonstrating the presence of anammox bacteria.** PCR with specific primers showed the presence of anammox bacteria in samples of boreholes BH102 and BH101. Lanes 1 – 9: BH102samples of 18 – 26 m depths; lanes 10 – 14: BH101 samples of 16 – 20 m depths; + is the positive control, M is the molecular size marker. 

Overall, the studies of Rexco show: 

- Phenol can naturally attenuate quite rapidly, but that ammonium pollution will be long-lived. 

- Sulphate is a major contributor to biodegradation, because it is present in high concentration in the     source, reducing the significance of fringe processes for phenol. 

- Fringe biodegradation with oxygen is the only biodegradation process operating for ammonium,     but is slow due to the lack of oxygen. Sorption of ammonium by cation exchange is an important     process which slows migration. 

- Mixed plumes will have complex behaviours with interferences between the contaminants, for     example, competition for available electron acceptors. 

**_Sjoelund site, Denmark_** 

The Sjoelund site (Denmark) is an old landfill site where leachate has created a contaminant plume in the underlying sandy aquifer (Tuxen et al 2003). The landfill was in use from 1965 to 1975 and received household waste, demolition waste and almost certainly some chemical waste. It covered an area of 6300 m^2 and had an average height of 5 m. Neither liners nor leachate collection systems exist. The landfill was located on a glacial outwash plain in a farmland area. 

The aquifer of different glacial sediments comprises an unsaturated zone of 15-18 m over a 3-5 m thick saturated zone. Organic carbon in leachate from the landfill in mg/L concentrations has resulted in the development of an anaerobic plume in the otherwise aerobic aquifer. Different micropollutants such as phenoxy acid herbicides including MCPP and dichlorprop were the compounds of major concern; these are compounds which are often identified at landfill sites^4. 

Field data was obtained from three MLSs (30 sampling points each, 12.5 cm increments) as well as from traditional boreholes. Chloride was used as an inert leachate indicator, while redox-sensitive parameters (oxygen, nitrate, manganese, iron etc.) and phenoxy acids and related compounds (MCPP, dichlorprop, 2CPP, 4-CPP; Reitzel et al. 2005) were monitored. Undisturbed sediment cores were collected across the plume fringe adjacent to one of the MLS and divided into 5 cm pieces. Those samples were used for phenoxy acid degradation experiments that mimicked the intrinsic conditions in the aquifer. 

(^4) Baun, A., Ledin, A., Reitzel, L.A., Bjerg, P.L. & Christensen, T.H. 2004: Xenobiotic organic compounds in leachates from ten Danish MSW landfills chemical analysis and toxicity tests. _Water Research_ , 38, 3845-3858. 


The vertical profiles display steep gradients of chloride in the plume fringe from which very small vertical dispersivities (2-3 mm) were deduced by solute transport modelling^5. The redox chemistry and phenoxy acid concentrations were also changed significantly across the fringe (Figure 11). The decrease of phenoxy acid concentrations was very steep – in one MLS the concentrations of dichlorprop fell from 300 μg/L to below detection limit within 1 m. 

**Figure 11 Conceptual model of the contamination as well as results of selected parameters from two multi-level samplers.** 

The laboratory degradation experiments with aquifer material across the fringe zone revealed a highly increased degradation potential at the narrow plume fringe, governed by the presence of phenoxy acids and dissolved oxygen (Figure 12). Oxygen is a prerequisite for degradation of phenoxy acids and increased oxygen levels enhance degradation rates (Tuxen et al. 2005). This resulted in the proliferation of a microbial population of specific phenoxy acid degraders, which further enhanced the degradation potential for phenoxy acids at the fringe (Tuxen et al. submitted). 

(^5) Prommer, H., Tuxen, N. & Bjerg, P.L. 2004: The importance of fringe processes for natural attenuation of phenoxy acids in landfill leachate plumes. _Geochimica et Cosmochimica Acta_ , 68, (11S), A391. 


**Figure 12 Specific degraders and degradation potential (expressed as evolved radioactively labelled CO 2 in the microcosms) across the fringe 50 metre down gradient from the landfill.** 

From the combination of all results it was concluded that: 

- A small vertical, transversal dispersivity can be quantified by high resolution multi level sampling     and reactive solute transport modelling. 

- The primary degradation takes place at the fringe of the plume, where there is a co-existence of     oxygen and phenoxy acids. 

- An increased number of specific phenoxy acid degrading bacteria are present at the fringe. 

- Fringe processes govern the fate of phenoxy acids at the landfill site. 

- Natural attenuation of phenoxy acids is occurring in the aquifer. 

**_Laboratory microbiology_** 

The laboratory microbiology was focussed on the natural attenuation of chloroethenes, the groundwater pollutants of the Brabant site in the Netherlands. It is normally assumed that natural attenuation of chloroethenes is governed by a reductive dechlorination process catalyzed by anaerobic bacteria, a process that can lead to the formation of harmless ethene. Dechlorination rates are estimated by measuring the parent compound and the dechlorination products along the plume in the aquifer, supposing that no other process is causing the dechlorination. Recent investigations in other laboratories indicated that anaerobic oxidation of vinyl chloride and ethene may occur under iron-reducing conditions. Hence, the rates of natural attenuation of chloroethenes based on dechlorination rate determination could be an 


underestimation of the actually occurring natural attenuation. The objectives of our laboratory microbiology studies were to provide evidence for anaerobic vinyl chloride oxidation, to develop a molecular tool for enumerating dehalorespiring bacteria, and detecting whether they are active or not. 

The first objective was studied in aquifer microcosms. Using sand samples from the contaminated site, we filled three columns enriched with anaerobic Fe(III)-coated sand with different set-ups. One column was fed with only vinyl chloride (VC), one with VC and acetate, and one with VC and a bactericide, mercury chloride (HgCl 2 ). The columns were operated for 21 months and analyzed periodically. Reductive dechlorination and methanogenesis took place in the column fed with VC and acetate, and disappearance of VC without obvious product formation was observed in the other two columns. Stable isotope analysis showed that in the VC-only and VC + HgCl 2 fed columns, the enrichment factor, ε, for 13 C in VC was between -1 and -5, while in the VC and acetate-fed column, the ε-value was between -13 and -18. Literature values for reductive dechlorination of VC range between -20 and -25. The absence of the dechlorination product ethene in the VC-only and VC + HgCl 2 fed columns and the clearly different ε–value indicate that the disappearance of VC in these two columns is due to another process, possibly anaerobic microbial VC oxidation. The ε-value in the VC and acetate-fed column was probably the result of two processes, reductive dechlorination and anaerobic VC oxidation. Iron speciation analyses of certain zones after dismantling the columns showed that in the VC and acetate-fed column, most of the Fe(III) was gone, while in the VC-only column, the concentration of Fe(III) was in the same range as the initial iron concentration. This suggests VC oxidation without concomitant iron reduction. In conclusion, the column studies gave indirect evidence that anaerobic VC oxidation might occur at the Brabant site and that the plume length and plume life estimated by using dechlorination rates are maximal values and might be lower in reality. 

For the quantification of dehalorespiring bacteria and the detection of their state of activity, we set up realtime PCR methods for _Dehalobacter_ spp., for _Desulfitobacterium_ spp. and _Dehalococcoides_ spp., and then tested the limits of this system. Absolute quantification was difficult due to different efficiencies between the templates, but relative quantification determining the population size within a bacterial community was easily possible (Smits et al. 2004). The ratio between 16S rRNA molecules and 16S rRNA genes was tested as indicator of metabolic activity of the cells. In a pure culture _Desulfitobacterium hafniense_ strain TCE1, this ratio during growth on lactate and PCE determined by real-time PCR varied between 100 and 12000 for actively growing cells, and decreased to 1-2 after one week of stationary phase. The method is reproducible and the results indicated that this ratio could be used as parameter for metabolically active or inactive cells. The method has still to be tested on microcosms and field samples. 

**_Laboratory plume model_** 

Glass tank experiments were used for high precision measurements of conservative and reactive tracer dispersion rates in various artificial (glass beads) and natural (sand) porous media (Figure 13). The results show that the transverse dispersivities are very small (< 0.25 grain diameter) and that they apparently decline with increasing flow velocity. The data obtained in the conservative tracer experiments led to a new empirical relationship taking into account a nonlinear increase of the dispersion coefficient with the Peclet number (Figure 14) (Olsson and Grathwohl, in prep.). 

This new relationship allowed pure forward prediction (that is, without any fitting of parameter values) of dispersion controlled reactions in a second set of tank experiments which established steady-state reactive plumes (Ham et al. submitted). These experiments measured vertical concentration gradients at the outlet of the tanks at high resolution. Such vertical chemical gradients are relevant for biodegradation in sediments and aquifers and have recently received much interest in the relatively new field of geobiology^6. 

(^6) Amend, J., Emerson, D., Edwards, K., Gralnick, J., Grathwohl, P., Hoehler, T., Kappler, A., Straub, K. 2005: Microbial activity in biogeochemical gradients. _Geobiology_ (submitted). 


On the other hand, experiments aiming at steady-state reactive plumes can be used to very simply derive transverse dispersion coefficients (Cirpka et al. 2005). The data obtained in the reactive transport experiments were used to validate the numerical model of reactive transport, PHT3D, which was used for the field and scenario modelling, reported below. 

 Middle inlet: Fluorescein Porous medium 

 Flow direction 

 Pump Sampling vials x 11 

 Pump 

 Inlet Outlet 

 Containers for tracer solutions and water 

 Middle inlet: Fluorescein Porous medium 

 Flow direction 

 Pump Sampling vials x 11 

 Pump 

 Inlet Outlet 

 Containers for tracer solutions and water 

**Figure 13 Schematic drawing of the laboratory plume experiment** 

In summary, the laboratory plume studies led to: 

- A new, more extensive predictive equation for dispersion coefficients; 

- Validation of the numerical model being used for field studies. 

**_Numerical model development and use_** 

The existing reactive multi-component transport model PHT3D (Prommer et al. 2003) was selected as a platform for additional numerical model development. Model testing, benchmarking and documentation were completed during the initial phase of the project. The PHT3D code is based on two widely used standard tools, the solute transport simulator MT3DMS^7 and the geochemical model PHREEQC-2^8. The resulting coupled model allows the simultaneous simulation of the fate of organic or inorganic contaminants and of the resulting primary and secondary geochemical changes, including water-sediment reactions such as mineral dissolution/precipitation and ion-exchange. The model and related information have been made available through a website (http://www.pht3d.org), where details of collaborative applications and developments in other projects can also be found. 

(^7) Zheng, C., Wang, P.P., 1999. MT3DMS: A modular three-dimensional multispecies model for simulation of advection, dispersion and chemical reactions of contaminants in groundwater systems. Documentation and User’s Guide, Contract Report SERDP-99-1, U.S. Army Engineer Research and Development Center, Vicksburg, MS (available at [http://hydro.geo.ua.edu).](http://hydro.geo.ua.edu).) (^8) Parkhurst D.L., Appelo C.A.J., 1999: User’s guide to PHREEQC (Version 2). A computer program for speciation, batchreaction, one-dimensional transport, and inverse geochemical modeling, U.S. Geol. Survey Water Investigations Report 99-4259. 


**Figure 14 Transverse dispersion coefficients plotted against the Peclet number, together with experimental results of other studies and fitted equations** 

The preparation of numerical models for the individual CORONA field sites and for the CORONA laboratory experiments was carried out by developing site-specific PHT3D reaction modules, each based on the corresponding conceptual hydrochemical model. The flexibility of the approach allowed us to constantly adapt the reaction modules as soon as new site-specific knowledge became available and to easily test alternative conceptual models as part of the field and/or lab data interpretation. 

PHT3D was furthermore used to complement the testing of a newly developed analytical solution to analytically predict the plume length of reactants (e.g., a contaminant which acts as electron donor) governed by bimolecular reactions in a two-dimensional aquifer (Ham et al. 2004). It was used for the scenario modelling that was aimed at identifying the sensitivity of plume length to key parameters such as transversal dispersivity, thickness of the contaminant source, flow velocity and groundwater recharge (Rolle et al. 2005). 

Field-scale PHT3D applications to CORONA sites were carried out for the BTEX/Styrene contaminated NIT site, to simulate the fate of phenoxy acids within a landfill leachate plume at the Sjoelund site (Figure 15), to simulate and investigate the role of iron cycling at the HRC site (Vencelides et al. in prep.), and to simulate the fate of the ammoniacal liquor contamination at the Rexco site^3. 


**Figure 15 Simulated chloride plume at the CORONA field site Sjoelund.** 

In summary, a sophisticated numerical code, PHT3D, was completed, validated, and customised for use within CORONA. In particular, it was used to interpret several of the field sites, and help to develop final, quantitative numerical models. 

**_CoronaScreen and guidance_** 

A key end-user output from the Corona project is CoronaScreen, which is a public-domain decision-support tool for the performance assessment of natural attenuation of plumes in groundwater (Thornton et al in preparation). It is derived from the Corona concept for plumes and includes three models, based on different approaches to estimate plume length and other parameters required in the evaluation of plume behaviour. 

The three alternative models included within CoronaScreen are created using different conceptual bases to evaluate plume behaviour. These concepts, and the key features of each model, are: 

 (a) a new closed-form analytical solution to the advection-dispersion transport equation (Ham et al. 2004, Guttierrez-Neri et al. in preparation). Electron donor inputs (e.g. contaminants) from the source area are compared with electron acceptor inputs from the background groundwater to determine plume length and time to reach steady-state along an idealised flow path when these inputs are balanced. This model is capable of simulating transient and steady-state electron donor inputs and also produces a centreline and vertical profile of contaminant concentration as a function of distance from the source. 

 (b) An electron balance model, in which electron donor fluxes entering the aquifer from the source area are balanced with electron acceptor inputs from background groundwater and biodegradation 


 processes in the plume core^9. This model can determine the steady-state plume length, electron donor flux at any distance (e.g. compliance point) before this length, and estimates a plume-scale first order degradation rate. It also considers sorption of contaminants in mixtures, when estimating these outputs, provides a plume-scale mass balance and includes the contribution of plume fringe and plume core degradation processes in natural attenuation. 

 (c) A travelling 1-D transport model, in which traverse dispersive mixing of electron donors and acceptors at the plume fringe is coupled to degradation using the PHREEQC geochemical code to simulate the steady state plume length, based on the time required for contaminant mass in a column of groundwater leaving the source area to be consumed. The outputs from this model are vertical profiles of electron donor and electron acceptors across the plume fringe as a function of distance along the flow path. 

**Figure 16 Opening view of CoronaScreen performance assessment model.** 

(^9) Thornton, S.F., Lerner, D.N. & Banwart, S.A. (2001) Assessing the natural attenuation of organic contaminants in aquifers using plume-scale electron and carbon balances: Model development with analysis of uncertainty and parameter sensitivity, _J. of Contaminant Hydrology,_ 53, 199-232. 


**Figure 17 Example output from CoronaScreen, showing estimates of plume length.** 

CoronaScreen is designed for oxidisable contaminants only and is not applicable for contaminants which are degraded by reduction (e.g. chlorinated hydrocarbons). There are important conceptual and technical innovations in CoronaScreen, which are a significant improvement upon existing screening models for natural attenuation assessment. These are (a) the conversion of all mass inputs (electron donors and electron acceptors) to a common form, electron equivalents, which simplifies the mathematical analysis and allows complex mixtures of these inputs to be included in plume predictions; (b) a new mathematical formulation describing the relationship between plume fringe thickness and aquifer dispersivity, as a function of distance from the source, allowing these parameters to be determined for individual sites. Figure 16 shows the opening view of CoronaScreen, while Figure 17 is an example of the outputs, showing predictions of plume lengths for a potential pollution plume. Data inputs for CoronaScreen are groundwater chemistry and aquifer properties easily obtained from site investigations for natural attenuation assessments. Illustrated user guides are provided for installation and interpretation using the various models in CoronaScreen. The models have been shown to be robust by validation testing against a range of real and synthetic sites from the EU and elsewhere. Predicted plume lengths are sensitive to transverse dispersivity, which can be estimated from field data using CoronaScreen. 

CoronaScreen and the supporting information are freely available for download from the project website. 

### CORONA knowledge exchange 

The overall aims of the CORONA project were to strengthen the scientific base of Monitored Natural Attenuation (MNA) as a feasible soil remediation strategy and to disseminate this knowledge into society. To accomplish this, it was crucial that the scientific research was focussed on the important issues and that results were made available quickly to the end-user community. Apart from the normal lectures at 


international conferences and publications in the scientific literature a Knowledge Exchange Group was created. This provided links with other project or network initiatives, as well as with a subgroup of regulators. The aim of the continuous knowledge exchange was to distribute the information to problem owners, regulators and scientists and to interactively discuss and adjust the outcomes of the project. Their remarks were reworked in the final version of reports, guidance document and the training course. An overview of the process is given in Figure 18. 

During the nearly 4 year project period the following knowledge exchange activities took place: 

- Yearly site knowledge exchange meetings at all 6 field sites; 

- Presentations at international meetings and workshops such as Consoil and Nicole, and at EU-     project meetings such as Welcome, Joint and Image-train; 

- A special session at the American Geophysical Union Fall 2003 conference convened by     CORONA scientists. 

- Realisation of a project web-site [http://www.shef.ac.uk/corona;](http://www.shef.ac.uk/corona;) 

- Delivery of a training course for the NA guidance document and the CoronaScreen model; 

- Release of a web-based version of the training course. 

- Organization of two international Knowledge Exchange and International Regulator meetings.     These were organized European conferences at ConSoil (Gent, 2003) and the Dechema     conference (Frankfurt, 2005). At the latter meeting, the final results of CORONA were presented     through the CORONA course (see below), and platform presentations, and posters. 

**Figure 18 Organisation of knowledge exchange between CORONA and external parties** 

To maximise dissemination of the key learning from the CORONA project to the widest possible audience, an interactive natural attenuation training course was developed by the project team. The course was designed to provide both the specialist and technically literate non-specialist with an introduction to: 

- the scientific principles underpinning natural attention; 

- the key findings of the CORONA research; 

- the application of the CORONA approach to the cost-effective assessment of natural attenuation; 

- the use of the CoronaScreen model as a decision-support tool. 

The course has been designed to communicate the key learning and deliverables from CORONA through a combination of tutor-led presentations and hands-on exercises on the application of CORONA techniques and the CoronaScreen model to example contaminated sites. The CORONA training course was 


presented as a one-day course to an audience of 17 European and North American delegates attending the Dechema 2nd^ European conference on Natural Attenuation (Frankfurt, May 2005) and has been made available as a stand-alone training course at [http://www.shef.ac.uk/corona.](http://www.shef.ac.uk/corona.) The availability of the web-based training has been publicised through a number of national and international organisations, including NICOLE and CLU-IN. 

The UK Environment Agency has contracted the project team to deliver a one day version of the course to its staff in regional offices. The project team also plan to deliver the course in several European countries during 2006 and of course all the materials (lectures, guidance document, CoronaScreen software and manual) will remain available from the website. Scientific publications will continue in the peer-reviewed literature as papers are completed and submitted. 

### Research impacts and benefits to society 

The development of unified guidance and the CoronaScreen model will provide a standard platform for the interpretation of site data and consistent performance evaluation of the viability of MNA as a sustainable remediation option for contaminated groundwater in the EU. The development of this technical guidance will provide significant benefit to EU countries that do not currently have a framework to evaluate MNA at contaminated sites but also fits within the evaluation framework recommended by those countries that have published MNA guidance. Moreover, the development of a generic performance model for a representative range of EU sites provides increased confidence in the prediction of MNA feasibility for contaminated groundwater in the community, using relevant site data, which can be obtained more cost-effectively. The uptake of these tools will be facilitated by the CORONA web-based training course and other scientific outputs. 

**_Take up of CORONA principles_** 

The UK Environment Agency has already agreed to incorporate CORONA’s new equations for plume length into its risk assessment tools. As noted above, it has requested training for its staff in the CORONA concepts. When its NA guidance is updated, the CORONA principles will be incorporated. In the meantime, the CORONA guidance document will be published in hard copy by CL:AIRE (www.claire.co.uk), an organisation dedicated to dissemination of science and technology innovations in the remediation of contaminated land. The final results will be sent to the co-ordinators of the Natural Attenuation Research Program in Germany and will be used in setting German guidelines for implementation of NA at contaminated sites. Monitored natural attenuation has been implemented as a remedy at the Sjoelund site. In the Czech Republic, manufacture of multilevel samplers has been started as a direct result of the project to enable further sites to be assessed using the CORONA principles. 

### ACKNOWLEDGEMENTS 

This research was supported by the European Commission under contract EVK1-2001-00087, and by the Swiss Federal Office for Education and Science (project 01.0119). Additional funding was provided by the Cowi-Foundation, the County of Soenderjylland and the Technical University of Denmark. 

The owners of the six field sites are thanked for providing access to the sites, background information, and permission to use the data for research. The project would not have been possible without their willing support. 

OPV Ltd., a consulting company based in Prague, gave substantial support through the provision of chemical analyses valued at ~€40 000. 

The two non-university partners, ESI and TNO, both provided major contributions to their own costs of taking part in CORONA.. Parts of the project where TNO was involved were also supported by the Dutch research programme TRIAS. 


### PUBLICATIONS 

Cirpka, O.A., Olsson, Å., Ju, Q., Rahman, A., Grathwohl, P. 2005. Determination of transverse dispersion coefficients from reactive plumes lengths. Accepted for _Ground Water._ 

Guttierrez-Neri, M., Watson, I. and Lerner, D.N., Analytical solution to contaminant transport with a combined kinetic and instantaneous reactions biodegradation model. In preparation. 

Ham, P.A.S, Schotting, R.J., Prommer, H., and Davis, G.B. 2004. Effects of hydrodynamic dispersion on plume lengths for instantaneous bimolecular reactions. _Advances in Water Resources_. 27, 803-813 

Ham P.A.S., Prommer, H., Olsson, A.H. Schotting, R.J., Grathwohl, P.: 2005: Predictive modelling of dispersion controlled reactive plumes at the laboratory scale. Submitted to _Journal of Contaminant Hydrology._ 

Olsson, A.H., Grathwohl, P. 2005: Transverse dispersion of non-reactive tracers in homogeneous porous media: A new nonlinear relationship to predict dispersivity. In preparation. 

Prommer, H., Barry, D.A., and Zheng, C. 2003. PHT3D – A MODFLOW/MT3DMS based reactive multi-component transport model. _Ground Water,_ 42(2), 247-257. 

Reitzel, L.A., Tuxen, N., Ledin, A. & Bjerg, P.L. 2004: Can degradation products be used as documentation for natural attenuation of phenoxy acids in groundwater? _Environmental Science and Technology_ , 38, 457-467. 

Rolle, M., Piepenbrink, M. Prommer, H., Ptak, T. and Grathwohl, P. 2005. Contaminant transport scenario modelling as a tool for a critical evaluation of natural attenuation. In: Proc. Aquifer Vulnerability and Risk, 4 Congress on the Protection and Management of Groundwater, Parma, 21-23 September 2005. 

 th 

Smits, T. H. M., Devenoges, C., Szynalski, K., Maillard, J., Holliger, C. (2004). Development of a real-time PCR method for quantification of the three genera _Dehalobacter, Dehalococcoides,_ and _Desulfitobacterium_ in microbial communities. _Journal of Microbiological Methods_ 57:369-378. 

Thornton S.F., Hüttmann A.H., Lerner, D.N., Wilson R.D. and Gutierrez-Neri, M., 2005. CoronaScreen: a new decision-support modelling tool for the evaluation of natural attenuation of plumes in groundwater. In preparation. 

Topinkova, B., Nesetril, K., Datel, J., Nol, O. and Hosl, P (2005). Geochemical heterogeneity and isotope geochemistry of natural attenuation processes in a gasoline-contaimnated aquifer at the Hnevice site, Czech Republic. Submitted to _Hydrogeology Journal._ 

Tuxen, N., Ejlskov, P., Albrechtsen, H.-J., Reitzel, L. A., Pedersen, J. K., and Bjerg, P. L., 2003. Application of natural attenuation to ground water contaminated by phenoxy acid herbicides at an old landfill (Sjoelund, Denmark). _Groundwater Monitoring and Remediation_ , 23, (4), 48-58. 

Tuxen, N., Reitzel, L.A., Albrechtsen, H-J. & Bjerg, P.L. (2005): Addition of oxygen enhances phenoxy acid biodegradation in ground water at contaminated sites. _Groundwater_. Accepted. 

Tuxen, N., Albrechtsen, H-J. and Bjerg, P.L.: Identification of a reactive degradation zone at a landfill leachate plume fringe using high resolution sampling and incubation techniques. Submitted. 

Vencelides, Z., Sracek, O., and Prommer, H. Iron cycling and its impact on the electron balance at a petroleum hydrocarbon contaminated site in Hnevice, Czech Republic. In preparation. 


### THE CORONA CONSORTIUM AND CONTACT DETAILS 

For further information, visit the CORONA website at [http://www.shef.ac.uk/corona,](http://www.shef.ac.uk/corona,) contact the coordinator, David Lerner at d.n.lerner@shef.ac.uk, or contact the various partners directly at the addresses below. 

University of Sheffield – Western Bank, S10 2TN Sheffield – United Kingdom Individuals involved in CORONA: M Fox, A Hüttmann, M Gutierrez-Neri, D Lerner, S Thornton, I Watson, R Wilson Web address: [http://www.shef.ac.uk/gprg](http://www.shef.ac.uk/gprg) Email: d.n.lerner@shef.ac.uk 

University of Tübingen – Wilhemstrasse 5, 72074 Tübingen Germany Individuals involved in CORONA: P Gratwohl, Å Olsson, M Piepenbrink, T Ptak Web address: [http://www.uni-tuebingen.de/zag](http://www.uni-tuebingen.de/zag) Email: gratwohl@uni-tuebingen.de 

Technical University of Denmark – Anker Engelundsvej 1, Building 115, 2800 Lyngby Denmark Individuals involved in CORONA: H-J Albrechtsen, P Bjerg, N Tuxen Web address: [http://www.er.dtu.dk](http://www.er.dtu.dk) Email: plb@er.dtu.dk 

University of Ferrara – Via Savonarola 9, 44100 Ferrara Italy Individuals involved in CORONA: N Colombani, A Gargini, M Mastrocicco, P Spensieri Web address: [http://www.unife.it](http://www.unife.it) Email: gga@unife.it 

Netherlands Institute for Applied Scientific Research – P.B.6060, Schoemarkerstaat 97, 2628 VK Delft Netherlands Individuals involved in CORONA: J Gerritse, N Hoekstra, M Luijten, H Slenders, J Ter Meer Web address: [http://www.tno.nl](http://www.tno.nl) Email: hans.slenders@tno.nl 

Ecole Polytechnique Fédérale de Lausanne – EPFL, Ecublens, 1015 Lausanne Switzerland Individuals involved in CORONA: C Holliger, T Smits, C Dévenoges Web address: [http://lbe.epfl.ch/](http://lbe.epfl.ch/) Email: christof.holliger@epfl.ch 

Charles University Prague – Ovocny trh 5, 116 36 Praha 1 Czech Republic Individuals involved in CORONA: J Cizek, J Datel, J Kubricht, K Nesetril, O Nol, A Sracek, B Topinkova, Z Vencelides Web address: [http://www.natur.cuni.cz/english_version/index.php](http://www.natur.cuni.cz/english_version/index.php) Email: datel@natur.cuni.cz 

Queen’s University Belfast – University Road, BT7 1NN, Belfast United Kingdom Individuals involved in CORONA: G Boshoff, A Downey, B Kalin, G O’Sullivan Web address: [http://www.prb-net.qub.ac.uk/eerg/eerg.htm](http://www.prb-net.qub.ac.uk/eerg/eerg.htm) Email: g.osullivan@qub.ac.uk 

Technical University of Delft – Julianalaan 134, 2628 BL Delft Netherlands Individuals involved in CORONA: B Putters, P Ham, H Prommer, R Schotting Web address: [http://www.tudelft.nl](http://www.tudelft.nl) Email: r.j.schotting@geo.uu.nl 

ESI Ltd. – Priory House, Priory Road, Shrewsbury SY1 1RU – United Kingdom Individuals involved in CORONA: K Green, P Morgan Web address: [http://www.groundwatermodels.com](http://www.groundwatermodels.com) 

Email: philmorgan@esinternational.com 


Lerner D.N., Bjerg P., Datel J., Gargini A., Gratwohl P., Holliger C., Morgan P., Ptak T., Schotting R., Slenders H., Thornton S.F., 2005. CORONA Confidence in forecasting of natural attenuation as a riskbased groundwater remediation strategy, Final report of the EU research project EVK1-2001-00087. University of Sheffield, UK. 25 pages. Available from [http://www.shef.ac.uk/corona.](http://www.shef.ac.uk/corona.) 


