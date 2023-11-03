#### GEOLOGICA ULTRAIECTINA 

 Mededelingen van de Faculteit Geowetenschappen Universiteit Utrecht 

 No. 303 

# Multiphase flow and enhanced 

# biodegradation of dense 

# non-aqueous phase liquids 

### Marian Langevoort 



# Multiphase flow and enhanced 

# biodegradation of dense 

# non-aqueous phase liquids 

# Meerfasenstroming en 

# gestimuleerde biologische 

# afbraak van organische 

# vloeistoffen 

### (met een samenvatting in het Nederlands) 

### PROEFSCHRIFT 

ter verkrijging van de graad van doctor aan de Universiteit Utrecht op gezag van de rector magnificus, prof.dr. J.C. Stoof, ingevolge het besluit van het college voor promoties in het openbaar te verdedigen op vrijdag 20 maart 2009 des middags te 12.45 uur door 

 Marian Langevoort 

 geboren op 19 augustus 1980 te Zwolle 


Dit proefschrift is goedgekeurd door de promotor: 

Prof. dr. ir. S.M. Hassanizadeh 

Samenstelling leescommissie: 

Prof. dr. R.J. Schotting Universiteit Utrecht Prof. dr. ir. A. Leijnse Wageningen Universiteit Prof. dr. P. Van Cappellen Universiteit Utrecht / Georgia Institute of Technology Prof. dr. T.H. Illangasekare Colorado School of Mines Dr. ir. H.H.M. Rijnaarts TNO Bouw en Ondergrond/Deltares 

Dit proefschrift werd (mede) mogelijk gemaakt met financile steun van TRIAS (samenwerking van NWO-ALW, SKB en Delft Cluster). 

Printed by W ̈ohrmann Print Service, Zutphen 

#### ISBN/EAN: 978-90-5744-165-3 


# Table of Contents 

1 Introduction 1 

 1.1 Background............................ 1 1.2 Motivation............................. 3 1.3 Research questions........................ 4 1.4 Thesis outline........................... 5 Bibliography.............................. 5 

2 Review DNAPL source zone biodegradation 7 

 2.1 Introduction............................ 8 2.2 Mathematical description of (D)NAPL biodegradation in groundwater............................... 9 2.2.1 Mass balance equation for components......... 12 2.2.2 Biologically mediated mass exchange terms....... 14 2.2.3 Abiotic mass exchange terms............... 16 2.3 Biodegradation processes..................... 19 2.3.1 Basic concepts...................... 19 2.3.2 Thermodynamic limitations............... 19 2.3.3 Kinetics of inhibition................... 28 2.3.4 Kinetics of competition between processes....... 31 2.3.5 Dechlorination of high concentrations of PCE...... 33 2.4 Enhanced dissolution....................... 36 2.4.1 Introduction........................ 36 2.4.2 Batch experiments.................... 38 


vi TABLE OF CONTENTS 

 2.4.3 Columns Experiments.................. 41 2.4.4 Two-dimensional experiments.............. 44 2.5 Summary and conclusions.................... 48 Bibliography.............................. 50 

3 Batch experiments 61 

 3.1 Introduction............................ 62 3.2 Material and Methods....................... 64 3.2.1 Chemicals......................... 64 3.2.2 Dechlorinating microbial assemblage.......... 64 3.2.3 Batch experiments.................... 65 3.2.4 Analytical methods.................... 66 3.2.5 Reaction rates....................... 68 3.3 Results............................... 69 3.3.1 Characterization of dechlorinating microbial assemblage 69 3.3.2 Degradation rates..................... 69 3.3.3 Degradation kinetics................... 72 3.4 Discussion............................. 72 3.5 Conclusions............................ 77 Bibliography.............................. 78 

4 Uncertainty in parameter estimation batch experiments 83 

 4.1 Introduction............................ 84 4.2 Experimental data......................... 86 4.3 Model development........................ 87 4.3.1 Implementation of sequential PCE dechlorination.... 88 4.3.2 Inverse modelling..................... 95 4.4 Results and discussion...................... 95 4.5 Conclusion............................ 102 Bibliography.............................. 104 Appendices............................... 109 


Table of Contents vii 

5 Column experiments 119 

 5.1 Introduction............................ 120 5.2 Material and methods....................... 122 5.2.1 Chemicals......................... 122 5.2.2 Column set-up and experimental procedure....... 122 5.2.3 Analytical methods.................... 127 5.2.4 Hydraulic parameters determination........... 129 5.3 Numerical model......................... 130 5.3.1 Dissolution mass transfer from residual DNAPL.... 131 5.3.2 Biodegradation...................... 133 5.3.3 Initial and boundary conditions............. 133 5.3.4 Parameter estimation................... 135 5.4 Experimental results....................... 135 5.4.1 Column type 1: vertical column with dissolved PCE.. 135 5.4.2 Column type 2: vertical column with residual PCE... 135 5.4.3 Column type 3: horizontal column with residual and pooled PCE............................ 139 5.4.4 Microbial assemblage analysis.............. 140 5.5 Modelling results......................... 142 5.5.1 Column type 1: vertical column with dissolved PCE concentration......................... 144 5.5.2 Column type 2: vertical column with residual PCE... 147 5.6 Discussion and conclusions.................... 150 Bibliography.............................. 154 

6 Tank experiments 159 

 6.1 Introduction............................ 160 6.2 Material and Methods....................... 162 6.2.1 Chemicals......................... 162 6.2.2 Description of the tank setup............... 163 6.2.3 Packing of the tank.................... 166 6.2.4 System startup...................... 167 


viii TABLE OF CONTENTS 

 6.2.5 PCE injection and biodegradation............ 168 6.2.6 Sampling scheme..................... 168 6.2.7 TDR measurements.................... 169 6.2.8 Head measurements................... 171 6.2.9 Tracer experiments.................... 172 6.2.10 PCE volume at the end of the experiment........ 173 6.2.11 Spatial data analysis................... 173 6.3 Experimental results....................... 176 6.3.1 Head measurements................... 176 6.3.2 Tracer experiments.................... 177 6.3.3 PCE source zone architecture.............. 177 6.3.4 Water content measurements............... 183 6.3.5 Biodegradation process.................. 186 6.3.6 Distribution of PCE and its degradation products.... 190 6.3.7 Mass balance....................... 195 6.4 Numerical study.......................... 199 6.4.1 Model setup........................ 200 6.4.2 Mass transfer from a DNAPL pool............ 202 6.4.3 Numerical results..................... 203 6.4.4 Evaluation of numerical results............. 206 6.5 Discussion and conclusions.................... 207 6.6 Summary and conclusions.................... 209 6.7 Acknowledgements........................ 210 Bibliography.............................. 211 

7 Discussion and conclusions 217 

Summary 221 

Samenvatting 227 

Curriculum Vitae 233 

Acknowledgements 235 


## Chapter 1 

# Introduction 

## 1.1 Background 

A large portion of soil and groundwater contaminations are caused by non-aqueous phase liquids (NAPLs). These NAPLs are immiscible with water and form oily substances that are present as a separate phase. NAPLs can be grouped in two classes, based on their density; light or dense non-aqueous phase liquids, LNAPL or DNAPL, respectively. When spilled on the land surface, NAPL will move down vertically in the unsaturated zone under the influence of gravity. Once it reaches the capillary fringe, where the pores are filled with water, LNAPL and DNAPL behave differently (see Figure 1.1). A LNAPL forms a pool over the water table, whereas a DNAPL penetrates the water table and migrates further down if the amount of accumulated DNAPL is sufficient to overcome the capillary forces. As DNAPLs are immiscible with water, they will flow through the saturated zone as a separate liquid phase. It will continue migrating downward until it reaches a low-permeable layer, where a DNAPL pool can be formed. Due to its high density, the pool can move laterally in the direction of the lowest point of the low-permeable layer, regardless of the direction of groundwater flow. Over the whole trajectory of the migrating NAPL, in the saturated and unsaturated zones, discontinuous blobs of NAPL will get trapped by capillary forces and retained in the subsurface. This immobile mass of NAPL is called residual or entrapped NAPL (see Figure 1.2). The source zone of a contamination is defined as the area where NAPL is present, either as residual or pooled configuration. The area downstream the source zone, where NAPL is dissolved in the water phase, is called the contaminant plume. Typically, aqueous phase NAPL concentrations are lower in the plume than in the source zone. 


2 Chapter 1. Introduction 

Figure 1.1: a) (L)NAPL will flow along low permeability lenses and through high permeability lenses. b) LNAPL entrapment in a coarser sand lens below the water table. c) DNAPL flows below the water level, from Mayer and Hassanizadeh (2005). 

NAPL presence in the subsurface poses environmental health risks and sites contaminated with NAPLs often require remediation. In particular, if the source zone is not removed, a continuous delivery of NAPL to the groundwater can proceed for decades and may threaten our drinking water supplies for a long time (Schwille, 1998). Although most NAPLs have a very low solubility, the dissolved concentration may easily exceed permissible values. Additionally, the seemingly random distribution of NAPL due to the sensitivity of NAPL to soil heterogeneity, and the possibility of DNAPL being present at great depth, make DNAPL contaminations especially difficult to remove. Several techniques, such as excavation, pump and treat, co-solvent and surfactant flushing, thermal methods, and in-situ chemical oxidation have been employed for NAPL cleanup with varying success (McGuire et al., 2006). Site characteristics and economical considerations determine which technique(s) is more suitable in a given situation. Successful application largely depends on dissolution of the NAPL into the water phase. In particular, it is hard to remove immobile residual NAPL without dissolution and/or volatilization. 

One of the most effective and economically feasible methods for NAPL cleanup is in-situ bioremediation. Even at sites where biodegradation is hampered, inhibitory factors can be overcome by the addition of electron donors or nutrients (biostimulation) and/or by the addition of biomass to the subsurface (bioaugmen


1.2. Motivation 3 

Figure 1.2: Illustration of NAPL at residual saturation. On the left side, the unsaturated zone where water forms a film around the soil grains and the NAPL is the intermediate wetting fluid, with gas in the middle of the pores. On the right side, the saturated zone in a water-wet system, from Mayer and Hassanizadeh (2005). 

tation). Early bioremediation activities were directed at contamination plumes. Bioremediation of source zone has not been widely considered because high concentrations of DNAPL are considered to be toxic to bacteria. However, recently, interest is growing more and more in the application of biodegradation to source zones. 

## 1.2 Motivation 

Commercial application of bioremediation is one area where interaction between biodegradation and DNAPL is relevant. Successful field applications of bioremediation of a plume of tetrachloroethylene (PCE) which is a DNAPL have been reported. Commercial companies are interested in the next step: application of bioremediation to source zones. During such a field-scale remediation, biodegradation of DNAPL source zones may influence dissolution and flow properties. Up to now, biodegradation near source zones has not been well studied, although some efforts have been made in this direction. The present research will lead to enhancing our knowledge of bioremediation of DNAPL source zones. To policy makers, insight in the interaction between biodegradation and DNAPL 


4 Chapter 1. Introduction 

flow is of interest. The problem of how to remediate DNAPL source zones has not yet been solved. In the mean time, these source zones persist in our subsurface although it is believed that natural biodegradation occurs around them, even without active remediation or stimulation schemes. Knowledge about the effects of both natural and enhanced biodegradation near source zones is necessary to decide which approach is the best. Recent works have shown that dissolution of residual DNAPL may be enhanced up to sixteen fold due to an increased local concentration gradient as a result of biodegradation (Cope and Hughes, 2001, Yang and McCarty, 2000). This means that biodegradation may reduce the life span of a residual DNAPL from, for example, 300 years to 60 years. It may also have practical implications, as dissolution rate is often assumed to be the limiting factor in treatment of source zones, especially for DNAPLs present in pools. Research on the interaction between biodegradation and DNAPL flow may contribute to modifications in remediation guidelines. From a fundamental point of view, the interaction between biodegradation and DNAPL flow is also of interest. DNAPL flow models are invariably based on experiments with clean, inactive soil. But DNAPL flow in a biologically inactive soil sample may differ from DNAPL flow in a biologically active environment, such as natural soil. It is known that biodegradation significantly influences DNAPL dissolution rate. Biodegradation processes may also significantly influence interfacial tension, perhaps leading to mobilization of entrapped DNAPL. Therefore, biodegradation may influence both water and DNAPL flow processes. Knowledge of this kind of interactions will be of interest to many scientists working on multi-phase flow problems. 

## 1.3 Research questions 

The objective of this research has been to gain better understanding of biodegradation within DNAPL source zones. This led to the following research questions that were addressed: 

- What is the significance of biodegradation of dissolved contaminants in     residual and/or pooled PCE zones? 

- To what extent does biodegradation lead to mobilization of entrapped DNAPL? 

- What are the influences of biodegradation on DNAPL dissolution? 


1.4. Thesis outline 5 

## 1.4 Thesis outline 

This thesis consists of six chapters. Chapter 2 presents a literature review of previous works; in particular, biodegradation in the presence of DNAPL and enhanced dissolution. Governing equations are provided and processes relevant to DNAPL source zone biodegradation are described. Chapters 3 to 6 describe the experiments performed. Chapter 3 shows performed batch experiments aimed at evaluating the potential of the dechlorinating microbial assemblage to dechlorinate PCE over a wide range of dissolved concentrations. Chapter 4 contains a systematic modelling approach of the batch experiments to study the importance of underlining biological processes and sensitivity of model parameters. Chapter 5 describes column experiments performed to investigate whether PCE dechlorination could occur in a system with liquid flow. Next to that, a special setup was designed to investigate the possibility of mobilization of entrapped DNAPL. A biodegradation model was used to determine parameters. Chapter 6 extends this knowledge to perform and model a two-dimensional tank experiment with entrapped and pooled DNAPL. Chapter 7 elaborates on the implications of biological remediation of DNAPL source zones in the field. Finally, there is a summary of the thesis, which addresses the research questions posed in chapter 

1. This is available in both English and Dutch. 

## Bibliography 

Cope, N., and J. B. Hughes (2001), Biologically-enhanced removal of PCE from NAPL source zones, Environmental Science and Technology, 35 , 2014–2021. 

Mayer, A. S., and S. M. Hassanizadeh (2005), Soil and groundwater contamination: nonaqueous phase liquids, American Geophysical Union, Washington, DC. 

McGuire, T. M., J. M. McDade, and C. J. Newell (2006), Performance of DNAPL source depletion technologies at 59 chlorinated solvent-impacted sites, Ground Water Monitoring And Remediation, 26 (1), 73–84. 

Schwille, F. (1998), Dense chlorinated solvents in porous and fractured media. Model experiments, Lewis Publishers, Chelsea, Michigan. 

Yang, Y., and P. L. McCarty (2000), Biologically enhanced dissolution of tetrachloroethene DNAPL, Environmental Science and Technology, 34 , 2979– 2984. 



## Chapter 2 

# A comprehensive review on 

# biodegradation of (D)NAPLs in 

# the vicinity of a source zone. 

## 1 

## Abstract 

Contaminated zones with a dense non-aqueous-phase liquid (DNAPL) typically serve as a long-term source of a groundwater contamination. Microorganisms can degrade DNAPLs in the aqueous phase in the presence of a suitable electron donor often under reduced conditions. Dissolution from the NAPL to the water phase is essential for degradation to occur. Although dissolution and biodegradation of DNAPLs are separately well understood, there are open questions regarding their mutual influence on each other. On one hand, source-zone longevity can be shortened as the biodegradation enhances the dissolution. On the other hand, this enhanced dissolution promotes biodegradation. This paper reviews current perspectives on the dissolution and biodegradation of DNAPL in and around source zones. In particular, the focus is on how these processes are measured, modelled, and, especially, how they interact. The coupling of biodegradation and dissolution has been investigated in modelling studies and laboratory experiments. The conclusion has been that biodegradation enhances dissolution significantly, up to a factor 16. In modelling studies, biodegradation has been expressed in several ways. The complex nature of the microorganisms present at a contami

(^1) This chapter has been prepared for submission as an article as: Langevoort, M. and Hassanizadeh, S.M.; A comprehensive review on biodegradation of (D)NAPLs in the vicinity of a source zone. 


8 Chapter 2. Review DNAPL source zone biodegradation 

nated site demand knowledge of bacterial competition and inhibition. Therefore, different modelling options for biodegradation are reviewed first. In laboratory experiments, difficulties arise when dissolution is measured in the presence and absence of biodegradation to determine the enhancement factor. We believe that this survey will facilitate further studies of the feasibility and effectiveness of biodegradation of DNAPLs near source zones. 

## 2.1 Introduction 

Widespread use of chlorinated solvents in dry cleaning industry and in metal degreasing operations has caused major soil and groundwater pollution. Chlorinated solvents belong to the group of dense non-aqueous phase liquids (DNAPLs). These liquids are immiscible with water and have a higher density. When spilled on the land surface, the DNAPL will move down vertically in the unsaturated zone under the influence of gravity and capillary forces. As DNAPL is immiscible in water, it will flow through the saturated zone as a separate liquid phase. Once it reaches the capillary zone, where the pores are filled with water, the DNAPL has to accumulate before it can displace the water and migrate further. If the amount of accumulated DNAPL is sufficient to overcome the capillary forces, it will continue migrating downward until it reaches a low-permeable layer, where a DNAPL pool can be formed. Due to its high density, the pool can move laterally in the direction of the lowest point of the low-permeable layer, regardless of the direction of groundwater flow. Over the whole trajectory of the migrating DNAPL, in the saturated and unsaturated zone, discontinuous blobs of NAPL are trapped by capillary forces and are retained in the subsurface. This immobile mass of NAPL is called residual NAPL. The source zone of a contamination is defined as the area where DNAPL is present, either in the form of residual or pooled configurations. The large contact area between DNAPL and water, especially in residual configurations, in combination with their low solubility may result in a continuous delivery of DNAPL to the groundwater, and may threaten our drinking water supplies, for a long time (Schwille, 1998). Although most DNAPLs have a very low solubility, the dissolved concentration may easily exceed permissible values. Additionally, the seemingly random distribution of DNAPL, due to the sensitivity of DNAPL to soil heterogeneity, and the possibility of DNAPL present at great depth, make DNAPL contaminations difficult to remove. Classical remediation techniques, such as excavation, pump and treat, and air stripping, have had varying success in effective removal of residual DNAPL 


2.2. Mathematical description of (D)NAPL biodegradation in groundwater 9 

(McGuire et al., 2006). Successful application largely depends on dissolution of the NAPL into the water phase. In particular, the immobile residual NAPL is hard to remove without mobilization or volatilization. Advanced remediation techniques, such as, steam injection, surfactant or co-solvent flushing are used to increase the dissolution of NAPL by increasing its solubility. Furthermore, dissolution rate depends on the difference between the aqueous phase concentration and solubility of the NAPL. So, another option to increase the dissolution rate is by removal of the NAPL in the water phase. This can be achieved by flushing and/or (bio)degradation. For some time, biodegradation is seen as an ideal method to remediate low concentrations of DNAPL in plumes in the form of natural attenuation (Lee et al., 1998). Recently, laboratory studies have shown that also higher concentrations of DNAPL can be degraded (Nielsen and Keasling, 1999, Dennis et al., 2003, Yu and Semprini, 2004). This led to an increased interest in the application of biodegradation near DNAPL source zones (Adamson et al., 2003). This growing interest has, in turn, led to questions about the influence of biodegradation on dissolution of DNAPL. DNAPL dissolution and biodegradation have been intensively studied but as separate processes. There are only a few studies (Seagren et al., 1993, 1994, Clement et al., 2004) that investigated the interplay and the combination of both processes. These focussed on the role of enhanced dissolution caused by biodegradation. Stroo et al. (2003) postulated that to use in-situ bioremediation for source zone treatment, ”we need a better understanding of the interrelated dissolution and degradation processes, as well as the appropriate uses of bioaugmentation”. In this paper, we provide a comprehensive review of the literature on biodegradation in the vicinity of a DNAPL in relation with dissolution. In particular, this study discusses dissolution and biodegradation of PCE. 

## 2.2 Mathematical description of (D)NAPL biodegrada

## tion in groundwater 

Mathematical models of NAPL biodegradation must account for multi-component transport and single-phase flow. Usually the NAPL phase at residual saturation is not moving. Relevant processes one should take into account in the study of biodegradation in a groundwater system are: advection, dispersion, diffusion, dissolution, (bio)degradation, adsorption, and volatilization. These mechanisms contribute to the dilution, immobilization and/or transformation of contaminants. The relative importance of these mechanisms depends on the characteristics of the 


10 Chapter 2. Review DNAPL source zone biodegradation 

compounds (volatility, solubility, see Table 2.1) and rates of relevant processes. These processes are briefly described below. 

 Table 2.1: Properties of PCE, TCE and cDCE from Mercer and Cohen (1990). Molecular Density Viscosity Water Vapor log Henry Surface weight solubility pressure coefficient tension · 103 kg m−^3 cP mg l−^1 mm Hg atm m^3 mol−^1 dyne cm−^1 PCE 165.8 1.63 0.932 200 17.8 2.59· 10 −^2 44.4 TCE 131.4 1.46 0.566 1100 57.9 9.10· 10 −^3 35 cDCE 96.9 1.27 0.444 3500 208 7.58· 10 −^3 30 

Advection Dissolved components are carried along with the flowing groundwater. When only advection is operating, mass added to stream lines will remain in those stream lines, and the direction of mass spreading in steady-state systems is defined by path lines even in relatively complex flow systems. 

Dispersion Dispersion spreads mass beyond the region it normally would occupy due to advection alone. Mechanical dispersion is the mixing caused by local variations in velocity around some mean velocity of flow. With time, mass becomes gradually more dispersed as different fractions of mass are transported in these varying velocity regimes. Variability in the direction and rate of transport is caused by heterogeneities in the porous medium. Heterogeneities exist at a variety of scales ranging from microscopic to megascopic and larger scales. Dispersion in three dimensions involves spreading in longitudinal, and two transversal directions. 

Diffusion Molecular diffusion is mixing caused by random molecular motions due to the thermal kinetic energy of the solute. Because of the distance between the molecules, the diffusion coefficient in gases is much larger than in liquids and is larger in liquids than in solids. The diffusion coefficient in a porous medium is smaller than in pure liquids primarily because collision with pore walls hinders diffusion. In a flowing groundwater, commonly the effect of diffusion is negligible compared to dispersion. 

Dissolution Dissolution is the mass transfer taking place from the NAPL to the aqueous phase. Dissolution from NAPL occurs slowly, creating long-lasting plumes of contamination in the direction of the groundwater movement. All 


2.2. Mathematical description of (D)NAPL biodegradation in groundwater 11 

NAPL components have a maximum concentration in water, which is called the solubility (limit). Solubility is a function of temperature as well as NAPL composition. When the aqueous concentration is zero, the (dissolution) flux from NAPL to water will be relatively high. As the aqueous concentration approaches the solubility limit, the flux will decrease steadily. 

Adsorption Sorption is the overall term for solid-fluid interphase transfer, including absorption, adsorption, and desorption. Absorption is a process in which a gas or liquid diffuses into the solid. Adsorption is a process in which a gas or liquid accumulates at the surface of a solid. 

Volatilization Strictly speaking, volatilization is the process of mass transfer from the NAPL itself to the gas phase. However, frequently the transfer of the NAPL dissolved in the water phase to the gas phase is also included. Components with a relatively high vapor pressure are considered to be volatile components. PCE is rapidly lost through volatilization to the air phase. In the field, DNAPL contaminations can cause problems of high gas concentrations in basements and spaces below houses. Especially when the rooms are badly ventilated, the gas concentrations can become dangerously high. 

Biodegradation Biodegradation can be defined as the process in which an organic molecule is degraded or destructed by microorganisms. Biodegradation is the only process that can potentially transform the components into less toxic ones. Ideally, PCE is completely degraded under anaerobic conditions stepwise (Fig. 2.1) to trichloroethylene (TCE), cis-dichloroethylene (cDCE), vinyl chloride (VC), ethene (ETH) and methane to carbon dioxide and water (McCarty, 1997). This degradation process is called dehalogenation, or more specifically reductive dechlorination, in which a chlorine atom is biologically replaced by a hydrogen atom. 

 Figure 2.1: Degradation pathway of PCE 


12 Chapter 2. Review DNAPL source zone biodegradation 

In this redox reaction, electrons are transferred from the electron donor (H 2 ) to the electron acceptor (PCE or chlorinated daughter products). For this reaction to occur, stronger electron acceptors should be absent, thus, anaerobic conditions are required. Complete reactions for reductive dechlorination of PCE and daughter products are: 

 C 2 Cl 4 + H 2 → C 2 Cl 3 H + HCl C 2 Cl 3 H + H 2 → C 2 Cl 2 H 2 + HCl C 2 Cl 2 H 2 + H 2 → C 2 ClH 3 + HCl C 2 ClH 3 + H 2 → C 2 H 4 + HCl 

Beside the presence of an electron acceptor and donor, nutrients are essential for growth. Other variables that influence growth of bacteria are temperature, pH, acclimation, soil moisture, population density and presence of other bacteria and inhibiting components. All of these components and conditions influence the rate of biomass growth and, thus, biodegradation. 

### 2.2.1 Mass balance equation for components 

In saturated systems with a (D)NAPL, two liquid phases can be distinguished: water and NAPL, for which governing equations for mass transport of all mobile components are written. These equations should be solved simultaneously, because of coupling via the exchange of a component between the two phases. Here, the assumption is made that the system has mobile (ground)water and an immobile DNAPL. This DNAPL can be entrapped in residual or pooled configurations. In a residual zone, some (large) pores may be partially filled with NAPL, with many neighboring pores almost devoid of it. In a pool, which forms on top of low-permeability lenses (in the saturated soil), NAPL has partially filled almost all pores. 

Consider a saturated system with a NAPL as the initial contaminant in residual form. From the processes described above, only volatilization of the NAPL is not relevant, as the considered system does not contain a gas phase. 

The mass balance equation for an aqueous component (dissolved NAPL, electron donor, and nutrients) can be written by the advection, diffusion, reaction equation 2.1. The reactions are dissolution, adsorption, degradation, and produc


2.2. Mathematical description of (D)NAPL biodegradation in groundwater 13 

tion. 

 ∂nS wCwi ∂t 

 + ∇ · (qwCwi) − ∇ · (nS wD · ∇Cwi) = ri diss − ri ads − 

 ∑^ Nx 

 j= 1 

 ri j deg + ri prod (2.1) 

where n [-] is porosity, S w^ [-] is water saturation, Cwi^ [M/L^3 ] is water phase concentration of component i, qw^ [L/T] is water phase Darcy velocity vector, D [M/L^2 T] is the diffusion-dispersion tensor, r dissi [M/L^3 T] is the rate of dissolution of NAPL component i into the water, ri ads [M/L^3 T] is the adsorption rate of com

ponent i, ri j deg [M/L^3 T] is the degradation of component i by bacterial consortium 

j, and ri prod [M/L^3 T] is the production of component i due to the degradation of the mother product. The total number of bacterial consortia is denoted by Nx. Production of component i is related to the degradation of component i − 1 , expressed as: 

 ri prod = + 

 ∑^ Nx 

 j= 1 

 ri deg−^1 , j (2.2) 

The mass exchange rate for components in the NAPL phase is assumed to be only influenced by dissolution. NAPL components can go from the NAPL to the water phase. The amount of biodegradation and adsorption taking place directly from the NAPL phase is negligible. The mass balance equation for the components in the NAPL phase can be written as follows: 

 ∂nS nCni ∂t 

 = −ri diss (2.3) 

where S n^ [-] is NAPL saturation, and Cni^ [M/L^3 ] is NAPL phase concentration of component i. Mass balances equations of water and NAPL are coupled through the mass exchange terms. 

Although we consider a single phase flow system, the saturation of NAPL and water can change due to dissolution. This change in saturation has an effect on the flow field. The saturation change can be expressed as a change in relative permeability (Mualem or Burdine model) which scales the hydraulic conductivity. 

In order to account for competition between bacteria, a number of microbial consortia are taken into account, indicated by index j. A consortium is a group of microorganisms that interact with each other in complex ways. We assume that the bacteria that completely degrade the DNAPL are members of one con


14 Chapter 2. Review DNAPL source zone biodegradation 

sortium. Microorganisms that use the electron donor for another process, such as methanogenesis, are considered to be members of another consortium. In this way, competition between bacteria for the electron donor can be modelled. The concentration of different bacterial consortia in the water phase can change by growth and natural decay. The concentration of a bacterial consortium can grow due to the degradation of several components i in the water phase. Therefore a summation should be made over all components that can be degraded by 

the bacterial consortium j. A stoichiometric factor, Y (^) j, should be included, as not all degraded moles of components are incorporated into biomass. The mass balance equation for a bacterial consortium is given by: ∂X j ∂t = −r (^) decayj + ∑^ Nw i= 1 Y jr degi j (2.4) where X j^ [M/L^3 ] is biomass concentration of bacterial consortium j, r (^) decayj [M/L^3 T] is the decay rate of bacterial consortium j, and Y j^ [-] the fraction of electron donor electrons converted to biomass electrons during synthesis of new biomass. The total number of aqueous phase components (other than pure water), i, is denoted by Nw. 

### 2.2.2 Biologically mediated mass exchange terms 

Rates of biodegradation reactions, for example r (^) decayj and ri j deg, can be a function of all factors that affect activities of microorganisms. The biodegradation rates can be determined at various scales, ranging from laboratory batch experiments to the field scale. The dependence of biodegradation rate on the concentration of reactants is reflected in the order of the reaction. If a reaction is of zeroth order, the rate is not dependent on the concentration of the reactant in solution (i.e. rdeg = k). If increases in the reactant concentration can result in a proportionate increase in the reaction rate, then the rate is first order (i.e. rdeg = kC). A general example of a first-order reaction is isotopic decay of radio-active elements. Higher-order reactions are also possible: rdeg = kC^2 or rdeg = kC^1 C^2. The elementary model for biodegradation is based on first-order kinetics. When biodegradation is taking place under ideal growth conditions, the degradation rate is proportional to the component concentration. This first-order rate expression is: ri j deg = ki jCwi^ (2.5) where ki j^ is the first-order rate constant of consortium j, that may degrade dif


2.2. Mathematical description of (D)NAPL biodegradation in groundwater 15 

ferent components at different rates. This formula assumes that there are no limitations, for example with respect to electron donor, acceptor or pH. However, laboratory degradation experiments show that the reaction rate is not always continuously increasing with the reactant concentration. At higher reactant concentrations, the reaction rate will start to level off, caused by a deficiency in required components. Is is even possible that the reaction rate will decrease caused by, for example, the presence of a toxic component. Most laboratory studies use the Monod kinetic formula to describe DNAPL degradation kinetics. 

The Michaelis-Menten formula was originally developed by Michaelis and Menten for enzyme kinetics in the beginning of the 20th^ century (Michaelis and Menten, 1913). Later, the French microbiologist Jacques Monod used this expression to describe bacterial growth rates (Monod, 1949). For bacterial growth, the equation is actually an empirical relation, but since it has the same form as the Michaelis-Menten enzyme kinetics equation, one can think of Monod kinetics as describing a chain of enzymatically mediated reactions with a limiting step. The main difference between Monod and Michaelis-Menten kinetics is that the process is catalyzed by a single enzyme in Michaelis-Menten kinetics, whereas Monod kinetics describes processes in which many enzymes could be involved. Strictly speaking, it is not correct to describe the kinetics of growthlinked biodegradation as Michaelis-Menten kinetics (Kov ́arov ́a-Kovar and Egli, 1998). However, this subtle difference is often ignored and both names are frequently used interchangeably. 

The classical form of the Monod kinetic formula models the degradation rate as a function of the concentration of a rate limiting substrate, Cwi, and the maxi

mum specific growth rate, μ (^) maxj. r degi j = μ (^) maxj Cwi Kis + Cwi^ 

#### (2.6) 

This equation shows that the degradation rate is also influenced by the halfsaturation constant, Kis, which represents the substrate affinity constant. In Michaelis-Menten kinetics, the half-saturation constant is noted as Kmi and represents affinity of the degrading enzyme for the substrate. A high value for the halfsaturation constant means that the enzyme binds only weakly to the substrate; a low value means a strong binding. Furthermore, in both kinetic expressions, a low half-saturation constant leads to a high degradation rate compared to higher half-saturation constants. As both names of kinetic expressions are used interchangeably, also the half-saturation constant is expressed with Ks or Km without notice of the different biological meaning. 


16 Chapter 2. Review DNAPL source zone biodegradation 

The Monod kinetic formula is neither zero nor first order, but is an intermediate between the two cases. At low substrate concentrations, (Cwi^ much smaller than the half-saturation constant, Kis) the formula reduces to a first-order reaction: 

 ri j deg = 

μ (^) maxj Ksi Cwi^ (2.7) At high substrate concentration, (Cwi^ much larger than the half-saturation constant, Kis) the reaction becomes zeroth order: ri j deg = μ (^) maxj (2.8) In equation 2.6, only component i, for example, the electron acceptor, is assumed to be essential for the reaction to occur. If there are other components limiting the degradation rate, by their absence or presence, the right-hand side of the equation can be modified slightly. These modifications are explained in more detail in section 2.3.3. Decay of bacteria Commonly, microorganisms can become inactive, for example because of cell aging. The natural decay of microorganisms can be expressed by a first-order reaction: r (^) decayj = k (^) decayj (X j^ − X (^) bgj) (2.9) where k (^) decayj [1/T] is the decay constant and X (^) bgj is the natural background concentration of bacteria present in the soil. 

### 2.2.3 Abiotic mass exchange terms 

Dissolution Dissolution occurs across the NAPL-water interface. At the pore scale, one can almost always assume local equilibrium; i.e. the dissolved concentration in the water side of the interface is uniquely related to the concentration of the corresponding component in the NAPL side of the interface (Khachikian and Harmon, 2000). This relationship is commonly prescribed by Raoult’s Law, which states: 

 csi^ = ̃χni^ swipure (2.10) 

where csi^ is the solubility concentration, established at the interface just inside the water phase, cwipure is the solubility limit of component i if it was present as 


2.2. Mathematical description of (D)NAPL biodegradation in groundwater 17 

a pure phase, and ̃χni^ is the mole fraction of component i at the interface just inside the NAPL. Away from the interface, dissolved components concentrations will be less than solubility. Thus at the larger scale, where processes based on average concentrations are described, the equilibrium assumption is not valid anymore. This depends on whether or not dissolution is sufficiently fast, relative to groundwater flow rates, to achieve equilibrium with that flow. If averaged concentration of dissolved components is less than the corresponding solubility limit, dissolution must be described by a kinetic relationship, which supports the non-equilibrium assumption. Nevertheless, under certain conditions, the local equilibrium assumption may be also employed at the Representative Elementary Volume (REV) scale (see e.g. Powers et al. (1991), Miller et al. (1990)). In particular, if dissolution rate is fast, flow rate is small, NAPL saturation is high and biodegradation is absent or slow, one may expect the solubility limit to be reached in the water within the zone where residual NAPL is present. In such cases, for a single-component NAPL, the dissolved concentration will be equal to the solubility limit and will remain constant in the residual NAPL zone, until all NAPL is dissolved (or limiting low saturations are reached). For a multi-component NAPL, however, the NAPL composition (i.e. mole fractions of the components) will change with time, because the solubilities of the various components are different. As a result, the dissolved concentrations of components change with time according to Raoult’s Law: Csi^ = χniCwipure (2.11) 

where Csi^ is the solubility concentration, χni is the mole fraction of component i present in the NAPL, and Cwipure is solubility of component i if it was present as a pure phase. In this case, governing Equation 2.1 and 2.3 must be added and Equation 2.11 should be used to replace Csi^ with χni, which can be related to Cni. 

In many situation, in column experiments and under field conditions, local equilibrium assumption does not hold. This is often the case when the flow velocity is high compared to the dissolution rate (Powers et al., 1992). In nonequilibrium modelling of NAPL dissolution, a kinetic formula is used, where the driving force is the difference between the aqueous phase concentration and the solubility limit, Csi, calculated with Raoult’s Law (Equation 2.11). 

 ri diss = kian(Csi^ − Cwi) (2.12) 

where ki^ is average mass transfer coefficient for the total specific interfacial area between DNAPL and groundwater for an REV, an. In the absence of detailed estimates of interfacial area, studies have employed a lumped mass transfer coef


18 Chapter 2. Review DNAPL source zone biodegradation 

ficient, κi^ [1/T], to yield: ri diss = κi(Csi^ − Cwi) (2.13) 

which is a quasi steady-state form of Fick’s linear dissolution model. Advantage is that the NAPL geometry is not needed, but as the NAPL-water interfacial area will decrease over time, the lumped dissolution rate coefficient is not a parameter that is easily measured or calculated. Determination of the coefficient is usually done through dimensionless numbers. Empirical relationships have been developed for specific experimental geometries and flow systems. A review by Khachikian and Harmon (2000) provides expressions of the Sherwood number in terms of the Schmidt, Peclet, and Reynolds numbers. A commonly used expression is given by Miller et al. (1990), which relates the Sherwood number, S h, to Reynolds number and NAPL saturation: 

 S hi^ = 

 κid^2 Dim 

 = βi 0 Reβ 

 i 1 (S n)β 

 i 2 (2.14) 

where d is the mean soil particle diameter, Dm is the molecular diffusion coefficient, Re(= vρ μd ) is the Reynolds number, and β’s are constants. Values for β’s are obtained from experiments (see e.g., Mayer and Miller, 1996, Powers et al., 1992). Other DNAPL-aqueous-phase mass transfer correlations are obtained by Powers et al. (1992, 1994), Imhoff et al. (1997) and Saba and Illangasekare (2000). 

Adsorption Many NAPL contaminants partition strongly to the solid phase, for example PCE adsorbes to solid organic matter in the aquifer (Drever, 1997). The relevance of taking into account NAPL adsorption is dependent on the system. In the presence of large amounts of (residual) NAPL, the amount adsorbed to soil particles is often insignificant. However, in field remediation, adsorbed NAPL can deliver to the groundwater when NAPL concentrations in the water become lower. Because water is usually the wetting phase in the subsurface, the soil grains are covered with a layer of water. Therefore, adsorption onto the solid phase occurs primarily from the aqueous phase, rather than from the NAPL. 

Adsorption of aqueous phase components other than NAPL constituents can be important when nutrient concentrations are limiting biodegradation. For example, nutrient adsorption can control the nutrient concentration in the subsurface. If nutrients necessary for biodegradation become unavailable to microorganisms in the water phase, degradation rates can decrease. 

 For adsorption, the same approaches as for dissolution are available: local 


2.3. Biodegradation processes 19 

equilibrium and non-equilibrium. Commonly, adsorption is modelled as an equilibrium process with linear, Freundlich, or Langmuir isotherms. So, in cases that adsorption can not be neglected, considerations should be made to include one of the (non)equilibrium relations. 

## 2.3 Biodegradation processes 

### 2.3.1 Basic concepts 

Biodegradation of PCE can occur via a metabolic or co-metabolic process. In this first process energy is gained by the degradation of the contaminant itself, whereas in a co-metabolic process energy is gained from the transformation of another component. Dehalorespirers are able to gain energy from the electron transfer to (i.e. the reduction of) the chlorinated hydrocarbons. The only known microorganisms that is able to completely dechlorinate PCE is Dehalococcoides ethenogenes, in which the dechlorination step from VC to ethene is co-metabolic (Maym ́o-Gatell et al., 1995). Beside dehalorespirers, there are other groups of anaerobic microorganisms that can dechlorinate PCE, usually partly to cDCE: fermentative bacteria, sulfate-reducing bacteria, homoacetogenic, and methanogenic bacteria (Cabirol et al., 1998b). A detailed description and characterization of dechlorinating microorganisms is beyond the scope of this review and can be found elsewhere (L ̈offler et al., 2003, Holliger et al., 2003, 1999). In anaerobic degradation, PCE acts as an electron acceptor (i.e. it is reduced) and therefore, electron donors are needed. Most suitable electron donors are hydrogen and organic substrates such as benzoate, lactate, acetate, propionate, butyrate, ethanol, methanol, molasses, glucose, formate, and yeast extract. Several authors have concluded that hydrogen is the most important electron donor for several known dechlorinating species (Fennell et al., 1997, DiStefano et al., 1992, Smatlak et al., 1996, Carr and Hughes, 1998). The organic substrates mentioned above can serve as a precursor for hydrogen formation via fermentation. 

### 2.3.2 Thermodynamic limitations 

For reductive dechlorination, beside the presence of microorganisms capable of dechlorination, also the redox conditions should be ideal. Which redox reaction occurs, or stated differently, which electron acceptor is used, depends on the amount of energy that microorganisms can extract from a reaction. In biochemistry, the conventional indicator for determining this is the oxidation-reduction 


20 Chapter 2. Review DNAPL source zone biodegradation 

potential or the redox potential. Redox potential expresses the tendency of a substance to accept or donate electrons. The more negative the redox potential of a substance, the greater the tendency of the substance to donate electrons (and be oxidized). Similarly, the more positive the potential, the greater the tendency to accept electrons (and be reduced). The difference in redox potential between the electron donor and acceptor is equal to the energy yield from the reaction. The greater the difference, the higher the amount of energy released. 

In thermodynamics, the energy yield of a reaction can be determined with the change in Gibbs free energy, ∆G◦ r , which is given by 

 ∆G◦ r = 

#### ∑ 

 G◦ f (products)− 

#### ∑ 

 G◦ f( reactants) (2.15) 

where 

#### ∑ 

G◦ f (kJ/mol) is the standard free energy of formation of products or reactants at standard state (Stumm and Morgan, 1996). Gibbs free energy changes are related to the change in redox potential, E◦ H (V): 

#### ∆E◦ H = 

 −∆G◦ r nF 

#### (2.16) 

where n (mol) is the number of electrons transferred in the reaction and F is the Faraday constant (96.485 kJ/V). The larger the change in redox potential, the greater the tendency of the reaction to occur. This change gives insight into the amount of energy that is available for a certain reaction, or how far from equilibrium that reaction is. 

Microorganisms preferentially catalyze those reactions that give them the highest energy yield. Herewith, an estimate can be made which reactions can occur in the presence of certain redox conditions and electron acceptors. The dechlorination process is a reductive process with a ∆G◦^ between -180 to -130 kJ mol−^1 per chloride removed (Dolfing, 2003). This yields a redox potential which is comparable to denitrification, which is higher that for sulphate reduction and methanogenesis. This suggests that dechlorination will not occur under aerobic conditions, but rather under anaerobic conditions (Holliger et al., 1999). 

Another way to determine which redox reaction may occur is through examining the H 2 threshold concentration. Each hydrogenotrophic process (i.e. a biological process that uses hydrogen such as acetogenesis and methanogenesis) has a different H 2 threshold concentration, which is the concentration required for the hydrogenotroph to become active. Below the H 2 threshold concentration, the free energies of the respective reactions cease to be negative. The H 2 threshold is inversely correlated with changes in Gibbs free energy and the electrochemi


2.3. Biodegradation processes 21 

cal potential of the H 2 -consuming reaction (equation 2.16). Therefore, processes with more energy release have lower H 2 threshold concentrations. According to this concept, the order of occurrence of processes in uncontaminated systems, from the least to most favorable electron acceptor, is the order of decrease in H 2 threshold concentration: acetogenesis, methanogenesis, sulfate reduction, iron(III) reduction, manganese reduction, denitrification, and aerobic respiration. This sequence can also be seen in table 2.2, which contains a summary of H 2 threshold concentrations for different processes, including dechlorination. Based on these observations, it follows that chlorinated compounds are thermodynamically favored as electron acceptors under acetogenic, methanogenic, and sulfate reducing conditions. As the H 2 threshold concentration of dechlorination is close to denitrification, preferential use of chlorinated components as electron acceptor under nitrate reducing conditions is less probable. 

Yang and McCarty (1998) proved that the level of the hydrogen threshold concentration for dechlorination and methanogenesis is independent of the electron donor and the fermentation pathway. This was also confirmed by Kassenga et al. (2004) who found that the H 2 threshold concentration was not dependent on the kinetics of the degradation. They stated that the steady-state H 2 concentration will be reached faster in the case of a higher rate of degradation, but the final hydrogen concentration is not influenced. However, the type of electron donor can have an influence on the levels of H 2 in the subsurface. Fermentation of electron donor can cause H 2 concentrations to vary by orders of magnitude, depending on the thermodynamics of the particular fermentation reaction. Because dechlorination has a lower H 2 threshold concentration than methanogenesis, dechlorinators can grow (and dechlorinate chlorinated hydrocarbons) at lower hydrogen concentrations than methanogens can. This suggests that by controlling hydrogen concentration in sites contaminated with chlorinated ethenes, biological dechlorination can be optimized (Smatlak et al., 1996, Ballapragada et al., 1997). Theoretically, it would be most favorable to have a long-term delivery of hydrogen at low concentrations. Several investigations have been conducted to determine the most suitable electron donor to optimize dechlorination using its competitive advantage at low H 2 concentrations. Smatlak et al. (1996) suggested that the success of butyric acid as an electron donor can be explained by a slow release of H 2. 

Fennell et al. (1997) studied four different electron donors to address the potential for selective enhancement of dechlorination above methanogenesis through H 2 delivery. They chose four substrates: ethanol and lactic acid, that are readily fermented under relatively high H 2 levels; and butyric and propionic acids, that 


22 Chapter 2. Review DNAPL source zone biodegradation 

Table 2.2: Hydrogen threshold concentration for different processes; the order is from the most to the least favorable. 

 Electron accepting process H 2 threshold concentration References (nM) Aerobic respiration <0.1 Bossert et al. (2003) Denitrification <0.1 Bossert et al. (2003) <0.05 L ̈offler et al. (1999), Lovley and Goodwin (1988) 0.04 ± 0.03 Luijten et al. (2004) 0.06 ± 0.03 Dechlorination PCE 0.21 ± 0.16 L ̈offler et al. (1999) 0.16 ± 0.07 <0.5 Mazur and Jones (2001) TCE < 0.5 Mazur and Jones (2001) 0.7 ± 0.3 Hoelen and Reinhard (2004) cDCE 0.24 ± 0.07 L ̈offler et al. (1999) 0.34 ± 0.25 0.21 ± 0.08 2.2 ± 0.9 Yang and McCarty (1998) 2.5 ± 0.09 Kassenga et al. (2004) 0.82 Mazur et al. (2003) 1.6 ± 0.2 Hoelen and Reinhard (2004) VC 0.20 ± 0.05 L ̈offler et al. (1999) 0.19 ± 0.13 0.21 ± 0.11 2.2 ± 0.9 Yang and McCarty (1998) 1.6 ± 0.2 Hoelen and Reinhard (2004) Ammonification 0.015 – 0.025 L ̈offler et al. (1999) Manganese reduction <0.05 Luijten et al. (2004), Lovley and Goodwin (1988) Iron (III) reduction 0.2 – 0.6 Bossert et al. (2003) 0.1 – 0.8 L ̈offler et al. (1999) 0.2 Lovley and Goodwin (1988) Sulfate reduction 1 – 4 Bossert et al. (2003) 1 – 15 L ̈offler et al. (1999) 1.76 ± 0.15 Luijten et al. (2004) 1 – 1.5 Lovley and Goodwin (1988) 0.8 Mazur et al. (2003) 2.5 ± 0.3 Hoelen and Reinhard (2004) Methanogenesis 5 – 95 L ̈offler et al. (1999) 5 – 100 Luijten et al. (2004) 7 – 10 Lovley and Goodwin (1988) 11.5 ± 1.6 Yang and McCarty (1998) 10.9 ± 3.3 9.8 Mazur and Jones (2001) Acetogenesis 336 – 3640 L ̈offler et al. (1999) > 350 Luijten et al. (2004) 


2.3. Biodegradation processes 23 

are fermented only under low H 2 levels. Batch experiments with a mixed culture were amended every other day with PCE and one of the four donors. Additionally, shorter batch experiments were carried out to investigate the culture performance. Both experiments were performed with different ratios of PCE to electron donor. A priori, they expected that the cultures fed with lactic acid or ethanol, which are fermented more rapidly and produce higher levels of H 2 , would eventually fail as methanogens would predominate the culture and marginalize dechlorinators. This expectation was only partly realized. In the short-term experiments, expectations were observed, as here no yeast extract was added that can serve as a electron donor that is releasing H 2 slowly. The slowly fermented, low-H 2 -producing substrates (butyric and propionic acids) did support dechlorinators while minimizing, and in the case of propionic acid essentially excluding, methanogenic competition. The long-term batches with different electron donors showed no differences in dechlorination. They attributed this to the fact that yeast extract was added in these experiments that released H 2 slowly. Another possible explantation is that the fermentation pathways of the electron donors used were not directly to H 2. For example, lactic acid can produce propionic acid, thereby transforming from a rapidly degrading, high-H 2 -producing substrate into a slowly degrading, low-H 2 -producing substrate. 

The complexity of investigating microbial competition among dechlorinators and H 2 -utilizing organisms was also encountered by Carr and Hughes (1998). In batches and column experiments, fed with PCE and either lactate, methanol, or H 2 , they did not observe dechlorination and methanogenesis inhibiting each other; they occurred simultaneously. In a comment on this article, Fennell and Gossett (1999) stated this to be a consequence of the ratio of concentration of electron donor to PCE. Low concentrations of PCE and high concentrations of electron donor cause no competition between microorganisms. Any donor added will produce enough H 2 to sustain not only methanogenesis, but also dechlorination and possibly acetogenesis. Carr and Hughes (1999) responded that the observed ratio of electron donor to PCE was not constant throughout their study. Due to the excess of H 2 in the experiments, the rates of all competing processes were at maximum and competition effects were to be observed. Dechlorination rate increased throughout the experiment, although dechlorinators were able to operate for shorter time than methanogens, as PCE was not continuously present. 

In a similar study, Yang and McCarty (1998) tested the difference in dechlorination due to the use of propionate and benzoate. The fermentation of propionate is thermodynamically regulated and is causing a slow release of hydrogen. Fermentation of benzoate is very fast and causes high concentrations of hydrogen. 


24 Chapter 2. Review DNAPL source zone biodegradation 

Dechlorination in the presence of propionate yielded three times more ethene than benzoate fed microcosms, while the amount of methane formed was three times less. Benzoate-fed bottles produced hydrogen levels far above the hydrogen threshold for methanogenesis, causing methanogens to use a lot of hydrogen. In contrast, the propionate bottles were having hydrogen concentrations below the hydrogen threshold for methanogenesis, causing more dechlorination to occur. 

Another important electron donor that can play an important role in the competition between dechlorinators and methanogens is biomass. This was nicely shown by Lee et al. (2004). They tested three electron donor substrates: (i) glucose, (ii) soluble glucose fermentation products (SGFP), and (iii) biomass from glucose fermentation on PCE and cDCE dechlorination. The culture originated from aquifer material from a PCE-contaminated site. When biomass was added as electron donor substrate, both simulated and experimental PCE dechlorination were much slower than with glucose or SGFP because of the slower production of H 2 from cell decay. Also here, lower H 2 concentrations are maintained, thus reducing the competition for hydrogen by methanogens and a more complete PCE dechlorination. In batches with cDCE and glucose or SGFP, methane was produced, because H 2 concentrations were above the threshold concentration for methanogens. This was only observed in batches with cDCE because PCE dechlorination is a stronger competitor for H 2 than cDCE dechlorination. Lee et al. (2004) concluded from their model that the initial distribution of biomass can have a large impact on the extent of dechlorination. When omitting the biomass decay in the model, simulations gave a very poor fit to the experimental data, indicating decay of biomass from glucose can play a significant role in the dechlorination achieved with this substrate. Periodic addition of glucose for dechlorination of cDCE yielded more efficient dechlorination and less methane production. Dechlorination of cDCE was complete within 130 days when the interval between periodic glucose addition was 10 days. Intervals shorter than 10 days caused less dechlorination and produced more methane. Dechlorination of PCE was not enhanced by periodic additions, as competition for H 2 yielded effectively more reducing equivalents for dechlorination with two different dechlorinating groups acting than if acetogens and methanogens were also involved. 

An extension of the H 2 threshold concept has been developed by Fennell and Gossett (1998). Their model accounted for thermodynamic as well as kinetic limitations of the reactions. Processes included were dechlorination, fermentation of the substrate, competition with methanogens through the use of hydrogen and acetate, and the growth of all involved microbial populations. The electron donor fermentation was described using Michaelis-Menten kinetics, with the inclusion 


2.3. Biodegradation processes 25 

of the thermodynamic influence of the product formation (acetate and H 2 ) on the rate of fermentation. 

 dMdonor dt = −kmaxdonor Xdonor 

 (Cdonor^ − Cdonor∗) Kdonor m + Cdonor^ 

#### (2.17) 

where Mdonor^ is the total amount of donor (μmol) and kdonormax is the maximum specific rate coefficient of donor degradation (in μmol per mg of VSS per hour, VSS is volatile suspended solids). Xdonor^ is the donor-fermenting biomass in the bottle (mg of VSS), K mdonor is the half-saturation coefficient for the donor (μM), Cdonor^ is the donor concentration (μM), Cdonor∗^ is the hypothetical donor concentration that, under the instantaneous culture conditions, would result in ∆Grxn = ∆Gcritical, given the concentrations of all the other reactants and products at that instant, i.e. the threshold concentration. It is related to ∆Gcritical, which refers to some marginally negative free energy that the organisms must have available to live and grow. 

 ∆Gcritical = ∆G◦^ + RT ln( [products] Cdonor∗[other reactants] ) 

#### (2.18) 

∆Grxn is the free energy available from the substrate fermentation at that point in time: 

 ∆Grxn = ∆G◦^ + RT ln( 

 [products] Cdonor[other reactants] ) 

#### (2.19) 

In equation 2.17, the only difference between kmax and μmax (e.g. in equation 2.6) is the dimension; kmax is in Mdonor/MXdonor t, whereas μmax is in Mdonor/ V MX donor t. Equation 2.17 is rewritten into measurable quantities by use of a thermodynamic function, Φ. Rewriting Cdonor^ − Cdonor∗^ (Fennell and Gossett, 1998): 

 Cdonor^ − Cdonor∗^ = Cdonor 

#### [ 

 1 − exp 

#### ( 

 ∆Grxn − ∆Gcritical RT 

#### )] 

 = CdonorΦ 

 where, Φ = 1 − exp 

#### ( 

 ∆Grxn − ∆Gcritical RT 

#### ) 

#### (2.20) 

where R is the universal gas constant (8.314 J/K mol) and T is the temperature (K). ∆Gcritical is a constant for each donor fermentation reaction, whereas ∆Grxn must be calculated for every time step with use of the concentrations of the components. The value of Φ is between 0 and 1 and is a measure of how far the reaction is from thermodynamic equilibrium. If the fermentation is far from equilibrium, the donor concentration is high relative to the concentrations of the 


26 Chapter 2. Review DNAPL source zone biodegradation 

products of the reaction, the driving force is high, approaching 1. The fermentation reaction is then limited by the kinetics. If the fermentation reaction is close to equilibrium, the driving force is low, approaching 0. The fermentation reaction is limited primarily by thermodynamics. The thermodynamic function Φ is used as a correction on the concentration of substrates and products in MichaelisMenten-like kinetics. 

The model with Michaelis-Menten-type kinetics, H 2 thresholds for dechlorinators and methanogens, and thermodynamic limitations on donor fermentation were successfully used to describe experimental data (Fennell et al., 1997), with a mixed anaerobic culture in which methanogens and dechlorinators competed for H 2. Incorporations of threshold concentrations for H 2 used by dechlorinators and methanogens reflects experimentally-observed reality. However, precise knowledge of the specific threshold values is not critical; knowing the relative values among competing microbial groups is sufficient. In fact, since these differences also have a thermodynamic basis, there is reason to suggest that these relative differences may have universal application (Fennell and Gossett, 1998). 

Lee et al. (2004) used a similar approach to study dechlorination including fermentation and competition for H 2. Their model accounted for four cultures, i.e. fermentators, methanogens, and two dechlorinating groups: one for PCE transformation to cDCE and one for cDCE degradation to ethene. In the fermentation reactions, glucose was used as starting component, which was transformed to butyrate, acetate or ethanol. Subsequently, butyrate and ethanol could be transformed to H 2 , which was the only electron donor that the dechlorinating microorganisms could utilize in the model. Michaelis-Menten kinetics including H 2 threshold concentrations was used to model the degradation of the chlorinated ethenes. For the above described fermentation reactions, Monod kinetics were assumed. For the production of H 2 from butyrate and ethanol, thermodynamic limitations were considered by including H 2 threshold concentration. Biomass was considered to be a source of H 2. From the biomass, 30% was taken to be converted into H 2 , and the remainder into acetate. For biomass decay, it was assumed that 80% of the total organic mass was biodegradable, following first order kinetics. The model was calibrated with experimental data from batch experiments performed with PCE and cDCE. The simulated results described the experimental behavior reasonably well (see Figure 2.2). 

The H 2 concentration may be a valuable tool to determine the actual redox conditions in the subsurface (Lovley et al., 1994, Ballapragada et al., 1997, Smatlak et al., 1996, Mazur and Jones, 2001). Even the presence of dechlorinators could be determined by the hydrogen threshold concentrations (L ̈offler et al., 


2.3. Biodegradation processes 27 

Figure 2.2: Comparisons between simulated and experimental results for reductive dechlorination of PCE: (a) blank, (b) glucose, (c) SGFP and (d) biomass from Lee et al. (2004). 


28 Chapter 2. Review DNAPL source zone biodegradation 

1999). Although L ̈offler et al. (1999) stated that ”H 2 threshold data cannot predict the extent of reductive dechlorination”, Luijten et al. (2004) stated that the measured hydrogen concentration in situ can be an indicator of the extent of anaerobic reductive dechlorination. They found that lower hydrogen concentrations in wells were accompanied by partial dechlorination of PCE, whereas at relatively higher hydrogen concentrations complete degradation was observed. They concluded that low H 2 concentration is enough to reduce PCE and TCE, whereas (slightly) higher hydrogen concentration is required for the degradation of cDCE to VC and further. However, recently, Brown et al. (2005) placed question marks on the use of H 2 concentration as a measure of redox conditions, and consequently as a measure of dechlorination. They investigated the impact of acetate and H 2 on the kinetics of each other during iron reduction and concluded that both the presence of a carbon source and electron donor limitation affect steady state hydrogen levels but that for low carbon concentrations hydrogen levels remain rather stable. As this balance, especially in field situations, is a complicated function of the rate-limited availability of these compounds, it is unlikely that H 2 levels observed in the field can be predicted based on kinetic coefficients measured under ideal growth conditions in laboratory settings. While hydrogen concentrations in laboratory studies may serve as an indication for redox conditions, its utility in this regard in the field in limited. 

### 2.3.3 Kinetics of inhibition 

Above-mentioned values for the H 2 threshold concentration were all determined experimentally. However, these values can also be calculated from thermodynamics of reaction. Dolfing (2003) calculated that at hydrogen concentrations as low as roughly 10−^26 nM, dechlorination of chlorinated ethenes may occur. In practice, this is unrealistic, because microorganisms cannot metabolize at meaningful rates at such low H 2 concentrations. This suggests that dechlorination is not only controlled thermodynamically, but it is also under kinetic control. A short introduction to various kinetic equations for describing degradation is provided in section 2.2.2. Commonly, first-order kinetics is used to simulate NAPL dechlorination in field studies (Seagren et al., 1993, Carr et al., 2000, Clement et al., 2004). A more sophisticated kinetic description is needed when dechlorination rate is not only a function of the chlorinated ethene concentration but also depend on degradation products, electron donor, or nutrient concentrations. These extended models have a large(r) number of unknown parameters, which are not easy to determine, especially not in field situations. Then, usually investigators choose to 


2.3. Biodegradation processes 29 

model the NAPL dechlorination with first-order kinetics, which represents practical situations reasonably well (Clement et al., 2000). However, more and more researchers use the Monod equation to model NAPL dechlorination. In a few studies (Nielsen and Keasling, 1999, Haston and McCarty, 1999) the dechlorination rate has been assumed to depend on PCE only, following equation 2.6, whereas other researchers, however, have included inhibition terms to account for electron donor limitations or toxicity (Fennell and Gossett, 1998, Lee et al., 2004, Christ and Abriola, 2007). Based on Michaelis-Menten enzyme kinetics, several inhibition types are possible. Hereunder, we describe competitive inhibition, non-competitive inhibition, self-inhibition, multi-component limitation, and toxicity. 

First, consider competitive inhibition, which has an effect on the half-saturation constant, Km. An inhibitor binds the sites of the enzyme that are used for biodegradation. As a result, the substrate can not bind the specific enzyme as the inhibitor is sitting on that position. This causes the apparent affinity of the substrate to the binding site to be decreased, while the maximum degradation rate is unchanged. Competitive inhibition can also be called specific inhibition because the inhibitors essentially decrease the availability of specific enzyme sites (Cornish-Bowden, 1995). The half-saturation constant changes and is expressed as an effective halfsaturation constant, Keff m , in the following way: 

 Keff m = Km(1 + 

#### CI 

#### KI 

#### ) (2.21) 

where CI [M/L^3 ] is the concentration of the inhibitor and KI [M/L^3 ] is its inhibition constant. An example is co-metabolic degradation of TCE by methanotrophs, which gain energy for growth from methane. The oxidation of methane to methanol is catalyzed by an enzyme called methane mono-oxygenase (MMO). In the presence of TCE, MMO enzyme interacts differently converting methane to an epoxide. Methane oxidation and TCE degradation processes are both slowed down (Rittmann and McCarty, 2001). 

A special case of competitive inhibition is product inhibition. This is often used in modelling PCE biodegradation, where an equation similar to 2.21 is mostly used (Yu and Semprini, 2004, Cupples et al., 2004a,b, Yu et al., 2005, Chu et al., 2004, Lee et al., 2004). Differences among these studies occur in the way that components are responsible for the inhibiting effect. For example, Yu et al. (2005) showed that PCE had an inhibitory effect on the degradation of lighter chlorinated solvents. But, they stated that the lighter chlorinated components had a very weak effect on the degradation of the more chlorinated components and 


30 Chapter 2. Review DNAPL source zone biodegradation 

therefore they did not include this effect in their model. Also, Cupples et al. (2004b) found that VC was less inhibitory for cDCE and TCE dechlorination. However, DiStefano et al. (1991) found in batch experiments that PCE dechlorination was inhibited at VC levels of 30-60 μmol (nominal concentration). It must be noted that these observations are difficult to compare, as they use different microbial cultures which have a significant effect on PCE dechlorination. 

Another type of inhibition is non-competitive inhibition, which has an effect on the maximum growth rate as in equation 2.22, but no effect on the halfsaturation constant. This means that an inhibitor interferes with the catalytic properties of the enzyme but the affinity for the substrate remains unchanged. In practice, non-competitive inhibition is not considered to be important, because it is very unlikely that two molecules with quite different properties had equal binding constants for the inhibitor (Cornish-Bowden, 1995). 

 μeffmax = μmax 1 + C KII 

#### (2.22) 

Of course, it may also happen that both competitive and non-competitive inhibition act together, called uncompetitive inhibition or mixed inhibition, which was for example used by Chu et al. (2004). 

Another type of inhibition for chlorinated ethenes is substrate or self-inhibition. In this case, the degradation process is slowed down by the high concentration of the component (e.g. PCE) itself. It is not clear whether the self-inhibition occurs directly through affecting the degrading enzyme or indirectly through hindering electrons or energy flow after the original donor reaction (Rittmann and McCarty, 2001). Frequently, this kind of inhibition is modelled with Haldane or Andrews kinetics, that shows a gradual decline in the degradation rate as substrate concentration increases. Effective maximum growth rate is similar to equation 2.22 and the effective half-saturation constant following: 

 Ke f fm = Km 

1 + (^) KCI 

#### (2.23) 

Nevertheless, other models are available (Carrera et al., 2004). Among these, the model proposed by Luong (1987), representing a terminal inhibition concentration Cmax after which degradation ceases. The Michaelis-Menten expression 

is then multiplied by: (^) ( 1 − 

#### C 

 Cmax 

 )n (2.24) 


2.3. Biodegradation processes 31 

Another extension to the basic Michaelis-Menten equation relates to multicomponent limitation. Equation 2.6 considers only one essential component for the biodegradation process to occur. This could be, e.g. under anaerobic conditions, the electron acceptor. When there are other components negatively influencing the degradation rate, the right-hand side of the equation has to be modified through multiplication by an additional term. An example of multi-component limitation is when in addition to the electron acceptor, an electron donor controls the kinetics. This can be modelled as follows: 

ri j deg = μ (^) maxj X j^ Cwi Kmi + Cwi CwED KmED + CwED^ 

#### (2.25) 

where ED stands for electron donor. Obviously, in environments with an excess amount of a component (e.g. if CwED^  KmED ), the term corresponding to this component will approach unity and is not needed to be included. Finally, the rates of degradation and microbial growth can be also slowed down by the presence toxic factors. Examples of such inhibitors are chemicals such as heavy metals or pesticides. One example of an inhibitor of TCE inhibition is the chemical acetylene. This can be produced in the course of abiotic treatment of a chlorinated-ethenes-contaminated plume using zero-valent iron. Pon et al. (2003) showed that TCE and VC degradation stopped in presence of acetylene. Difficulties occur in translating the parameters obtained in controlled laboratory experiments to field situations. A thorough discussion of this important issue in found in Kov ́arov ́a-Kovar and Egli (1998). They raised the question: ”how these kinetic concepts can be applied to the environmental situation where a mixed microbial population is most probably utilizing several substrates”. 

### 2.3.4 Kinetics of competition between processes 

These kinetic equations can be applied to result in competition for hydrogen between dechlorination and methanogenesis as was proposed by the thermodynamic approach. Limitation of H 2 as electron donor can be taken into account through an additional term in Michaelis-Menten kinetic description, as was proposed in equation 4.2. Smatlak et al. (1996) determined the corresponding half-saturation constant, KH m 2 , for methanogenesis and dechlorination in batch experiments with PCE. They reported a 10-fold smaller half-saturation coefficient (100 ± 50 nM) for hydrogen use by dechlorinators than for hydrogenotrophic methanogens (960 ± 180 nM) in their mixed culture. This means that with low levels of H 2 , the dechlorination potential is maximized while methanogenesis is 


32 Chapter 2. Review DNAPL source zone biodegradation 

minimized. The half-saturation coefficient for hydrogen used in dechlorination was also determined by Ballapragada et al. (1997). In a mixed methanogenic dechlorinating culture the KH s 2 for dechlorination was in the range of 12 to 28 nM. The half-saturation coefficient for H 2 is lower for dechlorination than for methanogenesis, i.e. the affinity of dechlorinators for H 2 is higher than methanogens have for H 2. Ballapragada et al. (1997) and Smatlak et al. (1996) suggested that this higher affinity for H 2 for dechlorination may be generally true for hydrogenotrophic dechlorinators. Beside half-saturation coefficients for H 2 Ballapragada et al. (1997) also determined H 2 partial pressures. Below 100 ppm H 2 partial pressure, dechlorinators can compete successfully with methanogens, because at these H 2 concentrations the specific growth rate of dechlorinators is higher than methanogens. Above 100 ppm H 2 , methanogens will outcompete dechlorinators. However, the H 2 partial pressure cannot always be used to evaluate whether dechlorination occurs in a certain system. In many dechlorinating systems only a part of the electrons will be consumed by dechlorinating organisms (Dolfing, 2003). 

Beside thermodynamic preference of dechlorination above methanogenesis, DiStefano et al. (1991) stated that high concentrations of PCE (0.3 mM) are also inhibitory for methanogens. In their batch experiment, PCE concentration was increased, which eventually led to halting methane production. They suggested that methanogenesis was inhibited by the high concentrations of PCE and/or its dechlorination products. This was in accordance with batch experiments performed by Nielsen and Keasling (1999), with concentrations up to solubility of PCE and TCE. High PCE concentrations were shown to inhibit methanogenesis also in experiments by Smatlak et al. (1996) (120 μM) and Fennell et al. (1997) (330 μM). 

Yang and McCarty (2000) studied competition between dechlorinators, methanogens and acetogens. In the absence of PCE, methane production was complete within 5 days, and only a small amount of acetate was formed. In the presence of 0.1 mM PCE, only about 6 μmol of methane was produced during the first five days when PCE was present. Following PCE disappearance, methane quickly rose to 76 μmol, whereas no acetate was formed. With a PCE concentration of 0.3 mM, no significant methane or acetate production was observed before the disappearance of PCE. However, as soon as PCE disappeared, acetate was quickly produced and only a small amount of methane was produced. This suggests that concentrations of PCE, even as low as 0.1 mM, can inhibit methanogenesis and homoacetogenesis. Homoacetogens appear to have been inhibited somewhat less than methanogens by PCE. Since high concentrations of PCE diminished the ac


2.3. Biodegradation processes 33 

tivity of methanogens and homoacetogens, the substrate utilization efficiency for dechlorination is higher. However, active methanogenesis or homoacetogenesis occurred after PCE disappeared, and thus insufficient hydrogen was available for complete dechlorination to ethene. Contradicting results were obtained in column experiments. Yang and McCarty (2002), Cabirol et al. (1998a) and Isalou et al. (1998) observed that methanogenesis was always active even at high concentrations of PCE. This is in contrast to previous findings in batch experiments, where high concentration of PCE and its transformation products were found to be inhibitory to methanogenesis. Cabirol et al. (1998a) thought that the diversity of the microbial consortia might have caused this absence of inhibition. However, more probably the different experimental setup, column versus batch experiment, could explain the observed differences. Isalou et al. (1998) suggested that biofilms created microenvironments in their column experiments that were not exposed to high concentrations of PCE. It was hypothesized that the heterogeneity of aquifer material in the columns and difference in spatial distribution of different organisms and substrates might play an important role in the reduced toxicity observed. Although the effluent PCE concentration was near saturation, the PCE concentration in some pores in the column was likely to be well below saturation. 

### 2.3.5 Dechlorination of high concentrations of PCE 

If dechlorinating bacteria can compete with other hydrogenotrophic organisms, the question is raised what the capability of microorganisms is to dechlorinate high PCE concentrations. It is not easy to give a conclusive answer to this question. Several experiments in different setups and with different bacterial cultures are performed to determine the level of PCE that could be dechlorinated. DiStefano et al. (1991) tested the ability of a methanol-PCE methanogenic culture to dechlorinate about 0.3 mM PCE in a batch experiment. Bottles contained 100 ml medium and dechlorinating culture. Every two days, PCE was added and the headspace in the bottles was flushed to remove volatile, possible toxic, components such as VC and ethene. At first, PCE was added from a water stock solution saturated with PCE. As the PCE concentration increased, the use of an aqueous stock solution required a prohibitively large volume of solution because of low PCE solubility. So, instead the PCE was dissolved in methanol. PCE was dechlorinated to 80% ethene and 20% VC within two days at 35°C. With four days of incubation, less than 1% VC remained, indicating PCE dechlorination was almost complete. Tandoi et al. (1994) used a similar methodology, but only added PCE in neat form. Dechlorination from PCE to VC was rapid 


34 Chapter 2. Review DNAPL source zone biodegradation 

with near zero-order kinetics, but VC dechlorination was inhibited by PCE. 

Nielsen and Keasling (1999) investigated the impact of saturated PCE and TCE concentrations on dechlorination. In 160 ml serum bottles, 50 ml medium solution and 50 ml chlorinated ethene dechlorinators, from a TCE-contaminated field, were added with 0.05 and 0.175 ml PCE or 0.025 and 0.25 ml TCE. They observed that PCE and TCE were rapidly converted to ethene with little accumulation of VC. In a separate experiment, the VC and ethene production rates were measured over a range of TCE concentrations. With increasing TCE concentration, the VC production rate decreased, the ethene production rate increased, and methane production decreased. 

Yang and McCarty (2000) supplied a dechlorinating culture in a reactor with a continuous feed of 0.98 mM PCE. Batch experiments were performed in 120-mL serum bottles, to which 60 mL of a dechlorinating culture was added and pentanol was used as electron donor. Different amounts of pure PCE were added to create a set of initial aqueous concentrations of 0.26, 1.06, 2.11, and 4.22 mM. Concentrations higher than the PCE solubility (0.9 mM) contained the excess PCE as a separate phase. Within four months, complete dechlorination to ethene was obtained with the two lower PCE concentrations of 0.26 and 1.06 mM. The PCE concentrations as high as 4.22 mM were dechlorinated to cDCE within 80 days. 

Yu et al. (2005) and Yu and Semprini (2004) carried out batch experiments to determine maximum rates and half-saturation coefficients for each step of the dechlorination of PCE to ethene for two different mixed cultures and evaluated inhibition between chlorinated ethenes. The cultures were grown in batch reactors with 0.6 mM PCE or TCE. Serum bottles were filled with 125 ml liquid culture and leaving approximately 30 ml anaerobic gas headspace. PCE concentrations ranged from 39 μM up to the solubility limit with a nominal aqueous phase concentration of 1.128 mM. They observed PCE degradation without a lag phase to cDCE. PCE did not inhibit cDCE transformation. This likely resulted from different microorganisms in the culture or different enzyme systems being responsible for PCE and cDCE and VC transformation. Ethene production started after most of the cDCE was transformed to VC, indicating cDCE strongly inhibited VC dechlorination to ethene. 

Kaplan et al. (2008) investigated the ability of the KB-1 microbial consortium in the presence of neat PCE. They added 20 ml PCE to serum bottles with the microbial suspension and methanol. Dechlorination was initially slow, but after a lag time of two weeks, transformation of PCE began. VC and ethene were produced, though only after depletion of the PCE. 


2.3. Biodegradation processes 35 

Carr and Hughes (1998) demonstrated degradation of PCE at a concentration of approximately 0.5 mM in a column study. The glass column was packed with anaerobic granular sludge and had no history of PCE contamination. The columns were amended with nutrient medium and PCE/methanol mixture. Influent concentrations were incrementally increased to 0.48 mM. Effluent PCE and TCE concentrations were below detectable limits. The analysis of the gas trapped in the water showed that cDCE and VC were the major end products being formed. 

Isalou et al. (1998) showed degradation of 0.72 mM PCE in a 2-m long column to VC and ethene, without the detection of cDCE, within the residence time of approximately 17 hours. The experiment was performed on coarse silica sand and with a mixed culture originating from an anaerobic digester at a treatment plant. The PCE dissolved in methanol was mixed with supporting basal medium before the injection to the column at the bottom. To achieve biodegradation of VC, half-way the column, additional electron donor was added. Dennis et al. (2003) investigated the microbial consortium used by Isalou et al. (1998) via a phylogenetic study. The column was cut into two 1-m sections, each containing seven sampling ports. Neat PCE was injected in amounts of 0.5 to 3.0 ml through a port at the first half of one column, every 46 weeks. Dechlorination of PCE took place in the second meter of the column to ethene. With the concentration gradients of the chlorinated ethenes, variations in community structure were observed in the column. Some members of the microbial community were able to withstand high levels of PCE near the source zone. 

Cirpka et al. (1999) performed an experiment in a large container (10100 x 700 x 200 mm) filled with a fine sand matrix with coarse sand lenses. The goal was to establish a potentially active dechlorinating biomass in regions with low actual activity of dechlorination, i.e. bioaugmentation of a system. Electron donor (ethanol) was introduced into the container inlet and water with PCE at solubility concentration was continuously injected into a well. Inoculation was done with Dehalospirillum multivorans and an enriched mixed culture. Inoculation failed due to acidification of the system. Then, the system was buffered by the continuous injection of sodium sulfide and reinoculated with Dehalospirillum multivorans and Desulfovibrio desulfuricans. Reductive dechlorination was incomplete and TCE and mainly cDCE were formed over the course of the experiment. However, soil sample analysis showed that the bacteria needed for complete dechlorination were present in the aquifer, although not at high densities. 

 A similar investigation to initiate reductive dechlorination was performed by 


36 Chapter 2. Review DNAPL source zone biodegradation 

Adamson et al. (2003). A metal tank (5490 x 2130 x 1830 mm) open to the atmosphere was filled with silty sand originating from a quarry. Through three sample ports, 0.33 l PCE was injected in each port. Initially the flow of water, consisting of a mix of surface water and groundwater, was carried out in recycling mode, yielding a residence time of 9 days. An activated carbon filter was installed in the effluent to remove any chlorinated ethene before reintroduction into the tank. In the following 50 days, the system was made anaerobic and provided with electron donor (acetate and lactate). Inoculation occurred with a dechlorinating, methanogenic mixed culture, after which a long-term source of hydrogen (electron donor) was added. Dechlorination started around day 64, but it levelled off as the system became too acidic, due to the fermentation of organic acids. In order to revive dechlorination, the system was changed to a flow-through mode on day 93. Shortly thereafter, the PCE concentrations in effluent samples started to decrease and TCE, cDCE, VC, and ethene concentrations increased. To explain that biodegradation occurs in source zones, various researchers suggested that in soil pores micro-environments could exist in which organisms are exposed to lower concentrations of DNAPL (Dennis et al., 2003, Isalou et al., 1998). This could be an explanation for the capability of some members of the microbial community to withstand very high levels of PCE near the source zone in above-mentioned column and tank experiments. Next to that, dechlorination of PCE and TCE source zones was also observed in the field (Hood et al., 2008, Wymore et al., 2006, Payne et al., 2006, Lebr ́on et al., 2007). Dechlorination close to PCE or TCE phase in source zones is likely to influence the mass transfer from the DNAPL to the aqueous phase, which is discussed next. 

## 2.4 Enhanced dissolution 

### 2.4.1 Introduction 

Dissolution is the only mass transfer mechanism that makes DNAPL available to microorganisms for biodegradation in the aqueous phase. If dechlorination occurs in the vicinity of the DNAPL, the mass transfer of components from DNAPL to the aqueous phase can be enhanced. This is called biologically-enhanced or bioenhanced dissolution. It is clear that bioenhanced dissolution can only be investigated in NAPL source zones in the presence of the non-aqueous phase. In a few field experiments on biodegradation of DNAPL source zones indications for bioenhanced dissolution have been reported (Hood et al., 2008, Wymore et al., 2006, Payne et al., 2006, Lebr ́on et al., 2007). 


2.4. Enhanced dissolution 37 

There are various mechanisms that contribute to dissolution enhancement. The mass transfer between DNAPL and water is controlled by one dependent variable, namely the aqueous phase concentration, Cwi, and two parameters, the dissolution rate constant, κ, and the solubility limit, Csi^ (see Equation 2.13). Thus, enhanced dissolution may occur if: i) dissolution rate constant, κ, is increased, ii) maximum solubility, Csi, is increased, and/or iii) the aqueous phase concentration, Cwi, is kept low. 

Technologies that increase the solubility limit, Csi, (e.g. hot water flooding, steam injection, (bio)surfactant / co-solvent flushing) or decrease the aqueous phase concentration (e.g. advective flushing, oxidation, and/or (bio)degradation ) will increase the dissolution driving force and enhance the overall mass flux. Solubility is a function of properties of NAPL and water phases as well as temperature, and it is tabulated in the literature for a large number of NAPLs (see e.g., Davis, 1997, Knauss et al., 2000). Dissolution of NAPL into the aqueous phase may be improved by elevated temperature. An example is hot water flooding, which is used as a mobilization technique for soils with high NAPL saturations and for improvement of oil recovery in petroleum industry. Also high temperatures cause an increase in mass transfer rate coefficient, as well as increase in the aqueous phase solubility. An increase in the mass transfer rate may also be caused by surfactants (Bai et al., 1997, Clifford et al., 2007). A surfactant contains a hydrophobic tail and a hydrophilic head. Spherical structures will form with the DNAPL in the middle surrounded by the hydrophobic tails, this is called micellar partitioning. Not only mass transfer will be enhanced by surfactants, but also mobilization of DNAPLs can occur. Harwell et al. (1999) showed mobilization of residual PCE with a food grade surfactant in a column filled with glass beads. The aqueous-phase solubility of DNAPLs can also be increased by some electron donors. For example, Hood et al. (2007) showed that salts of carboxylic acids (e.g. sodium lactate) decreased the solubility of TCE while other donors (lactic acid, acetic acid, and ethanol) increased TCE solubility by up to fourfold at ethanol concentrations of 25 wt%. 

It is often difficult to determine which mechanism is more responsible for the enhancement. Imhoff et al. (1997) compared results from PCE dissolution experiments with existing dimensionless correlations for NAPL dissolution in porous media. They found that flushing with hot water had a small effect on the solubility limit of PCE, but increased the mass transfer rate coefficient by a factor of approximately two as the aqueous phase temperature was increased from 5 to 40 °C. 

 As mentioned above, processes that decrease the concentration of the NAPL 


38 Chapter 2. Review DNAPL source zone biodegradation 

in the aqueous phase, such as flushing and (bio)degradation, cause an enhancement of the driving force, namely the difference between the actual aqueous phase concentration and the solubility of the NAPL. This results in faster dissolution of the NAPL. In bioenhanced dissolution, the reduction in aqueous phase concentration is caused by bacterial activity. This can occur when a microbial culture grows in the DNAPL source zone, as the parent contaminants are rapidly degraded after they dissolve into groundwater. In the case of PCE dechlorination, the daughter products are more soluble than PCE, which allows more moles of contaminants to be present in the aqueous phase when dechlorination is occurring as compared to abiotic dissolution alone. While laboratory studies have been able to quantify DNAPL mass transfer enhancements due to the individual mechanisms described above, observations from the field are more likely to represent the combined effects of all of these mechanisms. Detailed knowledge on bioenhanced dissolution is obtained from batch, column, and two-dimensional experiments, which are discussed below. Quantifying the enhancement is usually done by comparing a reference case to an alternative case. This can involve a change in process parameters but also inclusion of processes such as advection and biodegradation. For example, an experimental setup involving PCE dissolution without biodegradation can be compared with a similar setup with biodegradation. There are three ways how bioenhanced dissolution can be quantified. First, the total dissolved NAPL concentration can be compared to the total dissolved NAPL concentration plus its degradation products in the case of biodegradation. Taking into account the stoichiometry of the degradation reaction, an enhancement factor can be calculated. This can be a valuable measure if the NAPL source results in concentration at solubility. However, dissolution of NAPL is not constant in time and if the NAPL dissolution yields lower aqueous phase concentrations, the bioenhanced dissolution factor can be too low. A better approach is to measure the total mass of neat NAPL over a certain period in a biotic and abiotic case. The third way is to compare for both cases the total mass that left the system at a given time. 

### 2.4.2 Batch experiments 

Experiments have been done in order to investigate enhanced dissolution of DNAPLs by biological activity, among them batch experiments. In batch experiments, usually there is no soil medium. Also, the system is well mixed; thus microorganisms cannot create micro-environments with lower DNAPL concentrations. This means that the bacteria should be able to either cope with high DNAPL concentrations, or dechlorinate faster than the dissolution rate to prevent inhibitory 


2.4. Enhanced dissolution 39 

concentrations to occur. In the first case, dissolution could occur, whereas in the second case non-equilibrium dissolution must occur. 

Carr et al. (2000) conducted experiments in continuous-flow stirred tank reactors containing a model NAPL consisting of PCE and tridecane. Dissolution in reactors containing a PCE-dechlorinating enrichment culture was compared to abiotic experiments with dissolution alone. For the biotic reactors, the aqueous phase contained a solution with nutrients and formate as electron donor, whereas in abiotic reactors a solution containing CaCl 2 was used. The aqueous phase was continuously replaced with new solution, resulting in a hydraulic retention time of three days. The model NAPL was also added every 72 hours to the reactors. Aqueous PCE concentrations in the abiotic reactors demonstrated that equilibrium dissolution was maintained throughout the experiment and no mass transfer limitations were present. Decreases in PCE concentrations in the abiotic reactors occurred as the mole fraction of PCE in the NAPL decreased. In the biotic reactors, aqueous PCE concentrations decreased at a faster rate than observed in the abiotic ones and cDCE became the major end product. At the end of the experiment, the total mass of PCE removed from biotic reactors was 0.59 mmol out of 1.18 mmol, whereas in the abiotic reactor, it was 0.20 mmol out of 1.16 mmol. This leads to an enhancement factor of about three. 

Adamson et al. (2004) did biotic and abiotic batch experiments to investigate flux in NAPL-contaminated systems. Both biotic and abiotic reactors consisted of 38 ml glass bottles with a glass test tube placed inside with their open end facing up. In the test tube, 0.15 mmol PCE was present in different mole fractions in tridecane. Outside the test tube, in the glass bottles, abiotic reactors contained 14 ml of reduced deionized water whereas biotic reactors contained 3 ml of a reduced anaerobic medium and 11 ml of a dechlorinating, methanogenic mixed culture. The NAPL in the test tube had no contact with the liquid in the reactor as the opening of each test tube was located well above the water level. PCE volatilized into the headspace of the bottle and then partitioned into the aqueous phase. Samples from reactor’s headspace were taken regularly and analyzed for chlorinated ethenes. From these measurements, they calculated the total mass of PCE that had left the test tube. The flux of PCE from the NAPL for biotic systems, was based on the total mass that partitioned out of the NAPL. With the determined tridecane-water partition coefficients, masses of all chlorinated ethenes in water and tridecane phase were determined. Samples from the biotic reactor collected in the first 1 and 2 hour following inoculation indicated that flux was at least 2.1 to 2.5 times greater than that of comparable abiotic systems. The flux of mass from NAPL to gas and liquid phases differed less than 20% among 


40 Chapter 2. Review DNAPL source zone biodegradation 

biotic systems with different PCE mole fractions, whereas in abiotic systems, the flux of PCE was dependent on the initial mole fraction. This could be only explained if the difference between aqueous and solubility limit had been the same for all biotic systems regardless of the initial mole fraction. The organisms appear to be capable of lowering the aqueous-phase concentration to a level at which this concentration difference was relatively constant. Amos et al. (2007) investigated dechlorination of dissolved PCE by four pure cultures: Desulfuromonas michiganensis strain BB1, S. multivorans, Geobacter lovleyi strain SZ, and Desulfitobacterium sp. strain Viet1. Serum bottles (160 ml), that were shaken, were filled with 100 ml liquid containing the microorganisms, a reduced anaerobic medium of mineral salts and acetate and pyruvate. Aqueous phase concentrations of 0.3, 0.6, 0.8, 1 and 1.2 mM were tested. All pure cultures tested were unable to dechlorinate when the aqueous PCE concentration exceeded 0.54 mM. The dechlorinating performance of three of these pure cultures were also tested in the presence of neat PCE under non-equilibrium conditions. A single PCE droplet was formed in the bottles that were shaken. Stain BB1 and strain SZ dechlorinated PCE until inhibitory PCE concentration of 0.54 mM was reached in the aqueous phase. S. multivorans could keep the aqueous PCE concentration below inhibitory levels and dechlorinated the whole PCE droplet to cDCE. This also occurred in experiment where the agitation speed was increased, which increased the dissolution rate. To quantify the relationship between the rate of dissolution and the rate of biotransformation, the bioavailability number, Bn, is proposed by Bosma et al. (1997), which is the ratio of the mass transfer coefficient to the microbial affinity: 

 Bni^ = κi μimax/Kim 

#### (2.26) 

Amos et al. (2007) determined that a bioavailability number between 1· 10 −^2 and 2 · 10 −^2 indicate that dechlorinating microorganisms are incapable of dechlorination at high or saturated PCE concentrations, and can continuously dechlorinate in the presence of a DNAPL. This would mean that the biotransformation rate is adequately faster than the dissolution rate to prevent inhibitory concentrations. In summary, in all batch experiments where biodegradation in the presence of NAPL phase did occur, a decrease in aqueous phase NAPL concentration was reported. This means there was an increase in the difference between the NAPL solubility and aqueous phase concentration, and therefore enhancing dissolution occurred. Enhanced dissolution by dechlorination yielded bioenhanced dissolution factors varying between 1 to 14. Difference in these enhancement factors are 


2.4. Enhanced dissolution 41 

probably caused by difference in experimental setups. In particular, the ability of the microorganisms to withstand high DNAPL concentrations and the capacity to dechlorinate at high rates determine the bioenhanced dissolution factors. 

### 2.4.3 Columns Experiments 

Column experiments are more representative than batch experiments as they contain a porous medium, either soil or glass beads, within which spatial concentration gradients can develop. Also an important processes, namely advection is present. This process can result in lowering the aqueous phase concentration by flushing. The effect of flow velocity on bioenhanced dissolution was investigated numerically by Seagren et al. (1993). They presented a model for a simple NAPL contamination scenario in order to investigate theoretically when flushing and biodegradation can significantly accelerate NAPL dissolution. The domain consisted of a semi-infinite column with a saturated, homogeneous, isotropic medium and one-dimensional flow. The NAPL was a single component and present as residual saturation of immobile blobs uniformly distributed throughout the column. The transport of dissolved NAPL components was described by the advection-dispersion-reaction equation with steady flow. Dissolution was modelled following equation 2.13. Biodegradation was modelled as a first-order process. They obtained an analytical solution for this simplified situation. They found that for typical flow velocities, biodegradation may have a significant effect on the enhancement of the dissolution rate as it decreases the concentration in the aqueous phase. The relative share of advection and biodegradation in dissolution enhancement depends on the flow velocity. If the velocity is low, advection cannot decrease the concentration around a NAPL blob too far below solubility but biodegradation can; in this case, the share of biodegradation in enhanced dissolution will be significant. But if velocity is high, the concentration around a NAPL blob will be kept low, and biodegradation can not make a significant effect anymore. Yang and McCarty (2000) performed a column study to investigate if dechlorination from PCE DNAPL could occur. The column (25 mm inner diameter, 220 mm in length) was filled with aquifer material for the lower 70 % and with a dechlorinating culture for the remaining upper 30% (i.e. so, no porous medium). This culture was maintained in a reactor initially seeded with aquifer material from a PCE-contaminated site. The aquifer material in the column came from an uncontaminated site. While filling the column, PCE was added to the aquifer material to reach a saturation of about 2% as uniformly as possible. The column was continuously fed, with upward flow, with a sterile basal medium solution 


42 Chapter 2. Review DNAPL source zone biodegradation 

containing pentanol as electron donor. The effluent concentrations of PCE and its degradation products were measured as a function of time. After 130 days of operation, the total concentration of the chlorinated ethenes and ethene in the effluent was about 4.5 mM. This represents about five times their maximum PCE aqueous solubility. This suggests dechlorination resulted in a significantly enhanced PCE dissolution rate. 

A lower enhancement dissolution factor was found by Yang and McCarty (2002) in a later column study. Four columns (25 mm inner diameter, 300 mm in length) were filled with aquifer material and amended with PCE to about 2% saturation of the pore space. The columns were bio-augmented by pumping two pore volumes of anaerobic PCE dechlorinating culture through the columns. Flow was upwards in all experiments. Then, a sterile basal medium solution containing nutrients and different electron donors was continuously fed with a syringe pump to yield a residence time of about 14 days. Column 1 contained no electron donor, to serve as a control for monitoring PCE dissolution alone; column 2 contained pentanol (a soluble substrate); column 3 contained sodium oleate and calcium chloride (a slow hydrogen releasing substrate); and column 4 contained mixed PCE and olive oil (substrate and PCE were well mixed). Results showed that after an adaptation period, the total concentration of PCE and its degradation products significantly exceeded PCE solubility. The increase was by a factor 2.1 in column 2 before day 150 and 2.5 after that. Solubility was exceeded by a factor of 3 in both columns 3 and 4. This is lower that the enhancement factor of five they reported earlier (Yang and McCarty, 2000). This may have been caused by the absence of aquifer material in a part of the column in the previous study and differences in flow rate. 

Christ and Abriola (2007) developed a mathematical model to simulate the column experiments of Yang and McCarty (2002). The model accounted for dissolution and reductive dechlorination of PCE using Monod kinetics including hydrogen thresholds and competitive inhibition. Four bacterial groups and eight species were included to model competition between populations for electron donor. The aqueous phase relative permeability could change by bio-clogging. Experimental results were simulated quite well. However, after approximately 120 days, the simulated cDCE concentrations stayed constant whereas measured cDCE concentrations had declined. Christ and Abriola (2007) hypothesized that a clogging mechanism (methane production or biomass growth) was not properly incorporated in their model. 

Christ and Abriola (2007) used their model to simulate dissolution of DNAPL ganglia. They compared their model results with the theoretical dissolution en


2.4. Enhanced dissolution 43 

hancement predictions of Seagren et al. (1993) described above. The solutions by Seagren et al. (1993) were rewritten to quantify the dissolution enhancement factor as the ratio of the biotic and abiotic dissolution fluxes. Seagren et al. (1993) analytical solution was for a steady-state system with spatially uniform rates of dissolution and dechlorination. In contrast, the model by Christ and Abriola (2007) was capable of simulating spatially non-uniform, non-linear dechlorination kinetics in a transient system. The effect of maximum PCE degradation rate, DNAPL saturation, DNAPL source zone length, and DNAPL source zone configuration on enhanced dissolution was investigated. In the simplified analytical model, dechlorination rate limitations were neglected, whereas in the numerical model, dechlorination was constrained by limitations on biomass growth and insufficient electron donor. Therefore, for systems that were rate-limiting, the simplified model over-estimated bioenhanced dissolution. This effect is also seen in comparing different DNAPL zone lengths. As the source-zone length increases, dechlorination rate limitation can occur. The numerical model also indicated that sustained bioenhanced dissolution factors are not likely. As the source zone length decreases due to DNAPL dissolution, the enhancement factor becomes constrained as a result of dissolution rate limitations. 

Cope and Hughes (2001) performed experiments in a glass column (25 mm inner diameter, 250 mm in length) packed with 0.5-0.75 mm glass beads. Residence time was adjusted to be three days. A mixture of tridecane and 14 C-labelled PCE was introduced into the column followed by deionized water flushing, resulting in a residual NAPL over the whole column. Microbial inoculation was done with a mixed culture of dechlorinating and methanogenic bacteria. Continuous upward flow of water was maintained, with additional nutrients and electron donor (pyruvate) added. The effluent concentrations of PCE and its degradation products were measured over time. Three biotic columns were run, with different electron donor concentrations. The cumulative flux of chlorinated ethenes leaving the columns with low and intermediate electron donor concentrations was far greater than PCE dissolution under abiotic conditions, with enhancement factors of 6.5 (with a maximum of 16) and 5.0, respectively. But, the column with the highest electron donor concentration showed only slightly larger cumulative removal of chlorinated ethenes than by dissolution alone (enhancement factors of 1.3). They suggested that washout removed essentially the entire dechlorinating population from this column. 

Amos et al. (2008) performed column experiments to assess the spatial distribution and activity of a PCE dechlorinator within source zones and the associated plume areas. Sand columns contained a 10-cm long source zone, a 10


44 Chapter 2. Review DNAPL source zone biodegradation 

cm long transition zone directly down-gradient of the source zone, and a 40-cm long plume region down-gradient the transition zone. The source zone consisted of either a mixed NAPL of PCE in hexadecane or pure PCE. The column with neat PCE showed very low dechlorination ([cDCE] < 0.01 mM) and no microbial growth, whereas in the column with mixed NAPL, microbial growth was associated with dechlorination yielding a dissolution enhancement factor of 4.6. The absence of dechlorination in the neat PCE column was suggested to be because PCE dechlorinators that could not tolerate elevated PCE concentrations. The microbial culture used had an inhibitory PCE concentration of 0.54 mM. In the column with mixed NAPL, the aqueous PCE solubility was around 0.3 mM, which was below the inhibitory level and dechlorination could occur. Kaplan et al. (2008) performed column experiments (2.5 cm inner diameter, 30 cm in length) to determine PCE mass fluxes at two different flow velocities. PCE saturation of 35% was established either throughout the entire column or only in the lower quarter of the column. Each column was first run under abiotic conditions, after which inoculation with KB-1 consortium allowed for biotic conditions. Upward flow was applied with water, consisting of KB-1 nutrient medium and 6 mM methanol. PCE, TCE, and cDCE were detected in the effluent of the biotic columns. PCE effluent concentrations were consistently greater in biotic columns than in abiotic columns, suggesting the influence of microbially generated surfactants. The overall bioenhancement factor was 1.5, determined by mass flux calculations. This is partly due to the increase in daughter products in the biotic effluent, but the main contributor is the higher PCE effluent concentration in the biotic columns, which in some cases, exceeded the PCE solubility limit. This was supported by surface tension measurements which showed reduced surface tension values. Concentrations of daughter products in effluents of columns with NAPL in the lower quarter of the column were greater than those from columns with NAPL throughout the column. This suggests that dechlorination is better in zones near than within NAPL source zones. In columns with higher flow velocities, a smaller mass flux of PCE daughter products were found than in slower columns. This indicates a certain residence time for microorganisms is required before dechlorination occurs. 

### 2.4.4 Two-dimensional experiments 

A column with one-dimensional flow will show clogging more readily than in a contamination zone in the field, where flow can more easily take pathways around a clogged section. The difficulty with DNAPL dissolution is that diverted flow may bypass the DNAPL zone, which would reduce dissolution effective


2.4. Enhanced dissolution 45 

ness. Therefore, two-dimensional experiments on DNAPL source zone degradation have been performed on different scales ranging from small to intermediate. Lenhard et al. (1995) defined the conditions needed before an experiment can be classified as intermediate-scale: (i) the experimental configuration has to allow small-scale processes to manifest themselves at a larger scale so that their relative contributions to flow and transport phenomena can be studied and quantified; (ii) the size of the experiment has to be small enough for the environment to be controlled; (iii) the experimental cell dimensions also has to be compatible with measurement and sampling techniques. Although experiments on DNAPL source zone biodegradation cannot all be quantified as intermediate-scale experiments, two-dimensional experiments can be used to study enhanced dissolution, and specifically the effect of DNAPL pools on enhanced dissolution. 

Sleep et al. (2006) performed an intermediate-scale experiment to study bioaugmentation in a PCE source zone and associated changes in microbial community. Two boxes (760 x 380 x 25.4 mm) were packed with soil from a field site and 10 ml PCE was injected in the middle. Groundwater from a site was pumped through each box to yield a residence time of 6.5 days. Until 110 days, no dechlorination was observed. At that time, bio-stimulation of both boxes was started in three periods with methanol, acetate, and ethanol. One box was also bioaugmented with the KB1 dechlorinating culture. On day 275, complete dechlorination to ethene was observed in the box where bioaugmentation took place. A bioenhanced dissolution factor of 1.7 was observed, with a maximum factor of three. This initial biological enhancement factor declined with time. Probably, biomass growth and methane gas generation upstream of the source zone caused both consumption of electron donor and bypassing of flow around the DNAPL source zone. 

Seagren et al. (2002) performed a number of column experiments with a LNAPL, toluene-in-dodecane mixture, present in a small extension of the column. This was ranked as a two-dimensional experiments since columns were placed horizontally and a reservoir extension (10 mm height) was placed on the top of the column. The reservoir contained a LNAPL pool. Borosilicate-glass columns with square cross section (45 mm) and length 400 mm were packed with soda-lime glass beads with a diameter of 2 mm. They inoculated the columns with PpG9, a wild-type strain originally isolated from soil, which is able to grow via toluene oxidation. Comparisons were made between columns with various toluene mole fractions in dodecane, with and without biodegradation, and various water flow velocities. Abiotic experiments were performed by adding NaN 3 to the bulk feed solution; this compound inhibits biological activity. Columns 1 


46 Chapter 2. Review DNAPL source zone biodegradation 

and 2 had, respectively, a relatively low and high toluene mole fractions in the pool. Sampling ports were located along the column length. The toluene dissolution flux, averaged over the entire projected pool area, was calculated by dividing the toluene dissolution rate by the total planar pool area. This toluene dissolution flux was compared to the dissolution flux in the absence of biological activity. In column 1, with a flow velocity of 1 m day−^1 , the presence of biological activity enhanced the dissolution flux by a factor of 1.73, whereas with a lower flow velocity of 0.1 m day−^1 , the presence of biological activity enhanced dissolution by 1.16 to 1.87. For similar experimental conditions in column 2, the enhancement factor was insignificant. Note that the absence of bioenhancement does not indicate a lack of biological activity. They suggested that the absence of bioenhancement in column 2 was related to the ratio of NAPL mass depletion due to biodegradation to the dissolution. The bacteria in column 2 were unable to degrade the toluene at a sufficiently rapid rate to have an impact on the interfacial toluene concentration gradient and the dissolution flux. The biomass accumulation per unit surface area in column 2 was lower than in column 1. As the kinetic parameters were the same in both reactors and the electron donor was present in surplus, the high concentration of toluene in column 2, i.e. toxicity effect, must be the reason for this observation. 

A small-scale experiment was performed by Glover et al. (2007), who determined the effect and significance of bioenhanced dissolution from DNAPL pools. They investigated this in a 5-cm long spheroidal flow cell with coarse sand overlain by a fine-grained sand. A DNAPL pool was created in the coarse sand. Three pairs of biotic (KB-1 mixed culture) and abiotic experiments were performed, with DNAPL saturation of 0.25, 0.55 and 0.74, and different flow rates between 0.005 and 0.168 ml hour−^1. Inflow water, consisting of a medium solution with methanol as electron donor, flowed in horizontal direction. At high DNAPL saturations, bioenhanced dissolution was limited. For the lower saturation cells, however, an enhancement factor between four and thirteen was determined. The enhancement was most pronounced at lower flow rates. They postulated that the bioenhancement of dissolution was determined by the thickness of the transition zone near the pool boundary, where the mixing of electron acceptor with the electron donor and nutrients occurred. For pools with a sharp transition zone, dissolution was controlled by diffusion of components away from the pool interface. 

Chu et al. (2003) numerically studied the influence of biomass accumulation, which caused a change in groundwater flow, on microbially enhanced PCE dissolution of a single pool. They presented a two-dimensional advection-dispersion


2.4. Enhanced dissolution 47 

reaction model for a rectangular domain (15 by 5 mm), with groundwater flowing over a PCE pool. Dechlorination was assumed to follow a double MichaelisMenten equation, with electron donor (acetate) and acceptor (PCE) as possible limiting components. The hydraulic conductivity was assumed to be a function of the amount of biomass. Two different relations were used for change in hydraulic conductivity: either due to biofilm growth or due to bacterial plugs formation. Effect on dissolution enhancement was determined for different clogging mechanisms, electron donor concentration, biomass density, and PCE dechlorination rate. The result of abiotic flushing formed the basis for assessing the dissolution enhancement. When clogging was taken into account, biomass accumulation reduced water velocity near the NAPL-water interface and bioenhanced dissolution decreased. Therefore, in both clogging cases, the degree of enhancement was small at the end of the simulations. The electron donor concentration had also an influence on the enhancement of dissolution. They found that at low donor concentrations (500 μM), active biomass tended to grow toward the limiting substrate, so the biomass accumulated away from the NAPL-water interface. This reduced the flow near the NAPL-water interface and increased the diffusion length from the PCE source to the active biomass. The effluent concentration of total chlorinated ethenes was about the same as in the abiotic case; consequently no dissolution enhancement by dechlorinating activity occurred. However, at higher electron donor concentrations, when the active biomass was closer to the NAPL-water interface, a bioenhancement factor of three was found. At low electron donor concentration, the the biomass density and PCE dechlorination rate had little impact on the dechlorination, and thus on bioenhanced dissolution. This suggested that the reaction kinetics were not the limiting factor, but rather the transport of electron donor and acceptor were limiting dechlorination. When electron donor concentration was increased, higher values for the biomass density and PCE dechlorination rate had a positive effect on dechlorination. 

The same model was used to investigate the effects of inhibition kinetics on dissolution enhancement (Chu et al., 2004). Main differences were that the NAPL source was defined in eight rectangular blocks along the boundary of the domain and that two types of bacteria were assumed: (i) dechlorinating bacteria, which use the electron donor for degrading PCE and TCE, and (ii) bacteria that consume electron donor without dechlorination. In order to evaluate how the extent of bioenhanced dissolution was influenced, breakthrough curves for biotic cases were compared with the corresponding abiotic case. Biotic cases were modelled with various microbial kinetics: (i) double Monod kinetics without inhibition (with different electron donor concentrations), (ii) PCE inhibition (with 


48 Chapter 2. Review DNAPL source zone biodegradation 

and without competition for electron donor, two domain widths), (iii) cDCE inhibition, (iv) mixed inhibition of PCE and cDCE, and (v) competitive inhibition between PCE and TCE. The extent of bioenhanced dissolution was controlled by the microbial-related parameters, such as maximum specific growth rate, halfsaturation constant and inhibition constants. Bioenhanced dissolution raised the total effluent concentration of chlorinated ethenes by at least two to nine times, when dechlorination was not subjected to electron donor limitation (e.g. no other microorganisms were using electron donor) or inhibition. 

## 2.5 Summary and conclusions 

Chlorinated compounds are thermodynamically favored as electron acceptors under anaerobic conditions (Dolfing, 2003). Several researchers (Fennell et al., 1997, Yang and McCarty, 1998, Ballapragada et al., 1997) reported that lower hydrogen levels are more favorable for dechlorination than methanogenesis. When hydrogen levels drop below the H 2 threshold concentration for methanogenesis, dechlorination takes place, whereas methanogenesis cannot occur. This has resulted in studies to proliferate dechlorination above methanogenesis by management of hydrogen delivery. This can be achieved through the choice of an electron donor whose fermentation results in a slow-steady, and low-level release of hydrogen over time. Besides thermodynamic preference of dechlorination above methanogenesis, high PCE concentrations (0.3 mM) are inhibitory for methanogens (DiStefano et al., 1991, Nielsen and Keasling, 1999, Smatlak et al., 1996, Fennell et al., 1997). This is beneficial for dechlorination to occur in DNAPL source zones. Experiments at various scales have shown that dechlorination enhances dissolution from NAPL source zones. This can be observed in batch experiments only if bacteria are able to cope with saturated DNAPL concentrations, and/or dechlorinate faster than the dissolution rate to prevent inhibitory concentrations. But toxicity effects to bacteria are frequently present. This does not mean that dechlorination in source zones cannot occur, or that bioenhanced dissolution cannot occur. In experiments in columns or two-dimensional flow cells, micro-environments can be formed in which PCE concentration can be below PCE inhibitory concentration in pores near or within NAPL source zones. Bioenhancement dissolution factors vary between one and sixteen. This is quiet a wide range, because bioenhanced dissolution is dependent on a large number of parameters. Most important are parameters that determine microbial degradation kinetics and DNAPL dissolution, such as aqueous concentrations of 


2.5. Summary and conclusions 49 

electron donor, inhibitors, microbes and competitors, as well as water velocity and clogging mechanisms. 


50 Chapter 2. Review DNAPL source zone biodegradation 

## Bibliography 

Adamson, D. T., J. M. McDade, and J. B. Hughes (2003), Inoculation of a DNAPL source zone to initiate reductive dechlorination of PCE, Environmental Science and Technology, 37 , 2525–2533. 

Adamson, D. T., D. Y. Lyon, and J. B. Hughes (2004), Flux and product distribution during biological treatment of tetrachloroethene dense non-aqueous-phase liquid, Environmental Science and Technology, 38 , 2021–2028. 

Amos, B. K., J. A. Christ, L. M. Abriola, K. D. Pennell, and F. E. L ̈offler (2007), Experimental evaluation and mathematical modeling of microbially enhanced tetrachloroethene (pce) dissolution, Environmental Science and Technology, 41 (3), 963–970, doi:10.1021/es061438n. 

Amos, B. K., E. J. Suchomel, K. D. Pennell, and F. E. L ̈offler (2008), Microbial activity and distribution during enhanced contaminant dissolution from a napl source zone, Water Research, 42 , 2963–2974. 

Bai, G., M. L. Brusseau, and R. M. Miller (1997), Biosurfactant-enhanced removal of residual hydrocarbon from soil, Journal of Contaminant Hydrology, 25 , 157–170. 

Ballapragada, B. S., H. D. Stensel, J. A. Puhakka, and J. F. Ferguson (1997), Effect of hydrogen on reductive dechlorination of chlorinated ethenes, Environmental Science and Technology, 31 , 1728–1734. 

Bosma, T. N. P., P. J. M. Middeldorp, G. Schraa, and A. J. B. Zehnder (1997), Mass transfer limitation of biotransformation: Quantifying bioavailability, Environmental Science and Technology, 31 (1), 248–252. 

Bossert, I. D., M. M. H ̈aggblom, and L. Y. Young (2003), Microbial ecology of dehalogenation, in Dehalogenation. Microbial processes and environmental applications, edited by M. M. H ̈aggblom and I. D. Bossert, first ed., section 2, pp. 33–52, Kluwer Academic Publishers, Boston. 

Brown, D. G., J. Komlos, and P. R. Jaff ́e (2005), Simultaneous utilization of acetate and hydrogen by geobacter sulfurreducens and implications for use of hydrogen as an indicator of redox conditions, Environmental Science and Technology, 39 , 3069–3076. 


Bibliography 51 

Cabirol, N., F. Jacob, J. Perrier, B. Fouillet, and P. Chambon (1998a), Complete degradation of high concentrations of tetrachloroethylene by a methanogenic consortium in a fixed-bed reactor, Journal of Biotechnology, 62 , 133–141. 

Cabirol, N., R. Villemur, J. Perrier, F. Jacob, B. Fouillet, and P. Chambon (1998b), Isolation of a methanogenic bacterium, methanosarcina sp. strain fr, for its ability to degrade high concentrations of perchloroethylene, Canadian Journal Of Microbiology, 44 (12), 1142–1147. 

Carr, C. S., and J. B. Hughes (1998), Enrichment of high-rate PCE dechlorination and comparative study of lactate, methanol, and hydrogen as electron donors to sustain activity, Environmental Science and Technology, 32 , 1817–1824. 

Carr, C. S., and J. B. Hughes (1999), Response to ’comment on ”Enrichment of high-rate PCE dechlorination and comparative study of lactate, methanol, and hydrogen as electron donors to sustain activity”’, Environmental Science and Technology, 33 , 2683–2684. 

Carr, C. S., S. Garg, and J. B. Hughes (2000), Effect of dechlorinating bacteria on the longevity and composition of PCE-containing nonaqueous phase liquids under equilibrium dissolution conditions, Environmental Science and Technology, 34 , 1088–1094. 

Carrera, J., I. Jubany, L. Carvallo, R. Chamy, and J. Lafuente (2004), Kinetic models for nitrification inhibition by ammonium and nitrite in a suspended and an immobilised biomass systems, Process Biochemistry, 39 , 1159–1165. 

Christ, J. A., and L. M. Abriola (2007), Modeling metabolic reductive dechlorination in dense non-aqueous phase liquid source-zones, Advances in Water Resources, 30 (6-7), 1547–1561, doi:10.1016/j.advwatres.2006.05.024. 

Chu, M., P. K. Kitaradis, and P. L. McCarty (2003), Effects of biomass accumulation on microbially enhanced dissolution of a PCE pool: a numerical simulation, Journal of Contaminant Hydrology, 65 (1-2), 79–100, doi:10.1016/S01697722(02)00232-2. 

Chu, M., P. K. Kitanidis, and P. L. McCarty (2004), Possible factors controlling the effectiveness of bioenhanced dissolution of non-aqueous phase tetrachloroethene, Advances in Water Resources, 27 (6), 601–615, doi: 10.1016/j.advwatres.2004.03.002. 


52 Chapter 2. Review DNAPL source zone biodegradation 

Cirpka, O. A., C. Windfuhr, G. Bisch, S. Granzow, H. Scholz-Maramatsu, and H. Kobus (1999), Microbial reductive dechlorination in large-scale sandbox model, Journal of Environmental Engineering, 125 , 861–870. 

Clement, T. P., C. D. Johnson, Y. Sun, G. M. Klecka, and C. Bartlett (2000), Natural attenuation of chlorinated ethene compounds: model development and field-scale application at the Dover site, Journal of Contaminant Hydrology, 42 , 113–140. 

Clement, T. P., Y. C. Kim, T. R. Gautam, and K. K. Lee (2004), Experimental and numerical investigation of dnapl dissolution processes in a laboratory aquifer model, Ground Water Monitoring And Remediation, 24 (4), 88–96. 

Clifford, J. S., M. A. Ioannidis, and R. L. Legge (2007), Enhanced aqueous solubilization of tetrachloroethylene by a rhamnolipid biosurfactant, Journal of Colloid and Interface Science, 305 , 361–365. 

Cope, N., and J. B. Hughes (2001), Biologically-enhanced removal of PCE from NAPL source zones, Environmental Science and Technology, 35 , 2014–2021. 

Cornish-Bowden, A. (1995), Fundamentals of enzyme kinetics, Portland Press, London. 

Cupples, A. M., A. M. Spormann, and P. L. McCarty (2004a), Vinyl chloride and cis-dichloroethene dechlorination kinetics and microorganism growth under substrate limiting conditions, Environmental Science and Technology, 38 (4), 1102–1107, doi:10.1021/es0348647. 

Cupples, A. M., A. M. Spormann, and P. L. McCarty (2004b), Comparative evaluation of chloroethene dechlorination to ethene by dehalococcoides-like microorganisms, Environmental Science and Technology, 38 , 4768–4774. 

Davis, E. L. (1997), How heat can accelerate in-situ soil and aquifer remediation: Important chemical properties and guidance on choosing the appropriate technique, Tech. Rep. EPA/540/S-97/502, EPA Ground Water Issue, U.S. Environmental Protection Agency, Washington, DC. 

Dennis, P. C., B. E. Sleep, R. R. Fulthorpe, and S. N. Liss (2003), Phylogenetic analysis of bacterial populations in an anaerobic microbial consortium capable of degrading saturation concentrations of tetrachloroethylene, Canadian Journal of Microbiology, 49 , 15–27. 


Bibliography 53 

DiStefano, T. D., J. M. Gossett, and S. H. Zinder (1991), Reductive dechlorination of high concentrations of tetrachloroethene to ethene by an anaerobic enrichment culture in the absence of methanogenesis, Applied and Environmental Microbiology, 57 , 2287–2292. 

DiStefano, T. D., J. M. Gossett, and S. H. Zinder (1992), Hydrogen as an electron donor for dechlorination of tetrachloroethene by an anaerobic mixed culture, Applied and Environmental Microbiology, 58 , 3622–3629. 

Dolfing, J. (2003), Thermodynamic considerations for dehalogenation, in Dehalogenation. Microbial processes and environmental applications, edited by M. M. H ̈aggblom and I. D. Bossert, first ed., section 4, pp. 89–114, Kluwer Academic Publishers, Boston. 

Drever, J. I. (1997), The geochemistry of natural waters: surface and groundwater environments, Prentice Hall, New York. 

Fennell, D. E., and J. M. Gossett (1998), Modeling the production of and competition for hydrogen in a chlorinating culture, Environmental Science and Technology, 32 , 2450–2460. 

Fennell, D. E., and J. M. Gossett (1999), Comment on ”Enrichment of high-rate PCE dechlorination and comparative study of lactate, methanol, and hydrogen as electron donors to sustain activity”, Environmental Science and Technology, 33 , 2681–2682. 

Fennell, D. E., J. M. Gossett, and S. H. Zinder (1997), Comparison of butyric acid, ethanol, lactic acid, and propionic acid as hydrogen donors for the reductive dechlorination of tetrachloroethene, Environmental Science and Technology, 31 , 918–926. 

Glover, K. C., J. Munakata-Marr, and T. H. Illangasekare (2007), Biologically enhanced mass transfer of tetrachloroethene from DNAPL in source zones: experimental evaluation and influence of pool morphology, Environmental Science and Technology, 41 , 1384–1389. 

Harwell, J. H., D. A. Sabatini, and R. C. Knox (1999), Surfactants for ground water remediation, Colloids and Surfaces, A, 151 , 255–268. 

Haston, Z. C., and P. L. McCarty (1999), Chlorinated ethene half-velocity coefficients (Ks) for reductive dehalogenation, Environmental Science and Technology, 33 , 223–226. 


54 Chapter 2. Review DNAPL source zone biodegradation 

Hoelen, T. P., and M. Reinhard (2004), Complete biological dehalogenation of chlorinated ethylenes in sulfate containing groundwater, Biodegradation, 15 , 395–403. 

Holliger, C., G. Wohlfarth, and G. Diekert (1999), Reductive dechlorination in the energy metabolism of anaerobic bacteria, FEMS Microbiology reviews, 22 , 383–398. 

Holliger, C., C. Regeard, and G. Diekert (2003), Dehalogenation by anaerobic bacteria, in Dehalogenation. Microbial processes and environmental applications, edited by M. M. H ̈aggblom and I. D. Bossert, first ed., section 5, pp. 115–157, Kluwer Academic Publishers, Boston. 

Hood, E., D. Major, and G. Driedger (2007), The effect of concentrated electron donors on the solubility of trichloroethene, Ground Water Monitoring And Remediation, 27 (4), 93–98. 

Hood, E. D., D. W. Major, J. W. Quinn, W. S. Yoon, A. Gavaskar, and E. A. Edwards (2008), Demonstration of enhanced bioremediation in a TCE source area at launch complex 34, Cape Canaveral Air Force Station, Ground Water Monitoring and Remediation, 28 , 98–107. 

Imhoff, P. T., A. Frizzell, and C. T. Miller (1997), Evaluation of thermal effects on the dissolution of a nonaqueous phase liquid in porous media, Environmental Science and Technology, 31 , 1615–1622. 

Isalou, M., B. E. Sleep, and S. N. Liss (1998), Biodegradation of high concentrations of tetrachloroethene in a continuous flow column system, Environmental Science and Technology, 32 , 3579–3585. 

Kaplan, A. R., J. Munakata-Marr, and T. H. Illangasekare (2008), Biodegradation of residual dense nonaqueous-phase liquid tetrachloroethene: Effects on mass transfer, Bioremediation Journal, 12 , 21–31, doi: 10.1080/10889860701866289. 

Kassenga, G., J. H. Pardue, W. M. Moe, and K. S. Bowman (2004), Hydrogen thresholds as indicators of dehalorespiration in constructed treatment wetlands, Environmental Science and Technology, 38 (4), 1024–1030, doi: 10.1021/es0348391. 

Khachikian, C., and T. C. Harmon (2000), Nonaqueous phase liquid dissolution in porous media: current state of knowledge and research needs, Transport in Porous Media, 38 , 3–28. 


Bibliography 55 

Knauss, K. G., M. J. Dibley, R. N. Leif, D. A. Mew, and R. D. Aines (2000), The aqueous solubility of trichloroethene (TCE) and tetrachloroethene (PCE) as a function of temperature, Applied Geochemistry, 15 , 501–512. 

Kov ́arov ́a-Kovar, K., and T. Egli (1998), Growth kinetics of suspended microbial cells: From single-substrate-controlled growth to mixed-substrate kinetics, Microbiology And Molecular Biology Reviews, 62 (3), 646–666. 

Lebr ́on, C. A., T. McHale, R. Young, D. Williams, M. G. Bogaart, D. W. Major, M. L. McMaster, I. Tasker, and N. Akladiss (2007), Pilot-scale evaluation using bioaugmentation to enhance PCE dissolution at Dover AFB National Test Site, Remediation, 18 , 5–17. 

Lee, I. S., J. H. Bae, Y. R. Yang, and P. L. McCarty (2004), Simulated and experimental evaluation of factors affecting the rate and extent of reductive dehalogenation of chloroethenes with glucose, Journal of Contaminant Hydrology, 74 (1-4), 313–331, doi:10.1016/j.jconhyd.2004.03.006. 

Lee, M. D., J. M. Odom, and R. J. Buchanan Jr. (1998), New perspectives on microbial dehalogenation of chlorinated solvents: Insights from the field, Annual Review of Microbiology, 52 , 423–452. 

Lenhard, R. J., M. Oostrom, C. S. Simmons, and M. D. White (1995), Investigation of density-dependent gas advection of trichloroethylene: Experiment and a model validation exercise, Journal of Contaminant Hydrology, 19 , 47–67. 

L ̈offler, F. E., J. M. Tiedje, and R. A. Sanford (1999), Fraction of electrons consumed in electron acceptor reduction and hydrogen thresholds as indicators of halorespiratory physiology, Applied and Environmental Microbiology, 65 (9), 4049–4056. 

L ̈offler, F. E., J. R. Cole, K. M. Ritalahti, and J. M. Tiedje (2003), Diversity of dechlorinating bacteria, in Dehalogenation. Microbial processes and environmental applications, edited by M. M. H ̈aggblom and I. D. Bossert, first ed., chap. 3, pp. 53–87, Kluwer Academic Publishers, Boston. 

Lovley, D. R., and S. Goodwin (1988), Hydrogen concentrations as an indicator of the predominant terminal electron-accepting reactions in aquatic sediments, Geochimica et Cosmochimica Acta, 52 , 2993–3003. 


56 Chapter 2. Review DNAPL source zone biodegradation 

Lovley, D. R., F. H. Chapelle, and J. C. Woodward (1994), Use of dissolved H 2 concentrations to determine distribution of microbially catalyzed redox reactions in anoxic groundwater, Environmental Science and Technology, 28 , 1205–1210. 

Luijten, M. L. G. C., W. Roelofsen, A. A. M. Langehoff, G. Schraa, and A. J. M. Stams (2004), Hydrogen threshold concentrations in pure cultures of halorespiring bacteria and at a site polluted with chlorinated ethenes, Environmental Microbiology, 6 , 646–650. 

Luong, J. H. T. (1987), Generalization of Monod kinetics for analysis of growth data with substrate inhibition, Biotechnology and Bioengineering, 29 , 242– 248. 

Mayer, A. S., and C. T. Miller (1996), The influence of mass transfer characteristics and porous media heterogeneity on nonaqueous phase dissolution, Water Resources Research, 32 , 1551–1567. 

Maym ́o-Gatell, X., V. Tandoi, J. M. Gossett, and S. H. Zinder (1995), Characterization of an H 2 -utilizing enrichment culture that reductively dechlorinates tetrachloroethene to vinyl chloride and ethene in the absence of methanogenesis and acetogenesis, Applied and Environmental Microbiology, 61 , 3928– 3933. 

Mazur, C. S., and W. J. Jones (2001), Hydrogen concentrations in sulfatereducing estuarine sediments during PCE dehalogenation, Environmental Science and Technology, 35 , 4783–4788. 

Mazur, C. S., W. J. Jones, and C. Tebes-Stevens (2003), H 2 consumption during the microbial reductive dehalogenation of chlorinated phenols and tetrachloroethene, Biodegradation, 14 , 285–295. 

McCarty, P. L. (1997), Breathing with chlorinated solvents, Science, 276 , 1521– 1522. 

McGuire, T. M., J. M. McDade, and C. J. Newell (2006), Performance of DNAPL source depletion technologies at 59 chlorinated solvent-impacted sites, Ground Water Monitoring And Remediation, 26 (1), 73–84. 

Mercer, J. W., and R. M. Cohen (1990), A review of immiscible fluids in the subsurface: properties, models, characterization and remediation, Journal of Contaminant Hydrology, 6 , 107–163. 


Bibliography 57 

Michaelis, L., and M. L. Menten (1913), Die Kinetik der Invertinwerkung, Biochemische Zeitschrift, 49 , 333–369. 

Miller, C. T., M. M. Poirier-McNeill, and A. S. Mayer (1990), Dissolution of trapped nonaqueous phase liquids: mass transfer characteristics, Water Resources Research, 26 , 2783–2796. 

Monod, J. (1949), The growth of bacterial cultures, Annual Review of Microbiology, 3 , 371–394. 

Nielsen, R. B., and J. D. Keasling (1999), Reductive dechlorination of chlorinated ethene DNAPLs by a culture enriched from contaminated groundwater, Biotechnology and Bioengineering, 62 , 160–165. 

Payne, F. C., S. S. Suthersan, D. K. Nelson, G. Suarez, I. Tasker, and N. Akladiss (2006), Enhanced reductive dechlorination of PCE in unconsolidated soils, Remediation, 17 , 5–21. 

Pon, G., M. R. Hyman, and L. Semprini (2003), Acetylene inhibition of trichloroethene and vinyl chloride reductive dechlorination, Environmental Science and Technology, 37 , 3181–3188. 

Powers, S. E., C. O. Loureiro, L. M. Abriola, and W. J. Weber (1991), Theoretical-study of the significance of nonequilibrium dissolution of nonaqueous phase liquid in subsurface systems, Water Resources Research, 27 (4), 463–477. 

Powers, S. E., L. M. Abriola, and W. J. Weber (1992), An experimental investigation of nonaqueous phase liquid dissolution in saturated subsurface systems 

- steady-state mass-transfer rates, Water Resources Research, 28 (10), 2691– 2705. 

Powers, S. E., L. M. Abriola, J. S. Dunkin, and W. J. Weber (1994), Phenomenological models for transient napl-water mass-transfer processes, Journal of Contaminant Hydrology, 16 (1), 1–33. 

Rittmann, B. E., and P. L. McCarty (2001), Environmental Biotechnology: Principles and Applications, McGraw-Hill, New York. 

Saba, T., and T. Illangasekare (2000), Effect of groundwater flow dimensionality on mass transfer from entrapped nonaqueous phase liquid contaminants, Water Resources Research, 36 (4), 971–979. 


58 Chapter 2. Review DNAPL source zone biodegradation 

Schwille, F. (1998), Dense chlorinated solvents in porous and fractured media. Model experiments, Lewis Publishers, Chelsea, Michigan. 

Seagren, E. A., B. E. Rittmann, and A. J. Valocchi (1993), Quantitative evaluation of flushing and biodegradation for enhancing in situ dissolution of nonaqueousphase liquids, Journal of Contaminant Hydrology, 12 , 103–132. 

Seagren, E. A., B. E. Rittmann, and A. J. Valocchi (1994), Quantitative evaluation of the enhancement of NAPL-pool dissolution by flushing and biodegradation, Environmental Science and Technology, 28 , 833–839. 

Seagren, E. A., B. E. Rittmann, and A. J. Valocchi (2002), Bioenhancement of NAPL pool dissolution: experimental evaluation, Journal of Contaminant Hydrology, 55 , 57–85. 

Sleep, B. E., et al. (2006), Biological enhancement of tetrachloroethene dissolution and associated microbial community changes, Environmental Science and Technology, 40 , 3623–3633. 

Smatlak, C. R., J. M. Gossett, and S. H. Zinder (1996), Comparative kinetics of hydrogen utilization for reductive dechlorination of tetrachloroethene and methanogenesis in an anaerobic enrichment culture, Environmental Science and Technology, 30 , 2850–2858. 

Stroo, H. F., M. Unger, C. H. Ward, M. C. Kavanaugh, C. Vogel, A. Leeson, J. A. Marqusee, and B. P. Smith (2003), Remediating chlorinated solvent source zones, Environmental Science and Technology, 37 , 224A–230A. 

Stumm, W., and J. J. Morgan (1996), Aquatic chemistry. Chemical equilibria and rates in natural waters, third ed., John Wiley & Sons, Inc, New York. 

Tandoi, V., T. D. DiStefano, P. A. Bowser, J. M. Gossett, and S. H. Zinder (1994), Reductive dehalogenation of chlorinated ethenes and halogenated ethanes by a high-rate anaerobic enrichment culture, Environmental Science and Technology, 28 , 973–979. 

Wymore, R. A., T. W. Macbeth, R. J. S., L. N. Peterson, L. O. Nelson, K. S. Sorenson Jr., N. Akladiss, and I. Tasker (2006), Enhanced anaerobic bioremediation in a DNAPL residual source zone: test area north case study, Remediation, 17 , 5–22. 


Bibliography 59 

Yang, Y., and P. L. McCarty (1998), Competition for hydrogen within a chlorinated solvent dehalogenating anaerobic mixed culture, Environmental Science and Technology, 32 , 3591–3597. 

Yang, Y., and P. L. McCarty (2000), Biologically enhanced dissolution of tetrachloroethene DNAPL, Environmental Science and Technology, 34 , 2979– 2984. 

Yang, Y. R., and P. L. McCarty (2002), Comparison between donor substrates for biologically enhanced tetrachloroethene DNAPL dissolution, Environmental Science and Technology, 36 (15), 3400–3404, doi:10.1021/es011408e. 

Yu, S., and L. Semprini (2004), Kinetics and modeling of reductive dechlorination at high PCE and TCE concentrations, Biotechnology and Bioengineering, 88 (4), 451–464. 

Yu, S. H., M. E. Dolan, and L. Semprini (2005), Kinetics and inhibition of reductive dechlorination of chlorinated ethylenes by two different mixed cultures, Environmental Science and Technology, 39 (1), 195–205, doi: 10.1021/es0496773. 



## Chapter 3 

# Kinetics of tetrachloroethylene 

# transformation investigated up 

# to solubility by a dechlorinating 

# microbial assemblage. 

## 1 

## Abstract 

In order to investigate the applicability of bioremediation of tetrachloroethylene (PCE) in source zones, batch experiments were carried out using a dechlorinating microbial assemblage. Initial aqueous PCE concentrations were in the range of 0.09 to 0.8 mM and up to the solubility limit (∼1.2 mM) with the presence of PCE as a separate phase. Although recent publications suggest that PCE could be dechlorinated up to saturation concentrations by mixed cultures, the dechlorinating microbial assemblage tested in this study was only able to dechlorinate PCE up to approximately 0.5 mM. No dechlorination was found at higher initial PCE concentrations. Dechlorination of PCE was described by a biokinetic model with the Michaelis-Menten equation including self inhibition with a maximum degradation rate of 80 μmol PCE l−^1 day−^1 , a half saturation constant of 0.33 mM and a PCE inhibition constant of 0.5 mM. In the literature, microbial capabilities to transform PCE are found to be higher. However, these reported values on dechlorination of saturated PCE concentrations by laboratory cultures 

(^1) This chapter has been prepared for submission as part of an article with Laverman, A.M., and Hassanizadeh, S.M. 


62 Chapter 3. Batch experiments 

might have resulted in adaptation to higher PCE concentrations. 

## 3.1 Introduction 

Soil and groundwater pollution by chlorinated solvents, such as tetrachloroethylene (PCE) caused by spills in the dry cleaning and metal (degreasing) industries, are common throughout the industrialized world. These contaminants belong to the group of dense non-aqueous phase liquids (DNAPLs). Chlorinated solvents are toxic and carcinogenic substances and their presence in the subsurface poses environmental and human health risks. Sites contaminated by these DNAPLs often require remediation, however DNAPLs removal is complicated as it is difficult to locate them. This is partly due to their high density, as a result of which they move downward into the subsurface in a flow path that is hard to predict due to micro-heterogeneity of the soil. Another complication for remediation of DNAPLs is their low solubility, which results in a continuous dissolution of contaminant to the groundwater for decades (Schwille, 1998) and reduces effectiveness of many remediation methods. There are several chemical, physical or biological techniques to remove DNAPL pollution, among these, bioremediation is a frequently used technology. The major advantage of biological methods is that toxic compounds are transformed into harmless products, whereas most other techniques only transfer the pollutant to another phase. In addition, biodegradation is an economical technique as it requires minimum maintenance. A variety of anaerobic bacteria are able to reductively dechlorinate PCE to trichloroethylene (TCE) and cis-1,2-dichloroethylene (cDCE) (L ̈offler et al., 2003). Only members of the Dehalococcoides group are able to dechlorinate this further to vinyl chloride (VC) and ethene (ETH) (Maym ́o-Gatell et al., 1995, He et al., 2003). Extensive research has been done on dechlorination of PCE using laboratory experiments. Most experimental research has involved PCE at low concentrations (e.g. de Bruin et al., 1992, Cabirol et al., 1998, Isalou et al., 1998), which is indeed relevant to the majority of PCE plumes encountered in the field. Batch experiments with enrichment cultures showed a rapid degradation of PCE, in concentrations up to 0.3 mM, into 80% ethene and 20% VC (DiStefano et al., 1991). Kinetic parameters (Tandoi et al., 1994) and the effect of different electron donors (Fennell et al., 1997) were also determined for these relatively low concentrations by enrichment cultures. Recently, there has been growing interest in the application of biodegradation to source zones where PCE is present at high concentrations and as a non-aqueous 


3.1. Introduction 63 

phase liquid (NAPL). In source zones, aqueous phase concentrations can reach solubility limit of the DNAPL components (for PCE this is ∼1.2 mM) within short time frames. The ability of microorganisms to dechlorinate high PCE concentrations has been given little attention in the past, mainly because saturation concentrations of chlorinated solvents and the presence of a DNAPL were believed to be toxic to microorganisms (Aulenta et al., 2006). However, dechlorination in source zones has been observed in the field (Hood et al., 2008, Wymore et al., 2006, Payne et al., 2006, Lebr ́on et al., 2007). Thus, recently, more studies have been dedicated to dechlorination in the presence of NAPLs at different laboratory scales. Usually, batch experiments are performed as an easy first test to assess the dechlorination potential. However, batch investigations on dechlorination of dissolved PCE at high concentrations and dissolved PCE in the presence of a non-aqueous phase have shown conflicting results (Sharma and McCarty, 1996, Tandoi et al., 1994, Nielsen and Keasling, 1999, Amos et al., 2007). Some studies show dechlorination to ethene, whereas others report PCE inhibition concentrations between 0.5 and 0.8 mM PCE (Yang and McCarty, 2000, Duhamel et al., 2002, Amos et al., 2007). Variation in dechlorination kinetics and pathways could be explained by differences in pre-treatments of microbial cultures involved and the experimental setup. However, all those laboratory studies were performed with bacteria that were maintained in the presence of dissolved PCE in the laboratory for months, or even years, under ideal circumstances (e.g. temperature, nutrient supply) before and during experiments. This would presumable result in the adaptation of bacteria to high PCE concentrations and their ability for bioaugmentation of source zones in the field. To extrapolate experimental data on PCE dechlorination to the field, we performed batch experiments with a dechlorinating microbial assemblage that was present and active in an aquifer. To make the link with the aquifer, sand was added to some batches to provide the bacteria with attachment sites. Thus, we have performed batch experiments on dechlorination of PCE using dechlorinating bacteria originating from field sites where bioaugmentation of PCE pollution had been carried out. Dechlorinating microbial assemblages were obtained from an on-site bioreactor as well as from a monitoring well within the source zone. The bacteria were not subjected to prior acclimatization before usage in the experiments. Thus, parameters relevant to field conditions were determined through fitting our results to Michaelis-Menten degradation kinetics including inhibition. 


64 Chapter 3. Batch experiments 

## 3.2 Material and Methods 

### 3.2.1 Chemicals 

The PCE (≥ 99.9% purity) used in the batch experiments was purchased from Merck BV. Neat PCE was dyed with Sudan Red B from Fluka. To calibrate the liquid degradation products, the following chemicals were purchased from Merck BV: TCE (≥ 99.5%), cDCE (≥ 98%), and from Sigma-Aldrich: 1,1-dichloroethylene (1,1DCE, ≥ 99.9%) and trans-1,2-dichloroethylene (tDCE, ≥ 98%). To calibrate the gaseous degradation products, the gases VC, ethene, ethane, and methane (all ∼5 vol%) were obtained from Air Products (Brussels) in a helium gas cylinder. 

### 3.2.2 Dechlorinating microbial assemblage 

The dechlorinating microbial assemblage was provided by Bioclear B.V. (Groningen, The Netherlands), who developed it in a large bioreactor by adapting sludge under anaerobic and favorable conditions for dechlorinating microorganisms (temperature, electron donor, and nutrients). This bioreactor was placed on site at several locations contaminated with PCE or TCE in The Netherlands. In this method, groundwater was continuously pumped up from between 10 to 40 m below ground surface to one or more reactor(s) at the surface. Water was then mixed with anaerobic electron donor in the bioreactor before injection back into the subsurface. The microbial assemblage used in our batch experiments came from the effluent of a bioreactor or from groundwater from a monitoring well at a contaminated site. The bioreactor was used to remediate a contaminant plume situated in Twello (The Netherlands). The monitoring well, 10 m below ground surface, was situated in a source zone at the Evenblij site in Hoogeveen (The Netherlands). At this site, a bioreactor was present from 2001 to 2003 in which acetate and lactic acid were added as electron donors. After 2003, the source zone was not completely removed but remediation activities stopped. Biodegradation halted due to limiting concentration of electron donor, but anaerobic conditions were conserved. In 2006, groundwater from the monitoring well was collected. The water from the bioreactor did not contain any chlorinated solvents, whereas the water from the monitoring well contained low concentrations of cDCE (50 μM) and VC (20 μM). Water was collected anaerobically in green glass bottles and filled to the top. Transportation took place at ±10 °C. The experiments started within a day of the water arriving in the laboratory. To get a general insight in the numbers of three different groups of bacte


3.2. Material and Methods 65 

ria, a quantitative-polymerase chain reaction (q-PCR) analysis was performed under standard conditions by Bioclear B.V. (The Netherlands, personal communication). Water samples from the bioreactor (B) and the monitoring well (MW) were analyzed at the start of the experiment. Three groups of bacteria were quantitatively analyzed: Bacteria, Archeae, and Dehalococcoides spp. (Dhc); the latter being a specific group of microorganisms able to dechlorinate PCE beyond cDCE. This Dhc bacteria belong to the domain Bacteria. 

### 3.2.3 Batch experiments 

In total, ten sets of batch experiments, mostly in triplicates, were performed. A list of all experiments is given in Table 3.1. Batch experiments were carried out with different PCE concentrations, ranging from 0.09 to 0.8 mM by adding 0.01 up to 0.09 mmol PCE, increasing in steps of 0.01 mmol. Two series contained PCE as a separate phase and in these bottles the aqueous PCE concentration was equal to the solubility limit. Two batch experiments contained sand (Quartzsand H31, Sibelco, Belgium) in order to provide the microbial assemblage with attachment sites. Sterile controls to account for non-biological transformations were prepared by autoclaving the water containing the dechlorinating microbial assemblage and 0.02 mmol PCE. The experiments were preformed in 120-ml glass bottles (Alltech) closed with a viton stopper (Rubber B.V., Hilversum, The Netherlands). The bottles contained 90 ml of an anaerobic medium which consisted of: 2 mM Na-acetate (Merck), 5 mM K-L-lactate (Fluka), 1.6 mM NH 4 Cl (Merck), 0.37 mM KH 2 PO 4 (Merck), and 16.4 mM NaHCO 3 (Merck). The pH of the medium was 7.5. Resazurin (1 mg l−^1 , Sigma-Aldrich) was added as a redox indicator and 1 ml l−^1 of a trace element solution (De Zeeuw, 1984) was added. All bottles were autoclaved at 120 °C for 20 minutes and flushed with N 2 /CO 2 gas (99.5 vol%/0.5 vol%) during cooling. To completely reduce the medium, 100 μl of pre-autoclaved 0.2 M sodium-sulfide solution (Na 2 S, Sigma-Aldrich) was added. PCE was added to the bottles in two different ways depending on the target concentration. The bottles with PCE lower than 1 mmol were amended with PCE dissolved in methanol (Merck, ≥ 99.9%). This stock solution (50 mM PCE) was prepared to obtain the desired PCE concentrations in the bottles. Direct use of neat PCE to the bottles would have required a prohibitively small volume to be added. The methanol in the stock solution was autoclaved and flushed with N 2 /CO 2 gas during cooling. PCE was only flushed with the gas, not autoclaved. To completely reduce the stock solution, 100 μl of sodium-sulfide solution was added. The bottles with neat PCE were amended with 50 and 100 μl flushed PCE. 


66 Chapter 3. Batch experiments 

Table 3.1: Details of performed batch experiments. The origin of the culture is B for Bioreactor and MW for Monitoring Well. Ratio electron donor (ED) equivalents to PCE equivalents is on CO 2 basis. 

 Initial Ratio ED equiv. No. of Experiment Origin of Additional PCE to PCE equiv. bottles time culture information mmol days 0.01 456 3 175 B 5 110 MW 0.02 413 3 175 B 2 175 B Sterile control 4 110 MW 2 110 MW Contained 15 g sand 0.03 399 3 175 B 0.04 392 3 175 B 0.05 388 3 175 B 0.06 385 3 175 B 0.07 383 3 175 B 0.08 381 3 175 B 0.09 380 2 175 B 4.9 1.8 2 175 B NAPL present 9.8 0.9 3 175 B NAPL present 

Finally, in an inflatable glove chamber (I^2 R, Instruments For Research & Industry, Cheltenham, Pennsylvania) filled with N 2 /CO 2 gas, 10 ml of the water containing dechlorinating culture was added to each bottle. The electron donor to PCE ratio (ED:PCE) in the experiments are given in Table 3.1. The bottles that received neat PCE had a low ED:PCE ratio because this is based on the total moles of PCE present (and not only the dissolved mass). During cultivation at 20 °C (± 1 °C), the bottles were covered with aluminium foil to prevent growth of photosynthetic microorganisms. They were placed in inverted position on an orbital platform shaker with 80 rpm. 

### 3.2.4 Analytical methods 

For the analysis of chlorinated ethenes, water samples (0.1 1 ml) were withdrawn by a syringe from the bottles. Sterile disposable needles were first flushed with N 2 /CO 2 gas to prevent any oxygen entering the bottles. The extracted water volume was compensated by injecting the same volume of N 2 /CO 2 gas into the bottles. The water sample was transferred to a 1.5-ml measurement vial 


3.2. Material and Methods 67 

(crimp neck, Alltech, The Netherlands) containing 30 μl of H 3 PO 4 to prevent further degradation of the chlorinated ethenes. Crimp neck vials were capped with teflon/red rubber septa immediately after sampling. 

The concentration of the PCE and degradation products were determined using gas chromatography (GC). GC measurements were performed using a HP6890 (Agilent Technologies) gas chromatograph with two detectors: an electron capture detector (ECD) and a flame ionization detector (FID). The ECD was used for the detection of PCE and TCE, whereas the lighter chlorinated ethenes and ethene, ethane, and methane were detected on the FID. Measurements were automated using a 8200 Auto-sampler (Varian Chrompack) and injection of the sample into the GC column was achieved by a solid phase micro extraction (SPME) fiber (Supelco). The fiber had a polydimethylsiloxane (PDMS) coating and a thickness of 100 μm and was placed in the headspace of the 1.5-ml measurement vial for five minutes, during which adsorption of the volatile compounds to the SPME fiber takes place. Then, the fiber was inserted for three minutes into the inlet of a gas chromatograph, which was at 240 °C, allowing desorption of the chlorinated ethenes to occur and the components to enter the GC column. 

Chromatographic separation was achieved using a 30 m x 0.32 mm Heliflexr ATT M^ -Q column (Alltech, The Netherlands) with a porous divinyl benzene polymer phase and helium as the carrier gas. The GC oven was initially set at 30 °C for three minutes. The temperature was then raised at a rate of 30 °C/min to 180 °C; 25 °C/min to 230 °C; then held constant for ten minutes. The program was run under constant pressure (∼0.6 bar overpressure) mode with a split ratio of 20:1. The temperature of the detectors was maintained at 250 °C. To prevent overload in the GC column, samples with a concentration higher than 0.1 mM PCE were diluted with distilled water. Dilutions were performed in 1.5-ml vials with a minimum headspace to prevent the loss of chlorinated ethene to the gas phase. All measurement vials contained 1 ml liquid. It was assumed that there was no mass-transfer limitation of chlorinated ethenes on the time scale (days) of the extraction of samples from the aqueous phase. 

A six-point standard calibration curve for each chlorinated ethene was generated by spiking distilled water with target analytes. Two stock solutions in methanol were prepared containing all liquid chlorinated ethenes (PCE, TCE, cDCE, tDCE, and 1,1-DCE) with two different concentrations. From these stocks, six solutions with known concentrations were prepared in 12-ml vials closed with aluminum crimp caps and teflon-lined butyl rubber stoppers. Next, from these solutions, 1 ml samples were transferred to 1.5-ml measuring vials via a gas tight syringe. Gaseous components (VC, ethene, ethane, and methane) were added to the 


68 Chapter 3. Batch experiments 

measuring vials using a similar syringe. Concentrations of all ethene components in these vials were exactly known and the peak heights from GC measurements of these dilutions were used to calculate calibration curves. Finally, concentrations in samples from the bottles could be calculated by comparing the corresponding peak height with the standard calibration curve. Detection of methane was only qualitative, not quantitative as the SPME fiber was not that sensitive to methane for the concentrations in the gas cylinder. 

### 3.2.5 Reaction rates 

The PCE dechlorination rate was calculated from the decline of aqueous phase PCE concentrations. Each time a sample was taken, a small amount of mass of chlorinated ethene was taken and the liquid volume in the bottles decreased. Therefore, the aqueous phase concentration decreased as a result of the equilibrium between the liquid and gas phase according to Henry’s Law. The bottles with the lowest PCE concentration required the largest sample volume and, consequently, the change in phase volume was most pronounced. Based on a maximum extracted water volume of 10 ml for the time PCE was dechlorinated and a Henry coefficient, KhPCE , of 0.54 (Gossett, 1987), the error in the PCE water concentration would be 4% when neglecting this phase volume change. Therefore, for the calculation of the PCE dechlorination rate, the change in phase volume were neglected. In all experiments, PCE dechlorination started with a lag time. Rates of PCE dechlorination in the batch experiments were calculated after the lag time. The PCE dechlorination lag time was defined as the time from the start of the experiment to the time at which the concentration was 70% of the initial nominal PCE concentration and cDCE was detected. This measurement point is also used to determine the average PCE degradation rate, which is the slope of a linear equation based on five surrounding points. The PCE dechlorination rates for different initial concentrations were fitted to the Michaelis-Menten formula. To account for toxic PCE concentrations, self-inhibition was included: 

 dC dt = Rmax 

#### C 

 C + Km 

#### ( 

#### 1 − 

#### C 

 Cmax 

 )n (3.1) 

where C (mmol l−^1 ) is the PCE concentration, Rmax (mmol l−^1 day−^1 ) is the maximum PCE degradation rate, Km (mmol l−^1 ) is the half-saturation constant, Cmax (mmol l−^1 ) is the maximum concentration at which degradation will occur and is referred to as the PCE inhibition constant, and n is a constant (Luong, 1987, 


3.3. Results 69 

Amos et al., 2007). Note that Rmax and Km are apparent kinetic parameters that depend on factors such as temperature, electron donor availability, and community composition. Another type of inhibition tested was competitive inhibition: 

 dC dt = Rmax 

#### C 

 C + Km 

#### ( 

1 + (^) KCI 

#### ) (3.2) 

where KI (mmol l−^1 ) is the inhibitory PCE concentration (Cornish-Bowden, 1995). Values for Rmax and Km were first determined with data from bottles that were not inhibited, after which inhibition parameters were estimated. Optimized values for Rmax, Km, KI , Cmax, and n were obtained by forward derivative Newton search algorithm using Excel solverr. 

## 3.3 Results 

### 3.3.1 Characterization of dechlorinating microbial assemblage 

The results of the q-PCR analysis of the different bacterial groups are presented in Table 6.3. Although, the site with the MW was not biostimulated for three years, there are still high numbers of Dhc present. The percentage Dhc, used as an indicator for the dechlorinating capacity, is one order of magnitude larger in the water from the well. In addition, the effluent from the bioreactor contains much more cells from the domain Bacteria. 

Table 3.2: Results of the molecular analysis with q-PCR. The actual number of cells (N) ranges from 0.5*N to 2*N. Here the assumption is that one cell contains one DNA copy. 

 Source water PCE Dehalococcoides Bacteria Dhc/Bacteria Archaea spp. (Dhc) cells ml−^1 cells ml−^1 % cells ml−^1 Bioreactor Plume 4.7· 106 1.6· 108 2.9 6.8· 105 Monitoring Well Source 1.2· 105 5.6· 105 21 1.8· 105 

### 3.3.2 Degradation rates 

The variation in mass of PCE and its degradation products with time, in two bottles with initially 0.02 and 0.03 mmol PCE, are shown in Figure 3.1. These bottles were inoculated with dechlorinating microbial assemblage from the bioreactor. 


70 Chapter 3. Batch experiments 

Mass balances of all bottles were calculated with the masses of the components in the aqueous and gas phase, and the masses withdrawn for samples. In Figure 3.1, the total mass is presented as a line. Except for four bottles with 0.01 mmol PCE, the recovered mass at the end of the experiment was larger than 75%. Results of all batches are given in Table 3.3. Each sign in the PCE column represents a batch experiment. Positive signs (+) indicate dechlorination of the chlorinated ethene. Negative signs (-) indicate no dechlorination and then for the next chlorinated ethene no sign is shown. 

Table 3.3: Overview of results of batch experiments on PCE biodegradation with different initial PCE concentrations. Plus signs represent dechlorination, plus-minus signs represent partial dechlorination, and minus signs show no dechlorination. The number of signs in the PCE column corresponds to the number of bottles used. The origin of dechlorinating microbial assemblage is shown by B for Bioreactor and MW for Monitoring Well. 

 Initial Origin of Additional Substrate used PCE culture information PCE TCE cDCE VC mmol 0.01 B +++ +++ ++++ MW +++++ +++++ ++++++0.02 B +++ +++ ± ± ± B Sterile control MW ++++ ++++ MW 15 g sand ++ ++ 0.03 B +++ +++ 0.04 B +++ +++ 0.05 B +++ +++ 0.06 B ++ 0.07 B 0.08 B 0.09 B 4.9 B NAPL present 9.8 B NAPL present 

It is evident that PCE was (partially) transformed up to 0.05 mmol PCE, whereas no dechlorination was found in bottles with higher PCE. The dechlorination occurred with a lag time, which increased with the initial PCE concentration. 


3.3. Results 71 

When PCE dechlorination started, almost immediately cDCE was detected and the observation of TCE was minimal. This indicates that the dechlorination step from TCE to cDCE is fast (< 3 days). Dechlorination of cDCE occurred only in the bottles with low initial PCE concentration: full dechlorination to VC at 0.01 mmol and incomplete dechlorination at 0.02 mmol PCE. Ethene and ethane concentrations were below detection limits. Methane was detected in bottles with 0.01, 0.02 and 0.03 mmol PCE, first after 26 days. Abiotic microcosms showed no significant PCE dechlorination. PH measurements, over the course of the experiment, showed that the bottles stayed in neutral conditions. 

 0 50 100 150 200 0 

 0.01 

 0.02 

 0.03 i) 

 0 50 100 150 200 0 

 0.01 

 0.02 

 0.03 

 0.04 ii) 

 0 

 25 

 50 

 75 

 100 

 Mass balance (%) 

 PCE TCE cDCE VC Mass balance 

 0 

 25 

 50 

 75 

 100 

 Time (days) 

 Chlorinated ethenes (mmol) 

Figure 3.1: Batch experiment with i) 0.02 mmol and ii) 0.03 mmol PCE with dechlorinating microbial assemblage from the bioreactor. Ethene and ethane were below detection limit. Trace amounts of 1,1-DCE and tDCE were detected and are not shown. 


72 Chapter 3. Batch experiments 

### 3.3.3 Degradation kinetics 

In Figure 3.2, PCE degradation rate and lag time are plotted against the initial aqueous PCE concentration. The PCE dechlorination rate is shown for each bottle with the 95% confidence interval to the linear fit. Maximum potential degradation rates, Rmax, and half-saturation constant, Km, were determined using the standard Michaelis-Menten equation (Equation 3.1, without the last inhibition term) and fitting the measured PCE degradation rates in the bioreactor experiments with PCE concentration lower than 0.47 mM. The Rmax value was about 80 μmol l−^1 day−^1. The half-saturation constant for PCE was 0.33 mM. The PCE inhibition concentration was chosen as 0.5 mM, with which exponent n was determined to be 0.19. For comparison, the profile for competitive inhibition is shown as well. The PCE inhibition constant, KI , was 0.42 mM. The measured PCE degradation rates in the monitoring well (MW) experiments only covered PCE concentrations up to 0.24 mM. However, PCE dechlorination rate for the monitoring well seems to be higher than for the bioreactor as values of 100 μmol l−^1 day−^1 were observed (data not shown). 

## 3.4 Discussion 

The microbial assemblage from the bioreactor was able to dechlorinate PCE up to 0.5 mM, with a Rmax of 80 μmol l−^1 day−^1 and a Km of 0.33 mM based on our experiments. Degradation was inhibited at concentrations above 0.5 mM, which was set as the value for the PCE inhibition constant (Cmax). Similar inhibitory levels have been found by others (e.g. 0.54 mM by Amos et al., 2007), even though in those studies degradation was achieved using pure cultures (see Table 3.4). Conversely, several other studies have showed complete degradation at or near the aqueous solubility of PCE by mixed cultures (Yu and Semprini, 2004, Adamson et al., 2004, Nielsen and Keasling, 1999, Yang and McCarty, 2000, Duhamel et al., 2002) and pure cultures (Sung et al., 2003, Amos et al., 2007). In all those cases, cultures were maintained on PCE or other chlorinated ethenes in the laboratory for several years under optimal conditions, which most likely results in the cultures having a higher capacity to dechlorinate PCE. This is confirmed by the fact that no lag time was reported, suggesting that these bacteria were sufficiently adapted to high concentrations. The microbial assemblage described in the present paper showed a lag time before PCE degradation that was positively correlated to the initial PCE concentration. This lag time is most probably linked to the adaptation time needed for the bacteria to high concentrations. The only 


3.4. Discussion 73 

 0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0 

 50 

 100 

 150 

 200 

 Aqueous PCE concentration (mM) 

 PCE degr. lag time 

 (days) 

 Bioreactor data Michaelis−Menten (MM) kinetics MM with competitive inhibition MM with self inhibition Monitoring well data Monitoring well data with sand 

 0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0 

 0.05 

 0.1 

 0.15 

 0.2 

 PCE degradation rate 

 (mmol l 

 −1 

 day 

 −1 

 ) 

Figure 3.2: (i) Calculated PCE degradation rate as a function of initial PCE concentration. Model fits are based on Michaelis-Menten (MM) kinetics without inhibition and MM with self-inhibition and MM with competitive inhibition. (ii) PCE degradation lag time for different initial PCE concentrations. Different symbols refer to different batches shown in Table 3.1. There are as many symbols as the number of bottles with a given initial concentration. For the 0.5 mM experiment, the lag time could be between 50 and 120 days, here plotted in the middle at 85 days. 

similar lag time was reported by Yang and McCarty (2000) in a batch experiment with PCE phase present. The higher capacity to dechlorinate PCE by cultures maintained on PCE in the laboratory for years, should also be visible in the dechlorination rate. An overview of batch experiments on dechlorination of high PCE concentrations (≥0.3 mM) is given in Table 3.4. Care should be taken in comparing dechlorination rates from different studies, as they have been reported in different units, 


74 Chapter 3. Batch experiments 

as a result of different normalization, i.e. either per unit of culture volume or per unit of measured biomass concentration. To compare the dechlorination rate reported here with literature values, the cell concentration can be expressed in mg protein l−^1 by assuming that a single cell has a protein content of 1.56· 10 −^13 g (Neidhardt and Umbarger, 1996). If all bacteria are included, the dechlorination rate is equivalent to 40 μmol mg protein−^1 day−^1. This is comparable to the degradation rates reported in Table 3.4. The half-saturation constants are lower than the value deduced in this paper, however, the reported values vary with two orders of magnitude. The half-saturation constant obtained from our experiments compare to the half-saturation constant from Nielsen and Keasling (1999) in their mixed culture that dechlorinated saturated PCE concentrations. 

Table 3.4: Literature review on biodegradation results of batch experiments with high (>0.3 mM) initial PCE concentrations. Plus signs represent complete degradation, plusminus signs represent degradation up to certain PCE load, and minus signs show no degradation. M is a Mixed, P is a Pure culture and Sat is Saturation. 

 Bacterial Degradation rate and culture capacity KmPCE CPCE max Reference PCE TCE cDCE VC μM μM μmol mg protein−^1 d−^1 P(ure) 129 335 14 540 Amos et al. (2007) P 234 259 14 P 200 + + Sat Sung et al. (2003) M(ixed) 28 + + + 250 No Nielsen and Keasling (1999) M 12.4 125 13.8 8.1 2.8 No Yu and Semprini (2004) M 13.3 124 22 2.4 3.9 M 10 + ± ± No Yang and McCarty (2000) d−^1 Pseudo first order rate M 4.3 6.5 0 No Carr et al. (2000) M + + ± ± No Adamson et al. (2004) M + + + + No DiStefano et al. (1991) μmol l−^1 d−^1 M 300 960 720 1080 No Tandoi et al. (1994) M 30-50 Sat Duhamel et al. (2002) M 80 + + ± 330 500 This research 

At low PCE concentrations (0.1 mM) the mass balance was incomplete. This set of experiments is the only PCE concentration tested in which dechlorination to VC occurred. VC concentration decreased after its gradual formation, whereas ethene and ethane were not detected. However, we believe that this mass bal


3.4. Discussion 75 

ance deficiency (40%) can be explained by the formation of ethene. The detection limit of ethene and ethane is relatively high (30 μM). Consequently, the withdrawn mass due to sampling would yield a remaining aqueous phase concentration around this value. Alternatively, mass balance deficiency in most bottles (>80%) might have been due to accidental gas escape during sampling. In bottles with PCE lower than 0.03 mmol, a pressure increase in the bottles was noticed and it is possible that the volatile components were lost during sampling. This pressure increase in these bottles could have been caused by the formation of methane by methanogenic bacteria present in the microbial assemblage. This is confirmed by the appearance of methane peaks on the gas chromatogram after 25 days for bottles with PCE lower than 0.03 mmol. In bottles with PCE higher than 0.04 mmol, no pressure increase was observed. This is in line with previous studies which have shown that high PCE concentrations inhibit methanogenesis (DiStefano et al., 1991, Smatlak et al., 1996, Fennell et al., 1997, Yang and McCarty, 2000). 

During complete dechlorination of PCE, the final products are VC and ethene. However, in many experimental studies, at both laboratory and field scales, only partial dechlorination of PCE has been observed (Major et al., 2002). There is evidence that members of the Dehalococcoides group are present where complete dechlorination is observed but are absent where dechlorination is only partially taking place (Fennell et al., 2001, Hendrickson et al., 2002). At present, research suggests that several strains of microorganisms are able to dechlorinate PCE to cDCE, whereas the reduction of cDCE can be achieved by only a limited group of bacteria (Aulenta et al., 2006). In the experiments presented in this paper, a significant level of reductive dechlorination beyond cDCE only occurred in batches with 0.01 mmol PCE. This means that bacteria capable of complete biodegradation are present in all bottles. However, dechlorination of cDCE did not occur in batches with initial PCE higher than 0.02 mmol. This could indicate that Dehalococcoides spp. present were inhibited in bottles with higher PCE concentrations as dechlorination of cDCE stalled. Therefore, it is far more likely that PCE reduction was mediated by a genus other than Dehalococcoides spp. present in the dechlorinating microbial assemblage. 

The molecular analysis of the two microbial assemblages used in this study confirm the presence of Dehalococcoides spp. at both the monitoring well and the bioreactor. Although the percentage Dehalococcoides spp. over bacteria is higher in the monitoring well, the actual number is higher in the bioreactor. This difference is probably caused by the number of bacteria in the two microbial assemblages. The monitoring well was situated in the source zone of a contam


76 Chapter 3. Batch experiments 

inated area and had not been supplied with additional electron donor since the removal of the bioreactor in 2003. In the bioreactor, however, continuous supply of electron donor caused growth of all groups of bacteria; therefore, the percentage of Dehalococcoides spp. of the total bacterial community was low compared to that of the monitoring well. Quantification of mixed cultures with q-PCR not only include the DNA from active dechlorinating organisms but also from inactive organisms. Apparently, the PCE degrading microbial community in the monitoring well developed strongly. 

Low inhibitory PCE concentrations and large PCE lag times, as observed in batch experiments presented in this paper, could have consequences for remediation in source zones. In these zones, concentrations can be around solubility limit, which can be higher than the inhibitory PCE concentration found in this study, and thus biodegradation may not take place. This, however, does not necessarily mean that biodegradation was absent in source zones, as explained below. On the contrary, biodegradation was observed in source zones in the field (Payne et al., 2006, Lebr ́on et al., 2007). The large PCE lag time might have a negative influence on biodegradation in situations where PCE slowly dissolves to yield high concentrations in the water phase, for example in situations where dissolution is controlled by diffusion. The kinetic parameters, including a PCE inhibition constant (Cmax) obtained in this study, are directly related to the microbial assemblage. Apparently this assemblage is capable of degrading PCE at the contaminated site, as degradation in the source zone was established (Van der Werf et al., 2004). 

Two mechanisms can help to promote biodegradation in source zones with high PCE concentration. First, bacteria could create micro-environments with lower PCE concentrations in some pores within a short distance from pores containing PCE. The addition of sand to provide attachment sites is unlikely to be beneficial in creating microsites and no difference in degradation rate or lag time in batches with and without sand were observed during this study. Second, bacteria could dechlorinate PCE so fast, that the PCE concentration always remains below the inhibitory concentration. This has been observed by Amos et al. (2007), who tested pure cultures of which one was able to keep the aqueous PCE concentration below the inhibitory level in the presence of PCE. Apparently, this was not occurring in the batch experiments described here. Future work will involve soil column experiments to test these hypotheses. 


3.5. Conclusions 77 

## 3.5 Conclusions 

Batch experiments were performed with a dechlorinating microbial assemblage from a bioreactor used for bioaugmentation and from a monitoring well in a bioaugmented site, three years after bioaugmentation. The culture from the monitoring well dechlorinated PCE in bottles with tested initial concentrations up to 0.2 mM. The culture from the bioreactor was able to dechlorinate PCE concentrations up to 0.5 mM, which was the inhibitory PCE concentration. Estimated PCE dechlorination rate, Rmax, was 80 μmol l−^1 day−^1 and the half-saturation constant, Km, was 0.33 mM. Dechlorination of the bioreactor was best fit to the Michealis-Menten equation with self inhibition. As the culture had no prior acclimatization and the bacteria were not in the laboratory adapted to PCE, the observed capability to transform PCE and deduced parameter values could be valid for contaminated field sites. 

## Acknowledgment 

This study has been financially supported by the TRIAS program, a joint venture of the Netherlands Organization of Scientific Research (NWO), the Netherlands Center for Soil Quality Management and Knowledge Transfer (SKB) and Delft Cluster. The authors thank K. Reimer, Netherlands Institute for Applied Scientific Research (TNO), for help on the chlorinated ethene analysis and Bioclear B.V., Groningen, The Netherlands, for performing the q-PCR analysis. 


78 Chapter 3. Batch experiments 

## Bibliography 

Adamson, D. T., D. Y. Lyon, and J. B. Hughes (2004), Flux and product distribution during biological treatment of tetrachloroethene dense non-aqueous-phase liquid, Environmental Science and Technology, 38 , 2021–2028. 

Amos, B. K., J. A. Christ, L. M. Abriola, K. D. Pennell, and F. E. L ̈offler (2007), Experimental evaluation and mathematical modeling of microbially enhanced tetrachloroethene (pce) dissolution, Environmental Science and Technology, 41 (3), 963–970, doi:10.1021/es061438n. 

Aulenta, F., M. Majone, and V. Tandoi (2006), Enhanced anaerobic bioremediation of chlorinated solvents: environmental factors influencing microbial activity and their relevance under field conditions, Journal Of Chemical Technology And Biotechnology, 81 (9), 1463–1474, doi:10.1002/jctb.1567. 

Cabirol, N., F. Jacob, J. Perrier, B. Fouillet, and P. Chambon (1998), Complete degradation of high concentrations of tetrachloroethylene by a methanogenic consortium in a fixed-bed reactor, Journal of Biotechnology, 62 , 133–141. 

Carr, C. S., S. Garg, and J. B. Hughes (2000), Effect of dechlorinating bacteria on the longevity and composition of PCE-containing nonaqueous phase liquids under equilibrium dissolution conditions, Environmental Science and Technology, 34 , 1088–1094. 

Cornish-Bowden, A. (1995), Fundamentals of enzyme kinetics, Portland Press, London. 

de Bruin, W. P., M. J. J. Kotterman, M. A. Posthumus, G. Schraa, and A. J. B. Zehnder (1992), Complete biological reductive transformation of tetrachloroethene to ethane, Applied and Environmental Microbiology, 58 , 1996– 2000. 

De Zeeuw, W. J. (1984), Acclimatization of anaerobic sludge for uasb reactor start-up, Ph.D. thesis, Wageningen Agricultural University, The Netherlands. 

DiStefano, T. D., J. M. Gossett, and S. H. Zinder (1991), Reductive dechlorination of high concentrations of tetrachloroethene to ethene by an anaerobic enrichment culture in the absence of methanogenesis, Applied and Environmental Microbiology, 57 , 2287–2292. 


Bibliography 79 

Duhamel, M., S. D. Wehr, L. Yu, H. Rizvi, D. Seepersad, S. Dworatzek, E. E. Cox, and E. A. Edwards (2002), Comparison of anaerobic dechlorinating enrichment cultures maintained on tetrachloroethene, trichloroethene, cis-dichloroethene and vinyl chloride, Water Research, 36 , 4193–4202. 

Fennell, D. E., J. M. Gossett, and S. H. Zinder (1997), Comparison of butyric acid, ethanol, lactic acid, and propionic acid as hydrogen donors for the reductive dechlorination of tetrachloroethene, Environmental Science and Technology, 31 , 918–926. 

Fennell, D. E., A. B. Carroll, J. M. Gossett, and S. H. Zinder (2001), Assessment of indigenous reductive dechlorinating potential at a TCE-contaminated site using microcosms, polymerase chain reaction analysis, and site data, Environmental Science and Technology, 35 , 1830–1839. 

Gossett, J. M. (1987), Measurement of Henry’s Law constants for C 1 and C 2 chlorinated hydrocarbons, Environmental Science and Technology, 21 , 202– 208. 

He, J., K. M. Ritalahti, M. R. Aiello, and F. E. L ̈offler (2003), Complete detoxification of vinyl chloride by an anaerobic enrichment culture and identification of the reductively dechlorinating population as a Dehalococcoides species, Applied and Environmental Microbiology, 69 , 996–1003. 

Hendrickson, E. R., J. A. Payne, R. M. Young, M. G. Starr, M. P. Perry, S. Fahnestock, D. E. Ellis, and R. C. Ebersole (2002), Molecular analysis of Dehalococcoides 16S ribosomal DNA from chloroethene-contaminated sites throughout north america and Europe, Applied and Environmental Microbiology, 68 , 485– 495. 

Hood, E. D., D. W. Major, J. W. Quinn, W. S. Yoon, A. Gavaskar, and E. A. Edwards (2008), Demonstration of enhanced bioremediation in a TCE source area at launch complex 34, Cape Canaveral Air Force Station, Ground Water Monitoring and Remediation, 28 , 98–107. 

Isalou, M., B. E. Sleep, and S. N. Liss (1998), Biodegradation of high concentrations of tetrachloroethene in a continuous flow column system, Environmental Science and Technology, 32 , 3579–3585. 

Lebr ́on, C. A., T. McHale, R. Young, D. Williams, M. G. Bogaart, D. W. Major, M. L. McMaster, I. Tasker, and N. Akladiss (2007), Pilot-scale evaluation using 


80 Chapter 3. Batch experiments 

 bioaugmentation to enhance PCE dissolution at Dover AFB National Test Site, Remediation, 18 , 5–17. 

L ̈offler, F. E., J. R. Cole, K. M. Ritalahti, and J. M. Tiedje (2003), Diversity of dechlorinating bacteria, in Dehalogenation. Microbial processes and environmental applications, edited by M. M. H ̈aggblom and I. D. Bossert, first ed., chap. 3, pp. 53–87, Kluwer Academic Publishers, Boston. 

Luong, J. H. T. (1987), Generalization of Monod kinetics for analysis of growth data with substrate inhibition, Biotechnology and Bioengineering, 29 , 242– 248. 

Major, D. W., M. L. McMaster, E. E. Cox, E. A. Edwards, S. M. Dworatzek, E. R. Hendrickson, M. G. Starr, J. A. Payne, and L. W. Buonamici (2002), Field demonstration of successful bioaugmentation to achieve dechlorination of tetrachloroethene to ethene, Environmental Science and Technology, 36 , 5106–5116. 

Maym ́o-Gatell, X., V. Tandoi, J. M. Gossett, and S. H. Zinder (1995), Characterization of an H 2 -utilizing enrichment culture that reductively dechlorinates tetrachloroethene to vinyl chloride and ethene in the absence of methanogenesis and acetogenesis, Applied and Environmental Microbiology, 61 , 3928– 3933. 

Neidhardt, C. F., and E. Umbarger (1996), Chemical composition of escherichia coli, in Escherichia coli and Salmonella: cellular and molecular biology, edited by F. C. Neidhardt, R. Curtiss III, J. L. Ingraham, E. C. C. Lin, K. B. Low, B. Magasanik, W. S. Reznikoff, M. Riley, M. Schaechter, and H. E. Umbarger, 2 ed., pp. 13–16, ASM Press, Washington, D.C. 

Nielsen, R. B., and J. D. Keasling (1999), Reductive dechlorination of chlorinated ethene DNAPLs by a culture enriched from contaminated groundwater, Biotechnology and Bioengineering, 62 , 160–165. 

Payne, F. C., S. S. Suthersan, D. K. Nelson, G. Suarez, I. Tasker, and N. Akladiss (2006), Enhanced reductive dechlorination of PCE in unconsolidated soils, Remediation, 17 , 5–21. 

Schwille, F. (1998), Dense chlorinated solvents in porous and fractured media. Model experiments, Lewis Publishers, Chelsea, Michigan. 


Bibliography 81 

Sharma, P. K., and P. L. McCarty (1996), Isolation and characterization of a facultatively aerobic bacterium that reductively dehalogenates tetrachloroethene to cis-1,2-dichloroethene, Applied and Environmental Microbiology, 62 , 761– 765. 

Smatlak, C. R., J. M. Gossett, and S. H. Zinder (1996), Comparative kinetics of hydrogen utilization for reductive dechlorination of tetrachloroethene and methanogenesis in an anaerobic enrichment culture, Environmental Science and Technology, 30 , 2850–2858. 

Sung, Y., K. M. Ritalahti, R. A. Sanford, J. W. Urbance, S. J. Flynn, J. M. Tiedje, and F. E. L ̈offler (2003), Characterization of two tetrachloroethene-reducing, acetate-oxidizing anaerobic bacteria and their description as Desulfuromonas michiganensis sp. nov., Applied and Environmental Microbiology, 69 , 2964– 2974. 

Tandoi, V., T. D. DiStefano, P. A. Bowser, J. M. Gossett, and S. H. Zinder (1994), Reductive dehalogenation of chlorinated ethenes and halogenated ethanes by a high-rate anaerobic enrichment culture, Environmental Science and Technology, 28 , 973–979. 

Van der Werf, A. W., M. J. C. Henssen, C. Hubach, H. Van Vilsteren, and C. Haasnoot (2004), Total Concept Evenblij: From orientation to implementation, Tech. Rep. SV-058, Netherlands Centre for Soil Quality Management and Knowledge Transfer (SKB), Gouda. 

Wymore, R. A., T. W. Macbeth, R. J. S., L. N. Peterson, L. O. Nelson, K. S. Sorenson Jr., N. Akladiss, and I. Tasker (2006), Enhanced anaerobic bioremediation in a DNAPL residual source zone: test area north case study, Remediation, 17 , 5–22. 

Yang, Y., and P. L. McCarty (2000), Biologically enhanced dissolution of tetrachloroethene DNAPL, Environmental Science and Technology, 34 , 2979– 2984. 

Yu, S., and L. Semprini (2004), Kinetics and modeling of reductive dechlorination at high PCE and TCE concentrations, Biotechnology and Bioengineering, 88 (4), 451–464. 



## Chapter 4 

# Uncertainty in parameter 

# estimation on a data set on 

# dechlorination of 

# tetrachloroethylene in batch 

# experiments. 

## 1 

## Abstract 

A model was developed to investigate the results of batch experiments performed with a dechlorinating microbial assemblage over a range of initial PCE concentrations. Experimental results revealed that with increasing PCE concentrations, dechlorination was incomplete and stalled at initial PCE concentrations higher than 0.5 mM. Moreover, results of triplicate batch experiments did not always show the same pattern. The constructed model included kinetic and thermodynamic constraints for dechlorination, fermentation, and biomass growth. Dechlorination rate parameters were estimated for one batch experiment by fitting the chlorinated ethene concentrations with the SCEM-UA algorithm. Application of the obtained parameters to other batch experiments did not result in a good fit with the experimental results. The model showed a high sensitivity for the rate of competitive inhibition between chlorinated ethenes, reaction rates of electron donor fermentation related to electron donor consumption by competing processes and 

(^1) This chapter has been prepared for submission as part of an article with Heimovaara, T.J. 


84 Chapter 4. Uncertainty in parameter estimation batch experiments 

initial biomass concentrations. A slight change in initial conditions will result in very different chlorinated ethene concentrations. This leads to the conclusion that in field conditions, changes in initial conditions can prevent biological processes to proceed at maximum degradation rates. 

## 4.1 Introduction 

Application of bioremediation to PCE source zones is a widely applied technique to remove PCE pollution (Christ and Abriola, 2007, Amos et al., 2008). Reductive dechlorination of PCE proceeds stepwise via TCE, cDCE, VC, to ethene where in each step a proton is incorporated into the molecule and chloride is released. This is a redox reaction in which the chlorinated ethenes are the electron acceptors. Extensive research has been done on dechlorination of PCE at low concentrations (Holliger et al., 1999, L ̈offler et al., 2003). In source zones, however, PCE is present as pure NAPL, either in the form of films or small droplets bound by capillary forces or as a pool on an impermeable layer. For dechlorination in source zones, it is relevant to investigate kinetics of dechlorination of high PCE concentrations close to solubility levels which are present in source zones. Previously, batch experiments were performed with a dechlorinating microbial assemblage over a range of initial PCE concentrations (see Chapter 3). Results revealed that with increasing PCE concentrations, dechlorination was incomplete and even stalled at initial PCE concentrations of 0.5 mM. Moreover, results of triplicate batch experiments did not always show the same dechlorination pattern. However, there are no reasons to assume that the results of the triplicate experiments are wrong as the procedure was identical. To investigate the deviation in experimental results and the incomplete dechlorination at higher initial PCE concentration, a model was constructed. Commonly, first-order kinetics are used to simulate PCE dechlorination in field studies (Seagren et al., 1993, Carr et al., 2000), an approach that represents practical situations reasonably well in the case of low PCE concentrations (Clement et al., 2000). Under certain conditions, for example when the dechlorination rate is limited by a lack of electron-donor, first order approaches cannot describe the dechlorination process adequately. It is now well known that dechlorination rates can depend on the concentrations of electron donor, nutrient or dechlorination products. A range of microorganisms are involved in the sequential dechlorination of chlorinated compounds and it appears that it is generally a consortium of organisms that perform various reactions required (Aulenta et al., 2006). To incorporate these types of concentration dependence and competition 


4.1. Introduction 85 

between microorganisms, more complicated relationships are required in models used for describing the sequential dechlorination. It is clear that these models will depend on a large number of parameters which often cannot be obtained by direct means. 

Researchers frequently use the Michaelis-Menten equation to model dechlorination (Nielsen and Keasling, 1999, Haston and McCarty, 1999), where inhibition terms can be included to account for rate controlling substances or toxicity effects. For example, Yu and Semprini (2004) developed two biokinetic models to simulate batch experiments of PCE and TCE dechlorination. They determined maximum dechlorination rates and half-saturation constants for two different mixed cultures for each dechlorination step from PCE to ethene and evaluated inhibition between chlorinated ethenes. One model was based on MichaelisMenten kinetics with competitive inhibition among chlorinated ethenes, while the other model included both competitive and Haldane inhibition at high chlorinated ethene concentrations. All model parameters were obtained from (previously) reported experiments or by fitting the model to experimental data. The model with competitive inhibition simulated experimental results well with PCE concentrations lower that 0.3 mM. However, the experiment with higher initial PCE concentrations was described better by the model with the combined competitive and Haldane inhibition. Later, they conducted a similar study to evaluate inhibition between chlorinated ethenes (Yu et al., 2005). For the competitive inhibition constants, they used the same values as the half-saturation constants. But, they concluded that much higher values would be required in order to simulate the less chlorinated ethene inhibition effect on the more chlorinated ethene. 

Michaelis-Menten equations including inhibition terms are frequently used in combination with the incorporation of various microbial groups as well. Some studies concluded that the initial distribution of biomass can have a large impact on the extent of dechlorination (Lee et al., 2004). The common understanding is that dechlorination of PCE to cDCE can be performed by a large variety of anaerobic bacteria but the following steps are performed by only a selective group of organisms (He et al., 2003, Cupples et al., 2003). Many dechlorinators have been reported to use molecular hydrogen as their main electron donor (Maym ́o-Gatell et al., 1995, Fennell et al., 1997, DiStefano et al., 1992, Smatlak et al., 1996), which is a result of fermentation of organic substrates by fermentative organisms. Fennell and Gossett (1998) described electron donor fermentation using Michaelis-Menten kinetics in which they added a thermodynamic constraint. In their approach, the rate of donor degradation decreases when product formation begins to thermodynamically limit the fermentation. In addition, competition for 


86 Chapter 4. Uncertainty in parameter estimation batch experiments 

hydrogen gas was added as well. The main competitors for the hydrogen gas were methanogens and acetogens. The most comprehensive numerical model has been developed by Christ and Abriola (2007) which was verified by comparison to results from column experiments by Yang and McCarty (2002). The model accounted for dissolution and dechlorination of PCE using Monod kinetics including hydrogen thresholds and competitive inhibition. Four bacterial groups and eight species were included to model bacterial growth and competition between populations for electron donor. Kinetic coefficients and initial biomass concentrations were taken from a recent study that used the same culture (Lee et al., 2004). Because of the large number of processes involved in the dechlorination of mixed cultures, the modelling is not an easy task. The culture should be well characterized or a large amount of component concentrations should be measured to estimate parameters and to determine relevant processes. Many data sets are available, but often these parameters have not been measured. Nevertheless, application of comprehensive biodegradation models to these data sets can provide information on the relevance of various processes and qualify the conceptual model. Recently, we performed a series of batch experiments in triplicate with a range of initial PCE concentrations. We found that differences in results among triplicates and with increasing initial PCE concentration. To investigate our data set, we constructed a model based on the above-mentioned kinetic and thermodynamic considerations for PCE dechlorination, including electron donor fermentation and biomass growth. The goal was to describe experiments with various initial PCE concentrations (up to solubility) with one conceptual model. Therefore, we optimized unknown model parameters by fitting the results to data from one batch experiment and used those model parameters to describe the other experiments in our data set. This model should allow us to characterize our dechlorinating microbial assemblage and to determine what the most important processes are. 

## 4.2 Experimental data 

The experimental data used for estimation and comparison with the model were reported in section 3. The microbial dechlorinating assemblage came from the effluent of a bioreactor at a contaminated site and was able to dechlorinate PCE completely. The batch experiments (120 ml bottles with 100 ml liquid) were enriched with PCE, lactate as electron donor, acetate as carbon source, nutrients, 


4.3. Model development 87 

and trace elements (see Table 4.1). Initial PCE concentrations, C 0 , ranged from 0.1 mM to the solubility limit. The bottles were run at 20 °C on an orbital platform shaker. Regular measurements of chlorinated ethene concentrations were performed during 180 days by taking samples of the liquid from the bottles. These were the only measurements performed and the kinetics of the dechlorinating microbial assemblage was unknown. 

 Table 4.1: Initial conditions in the batch experiments. 

 PCE 3 x 0.1; 3 x 0.2; 3 x 0.3; 3 x 0.4; 3 x 0.5; 3 x 0.6; 3 x 0.7; 3 x 0.8; 2 x 0.9; 5 x 1.2 mM Na-acetate 2 mM K-L-lactate 5 mM NH 4 Cl 1.6 mM KH 2 PO 4 0.37 mM NaHCO 3 16.4 mM Na 2 S 0.2 mM Resazurin 1 mg l−^1 Trace element solution 1 ml l−^1 Pressure 1 atm N 2 /CO 2 gas (99.5 vol%/0.5 vol%) pH 7.5 

PCE dechlorination was complete in two batches with C 0 = 0.1 mM. For higher initial PCE concentrations, dechlorination was less complete and even stalled at C 0 values higher than 0.5 mM. In Appendix A, results of the six lowest initial PCE concentrations are shown. PH measurements, over the course of the experiment, showed that neutral conditions remained. In bottles with C 0 lower than 0.3 mM PCE, a pressure increase was observed in the bottles. This could have been caused by the formation of methane by methanogenic bacteria present in the microbial assemblage. This is confirmed by the appearance of methane peaks on the gas chromatogram after 25 days for bottles with C 0 lower than 0.3 mM. 

## 4.3 Model development 

The model was implemented in Matlab R2007b and consisted of a kinetic and an equilibrium module. Each time step, changes in aqueous phase concentrations 


88 Chapter 4. Uncertainty in parameter estimation batch experiments 

due to kinetic reactions were calculated, after which equilibrium partitioning between aqueous, gas, and solid phase was performed. The kinetic part of the numerical model was based on the approach developed by Mora-Naranjo et al. (2004) and improved by Reichel et al. (2007). They modelled the chemical and biological reaction processes in municipal landfills. Oxidation half reactions were combined to obtain dissimilatory and assimilatory redox reactions. These redox reactions were combined using yield coefficients. The reaction kinetics included several functions to limit the degradation rate. A detailed explanation of the mathematical implementation of the matrices and vectors is given in Appendix B. The approach to calculate thermodynamic equilibrium was described by Bethke (2008). It is based on a Morel-tableau for defining reactions in the system (Morel and Hering, 1993) and the Newton-Raphson method for calculating the species distribution at thermodynamic equilibrium (Carrayrou et al., 2002). The Moreltableau gives the stoichiometry coefficients and the equilibrium constants for the formation of each species from a set of master-species. The equilibrium model allows for aqueous, gaseous, and solid species. Activity coefficients are used to correct for activity of aqueous phase species, in order to correct for deviations from the ideal system. The model can simulate systems with a fixed gas volume or a fixed gas pressure. For solid species, a saturation index is calculated to determine undersaturation or supersaturation of precipitated species. The concentration of species in the gas phase is calculated with Henry’s Law, describing the relation between aqueous and gas phase concentration. For a complete description of the chemical equilibrium system, equations are given in Appendix C. 

### 4.3.1 Implementation of sequential PCE dechlorination 

The model was developed in order to simulate sequential PCE dechlorination in batch experiments carried out in closed, 120-ml bottles. The numerical model was implemented to simulate a situation with fixed volume and variable pressure. Sampling of the batch experiments occurred via extraction of liquid from the bottles and resulted in a loss of total mass of components and water volume, which was accounted for in the model. 

Input for kinetic model 

The kinetic model was based on the aqueous phase concentrations. Starting points are the catabolic and anabolic redox reactions which are combined with 


4.3. Model development 89 

 Table 4.2: Catabolic reactions in the kinetic model. 

 C 2 Cl 4 + H 2 −→ C 2 HCl 3 + H+^ + Cl−^ R.1 C 2 HCl 3 + H 2 −→ C 2 H 2 Cl 2 + H+^ + Cl−^ R.2 C 2 H 2 Cl 2 + H 2 −→ C 2 H 3 Cl + H+^ + Cl−^ R.3 C 2 H 3 Cl + H 2 −→ C 2 H 4 + H+^ + Cl−^ R.4 CH 3 CH 2 OCOOH + 2 H 2 O −→ CH 3 COOH + H+^ + HCO− 3 + 2 H 2 R.5 CH 3 CH 2 OCOOH −→ 13 HCO− 3 + 13 H+^ + 23 CH 3 CH 2 COOH+ 1 3 CH^3 COOH^ R.6 CH 3 CH 2 COOH + 3 H 2 O −→ CH 3 COOH + H+^ + HCO− 3 + 3 H 2 R.7 CH 3 COOH + H 2 O −→ CH 4 + HCO− 3 + H+^ R.8 HCO− 3 + H+^ + 4 H 2 −→ CH 4 + 3 H 2 O R.9 2 5 C^5 H^7 NO^2 +^1 1 5 H^2 O^ +^ 2 5 H+^ −→^ CH^3 COOH^ +^ 2 5 NH+ 4 R.10 

the yield coefficient. The catabolic processes involved are dechlorination, electron donor fermentation, methanogenesis, and cell lysis; corresponding reactions are listed in Table 4.2. Dechlorination of PCE to TCE to cDCE to VC and to ethene, occurs via stepwise release of a chloride atom. Three fermentation reactions are taken into account: fermentation of lactate to acetate, lactate to acetate and propionate, and propionate to acetate. For a large part, these equations control the supply of the most important electron donor, hydrogen. Methanogenesis can be performed with acetate or carbon dioxide as carbon source. Lysis of (dead) biomass will result in the production of acetate. An average element composition of C 5 H 7 NO 2 is assumed for biomass. There are six microbial groups in the model for which the stoichiometry of the decay reactions are identical. Therefore, the decay or lysis reaction of each group is expressed by reactions R.10 to R.15 with identical stoichiometry. These six microbial populations are: a PCE-to-cDCE dechlorinator (reactions R.1 and R.2 shown in Table 4.2), a cDCE-to-ethene dechlorinator (reactions R.3 and R.4), a lactate fermentor for reactions R.5 and R.6, a propionate fermentor for reaction R.7, a methanogen using acetate for reaction R.8, and a methanogen using bicarbonate for reaction R.9. Their growth is expressed in their anabolic reaction, see Table 4.3, and is dependent on which carbon source is used. Reaction B.1 models biomass generation from bicarbonate in reactions R.1 to R.4 and R.9, reaction B.2 from lactate in R.5 and R.6, reaction B.3 from propionate in R.7, and reaction B.4 from acetate in R.8. The yield coefficients for microbial biomass growth (mol mol−^1 ) are calculated from the anabolic and catabolic growth requirement of an organism (Harris and Arnold, 1995, Rittmann and McCarty, 2001). The anabolic reactions (B) are 


90 Chapter 4. Uncertainty in parameter estimation batch experiments 

 Table 4.3: Anabolic reactions in the kinetic model. 

 1 35 H+^ + 2 HCO− 3 + 4 H 2 + 25 NH+ 4 −→ 25 C 5 H 7 CNO 2 + 5 15 H 2 O B.1 

(^25) NH 4 + + 23 CH 3 CH 2 OCOOH −→ 25 C 5 H 7 NO 2 + 1 15 H 2 O + 25 H+ (^) B.2 (^47) CH 3 CH 2 COOH + 27 HCO− 3 + 25 NH 4 + (^) −→ 354 H+ (^) + 1 15 H 2 O + 25 C 5 H 7 NO 2 B.3 (^25) NH+ 4 + CH 3 COOH −→ 25 C 5 H 7 NO 2 + 1 15 H 2 O + 25 H+ (^) B.4 combined with the catabolic reactions (R), taking into account the yield coefficient, to obtain the metabolic reactions. Kinetic degradation rates are based on these metabolic reactions. The reaction kinetics are implemented as a maximum degradation rate constant, μmax, multiplied by several environmental factors that limit the biodegradation rate. The factors used include a pH optimum, fpH, Michaelis-Menten kinetics with competitive inhibition fMM, and a thermodynamic constraint, Φ. As dechlorination is an acidifying process, biological reactions are inhibited at low pH values. Theoretically, high pH values are not optimal for biological processes either. Therefore, the pH dependency is assumed to follow the approach from Henze et al. (1995), with a optimum pH: fpH = kpH kpH + (^1010) pHoptpH 1 + 10 pHopt 2 10 pH^ −^2 

#### (4.1) 

where kpH is a system constant, equal to 500 (Reichel et al., 2007) and pHopt 1 is 6 and pHopt 2 is 8. 

The dependence on the electron acceptor, donor, and other required species for the reaction to occur, for example ammonium, are implemented via the MichaelisMenten relation (see also Appendix B): 

 fMM = 

#### CEA 

 KEAm + CEA 

#### CED 

 KmED + CED 

#### CNH 

 + 4 

 K NH+ 4 m +^ CNH 

#### + 4 (4.2) 

Values or Km fr various species are listed in Table 4.4. If competitive inhibition is to be incorporated, then the half-saturation constant, Km, should be replaced by K meff (Cornish-Bowden, 1995): 

 Keff m = Km(1 + 

#### CI 

#### KI 

#### ) (4.3) 


4.3. Model development 91 

where CI [M/L^3 ] is the concentration of the inhibitor and KI [M/L^3 ] is the inhibition coefficient of the competitive inhibitor. This formulation is especially suitable for describing the inhibition of dechlorination of one chlorinated ethene by another (Yu and Semprini, 2004, Cupples et al., 2004, Yu et al., 2005, Chu et al., 2004, Lee et al., 2004). Which chlorinated ethene is inhibiting another, is highly dependent on the microorganisms involved. Inspection of the experimental data showed that the most plausible assumption for the dechlorinating microbial assemblage used is that VC formation was inhibited by PCE and ethene formation was inhibited by cDCE in our experiments. A thermodynamic constraint on the rate of a reaction was included following the approach by Fennell and Gossett (1998): 

 Φ = 1 − exp 

#### ( 

 ∆Grxn − ∆Gcritical RT 

#### ) 

#### (4.4) 

where R is is the universal gas constant (8.314 J K−^1 mol−^1 ), T is the temperature (K), ∆Gcritical is -19 kJ mol−^1 and ∆Grxn is the free energy available from the reaction at a given time. For each time step, the free-energy change of the reactions were calculated using the aqueous phase concentrations and the free-energy change under standard-state conditions, ∆G◦^ (listed in Tables 4.4 and 4.5): 

 ∆Grxn = ∆G◦^ + RT ln( [products] Cdonor[other reactants] ) 

#### (4.5) 

If the reaction could occur thermodynamically, the reaction rate was not inhibited and the thermodynamic factor was set equal to unity Otherwise, when there is thermodynamic limitation on the reaction, the reaction rate was lowered by the thermodynamic factor which is between 0 and 1. 


92 Chapter 4. Uncertainty in parameter estimation batch experiments 

Table 4.4: Parameter values for species in the kinetic model (Lide, Internet Version 2008, Yaws, Internet Version 2003). 

 Species Mwt ∆G◦^ Km Cini kJ mol−^1 mol l−^1 mol l−^1 C 2 Cl 4 165.82 27.59 1 · 10 −^5 in Equil C 2 HCl 3 131.38 25.41 1 · 10 −^5 in Equil C 2 H 2 Cl 2 96.94 27.8 1 · 10 −^5 in Equil C 2 H 3 Cl 62.49 59.65 1 · 10 −^5 in Equil C 2 H 4 28.05 81.43 in Equil CH 3 COOH 60.05 -382.9 1 · 10 −^5 in Equil CH 3 CH 2 COOH 74.08 -366.7 1 · 10 −^5 in Equil CH 3 CH 2 OCOOH 90.07 -516 1 · 10 −^5 in Equil H+^ 1.01 0 in Equil HCO− 3 61.01 -586.8 1 · 10 −^5 in Equil H 2 2.02 17.73 1 · 10 −^5 in Equil NH+ 4 18.04 -79.37 1 · 10 −^5 in Equil CH 4 16.04 -50.81 in Equil Cl−^ 35.45 -131.2 in Equil H 2 O 18.04 -237.18 55.65 C 5 H 7 NO 2 -A 113.11 -166.04 1 · 10 −^5 0.0001 C 5 H 7 NO 2 -B 113.11 -166.04 1 · 10 −^5 0.0001 C 5 H 7 NO 2 -C 113.11 -166.04 1 · 10 −^5 0.001 C 5 H 7 NO 2 -D 113.11 -166.04 1 · 10 −^5 0.001 C 5 H 7 NO 2 -E 113.11 -166.04 1 · 10 −^5 0.001 C 5 H 7 NO 2 -F 113.11 -166.04 1 · 10 −^5 0.001 


4.3. Model development 93 

Table 4.5: Parameter values for reactions in the kinetic model (Lide, Internet Version 2008, Yaws, Internet Version 2003). 

 Reaction ∆G◦^ Yield μmax kJ mol−^1 day−^1 R.1 -151.61 0.058 par(1) R.2 -145.55 0.057 par(2) R.3 -119.11 0.053 par(3) R.4 -126.69 0.054 par(4) R.5 56.12 0.0001 0.001 R.6 -62.9 0.049 0.001 R.7 178.53 0.0001 0.001 R.8 -1.27 0.027 0.001 R.9 -230.21 0.057 0.001 R.10 to R.15 0 0 0.0001 

Input for equilibrium model 

All species in the redox reactions were included in the equilibrium model (see Tableau in Table 4.6) to account for acid-dissociation and heterogenous reactions. Acid-dissociation constants were written as a formation reaction and values of 

the formation constants, logK (^) f orm, are also shown in Table 4.6. Mass transfer between the aqueous and gas phases were incorporated in the model via Henry’s Law constants, logKH , for the chlorinated ethenes, ethene, methane, hydrogen and carbondioxide. 


94 Chapter 4. Uncertainty in parameter estimation batch experiments 

 Table 4.6: 

 Tableau for the system involving PCE dechlorination and electron donor fermentation with formation and Henry constants 

 (Lide, Internet Version 2008, Yaws, Internet Version 2003).^ Species 

 HCO− 3 

 H+ 

 H 2 

 CH 4 

 C 2 Cl 4 

 C 2 HCl 3 

 C 2 H 2 Cl 2 

 C 2 H 3 Cl 

 C 2 H 4 

 CH 3 COOH 

 CH 3 CH 2 COOH 

 CH 3 CH 2 OCOOH 

 PO^34 − 

 Na+ 

 Cl− 

 NH+ 4 

 Ca^2 + 

 N 2 

logK (^) f orm logKH (mol l−^1 atm−^1 ) HCO − 3 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 +H 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 H^2 (g) 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -3.11 CH 4 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -2.85 C^2 Cl 4 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -1.43 C^2 HCl 3 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 -1.06 C^2 H 2 Cl 2 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 -0.87 C^2 H 3 Cl^ 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 -1.35 C^2 H 4 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 -2.32 CH COOH 3 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 CH CH 3 COOH 2 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 CH CH 3 OCOOH 2 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 PO 3 − 4 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 Na +^ 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 −Cl 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 NH + 4 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 Ca 2 +^ 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 N^2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 -3.18 CO 2 − 3 1 -1^ 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 10.34 0 CO (g) 2 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -6.36 -1.47 CH COO 3 −^ 0 -1^ 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 2.36 0 CH CH 3 COO 2 −^ 0 -1^ 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 4.87 0 CH CH 3 OCOO 2 −^ 0 -1^ 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 3.86 0 HPO 2 − 4 0 1 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 -12.34 0 H^2 PO − 4 0 2 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 -19.55 0 H^3 PO 4 0 3 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 -21.70 0 CaCO (s) 3 1 -1^ 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 1.94 0 Initial conc (mol l −^1 ) 1.64· 10 −^2 7.81· 10 −^4 1 · 10 −^12 1 · 10 −^12 par(7) 1 · 10 −^12 1 · 10 −^12 1 · 10 −^12 1 · 10 −^12 2 · 10 −^3 1 · 10 −^12 5 · 10 −^3 3.7· 10 −^4 1.68· 10 −^2 1.6· 10 −^3 1.6· 10 −^3 1 · 10 −^12 8.13· 10 −^3 

- 

- 


4.4. Results and discussion 95 

### 4.3.2 Inverse modelling 

Numerical simulations are performed to calculate aqueous phase concentrations of all components. In total, seven parameters were estimated, which included four maximum degradation rates, μmax, for reactions R.1 to R.4 (listed in Table 4.2), two competitive-inhibition constants, and the initial concentration of PCE. These parameters were found by fitting the chlorinated ethene concentrations to data from the batch experiment with initial PCE concentration of 0.1 mM. The parameters in the model were optimized with the shuffled complex evolution Metropolis algorithm (SCEM-UA). This algorithm is based on locating the global optimum in the parameter space and determines the probability functions of all parameters in the vicinity of the global optimum (Vrugt et al., 2003)). 

## 4.4 Results and discussion 

The model allowed for flexibility in the choice of the degradation kinetics. If first-order kinetics were applied, observed chlorinated ethene concentrations in batch experiments could not be simulated well, especially not beyond cDCE. First-order kinetic degradation resulted in production of the daughter product as soon as the mother product was available. In experiments, this was not the case for cDCE, where a built up took place after which dechlorination only occurred when PCE concentrations were low enough. Similarly, VC dechlorination was inhibited by the presence of cDCE. This means that the simulation with first-order kinetics was not optimal because important inhibition factors were missing. With the inclusion of competitive inhibition for cDCE by PCE and cDCE by VC, model simulations more closely matched the experimental results. For the batch experiment with C 0 = 0.1 mM, dechlorination parameters were estimated with SCEM-UA algorithm. Figure 4.1 shows the measured and simulated chlorinated ethene concentrations for this batch experiment after all seven parameters were optimized. Simulated results are based on the mean parameter values, with their 95% confidence intervals determined from 1000 realizations sampled from posteriori-determined distributions of the parameters. In general, the model could accurately describe the measurements. The SCEM-UA derived mean values and standard deviations of the estimated parameters are given in Table 4.7. Most of the parameters in the Redox-Equilibrium model were well defined by calibration against measured chlorinated ethene concentrations. Hence, the posterior parameter ranges were narrow for most of the model parameters, indicating that the measured chlorinated ethene concentration data set contains sufficient informa


96 Chapter 4. Uncertainty in parameter estimation batch experiments 

tion to identify seven model parameters. 

 0 20 40 60 80 100 120 140 160 180 0 

 0.2 

 0.4 

 0.6 

 0.8 

 1 

 1.2 x 10 

 −4 

 Time (days) 

 Aqueous concentration (mol/l) 

 PCE TCE cDCE VC Ethene Exp.PCE Exp.TCE Exp.cDCE Exp.VC 

Figure 4.1: Concentrations of PCE, cDCE, VC, and ethene from model generated with optimized parameter (lines) and experimental measurements (points). 

Figure 4.2 presents a scatter plot of values for the maximum cDCE dechlorination rate versus the constant of inhibition by PCE, generated with the SCEMUA algorithm after convergence to a stationary posterior distribution. Obviously, these two parameters are highly correlated. This means that the individual parameter values could not be estimated uniquely. The scatter plots for all other combinations of parameters show a cloud of points, indicating that these parameters were not correlated and parameter values were uniquely defined. The estimated parameters from the batch experiment with C 0 = 0.1 mM were assumed to be representative for systems in which the dechlorinating microbial assemblage was present. In order to investigate this assumption, other batch experiments were simulated with the estimated parameter values. The batch experi


4.4. Results and discussion 97 

Table 4.7: Parameter values after optimization against batch experiment with 0.1 mM PCE. 

 Parameter Mean Standard deviation Maximum PCE dechlorination rate (day−^1 ) 7.3· 10 −^3 8.07· 10 −^4 Maximum TCE dechlorination rate (day−^1 ) 1.46· 10 −^2 3.1· 10 −^3 Maximum cDCE dechlorination rate (day−^1 ) 7.68· 10 −^4 2.83· 10 −^4 Maximum VC dechlorination rate (day−^1 ) 5.75· 10 −^4 7.44· 10 −^5 Inhibition constant (mol l−^1 ) 4.53· 10 −^8 3.52· 10 −^8 Inhibition constant (mol l−^1 ) 3.84· 10 −^4 2.28· 10 −^4 Initial PCE concentration (mol l−^1 ) 1.13· 10 −^4 2.12· 10 −^6 

 −3.4 −3.3 −3.2 −3.1 −3 −2.9 −2.8 −2.7 −2.6 

 −8 

 −7.5 

 −7 

 −6.5 

Log constant of PCE inhibition of cDCE dechlorination Log maximum cDCE dechlorination rate (mol l−1 (^) day−1) Figure 4.2: Scatter plot of SCEM-UA generated values for the maximum cDCE dechlorination rate and its inhibition constant by PCE. 


98 Chapter 4. Uncertainty in parameter estimation batch experiments 

ment with C 0 = 0.1 mM was performed in triplicate. Estimated parameters could be used to simulate one of these experiments well, but not the third one, where cDCE dechlorination did not occur at all. For higher initial PCE concentrations, more deviations between simulation and experimental results were found. For example, results for the batch experiment with C 0 = 0.2 mM are shown in Figure 4.3. Simulated time frames of PCE and TCE dechlorination were consistent with experimental results, but cDCE dechlorination proceeded completely to VC and ethene whereas in the experiment, cDCE dechlorination stalled. With even higher initial PCE concentrations, cDCE dechlorination probably did not occur as no VC was detected (not shown). 

 0 20 40 60 80 100 120 140 160 180 

 0 

 1 

 2 

 x 10−4 

 Time (days) 

 Aqueous concentration (mol/l) 

 PCE TCE cDCE VC Ethene Exp.PCE Exp.TCE Exp.cDCE Exp.VC 

Figure 4.3: Simulated (lines) and experimental (points) chlorinated ethene concentrations for a batch experiment with initially 0.2 mM PCE. Simulations are performed with parameter values estimated from a batch experiment with initially 0.1 mM PCE. 

The stalled dechlorination of cDCE in the batch experiment with 0.2 mM PCE was probably the result of electron donor depletion caused by methanogenesis. 


4.4. Results and discussion 99 

Indeed, in experiments with low C 0 values, an overpressure was developed, most probably caused by the production of methane. This assumption is supported by reports that methanogenesis is inhibited by higher PCE concentrations (approximately 0.3 mM) in batch experiments (DiStefano et al., 1991, Smatlak et al., 1996, Fennell et al., 1997, Nielsen and Keasling, 1999, Yang and McCarty, 2000) but not by low PCE concentrations. Methanogenesis was included as the competitor for electron donor in our model (reaction R.9) and it is an important reaction controlling the electron donor concentration. In our simulation of C 0 = 0.1 mM, the methane production was increased in order to decrease the available electron donor for dechlorination. On the other hand, because the chlorinated ethene concentrations had to match experimental results, also the rate of electron donor production was increased. The two reactions that produce hydrogen are R.5 and R.7, from which reaction R.7 was thermodynamically limited and, thus, not important for the electron donor concentration. Thus, manually, the electron donor production and consumption by R.5 and R.9 were changed in order to increase methane production and at the same time match the measured chlorinated ethene concentrations simulating the batch experiment of initially 0.1 mM PCE. Moreover, a thermodynamic preference of dechlorinators above methanogens exist (Fennell et al., 1997, Ballapragada et al., 1997, Carr and Hughes, 1998, Fennell and Gossett, 1999, Carr and Hughes, 1999), which make the influence of the processes on each other complex. To increase methane production with the same chlorinated ethene concentrations, the maximum degradation rate of R.5 was set to 0.0025 day−^1 and for R.9 to 0.0035 day−^1. The simulation of higher PCE concentrations showed an electron donor limitation which occurred later than observed in the laboratory experiments (see Figures 4.4-ii and -iii). 

The batch experiment with C 0 = 0.2 mM contains probably more information about the reactions controlling the electron donor. By manually fitting maximum degradation rates of R.5 and R.9 to this batch experiment, the fit of simulated to experimental results was much better over all ranges of initial PCE concentrations (see Figure 4.5). However, with 0.1 mM PCE, low concentrations of cDCE remain in the simulation. 

The data set could be fitted with incorporation of competitive inhibition. Moreover, competition of electron donor could be included to model batch experiments with 0.2 and 0.3 mM initial PCE concentration. At higher PCE concentrations, methanogenesis is probably inhibited by PCE. This means that in systems with high PCE concentrations, electron donor consumption by methanogenesis is inhibited and more electron donor is available for PCE. However, in our batch experiments dechlorination did not proceed with C 0 higher than 0.5 mM, although 


100 Chapter 4. Uncertainty in parameter estimation batch experiments 

 0 20 40 60 80 100 120 140 160 180 

 0 

 1 

 2 

 3 

 4 x 10 

 −4 i) 

 PCE TCE cDCE VC Ethene Exp.PCE Exp.TCE Exp.cDCE Exp.VC 

 0 20 40 60 80 100 120 140 160 180 

 0 

 1 

 2 

 3 

 4 x 10 

 −4 

 Aqueous concentration (mol/l) 

 ii) 

 0 20 40 60 80 100 120 140 160 180 0 

 1 

 2 

 3 

 4 x 10 

 −4 

 Time (days) 

 iii) 

Figure 4.4: Simulated (lines) and experimental (points) chlorinated ethene concentrations for a batch experiment with initially i) 0.1 mM PCE, ii) 0.2 mM PCE, and iii) 0.3 mM PCE. Simulations are performed with parameter values estimated from a batch experiment with initially 0.1 mM PCE. 


4.4. Results and discussion 101 

 0 20 40 60 80 100 120 140 160 180 

 0 

 1 

 2 

 3 

 4 x 10 

 −4 i) 

 PCE TCE cDCE VC Ethene Exp.PCE Exp.TCE Exp.cDCE Exp.VC 

 0 20 40 60 80 100 120 140 160 180 

 0 

 1 

 2 

 3 

 4 x 10 

 −4 

 Aqueous concentration (mol/l) 

 ii) 

 0 20 40 60 80 100 120 140 160 180 

 0 

 1 

 2 

 3 

 4 x 10 

 −4 

 Time (days) 

 iii) 

Figure 4.5: Simulated (lines) and experimental (points) chlorinated ethene concentrations for a batch experiment with initially i) 0.1 mM PCE, ii) 0.2 mM PCE, and iii) 0.3 mM PCE. Simulations are performed with parameter values with a manual fit to the batch experiment with initially 0.2 mM PCE. 


102 Chapter 4. Uncertainty in parameter estimation batch experiments 

competition for electron donor was less. Probably, degradation reactions did not proceed by toxicity effects on some of the microorganisms. As mentioned earlier, even modelling of triplicate experiments with the same parameter values was not always possible. This is probably because of the sensitivity of model results to certain parameters. If a given reaction controls the system, results can change significantly due to a small difference in initial conditions. Which reaction proceeds is dependent on the values of the maximum degradation rates and the initial biomass concentration. Therefore, these parameters should be estimated independently. Because these two parameters are multiplied by limiting factors, which depend on other reactions through the component concentrations, the system becomes quite complex. The complexity of the model by the interactions and dependence of reactions on each other, make the model results to change rather fast for some parameters, indicating that some model parameters had a high sensitivity. This can also be an explanation for the large variability found in degradation constants and degradation possibilities. 

## 4.5 Conclusion 

A model was constructed that included kinetic and thermodynamic considerations for dechlorination, fermentation, and biomass growth. The model was used to simulate a series of batch experiments involving high initial PCE concentrations varying for 0.1 mM to solubility limit of 1.2 mM. Although only variations of chlorinated ethene concentrations with time was measured and the concentration of the dechlorinating microbial assemblage was unknown, dechlorination rate parameters could be estimated by fitting with results of the batch experiment with initial PCE concentration, C 0 = 0.1 mM. Subsequent simulations with these parameters for other initial PCE concentrations did not match experimental results. By manually changing initial conditions in the model, results changed drastically. The data set could be fitted with incorporation of competitive inhibition. Moreover, competition of electron donor could be included to model batch experiments with 0.2 and 0.3 mM initial PCE concentration. Without limitations, reactions can proceed at the maximum degradation rate. However, in field situations, the presence of microorganisms, nutrients, and varying conditions can introduce limitations. Specifically, in application of in-situ bioremediation, one should realize that biological processes are controlled by a complex system with all kinds of possible limitations. Future work will include an optimization of degradation rate parameters and initial biomass concentrations to perform a better simulation of experimental re


4.5. Conclusion 103 

sults of different initial PCE concentrations. Through inclusion of results from higher initial PCE concentrations, probably more information will be available about the electron donor consumption and production. 


104 Chapter 4. Uncertainty in parameter estimation batch experiments 

## Bibliography 

Amos, B. K., E. J. Suchomel, K. D. Pennell, and F. E. L ̈offler (2008), Microbial activity and distribution during enhanced contaminant dissolution from a napl source zone, Water Research, 42 , 2963–2974. 

Aulenta, F., M. Majone, and V. Tandoi (2006), Enhanced anaerobic bioremediation of chlorinated solvents: environmental factors influencing microbial activity and their relevance under field conditions, Journal Of Chemical Technology And Biotechnology, 81 (9), 1463–1474, doi:10.1002/jctb.1567. 

Ballapragada, B. S., H. D. Stensel, J. A. Puhakka, and J. F. Ferguson (1997), Effect of hydrogen on reductive dechlorination of chlorinated ethenes, Environmental Science and Technology, 31 , 1728–1734. 

Bethke, C. M. (2008), Geochemical and Biogeochemical Reaction Modeling, Cambridge University Press, New York. 

Carr, C. S., and J. B. Hughes (1998), Enrichment of high-rate PCE dechlorination and comparative study of lactate, methanol, and hydrogen as electron donors to sustain activity, Environmental Science and Technology, 32 , 1817–1824. 

Carr, C. S., and J. B. Hughes (1999), Response to ’comment on ”Enrichment of high-rate PCE dechlorination and comparative study of lactate, methanol, and hydrogen as electron donors to sustain activity”’, Environmental Science and Technology, 33 , 2683–2684. 

Carr, C. S., S. Garg, and J. B. Hughes (2000), Effect of dechlorinating bacteria on the longevity and composition of PCE-containing nonaqueous phase liquids under equilibrium dissolution conditions, Environmental Science and Technology, 34 , 1088–1094. 

Carrayrou, J., R. Mos ́e, and P. Behra (2002), New efficient algorithm for solving thermodynamic chemistry, Environmental and energy engineering, 48 , 894– 904. 

Christ, J. A., and L. M. Abriola (2007), Modeling metabolic reductive dechlorination in dense non-aqueous phase liquid source-zones, Advances in Water Resources, 30 (6-7), 1547–1561, doi:10.1016/j.advwatres.2006.05.024. 

Chu, M., P. K. Kitanidis, and P. L. McCarty (2004), Possible factors controlling the effectiveness of bioenhanced dissolution of non-aqueous phase 


Bibliography 105 

 tetrachloroethene, Advances in Water Resources, 27 (6), 601–615, doi: 10.1016/j.advwatres.2004.03.002. 

Clement, T. P., C. D. Johnson, Y. Sun, G. M. Klecka, and C. Bartlett (2000), Natural attenuation of chlorinated ethene compounds: model development and field-scale application at the Dover site, Journal of Contaminant Hydrology, 42 , 113–140. 

Cornish-Bowden, A. (1995), Fundamentals of enzyme kinetics, Portland Press, London. 

Cupples, A. M., A. M. Spormann, and P. L. McCarty (2003), Growth of a Dehalococcoides-like microorganism on vinyl chloride and cis-dichloroethene as electron acceptors as determined by competitive PCR, Applied and Environmental Microbiology, 69 , 953–959. 

Cupples, A. M., A. M. Spormann, and P. L. McCarty (2004), Comparative evaluation of chloroethene dechlorination to ethene by dehalococcoides-like microorganisms, Environmental Science and Technology, 38 , 4768–4774. 

DiStefano, T. D., J. M. Gossett, and S. H. Zinder (1991), Reductive dechlorination of high concentrations of tetrachloroethene to ethene by an anaerobic enrichment culture in the absence of methanogenesis, Applied and Environmental Microbiology, 57 , 2287–2292. 

DiStefano, T. D., J. M. Gossett, and S. H. Zinder (1992), Hydrogen as an electron donor for dechlorination of tetrachloroethene by an anaerobic mixed culture, Applied and Environmental Microbiology, 58 , 3622–3629. 

Fennell, D. E., and J. M. Gossett (1998), Modeling the production of and competition for hydrogen in a chlorinating culture, Environmental Science and Technology, 32 , 2450–2460. 

Fennell, D. E., and J. M. Gossett (1999), Comment on ”Enrichment of high-rate PCE dechlorination and comparative study of lactate, methanol, and hydrogen as electron donors to sustain activity”, Environmental Science and Technology, 33 , 2681–2682. 

Fennell, D. E., J. M. Gossett, and S. H. Zinder (1997), Comparison of butyric acid, ethanol, lactic acid, and propionic acid as hydrogen donors for the reductive dechlorination of tetrachloroethene, Environmental Science and Technology, 31 , 918–926. 


106 Chapter 4. Uncertainty in parameter estimation batch experiments 

Harris, R. F., and S. M. Arnold (1995), Redox and energy aspects of soil bioremediation, in Bioremediation: Science and applications, edited by H. D. Skipper and R. F. Turco, chap. 4, pp. 55–87, Soil Science Society of America, Madison, WI, SSSA Special Publication 43. 

Haston, Z. C., and P. L. McCarty (1999), Chlorinated ethene half-velocity coefficients (Ks) for reductive dehalogenation, Environmental Science and Technology, 33 , 223–226. 

He, J., K. M. Ritalahti, M. R. Aiello, and F. E. L ̈offler (2003), Complete detoxification of vinyl chloride by an anaerobic enrichment culture and identification of the reductively dechlorinating population as a Dehalococcoides species, Applied and Environmental Microbiology, 69 , 996–1003. 

Henze, M., P. Harremoes, J. Jansen, and E. Arvin (1995), Wastewater Treatment 

- Biological and chemical processes, Springer Verlag, Berlin. 

Holliger, C., G. Wohlfarth, and G. Diekert (1999), Reductive dechlorination in the energy metabolism of anaerobic bacteria, FEMS Microbiology reviews, 22 , 383–398. 

Lee, I. S., J. H. Bae, Y. R. Yang, and P. L. McCarty (2004), Simulated and experimental evaluation of factors affecting the rate and extent of reductive dehalogenation of chloroethenes with glucose, Journal of Contaminant Hydrology, 74 (1-4), 313–331, doi:10.1016/j.jconhyd.2004.03.006. 

Lide, D. R. (Ed.) (Internet Version 2008), CRC Handbook of Chemistry and Physics, chap. Standard thermodynamic properties of chemical substances, 88th ed., CRC Press/Taylor and Francis, Boca Raton, FL. 

L ̈offler, F. E., J. R. Cole, K. M. Ritalahti, and J. M. Tiedje (2003), Diversity of dechlorinating bacteria, in Dehalogenation. Microbial processes and environmental applications, edited by M. M. H ̈aggblom and I. D. Bossert, first ed., chap. 3, pp. 53–87, Kluwer Academic Publishers, Boston. 

Maym ́o-Gatell, X., V. Tandoi, J. M. Gossett, and S. H. Zinder (1995), Characterization of an H 2 -utilizing enrichment culture that reductively dechlorinates tetrachloroethene to vinyl chloride and ethene in the absence of methanogenesis and acetogenesis, Applied and Environmental Microbiology, 61 , 3928– 3933. 


Bibliography 107 

Mora-Naranjo, N., J. A. Meima, A. Haarstrick, and D. C. Hempel (2004), Modelling and experimental investigation of environmental influences on the acetate and methane formation in solid waste, Waste Management, 24 (8), 763 – 773, doi:DOI: 10.1016/j.wasman.2004.04.006. 

Morel, F. M. M., and J. G. Hering (1993), Principles and applications of aquatic chemistry, Wiley, New York. 

Nielsen, R. B., and J. D. Keasling (1999), Reductive dechlorination of chlorinated ethene DNAPLs by a culture enriched from contaminated groundwater, Biotechnology and Bioengineering, 62 , 160–165. 

Reichel, T., L. K. Ivanova, R. P. Beaven, and A. Haarstrick (2007), Modeling decomposition of MSW in a consolidating anaerobic reactor, Environmental Engineering Science, 24 (8), 1072–1083, doi:10.1089/ees.2006.0230. 

Rittmann, B. E., and P. L. McCarty (2001), Environmental Biotechnology: Principles and Applications, McGraw-Hill, New York. 

Seagren, E. A., B. E. Rittmann, and A. J. Valocchi (1993), Quantitative evaluation of flushing and biodegradation for enhancing in situ dissolution of nonaqueousphase liquids, Journal of Contaminant Hydrology, 12 , 103–132. 

Smatlak, C. R., J. M. Gossett, and S. H. Zinder (1996), Comparative kinetics of hydrogen utilization for reductive dechlorination of tetrachloroethene and methanogenesis in an anaerobic enrichment culture, Environmental Science and Technology, 30 , 2850–2858. 

Stumm, W., and J. J. Morgan (1996), Aquatic chemistry. Chemical equilibria and rates in natural waters, third ed., John Wiley & Sons, Inc, New York. 

Vrugt, J. A., H. V. Gupta, W. Bouten, and S. Sorooshian (2003), A shuffled complex evolution Metropolis algorithm for optimization and uncertainty assessment of hydrologic model parameters, Water Resources Research, 39 , 2101, doi:10.1029/2002WR001642. 

Yang, Y., and P. L. McCarty (2000), Biologically enhanced dissolution of tetrachloroethene DNAPL, Environmental Science and Technology, 34 , 2979– 2984. 

Yang, Y. R., and P. L. McCarty (2002), Comparison between donor substrates for biologically enhanced tetrachloroethene DNAPL dissolution, Environmental Science and Technology, 36 (15), 3400–3404, doi:10.1021/es011408e. 


108 Chapter 4. Uncertainty in parameter estimation batch experiments 

Yaws, C. L. (Ed.) (Internet Version 2003), Yaws’ Handbook of Thermodynamic and Physical Properties of Chemical Compounds., Knovel. 

Yu, S., and L. Semprini (2004), Kinetics and modeling of reductive dechlorination at high PCE and TCE concentrations, Biotechnology and Bioengineering, 88 (4), 451–464. 

Yu, S. H., M. E. Dolan, and L. Semprini (2005), Kinetics and inhibition of reductive dechlorination of chlorinated ethylenes by two different mixed cultures, Environmental Science and Technology, 39 (1), 195–205, doi: 10.1021/es0496773. 


 Appendices 109 

## Appendix A: Results of batch experiments 

 0 50 100 150 200 0 

 0.5 

 1 

 1.5 x 10 

 −4 i) 

 0 50 100 150 200 0 

 1 

 2 

 3 

 4 x 10 

 −4 ii) 

 0 50 100 150 200 0 

 0.5 

 1 

 1.5 x 10 

 −4 iii) 

 0 50 100 150 200 0 

 1 

 2 

 3 

 4 x 10 

 −4 iv) 

 0 50 100 150 200 

 0 

 0.5 

 1 

 1.5 x 10 

 −4 v) 

 0 50 100 150 200 

 0 

 1 

 2 

 3 

 4 x 10 

 −4 

 Time (days) 

 Aqueous concentration (mol/l) 

 vi) 

 PCE TCE cDCE VC 

Figure 6: Experimental results of batch experiments with initial PCE concentration, C 0 = 0.1 mM on the left and C 0 = 0.2 mM on the right. 


 110 Chapter 4. Uncertainty in parameter estimation batch experiments 

 0 50 100 150 200 

 0 

 1 

 2 

 3 

 4 x 10 

 −4 vii) 

 0 50 100 150 200 

 0 

 2 

 4 

 6 x 10 

 −4 viii) 

 0 50 100 150 200 0 

 1 

 2 

 3 

 4 x 10 

 −4 ix) 

 0 50 100 150 200 0 

 2 

 4 

 6 x 10 

 −4 x) 

 0 50 100 150 200 0 

 1 

 2 

 3 

 4 x 10 

 −4 xi) 

 0 50 100 150 200 0 

 2 

 4 

 6 x 10 

 −4 

 Time (days) 

 Aqueous concentration (mol/l) 

 xii) 

 PCE TCE cDCE VC 

Figure 6: Experimental results of batch experiments with initial PCE concentration, C 0 = 0.3 mM on the left and C 0 = 0.4 mM on the right (continued). 


 Appendices 111 

 0 50 100 150 200 

 0 

 2 

 4 

 6 x 10 

 −4 xiii) 

 0 50 100 150 200 

 0 

 2 

 4 

 6 x 10 

 −4 xiv) 

 0 50 100 150 200 

 0 

 2 

 4 

 6 x 10 

 −4 xv) 

 0 50 100 150 200 

 0 

 2 

 4 

 6 x 10 

 −4 xvi) 

 0 50 100 150 200 

 0 

 2 

 4 

 6 x 10 

 −4 xvii) 

 0 50 100 150 200 

 0 

 2 

 4 

 6 

 8 x 10 

 −4 

 Time (days) 

 Aqueous concentration (mol/l) 

 xviii) 

 PCE TCE cDCE VC 

Figure 6: Experimental results of batch experiments with initial PCE concentration, C 0 = 0.5 mM on the left and C 0 = 0.6 mM on the right (continued). 


112 Chapter 4. Uncertainty in parameter estimation batch experiments 

## Appendix B: Kinetic implementation based on redox re

## actions 

The kinetic part of the numerical model was based on the approach developed by Mora-Naranjo et al. (2004) and improved by Reichel et al. (2007). First, the stoichiometric coefficients of the biological degradation processes are inserted into a reaction matrix, MR(m×n), with m being the number of reactions, and n the number of components: 

 MR(m×n) = 

####  

####  

####  

####  

####  

####  

####  

####  

 vR 1 , 1... vR 1 ,i vR 1 ,n .. . 

#### ... 

#### ... 

#### .. 

#### . 

 vRj, 1... 

#### ... 

 vRj, 1 vRm, 1... vRm,i vRm,n 

####  

####  

####  

####  

####  

####  

####  

####  

#### (6) 

Second, the stoichiometric coefficients for biomass growth are inserted into a biomass matrix, MB(m×n), for the biological degradation reactions that are associated with biomass growth. 

 MB(m×n) = 

####  

####  

####  

####  

####  

####  

####  

####  

 vB 1 , 1... vB 1 ,i vB 1 ,n .. . 

#### ... 

#### ... 

#### .. 

#### . 

 vBj, 1... 

#### ... 

 vBj, 1 vBm, 1... vBm,i vBm,n 

####  

####  

####  

####  

####  

####  

####  

####  

#### (7) 

The yield coefficient, Y (^) j, is defined as the ratio between the biomass formed and the limiting substrate consumed. The yield vector, y(m×1), combines the two stoichiometry matrices of reactions and biomass. y(m×1) = 

####  

####  

####  

####  

####  

####  

####  

#### Y 1 

#### .. 

#### . 

Y (^) j Ym 

####  

####  

####  

####  

####  

####  

####  

#### (8) 

This yield vector is used to construct a yield matrix for biomass formation and for substrate and product formation. 

 yB(m×n) = y(m×1) × β(1×n) (9) 

 yR(m×n) = (α(m×1) − y(m×1)) × β(1×n) (10) 


Appendices 113 

where α(m×1) and β(1×n) are vectors where the elements of each of the vectors have the value 1. The overall stoichiometry matrix can than be calculated, here in units of mol: 

 M(m×n) = yR(m×n) ∗ MR(m×n) + yB(m×n) ∗ MB(m×n) (11) 

To combine the stoichiometry matrix with the reaction kinetics, a reaction vector is defined. This vector contains kinetics and environmental influence functions of each reaction. 

 r(m×1) = 

####  

####  

####  

####  

####  

####  

####  

#### R 1 

#### .. 

#### . 

R (^) j Rm 

####  

####  

####  

####  

####  

####  

####  

#### (12) 

with 

R (^) j = φ (^) j ·k (^) j · fMM, j · fpH, j · Φ · f., j ︸ ︷︷ ︸ φ (^) j 

#### (13) 

where φ (^) j is a weighting factor to express the use of limiting substrate in parallel running reactions, k (^) j is the maximum degradation rate for reaction j, fMM, j is the substrate limiting function via the Michaelis-Menten relation (see equation 4.2), fpH, j is a pH limitation (see equation 4.1), and Φ is a thermodynamic constraint (see equation 4.4). More environmental functions, f., j, that modify the maximum degradation rate for non-optimal conditions can be included in reaction 13. Reichel et al. (2007) included the following limiting functions: for other substrates, fS 2 , j; inhibition, fI, j; temperature, fT, j; pH, fpH, j; and water content, fW, j. For the competition between reactions using the same substrate, a weighting factor is introduced. It is assumed that the faster the reaction, the higher its priority to use the limiting substrate available. φ (^) j = φ (^) j ∑m j= 1 φ^ j 

#### (14) 

where φ (^) j is defined as the product of the environmental functions and the maximum degradation rate (see equation 13). Now, the overall stoichiometry matrix can be multiplied with the reaction vector to obtain the reaction matrix, B(m×n): B(m×n) = M(m×n) · (r(m×1) × β(1×n)) (15) The change in concentration of different species involved in the reactions can be 


114 Chapter 4. Uncertainty in parameter estimation batch experiments 

monitored from a process matrix, which is obtained by the sum of the elements of the reaction matrix for all components: 

 B(n×n) with Bi,Λ( j) = 

 ∑^ m 

 j= 1 

 {B 0 ( j(Λ = Λ( j)), i)} (16) 

The yield coefficients are calculated from the assimilatory and dissimilatory growth requirement of an organisms, based on equations given in Harris and Arnold (1995): 

 Yx/s = 

#### 1 

 As/x 

#### = 

#### 1 

 Aas/x + Ads/x 

#### = 

#### 1 

 Nae/x Vae/s +^ 

 NkJ/x VkJ/s 

#### (17) 

where Yx/s is the specific growth yield of biomass x on electron donor substrate s, As/x is the corresponding specific growth requirement which is subdivided into an assimilatory Aas/x and a dissimilatory Ads/x requirement. The assimilatory requirement is expressed as the cell need for available electrons from the electron donor (Nae/x) divided by the available electrons from the electron donor substrate (Vae/s). The dissimilatory requirement is expressed as the energy need of the cells (NkJ/x) divided by the energy value of the electron donor (VkJ/s). 


Appendices 115 

## Appendix C: Equilibrium model 

The mass action law for the reaction of species in solution, Ci, is written with the equilibrium constant, Ki, and the stoichiometric coefficients, ai j, for each 

component, Comp (^) j: Ci = 

#### ∑ 

 j 

ai jComp (^) j (18) log Ci = − log Ki + 

#### ∑ 

 j 

ai j log Comp (^) j (19) [Ci] = 

#### 1 

 Ki 

 N∏comp 

 j= 1 

[Comp (^) j]ai j^ for i = 1 : NC (20) where NComp is the number of species. Precipitated species are incorporated in the model. If the saturation index defined below is larger than one, a mineral is allowed to precipitate. [S Ii] = 

#### 1 

 Kpi 

 N∏comp 

 j= 1 

[Comp (^) j]api j^ = 1 for i = 1 : NCP (21) where NCP is the number of precipitated species. To account for volatile species, the gas phase mass action law is incorporated. [Pi] = 

#### 1 

 KiKHi 

 N∏comp 

 j= 1 

[Comp (^) j]agi j^ for i = 1 : NG (22) where Pi is the partial pressure in the gas phase, KHi is the Henry coefficient, and NG is the number of volatile species. The total mass in the system is a sum of the mass in the liquid, gas and solid phase: T (^) j = Ts j + Tcp j + Tg j (23) 


116 Chapter 4. Uncertainty in parameter estimation batch experiments 

For the liquid and the solid phase, the equation can be expressed as: 

 Ts j = 

#### ∏^ NC 

 i= 1 

 ai j[Ci] (24) 

 Tcp j = 

#### ∏^ NCP 

 i= 1 

 api j[C pi] for j = 1 : Ncomp (25) 

The mass in the gas phase is calculated in two ways, depending on whether the gas phase has a fixed volume or a fixed pressure. For a fixed volume, the number of moles in the gas phase can be calculated from: 

 ngi = 

 PiVtot RT 

#### (26) 

Together with the amount of dissolved species, the mass in the gas phase with a fixed volume becomes: 

 Tg j = 

#### ∏^ NG 

 i= 1 

 agi j[Cgi] + 

#### ∏^ NG 

 i= 1 

 agi j Vtot RT Pi^ 

#### (27) 

A system with a fixed pressure, for example a system open to the atmosphere, has an additional constraint: 

 ∏^ NG 

 i= 1 

 Pi ≤ Ptot which can be written as 

#### 1 

 Ptot 

#### ∏NG 

 i= 1 

 Pi ≤ 1 (28) 

The number of moles of a gas component is equal to the ration of the partial gas pressure over total gas pressure times the total number of moles in the gas phase: 

 ngi = Ngas 

 Pi Ptot 

#### (29) 

In this case, we require an additional master variable, Ngas which needs to be solved. The mass in the gas phase with a fixed pressure is: 

 Tg j = 

#### ∏^ NG 

 i= 1 

 agi j[Cgi] + 

#### ∏^ NG 

 i= 1 

 agi j 

 Ngas Ptot Pi (30) 

The unknowns in these equations are: concentration of the components, Comp (^) j, and solid phase species, C pi, and partial pressures, Pi. Their values at equilibrium 


Appendices 117 

can be found when the objective functions Y (^) j equal zero. For fixed volume: Y (^) j| (^) j=1:Ncomp = −T (^) j + 

#### NC∏ +NG 

 i= 1 

 ai j[Ci] + 

#### ∏^ NCP 

 i= 1 

 api j[C pi] + Vtot RT 

#### ∏^ NG 

 i= 1 

 agi jPi (31) 

and for fixed pressure: 

Y (^) j| (^) j=1:Ncomp = −T (^) j + 

#### NC∏ +NG 

 i= 1 

 ai j[Ci] + 

#### ∏^ NCP 

 i= 1 

 api j[C pi] + 

 Ngas Ptot 

#### ∏NG 

 i= 1 

 agi jPi (32) 

If some species can precipitate, the following objective function is included: 

Y (^) j| (^) j=Ncomp+1:Ncomp+NCP = 1 − S I (^) j−Ncomp (33) For fixed pressure, one more equation is required: Y (^) j| (^) j=Ncomp+NCP+ 1 = ( 

#### ∏^ NG 

 i= 1 

 Pi) − Ptot (34) 

If precipitates can exist, first equilibrium is searched without taking any precipitated species into account. The saturation index, SI, is then calculated. If all SIs are equal or smaller than one, all precipitated species are undersaturated and the calculated equilibrium is accepted. If some SIs are greater than one, some species are supersaturated. The most supersaturated species is then taken into account and a precipitate is formed. This procedure is repeated until all the SIs are equal or smaller than one (Carrayrou et al., 2002). 

To account for a non-ideal systems, the activities are corrected using the relationship by Davies (Stumm and Morgan, 1996): 

 ln(γi) = −Az^2 i 

#### √ 

#### I 

#### 1 + 

#### √ 

#### I 

 − bI) (35) 

with A = 1. 82 · 106 (wT )−^3 /^2 (36) 

and the ionic strength as: 

 I = 

#### 1 

#### 2 

#### ∏ 

 i 

 [Ci]z^2 i (37) 

 The Newton-Raphson method is used to minimize the objective function. 


118 Chapter 4. Uncertainty in parameter estimation batch experiments 

 Table 8: Jacobian matrix. 

 Compk C pk Ngas 

Mass balance Znj,k| (^) kj==1:1:NNcompcomp Znj,k| (^) kj==1:NNcompcomp +1:Ncomp +NCP Znj,k| (^) kj==1:NNcompcomp +NCP+ 1 Saturation index Znj,k| (^) kj==N1:compNcomp^ +1: Ncomp^ +NCP Gasphase Znj,k| (^) kj==1:1:NNcompcomp^ + NCP^ +^1 Starting with initial concentrations, the residual vector and the gradient matrix, Jacobian, are calculated. The Jacobian, Z (^) j,k, is a square matrix which is filled according to Table 8. As the objective functions are different for fixed pressure or fixed volume, also the Jacobian matrix is different for these two approaches. Then the correction in the vector with the component concentrations are calculated, according to: Compn i +^1 = Compni + ∆Compni (38) The iteration procedure is repeated until the convergence criteria for the objective functions are met. 


## Chapter 5 

# Study of DNAPL source zone 

# biodegradation in column 

# experiments. 

## 1 

## Abstract 

In order to investigate the applicability of bioremediation of tetrachloroethylene (PCE) near source zones, we carried out a set of column experiments involving biodegradation of PCE by a dechlorinating microbial assemblage and analyzed these with a numerical model. In three different setups in eight columns, biodegradation of dissolved, residual, and pooled PCE was investigated. Biodegradation in columns with dissolved PCE proceeded completely to ethene, with concentrations tested up to 0.6 mM. In columns with residual PCE, cDCE was the main degradation product and we determined that dissolution was five times enhanced in the presence of active dechlorination, which is comparable to bioenhancement factors found in the literature. Mobilization of residual NAPL due to biodegradation was also observed. These experiments were simulated by a model for which biodegradation and dissolution parameters were optimized. Modelling of the column experiments yielded information about the relevance and interplay of biodegradation and dissolution processes. The most important observation was that a better fit with the experimental results was obtained when PCE solubility and/or dissolution rate constant were included in the model. 

(^1) This chapter has been prepared for submission to Journal of Contaminant Hydrology as: Langevoort, M., Hassanizadeh, S.M., Leijnse, A., and Kleingeld, P.J.; Study of DNAPL source zone biodegradation in column experiments. 


120 Chapter 5. Column experiments 

## 5.1 Introduction 

Soil and groundwater pollution with chlorinated solvents, such as tetrachloroethylene (PCE), caused by (accidental) spills in the dry cleaning and metal (degreasing) industries, are present all over the world. These contaminants belong to the group of dense non-aqueous phase liquids (DNAPLs). Their presence in the subsurface poses environmental health risks and sites contaminated with DNAPLs often require remediation. In particular, if the source zone is not removed, a continuous delivery of DNAPL to the groundwater can proceed for decades (Schwille, 1998). Several techniques, such as excavation, pump and treat, co-solvent and surfactant flushing, thermal methods, and chemical oxidation have been employed for DNAPL cleanup with varying success (Abriola, 2005). Site characteristics and economical considerations determine which technique(s) are more suitable. Usually a distinction is made between the source zone, where a DNAPL is present as a separate phase, and the contaminant plume, where DNAPL is dissolved in water. One of the most effective and economically feasible methods is in-situ bioremediation. Even at sites where biodegradation is hampered, inhibitory factors can be overcome by the addition of electron donors or nutrients (biostimulation) and/or by the addition of biomass to the subsurface (bioaugmentation). Early bioremediation activities were directed at contamination plumes with generally low contaminant concentrations by natural attenuation (Wiedemeier T. H., 1999). Recently, interest in the application of biodegradation to source zones has been growing, although much higher concentrations of DNAPL components exist in these zones. This may vary from bioaugmentation of a DNAPL source zone (Adamson et al., 2003) to the use of biodegradation, either directly aimed to the source zone (Amos et al., 2008) or as a polishing step after a chemical or physical remediation technology (Christ et al., 2005). There is extensive literature on batch studies of PCE dechlorination. It is commonly found that high concentration of DNAPL is toxic for most bacteria (Aulenta et al., 2006b). Therefore, it is often reported that dechlorination is inhibited when concentration is high (say, more than half the solubility of PCE (see e.g. Duhamel et al. (2002) and Chapter 3). In these studies, the batch solution is almost always placed on a shaker table and continuously stirred, so that there is a complete mixing. Such conditions, however, are not representative of field situations. In fact, in batch experiments where the solution was not stirred, dechlorination occurred even in the presence of a DNAPL phase (see e.g. Amos et al., 2007). This was possible because aqueous phase concentration was kept low (below toxicity limit, which was 0.8 mM in Amos et al. (2007)) by bacteria 


5.1. Introduction 121 

in pores at a small distance from the DNAPL blobs. Similar conditions can be created in a column experiment, which is closer to field conditions than batch experiments. 

Column experiments have been performed on dechlorination of high PCE concentrations, either dissolved (Carr and Hughes, 1998, Isalou et al., 1998) or present as a non-aqueous phase (Yang and McCarty, 2000, 2002, Cope and Hughes, 2001, Brennan et al., 2006). Dechlorination was found to be possible for dissolved PCE at concentrations near or at solubility levels. It was also observed that the mass transfer from the DNAPL to the aqueous phase could be influenced by dechlorination. When (bio)degradation of components in the water phase occurs near the DNAPL source, a large local concentration gradient is created, and thus more components from the DNAPL can dissolve into the water phase. This so-called enhanced dissolution has been investigated in batch (Carr et al., 2000, Amos et al., 2007), column (Cope and Hughes, 2001, Yang and McCarty, 2000, 2002), and 2D flow cell experiments (Sleep et al., 2006, Glover et al., 2007). The overall enhancement factor was found to vary from two (one is no enhancement) (Yang and McCarty, 2000) to thirteen (Glover et al., 2007). This large range in bioenhancement factor is caused by differences in experimental setup, such as bacterial culture, NAPL (mixture), NAPL saturation, and flow regime. For example, bioenhanced dissolution in column experiments was determined by a factor of three to five with a residual PCE saturation of 0.02 (Yang and McCarty, 2000), one with a residual PCE saturation of 0.2, 4.5 with a residual saturation of PCE in hexadecane of 0.2 (Amos et al., 2008), and 1.5 times with a residual PCE saturation of 0.35 (Kaplan et al., 2008). This variability in bioenhancement factors indicate that determined enhancement factors are not necessarily valid for other systems and that a determination of underlining processes is of much more interest. 

Another important effect of bioremediation in DNAPL source zones that has received little attention is the formation of biosurfactants. The secretion of surfactants may change the NAPL dissolution by increasing the apparent solubility of the dissolved NAPL (Kaplan et al., 2008, Clifford et al., 2007, Bai et al., 1997) or change the NAPL mobility by reducing the interfacial tension between the aqueous and NAPL phase (Clifford et al., 2007, Bai et al., 1997). 

Here, we present our study of the dissolution enhancement by dechlorination in residual NAPL zones in a series of column experiments. In three columns, with water flowing upward, a residual zone was created at the top near the exit. Due to this experimental setup, we were able to observe possible mobilization and increases in apparent NAPL dissolution. These column experiments were 


122 Chapter 5. Column experiments 

modelled to obtain process knowledge and parameter values. In order to determine the dechlorination rate, three column experiments were run with dissolved PCE only. Furthermore, two column experiments were run in horizontal position with different flow velocities with PCE in residual and pooled configuration. This setup allowed us to see the differences between a residual zone and pool, regarding dechlorination. 

## 5.2 Material and methods 

### 5.2.1 Chemicals 

The PCE (≥ 99.9% purity) used in the column experiments was ordered from Merck BV. Neat PCE was dyed with Sudan Red B from Fluka for visualization of entrapped PCE within the columns. To prepare a standard calibration curve for sample analysis, the liquid dechlorination products were purchased from Merck BV; TCE (≥ 99.5%), cDCE (≥ 98%), and 1,1-dichloro-ethylene (1,1DCE, ≥ 99.9%) and trans-dichloroethylene (tDCE, ≥ 98%) was obtained from Sigma-Aldrich. To calibrate the gaseous dechlorination products, the gases VC, ethene, ethane, and methane (all ± 5%) were obtained from Air Products (Brussels) in helium in a gas cylinder. 

### 5.2.2 Column set-up and experimental procedure 

The experiments were performed in eight columns made of glass. Seven columns were 19 cm long and 4.5 cm in diameter. Top and bottom lids were stainless steel, with an inlet in the middle for the liquid flow. Between the lid and the soil, a glass porous plate (Schott Duran, Por 1) was placed to spread the liquid equally over the porous medium. The stainless steel lids were made water tight by a viton o-ring (Eriks, Alkmaar, The Netherlands) that was placed between the lid and a POM (Delrinr) ring around the column and secured with bolts. The top and bottom lids were connected to each other by two rods. The columns were fitted with four sampling ports evenly spaced along the column (see Figure 5.1). These sampling ports were equipped with a teflon-lined septum (Alltech) in a PVDFSerto connection. The eighth column was 59.5 cm long with a diameter of 5.3 cm and had six sampling ports evenly spaced along the column. Top and bottom lids were made of teflon, but all other details were the same as described above. Prior to packing of the columns under saturated conditions, the sand (Quartz sand H31, Sibelco, Belgium) was boiled to make the grains water wet and remove oxygen. The sand had grain diameters between 0.1 and 1 mm with a median 


5.2. Material and methods 123 

diameter of 0.4 mm and a light color, which facilitated the observation of dyed PCE in the column. The column was packed under water saturated conditions in an alternating fashion between the addition of sand (1 cm thick lifts) and the homogenization of the sand with a comb-like tool. The column was vibrated after each layer of sand was added to help with settling of the sand. 

First, all columns were flushed with an anaerobic solution, hereafter referred to as ”the medium”. The medium contained 2 mM Na-acetate (Merck), 5 mM K-L-lactate (Fluka), 1.6 mM NH 4 Cl (Merck), 0.37 mM KH 2 PO 4 (Merck), and 16.4 mM NaHCO 3 (Merck). These chemicals served as the electron donor (source), nutrients and pH buffer. Resazurin (1 mg l−^1 , Sigma-Aldrich), a redox indicator, and 1 ml l−^1 of a trace element solution (De Zeeuw, 1984) were added. The pH of the medium was 7.5. The water for the medium was distilled in a distillation setup under 99.5% N 2 0.5% CO 2 -gas atmosphere. To completely reduce the medium, < 100 μl of pre-autoclaved 0.2 M sodium-sulfide solution (Na 2 S, Sigma-Aldrich) was added. All columns were covered with aluminum folie to prevent growth of photosynthetic micro-organisms. Experiments were performed in a temperaturecontrolled room at ± 20 °C. 

Second, the columns were flushed with two pore volumes of water containing a dechlorinating culture immediately after arrival in the laboratory. This water with a dechlorinating microbial assemblage was provided by Bioclear B.V. and originated from a PCE-contaminated site, Evenblij in Hoogeveen (The Netherlands). At the site, remediation had been taking place by stimulation of the dechlorination process. The water used in our experiments was pumped from a well 10 m below surface in the contaminant plume. This water was collected anaerobically in green-glass bottles and top-filled. Transportation took place at ± 10 °C. 

After the introduction of the biomass, the columns were kept under no-flow conditions for 60 hours to permit attachment of bacteria. After that, the columns were run with flow upwards in a closed circuit to permit attachment of the bacteria and to establish dechlorination. This acclimatization period took 52 days. In the influent, on days 3, 10, and 39, 1 ml water was added with a PCE concentration around solubility. On day 52, columns were divided into three groups in order to carry out three different sets of experiments with details summarized in Table 5.1. 

In the first set of experiments, three columns were fed with dissolved PCE and the medium in an upward flow mode. The goal was to determine dechlorination parameters of the bacteria in a soil column. In order to prepare PCE-saturated water, anaerobic water was flown through a water-saturated glass-beads-filled column containing 30 ml PCE (see Figure 5.1). This water was then diluted with 


124 Chapter 5. Column experiments 

Table 5.1: Setup column experiment. Column PCE Set Number Orientation Length τRa^ Present Volume Length Medium as: zone cm days ml cm 1 I Vertical 19 ∼ 2.9 0.5 mM Anaerobic II Vertical 19 ∼ 2.6 0.45 mM Anaerobic III Vertical 19 ∼ 3.2 0.55 mM Anaerobic 2 IV (c) Vertical 19 7 Residual 4.1 3 b^ Anaerobic without electron donor V Vertical 59.5 12.5 Residual 6.9 4.5 Anaerobic VI Vertical 19 6.5 Residual 7.4 3 b^ Aerobic 3 VII Horizontal 19 6.5 Residual 5 10 ∼ 15 Anaerobic and pool VIII Horizontal 19 19 Residual 5 10 ∼ 15 Anaerobic and pool aτR is residence time bThe front of the PCE pumped into the column is not as sharp as drawn in Figure 5.2, due to micro-heterogeneities some fingering occurred. 

the medium in order to have a specific PCE concentration in the influent of the column in the range of 0.4-0.6 mM PCE. Each column had a separate medium reservoir that contained concentrated medium to account for the dilution, yielding the desired concentrations (given in Table 5.1) in the influent of the column. The flow of water saturated with PCE was controlled by a peristaltic pump (Gilson) with viton tubing (Cole Parmer). The medium flow was controlled by a peristaltic pump (Ismatec) with tygon tubing (Ismatec). At 5 cm distance before the inlet to the column, the two tubes were connected to one viton tube, which was attached to the column. 

The second set of experiments were set up to investigate bio-enhanced dissolution and other possible effects of presence of residual NAPL. Three columns, including the large column, were run with a residual PCE emplaced in the top part of the column. This residual PCE was put in place following a procedure illustrated in Figure 5.2. First, between 25 and 40 ml of PCE was injected into the column from below. Then, the top opening of the column was connected to a reservoir of anaerobic medium and the mobile PCE could drain from the column. When all mobile PCE had drained, the column was turned up-side down. Two columns (one small and one large), were fed the anaerobic medium from below by the peristaltic pump with tygon tubing (Ismatec). A small column was fed in a similar way, but the medium did not contain electron donor, nor was it flushed with nitrogen gas to make it anaerobic. This column (no. IV in Table 5.1) served 


5.2. Material and methods 125 

 Anaerobic water 

 Anaerobic medium 

 19 cm 16 cm 12 cm 8 cm 4 cm 0 cm 

 Column with residual PCE 

 Waste 

Figure 5.1: Experimental setup for preparing dissolved PCE solution for the first set of column experiments. Anaerobic water is flown through a column containing neat PCE. The effluent, with saturated PCE concentration is used as influent to the column, diluted by anaerobe medium to a desirable concentration. 

as control (c) for abiotic processes. 

The third set of experiments were aimed at investigating bio-enhanced dissolution of NAPL present both in residual form and in a pool. Two columns were placed in horizontal position and 5 ml PCE was injected through the sampling port at 8 cm (see Figure 5.3). This resulted in a residual zone over the column cross section, as well as a PCE pool, below the injection point. Then, horizontal flow of anaerobic medium was established in the column. The two columns had different flow rates and thus, different residence times, τR (see Table 5.1). The discharge of each column was measured on a regular basis to check the flow rate. All anaerobic media or water reservoirs were kept under 0.2 bar overpressure with 99.5% N 2 0.5% CO 2 -gas to maintain anoxic conditions. As the pumps were between the reservoirs and the columns, the columns themselves were not under pressure. The outflow reservoirs of all columns had a constant head above the columns exit face (saturated conditions were always maintained) at atmospheric pressure. At the conclusion of the experiment, the five columns containing PCE (e.g. 


126 Chapter 5. Column experiments 

 PCE injected Mobile PCE flows out 

 Residual PCE 

 Column turned upside down 

 Figure 5.2: Procedure to obtain a residual PCE zone in the top part of the column. 

 Figure 5.3: Picture of the horizontal columns (type 3). 


5.2. Material and methods 127 

type 2 and 3) were put in a bag with 99.5% N 2 0.5% CO 2 gas. They were then frozen overnight (-80 °C) to prevent any additional microbial activity and redistribution of PCE. The cores were then sliced into pieces to obtain soil samples of 10 gram from different areas in the source zone or plume (see Table 5.2) for a quantitative-polymerase chain reaction (q-PCR) analysis on Bacteria, Archeae, and Dehalococcoides spp. (Dhc); the latter being a specific group of microorganisms able to degrade chlorinated ethenes. This Dhc bacteria belongs to the domain Bacteria. The analysis was performed on 5 gram samples under standard conditions by Bioclear B.V. (The Netherlands, personal communication). 

 Table 5.2: Summary soil samples for q-PCR analysis on day 266. 

 Column No. of samples in Description Type Number Source zone Plume 2 IV 1 1 At 6 and 16 cm V 2 2 At 10, 13, 17, and 18 cm VI 0 0 Column experiment ended after 190 days due to setup failure 3 VII 1 1 At 8 and 15 cm VIII 1 1 At 4 and 15 cm 

### 5.2.3 Analytical methods 

Monitoring of dissolved concentration in the effluent was conducted for a period of 250 days. Water samples were also taken regularly from sampling ports along the columns. Ports were sampled starting from the top port. For sampling the ports, two needles were connected to the two ends of a short viton tube. One needle was inserted through the septum of a sampling port into the column. The outflow end of the sampling tube, also connected to a needle, was placed higher than the top of the column. Then, the column effluent line was closed and a small amount of water was allowed to flow out of the end needle of the tube. The end needle was then inserted into the teflon/red rubber septum of a sampling vial (1.5 ml crimp neck, Alltech, The Netherlands). In this way, the samples were taken at the flow rate of the columns and this minimized disruption of flow within the column. To prevent pressure buildup in the sampling vial, a special assembly of vials and capillaries was used (see Figure 5.4). The headspace of the first vial, containing the sample, was connected to the headspace of a second 1.5-ml vial via a capillary. This second vial was filled with distilled water leaving very little 


128 Chapter 5. Column experiments 

headspace. This water was connected by another capillary to a third 1.5-ml vial, empty at the start. As the first vial filled up, its headspace pressure increased causing a pressure build up in the second vial, which in turn forced water into the third vial which was open to the atmosphere. Without this setup pressure in the sampling vial could have increased and thus prevented flow of water out of the column. The assembly allows for keeping the pressure in the vial low and at the same time, minimize the loss of volatile components. 

 First vial, containing the sample 

 2 nd^ vial 3 rdvial 

 End needle of the sampling tube 

Figure 5.4: Set of vials and capillaries used to sample with a minimum loss of volatile components. 

The concentration of the PCE and dechlorination products in the first sampling vial were determined with gas chromatography (GC). GC measurements were performed using a HP6890 (Agilent Technologies) gas chromatograph with two detectors: an electron capture detector (ECD) and a flame ionization detector (FID). Measurements were automated using a 8200 Auto-sampler (Varian Chrompack). Injection of the sample into the GC column was achieved by a solid phase micro extraction (SPME) fiber (Supelco). The fiber had a polydimethylsiloxane (PDMS) coating and a thickness of 100 μm. SPME headspace adsorption was five minutes and desorption three minutes at 240 °C. All measuring vials contained 1 ml water. Chromatographic separation was achieved using a 30 m x 0.32 mm Heliflexr 


5.2. Material and methods 129 

ATT M^ -Q column with a porous divinyl benzene polymer phase and helium as the carrier gas. The GC oven program started at 30 °C for three minutes, and then heated at 30 °C/min to 180 °C and at 25 °C/min to 230 °C, and then held at 230 °C for ten minutes. The program was run under constant pressure (∼0.6 bar overpressure) mode with a split ratio of 20:1. A six-point standard calibration curve for each chlorinated ethene was generated by spiking distilled water with target analytes. To prevent overload in the GC column, all samples with a concentration higher than 0.1 mM PCE were diluted with distilled water. Dilutions were performed in 1.5-ml vials with a minimum headspace to prevent chlorinated ethene losses to the gas phase. 

### 5.2.4 Hydraulic parameters determination 

The porosity, n, of columns was estimated from the weight of the sand, Ms, and the volume of the column, V, according to the following formula: 

 n = 1 − ρb ρs 

 ; ρb = Ms V 

#### (5.1) 

where ρb is the bulk density of the sand column and ρs is its mass density (2.65 g/ml). 

The hydraulic conductivity was determined by the falling head method (Domenico and Schwartz, 1997). In this method, a water-saturated, sand-filled column is connected to a standpipe at the bottom of the column. At the top of the column a constant head is applied. The water level in the standpipe is raised above the column top and the head is allowed to fall. After a sufficient volume of water is collected over a time period, the hydraulic conductivity, K, is calculated according to: 

 K = aL A∆t 

 ln 

#### ( 

 h 0 h 1 

#### ) 

#### (5.2) 

where a and A are cross-sectional areas of the standpipe and the column, respectively, L is the length of the column, and h 0 and h 1 are the water levels in the standpipe at t=0 and t=∆t, respectively. 

A tracer experiment was performed to determine the effective dispersion coefficient for the system. A sand column was packed similarly to all other columns. A solution of 1 g/l NaCl in distilled water was continuously fed into the column, at a rate of 19 ml/hr. Inflow and outflow electrical conductivity was determined as a measure of concentration and the resulting breakthrough curve was fit with 


130 Chapter 5. Column experiments 

the following analytical solution: 

 C(x, t) = 

#### 1 

#### 2 

#### C 0 

#### [ 

 erfc 

#### ( 

 x − vt 2 

#### √ 

 Dxt 

#### ) 

 + exp 

#### ( 

 xv Dx 

#### ) 

 erfc 

#### ( 

 x + vt 2 

#### √ 

 Dxt 

#### )] 

#### (5.3) 

where C(x, t) is the scaled electrical conductivity of the outflow, C 0 is the electrical conductivity of the inflowing liquid, x (L) is the distance, v (L/T) is the velocity, t (T) the time, and Dx (L^2 /T) is the longitudinal hydrodynamic dispersion coefficient. The dispersion coefficient consist of two main parts: effective diffusion coefficient De f fm and mechanical dispersion coefficient, which is assumed to be linearly dependent on flow velocity. This is mathematically expressed as Dx = De f fm + αxv, where αx is the longitudinal dispersivity. 

## 5.3 Numerical model 

In this section, the model used for simulating our experimental results from column type 1 and 2 is described. The coupled model equations given below are solved by the computer code RT3D (Clement et al., 1998, Clement, 1998). This code is a finite-difference code for simulation of three-dimensional, multispecies, single-phase, reactive transport in porous media, based on the transport code MT3D (Zheng, 1990). The flow field needs to be provided as the solution of a groundwater flow package such as MODFLOW (McDonald and Harbaugh, 1988). The RT3D code uses the operator-splitting (OS) technique which allows representation of various reaction frameworks (Clement, 1998). Using the OS technique, the reaction kinetics can be separated from the transport equations. 

An extension to RT3D code was developed by a consortium under direction of Netherlands Centre for Soil Quality Management and Knowledge Transfer, The Netherlands (Roelofsen and Kassels, 2003), to account for the process of Oil Weathering (OW). This code, referred to as RT3D-OW, was developed to model dissolution and degradation of multi-component LNAPL in the subsurface, either in residual form or in pooled configuration. To use the model in this research, modifications have been made to account for the presence of pooled DNAPL at the bottom of the model domain and sequential dechlorination. 

The partial differential equations describing the fate and transport of component i in the aqueous phase can be written as follows: 

 ∂nS wCwi ∂t + ∇ · (Cwiqw) − ∇ · (nD∗i∇Cwi) = ri diss − ri degr + ri prod (5.4) 


5.3. Numerical model 131 

As the non-aqueous phase is immobile, no terms for advection and dispersion are included in the equation describing the fate and transport of component i in the non-aqueous phase: ∂nS nCni ∂t 

 = −ri diss (5.5) 

where n is the porosity, S w^ and S n^ are the aqueous and non-aqueous phase saturations, Cwi^ and Cni^ are the aqueous and non-aqueous phase concentrations of component i, qw^ is the Darcy velocity, D∗i^ is the effective dispersion tensor, r dissi is dissolution rate, ri degr and ri prod are the source and sink terms due to dechlorination, respectively. Moreover, no term for dechlorination in the non-aqueous phase is written as this is only taking place in the aqueous phase. Similarly, the components of the NAPL are assumed not to adsorb to the solid phase. The mass transfer from the pooled DNAPL is modelled differently than from residual DNAPL. The dissolution mass transfer from residual DNAPL is described shortly, whereas dissolution mass transfer from pooled DNAPL is described later in chapter 6.4.2. Also, models for r dissi , r degri , and ri prod are given in the next section. 

### 5.3.1 Dissolution mass transfer from residual DNAPL 

The mass transfer from residual DNAPL is modelled by a first-order kinetic relation. Non-equilibrium exists when the rate of processes in the aqueous phase (e.g. advection or degradation) are potentially faster than the dissolution rate. In this case, equilibrium between the non-aqueous and the aqueous phase, will not be reached. The driving force for mass transfer is the difference between the aqueous phase concentration and the solubility of the components: 

 ri diss = κi(Csi^ − Cwi) (5.6) 

where κi^ is a lumped mass transfer coefficient of component i, Csi^ is the effective solubility of component i, and Cwi^ is the concentration of component i in the water phase. The effective solubility Csi^ is related to the concentration of the components in the NAPL by Raoult’s Law: 

 Csi^ = XniS wi pure (5.7) 

where Xni^ is the mole fraction of component i present in the NAPL, and S wi pure is the pure phase solubility of component i. The mass transfer coefficient is obtained through an empirical equation in


132 Chapter 5. Column experiments 

volving the dimensionless Sherwood number, S h (Mayer and Miller, 1996): 

 S hi^ = κid^2 Dim 

 = βi 0 Reβ i 1 (S n)β i 2 (5.8) 

where d is the mean particle diameter, Dim is the molecular diffusion coefficient; Re = vρd/μ is the dimensionless Reynolds number which is the ratio of inertial forces to viscous forces, where v is the flow velocity, and μ is the viscosity; and βi 0 , βi 1 , and βi 2 are empirical parameters. 

Equations 5.6, 5.7, and 5.8 are programmed in a new module, which is added to the RT3D reaction package. Values for the fixed parameters can be specified by the user via the reaction package input file and mass transfer between NAPL and aqueous phase will be calculated. To obtain the saturation change of the residual NAPL, equation 5.5 and 5.6 are combined and summed over all components within the NAPL: 

 ∂nS n ∂t 

#### = − 

 ∑^ Nnc 

 i 

 κi(Csi^ − Cwi) ρn^ 

#### (5.9) 

where variations in ρn, the density of the NAPL, are neglected and is assumed that the NAPL is composed of Nnc^ components that can dissolve in water with different solubilities. 

The change of concentration of components in the NAPL and aqueous phase are obtained using equation 5.4 and 5.5 combined with 5.6. For NAPL, the first term in equation 5.5 is approximated as: 

nS (^) oldn ∂Cni ∂t 

#### = 

 ∂nS nCni ∂t − Cniold 

 ∂nS n ∂t 

#### (5.10) 

where S nold and Cniold are the saturation and concentration values at the old time step. This term is then combined with equation 5.9 to obtain: 

 nS nold ∂Cni ∂t = −κi(Csi^ − Cwi) + 

 Cniold ∑Nn i κ 

i(Csi (^) − Cwi) ρn^ 

#### (5.11) 

For the change of concentration of components in the water, we employ the following approximation: 

 nS wold ∂Cwi ∂t = +κi(Csi^ − Cwi) − 

 Cwiold 

 ∑Nn i κ 

i(Csi (^) − Cwi) ρn^ − ri degr + ri prod (5.12) 


5.3. Numerical model 133 

### 5.3.2 Biodegradation 

PCE can biologically be dechlorinated under anaerobic conditions via the following sequential reaction chain (McCarty, 1997): PCE to TCE to cDCE to VC to ethene. TCE was not included as a component in our model, as the degradation step from TCE to cDCE was very fast, in other words, PCR dechlorinated to cDCE in the model. In batch experiments (see Chapter 3), performed with the same microbial assemblage, TCE was detected only in very low concentrations. Dechlorination of all chlorinated components was modelled with the classical form of the Michaelis Menten kinetic relation. Herein the dechlorination rate was given as a function of the component concentration, Cwi^ (mol l−^1 ), and the biomass concentration, X (cell l−^1 ): 

 ri degr = Ri maxX 

 Cwi Kis + Cwi^ 

#### (5.13) 

where Ri max (mol cell−^1 day−^1 ) is the maximum dechlorination rate, and Kis (mol l−^1 ) is the half-saturation constant. In the sequential reaction chain, the production rate is equal to the dechlorination rate of the mother component because they are expressed in molar units per time, so, 

 ri prod = r degri−^1 (5.14) 

Obviously, for PCE the production rate was zero, r prodPCE = 0. The change in the biomass was modelled by: 

 ∂X ∂t = −kd X + 

#### ( 

 rPCE deg + r degcDCE + rVC deg 

 ) (^ Xmax^ − X Xmax 

#### ) 

#### Y (5.15) 

where kd (day−^1 ) is the biomass decay constant, Y (cell mol−^1 ) is the yield coefficient, and Xmax^ is the maximum concentration of bacteria (Zysset et al., 1994). The assumption was made that the biomass is growing from the dechlorination of all chlorinated ethenes in the model, i.e. PCE, cDCE and VC, with the same yield and that it is not mobile. 

### 5.3.3 Initial and boundary conditions 

The reaction kinetics described by equations above were programmed as a userdefined reaction package in the RT3D model using four mobile components to represent the aqueous phase contaminants (PCE, cDCE, VC, and ethene) and 


134 Chapter 5. Column experiments 

five immobile components to represent their corresponding non-aqueous phase contaminants plus the biomass. 

For columns with dissolved PCE (type 1), the influent PCE concentration was defined with a constant flux boundary specified at the lower column boundary. The outflow boundary condition was chosen to be zero dispersive flux. Initially, the column contained only a low cDCE concentration, which was produced before the actual experiment during the period of biodegradation establishment. In short, the initial and boundary conditions for the columns with dissolved PCE (type 1) were: 

 qwCw,PCE^ − D∗PCE^ 

 dCw,PCE dx (x = 0 , t) = qw 0 C 0 w ,PCE for t > 0 (5.16) 

 qwCwi^ − D∗i^ dCwi dx (x = 0 , t) = 0; i = cDCE, VC, and ethene (5.17) 

 ∂C ∂x (x = L, t) = 0 for t > 0 (5.18) 

 Cw,cDCE^ (x, t = 0) = Cw 0 ,cDCE (5.19) 

 Cwi(x, t = 0) = 0; i = PCE, VC, and ethene (5.20) X(x, t = 0) = X 0 (5.21) 

For the columns with a residual DNAPL present at the start of the experiment (type 2), the first boundary condition (Equation 5.16) is also no mass flux for PCE: 

 qwCwi^ − D∗i^ 

 dCwi dx (x = 0 , t) = 0; i = PCE, cDCE, VC, and ethene (5.22) 

The residual PCE zone was defined as the length of the column, L, minus the length of residual zone, Lz. The NAPL was assumed to be pure PCE, i.e. initial concentration of all other components was set to zero. Furthermore within the residual PCE zone the initial PCE saturation was defined: 

 S n([L − Lz], t = 0) = S n 0 (5.23) Cn,PCE^ ([L − Lz], t = 0) = ρPCE^ (5.24) 


5.4. Experimental results 135 

### 5.3.4 Parameter estimation 

The computer code PEST (Doherty et al., 1994) was used for parameter optimization. PEST is a model-independent parameter estimator, that gives information about parameter variances and covariances or correlation coefficients. This provides an insight in how well the included observations can determine the parameters. PEST minimizes the sum squares of weighted differences between the model outputs and the measurements (the concentration measured in the effluent and sampling ports of the columns) by changing assigned model parameters within given ranges of uncertainty using a Gauss-Marquardt-Levenberg-based optimization algorithm. 

## 5.4 Experimental results 

### 5.4.1 Column type 1: vertical column with dissolved PCE 

Results of the first set of experiments involving three columns with a continuous input of dissolved PCE are presented in Figure 5.5. Concentrations of PCE and its dechlorination products in the influent and effluent of the three columns are plotted with time. As it can be seen, the influent PCE concentration was not really constant but varied around the target concentration. Discharge measurements of the effluent from the columns showed that velocity variations were minimal (< 7%), mainly caused by changing tubing connected to the column. There was no PCE or TCE detected in the effluent, or in any of the sampling ports along the columns. Even in the lowest sampling port, at four cm distance from the influent, PCE concentrations were below 0.05 mM. This indicates that the dechlorination of PCE was fast (< 0.5 day). This was similar for the step from TCE to cDCE, as TCE was never detected. The main dechlorination products were cDCE and VC in columns I and III, where VC concentration was relatively low compared to the cDCE concentration. In column II equal amount of cDCE and VC were produced from day 50 to 100. On day 150, cDCE was fully converted to VC, which was dechlorinated to ethene later in time. 

### 5.4.2 Column type 2: vertical column with residual PCE 

In this section, results of the second set of experiments involving three columns with a zone of residual PCE in the upper part of the column are presented (see Figure 5.2). In Figure 5.6, concentrations of PCE and its dechlorination products 


136 Chapter 5. Column experiments 

 0 50 100 150 200 250 300 

 0 

 0.2 

 0.4 

 0.6 

 Column I i) 

 0 50 100 150 200 250 300 0 

 0.2 

 0.4 

 0.6 

 Column II ii) 

 0 50 100 150 200 250 300 

 0 

 0.2 

 0.4 

 0.6 

 Column III iii) 

 PCE cDCE VC Ethene PCE in 

 Time (days) 

 Concentration (mM) 

Figure 5.5: Chlorinated ethene concentrations in the effluent and PCE concentration in the influent (PCE in) from columns i) I, ii) II, and iii) III. 

in the effluent are plotted as a function of time, where also the PCE solubility is shown. First, consider the control column, column IV. Here, despite the nonideal conditions, some dechlorination occurred. Probably due to some microorganisms present in the dechlorinating microbial assemblage, the aerobic medium was made anaerobic in the first 15 cm of the column before the PCE residual zone at the top of the column was reached. Electron donor was presumably attached to the soil grains and available for the microorganisms. After 150 days, however, production of cDCE decreased and dechlorination ceased. PCE concentration did 


5.4. Experimental results 137 

not reach the solubility limit but a steady-state value of 0.5 mM was established. In fact, the steady-state PCE concentration of 0.5 mM was also observed in the period when dechlorination took place. Solubility level concentrations were not reached because of the short residence time of the residual DNAPL zone. During the period of active dechlorination, the total chlorinated ethene concentration (sum of the PCE and cDCE; not shown) first increased and later decreased. As the PCE concentrations remained constant while the total chlorinated ethene concentration changed, PCE dissolution rate cannot have been constant in time. Probably, PCE solubility or dissolution rate coefficient had increased in the presence of dechlorination. The same effects were observed in columns V and VI which had optimal conditions for dechlorination (Figures 5.2-ii and iii). PCE effluent concentration was almost constant over the whole period of the experiment. Concentration of cDCE increased and reached maximum values of 3 mM and 2 mM in columns V and VI, respectively. If PCE solubility or dissolution rate coefficient were constant in time, the PCE concentration would have decreased. 

Despite the detection of cDCE, VC concentration was very low in column VI and not detectable in the other two columns. Similarly, ethene was not detected in any column. The concentration of the chlorinated ethenes was used to determine a bioenhanced dissolution factor. This was calculated as the ratio of the total effluent concentrations or total effluent masses for cases with and without biodegradation. Indeed, in column IV (without dechlorination) after a steady-state was reached only PCE was measured, at a constant concentration of 0.5 mM. In the columns with optimal conditions for biodegradation the total effluent concentrations were about 3 mM and 2 mM of cDCE for columns V and VI, respectively, plus 0.5 mM of PCE. This amounts to bioenhanced dissolution factors of approximately 7 and 5 in columns V and VI, respectively. 

Concentrations measured at sampling ports below the source zone were examined in order to look for any possible mobilization of PCE. In Figure 5.7, a plot of chlorinated ethene concentrations at two sampling ports at positions 45 and 55 cm and in the effluent of column VI on day 72 is shown. The column itself is shown on the left hand side of the plot, with the zone that contained the residual PCE in red in the upper part. The concentrations of PCE, TCE, cDCE and VC are plotted in the horizontal bars at the location of the sample with the effluent concentration in the top. The bar length gives the total concentration of chlorinated ethenes. Each bar is multicolored, with colors corresponding to the components (see legend). It is evident that TCE and VC were detected in very low concentrations and main components measured were PCE and cDCE. 

 The presence of PCE and its dechlorination products below the residual zone 


138 Chapter 5. Column experiments 

 0 50 100 150 200 250 300 

 0 

 1 

 2 

 3 

 Column IV (control) i) 

 0 50 100 150 200 250 300 

 0 

 1 

 2 

 3 

 Column V 

 PCE solubility 

 ii) 

 0 50 100 150 200 250 300 0 

 1 

 2 

 3 

 Column VI 

 PCE solubility 

 iii) 

 PCE cDCE VC 

 Time (days) 

 Concentration (mM) 

Figure 5.6: Chlorinated ethene concentrations in the effluent from columns i) IV, and ii) V, and iii) VI. Column IV received aerobic medium without electron donor. No ethene was detected in any of the columns. 

can be only explained by PCE mobilization. A more comprehensive picture is presented in Figure 5.8, where chlorinated ethene concentrations measured at sampling ports and in effluent of columns IV, V, and VI are shown on several days. In the control column IV, measured PCE concentrations in the sampling port below the residual zone were practically zero at all times. In columns with dechlorination, however, high PCE concentrations were detected below the residual zone approaching the PCE solubility limit on day 127. The detection of PCE in the sampling ports below the residual PCE zone could occur only if PCE was mobilized and moved to the sampling port from the residual PCE zone above. It must be emphasized that the mobilization of residual PCE was observed only in columns with dechlorination. Later, as the mobilized PCE was dissolved, PCE concentration decreased again (on day 225). Here the mobilized PCE dropped 


5.4. Experimental results 139 

 0 0.5 1 1.5 2 2.5 3 3.5 4 

 45 

 55 

 60 

 Day 72 

 Concentration (mM) 

 PCE TCE cDCE VC 

Figure 5.7: Chlorinated ethene concentrations measured at sampling ports below residual zone and effluent of column VI on day 72; with optimal conditions for dechlorination. 

only a few centimeters. But this occurred in the direction opposite to water flow. The extent would have been probably bigger if the water flow had been in horizontal direction. 

### 5.4.3 Column type 3: horizontal column with residual and pooled 

### PCE 

In Figure 5.9, the effluent concentrations of horizontal columns VII and VIII are shown. Here, the PCE residual zone was situated in the middle of the column with a PCE pool at the bottom. No PCE or TCE was detected in the effluent as the dechlorinating microbial assemblage was effective enough to dechlorinate dissolved PCE before it reached the end of the column. Main product of dechlorination was cDCE with very low VC concentrations found in the effluent of column VIII. The total chlorinated ethene concentration in the effluent increased with time, which makes it difficult to determine a sustained bioenhanced dissolution factor. In column VII, the dechlorination process enhanced the removal of chlorinated ethenes by a maximum of four times. This factor was obtained by assuming that the total effluent chlorinated ethenes concentration in the absence of dechlorina


140 Chapter 5. Column experiments 

 0 0.5 1 

 12 

 16 

 19 

 Day 58 0 2 4 

 12 

 16 

 19 

 Day 58 

 n.m. 

 0 2 4 

 45 

 55 

 60 

 Day 58 

 0 0.5 1 

 12 

 16 

 19 

 Day 72 0 2 4 

 12 

 16 

 19 

 Day 72 0 2 4 

 45 

 55 

 60 Day 72 

 0 0.5 1 

 12 

 16 

 19 

 Day 98 0 2 4 

 12 

 16 

 19 

 Day 98 0 2 4 

 45 

 55 

 60 Day 98 

 0 0.5 1 

 12 

 16 

 19 

 Day 127 0 2 4 

 12 

 16 

 19 

 Day 127 0 2 4 

 45 

 55 

 60 Day 127 

 0 0.5 1 

 12 

 16 

 19 

 Day 225 0 2 4 

 12 

 16 

 19 

 Day 225 

 Column IV (control) Column V Column VI 

 Concentration (mM) 

 PCE TCE cDCE VC 

Figure 5.8: Chlorinated ethene concentrations measured at sampling ports and effluent from columns IV (control), V, and VI; number along the vertical give the position of measurement points; n.m. stands for not measured. 

tion would have been 1.2 mM. In column VIII, the bioenhancement was much lower, with approximately a factor of two. Moreover, the cDCE concentration approached the PCE solubility after 200 days of experiment, indicating that at that time the bioenhancement of dissolution was negligible. 

### 5.4.4 Microbial assemblage analysis 

The dechlorinating microbial assemblage used in the column experiments was also used for the batch experiments described in chapter 3. There, a table was presented with numbers of bacteria present in water samples from the same mon


5.4. Experimental results 141 

 0 50 100 150 200 250 300 

 0 

 2 

 4 

 6 

 Column VII 

 PCE solubility 

 i) 

 0 50 100 150 200 250 300 

 0 

 1 

 2 

 3 

 Column VIII 

 PCE solubility 

 ii) 

 PCE cDCE VC 

 Time (days) 

 Concentration (mM) 

Figure 5.9: Enhanced dissolution in effluent chlorinated ethene concentrations from column i) VII and ii) VIII. No ethene was detected. 

itoring well before start of the experiments (batch and columns). At the end of the column experiment, q-PCR analysis was also performed on soil samples from columns with neat PCE (see Table 6.3) in the source zone and in the plume. Dehalococcoides spp. was used as an indicator for dechlorination. This was not the only microorganisms that could mediate the dechlorination of PCE. Research suggests that several strains of microorganisms are able to degrade PCE to cDCE. However, whereas the reduction of cDCE can be achieved by only a limited group of bacteria (Aulenta et al., 2006a) of which Dehalococcoides spp. is one group. Generally, the bacterial counts on soil samples in the columns yielded high numbers of bacteria, indicating that an active pool of bacteria was present. This was also the case for the control column (IV) that received aerobic medium and no electron donor. This can explain the fact that dechlorination occurred in this col


142 Chapter 5. Column experiments 

umn to yield low cDCE concentrations. Column V had four samples taken in the top half of the column. The ratio of Dehalococcoides spp. to bacteria is low in the area without PCE and increased to the top of the column in the residual PCE zone. Overall, the ratio was higher in samples from the PCE source zone than from the plume or upstream the source zone. 

Table 5.3: Results of the molecular analysis with q-PCR on soil samples from the columns with neat PCE at the end of the experiment on day 266 as well as the control column IV. The actual number of cells (N) ranged from 0.5*N to 2*N. Here the assumption was that one cell contained one DNA copy. 

 Column Position PCE Dehalococcoides Bacteria Dhc/Bacteria Archaea type number spp. cells g−^1 cells g−^1 ‰ cells g−^1 2 IV (c) 16 cm yes 5.2· 107 7.2· 108 72.2 1.5· 107 6 cm no 2.2· 105 2.5· 108 0.9 7.5· 106 2 V 18 cm yes 2.2· 106 2.9· 108 7.6 2.0· 107 17 cm yes 3.7· 107 9.4· 109 3.9 8.4· 107 13 cm no 1.8· 107 2.6· 1011 0.1 7.2· 108 10 cm no < 2.2· 104 8.0· 107 0.3 1.0· 107 3 VII 15 cm no 4.8· 105 1.2· 109 0.4 1.7· 107 8 cm yes 1.9· 105 1.7· 108 1.1 2.6· 106 3 VIII 15 cm no 1.5· 107 4.8· 109 3.1 1.1· 107 4 cm yes 4.9· 105 2.8· 107 17.5 9.9· 105 

## 5.5 Modelling results 

The model setup we used for simulating the column experiments, described in section 5.3, included advection and dispersion, dissolution from residual PCE described by a kinetic relationship, and sequential dechlorination modelled by Michaelis-Menten kinetics formula. Supply of electron donor was assumed to be in excess and inhibitory components were assumed to be absent. To account for small variations in the pump discharge, multiple stress periods were defined for inflow of the columns. The flow field was assumed to remain unaffected by NAPL dissolution and the porosity was constant. Main parameter values used in the numerical simulations of all columns are shown in Table 5.4. The 190-mm columns were discretized into 99 cells with sizes ranging from 1 to 10 mm along the onedimensional domain. Cell size was small near the inand outflow boundaries and 


5.5. Modelling results 143 

around the boundary of the residual DNAPL zone. One-dimensional simulations were performed for columns of type 1 and 2. Two-dimensional simulations of columns of type 3 did not result in an approximation of the experimental results. Probably, three-dimensional simulations are required to simulate these horizontal columns. Unfortunately, with the current model this three-dimensional setup could not be realized. 

 Table 5.4: Values of parameters used in numerical simulations of column experiments. 

 Parameter Value Reference Diffusion coefficient DPCEm 1 · 10 −^9 m^2 sec−^1 Reid et al. (1987) Dispersivity αL 0.018 – 0.022 cm Determined Porosity n 0.38 Determined Hydraulic conductivity K 0.91 – 2.5· 10 −^5 m sec−^1 Determined Particle diameter d 4 · 10 −^2 m Determined Maximum biomass concentration Xmax 1.5· 1011 cell l−^1 Assumed Yield coefficient Y 5 · 1011 cell mmol−^1 Assumed Empirical dissolution constant β 0 12 Mayer and Miller (1996) Empirical dissolution constant β 1 0.75 Mayer and Miller (1996) Empirical dissolution constant β 2 0.6 Mayer and Miller (1996) PCE solubility Cs,PCE^ 200 mg l−^1 Lide (Internet Version 2008) 

In this research, the focus is on parameters of dechlorination and dissolution, which are maximum dechlorination rates, half-saturation constants, biomass yield and PCE dissolution rate coefficient. However, not all of these parameter could be estimated and PEST was used to determine parameter correlations. Half-saturation constants were not estimated as they were highly correlated with their associated maximum dechlorination rate. The half-saturation constant has an influence on the tail of the plot of concentration versus time. However, in our data set we have too few data points around the tail. Thus, the fitting could not give information on the value of the half-saturation constants. Their values were, therefore, set to 0.1 mM. This was based on literature values (Nielsen and Keasling, 1999, Amos et al., 2007) and our own batch experiments (see Chapter 3). The initial biomass concentration could not be estimated due to high correlation (∼0.95) with the maximum degradation rate of PCE. The initial biomass concentration was measured in the groundwater used to inoculate the columns. However, during the acclimatization period of the columns this concentration could have been changed. In the parameter estimation process, measurements were given nonequal weights as some measurements were known to be more prone to experimental errors than others. For example, results from samples along the column via sampling ports 


144 Chapter 5. Column experiments 

showed a lower total chlorinated ethene concentration than measured in the influent and effluent of the column. For side port sampling, a sampling needle was punctured through the septum. The sampling needle could not be fully inserted into the column due to blockage of the port capillaries with sand grains. As a result, samples were probably withdrawn from the dead volume of the ports, which is a likely explanation for the lower sum of chlorinated ethene concentrations observed in these ports as compared to the effluent concentrations (similar observations were made by Amos et al. (2008)). The inverse of the standard deviation of measured concentrations were used as the weighting factor. For effluent concentrations, a standard deviation of 0.05 mM was used, whereas for measurements taken along the column a standard deviation of 0.1 mM (and thus a lower weighting factor) was used. 

### 5.5.1 Column type 1: vertical column with dissolved PCE concen

### tration 

Columns of type 1 had a length of 190 mm and received a dissolved PCE concentration in the influent of the columns (see Table 5.1). Various parameter values used in the simulation are given in Tables 5.4 and 5.5. 

 Table 5.5: Additional parameters used in numerical simulations for column type 1. 

 Parameter Value Column for II Value for Column III X(x, t = 0) (cell l−^1 ) 1.2· 108 1.2· 108 K (m day−^1 ) 0.808 1.3824 No of stress periods 4 2 Length of stress periods (days) 32, 83, 8, 34 30, 45 Discharge well (m^3 day−^1 ) 5.72, 7.6, 2.8, 6.8 3.68, 5.44 

The total chlorinated ethene concentration of column I in the effluent (see Figure 5.5-i) was not equal to the PCE concentration in the influent. Over the first 50 days, an increase in total chlorinated ethene concentration in the effluent was observed. The observed breakthrough curve was not expected and our model did not simulate this behavior. With a residence time of approximately 3 days, the concentration would increase only during the first few days (i.e. breakthrough in 3 days). One possibility to obtain this behavior in the model was to include (kinetic) adsorption. But, then, even more unknown parameters are introduced 


5.5. Modelling results 145 

into the model. Consequently, column I was not used for parameter estimation and only columns II and III were studied. 

The simulation time for column II was set to 157 days, because during this period VC dechlorination did not occur as verified by the fact that ethene was not detected in any sample (Figure 5.5-ii). Therefore, the maximum VC dechlorination rate could be set to zero and as a result only the maximum dechlorination rates of PCE and cDCE had to be estimated. 

For column III, also the maximum dechlorination rates of PCE and cDCE were estimated with a simulation time of 75 days. The total number of measurements of PCE, cDCE, and VC concentrations were 126 for column II and 72 for column III. These were mainly measurements from effluent samples; only about 30% of the measurements were taken from sampling ports along the column. 

In Figure 5.10 and 5.11 for columns II and III, respectively, model results generated with the optimized parameter values (lines) are shown together with the measurements (points). PCE was not detected in any sampling port in the experimental and modelling results. Evidently, PCE was dechlorinated before the lowest sampling port at 4 cm and no information was available on the PCE concentration gradient. As a result, it is not surprising that the maximum PCE dechlorination rate was estimated with a large margin of uncertainty as indicated by the 95 % confidence limits (see Table 5.6). In contrast, the clear breakthrough of cDCE and VC concentration allowed the maximum cDCE dechlorination rate to be estimated with a small margin of uncertainty. The estimated maximum cDCE dechlorination rate constant of column II was higher than of column III. This resulted from the higher VC concentration and shorter residence time in column II compared to column III. 

The cDCE concentration decreased over the column length, with the corresponding increase in VC concentration. However, in the model VC breakthrough was earlier than in the laboratory experiment (see Figure 5.10-iv). The model could be improved by decreasing the yield coefficient, which was fixed in the estimation procedure due to high correlation with the maximum PCE dechlorination rate. 

The general trend in chlorinated ethene concentrations in the laboratory experiment are simulated well by the numerical model. There were no lag times for dechlorination included in the model; i.e. dechlorination would take place as soon as the mother component was present. 


146 Chapter 5. Column experiments 

 0 50 100 150 200 0 

 0.2 

 0.4 

 0.6 

 0.8 

 Concentration (mM) 

 Sampling port 4 cm i) 

 PCE cDCE VC PCE model cDCE model VC model 

 0 50 100 150 200 0 

 0.2 

 0.4 

 0.6 

 0.8 

 Sampling port 12 cm iii) 

 0 50 100 150 200 0 

 0.2 

 0.4 

 0.6 

 0.8 

 Column effluent iv) 

 Time (days) 

 0 50 100 150 200 0 

 0.2 

 0.4 

 0.6 

 0.8 

 Sampling port 8 cm ii) 

Figure 5.10: Column II results from model (lines), generated with the optimized parameters, and measurements (points). 

Table 5.6: Estimated parameter values and parameter correlation coefficients for column II and III with dissolved PCE (type 1). 

 Parameter Estimated 95 % confidence limits Parameter correlation coefficient value lower limit upper limit RPCE max RcDCE max Column II RPCE max 6 · 10 −^8 0 ∞ 1.0 -8.3· 10 −^2 RcDCE max 2.2· 10 −^12 2.0· 10 −^12 2.4· 10 −^12 -8.3· 10 −^2 1.0 Column III RPCE max 1 · 10 −^10 2.1· 10 −^11 4.7· 10 −^10 1.0 0.7 RcDCE max 4.2· 10 −^13 2.9· 10 −^13 6.0· 10 −^13 0.7 1.0 


5.5. Modelling results 147 

 0 20 40 60 80 0 

 0.2 

 0.4 

 0.6 

 0.8 

 Sampling port 4 cm i) 

 0 20 40 60 80 0 

 0.2 

 0.4 

 0.6 

 0.8 

 Sampling port 8 cm ii) 

 cDCE VC cDCE model VC model 

 0 20 40 60 80 0 

 0.2 

 0.4 

 0.6 

 0.8 

 Time (days) 

 Concentration (mM) 

 Sampling port 12 cm iii) 

 0 20 40 60 80 0 

 0.2 

 0.4 

 0.6 

 0.8 

 Column effluent iv) 

Figure 5.11: Column III results from model (lines), generated with the optimized parameters, and measurements (points). 

### 5.5.2 Column type 2: vertical column with residual PCE 

Columns of type 2 had a length of either 190 mm or 595 mm (see Table 5.1). The flow and transport in both columns were modelled as one dimensional. The initial PCE saturation in the upper part of the columns was calculated from the volume of injected PCE, the length of residual zone, and the porosity (see values reported in Table 5.1). The flow rate and therefore the flow velocity was known and assumed to be constant (thus, not affected by NAPL dissolution). The aqueous components included in the simulation were PCE, cDCE, VC, and ethene and their initial concentration in water was assumed to be zero. These aqueous components have an equivalent component in the non-aqueous phase. Except for PCE, their initial concentration in the NAPL was assumed to be zero. Initial PCE concentration in the NAPL was assumed to be equal to PCE density in the residual zone and zero everywhere else. Various parameter values used in the 


148 Chapter 5. Column experiments 

simulation are given in Tables 5.4 and 5.7. 

Table 5.7: Additional parameters used in numerical simulations for column type 2, with residual PCE at the top of the column. 

 Parameter Value Column for IV Value for Column V Value for Column VI X(x, t = 0) (cell l−^1 ) 5 · 108 5 · 108 5 · 108 K (m day−^1 ) 1.158 0.91 1.296 Knaplareae f f (m day−^1 ) 0.356 0.263 0.498 S n^ 0.24 0.25 0.2 Stress periods: Number 2 7 5 Length (days) 69, 31 69, 16, 21, 50, 33, 43, 29 55, 20, 10, 15, 50 Discharge well (m^3 day−^1 ) 2.2, 2.5 2.4, 2.6, 3.32, 3.4, 4.0, 2.4, 2.8, 5.6, 4.3, 2.32, 2.88 3.4 

For column IV, the first dissolution rate constant, β 0 , and the maximum dechlorination rate of PCE were estimated over the first 100 days. This column had non-optimal conditions that caused a production of cDCE over the first 150 days after which dechlorination ceased. For columns V and VI, the maximum dechlorination rate of PCE, the yield coefficient, and the first dissolution rate constant were estimated over 261 and 190 days, respectively. In column VI, cDCE dechlorination occurred as verified by the detection of VC in the samples. Therefore, the maximum cDCE dechlorination rate was also estimated for this column. Only effluent measurements were used in the estimation procedure for type 2 columns as PCE was present in the top of the columns. Column IV and V had in total 52 and 94 measurements, respectively, of PCE and cDCE concentrations in the estimation procedure. For column VI, also VC concentrations were included to yield 150 measurements. In Figure 5.12, model results (lines) generated with the optimized parameter values (see Table 5.8) are shown together with the measurements (points) for columns IV, V, and VI. For column IV, the model showed that the PCE concentration would stabilize at 0.5 mM after an initial period with higher PCE concentration. This initial overestimation resulted from a constant dissolution rate coefficient and PCE solubility. These parameters were optimized through minimizing the objective function. The sum of squared-weighted residuals between model and experimental result was used as the objective function. The optimized values were heavily influenced by the large number of data points after the increase in cDCE (around day 30). As there were few data points early in the experiment, parameter values were not sensitive to the variations in PCE concentration. 


5.5. Modelling results 149 

 0 50 100 150 200 250 300 0 

 0.5 

 1 

 Column IV i) 

 0 50 100 150 200 250 300 0 

 1 

 2 

 3 

 Concentration (mM) 

 Column V ii) 

 PCE model cDCE model VC model 

 0 50 100 150 200 0 

 1 

 2 

 3 

 Time (days) 

 Column VI iii) 

 PCE cDCE VC 

Figure 5.12: Model (lines) generation with the optimized parameters, and measurements (points) for columns i) IV (non-ideal conditions), ii) V, and iii) VI. 

In columns V and VI, the total chlorinated ethene concentration (sum of the PCE, cDCE, and VC; not shown) increased when dechlorination started, but over the same time period the PCE concentration remained constant around 0.5 mM. For the model to simulate these two features, it was necessary to assign high initial PCE concentrations, which does not correspond to experimental data. If the full range of measurement period were to be simulated with our model, we must have allowed dissolution parameters to increase with time. We feel that constructing such a model will require additional information and measurement 


150 Chapter 5. Column experiments 

that is not available. There is also a discrepancy between model and experiment regarding the onset of PCE dechlorination in column IV. As the yield coefficient was not optimized, the growth of the bacteria was too fast and cDCE concentrations peaked too early to the observed cDCE concentration. Although the yield coefficient was highly correlated with the maximum PCE dechlorination rate constant (see Table 5.8), it was included in the model runs for the other two columns V and VI. Therefore, for these columns, the onset of PCE dechlorination in the model matched the experimental results better. In general, the 95 % confidence limit of estimated parameters do not show a large margin of uncertainty. This indicates that we have the best-fit parameter values that can be obtained with this model. Estimated values for column V and VI are comparable. In these columns, conditions were similar and maximum PCE dechlorination rate constants are within the same order of magnitude and the dissolution rate constant fall even within the 95 % confidence intervals. Estimated parameters values from column IV were different than column V and VI. Conditions were completely different column IV and, moreover, the value for the yield coefficient was not estimated and the simulation was performed with a higher yield coefficient than in the other two columns. The fact that model results do not exactly fit the experimental data, in general, is due to the underlying assumptions on how processes are incorporated in the model. Firstly, the mobilization of residual PCE was not incorporated in the model. Secondly, we believe improvements can be made by allowing a dissolution parameter to change. For example, the first empirical dissolution rate constant, β 0 , or PCE solubility, Cs,PCE^ , could be made a function of degree of dechlorination or biomass concentration. 

## 5.6 Discussion and conclusions 

PCE dechlorination under continuous flow conditions give different results than batch experiments. Nutrients and electron donor and acceptor are continuously delivered to the source zone, and dissolved (toxic) components are transported away from the source zone. Moreover, the presence of a porous medium allows large variations in local concentrations to exist, which can be advantageous for PCE dechlorination. As shown in batch experiments, under mixed and homogeneous conditions, dechlorination ceased at PCE concentrations above 0.5 mM (see Chapter 3). However, under continuous flow conditions within a porous medium, PCE dechlorination to cDCE occurred at even higher concentrations. This shows that in porous media, there are pores within a source zone, where 


5.6. Discussion and conclusions 151 

Table 5.8: Estimated parameter values and parameter correlation coefficients for column IV, V, and VI with residual PCE (type 2). 

 Parameter Estimated 95 % confidence limits Parameter correlation coefficient value lower limit upper limit R maxPCE RcDCE max Y β 0 Column IV RPCE max 4.9· 10 −^12 4.2· 10 −^12 5.7· 10 −^12 1.0 0.42 β 0 14.5 12.9 16.0 0.42 1.0 Column V RPCE max 5.6· 10 −^11 4.7· 10 −^11 6.7· 10 −^11 1.0 -0.96 -0.48 Y 2.1· 10 +^9 1.6· 10 +^9 2.7· 10 +^9 -0.96 1.0 0.40 β 0 6.9 5.3 8.6 -0.48 0.40 1.0 Column VI RPCE max 3.9· 10 −^11 3.3· 10 −^11 4.5· 10 −^11 1.0 0.49 -0.93 -5.2· 10 −^2 RcDCE max 4.4· 10 −^13 3.2· 10 −^16 6.1· 10 −^10 0.49 1.0 -0.47 0.35 Y 5.4· 10 +^9 4.3· 10 +^9 6.8· 10 +^9 -0.93 -0.47 1.0 -1.5· 10 −^2 β 0 7.3 5.7 8.9 -5.2· 10 −^2 0.35 -1.5· 10 −^2 1.0 

the PCE concentration is below the PCE inhibitory level and microorganisms are capable of dechlorinating PCE. 

Column experiment with a PCE phase present have been performed by Yang and McCarty (2002) with 2% NAPL saturation, Amos et al. (2008) with 20% NAPL saturation, and Kaplan et al. (2008) with 35% NAPL saturation. Amos et al. (2008) showed minimal reductive dechlorination when the NAPL solely consisted of PCE at this high saturations. Also the production of PCE daughter product was minimal in column experiments by Kaplan et al. (2008). This suggests that microbial growth within source zones is possible, provided that microenvironments can develop with low chlorinated ethene concentrations. With higher NAPL saturations (as e.g. in a pool), these areas are probably more difficult to establish. 

Our setup also provided capabilities to investigate mobilization of residual DNAPL. We have established that mobilization of residual PCE occurred as a result of dechlorinating activities. To our knowledge, this is the first proof that dechlorination could cause the mobilization of residual NAPL droplets. Previously, natural mobilization of multicomponent DNAPLs pools was shown due to selective dissolution of NAPL components in the aqueous phase and subsequent change in the NAPL composition (Roy et al., 2002, 2004). Also, mobilization of residual PCE was observed during alcohol or surfactant flushing (Padgett and 


152 Chapter 5. Column experiments 

Hayden, 1999, Abriola et al., 1994). Recently, indications of residual DNAPL mobilization by dechlorination were provide through surface tension measurements by Kaplan et al. (2008). They concluded that surface tension in the presence dechlorination was lower than in abiotic conditions. They suggested that the secretion of microbially generated surfactants had changed NAPL dissolution. This was also supported by an increase in PCE solubility observed in columns with dechlorinating activity. In our column experiments, effluent PCE concentration did not reach PCE solubility limit, but rather a steady-state value of 0.5 mM PCE was reached, determined by the residence time in the source zone. However, over the course of the experiment, the PCE concentration remained constant whereas at the same time production of cDCE was observed. In other words, the total chlorinated ethene concentration increased whereas PCE concentration remained constant. Therefore, we hypothesize that either the PCE solubility or the dissolution rate constant should have increased to account for the difference in total chlorinated ethene concentration. This increased dissolution rate in the presence of dechlorination supports the hypothesis of the production of surfactants by the dechlorinating microbial assemblage. Beside Kaplan et al. (2008), other studies (Bai et al., 1997, Mulligan, 2005, Clifford et al., 2007) have also proposed biosurfactants as a mechanism for solubility enhancement of non-aqueous phase liquids. 

The increase in PCE solubility and the production of dechlorination products contributed to bioenhanced dissolution of PCE, yielded an enhancement factor between 5 and 7 for the vertical columns and between 1 and 4 for horizontal columns. Bioenhanced dissolution have been investigated in various experimental setups ranging from batches (Amos et al., 2007), flow-trough reactor (Carr et al., 2000), 1-D columns (Yang and McCarty, 2000, 2002, Cope and Hughes, 2001, Amos et al., 2008), 2-D tank (Sleep et al., 2006), 3-D tank (Adamson et al., 2003), and a small 3-D cell (Glover et al., 2007). The observations vary from almost no dissolution enhancement to about 13. Results from column experiments were in the range of 2.1 to 5, which is similar to the values found here. Our horizontal columns in which bypassing of flow around the DNAPL source zone is possible can be compared better to 3-D experiments. Sleep et al. (2006) found a sustained value of 1.7 with a maximum of 3.3. Glover et al. (2007) focussed in a small flow cell with PCE present in a pool. There, dissolution enhancement varied between 4 and 13 for pools with <55% saturation and was a maximum of 1.5 for pools with 74% saturation. The degree of dissolution enhancement has been found to depend on the DNAPL source zone architecture (Chu et al., 2004, Christ et al., 2006, Park and Parker, 2008). This may explain why the horizontal 


5.6. Discussion and conclusions 153 

columns with a DNAPL pool generate a lower dissolution enhancement than the vertical columns with only residual DNAPL. Another variable of dissolution enhancement is flow velocity. Kaplan et al. (2008) showed that PCE dissolution enhancement was lower for high flow velocity compared to lower flow velocity. This indicated that a certain residence time for microorganisms is required before dechlorination occurred. Another reason comes from modelling studies by Seagren et al. (1993, 1994). If the flow velocity is low, the concentration around a NAPL blob will be at solubility concentration. This can then be significantly reduced by biodegradation, resulting in a relatively large effect of enhanced dissolution. But if velocity is high, the concentration around a NAPL blob will be kept low, and biodegradation can not reduce it much further; which means a relatively small effect of biodegradation. On laboratory scale, this effect was observed in a small 2D cell by Glover et al. (2007). Here, we found that the horizontal column with the lowest flow velocity (i.e. highest residence time, column VIII) yielded a lower bioenhanced dissolution factor than the column with a higher flow velocity (column VII). However, this bioenhanced dissolution factor is not only dependent on flow velocity, but also electron donor limitation, and/or bypassing of flow due to bioclogging, or gas formation may have occurred. A numerical model was used to simulate results of our vertical column experiments and to estimate dechlorination and dissolution parameters. Although the complex processes in the column experiments were simplified incorporated in the model, the experimental results were simulated reasonably well. Some processes were not even included in the model, such as electron donor limitations, inhibition, mobilization of residual DNAPL, or permeability changes from dissolution of DNAPL or biomass growth. Some deviations between model and experimental results indicated more advanced (dechlorination) kinetics were required to obtain a better fit. For example, ethene was detected in the effluent of column II only after 160 days, whereas simulation of complete dechlorination (i.e. including VC dechlorination) would have resulted in the appearance of ethene as soon as VC had been produced. One option to overcome this problem is to introduce an inhibitory constraint on VC dechlorination due to the presence of cDCE. Another major observation in modelling columns with residual PCE was that dissolution parameters have probably increased with time when dechlorination occurred. 


154 Chapter 5. Column experiments 

## Bibliography 

Abriola, L. M. (2005), Contaminant source zones: Remediation or perpetual stewardship?, Environmental Health Perspectives, 113 (7), A438–A439. 

Abriola, L. M., K. D. Pennell, and G. A. Pope (1994), Impact of surfactant flushing on the solubilization and mobilization of dense nonaqueous phase liquids in soil columns, Abstracts Of Papers Of The American Chemical Society, 207 (Part 1), 137–ENVR. 

Adamson, D. T., J. M. McDade, and J. B. Hughes (2003), Inoculation of a DNAPL source zone to initiate reductive dechlorination of PCE, Environmental Science and Technology, 37 , 2525–2533. 

Amos, B. K., J. A. Christ, L. M. Abriola, K. D. Pennell, and F. E. L ̈offler (2007), Experimental evaluation and mathematical modeling of microbially enhanced tetrachloroethene (pce) dissolution, Environmental Science and Technology, 41 (3), 963–970, doi:10.1021/es061438n. 

Amos, B. K., E. J. Suchomel, K. D. Pennell, and F. E. L ̈offler (2008), Microbial activity and distribution during enhanced contaminant dissolution from a napl source zone, Water Research, 42 , 2963–2974. 

Aulenta, F., C. Di Tomassi, C. Cupo, M. P. Papini, and M. Majone (2006a), Influence of hydrogen on the reductive dechlorination of tetrachloroethene (pce) to ethene in a methanogenic biofilm reactor: role of mass transport phenomena, Journal Of Chemical Technology And Biotechnology, 81 (9), 1520–1529, doi:10.1002/jctb.1562. 

Aulenta, F., M. Majone, and V. Tandoi (2006b), Enhanced anaerobic bioremediation of chlorinated solvents: environmental factors influencing microbial activity and their relevance under field conditions, Journal Of Chemical Technology And Biotechnology, 81 (9), 1463–1474, doi:10.1002/jctb.1567. 

Bai, G., M. L. Brusseau, and R. M. Miller (1997), Biosurfactant-enhanced removal of residual hydrocarbon from soil, Journal of Contaminant Hydrology, 25 , 157–170. 

Brennan, R. A., R. A. Sanford, and C. J. Werth (2006), Chitin and corncobs as electron donor sources for the reductive dechlorination of tetrachloroethene, Water Research, 10 , 2125–2134. 


Bibliography 155 

Carr, C. S., and J. B. Hughes (1998), Enrichment of high-rate PCE dechlorination and comparative study of lactate, methanol, and hydrogen as electron donors to sustain activity, Environmental Science and Technology, 32 , 1817–1824. 

Carr, C. S., S. Garg, and J. B. Hughes (2000), Effect of dechlorinating bacteria on the longevity and composition of PCE-containing nonaqueous phase liquids under equilibrium dissolution conditions, Environmental Science and Technology, 34 , 1088–1094. 

Christ, J. A., L. D. Lemke, and L. M. Abriola (2005), Comparison of twodimensional and three-dimensional simulations of dense nonaqueous phase liquids (dnapls): Migration and entrapment in a nonuniform permeability field, Water Resources Research, 41 (1), doi:10.1029/2004WR003239. 

Christ, J. A., C. A. Ramsburg, K. D. Pennell, and L. M. Abriola (2006), Estimating mass discharge from dense nonaqueous phase liquid source zones using upscaled mass transfer coefficients: An evaluation using multiphase numerical simulations, Water Resources Research, 42 (11), doi:10.1029/2006WR004886. 

Chu, M., P. K. Kitanidis, and P. L. McCarty (2004), Possible factors controlling the effectiveness of bioenhanced dissolution of non-aqueous phase tetrachloroethene, Advances in Water Resources, 27 (6), 601–615, doi: 10.1016/j.advwatres.2004.03.002. 

Clement, T. P. (1998), RT3D A Modular Computer Code for Simulating Reactive Multi-Species Transport in 3-Dimensional Groundwater Aquifers. 

Clement, T. P., Y. Sun, B. S. Hooker, and J. N. Petersen (1998), Modeling multispecies reactive transport in groundwater, Ground Water Monitoring and Remediation, pp. 79–92. 

Clifford, J. S., M. A. Ioannidis, and R. L. Legge (2007), Enhanced aqueous solubilization of tetrachloroethylene by a rhamnolipid biosurfactant, Journal of Colloid and Interface Science, 305 , 361–365. 

Cope, N., and J. B. Hughes (2001), Biologically-enhanced removal of PCE from NAPL source zones, Environmental Science and Technology, 35 , 2014–2021. 

De Zeeuw, W. J. (1984), Acclimatization of anaerobic sludge for uasb reactor start-up, Ph.D. thesis, Wageningen Agricultural University, The Netherlands. 

Doherty, J., L. Brebber, and P. Whyte (1994), PEST: Model-Independent Parameter estimation., Watermark Numerical Computing. 


156 Chapter 5. Column experiments 

Domenico, P. A., and F. W. Schwartz (1997), Physical and chemical hydrogeology, 2nd ed., John Wiley & Sons, Inc. 

Duhamel, M., S. D. Wehr, L. Yu, H. Rizvi, D. Seepersad, S. Dworatzek, E. E. Cox, and E. A. Edwards (2002), Comparison of anaerobic dechlorinating enrichment cultures maintained on tetrachloroethene, trichloroethene, cis-dichloroethene and vinyl chloride, Water Research, 36 , 4193–4202. 

Glover, K. C., J. Munakata-Marr, and T. H. Illangasekare (2007), Biologically enhanced mass transfer of tetrachloroethene from DNAPL in source zones: experimental evaluation and influence of pool morphology, Environmental Science and Technology, 41 , 1384–1389. 

Isalou, M., B. E. Sleep, and S. N. Liss (1998), Biodegradation of high concentrations of tetrachloroethene in a continuous flow column system, Environmental Science and Technology, 32 , 3579–3585. 

Kaplan, A. R., J. Munakata-Marr, and T. H. Illangasekare (2008), Biodegradation of residual dense nonaqueous-phase liquid tetrachloroethene: Effects on mass transfer, Bioremediation Journal, 12 , 21–31, doi: 10.1080/10889860701866289. 

Lide, D. R. (Ed.) (Internet Version 2008), CRC Handbook of Chemistry and Physics, chap. Standard thermodynamic properties of chemical substances, 88th ed., CRC Press/Taylor and Francis, Boca Raton, FL. 

Mayer, A. S., and C. T. Miller (1996), The influence of mass transfer characteristics and porous media heterogeneity on nonaqueous phase dissolution, Water Resources Research, 32 , 1551–1567. 

McCarty, P. L. (1997), Breathing with chlorinated solvents, Science, 276 , 1521– 1522. 

McDonald, M. G., and A. W. Harbaugh (1988), A Modular Three-Dimensional Finite-Difference Ground-water flow model, U.S.G.S. 

Mulligan, C. N. (2005), Environmental applications for biosurfactants, Environmental Pollution, 133 , 183–198. 

Nielsen, R. B., and J. D. Keasling (1999), Reductive dechlorination of chlorinated ethene DNAPLs by a culture enriched from contaminated groundwater, Biotechnology and Bioengineering, 62 , 160–165. 


Bibliography 157 

Padgett, P. K., and N. J. Hayden (1999), Mobilization of residual tetrachloroethylene during alcohol flushing of clay-containing porous media, Journal of Contaminant Hydrology, 40 (3), 285–296. 

Park, E., and J. C. Parker (2008), Effects of mass reduction, flow reduction and enhanced biodecay of DNAPL source zones, Transport In Porous Media, 73 (1), 95–108, doi:10.1007/s11242-007-9164-x. 

Reid, R. C., J. M. Prausnitz, and B. E. Poling (1987), The properties of gases and liquids, 4th ed., McGraw-Hill; New York, NY. 

Roelofsen, F. J., and C. G. M. Kassels (2003), Development of a numerical simulator for LNAPL weathering. phase 5: Manual for RT3D-OW concept, Tech. rep. 

Roy, J. W., J. E. Smith, and R. W. Gillham (2002), Natural remobilization of multicomponent DNAPL pools due to dissolution, Journal of Contaminant Hydrology, 59 (3-4), 163–186. 

Roy, J. W., J. E. Smith, and R. W. Gillham (2004), Laboratory evidence of natural remobilization of multicomponent dnapl pools due to dissolution, Journal of Contaminant Hydrology, 74 (1-4), 145–161, doi: 10.1016/j.jconhyd.2004.02.009. 

Schwille, F. (1998), Dense chlorinated solvents in porous and fractured media. Model experiments, Lewis Publishers, Chelsea, Michigan. 

Seagren, E. A., B. E. Rittmann, and A. J. Valocchi (1993), Quantitative evaluation of flushing and biodegradation for enhancing in situ dissolution of nonaqueousphase liquids, Journal of Contaminant Hydrology, 12 , 103–132. 

Seagren, E. A., B. E. Rittmann, and A. J. Valocchi (1994), Quantitative evaluation of the enhancement of NAPL-pool dissolution by flushing and biodegradation, Environmental Science and Technology, 28 , 833–839. 

Sleep, B. E., et al. (2006), Biological enhancement of tetrachloroethene dissolution and associated microbial community changes, Environmental Science and Technology, 40 , 3623–3633. 

Wiedemeier T. H., N. C. J. W. J. T., Rifai H. S. (1999), Natural Attenuation of Fuels and Chlorinated Solvents in the Subsurface., John Wiley and Sons., New York. 


158 Chapter 5. Column experiments 

Yang, Y., and P. L. McCarty (2000), Biologically enhanced dissolution of tetrachloroethene DNAPL, Environmental Science and Technology, 34 , 2979– 2984. 

Yang, Y. R., and P. L. McCarty (2002), Comparison between donor substrates for biologically enhanced tetrachloroethene DNAPL dissolution, Environmental Science and Technology, 36 (15), 3400–3404, doi:10.1021/es011408e. 

Zheng, C. (1990), A Modular Three-Dimensional Transport Model for Simulation of Advection, Dispersion and Chemical Reaction of Contaminants in Groundwater Systems, U.S.E.P.A. Report. 

Zysset, A., F. Stauffer, and T. Dracos (1994), Modeling of reactive groundwater transport governed by biodegradation, Water Resources Research, 30 , 2423– 2434. 


## Chapter 6 

# Large two-dimensional 

# laboratory experiment with 

# dechlorination of a PCE source 

# zone. 

## 1 

## Abstract 

To investigate the effects of bioremediation on DNAPL source zones, we carried out a series of experiments in a two-dimensional tank filled with sand. A microbial assemblage originating from a field site contaminated with chlorinated ethene was used for inoculation without enrichment. Injection of 250 ml tetrachloroethene (PCE) into the tank yielded a residual zone of PCE with a pool at the bottom. After this injection, the tank was continuously flushed with anaerobic water containing sufficient electron donor and various nutrients. Chlorinated ethenes analysis, microbial groups counting, and the visual observation of the dyed PCE showed that PCE was dechlorinated in the source zone. Bio-enhanced dissolution is believed to have occurred as the total chlorinated ethene concentration was about four times higher than the solubility limit of PCE. Moreover, an increased PCE solubility limit in the source zone and mobilization of residual PCE were observed. Dechlorination of cDCE to vinyl chloride (VC) occurred 

(^1) This chapter has been prepared for submission to Journal of Contaminant Hydrology as: Langevoort, M., Hassanizadeh, S.M., Leijnse, A., Kleingeld, P.J., and Bouw, L.; Large twodimensional laboratory experiment with dechlorination of a PCE source zone 


160 Chapter 6. Tank experiments 

only when PCE concentrations were low (<0.1 mM). Similarly, transformation of VC to ethene occurred only after cDCE concentrations became low. After one year of experiment, approximately 135 ml of PCE had left the tank mainly as cDCE (73%). PCE left in the tank was 90 ml and was only present in the pool. This amounts to a total PCE of 225 ml, which is 10% less than the volume injected into the tank. Spatial moment analysis were performed to investigate the general plume behavior. This was compared to a model simulation with a modified version of RT3D that accounted for DNAPL dissolution and biodegradation. 

## 6.1 Introduction 

Chlorinated solvents in the form of dense non-aqueous phase liquids (DNAPLs), such as tetrachloroethylene (PCE), are common forms of environmental contamination. Chlorinated solvents are highly toxic and carcinogenic substances; their presence in the subsurface poses environmental and human health risks and sites contaminated by chlorinated ethenes often require remediation. DNAPL removal is not straight forward. Because of gravitational and capillary forces, source zones are formed that are characterized by residual ganglia and high-saturation pools located at capillary interfaces often far below groundwater table. Another complication for remediation is the low solubility of DNAPLs, which may result in a continuous delivery of DNAPL to the groundwater for decades (Schwille, 1998) and reduces effectiveness of many remediation methods. Bioremediation is an effective method for remediation of chlorinated solvent contaminations. In general, chlorinated solvents can be biologically degraded under reducing conditions by dehalogenation. The transformation of PCE to trichloroethylene (TCE) and cis-dichloroethylene (cDCE) can be performed by a variety of anaerobic bacteria. The dechlorination of less chlorinated hydrocarbons can only be performed by members of the Dehalococcoides group (Maym ́oGatell et al., 1995, He et al., 2003). Extensive research has been done on biodegradation of PCE using laboratory experiments. These studies have dealt with either plume or source zone remediation (Fure et al., 2006). Most experimental studies (e.g. de Bruin et al., 1992, Isalou et al., 1998) have involved PCE at low concentrations, which is indeed relevant to the majority of PCE plumes encountered in the field (e.g. Major et al., 2002, Ellis et al., 2000). The ability of microorganisms to degrade high PCE concentrations has been given little attention in the past, mainly because saturation concentrations of chlorinated solvents and the presence of a DNAPL were believed to be toxic to microorganisms (Aulenta et al., 2006). Recently, however, 


6.1. Introduction 161 

there has been growing interest in the application of biodegradation to source zones where PCE is present at high concentrations and as a non-aqueous phase liquid (NAPL). 

The possibility to degrade chlorinated solvents near and within source zones, offers the potential to increase the mass flux from the NAPL to the water and to reduce source longevity. In particular, researchers have observed dissolution enhancement factors of two (Yang and McCarty, 2000) to thirteen (Glover et al., 2007) (one is no enhancement). This can be a result of the increase in the concentration gradient over the NAPL-water interface and/or of the increase of the PCE solubility limit (Kaplan et al., 2008). 

Bioremediation of DNAPL source zones may not only affect mass flux by altering the physical and chemical interaction of the NAPL with its surrounding, but can also change the composition of NAPL itself. The secretion of biosurfactants by bacteria can lead to the increase in the aqueous-phase solubility of NAPL components (Clifford et al., 2007), or mobilization of DNAPL, by the reduction in interfacial tension (Bai et al., 1997). 

Experimental studies of biodegradation of PCE has been carried out at different scales. Early studies were batch experiments, which showed biodegradation of dissolved PCE at concentrations around solubility (Sharma and McCarty, 1996, Yu and Semprini, 2004) and in the presence of PCE phase (Amos et al., 2007). Column experiments have also shown that biodegradation occurred when PCE phase was present (chapter 5 Nielsen and Keasling, 1999, Carr and Hughes, 1998, Yang and McCarty, 2000, Glover et al., 2007, Kaplan et al., 2008, Amos et al., 2008). Later studies involved higher NAPL saturations. For example, Kaplan et al. (2008) and Amos et al. (2008) used residual saturations of 0.35 and 0.2, respectively, in their column experiments. 

In small-scale setups, as in batch experiments, conditions are well mixed and homogeneous. Column experiments provide more heterogeneous conditions, but these are still not representative of field situations. For instance, in column experiments, flushing solutions are forced through the contaminated zone and bring about dissolution of entrapped NAPL and biodegradation via electron donor availability. However, under field conditions, bypassing of flow around the DNAPL source zone may occur and preferential flow paths may develop. This can be caused by the presence of the DNAPL itself or due to biofilms and bioclogging that may change the hydraulic properties of the system (Thullner et al., 2002, 2004, Hill and Sleep, 2002). To investigate the effects of bioremediation on source zones in the field, larger scale experiments are needed as the complexity of flow processes influenced by source zone architecture, clogging or the for


162 Chapter 6. Tank experiments 

mation of biosurfactants may not be captured by microcosm or column studies (Aulenta et al., 2006, Oostrom et al., 2006). Larger scale experiment can account for micro-heterogeneities as these are known to exist even in apparently homogeneous soil layers. Only a few large-scale experiments on bioremediation of PCE have been performed: one on dissolved PCE (10100 x 700 x 200 mm by Cirpka et al., 1999), one with one liter PCE in a very large container (5490 x 2130 x 1830 mm by Adamson et al., 2003) and one with 10 ml PCE (760 x 380 x 25.4 mm by Sleep et al., 2006). The main objective of the first two studies was to evaluate the ability to inoculate a non-dechlorinating porous medium, whereas Sleep et al. (2006) continued after bioaugmentation to study the biological enhancement of PCE dissolution. Spatial distribution of PCE concentrations indicated that only residual PCE was present in their tank, and a pool at the bottom was absent. However, DNAPL dissolution from pools is different from residual zones (Parker and Park, 2004). The long-term persistence of DNAPL is controlled by slow dissolution of DNAPL from pools. Glover et al. (2007) investigated the effect of biodegradation on PCE dissolution from pools, but in a small experimental setup (50 mm long with a diameter of 25 mm) over a short term. To address the long-term effect of biodegradation of DNAPL source zones in the field, we performed a two-dimensional tank experiment. PCE was spilled into a tank (2000 x 940 x 45 mm) containing homogeneous sand resulting in a residual zone and a high-saturation pool. A microbial assemblage was used for inoculation that originated from the field. At the scale of our experiments, we expect micro-heterogeneities to have formed in the sand packing. We have seen evidences of it in the irregular architecture of the residual PCE zone. The purpose of the experiment was to investigate DNAPL source zone processes in the presence of biodegradation and to obtain a data set for model development and testing. The results of this research will increase our knowledge of source zone biodegradation and can be used to assist in the assessment and clean-up of contaminated sites. 

## 6.2 Material and Methods 

### 6.2.1 Chemicals 

The DNAPL used in the tank experiment, PCE (≥ 99.9% purity), was ordered from Merck BV. PCE was dyed with 0.5 g l−^1 Sudan Red B (Fluka) in order to make the flow and distribution pattern of the DNAPL qualitatively visible. For 


6.2. Material and Methods 163 

the calibration of the liquid degradation products, the following chemicals were purchased from Merck BV; TCE (≥ 99.5%), cDCE (≥ 98%), and 1,1-dichloroethylene (1,1DCE, ≥ 99.9%) and from Sigma-Aldrich: trans-dichloroethylene (tDCE, ≥ 98%). For the calibration of the gaseous degradation products, the gases VC, ethene, ethane, and methane (all ∼5 vol%) were obtained from Air Products (Brussels) in a helium gas cylinder. An anaerobic medium solution was prepared for optimal conditions for biodegradation and contained: 2 mM Na-acetate, 5 mM K-L-lactate, 1.6 mM NH 4 Cl, 0.37 mM KH 2 PO 4 , and 16.4 mM NaHCO 3 in distilled water. Resazurin (1 mg l−^1 ) (Sigma-Aldrich) was added as a redox indicator and 1 ml l−^1 of a solution with several trace elements (De Zeeuw, 1984) was added. This medium solution contained 76 electron donor equivalents on CO 2 basis, which is theoretically sufficient to dechlorinate 9.5 mM PCE completely to ethene. 

### 6.2.2 Description of the tank setup 

The tank (see Figure 6.1) was made of a steel box and a glass cover. The main body was constructed of one piece of 1.5 mm thick stainless steel (AISI 316, DTO/MOP, TUDelft, The Netherlands) formed into a box with inner dimensions of 2080 x 940 mm and a depth of 45 mm. The front glass wall (Lamon Glas, The Hague, The Netherlands) was 19-mm thick. Two constant head chambers were made at the two ends of the tank. The porous medium, placed between the two walls, had effective dimensions of 2000 x 940 x 45 mm. The chambers were separated from the sand by a perforated stainless steel sheet (Metaalketen, The Hague, The Netherlands). To prevent sand entering the chambers, they were covered with saltwater-resistant stainless steel mesh, SS 316, with a mesh size of 105 μm and a thread thickness of 65 μm (Kabel Zaandam BV, The Netherlands). The mesh combined with the perforated stainless steel allowed the fluid to pass through, but kept the sand out of the water chambers. In our experiments, water flowed from left to right. The inflow chamber at the left had six inflow valves (Eriks, Alkmaar, The Netherlands) and the outflow chamber had only one (see Figure 6.1). Both side chambers were equipped with a valve at the top to allow gas, which could be formed during biotic experiments, to be released. At the bottom of the tank, four valves were installed for safety, one in each water chamber and two in the sand chamber. These last two valves were covered with stainless steel mesh to prevent outflow of sand. At 750 mm from left water chamber, the tank featured one inflow valve at the top for the injection of DNAPL into the tank. 


164 Chapter 6. Tank experiments 

 1 

 2 

 3 

 4 

 5 

 6 

 7 

 8 

 9 

 10 

 11 12 13 

 14 15 16 

 17 18 19 

 20 

 21 

 22 

 23 

 24 

 25 

 26 

 27 

 28 

 29 

 30 

 31 

 32 

 33 

 34 

 35 

 36 

 37 

 38 

 39 40 41 

 42 43 44 

 45 46 47 

 48 

 49 

 50 

 51 

 53 52 

 54 

 55 

 56 

 57 

 58 

 60 

 61 

 62 63 64 

 65 66 67 

 68 69 70 

 71 

 72 

 73 

 74 

 75 

 76 

 77 

 78 

 79 

 80 

 81 

 82 

 83 

 84 

 85 

 59 

 Bentonite layer 

 Inflow chamber 

 Kaolinite 

 Thickness of the tank is 40 mm 

 99.5%0.5% 

 N^2 CO^2 

 Reservoirmediumsolution 

 Wastereservoir 

 Gas phaseconnected tothe fume hood 

 250 ml PCE in 

 Membranepump 

 Peristalticpump 

 Redoxprobe 

 Redoxprobe 

 1 

 2 

 3 

 4 

 5 

 6 

 7 

 8 

 9 

 10 

 11 

 12 

 13 

 14 

 15 

 0 40 

 640 

 790 

 1280 

 1390 

 2040 

 2080 

 0 940920870 700 530490 360 19010020 

 Kaolinite 

 Outflowchamber 

 Reinforcementsteel beams 

 Figure 6.1: 

 Schematic of the tank setup drawn to scale; numbers 1 to 85 are sampling ports; italic, underlined numbers 1 to 15 are 

 TDR probes; dimensions in mm. 


6.2. Material and Methods 165 

A number of measurement points were built into the steel wall of the tank. These included 15 triple-wire Time Domain Reflectometry (TDR) probes (indicated by italics underlined numbers in Figure 6.1). The length of the TDR probe was approximately 40 mm (i.e. equal to the sand thickness), and the inner wire was about 2 mm shorter than the two outer wires (see Figure 6.2). All wires had a diameter of 4 mm. The probes were distributed in five rows of three probes in each row, positioned in the expected flow path of the NAPL from the PCE inlet valve to the bottom of the tank, i.e. in the region where the DNAPL source zone was expected to form. There were 85 sampling ports. These were distributed in three rows of 22 ports in each row, three rows of five ports and two sampling ports in each end chamber. A sampling port (see Figure 6.2) consisted of a M6, stainless steel bolt, in which a short pipe (with diameter 2 mm) was inserted with its end opening at halfway the tank thickness. They allowed periodic sampling of phases (aqueous phase, NAPL or gas) present at this position in the tank. Each port was connected to a viton tubing, which was closed by folding and securing it with an aluminum ring (5 mm). It was also equipped with a luer lock connection to facilitate sampling with a gas tight syringe (see Figure 6.2). To prevent leakage, viton o-rings (Eriks, Alkmaar, The Netherlands) were placed around the TDR probes and water sampling ports. 

 13.5 mm 

 40 mm 

 4 mm 

 68 mm 

 2 mm 

 i) 

 ii) 

 Luer lock connection 

 Clamp for closing tube 

 Figure 6.2: Top-view presentation of a sampling port i) and a TDR probe ii) in the tank. 


166 Chapter 6. Tank experiments 

Redox measurement probes were installed at both ends of the tank (see Figure 6.1). In the inflow chamber, a weld-in socket was designed for the housing of a retractable redox probe (Mettler Toledo housing type InTrac777-SLM, Elscolab, Utrecht, the Netherlands). The socket was inclined with an angle of 15 °C above the horizontal to allow measurements at the tip of the probe, free of gas bubbles. The probe measured in situ, and could be cleaned while retracted without exchanging fluids between the tank and the outer environment. This allowed maintaining anaerobic conditions in the tank during the experiments, in case the probe needed to be cleaned or calibrated. In the outflow tube of the tank, a second redox probe was placed in a housing (Mettler Toledo housing type InFit761-25BTB, Elscolab, Utrecht, the Netherlands). Both probes were combined Eh/reference probes that corrected for temperature differences (Elscolab, Utrecht, the Netherlands). The redox probes were mainly used to verify that sustained reducing conditions existed in the tank over the course of the experiment. 

### 6.2.3 Packing of the tank 

Before filling the tank with sand, a non-swelling clay lining (kaolinite, Ankerpoort NV., Geertruidenberg, The Netherlands) was placed at the bottom of the tank in the form shown in Figure 6.1. The purpose of this layer was to prevent DNAPL from flowing into the water chambers and/or out of the tank. Kaolinite clay powder was mixed with water, forming a paste that was firmly placed in the open tank with glass wall removed and its steel wall in horizontal position. The clay layer length at the left side was 600 mm and at the right side 800 mm. The maximum height of the clay, at both ends of the sand chamber, was 100 mm. Then, the glass plate was mounted and the tank was put back in vertical position and set to level. Viton layers (Peter van den Berg, Barendrecht, the Netherlands) were placed between the steel box and the glass front wall and between the steel box and the top lid. Although tank walls were relatively thick and rigid, during some preliminary experiments, the walls bulged under pressure of sand and water. To remedy the situation, later on five iron beams were fitted around the tank at approximately 400 mm spacing. Once in vertical position, the top lid was removed to allow pouring sand into the tank. The tank was packed under water saturated conditions. The sand had grain diameters between 0.1 and 1 mm with a median diameter of 0.4 mm (Quartzsand H31, Sibelco, Belgium). Prior to packing, the sand was boiled to completely clean the grains and to make them water wet. The sand was transported into the tank via a tube by flowing water. The top surface of the deposited sand was continuously brushed with a comb-like tool to prevent formation of 


6.2. Material and Methods 167 

microlayers. A 20-mm layer of a commercially available Wyoming bentonite, marketed under the name Colclay A90T M^ (Ankerpoort NV., Geertruidenberg, the Netherlands), was added at the top to completely fill the tank. Because of its swelling property, a bentonite layer would ensure complete sealing of the tank, even if sand would settle at a later stage. This would also prevent preferential flow of water along the top edge of the tank. The tank was placed in a room maintained at 20 ± 1 °C. 

### 6.2.4 System startup 

Following packing of the tank, a tracer experiment was performed, as described below. After that, the tank was made anaerobic by flushing the tank with five pore volumes of anaerobic medium solution from a 20-liter reservoir (Fisher Emergo, Landsmeer, The Netherlands). To ensure the full reduction of the medium solution, approximately 2 mg l−^1 of sodium dithionite (Na 2 O 4 S 2 , Merck) was added to it and the reservoir was continuously flushed with 99.5% N 2 0.5% CO 2 -gas. To inoculate the tank, it was flushed with two pore volumes of groundwater containing a dechlorinating microbial assemblage provided by Bioclear B.V.. The groundwater was obtained from a monitoring well 10 m below ground surface at a PCE-contaminated site, Evenblij in Hoogeveen (The Netherlands). This monitoring well was placed in a source zone at the site where enhanced bioremediation by bioaugmentation had been applied from 2001 to 2003. This bioaugmentation consisted of an on-site bioreactor, with dechlorinating capacity. Groundwater was continuously pumped up and mixed with electron donors (acetate and lactic acid) before being injected back into the subsurface. At the time that the enhanced bioremediation had been stopped, the source zone was still not completely removed. The dechlorinating microbial assemblage was able to dechlorinate PCE to ethene and ethane. The start of our experiments was three years after the enhanced bioremediation had been stopped. Groundwater was collected anaerobically in three 25-liter, stainless-steel pressure vessels (UCON AF Containersysteme KG, Haiger, Germany). In the laboratory, the groundwater with the dechlorinating microbial assemblage was stored at ± 10 °C before injection into the tank, for a maximum of three days. In order to transfer water from vessels to the tank, nitrogen gas (with composition 99.5% N 2 0.5% CO 2 -gas) was injected into the vessels. This method allowed anaerobic transfer of groundwater and inoculation of the tank. The flow rate was approximately 75 ml min−^1. After inoculation, the tank was run under closed conditions (i.e. the effluent was recirculated back into the tank) for 35 days to permit attachment of bacteria. To establish biodegradation, halfway 


168 Chapter 6. Tank experiments 

this period, one ml of 14 mM PCE dissolved in methanol was injected halfway the flow path in sampling ports 67, 44, 16, 73, 50, and 22. 

### 6.2.5 PCE injection and biodegradation 

PCE, flushed with argon gas, was pumped in using a peristaltic pump (Masterflex) with viton tubing through the PCE injection port at the top of the tank. A total of 250 ml was injected in three hours. The choice of the PCE volume and injection rate was based on simulations with the STOMP simulator (White and Oostrom, 1996). We calculated the volume of PCE that was needed to obtain a residual zone and a pool, contained between clay linings at the bottom of the tank. During PCE injection, groundwater flow was stopped by maintaining equal head in the two water chambers of the tank. The DNAPL was allowed to equilibrate for one day before horizontal water flow with medium solution was resumed. Effluent was collected as waste water and was discharged properly. The start of the experiment is considered to be the onset of the water phase flow, i.e. day 0 is one day after the injection of PCE. During the first week, the inflow rate was set to 2 ml min−^1 to establish a plume. Thereafter, the flow rate was reduced to 1 ml min−^1. The flow rate was controlled by a Stepdos FEM08 TT.18 RC membrane pump (KNF Verder, Vleuten, The Netherlands) connected to one of the inflow valves of the inflow chamber. A constant head level was maintained at the outflow boundary by means of pumping excess water. This flow rate yielded an interstitial velocity of about 100 mm day−^1 (the residence time in the tank was approximately 20 days), which corresponds to typical field velocities. To get a general insight in the diversity of the microbial population, a quantitative-polymerase chain reaction (q-PCR) analysis was performed under standard conditions by Bioclear B.V. (The Netherlands, personal communication). From eight sampling ports, 5-ml liquid samples were collected using 5-ml gas tight syringes just before the injection of PCE on day -1 and on day 180. Three groups of bacteria were quantitatively analyzed: Bacteria, Archeae, and Dehalococcoides spp. (Dhc); the latter being a group of microorganisms able to degrade dechlorinated ethenes. This Dhc bacteria belongs to the domain Bacteria. 

### 6.2.6 Sampling scheme 

Over the course of the study, liquid samples (0.4-1.0 ml, depending on the concentration) were collected from the sampling ports using 0.5or 1-ml gas tight syringes (Alltech, The Netherlands). The samples were used for analysis of total 


6.2. Material and Methods 169 

dissolved organic carbon, PCE and degradation products. The dissolved organic carbon was monitored three times over the course of the experiment (see Table 6.1) to have an idea about the electron donor presence in the tank. Samples were taken from the medium inflow reservoir and from several sampling ports. The determination of the dissolved organic carbon (DOC) content of water samples was carried out using a Shimadzu TOC-5050A analyzer. Before analysis, the samples were acidified with HCl and sparged to remove inorganic carbon. The samples were oxidized to CO 2 in a combustion tube with an oxidation catalyst at 680 °C. The CO 2 was measured in a non-dispersive infrared (NDIR) gas analyzer. 

 Table 6.1: DOC measurements. 

 Day Port samples 27 Influent, 39 95 and 266 Influent, 39, 60, 65, 71, 75, 79 9, 14, 20, 24, 28 

Analysis for PCE and degradation products were performed by gas chromatography as described in Chapter 5. Samples were taken once a week. Not all ports were sampled every week, but only ports where variations in composition were expected, as reported in Table 6.2. Ports were sampled starting from the bottom of the tank going up a column of ports and proceeding from the outlet to the inlet side. Sampling in the source zone started 30 days after PCE injection to minimize disturbance of the onset of biodegradation in the system. Samples had only contact with viton, stainless steel and glass and were exposed to the atmosphere for only a few seconds prior to capping of the vials. Cross contamination between samples was avoided by rinsing the syringe with methanol once and distilled water twice. The total volume of liquid removed in one round of sampling had no significant effect on the liquid conditions in the tank or the flow. The total liquid volume in the tank was in the order of 100 liters, whereas the maximum amount of liquid extracted for measurements was 32 ml (maximum of 32 samples were taken in about one hour). 

### 6.2.7 TDR measurements 

TDR measurements are based on the quantification of the attenuation of a voltage pulse transmitted along a transmission line. Generally, a TDR probe is installed in 


170 Chapter 6. Tank experiments 

 Table 6.2: Sampling period of ports for GC analysis. 

 Port being sampled Sampling period between days: 3, 20, 48, 71 0 364 4, 24, 52, 75 5, 28, 56, 79 16, 67 30 364 13, 41, 64 40 170 14, 42, 65 40 210 12, 40, 63 50 125 43 50 275 83, 84, 85 75 340 29, 80 75 364 18, 46, 69 125 364 15, 66 175 275 17, 44, 45, 68 175 364 22, 50, 73 230 364 2, 11, 39, 62 Occasionally 9, 37, 60 Occasionally 

such a manner that the soil forms the dielectric material of the transmission line. Any discontinuity in impedance causes a change in the reflected voltage at the beginning of the transmission line, which is recorded by a cable tester with time. An interpretation of the waveform yields information on the water content and the bulk electrical conductivity, as these have a large influence on the dielectric properties of the soil. 

The TDR method is based on the determination of the apparent dielectric permittivity, Ka, of the soil, which can be calculated with: 

 Ka = 

#### ( 

 c∆ts 2 L 

#### ) 2 

 = n^2 a (6.1) 

where c is the speed of electromagnetic waves in vacuum (3· 108 ms−^1 ), ∆ts is the travel time in the soil, L is the length of the probe embedded in the soil, and na is 


6.2. Material and Methods 171 

the apparent refractive index. The travel time in the soil can be calculated by: 

 ∆ts = ∆tp − ∆t 0 (6.2) 

where ∆tp is the total travel time in the probe and ∆t 0 is the travel time through the epoxy resin of the probe (Heimovaara, 1993). The water content can be calculated by assuming that the apparent refractive index is made up of the sum of the refractive indices in soil, ns, water, nw, and NAPL, nn. The equation becomes: 

 na = Θsns + Θwnw + Θnnn (6.3) 

where Θs, Θw, and Θn are the content of, respectively, sand, water, and NAPL. With the following relations, Equation 6.3 can be solved for the water content. 

 Θs = ρb ρs 

#### (6.4) 

 Θs + Θw + Θn = 1 (6.5) φ = 1 − Θs (6.6) 

where φ is the porosity. Time domain reflectometry waveforms were obtained with the automated TDR measurement system developed by Heimovaara and Bouten (1990) and borrowed from the Institute for Biodiversity and Ecosystem Dynamics (IBED), University of Amsterdam, The Netherlands. TDR measurements were performed using a Tektronix (Beaverton, OR) 1502B cable tester connected to a PC through the Tektronix SP232 serial interface. The triple-wire probes were connected to the cable tester with a coaxial cable with a length of 4.5 m. The automated TDR measurement system stored waveform data together with all cable-tester settings. Two types of waveforms were stored, standard waveforms with 251 points that are normally used for the traditional time-domain analysis and waveforms with 2048 points that could be used for the frequency-domain analysis (Heimovaara, 1994, Heimovaara et al., 1996). For the tracer experiments, automated measurements were made every half hour, whereas over the course of the PCE experiment every two hours a measurement was performed. 

### 6.2.8 Head measurements 

To get a general view of the flow field in the tank, heads in all sampling ports were measured with an overall horizontal flow rate of 5 ml min−^1 before the tank was made anaerobic for inoculation and biodegradation. Furthermore, experiments 


172 Chapter 6. Tank experiments 

were performed to determine the hydraulic conductivity. The hydraulic conductivity was estimated in two ways. First, by the falling head method (Domenico and Schwartz, 1997) over the whole tank. A water reservoir was connected to the inflow chamber of the tank. It was placed above the tank at a known initial level and the head was allowed to fall, whereas at the outflow boundary of the tank, the head was kept constant. From the known volume of water flown into the tank over a certain time, the average hydraulic conductivity of the whole tank was calculated. In the second method, first a steady state flow rate of 16 ml min−^1 was established. Then, from measurements of hydraulic head at a row of sampling ports (starting with port 7), and using Darcy’s Law, the hydraulic conductivity distribution along the row was calculated. 

### 6.2.9 Tracer experiments 

Before the biotic experiment, a nonreactive tracer study was performed to investigate the flow field and estimate the horizontal transverse dispersivity, αl, in the tank. The flow rate and the concentration of the tracer were chosen so as circumvent gravity effects. The influence of gravity can be observed by the dimensionless gravity number, Ng, which is the ratio of gravitational to viscous forces and calculated as follows: 

 Ng = 

 k 0 g∆ρ μq 0 

#### (6.7) 

where k 0 is the intrinsic permeability, g is the gravity acceleration (9.81 m s−^1 ), ∆ρ is the density difference of invading and residence fluids, μ is the viscosity, and q 0 is the specific discharge. A gravity number much less than unity is desirable to avoid density effects in tracer experiments. Before injecting the tracer, a steady-state horizontal flow of distilled water of 20 ml min−^1 was established. Then the inflow was switched to a solution of distilled water with potassium chloride (C 0 = 2 g l−^1 KCl), pumped into the tank at the same flow rate (20 ml min−^1 ). This yielded a gravity number of 0.06, which was considered to be small enough. The tracer solution was injected for nine hours after which the flow of distilled water was continued at the same rate. The fifteen TDR probes were automated to measure every half hour. The 15 breakthrough curves were used to quantify local interstitial velocities and dispersivities. Electrical conductivity, σdc, was calculated from the 2048 points TDR wave


6.2. Material and Methods 173 

forms by σdc = 1 − ρ∞ (6.8) 

where ρ∞ is the reflection coefficient. The electrical conductivity was plotted with time to obtain salt breakthrough curves. Dispersion coefficients were determined by fitting the observed breakthrough curves to an analytical solution of the 1D advection-dispersion equation (see 5). Another tracer experiment was performed at the end of biodegradation, after disappearance of the source zone in order to investigate changes in flow pattern. The steady-state horizontal flow of medium solution was established at 20 ml min−^1 for one hour, before a medium solution with potassium chloride (C 0 = 2 g l−^1 KCl) was pumped into the tank at the same flow rate. The tracer solution was injected for 0.5 day. At that time, due to a technical problem, the pump started to inject gas into the tank. The problem was discovered and solved at time equal 0.7 day, at which time the medium solution was pumped in until day 1.1. 

### 6.2.10 PCE volume at the end of the experiment 

After the tracer experiments, on day 366, the flow was switched off and the amount of PCE left in the tank was determined to check the mass balance. The water in the tank was drained via the outflow port. One valve at the top in the outflow chamber was open to have atmospheric pressure. No pressure was applied. The tank was placed in horizontal position to open the tank by removing the glass plate. Six soil samples were taken from areas shown in Figure 6.3. Samples A and B were located in the area with residual PCE and four other samples contained the complete PCE pool. The complete sampling procedure was performed as fast as possible to minimize losses due to volatilization. Two samples were taken at the same time (one sample took 15 minutes after the glass plate was removed). Samples A and B were first taken, as their PCE concentration was expected to be lower than in the pool. The soil samples were put in a 2-liter bottle together with about one liter of 2-propanol (Merck). After five days of mixing on a shaker table, the solvent was analyzed for PCE by high-performance liquid chromatography (HPLC). Analysis were performed at the Institut f ̈ur Wasserbau of Universit ̈at Stuttgart. 

### 6.2.11 Spatial data analysis 

Contour lines of PCE, cDCE, VC and ethene concentrations were prepared through spatial interpolation using a kriging method. Beside the concentrations actually 


174 Chapter 6. Tank experiments 

 1 2 3 4 5 

 6 7 8 9 10 11 12 13 14 18 19 20 21 22 23 24 25 26 27 28 29 

 30 31 32 33 34 

 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 

 57 58 60 61 62 63 64 65 69 70 71 72 73 74 75 76 77 78 79 80 

 81 82 83 84 85 59 

 250 ml PCE in 

 A 

 B 

 C D FE 

Figure 6.3: Location of the soil samples (A to F) for the analysis of the remaining PCE after one year of experiment. 

measured at various sampling ports, nine points upstream the source zone were included with zero concentration; these points correspond to sampling ports 1, 7, 35, 58, 2, 11, 39, 62, and a point below port 2. Indeed, occasional analysis of water samples in the upstream ports 2, 11, 39, and 62, closest to the source zone, yielded zero concentration for all chlorinated ethenes. Also, two points at the bottom of the tank, in the pool, were added with a PCE concentration of 1.2 mM, the solubility limit of PCE. No water samples were taken in this zone, but measurements at the end of the experiment showed that large amounts of PCE were still present in the pool. For cDCE, VC, and ethene, no points in the pool were defined, as no information was available about their concentration. The ordinary kriging calculation was performed on a 100 mm x 47 mm grid, taking into account a minimum of four and a maximum of eight surrounding observations around the grid point in question. A variogram was determined for the PCE concentration data using the EasyKrig program for Matlab (Chu and Gentleman, 1998). Interpolated data were manually controlled to match the measured concentration at the sampling port. To further analyze the spatial data, the method of spatial moments was used. The plume development, displacement and dispersion, as a function of time were 


6.2. Material and Methods 175 

described. Following French (1999), the total mass of a component in the aqueous phase, M 00 , was described by the zeroth moment: 

 M 00 (t) = D 

∫ (^940) 0 ∫ (^2000) 0 nS (^) w(x, y, t)c(x, y, t)dxdy (6.9) where D is the thickness of the tank, n is the porosity, S w^ is the water saturation, c is the component concentration, x, and y are spatial coordinates, and t is time. The first moment was defined as: M 10 (t) = D ∫ (^940) 0 ∫ (^2000) 0 nS (^) w(x, y, t)c(x, y, t)xdxdy (6.10) M 01 (t) = D ∫ (^940) 0 ∫ (^2000) 0 nS (^) w(x, y, t)c(x, y, t)ydxdy (6.11) The center of mass in the horizontal and vertical directions, xc, yc, was found by the first moment about the origin normalized by the total mass: xc(t) = M 10 (t) M 00 (t) 

#### (6.12) 

 yc(t) = 

 M 01 (t) M 00 (t) 

#### (6.13) 

The second spatial moment in the horizontal and vertical directions are given by: 

 M 20 (t) = D 

∫ (^940) 0 ∫ (^2000) 0 nS (^) w(x, y, t)c(x, y, t)(x − xc)^2 dxdy (6.14) M 02 (t) = D ∫ (^940) 0 ∫ (^2000) 0 S (^) w(x, y, t)c(x, y, t)(y − yc)^2 dxdy (6.15) where the variances in horizontal and vertical directions, σ^2 xx, σ^2 yy, were described as: σ^2 xx(t) = M 20 (t) M 00 (t) 

#### (6.16) 

 σ^2 yy(t) = 

 M 02 (t) M 00 (t) 

#### (6.17) 


176 Chapter 6. Tank experiments 

## 6.3 Experimental results 

### 6.3.1 Head measurements 

In Figure 6.4, the head measurements are shown for the case of an overall horizontal flow rate of 5 ml min−^1. This distribution corresponds to a relatively uniform flow field with some deviations from the ideal, constant flow field. This indicates that the sandbox packing was reasonably homogeneous. 

 Distance (mm) 

 Distance (mm) 

 Head distribution 

 46.7 

 46.6 

 46.5 46.5 

 46.4 46.4 

 46.4 

 46.3 46.2 

 46.1 46.2 46.3 

 46.3 

 0 500 1000 1500 2000 0 

 200 

 400 

 600 

 800 

 Figure 6.4: Head measurements of the tank with a flow of 5 ml min−^1. 

Measurements based on falling head method yielded an average hydraulic conductivity of 22.3 m day−^1 with a standard deviation of 1.8 m day−^1 (based on 16 measurements). For this determination, an averaged height of 883 mm was used (to account for the presence of the clay). Using the second method, i.e. based on manometer measurements, an overall conductivity at 340 mm from the bottom of 53.3 m day−^1 was determined with a standard deviation of 34.2 m day−^1 (based on 9 measurements). This was based on the assumption that along this line velocity was constant, which was calculated from the overall discharge. This last method is less representative for the whole tank and deviation from the average is much higher than in the determination with the falling head method. 


6.3. Experimental results 177 

### 6.3.2 Tracer experiments 

In Figure 6.5, the breakthrough curves measured with the TDR probes before the biotic experiments are shown along with simulated curves. Note that the five graphs are shown in the same order as the corresponding probe row in the tank. The arrival times at probes 2, 5, 8, 11, and 14, which are at the same distance from the inlet, are not the same. Probes 2 and 14 show some delay. In general, it seems that the uppermost and lowermost row of probes showed a slower breakthrough. Probably, in these areas flow is affected by the boundaries of the tank. Moreover, dispersed clay particles at the top may have caused a lower permeability. But, in general, travel times for different positions in the tank verified that a relatively uniform flow field had been achieved. The average longitudinal dispersivity, αl, was determined to be 1.12 mm, with a standard deviation of 0.24 mm, based on fifteen breakthrough curves. In Figure 6.6, the breakthrough curves measured with the TDR probes after the biotic experiment are shown. From 0 to 0.5 day, tracer was injected. At that time, due to a technical problem the pump started to inject gas into the tank at the same flow rate. Medium solution was injected from day 0.7 until 1.1. It is evident that these breakthrough curves show a more complicated behavior than the curves shown in Figure 6.5 (from before biodegradation experiments). The curves show multiple slopes. The arrival of front at second, third, and fourth rows of probes is faster here than in Figure 6.5. This can be explained by the formation of gas due to biological activity during the experiment. Gas could have collected in the largest pores in the upper half of the tank, reducing the porosity available to flow. These curves also show two slopes in the breakthrough curves, indicating that regions with slow delivery were present, i.e. a dual porosity system had developed. At the bottom row of TDR probes, the influence of gas was minimal. This is in agreement with the visual observation of gas formation from the glass side of the tank. The flow at this row was less than in the area above, probably caused by a boundary effect on the clay and on the present DNAPL pool. 

### 6.3.3 PCE source zone architecture 

At the end of the PCE injection, a residual zone was formed directly below the injection point. It had a rather irregular shape, increasing in width towards the bottom. Also, a small pool was formed at the bottom of the tank. After one day, as all mobile PCE had sunk, the pool thickness increased to about 4 cm. The pool stayed between the two kaolinite clay layers at the bottom. The distribution of 


178 Chapter 6. Tank experiments 

 0 0.2 0.4 0.6 0.8 1 

 0 

 0.5 

 1 Probe 13 Probe 14 Probe 15 

 0 0.2 0.4 0.6 0.8 1 0 

 0.5 

 1 Probe 10 Probe 11 Probe 12 

 0 0.2 0.4 0.6 0.8 1 0 

 0.5 

 1 Probe 7 Probe 8 Probe 9 

 0 0.2 0.4 0.6 0.8 1 

 0 

 0.5 

 1 Probe 4 Probe 5 Probe 6 

 0 0.2 0.4 0.6 0.8 1 

 0 

 0.5 

 1 Probe 1 Probe 2 Probe 3 

 Time (days) 

 C/C0 

Figure 6.5: Breakthrough curves of the KCl tracer measured (points) with the fifteen TDR probes before the biotic experiment. Lines present fit with analytical solution to determine dispersivity. 


6.3. Experimental results 179 

 0 0.2 0.4 0.6 0.8 1 

 0 

 0.5 

 1 Probe 13 Probe 14 Probe 15 

 0 0.2 0.4 0.6 0.8 1 0 

 0.5 

 1 Probe 10 Probe 11 Probe 12 

 0 0.2 0.4 0.6 0.8 1 0 

 0.5 

 1 Probe 7 Probe 8 Probe 9 

 0 0.2 0.4 0.6 0.8 1 

 0 

 0.5 

 1 Probe 4 Probe 5 Probe 6 

 0 0.2 0.4 0.6 0.8 1 

 0 

 0.5 

 1 Probe 1 Probe 2 Probe 3 

 Time (days) 

 C/C0 

Figure 6.6: Breakthrough curves of the KCl tracer measured with the fifteen TDR probes after the biotic experiment. From 0 to 0.5 day, tracer was injected, from 0.7 to 1.1 day, medium was injected. 


180 Chapter 6. Tank experiments 

the dyed PCE, visible through the glass wall, is shown in Figure 6.7. 

Figure 6.7: Picture on day 0, PCE formed in an irregular residual zone with a pool at the bottom. 

Variation of dissolved PCE concentration with time measured at nine sampling ports located within a vertical strip of 10 cm at the upstream edge of the residual zone are shown in Figure 6.8, where the PCE solubility limit is also indicated (horizontal line at 1.2 mM). It is evident that a very sharp gradient existed. The PCE concentrations in the sampling ports at the upstream edge of the source zone (63, 40, and 12) were very low. Within 50 mm, from sampling port 40 to 41 (or 63 to 64), the PCE concentration increased rapidly to the solubility limit, which is an indication of PCE being present as a NAPL. The upstream boundary of the source zone was irregular. In sampling port 12, the PCE concentration was higher compared to ports 40 and 63, which all have the same x-coordinate. On the other hand, sampling port 13 showed lower PCE concentrations than ports 41 and 64. The irregularity in PCE distribution was visually observed in Figure 6.7. However, in some sampling ports (e.g. 65 and 


6.3. Experimental results 181 

42) where visually no dyed PCE was observed, PCE was detected at concentrations corresponding to PCE NAPL. The visual distribution of PCE was, therefore, only an indication of where PCE certainly was present and did not exclude the presence of PCE in the surrounding pores. 

 0 100 200 0 

 0.01 

 0.02 

 Port 63 i) 

 0 100 200 0 

 1 

 2 

 Port 64 ii) 

 0 100 200 0 

 1 

 2 PCE solubility 

 Port 65 iii) 

 0 100 200 0 

 0.01 

 0.02 

 Port 40 iv) 

 0 100 200 0 

 1 

 2 

 Port 41 v) 

 0 100 200 0 

 1 

 2 

 Port 42 vi) 

 0 100 200 

 0 

 0.01 

 0.02 

 Port 12 vii) 

 0 100 200 

 0 

 1 

 2 

 Port 13 viii) 

 0 100 200 

 0 

 1 

 2 

 Port 14 ix) 

 Time (days) 

 Concentration (mM) 

Figure 6.8: PCE concentration with time in selected ports at the upstream side of the source zone. PCE solubility limit is indicated by a horizontal line at 1.2 mM. 

In Figure 6.9, PCE concentrations in six sampling ports within the source zone are shown. In these ports, PCE concentrations are around solubility limit. We can also see that in some ports (e.g. 43 and 16) the PCE concentration clearly exceeds the solubility limit. PCE concentrations exceeding the PCE solubility could not be explained by measurement errors or the presence of PCE liquid in samples. The chlorinated ethene concentrations were measured in the headspace of the sample, which corresponds to the solubility of the component in the aqueous phase according to Raoult’s Law. A higher solubility could be only explained 


182 Chapter 6. Tank experiments 

by an increase in the solubility limit, Cs,PCE^. 

(^00 100 200 300 400) 1 2 Port 67 i) (^00 100 200 300 400) 1 2 PCE solubility Port 69 ii) 0 100 200 300 400 0 1 2 Port 43 iii) 0 100 200 300 400 0 1 2 Port 46 iv) (^00 100 200 300 400) 1 2 Port 16 v) (^00 100 200 300 400) 1 2 Port 18 vi) Time (days) Concentration (mM) Figure 6.9: PCE concentration with time in selected ports in the source zone. Note that sampling port 43 is not on the same x-coordinate as ports 16 and 67. With time, PCE concentrations declined, indicating that the PCE source was exhausted. At some ports, PCE concentrations increased again to above solubility (see e.g. Figure 6.8, port 42 and Figure 6.9, port 16) after which a decline occurred again. The increase in PCE concentration must have been due to the appearance of a new source of PCE. Therefore, an explanation could be that residual PCE was mobilized. Similar indications for mobilization of residual PCE were found in column experiments discussed in section 5.4.2. Mobilization was only observable in ports were the PCE concentration had dropped below solubility and only in ports where residual PCE was present in zones above them. 


6.3. Experimental results 183 

### 6.3.4 Water content measurements 

The water content in the source zone was measured with the TDR probes and results are shown in Figure 6.10. There are three processes that can influence the water content: gas formation, dissolution of residual DNAPL, and mobilization of gas or DNAPL. They have different characters and different effects. Gas formation due to biological activity (e.g. carbon dioxide or methane) is gradual in nature and causes a decrease in water content. Dissolution of residual DNAPL is also a slow process but leads to an increase of the water content. Mobilization results in a more rapid change in water content. It can cause either a decrease or increase in water content at a given point, depending on whether NAPL or gas appears at or moves away from the measurement point. The interpretation of the change in water content based on the probe readings is easiest on day zero. On this day, PCE was injected and a decrease of about 0.1 in water content was observed for some probes, as in probe 8 which was in the flow path of the PCE. In other probes, like 1 (not shown) or 4, no decrease in water content was measured around PCE injection; thus, no PCE was present at that point. This is in agreement with the distribution of the dyed PCE visible through the glass wall (Figure 6.7). Other changes in water content during the experiment are more difficult to interpret as the three processes, mentioned above, can occur at the same position and at the same time. However, at some probes, reasons for a change in water content can be better identified. For example, the slow increase at probe 10 between day 10 and 40 must have been caused by dissolution of residual DNAPL; this is also supported by visual observations (see Figure 6.11). The decrease in water content at probe 13 on day 25 and the increase in water content day 130 was caused by gas mobilizing to and away from that position, respectively. Overall, the general trend in all probes showed a decrease in water content, indicating that the influence of gas formation was overall more pronounced than mobilization or dissolution of PCE. In Figure 6.11, photographs of the front wall of the tank are shown at different times. It is evident that PCE has been dissolved during the experiment. The PCE disappearance began in the upper part of the tank and only in the residual zone; no significant change in PCE pool were observed. Already after 40 days of experiment, lighter zones became visible pointing at the formation of gas, which was confirmed by a decrease in water content in the upper rows of TDR probes (see probes 13, 10, and 8 in Figure 6.10). The gas was formed in an irregular pattern outside the source zone as well as in the areas where PCE had disappeared. 


184 Chapter 6. Tank experiments 

 0 50 100 150 200 250 300 350 400 

 0 

 0.5 

 Probe 13 

 0 50 100 150 200 250 300 350 400 

 0 

 0.5 

 Probe 10 

 0 50 100 150 200 250 300 350 400 0 

 0.5 

 Probe 8 

 0 50 100 150 200 250 300 350 400 

 0 

 0.5 

 Probe 4 

 0 50 100 150 200 250 300 350 400 

 0 

 0.5 

 Probe 3 

 Time (days) 

 Water content 

 Figure 6.10: Water content with time measured with five TDR probes. 


6.3. Experimental results 185 

 Figure 6.11: 

 Pictures of the source zone at various times. Decrease in PCE residual zone and gas formation (in regions where PCE 

 has disappeared) are visible. 


186 Chapter 6. Tank experiments 

### 6.3.5 Biodegradation process 

After we studied the distribution of PCE in the source zone, we closely examine the chlorinated ethenes that were present in the plume. In Figure 6.12, PCE and cDCE concentrations in eight ports located in the contaminant plume are shown. PCE breakthrough at the tank outlet occurred within 10 days, which corresponds to the medium velocity of 20 cm day−^1 in the first week. PCE concentration remained around solubility until residual PCE was dissolved. In the upper part of the tank, PCE concentration declined earlier than at the bottom due to the bigger width of the residual zone at the bottom and the influence of the PCE pool. Dechlorination of PCE started between days 15 and 20 to yield cDCE; their intermediate product, TCE, was measured in concentrations lower than 0.2 mM (not shown). Concentration of cDCE increased gradually to about 6 mM, after which it remained steady at approximately 4 mM (see e.g. ports 3 and 5 in Figure 6.12) followed by a further decrease. The maximum measured cDCE concentration was 6.8 mM in sampling port 52 (not shown) in the plume, which was below the cDCE solubility limit (66 mM at 25 °C from Lide (Internet Version 2008)). However, dechlorination and cDCE production mainly occurred within the source zone. Dechlorination of PCE in the plume was inhibited. In Figure 6.13, horizontal transects along the flow direction at four different y-coordinates are shown for day 95. The PCE source zone was located between 700 and 1000 mm. In the upper part of the tank (the upper two graphs in Figure 6.13), the PCE concentration decreased downstream of the residual zone, becoming zero at 1200 mm distance. In the lower part of the tank (two lower graphs in Figure 6.13), the PCE concentration was around solubility (1.2 mM) all the way to the outlet. cDCE was formed in the residual zone and its concentration remained constant in the plume. Although PCE was available in the plume, cDCE concentration did not increase, indicating that PCE was not dechlorinated in the plume. Another major difference between the source zone and plume area was related to the dechlorination of cDCE to VC and VC to ethene. The formation of VC and ethene was very sensitive to the presence of PCE. Within the source zone, no VC or ethene were detected (see Figure 6.14, Port 16). In the plume, VC and ethene concentrations increased when PCE concentration decreased (see Figure 6.14, Port 3 around day 240). The success of dechlorination is also evident from results of bacterial counts in the water shown in Table 6.3. On the day of PCE injection, molecular analysis showed low values for cells of all measured bacterial groups. After 180 days, the number of cells increased for all bacterial groups. In the last column of Table 6.3, the ratio of Dehalococcoides spp. to bacteria, which belong to the same 


6.3. Experimental results 187 

 0 100 200 300 400 0 

 2 

 4 

 6 

 PCE solubility 

 Port 71 i) 

 0 100 200 300 400 0 

 2 

 4 

 6 

 Port 79 ii) 

 0 100 200 300 400 

 0 

 2 

 4 

 6 

 Port 48 iii) 

 0 100 200 300 400 

 0 

 2 

 4 

 6 

 Port 56 iv) 

 0 100 200 300 400 

 0 

 2 

 4 

 6 

 Port 20 v) 

 0 100 200 300 400 

 0 

 2 

 4 

 6 

 Port 28 vi) 

 0 100 200 300 400 0 

 2 

 4 

 6 

 Port 3 vii) 

 0 100 200 300 400 0 

 2 

 4 

 6 

 Port 5 viii) 

 Time (days) 

 PCE cDCE 

 Concentration (mM) 

Figure 6.12: PCE and cDCE concentration with time in selected ports in the contaminant plume. Concentration of VC and ethene are detected (>0.5 mM) but not shown, whereas TCE concentration was below 0.2 mM. 


188 Chapter 6. Tank experiments 

 0 500 1000 1500 2000 0 

 1 

 2 

 3 

 4 

 5 

 Profile at y−coordinate of 690 

 0 500 1000 1500 2000 0 

 1 

 2 

 3 

 4 

 5 

 Profile at y−coordinate of 540 

 0 500 1000 1500 2000 

 0 

 1 

 2 

 3 

 4 

 5 

 Profile at y−coordinate of 340 

 0 500 1000 1500 2000 0 

 1 

 2 

 3 

 4 

 5 

 Profile at y−coordinate of 190 

 Distance (mm) 

 Concentration (mM) 

 PCE cDCE VC Ethene 

Figure 6.13: Concentration PCE, cDCE, VC, and ethene at horizontal transects in the tank on day 95. 


6.3. Experimental results 189 

 PCE cDCE VC Ethene 

 0 50 100 150 200 0 

 1 

 2 

 3 

 4 

 5 

 PCE solubility 

 Sampling port 16 i) 

 0 50 100 200 250 300 350 

 0 

 1 

 2 

 3 

 4 

 5 

 Sampling port 3 ii) 

## // 

 Time (days) 

 Concentration (mM) 

Figure 6.14: Chlorinated ethene concentration with time in sampling port 16 (source zone) and 3 (plume). 

domain, is given. Before the start of the experiment, the percentage was very low. Halfway through the experiment, the percentage was higher at all ports. In port 71, 100% of the bacteria were from the Dehalococcoides spp. Due to the uncertainty in the molecular analysis, the actual number of Dehalococcoides spp. could be higher than the number of bacteria, as it is within the range mentioned. 

Dissolved organic carbon (DOC) may be used as a measure of the electron donor in the tank. The DOC concentrations varied around 250 mg l−^1 (see Tabel 


190 Chapter 6. Tank experiments 

Table 6.3: Results of the molecular analysis with q-PCR on water samples taken from the tank. The actual number of cells (N) ranged from 0.5*N to 2*N. Here the assumption was that one cell contained one DNA copy. 

 Day Sampling Bacteria Archaea Dehalococcoides Percentage port spp. Dehalococcoides from Bacteria cells ml−^1 cells ml−^1 cells ml−^1 % 

 -1 

 3 1.2· 105 1.5· 105 < 6.3· 102 < 1 4 1.9· 104 2.5· 104 < 6.3· 102 < 3.5 71 2.8· 104 8.0· 104 < 1.0· 103 < 3.5 75 5.4· 104 2.2· 104 1.3· 103 2.5 

 180 

 3 7.8· 108 1.3· 106 2.7· 107 3.5 4 3.4· 107 1.4· 105 3.8· 106 11 71 3.5· 106 4.6· 104 1.4· 107 100 75 1.5· 109 2.2· 106 1.5· 108 10 

6.4). This indicates that enough electron donor was present to achieve complete dechlorination. Sampling ports upstream the source zone (first four sampling ports in Table 6.4) give a representative picture of the available electron donor. It must be noted that measured DOC can include dissolved chlorinated ethenes. As a result, when concentrations of less volatile components, such as PCE and cDCE, are high (as around day 95 in and downstream the source zone), then DOC measurements were high. On day 266, the sum of the chlorinated ethene concentrations were much lower than on day 95, and DOC measurements more accurately represent the concentration of electron donor. 

### 6.3.6 Distribution of PCE and its degradation products 

In Figure 6.15, the development of the PCE plume is shown through spatial interpolation using a kriging method. Clay layers present in the tank are shown, as well as the points used for interpolation. In the first three plots of Figure 6.15, the development of the PCE plume up to day 21 is shown. In this period, PCE concentrations increased and reached solubility of 1.2 mM everywhere downstream of the source zone. On day 27, the first decrease in PCE concentration was observed in the middle of the plume. With time, this area of declining PCE concentrations increased to the upper half of the tank. On day 175, PCE was measured downstream the source zone only in the row of sampling ports closest to the bottom of the tank. On day 252, no PCE was detected in any sampling 


6.3. Experimental results 191 

Table 6.4: Dissolved organic carbon in mg l−^1 in water samples during the biotic experiment. 

 Sampling port Day 27 Day 95 Day 266 Influent 282 262 338 9 207 error 258 60 282 257 39 286 266 14 251 248 65 328 228 20 336 250 71 375 250 24 339 251 75 336 283 28 399 250 79 334 258 

port. 

The first detection of cDCE was on day 13 and gradually a cDCE plume developed (see Figure 6.16). The cDCE concentration in the tank increased steadily up to day 77 (not shown) to about 5 mM. Degradation of cDCE started in the upper half of the tank after 70 days when PCE had almost disappeared; that is also the time that the formation of VC became visible (Figure 6.17). With the complete dissolution of the residual PCE in the upper half of the tank after 175 days, the source for cDCE production became exhausted. However, the PCE pool was still present and a cDCE plume at the bottom of the tank remained until the end of the experiment. 

Over the whole experiment period, the VC concentrations in the source zone were very low (< 0.1 mM). The hot spot of VC plume moved downward and downstream in the tank as the dissolved PCE was also depleted downward (see the last five plots in Figure 6.17). 

The ethene contour plots (Figure 6.18) look very similar to the VC contour plots, except that the formation happened with a time lag of approximately 30 days. The first hot spot of ethene appeared in the upper part around day 245, corresponding to the disappearance of VC in that part (see plot of day 245 in Figure 6.17). The hot spot then moved downward and persisted until the experiment 


192 Chapter 6. Tank experiments 

Figure 6.15: Evolution of PCE plume based on kriging PCE concentrations at various times. Black dots represent points used in the kriging process. These are measurements from sampling ports plus nine points upstream the source zone with zero PCE concentration and two points in the pool with 1.2 mM PCE concentration. Up to day 27, no measurements are performed in the residual zone and three points are included here with 1.2 mM PCE concentration. 


6.3. Experimental results 193 

Figure 6.16: Evolution of cDCE plume based on kriging cDCE concentrations at various times. Black dots represent points used in the kriging process. These are measurements from sampling ports plus nine points upstream the source zone with zero cDCE concentration. 


194 Chapter 6. Tank experiments 

Figure 6.17: Evolution of VC plume based on kriging VC concentrations at various times. Black dots represent points used in the kriging process. These are measurements from sampling ports plus nine points upstream the source zone with zero VC concentration. 


6.3. Experimental results 195 

was stopped. During the last 30 days of the experiment, only ethene was detected in sampling ports at the bottom of the tank, where the plume originating from the PCE pool existed. These interpolated chlorinated ethene concentrations can be analyzed by spatial moment analysis (Figure 6.19). These are performed to investigate the plume development, displacement and dispersion. In these calculations, the concentration was assumed constant over the thickness of the tank and water saturation was assumed to be unity. The zeroth moment represents the total mass in the aqueous phase (see Figure 6.19-i), i.e. mass present in the DNAPL was not included in this analysis. The largest amount of mass was accounted for by cDCE (72%), followed by PCE (21%), VC (4%), ethene (2%), and TCE (<1%). The horizontal coordinate of the center of mass of PCE (see Figure 6.19-ii) moved approximately from position 1200 mm to the area with the pool at 800 mm as residual PCE dissolved away. The center of mass of other chlorinated ethenes moved slightly away from the source zone and concentrated around 1500 mm. When residual PCE was dissolved, chlorinated ethenes were detected in only a few sampling ports and originated from the PCE pool. The vertical coordinate of the center of mass (see Figure 6.19-iii) showed a downward trend for all chlorinated ethenes. Initially, the center of mass of all chlorinated ethenes was located around 500 mm, which is in the middle of the tank, indicating that the chlorinated ethenes were distributed evenly over the tank in the vertical direction. As the zone with residual PCE increased in width towards the bottom of the tank, the residual PCE dissolved first in the upper part of the tank. Therefore, the center of mass for all chlorinated ethenes moved vertically to the bottom of the tank. For PCE, this would be the PCE pool, and for other detected parameters this would be the sampling ports 4 and 5 at 190 mm from the bottom. The horizontal and vertical variances (see Figure 6.19-iv and v) showed spreading of the plume in both directions. For PCE, the horizontal spreading stalled when no PCE was measured in any sampling port and it only remained in the pool. Generally an increased spreading was observed as the effect of dispersion and diffusion increased with time. 

### 6.3.7 Mass balance 

Results of measurements of PCE remaining in the tank at the end of experiments are shown in Table 6.5. There was no PCE found in the residual zone. The samples taken from the pool, however, did contain PCE. At the bottom of the tank (samples D and F), a higher amount of PCE was detected than just above in 


196 Chapter 6. Tank experiments 

Figure 6.18: Evolution of ethene plume based on kriging ethene concentrations at various times. Black dots represent points used in the kriging process. These are measurements from sampling ports plus nine points upstream the source zone with zero ethene concentration. 


6.3. Experimental results 197 

 0 100 200 300 400 

 0 

 50 

 100 

 150 

 Time (days) 

 Total mass (mmol) 

(^) i) (^) PCE TCE cDCE VC Ethene 0 100 200 300 400 500 1000 1500 2000 Horizontal center of mass (mm) Time (days) ii) 0 100 200 300 400 0 500 1000 Time (days) Vertical center of mass (mm) iii) 0 100 200 300 400 0 1 2 3 x 10 7 Time (days) Horizontal variance (mm 2 ) iv) 0 100 200 300 400 0 5 10 15 x 10 6 Time (days) Vertical variance (mm 2 ) v) Figure 6.19: Spatial moment analysis of the chlorinated ethene concentrations measured in the tank experiment. Zeroth moment is the total mass in the aqueous phase (i), first moment is used to determine the center of mass in horizontal (ii) and vertical direction (iii), and the normalized second moment is the variances in the horizontal (iv) and vertical directions (v). 


198 Chapter 6. Tank experiments 

samples C and E. Just above the bottom of the tank, the volume of PCE measured at the left is lower than at the right. This is probably caused by the flow which was from left to right; more PCE was dissolved from the left part of the pool compared to the right side. In total, about 90 ml of PCE was recovered from the pool zone. This may be safely assumed to be the only PCE left in the whole tank. Some PCE might have evaporated when taking soil samples, but that amount could not be significant. 

 Table 6.5: Results of the soil sample analysis on PCE after the biotic experiment. 

 Name Description PCE (ml) A Residual area at top 0.0 B Residual area in the middle 0.0 C Pool, left side above D 8.8 D Pool, left side at the bottom 38.8 E Pool, right side above F 11.3 F Pool, right side at the bottom 31.2 

To check for PCE mass balance, a calculation was made to determine the total mass that left the system during experiments. This will be based on measurements from the last column of sampling ports (ports 5, 28, 56, and 79), which are nearest to the outlet. These ports were frequently sampled and are assumed to represent the surrounding area such that the whole outflow boundary is covered (see Figure 6.20). We assume is that the flow rate was constant over the whole outflow area. For the four ports, the concentrations of PCE, TCE, cDCE, VC, and ethene were integrated over time and multiplied by the total discharge. These calculated masses were then transferred to liquid PCE volumes, leading to an estimated volume of 135 ml PCE. This is an estimate that does not account for PCE removed by the withdrawal of samples, or chlorinated ethenes lost during the tracer experiment. Together with 90 ml PCE left in the pool, we account for a total PCE volume of 225 ml, which is 10% less than the 250 ml originally injected into the tank. 

Based on the analysis of results from the last column of sampling ports, PCE accounted for 21% of the total mass that left the tank. The remainder consisted of TCE (<1%), cDCE (73%), VC (4%), and ethene (2%). Variation of mole fractions of components leaving the column with time are shown in Figure 6.21. Most abundant product over a large part of the experiment was cDCE. However, after 


6.4. Numerical study 199 

 0 

 200 

 400 

 0 

 200 

 400 

 600 

 800 

 0 

 1 

 2 

 Time (days) 

 PCE 

 Height (mm) 

 i) 

 Concentration (mM) 

 0 

 200 

 400 

 0 

 200 

 400 

 600 

 800 

 0 

 5 

 10 

 Time (days) 

 cDCE 

 Height (mm) 

 ii) 

 Concentration (mM) 

 0 

 200 

 400 

 0 

 200 

 400 

 600 

 800 

 0 

 0.5 

 1 

 Time (days) 

 VC 

 Height (mm) 

 iii) 

 Concentration (mM) 

 Concentration profiles over the height of the tank at position 1940 mm as a function of time 

 0 

 200 

 400 

 0 

 200 

 400 

 600 

 800 

 0 

 0.5 

 1 

 Time (days) 

 Ethene 

 Height (mm) 

 iv) 

 Concentration (mM) 

Figure 6.20: Concentration of PCE, cDCE, VC, and ethene interpolated over the last column of sampling ports as a function of time. Four sampling ports were used for the calculation (black dots) and borders of representative area are shown (red lines). 

250 days of experiment, the mole fraction of VC and ethene raised to account for 30% each. 

## 6.4 Numerical study 

Numerical experiments were performed to compare with our laboratory results. Additionally, an evaluation of bioenhanced dissolution was made through per


200 Chapter 6. Tank experiments 

(^00 50 100 150 200 250 300 350 400) 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1 Time (days) Mole fraction in effluent column (as percentage of total) PCE TCE cDCE VC Ethene Figure 6.21: Chlorinated ethene concentrations in the sampling port in the last column of the tank expressed as mole fractions. forming simulations with and without dechlorination while keeping all other conditions the same. Obviously, the same cannot be done in laboratory experiments. This comparison gives information about the relevance of bioenhanced dissolution and about time frames for remediation of the contaminant. Parameter values used in the numerical simulations were estimated from independent experiments or set equal to values used for the column experiments. We did not try to calibrate the model. There was no fitting procedure applied through matching the numerical results with our experimental data. 

### 6.4.1 Model setup 

The injection of PCE, its spread in the tank, and formation of the residual zone and the pool were modelled with STOMP (White and Oostrom, 1996). STOMP (an acronym for Subsurface Transport over Multiple Phases) is a simulator that has a variable-source configuration for flow of water, NAPL and/or air in variably 


6.4. Numerical study 201 

saturated porous media. The dissolution and biodegradation process were modelled with an extended version of RT3D code (Clement et al., 1998, Clement, 1998), called RT3D-OW (OW stands for Oil Weathering). The extension allowed for dissolution and aerobic biodegradation of a multi-component LNAPL under saturated conditions, either in residual form or in pooled configuration (see Roelofsen and Kassels (2003)). To use the model in our research, we modified the code for DNAPL to be present as residual zone or as a pool at the bottom of the modelling domain, and included sequential dechlorination. The mass transfer terms for residual and pooled DNAPL were modelled differently. The mass transfer from residual NAPL was presented in section 5.3 of the previous chapter on column experiments. The mass transfer from pooled DNAPL is explained in the next section. 

The PCE injection into the tank was modelled with the water-oil mode of STOMP. The Brooks and Corey capillary pressure-saturation relation was used in combination with Burdine relation for the relative permeability-saturation. Table 6.6 gives sand and clay properties including permeability and Brooks-Corey parameters used within the STOMP simulation. Boundary conditions for the top and bottom were zero-flux for both PCE and water. At the cell with PCE injection, however, a Neumann boundary condition was applied for PCE for the first three hours, to simulate the addition of 250 ml of PCE. The left and right boundaries were assigned constant hydraulic heads for water phase. The outflow level was set to the height of the actual outflow of the laboratory tank experiment. At these boundaries, the zero-flux condition was applied for NAPL. The model was run for 10 days. The simulated NAPL saturation and corresponding relative hydraulic conductivity for water obtained at the end of simulation were used as input to the RT3D model. 

Table 6.6: Properties of sand and clay used to model PCE injection into the tank with STOMP. 

 Units Sand Clay Permeability m^2 4.5· 10 −^11 1.0· 10 −^17 Porosity 0.33 0.15 Entry pressure m 0.1325 0.26 Pore size distribution index 2.49 2.49 Residual saturation 0.098 0.098 Effective NAPL maximum trapped saturation 0.1 0.1 


202 Chapter 6. Tank experiments 

The flow field for the RT3D code was calculated with MODFLOW. Left boundary had a flux boundary condition and right boundary a constant head. Other boundaries were no-flow boundaries. Flow velocities in the simulations corresponded to the velocities used in the laboratory tank experiment. Physical and chemical properties used in the RT3D simulations are shown in Table 6.7. The maximum PCE degradation rate was set to zero in order to simulate PCE dissolution in the absence of dechlorination. The simulation time was 367 days. 

 Table 6.7: Physical parameters for the tank experiment used in numerical simulations. 

 Parameter Value Comment DPCEm 0 m^2 sec−^1 No molecular diffusion included in RT3D-OW αL 1 mm Determined with tracer experiment n 0.38 Determined d 4 · 10 −^2 m Determined X 0 5 · 108 cell l−^1 Assumed Xmax 1.5· 1011 cell l−^1 Assumed kd 0.024 day−^1 Yu and Semprini (2004) Y 5 · 1011 cell mmol−^1 Assumed β 0 7 Estimated value from column experiment β 1 0.75 Mayer and Miller (1996) β 2 0.6 Mayer and Miller (1996) S wPCEpure 200 mg l−^1 Lide (Internet Version 2008) RmaxPCE 6.78· 10 −^11 mmol cell−^1 day−^1 Estimated value from column experiment RcDCEmax 8.59· 10 −^15 mmol cell−^1 day−^1 Estimated value from column experiment RVCmax 0 mmol cell−^1 day−^1 Estimated value from column experiment KmPCE 0.1 mM Assumed KmcDCE 0.1 mM Assumed 

The same domain discretization was used in both simulators to facilitate the output of STOMP simulator (i.e. the PCE distribution) in RT3D. The model domain was discretized into 136 horizontal and 94 vertical cells. The grid was refined near the source zone where high NAPL saturation was expected. Vertical and horizontal grid sizes were both 1 mm in the source zone. Outside the PCE source zone, a larger grid size of 2 mm in the horizontal direction was used. 

### 6.4.2 Mass transfer from a DNAPL pool 

In RT3D-OW, the NAPL pool is considered to form the boundary of the modelling domain. As pools tend to accumulate on top of low-permeable layers, they typically have flow past along one side of them only. We assume that there is a 


6.4. Numerical study 203 

stagnant film of water between the pool surface and the flow domain. The film is assumed to be in equilibrium with the pool, i.e. the concentrations of the components in the water film are at solubility level, as prescribed by Raoult’s Law, see equation 5.7. Then, the transfer of components from the film to the surrounding water is assumed to occur through lateral dispersion. 

### 6.4.3 Numerical results 

The STOMP simulation results are shown in Figure 6.22 A residual PCE zone over the height of the tank and a pool at the bottom were formed during the first day. Thereafter, there was no change in PCE distribution. Residual PCE contained most of the PCE liquid volume (around 160 ml) and the pool contained 88 ml PCE. The volume of PCE left in the pool at the end of our experiments was about 90 ml. This is close to the volume of PCE left in the pool in our numerical simulations (70 ml). 

 Figure 6.22: PCE saturation in tank simulated with STOMP on four different times. 

Dissolution of PCE without dechlorination yielded PCE concentrations at solubility level everywhere downstream the residual and pooled PCE. At the end of the simulation, the PCE pool, as well as (portions of) the residual PCE were still remaining. The total dissolved PCE mass in the aqueous phase (e.g. zeroth spatial moment, not shown) was almost constant, i.e. within 10 days it reached 25.8 


204 Chapter 6. Tank experiments 

mmol, and later it gradually decreased to 24.9 mmol over the simulation period. The simulation with dechlorination showed a much faster decrease in NAPL saturation compared to the simulation without dechlorination. This indicates that dissolution of DNAPL was much faster in the case where microbial activity was present. Nevertheless, at the end of the simulation with dechlorination, residual PCE was not completely dissolved. Contrary to the case of no dechlorination, PCE concentrations in aqueous phase never reached solubility limit, and were actually very low, even close to the DNAPL. Further downstream, the PCE concentration became zero as no limitations on dechlorination were imposed. As a result, mainly cDCE was observed in concentrations that approached 6 mM in the aqueous phase (see Figure 6.23). The cDCE concentration decreased with time as the residual PCE area became smaller. 

 0 50 100 150 200 250 300 350 400 0 

 2 

 4 

 6 

 8 

 Time (days) 

 Concentration (mM) 

 Sampling port 5 

 PCE cDCE VC 

Figure 6.23: Chlorinated ethene concentrations from a model from the tank experiment for a cell corresponding to sampling port 5. 

The variation of total mass of chlorinated ethenes in the aqueous phase over the simulation time of 367 days is shown in Figure 6.24-i. Most of the mass was accounted for by cDCE (99.6%), with trace amounts of PCE, and VC. The center of mass of the components (see Figures 6.24-ii and iii) showed minimal variations in space, except for PCE. The vertical coordinate of the center of PCE mass showed a downward trend. Initially, the center of PCE mass was located around 430 mm, which is a little lower than the middle of the tank, indicating that the chlorinated ethenes were distributed evenly over the tank in vertical direction. As the zone with residual PCE increased in width towards the bottom of the tank, residual PCE was first dissolved in the upper part of the tank. 


6.4. Numerical study 205 

 0 100 200 300 400 

 0 

 50 

 100 

 150 

 Time (days) 

 Total mass (mmol) 

(^) i) PCE cDCE VC 0 100 200 300 400 500 1000 1500 2000 Horizontal center of mass (mm) Time (days) ii) 0 100 200 300 400 0 500 1000 Vertical center of mass (mm) Time (days) iii) 0 100 200 300 400 0 0.5 1 1.5 2 x 10 5 Time (days) Horizontal variance (mm 2 ) iv) 0 100 200 300 400 0 5 10 x 10^4 Time (days) Vertical variance (mm 2 ) v) Figure 6.24: Spatial moment analysis of the chlorinated ethene concentrations derived in a model from the tank experiment. Zeroth moment is the total mass in the aqueous phase (i), first moment is used to determine the center of mass in horizontal (ii) and vertical direction (iii), and the normalized second moment is the variances in the horizontal (iv) and vertical directions (v). 


206 Chapter 6. Tank experiments 

Then, the vertical coordinate of the center of mass moved towards the bottom of the tank where due to the presence of the pool, a long-lasting source of PCE remained. The horizontal and vertical variances (see Figure 6.24-iv and v) showed spreading of the plume in both directions, except for PCE. Its vertical spreading decreased as PCE was dissolved and rapidly dechlorinated. 

### 6.4.4 Evaluation of numerical results 

Spatial moment analysis of the chlorinated ethene concentrations obtained with the model (Figure 6.24) are compared to the spatial moments from the laboratory experiment (Figure 6.19). In calculating spatial moments it was assumed that PCE and cDCE concentrations were constant over the thickness of the tank and water saturation was unity over the whole grid. Although more information on the water saturation was available from the model, a water saturation of one was chosen for comparison with the laboratory experiment in which less information was available. Overall, the general trend of the spatial moment of the laboratory experiment are matched by the model. The peak of cDCE mass was similar for both laboratory and model results (around 120 mmol). This is caused by the close approximation of cDCE concentrations in the aqueous phase between model and experimental results. In the model, maximum cDCE concentration approached 6 mM (see Figure 6.23), whereas in the laboratory tank experiment cDCE concentration stabilized around 4 mM (see Figure 6.12-vii). This is a reasonable agreement taking into account that the dechlorination parameters originate from the column experiment and no fitting was applied. The most significant difference between the model and the laboratory experiment is the PCE concentration. The percentage PCE from the total mass in the laboratory experiment was more than ten times the value obtained in the model. In the laboratory experiment, PCE concentration was at solubility downstream the source zone (see Figure 6.13), whereas in the model PCE was always partially dechlorinated. PCE dechlorination was assumed to depend only on the bacteria concentration, without any other limitations. Probably, model results would have matched experimental results better if PCE dechlorination was considered to be limited by the production of cDCE. The effect of absence of dechlorination limitations in the model can also be seen in the production of cDCE. In the laboratory experiment, the peak of total cDCE mass was around day 80, whereas in the model the peak occurred immediately at the beginning. This has probably to do with the acclimatization period of bacteria in the laboratory experiment which is not captured in the model. In 


6.5. Discussion and conclusions 207 

the model, growth of bacteria to the maximum bacteria concentration was very fast and after this maximum was reached, the concentration remained constant as long as chlorinated ethenes were present. A comparison was made between model results with and without dechlorination to study bioenhanced dissolution and remediation time frames. This was through comparing the total PCE volume that had left the system for the two cases (with and without dechlorination). This was calculated in the same way as PCE that left the laboratory tank experiment in section 6.3.7. Chlorinated ethene concentrations from four cells at the position of the last column of sampling ports were integrated with time and multiplied by the discharge. All chlorinated ethenes were expressed in terms of PCE volume. Over the whole simulation period (367 days), total PCE volume that left the system was 57.4 ml for the case without dechlorination and 174.2 ml for the case with dechlorination. This indicates that over this period three times more PCE was dissolved in the presence of dechlorination compared to abiotic dissolution. The total PCE volume that had left the system with dechlorination from the numerical simulations (174 ml) was higher than the total PCE volume that left the laboratory tank in our experiments (135 ml). It is very plausible to suggest that the PCE distribution in the laboratory tank deviated from the distribution used in the numerical experiment. Although 90 ml PCE remained in the pool at the end of the laboratory experiment, the PCE volume in the pool at the start of the experiment was probably higher. In the numerical model, the pool initially contained 88 ml PCE. Additionally, as the mass balance of the laboratory experiment was not 100%, the PCE volume that left the laboratory experiment is less exact than the PCE volume in the numerical experiment. 

## 6.5 Discussion and conclusions 

Dechlorination of DNAPL in the presence of a source zone, consisting of PCE ganglia and a pool, does occur. Residual PCE was dissolved first, after which only the PCE pool remained. This is because DNAPL pools dissolve substantially slower than ganglia as typical interfacial contact areas of NAPL pools with groundwater are smaller than the corresponding areas of ganglia (Kim and Chrysikopoulos, 1999). Other important observations from our experiments are: increase in PCE solubility, mobilization of residual PCE and bioenhanced dissolution. These are discussed here. PCE concentrations in the source zone exceeded the pure phase PCE solubility, indicating that the PCE solubility, Cs,PCE^ , had increased. Recently, Kaplan 


208 Chapter 6. Tank experiments 

et al. (2008) observed that PCE concentrations in the effluent of biotic columns were higher than in the effluent of abiotic columns. In some cases, the PCE concentration exceeded the PCE solubility limit. They suggested that this was caused by the production of biosurfactants which are known to reduce the surface tension and increase solubility (Clifford et al., 2007, Bai et al., 1997). This was confirmed by surface tension measurements that showed a lower surface tension in columns with biodegradation compared to columns without biodegradation. Reduced surface tensions can also lead to the mobilization of NAPL ganglia. Although we did not perform any surface tension measurements in our tank experiment, observations of mobilization of residual NAPL suggest that similar effects were present in our tank experiment. 

Enhanced dissolution of DNAPL due to dechlorination also was observed in our experiments. The sum of chlorinated ethene concentrations can be used to determine the bioenhancement factor. In the tank, this reached a maximum of 6.8 mM. But more sustained concentration (over a period of 100 days) were measured at 5 mM. This leads to a bio-enhancement factor of 5.7 and 4.2, respectively, which declined with time as DNAPL dissolved. These bioenhanced dissolution factors are higher than the other large-scale laboratory experiment on enhanced dissolution, performed by Sleep et al. (2006). They found a sustained (over a period of 100 days) bio-enhanced dissolution factor of at least 1.7, which also decreased with time. The difference between these bioenhanced dissolution factors is probably due to difference in experimental setup. Their source zone consisted of residual PCE without the presence of a pool; they used a different microbial culture; and their flow rate was a little higher, 11.7 versus 10 cm day−^1. 

Another way to determine biologically-enhanced removal factor is based on flux calculations. In our biotic experiment, the equivalent of 135 ml of PCE was removed from the system. In an abiotic system, theoretically, the maximum outflow PCE concentration would be the solubility limit over the whole outflow area over the whole time. This yields a maximum of 64 ml PCE flowing out of the system. In fact, this is an overestimation as at a certain time, PCE dissolves away and PCE concentration would drop below solubility. This is certainly valid for the upper part of the tank where the width of residual PCE is smaller as more to the bottom. This makes clear that dechlorination can increase the removal efficiency of PCE dissolution. 

It is usually seen that measurements of total dissolved chlorinated ethenes may show significant mass transfer enhancement early in the process, followed by a decrease in the mass flux (Interstate Technology & Regulatory Council, 2008, Sleep et al., 2006). This means that the bioenhanced dissolution factor 


6.6. Summary and conclusions 209 

is not constant in time (Christ and Abriola, 2007). This can be due to variations in dissolution rate limitations but also because of dechlorination rate limitations. Dissolution rate can change with time as the distribution of accessible DNAPL and water-NAPL interfacial area will decrease with time. The relatively accessible DNAPL in the form of ganglia dissolve away, whereas less accessible DNAPL in a pool remains. The pooled DNAPL will have a lower dissolution rate because mass transfer is controlled by molecular diffusion and it has a much lower surface to mass ratio. Biomass growth and methane gas generation in the source zone can cause groundwater and electron donor to bypass the DNAPL source zone (Sleep et al., 2006). This in turn, leads to dechlorination rate limitations in DNAPL source zone as insufficient electron donor would be available (Chu et al., 2003). Moreover, there might be an inhibition of the dechlorination step from PCE to cDCE. Adamson et al. (2004) stated that ”prolonged exposure to high concentrations of cDCE impedes PCE and TCE dechlorination activity”. Similarly, Sung et al. (2003) found that 4.5 mM cDCE is inhibiting for PCE dechlorination. Christ and Abriola (2007) demonstrated that the time the system is operating at steady state conditions may be only half of the DNAPL source longevity. Therefore, applying constant dissolution enhancement factors leads to the over-prediction of the DNAPL source longevity. Glover et al. (2007) postulated that thickness of boundary layer next to a pool determines the effectiveness of biodegradation and the possibility of bioenhanced dissolution. For sharp pool boundaries, dissolution is controlled by diffusion of components away from the pool interface. They stated that bioactivity had little effect on mass transfer from pools with sharp boundaries. This is in agreement with our numerical results that showed that dissolution from the pool was not enhanced by dechlorination. In our laboratory experiment, the total concentration of chlorinated ethenes in the aqueous phase in sampling port 5 approached 1.7 mM on the last measurement day, when only the PCE pool had remained. This points, in the direction that little bioenhancement occurred from the pool, assuming that without dechlorination the effluent PCE concentration would have been at the solubility limit of 1.2 mM. 

## 6.6 Summary and conclusions 

To investigate DNAPL source zone processes in the presence of biodegradation, a two-dimensional tank experiment was performed. To increase the link with field conditions, a dechlorinating microbial assemblage was used for inoculation that originated directly from a field site contaminated with chlorinated ethenes. 


210 Chapter 6. Tank experiments 

The tank was filled with a relatively homogeneous () sand. A PCE spill was created resulting in residual ganglia and a high-saturation pool. Water, containing electron donor and nutrients, was flown through the tank and the experiment run for one year. Within this time period, a total of nineteen pore volumes flowed through the tank and residual PCE was completely removed and only the PCE pool remained. At the end, a plume containing cDCE, VC and ethene emanated. Three important observations were made during source zone dechlorination were observed. First, PCE concentrations in the source zone exceeded the pure phase PCE solubility, indicating that the PCE solubility had increased. Second, dechlorination within the source zone caused an enhancement in dissolution by a factor of 4 to 5. Third, mobilization of residual PCE occurred. The first two observations increase the source mass flux and, therefore, decrease the source zone longevity. Observed remobilization of residual DNAPL did not increase the source mass flux in our experiment. However, theoretically, mobilization of residual DNAPL could result in a more intractable remediation problem in field cases. The specific question of whether or not this process of mobilization is active at DNAPL-contaminated field sites will require further studies. 

## 6.7 Acknowledgements 

The authors gratefully acknowledge the generous provision of the automated TDR measurement system by Prof.Dr.Ir. W. Bouten, Institute for Biodiversity and Ecosystem Dynamics (IBED), University of Amsterdam, The Netherlands, and the assistance of L. de Lange. This research was carried out in the framework of TRIAS research program financed by NWO, SKB, and Delft Cluster. 


Bibliography 211 

## Bibliography 

Adamson, D. T., J. M. McDade, and J. B. Hughes (2003), Inoculation of a DNAPL source zone to initiate reductive dechlorination of PCE, Environmental Science and Technology, 37 , 2525–2533. 

Adamson, D. T., D. Y. Lyon, and J. B. Hughes (2004), Flux and product distribution during biological treatment of tetrachloroethene dense non-aqueous-phase liquid, Environmental Science and Technology, 38 , 2021–2028. 

Amos, B. K., J. A. Christ, L. M. Abriola, K. D. Pennell, and F. E. L ̈offler (2007), Experimental evaluation and mathematical modeling of microbially enhanced tetrachloroethene (pce) dissolution, Environmental Science and Technology, 41 (3), 963–970, doi:10.1021/es061438n. 

Amos, B. K., E. J. Suchomel, K. D. Pennell, and F. E. L ̈offler (2008), Microbial activity and distribution during enhanced contaminant dissolution from a napl source zone, Water Research, 42 , 2963–2974. 

Aulenta, F., C. Di Tomassi, C. Cupo, M. P. Papini, and M. Majone (2006), Influence of hydrogen on the reductive dechlorination of tetrachloroethene (pce) to ethene in a methanogenic biofilm reactor: role of mass transport phenomena, Journal Of Chemical Technology And Biotechnology, 81 (9), 1520–1529, doi:10.1002/jctb.1562. 

Bai, G., M. L. Brusseau, and R. M. Miller (1997), Biosurfactant-enhanced removal of residual hydrocarbon from soil, Journal of Contaminant Hydrology, 25 , 157–170. 

Carr, C. S., and J. B. Hughes (1998), Enrichment of high-rate PCE dechlorination and comparative study of lactate, methanol, and hydrogen as electron donors to sustain activity, Environmental Science and Technology, 32 , 1817–1824. 

Christ, J. A., and L. M. Abriola (2007), Modeling metabolic reductive dechlorination in dense non-aqueous phase liquid source-zones, Advances in Water Resources, 30 (6-7), 1547–1561, doi:10.1016/j.advwatres.2006.05.024. 

Chu, D., and W. Gentleman (1998), Kriging software for matlab 5.2., Gulf of Maine News, Fall, 15pp. 


212 Chapter 6. Tank experiments 

Chu, M., P. K. Kitaradis, and P. L. McCarty (2003), Effects of biomass accumulation on microbially enhanced dissolution of a PCE pool: a numerical simulation, Journal of Contaminant Hydrology, 65 (1-2), 79–100, doi:10.1016/S01697722(02)00232-2. 

Cirpka, O. A., C. Windfuhr, G. Bisch, S. Granzow, H. Scholz-Maramatsu, and H. Kobus (1999), Microbial reductive dechlorination in large-scale sandbox model, Journal of Environmental Engineering, 125 , 861–870. 

Clement, T. P. (1998), RT3D A Modular Computer Code for Simulating Reactive Multi-Species Transport in 3-Dimensional Groundwater Aquifers. 

Clement, T. P., Y. Sun, B. S. Hooker, and J. N. Petersen (1998), Modeling multispecies reactive transport in groundwater, Ground Water Monitoring and Remediation, pp. 79–92. 

Clifford, J. S., M. A. Ioannidis, and R. L. Legge (2007), Enhanced aqueous solubilization of tetrachloroethylene by a rhamnolipid biosurfactant, Journal of Colloid and Interface Science, 305 , 361–365. 

de Bruin, W. P., M. J. J. Kotterman, M. A. Posthumus, G. Schraa, and A. J. B. Zehnder (1992), Complete biological reductive transformation of tetrachloroethene to ethane, Applied and Environmental Microbiology, 58 , 1996– 2000. 

De Zeeuw, W. J. (1984), Acclimatization of anaerobic sludge for uasb reactor start-up, Ph.D. thesis, Wageningen Agricultural University, The Netherlands. 

Domenico, P. A., and F. W. Schwartz (1997), Physical and chemical hydrogeology, 2nd ed., John Wiley & Sons, Inc. 

Ellis, D. E., E. J. Lutz, J. M. Odom, R. J. Buchanan Jr., C. L. Bartlett, M. D. Lee, M. R. Harkness, and K. A. DeWeerd (2000), Bioaugmentation for accelerated in situ anaerobic bioremediation, Environmental Science and Technology, 34 , 2254–2260. 

French, H. K. (1999), Transport and degradation of deicing chemicals in a heterogeneous unsaturated soil, Ph.D. thesis, Agricultural University of Norway. 

Fure, A. D., J. W. Jawitz, and M. D. Annable (2006), DNAPL source depletion: Linking architecture and flux response, Journal of Contaminant Hydrology, 85 , 118–140. 


Bibliography 213 

Glover, K. C., J. Munakata-Marr, and T. H. Illangasekare (2007), Biologically enhanced mass transfer of tetrachloroethene from DNAPL in source zones: experimental evaluation and influence of pool morphology, Environmental Science and Technology, 41 , 1384–1389. 

He, J., K. M. Ritalahti, M. R. Aiello, and F. E. L ̈offler (2003), Complete detoxification of vinyl chloride by an anaerobic enrichment culture and identification of the reductively dechlorinating population as a Dehalococcoides species, Applied and Environmental Microbiology, 69 , 996–1003. 

Heimovaara, T. J. (1993), Design of triple-wire time domain reflectometry probes in practice and theory, Soil Science Society of America Journal, 57 , 1410– 1417. 

Heimovaara, T. J. (1994), Frequency domain analysis of time domain reflectometry waveforms: 1. measurement of the complex dielectric permittivity of soils, Water Resources Research, 30 , 189–199. 

Heimovaara, T. J., and W. Bouten (1990), A computer-controlled 36-channel time domain reflectometry system for monitoring soil water content, Water Resources Research, 26 , 2311–2316. 

Heimovaara, T. J., E. J. G. De Winter, W. K. P. Van Loon, and D. C. Esveld (1996), Frequency-dependent dielectric permittivity from 0 to 1 GHz: Time domain reflectometry measurements compared with frequency domain network analyzer measurements, Water Resources Research, 32 , 3603–3610. 

Hill, D. D., and B. E. Sleep (2002), Effects of biofilm growth on flow and transport through a glass parallel plate fracture, Journal of Contaminant Hydrology, 56 , 227–246. 

Interstate Technology & Regulatory Council (2008), In situ bioremediation of chlorinated ethene: DNAPL source zones. bioDNAPL-3, Tech. rep., Washington D.C. 

Isalou, M., B. E. Sleep, and S. N. Liss (1998), Biodegradation of high concentrations of tetrachloroethene in a continuous flow column system, Environmental Science and Technology, 32 , 3579–3585. 

Kaplan, A. R., J. Munakata-Marr, and T. H. Illangasekare (2008), Biodegradation of residual dense nonaqueous-phase liquid tetrachloroethene: Effects on mass transfer, Bioremediation Journal, 12 , 21–31, doi: 10.1080/10889860701866289. 


214 Chapter 6. Tank experiments 

Kim, T. J., and C. V. Chrysikopoulos (1999), Mass transfer correlations for nonaqueous phase liquid pool dissolution in saturated porous media, Water Resources Research, 35 (2), 449–459. 

Lide, D. R. (Ed.) (Internet Version 2008), CRC Handbook of Chemistry and Physics, chap. Standard thermodynamic properties of chemical substances, 88th ed., CRC Press/Taylor and Francis, Boca Raton, FL. 

Major, D. W., M. L. McMaster, E. E. Cox, E. A. Edwards, S. M. Dworatzek, E. R. Hendrickson, M. G. Starr, J. A. Payne, and L. W. Buonamici (2002), Field demonstration of successful bioaugmentation to achieve dechlorination of tetrachloroethene to ethene, Environmental Science and Technology, 36 , 5106–5116. 

Mayer, A. S., and C. T. Miller (1996), The influence of mass transfer characteristics and porous media heterogeneity on nonaqueous phase dissolution, Water Resources Research, 32 , 1551–1567. 

Maym ́o-Gatell, X., V. Tandoi, J. M. Gossett, and S. H. Zinder (1995), Characterization of an H 2 -utilizing enrichment culture that reductively dechlorinates tetrachloroethene to vinyl chloride and ethene in the absence of methanogenesis and acetogenesis, Applied and Environmental Microbiology, 61 , 3928– 3933. 

Nielsen, R. B., and J. D. Keasling (1999), Reductive dechlorination of chlorinated ethene DNAPLs by a culture enriched from contaminated groundwater, Biotechnology and Bioengineering, 62 , 160–165. 

Oostrom, M., J. H. Dane, and T. W. Wietsma (2006), A review of multidimensional, multifluid intermediate-scale experiments: nonaqueous phase liquid dissolution and enhanced remediation, Vadose Zone Journal, 5 , 570–598, doi: 10.2136/vzj2005.0125. 

Parker, J. C., and E. Park (2004), Modeling field-scale dense nonaqueous phase liquid dissolution kinetics in heterogeneous aquifers, Water Resources Research, 40 (5), doi:10.1029/2003WR002807. 

Roelofsen, F. J., and C. G. M. Kassels (2003), Development of a numerical simulator for LNAPL weathering. phase 5: Manual for RT3D-OW concept, Tech. rep. 


Bibliography 215 

Schwille, F. (1998), Dense chlorinated solvents in porous and fractured media. Model experiments, Lewis Publishers, Chelsea, Michigan. 

Sharma, P. K., and P. L. McCarty (1996), Isolation and characterization of a facultatively aerobic bacterium that reductively dehalogenates tetrachloroethene to cis-1,2-dichloroethene, Applied and Environmental Microbiology, 62 , 761– 765. 

Sleep, B. E., et al. (2006), Biological enhancement of tetrachloroethene dissolution and associated microbial community changes, Environmental Science and Technology, 40 , 3623–3633. 

Sung, Y., K. M. Ritalahti, R. A. Sanford, J. W. Urbance, S. J. Flynn, J. M. Tiedje, and F. E. L ̈offler (2003), Characterization of two tetrachloroethene-reducing, acetate-oxidizing anaerobic bacteria and their description as Desulfuromonas michiganensis sp. nov., Applied and Environmental Microbiology, 69 , 2964– 2974. 

Thullner, M., J. Zeyer, and W. Kinzelbach (2002), Influence of microbial growth on hydraulic properties of pore networks, Transport in Porous Media, 49 , 99– 122. 

Thullner, M., M. H. Schroth, J. Zeyer, and W. Kinzelbach (2004), Modeling of a microbial growth experiment with bioclogging in a two-dimensional saturated porous media flow field, Journal of Contaminant Hydrology, 70 , 37–62. 

White, M. D., and M. Oostrom (1996), STOMP: Subsurface Transport Over Multiple Phases. Users Guide., Pacific Northwest National Laboratory, Richland, WA. 

Yang, Y., and P. L. McCarty (2000), Biologically enhanced dissolution of tetrachloroethene DNAPL, Environmental Science and Technology, 34 , 2979– 2984. 

Yu, S., and L. Semprini (2004), Kinetics and modeling of reductive dechlorination at high PCE and TCE concentrations, Biotechnology and Bioengineering, 88 (4), 451–464. 



## Chapter 7 

# Discussion and conclusions 

Soil and groundwater contaminations by DNAPLs are of major concern. A promising technique for remediation of DNAPL contaminations is biological degradation. Recently, interest is growing more and more in the application of biodegradation to DNAPL source zones. We have conducted a series of experiments, at various scales, to investigate the possibilities of application and consequences of active bioremediation in the vicinity of PCE. 

Previous experiments of dechlorination on high PCE concentrations show conflicting results. To have dechlorination in batch experiments, bacteria should be able to either cope with saturated DNAPL concentrations, or dechlorinate faster than the dissolution rate to prevent inhibitory concentrations. Our dechlorination microbial assemblage did not dechlorinate PCE concentrations above 0.5 mM in batch experiments, and toxicity effects are proposed as a reason for this inhibition. As confirmed by previous studies, this does not mean that in other systems, dechlorination in source zones cannot occur, or that bioenhanced dissolution cannot occur. In our column and tank experiments with a porous medium, dechlorination in the source zone took place. This difference in biodegradation behavior between batch and column arrangements is believed to be due do the interplay of biodegradation, advection, and diffusion. These processes create a pore-scale distribution of PCE concentration from solubility limit next to a blob, to lower-than-toxicity values within a short distance in small zones. In these micro-environments PCE concentration was below PCE inhibitory concentration and dechlorination occurs. 

This observation of dechlorination in source zones implicates that (enhanced) biodegradation of contaminations in the field can be a successful remediation technique for source zones as well as the more common acceptation of con


218 Chapter 7. Discussion and conclusions 

taminant plume remediation. Though, for similar dechlorination products and removal rates the conditions in the field should approach the conditions of our laboratory experiments in which reducing conditions were always achieved and electron donor availability for indigenous micro-organisms was high. Realistically, this might be challenging as far more (micro-)heterogeneities exist at field sites which can result in potential mass transfer and/or biodegradation limitations. Explicitly, the first is dissolution that brings the NAPL into the water phase and the second is biodegradation that actually breaks down the components. The presence of DNAPL may lead to high concentration of dissolved contaminant, and influence bacterial population dynamics. While some species are inhibited by PCE or TCE, others are unaffected. Methanogens are known to be inhibited by high concentrations of PCE or TCE, and therefore less methane production is to be expected. On the other hand, VC is only degraded further to ethene or ethane in the absence of PCE and TCE. However, if dechlorination occurs close to the DNAPL, dissolution of DNAPL can proceed faster as the aqueous phase concentration is lowered by bacteria. Thus, dissolution and biodegradation depend on each other, but both are also influenced by other factors as well. Dissolution rate could be initially high when accessible DNAPL is dissolved and decrease with time when only less accessible DNAPL is available. For biodegradation, electron donor could be limiting or other microbial consortia can compete for the same electron donor. The coupling of biodegradation to dissolution and the dependence of them on each other make predictions of total mass removal in field situations difficult. 

Although, field conditions are more complicated than our laboratory experiments, the results show that it can be beneficial to establish an active dechlorinating biomass within DNAPL source zones. A bioenhanced dissolution factor was determined between 1 and 7. The lower enhancement factors were determined is systems were PCE was present in more pool dominated configurations, whereas the high enhancement factors were determined in residual dominated systems. This implicates that dissolution can be enhanced by biodegradation especially in contaminations with residual PCE and that the longevity of the source zone can be shortened significantly. In the field, more unaccessible DNAPL may be present in high-permeability lenses or in pools on low-permeability strata. DNAPL pools are very hard to remove and as shown in our tank experiment bioenhanced dissolution is hardly increasing the mass flux from DNAPL to the water phase. Nevertheless, microbial activity in proximity of the DNAPL pool resulted in a plume of only cDCE, VC and ethene, without the detection of PCE. If conditions for dechlorination can be kept optimal downstream the source zone, the plume can 


#### 219 

be transformed to harmless products within short distances from the pool (in the order of meters). This can be seen as a biological isolation of the DNAPL pool. The bioenhanced dissolution factor resulted from a higher concentration gradient, higher solubility limit, and a increased dissolution rate coefficient. In our modelling studies of DNAPL dissolution and dechlorination in systems with a porous media the dissolution rate coefficient increased with time. Calculations with a traditional constant dissolution rate coefficient will lead to an underestimation in mass removed. This occurs also when a increase in PCE solubility limit is neglected. For bioenhanced dissolution to occur it is essential to have short distance between the actual dechlorination activity and the DNAPL. Therefore, the initial as the development of the flow field is for a large degree determining the effectiveness of bioenhanced dissolution. For example, regions with trapped NAPL in the field are preferentially bypassed by groundwater. This influences the dissolution of NAPL to groundwater and may negatively influence the source zone longevity. Not only dissolution might be lower due to water bypassing the source zone, but also the delivery of electron donor can be less efficient and as a result biodegradation can be slower or incomplete. On the other hand, in systems with biomass accumulation near the DNAPL-water interface, locally high gas concentrations can develop, and local changes in relative permeability and water saturation can occur. This may result in complex interaction between biodegradation and flow processes. Additionally, residual DNAPL was mobilized when active dechlorination occurred. The distance of this DNAPL mobilization was not exact determined from our experiments, as they were only designed to observe if any mobilization occurred. However, trying to interpret the consequences of residual DNAPL mobilization in the field, one can think that DNAPL will finally end up in DNAPL pools only. Residual DNAPL will be either dissolved and/or dechlorinated or mobilized down. This vertical downward movement follows, theoretically, the flow path of the mobile DNAPL that have flown before the residual became entrapped. The only hypothetical situation in which residual DNAPL mobilization enlarges the source zone is in situations in which a residual DNAPL has formed without a DNAPL pool. In this case, residual DNAPL mobilization results that the source zone is enlarged and the distance of DNAPL mobilization becomes important. Based on flow of DNAPL in saturated media, this will probably be in the order of cm to dm. 



# Summary 

Soil and groundwater pollution by chlorinated solvents, such as tetrachloroethylene (PCE), are common throughout the industrialized world. These so-called dense non-aqueous phase liquids (DNAPLs) pose environmental health risks and serve as a long-term source of groundwater contamination and, therefore, sites contaminated with DNAPLs often require remediation. One of the most effective and economically feasible methods for NAPL cleanup is in-situ bioremediation. Microorganisms can often degrade DNAPLs in the aqueous phase in the presence of a suitable electron donor under reduced conditions. Early bioremediation activities were directed at contamination plumes. However, recently, interest is growing more and more in the application of biodegradation to source zones. This thesis strengthens current knowledge and adds valuable insights into biodegradation within a DNAPL source zone. Chapter 2 reviews current perspectives on the dissolution and biodegradation of DNAPL in and around source zones. In particular, the focus is on how these processes are measured, modelled, and, especially, how they interact. Dissolution from the NAPL to the water phase is essential for biodegradation to occur. Although dissolution and biodegradation of DNAPLs are separately well understood, there are open questions regarding their mutual influence on each other. On one hand, source-zone longevity can be shortened as the biodegradation enhances the dissolution. On the other hand, this enhanced dissolution promotes biodegradation. The coupling of biodegradation and dissolution has been investigated in modelling studies and laboratory experiments. From these experiments, it was concluded that biodegradation enhances dissolution significantly, up to a factor 16, which is called the bioenhanced dissolution factor. A factor higher than one indicates that the longevity of the source zone can be shortened significantly. To investigate bioenhanced dissolution in modelling exercises, a good representation of the bacterial competition and inhibition is required for the simulation of the complex nature of the microorganisms present at a contaminated site. The following chapters describe the laboratory experiments that were per


222 Summary 

formed at different scales including batch, columns, and tank experiments. All experimental results were analyzed by numerical models. The experiments were carried out under anaerobic conditions with groundwater containing a dechlorinating microbial assemblage originating from a PCE-contaminated site. 

In chapter 3, results from dechlorination in batch experiments are reported with initial aqueous PCE concentrations in the range of 0.09 to 0.8 mM and up to the solubility limit (1.2 mM) with the presence of PCE as a separate phase in the latter case. Although recent publications suggest that PCE could be dechlorinated up to saturation concentrations by mixed cultures, the dechlorinating microbial assemblage tested in this study was only able to dechlorinate PCE up to approximately 0.5 mM. No dechlorination was found at higher initial PCE concentrations. Dechlorination of PCE was described by a biokinetic model with the Michaelis-Menten equation including self-inhibition with a maximum degradation rate of 80 μmol PCE l−^1 day−^1 , a half saturation constant of 0.33 mM and a PCE inhibition constant of 0.5 mM. In the literature, microbial dechlorination of higher concentrations of PCE are reported. However, these cases might have been the result of microbial adaptation to high PCE concentrations in the laboratory. 

Chapter 4 describes a model that was developed to investigate the results of batch experiments and to determine significance of other biological reactions influencing the dechlorination process. These experimental results revealed that with increasing PCE concentrations, dechlorination became incomplete and stalled at initial PCE concentrations higher than 0.5 mM. Moreover, contrary to expectation, triplicate batch experiments did not always produce the same result. The constructed model included kinetic and thermodynamic constraints for dechlorination, fermentation, and biomass growth. Dechlorination rate parameters were estimated for one batch experiment by fitting the chlorinated ethene concentrations with the SCEM-UA algorithm. Application of the obtained parameters to other batch experiments did not result in a good fit with the experimental results. The model showed a high sensitivity for the rate of competitive inhibition between chlorinated ethenes and reaction rates of electron donor fermentation related to electron donor consumption by competing processes. A slight change in initial conditions would result in very different chlorinated ethene concentrations. This led to the conclusion that under field conditions, changes in initial conditions may prevent biodegradation to proceed at maximum degradation rates. 

Chapter 5 contains experimental and numerical results from column experiments, which were designed to investigate the applicability of bioremediation of PCE near source zones. In three different setups in eight columns, dechlorination of dissolved, residual, and pooled PCE was investigated. Dechlorination 


#### 223 

in columns with dissolved PCE proceeded completely to ethene, with concentrations tested up to 0.6 mM. In columns with residual PCE, cDCE was the main dechlorination product and we determined that dissolution was five times enhanced in the presence of active dechlorination, which is comparable to bioenhancement factors found in the literature. Moreover, this setup allowed for the observation of residual NAPL mobilization in the presence of active dechlorination. The column experiments were simulated by a single-phase flow model for which dechlorination and dissolution parameters were optimized. Modelling of the column experiments yielded information about the relevance and interplay of dechlorination and dissolution processes. Although the complex processes in the column experiments were incorporated in the model in a simplified way, experimental results were simulated reasonably well. Some deviations between model and experimental results indicated more advanced (dechlorination) kinetics were required to obtain a better fit. The most important observation was that for columns with residual PCE, the dissolution parameters have probably increased with time when dechlorination occurred. Model calculations with a traditional constant dissolution rate coefficient and solubility limit can lead to an underestimation in mass removed. The difference in dechlorination behavior between batch and column arrangements is believed to be due do the interplay of biodegradation, advection, and dissolution. These processes create a pore-scale distribution of PCE concentration, varying from solubility limit, next to a blob, to lower-than-toxicity values within a short distance. These processes also lead to enhanced dissolution of PCE. 

The experiments in a two-dimensional tank filled with sand are reported in chapter 6. The tank had inner dimensions of 2080 x 940 mm and a depth of 45 mm. After inoculation, 250 ml PCE was injected into the tank which yielded a residual zone of PCE with a pool at the bottom. After this injection, the tank was continuously flushed with anaerobic water containing sufficient electron donor and various nutrients to simulate horizontal groundwater flow at rates comparable to field conditions. Chlorinated ethenes analysis, microbial groups counting, and the visual observation of the dyed PCE showed that PCE was dechlorinated in the source zone. Bio-enhanced dissolution is believed to have occurred as the total chlorinated ethene concentration was about four times higher than the solubility limit of PCE. This bioenhanced dissolution factor resulted from a higher concentration gradient, a higher PCE solubility limit, and an increased dissolution rate coefficient. Moreover, mobilization of residual PCE was observed. Dechlorination of cDCE to vinyl chloride (VC) occurred only when PCE concentrations were low (<0.1 mM). Similarly, transformation of VC to ethene occurred only 


224 Summary 

after cDCE concentrations became low. After one year of experiment, approximately 135 ml of PCE had left the tank mainly as cDCE (73%). The tank was disassembled and we found that only 90 ml was present in the pool. This amounts to a total PCE of 225 ml, which is 10% less than the volume injected into the tank. Spatial moment analysis were performed to investigate the general plume behavior. This was compared to a model simulation with a modified version of RT3D that accounted for DNAPL dissolution and dechlorination. Parameters determined with the column experiments were used to simulate the tank experiment. Spatial moments obtained from this model simulation were very similar to the spatial moments obtained from the experimental tank experiment. Moreover, the computations closely matched the total mass that left the tank in the laboratory experiment. In both column and tank experiments, we have established that mobilization of residual PCE occurred as a result of dechlorination activities. The mobilization and the observation of an increase in dissolution rate constant in the presence of dechlorination are probably effects of the production of surfactants by the dechlorinating microbial assemblage. 

The results of this research provide valuable insights in the relevance and implications for application of bioremediation in and around DNAPL source zones. DNAPL source zones can be successfully remediated by (enhanced) biodegradation. Conditions in the field determine to a large extent the dechlorination products and removal rates that can be achieved. The interplay between biodegradation, dissolution and advection is complex as they depend on each other, but are also influenced by other factors. Conditions can also change with time, resulting in a change in dechlorination. For example dissolution rate can decrease with time when accessible DNAPL is dissolved first. For biodegradation, electron donor could be limiting or other microbial consortia can compete for the same electron donor. These coupling of processes make predictions of total mass removal in field situations difficult. However, the results in this thesis show that biodegradation can potentially enhance dissolution about four times. Especially in contaminations with residual PCE, the longevity of the source zone can be shortened significantly. The more unaccessible DNAPL may be present in highpermeability lenses or in pools on low-permeability strata. DNAPL pools are very hard to remove and, as shown in our tank experiment, bioenhanced dissolution can hardly increase the mass flux from DNAPL pool to the water phase. Nevertheless, microbial activity in proximity of the DNAPL pool can result in a plume of harmless products within short distances from the pool (in the order of meters). This can be seen as a biological isolation of the DNAPL pool. The observation of mobilization of residual DNAPL means that theoretically only DNAPL present 


#### 225 

in pools will persist. Residual DNAPL will be either dissolved, dechlorinated or mobilized down. 



# Samenvatting 

Olieverontreinigingen in de bodem zijn talrijk en kunnen risico’s vormen voor bijvoorbeeld onze drinkwatervoorzieningen. Door de langzame oplossing in water, kan de olie in de bodem aanwezig zijn als puur product (in het Engels nonaqueous phase liquid, of NAPL) en het langsstromend grondwater verontreinigen voor tientallen jaren. Olieverontreinigingen worden onderverdeeld in twee catogorie ̈en op basis van het soortelijk dichtheid ten opzichte van water: lichtere en zwaardere oli ̈en, LNAPLs en DNAPLs, respectievelijk. De DNAPLs zullen door de onverzadigde en verzadigde bodem zakken totdat ze op (mogelijk grote diepte) een slecht doorlatende laag een zogenaamde zaklaag kunnen vormen. In het verleden is veel onderzoek gedaan naar de sanering met behulp van biologische afbraak van opgeloste olie componenten in de pluim. Dit is het grondwater benedenstrooms de zone met puur product, de zogenaamde bronzone. Aanpak van de bron zou echter de tijdsduur van de sanering aanzienlijk kunnen verkorten. Bronzones worden vaak met een intensievere saneringstechniek verwijderd dan de pluim omdat er onduidelijkheid bestaat over de toepasbaarheid van biologische afbraak in de bronzone. Dit proefschrift beschrijft het theoretische en experimentele onderzoek naar meerfasenstroming en gestimuleerde biologische afbraak in bronzones van een DNAPL verontreiniging. In hoofdstuk 2 wordt de huidige kennis besproken over het in oplossing gaan van puur product in water en biologische afbraak van hoge concentraties die karakteristiek zijn voor bronzones. Er wordt ingegaan op de manier waarop deze processen worden gemeten, gemodelleerd en hoe ze elkaar be ̈ınvloeden. Alhoewel deze processen afzonderlijk goed worden begrepen en zijn beschreven, bestaat onduidelijkheid over de interactie tussen de oplossing en afbraak van DNAPLs. Aan de ene kant is biologische afbraak afhankelijk van de oplossing van puur product naar de waterfase omdat het daarin plaatsvindt, maar anderzijds kan biologische afbraak in de waterfase ervoor zorgen dat de oplossing van puur product wordt versneld. Deze processen zijn onderzocht met behulp van laboratoriumexperimenten en computermodellen. Hieruit werd geconcludeerd 


228 Samenvatting 

dat biologische afbraak de oplossing van puur product met maximaal een factor 16 versneld. Als de factor groter is dan 1 wordt de levensduur van de bronzone verkort door biologische afbraak in de waterfase. Om in computermodellen een goede inschatting te kunnen maken van deze biologisch versnelde oplossing is een nauwkeurige weergave van de dynamische biomassa vereist. Dit is niet eenvoudig omdat de biomassa ter plaatse van verontreinigingsituaties onderhavig zijn aan de omgevingscondities, waardoor bijvoorbeeld de bacteri ̈en die DNAPL afbreken worden gehinderd door de aanof afwezigheid van bepaalde componenten of moeten concurreren met andere bacteri ̈en. 

In de volgende hoofdstukken worden laboratoriumexperimenten besproken die zijn uitgevoerd in flesjes, kolommen en een grote tweedimensionale tank met opgeloste olie of met puur product. De verschillende experimenten, met een looptijd van een jaar, zijn uitgevoerd onder ana ̈erobe omstandigheden met bacteri ̈en in het grondwater van een met tetrachlooretheen (Per) verontreinigde locatie in Ne-derland. Door de laboratoriumexperimenten te simuleren met numerieke modellen zijn de relevante processen die optreden bij biologische afbraak in bronzones gekwantificeerd. 

In hoofdstuk 3 worden de resultaten van de experimenten in flesjes besproken, die een beginconcentratie met Per hadden tussen de 0.09 en 0.8 mM of puur product van Per dat resulteert in een concentratie gelijk aan de maximale oplosbaarheid in de waterfase van 1.2 mM. Ondanks dat eerdere publicaties rapporteren dat Per werd afgebroken tot concentraties gelijk aan de maximale oplosbaarheid, werden in de experimenten in flesjes Per-concentraties tot 0.5 mM afgebroken. Met toenemende Per-concentratie nam de volledigheid van de afbraak geleidelijk af. Vervolgens kon de Per-afbraak worden gesimuleerd met een model met de Michaelis-Menten vergelijking en zelfinhibitie met een afbraakconstante van 80 μmol Per l−^1 dag−^1 , een half-saturatie constante van 0.33 mM en een Perinhibitie constante van 0.5 mM. In de literatuur worden hogere afbraaksnelheden gevonden, maar hierbij wordt verondersteld dat de gebruikte biomassa’s niet direct uit het veld komen en zijn aangepast aan de hogere Per-concentraties in de laboratoriumexperimenten. 

Hoofdstuk 4 beschrijft het model dat is ontwikkeld om de resultaten van de experimenten in de flesjes te onderzoeken. Deze resultaten laten zien dat bij toe-nemende Per-concentratie de afbraak niet volledig verloopt en vervolgens helemaal niet meer. Daarnaast zijn er verschillen waargenomen in de resultaten van experimenten die in drievoud zijn uitgevoerd. Met het model wordt de hypothese getest dat de hele dataset kan worden gesimuleerd met behulp van ́e ́en parameterset. Hiervoor worden afbraakparameters geschat en een gevoeligheids


#### 229 

analyse uitgevoerd om de relevantie en invloeden op de Per-afbraak te testen van verschillende andere biologische reacties. Het model bevat kinetische en thermodynamische concepten om Per-afbraak, elektrondonorfermentatie en de groei van biomassa te beschrijven. De afbraakparameters worden geschat door de concentraties van gechloreerde ethenen van ́e ́en experiment te simuleren met behulp van het SCEM-UA-algoritme. Simulaties met deze geschatte parameter voor de andere experimenten geven niet altijd hetzelfde resultaat als de laboratoriumexperimenten. Het model laat een grote gevoeligheid zien voor de inhibitie van gechloreerde ethenen en de snelheid van de fermentatiereacties die elektrondonor produceren in verhouding met de reacties die elektrondonor consumeren. Een kleine verandering in initi ̈ele condities zorgt ervoor dat de concentraties van de gechloreerde ethenen drastisch kunnen veranderen. De geconstateerde verschillen in de experimenten in de flesjes kunnen hiermee voor een groot gedeelte worden verklaard. Dit betekent voor de toepassing van biologische afbraak in veldsituaties dat een kleine verandering in de initi ̈ele condities ervoor kan zorgen dat de dechloreringsreacties niet op maximale snelheid kunnen verlopen omdat het systeem door een andere reactie wordt gedomineerd. 

Hoofdstuk 5 beschrijft het model en de laboratoriumexperimenten in kolommen. Acht kolomexperimenten zijn in drie verschillende opstellingen uitgevoerd met opgelost Per en puur product. De opgeloste Per kon volledig tot etheen worden gedechloreerd tot en met de geteste concentraties van 0.6 mM. In kolommen met een residuaire Per-concentratie was de afbraak niet compleet en was cis-dichlooretheen het eindproduct. De oplossing van Per werd echter wel met een factor vijf versneld door biologische afbraak. Daarnaast kon met deze opstelling de mobilisatie van residuair Per in de aanwezigheid van biologische afbraak worden aangetoond. De kolomexperimenten zijn gemodelleerd met een stoftransportmodel (aangepaste versie van RT3D) dat de oplossing van immobiel Per beschrijft en de afbraak in de waterfase. De parameters die deze processen beschrijven zijn geschat en dit geeft inzicht in de relevantie en interactie van deze processen. Ondanks dat de processen op een simplistische manier zijn gemodelleerd, werden de experimentele resultaten goed gesimuleerd. De belangrijkste observatie is dat de kolommen met een residuaire Per-concentratie niet exact konden worden gesimuleerd met constante parameters voor de Peroplossing. Waarschijnlijk nemen de oplossingsparameters toe in de tijd als biologische afbraak aanwezig is. Dit betekent dat modellen met een constante waarde voor de oplossing van Per een onderschatting geven van de totale massa die kan worden verwijderd. De afbraak verschillen tussen de experimenten in de flesjes en de kolommen kan worden verklaard door de interactie van oplossing, advectie 


230 Samenvatting 

en afbraak. Deze processen cree ̈eren op de porieschaal een Per-gradi ̈ent. Dichtbij de DNAPL-druppel ontstaan concentraties gelijk aan de maximale oplosbaarheid waarbij op korte afstanden daarvan lagere concentraties ontstaan die kunnen worden afgebroken. Dit is dan ook het mechanisme dat ervoor zorgt dat biologische afbraak het in oplossing gaan versneld. 

De tankexperimenten, beschreven in hoofdstuk 6, zijn de beste weergave van de praktijksituatie waar grondwater door de bronzone stroomt en een pluim van opgeloste oliecomponenten ontwikkelt. Hiertoe is een tank van 2080 x 940 mm met een dikte van 45 mm gevuld met zand. Na het inbrengen van bacteri ̈en is 250 ml Per ge ̈ınjecteerd aan de bovenkant, waardoor een bronzone is ontstaan met een residuaire Per en een poel op de bodem. Hierna is de tank continu doorstroomd met ana ̈eroob water met nutri ̈enten en elektrondonor om horizontale grondwaterstroming te simuleren. De analyse van gechloreerde ethene, microbi ̈ele groepen en visuele observatie van de bronzone geven aan dat de Per compleet werd gedechloreerd in de bronzone. De afbraak van cis-dichlooretheen naar vinylchloride verloopt alleen als de Per-concentraties laag zijn (<0.1 mM). Vergelijkbaar verloopt de afbraak van vinylchloride naar etheen pas als de cisdichlooretheen concentraties laag zijn. Biologische afbraak zorgde voor een versnelling van de oplossing omdat de totale concentratie opgeloste ethenen vier keer hoger was dan de maximale Per-oplosbaarheid. Dit is het resultaat van de grotere concentratie gradi ̈ent, hogere Per-oplosbaarheid en een hogere oplossingssnelheid. Daarnaast is ook hier de mobilisatie van residuaire Per aangetoond. Mobilisatie en de toename in oplossingssnelheid in de aanwezigheid van dechloreerders kan mogelijk worden verklaard door de uitscheiding van stoffen door de bacteri ̈en. Over een periode van ́e ́en jaar heeft 135 ml Per de tank verlaten, waarbij in de tank, voornamelijk in de poel, 90 ml is achtergebleven. Deze getallen kunnen worden gesimuleerd met het RT3D model door gebruik te maken van de parameters die zijn bepaald met de kolomexperimenten. 

In het laatste hoofdstuk worden de resultaten van dit onderzoek samengevat en de consequenties voor het toepassen van biologische afbraak op bronzones van DNAPLs verontreinigingen besproken. De resultaten van dit proefschrift laten zien dat biologische afbraak van DNAPL verontreinigingen in bronzones goed mogelijk is. De condities in het veld bepalen voor een groot gedeelte de afbraakproducten en de afbraaksnelheden. De interactie tussen biologische afbraak, oplossing van DNAPL en advectie bepalen dit, maar ze be ̈ınvloeden elkaar en worden be ̈ınvloedt door andere aanwezige factoren. Zelfs bij veranderende omstandigheden kan biologische afbraak van DNAPL anders verlopen of helemaal niet meer optreden. Zo kan bijvoorbeeld eerst al de makkelijk beschik


#### 231 

bare DNAPL oplossen, waarna de minder toegankelijke DNAPL veel langzamer oplost. Daarnaast is het mogelijk dat de bacteri ̈en wel aanwezig zijn, maar als gevolg van preferenti ̈ele stroombanen niet over genoeg elektrondonor beschikken en niet op volle capaciteit DNAPL afbreken. De koppeling van de processen en ruimtelijke variabiliteit zorgt ervoor dat de totale verwijderd massa moeilijk is in te schatten. Daarentegen, als biologische afbraak in de bronzone plaatsvindt, wordt de oplossing van DNAPL ongeveer vier keer versneld. Zeker in bronzones die bestaan uit residuaire Per, kan biologische afbraak ervoor zorgen dat de levensduur van de verontreiniging aanzienlijk wordt verkort. De minder beschikbare DNAPL, aanwezig in poelen, kan minder gemakkelijk met behulp van biologische afbraak versneld worden verwijderd. De bacteri ̈en kunnen er wel voor zorgen dat de pluim uit afbraakproducten bestaat en een beperkte afstand aflegt. De mobilisatie van residuaire Per kan er wel voor zorgen dat uiteindelijk de Per alleen in poelvormen aanwezig is. 



# Curriculum Vitae 

Marian Langevoort was born on the 19th August, 1980 in Zwolle, The Netherlands. In 1997, she completed her secondary eduction (HAVO) at the Nieuwe Veste in Coevorden, before perusing further education at the Saxion Hogeschool IJselland in Deventer. In June 2001, she graduated her B.Sc. with a thesis on the application of Biological Activity Reaction Tests (BARTs) to assess microbial dechlorination of chlorinated ethenes in the field. She continued her education in Environmental Geochemistry at University of Utrecht. Her Master’s thesis was carried out at the Hydrology and Ecology Group, Faculty of Civil Engineering and Technical Geosciences at Delft University of Technology on the subject of modelling a landfill leachate containing mecoprop in Sjølund (Denmark). In 2003, she started her PhD research on an NWO funded project entitled ’Multiphase flow and enhanced biodegradation of dense non-aqueous phase liquids’ at the Environmental Hydrogeology research group, Faculty of Geosciences at the University of Utrecht. The results of this research are summarized in this PhD thesis. From January 2009 she is working as a consultant at Tauw bv in Deventer. 



# Acknowledgements 

Tja, hoe ver ga je terug in de tijd om mensen te bedanken zodat ik tot dit proefschrift kon komen? De keus voor een vervolgstudie op het voortgezet onderwijs was een ware zoektocht en milieutechnologie was misschien wel met veel geluk gekozen. Zoals dit proefschrift bewijst heb ik nooit spijt gehad van de ingeslagen richting en heb ik een mooie weg bewandeld met dit resultaat. Toch maar beginnen met die mensen die me overtuigden en adviseerden over het aio-schap, Birgitta, maar toch ook vooral Majid. De afgelopen jaren heb ik ervaren als een mooie tijd met kansen en mogelijkheden die me brachten in Oxford, Wenen, Kopenhagen en San Francisco, waarbij ik altijd kon rekenen op het vertrouwen van Majid en Ruud. Majid, als mijn directe begeleider, wil ik speciaal bedanken. Hij zorgde altijd voor een open sfeer tijdens onze meetings en wist altijd de vinger op de zere plek te leggen. Met zoveel andere bezigheden, waaronder nog vier aio’s en een handjevol MSc studenten, verdient dat veel respect. Op wetenschappelijk gebied heb ik veel van hem geleerd, maar daarnaast heb ik ook veel aan zijn adviezen gehad voor mijn persoonlijke ontwikkeling. En daar wil ik hem het meest voor bedanken. Dat ik het project overnam van Laurien heb ik altijd lastig gevonden. Ik voelde bij iedereen een groot respect voor haar werkwijze en teleurstelling dat ze besloot te stoppen. De manier waarop Laurien hiermee omging heeft mijn grote bewondering en zorgde ervoor dat ik dit project goed wilde afronden omdat er al een gedegen basis lag. Ik hoop dat het een beetje geworden is wat je voor ogen had. Soms vond ik het wel eens lastig om een multidisciplinair onderzoek te doen. Gelukkig vond ik al snel Anniet en Yvonne bereid me te ondersteunen. Hun praktische instelling zorgde ervoor dat ik daadwerkelijk in het lab aan de slag ging, waar ik een beetje tegenaan hikte. Daarnaast werd ik bij mijn experimenten zeer vakkundig bijgestaan door Pieter. Ook werd ik goed opgeleid zodat ik met de tijd steeds minder hoefde te vragen en aardig zelfoplossend kon werken. Dat 


236 Acknowledgements 

was eigenlijk jammer want vervolgens miste ik Pieter’s gezelschap en het achter Pieter aanhollen door de gang bij een ingeving. De modelsimulaties heb ik uitgevoerd onder een deken van enthousiasme van Toon en Timo. Hoeveel fouten ik ook vond in de modellen, jullie leverden alleen maar energie omdat we zo uiteindelijk konden komen tot een model dat het beste onze experimenten kon simuleren. Als er dan toch nog verschillen zaten tussen onze experimentele resultaten en simulaties werden jullie haast enthousiast omdat we dan informatie konden winnen over de relevante processen. Jullie houding was voor mij erg leerzaam. Natuurlijk was dit onderzoek nooit mogelijk geweest zonder de financi ̈ele steun van NWO. Daarnaast mocht ik advies ontvangen van de commissieleden van TRIAS. Hierbij wil ik Helenius Rogaar, Theo Saat, Timo Heimovaara, Arjan van der Werf, Gosse Schraa, Toon Leijnse, Gerard van Meurs, Cor Hofstee en Peter Raats bedanken voor hun interesse en betrokkenheid bij mijn onderzoek. Bioclear bv. wil ik bedanken voor het ter beschikking stellen van de microbi ̈ele cultuur. Daarnaast bedank ik de Universiteit van Amsterdam voor het ter beschikking stellen van de TDR-apparatuur en Leen de Lange voor de adviezen gebracht met een gezellige noot. Daarnaast wil ik nog een aantal personen bedanken die mij gedurende dit project hebben geholpen op de UU: Kathrin Reimer, Ana Tamarit Esteve, Helen de Waard, Dineke van de Meent, Jan Drenth, Tom Bosma en het overige ondersteunend personeel. In het speciaal bedank ik Margreet voor haar vriendschap. I thank my PhD colleagues for the shared experiences and nice breaks. I would like to mention in particular: Katja, Phil, Sam, Cas, Henk, Twan, Bert-Rik, Saeed, Simona, Vahid, Mariene, Amir, Reza, Nikos, Brijesh, Eric en Maurits. I would also like to thank the BSc and MSc-students that I supervised over the past years. Tot slot wil ik mijn ouders bedanken dat ze me zoveel relativerend vermogen hebben meegegeven dat de te nemen hobbels tijdens dit promotietraject nooit te hoog werden. Wat ik ook doe, ”als ik er maar plezier in heb”, ik weet dat jullie me, samen met Annelies, Jacquelien en Nathana ̈el, altijd steunen. Tot slot wil ik Tom bedanken; ik hou het maar kort, maar ik hoop dat wij nog een lange tijd samen hebben. 

Marian 


