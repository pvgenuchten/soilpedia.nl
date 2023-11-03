# Chemically and Electrically Coupled Transport in Clayey Soils and Sed

# iments 

S. Bader (Ph.D. student) Department of Civil Engineering and Technical Geosciences Section for Hydrology and Ecology 

The objective of this research is to quantify the role of chemically and electrically coupled transport in clayey soils and to assess its relevance for the distribution and emission of contaminants and water. 

Introduction Transport of water and solutes in clayey soils and sediments is important in management of groundwater quantity and quality. In nearly all existing groundwater models, water movement is driven by pressure and water density gradients only. However, for well compacted clays, other driving forces can induce water transport as well. Expressions of this behaviour are chemical osmosis (fluid flow in direction of higher salinity), electro-osmosis (flow of water, dragged along by ions moving due to an electric potential gradient), ultrafiltration (accumulation of solute on the inflow side of a membrane due to an hydraulically forced fluid flow) etc. In this TRIAS project, chemical and electro-osmotic processes will be studied in the laboratory and in a field situation for the purpose of incorporating osmotic transport in an existing water and solute transport model; the behaviour of this model will be investigated, using numerical as well as mathematical analysis. The project is a cooperation of researchers from Delft, Utrecht and Amsterdam. In our part of the project we focus on the analytical and numerical modelling of coupled transport. 

Incorporating osmosis in a transient groundwater model leads to non-linear partial differential equations. These can be studied using (semi-)analytical and approximate methods to understand the nature and behaviour of the solutions. Also, numerical techniques can be applied to describe the system of coupled flow processes. A suitable code for this work is METROPOL, a finite element package that can handle variable density of groundwater and high solute concentrations. It will be adapted to incorporate chemical osmosis, electro-osmosis and related effects. This project started in 2001 and is due to finish in 2005. 

Results in 2002 In 2002, the complete model for chemical and electro-osmosis in clay was defined. For chemical osmosis, the following equations for specific discharge q and solute flux Jsd apply: 

 q = −K∇p + λρf ∇ω Jsd = −σρf ωq − Dρf ∇ω. 

Inserting these equations in the mass balances leads to a set of non-linear partial differential equations. It can be shown that, depending on the value of an effective storage parameter, the equations can be reduced to a simplified form, that can be solved analytically. This method was used to model two experiments from literature, one performed in the laboratory and the other experiment in a field situation. Using the scripted finite element builder and numerical solver FlexPDE, the full set of equations was modelled. Figure 1 shows the comparison between numerical and analytical results for the two experiments. The left graph also shows the experimental data of the laboratory experiment. For the first experiment, numerical and analytical results match perfectly. In the second experiment, the storage parameter is relatively large, resulting in a worse approximation for pressure evolution. Also, this research showed the necessary non-validity of the Boussinesq limit. Various 


 0 

 1000 

 2000 

 3000 

 4000 

 5000 

 6000 

 7000 

 8000 

 0 500000 1e+006 1.5e+006 2e+006 2.5e+006 

 pressure(Pa) x=0 

 t(s) analytical experimental numerical 

 -20000 

 0 

 20000 

 40000 

 60000 

 80000 

 0 5e+007 1e+008 1.5e+008 2e+008 2.5e+008 3e+008 3.5e+008 4e+008 

 pressure(Pa) r=a 

 t(s) analytical numerical 

 Figure 1: pressure evolution: comparison of analytical, numerical (and experimental) results 

limiting cases of the equations have been studied to reassure the general validity of the model. An article that reports of these results, has been written and will be published in 2003. For studying electro-osmosis, the following equations have been considered for the specific discharge and the electric current density: 

 q = −K∇p − κe∇V I = −κe∇p − σe∇V 

Some results have been obtained that will aid streaming potential (electric current induced by a pressure gradient) measurements that are performed in Utrecht. Finally, the groundwater code METROPOL has been adapted for chemical osmosis and will shortly be adapted for electro-osmosis. 

Research plan 2003 

- continuation of analysis on the groundwater model incorporating electro-chemical osmosis,     providing support for the design of field and lab experiments 

- extension of METROPOL with electro-osmosis 

- writing articles and start writing Ph.D. thesis 

Publications and presentations in 2002 

- Garavito, A.M., Bader, S., Kooi, H., Richter, K. and Keijzer, Th.J.S. Numerical modelling     of chemical osmosis and ultrafiltration across clay membranes, in: 14th International Con-     ference on Computational Methods in Water Resources (CMWR), 23 - 28 June 2002, Delft,     The Netherlands, 647 - 653, 2002. 

- ‘Analytical modelling of chemical osmosis in clay’ NWO report 

- ‘Chemically and Electrically Coupled Transport in Clayey Soils and Sediments’ Presenta-     tion held at the CMWR 2002 


