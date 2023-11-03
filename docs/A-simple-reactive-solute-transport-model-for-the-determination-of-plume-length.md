# A simple reactive solute transport model for the determination of 

# plume lengths 

Phil Ham∗, Ruud Schotting and Henning Prommer 

Delft University of Technology, Faculty of Civil Engineering & Geosciences, Section for Hydrology, P.O. Box 5048, 2600 GA Delft, The Netherlands. 

## ABSTRACT 

Transversal dispersion is considered to be the controlling mixing process in many cases where contaminant plumes attenuate naturally. In this article an analytical model is presented, which describes the transport of a reactant B continuously injected at the origin through a 2-D domain initially filled with a reactant A. Moreover a simple, instantaneous chemical reaction of the form A + B → AB is considered. The flow domain is a porous medium, the aquifer assumed homogeneous with steady, uniform flow. Explicit steady state solutions (in the limit t → ∞) are presented for the distributions of reactants and products in x − y space in the form of the modified Bessel function of zeroth order and second kind. From this a solution is presented to quantify the length of a plume given a few basic (geo)hydrological parameters. It is proven that zeroth or first order approximations to the Bessel function, in the limit 0. 1 > β > 1 and 0. 01 > β > 0 .1 respectively, where β = αT /αL; αL = 1, accurately represent plume lengths. Furthermore it is shown that in the first case plume length does not depend on longitudinal dispersivity αL, but only on pre-defined (geo)hydrological parameters, including αT. This result infers that in many practical situations the influence of αL upon plume length is negligible. In the latter case, the plume length is written as a function of both αT and αL. The assumption that αL is only important for the transient development of the plume, is verified through the use of a numerical solution. Results demonstrate that for small values of β plume growth is rapid and largely linear, quickly reaching an asymptotic value. For 0. 01 > β > 0 .1, plume growth demonstrates real longitudinal dispersive effects, growth rate being considerably slower. 

Keywords: Natural attenuation; transversal dispersion; plume length; mixing 

∗Corresponding author. Tel.:+31-(0)15-27-89128; fax: +31-(0)15-27-85915; e-mail: p.a.s.ham@citg.tudelft.nl 


1. Introduction 

Transversal dispersion is often the controlling mixing process in situations where contaminant plumes are subject to Natural Attenuation (NA) [Cirpka et al., 1999]. Indeed transversal mixing through hydrodynamic dispersion is crucial for the supply of electron acceptors, or growth limiting nutrients, to plumes of biodegradable, oxidisable organic compounds [Grathwohl et al., 2000; Klenk and Grathwohl, 2002]. It has been demonstrated through experimental measurements that in simple cases of biodegradation, where two solutes meet and react, there is a clear empirical relationship between plume length and transversal dispersivity [Grathwohl et al., 2001]. Given a number of simplifying assumptions, closed form solutions can be employed to solve the governing advection-diffusion equation, with sorption and/or biodegradation (i.e. decay) terms, e.g. Bear, (1972); Domenico (1987), to list but a few. Those solutions describe the transport and reaction of an electron donor, neglecting the dependency of the electron donor removal rate on the presence of other reactants, in particular electron acceptor concentrations. In the presence of reactions however, the problem is magnified in that both dispersion and reaction(s) tend to decrease the prevailing concentrations with travel distance and it is difficult to separate the influence of each [Domenico, 1987]. The conceptual model underlying the present study is that considered by Borden and Bedient (1986) where aerobic degradation of hydrocarbons is simulated as an instantaneous reaction between the hydrocarbon (electron donor) and oxygen (electron acceptor). It can also be seen as an extension of the study by Gramling et al. (2002). In that study, an instantaneous chemical reaction between aqueous solutions of CuSO 4 and EDT A^4 −, transported through an idealised porous medium, is quantified experimentally and compared to a one dimensional solute mass transport model coupled with reaction equations. The bimolecular reaction is of the form A+B → AB, i.e. a non-kinetic, equilibrium reaction, where amounts of reactants and products are stoichiometrically equal. In practice one should think of AB as a complex of A and B, where complex AB is only produced where both reactants A and B are present. In this way, either reactant A or B is the limiting reactant depending on which side of the reaction front the reaction is taking place. Thus the assumption is made that one electron acceptor is dominating the degradation process and the influence of all others is negligible, which in reality limits the general applicability of the model developed. Similar experimental and modelling work concerning this type of reaction has also recently been carried out by Rahman et al. (2003) and Knutsen et al. (2003). The problem considered by Gramling et al. (2002) is thus: A front of reactant A travels through a one dimensional domain initially filled with a concentration of reactant B. For simplicity CA/Co = CB /Co = 1. The schematics of the reaction between reactant A and B is represented in Figure 1. The schematics are analogous with the analytical solution presented in the paper. In Figure 1(a), the area under the left curve represents the total CA in the column, i.e. CA + CAB. Likewise the area under the right curve represents the total CB in the column, i.e CB + CAB. Note in Figure 1(b), at the centre of the reaction front, the concentrations of A and B are zero. For simplicity, the notation CAT^ and CB T^ will be used to denote the total aqueous molar concentration of A and B respectively. The focus of this article is on macro-scale dispersion; the governing flow and transport equations define advective and dispersive processes over representative elementary volumes. However, 


Figure 1: Schematics of reaction between two chemical species CA and CB within a column (from Gramling et al., 2002). 

it is well understood that in the context of biodegradation, the relevant scale of mixing is the pore scale [Bear, 1972; Cirpka et al., 1999]. It is therefore important to clarify that the mechanisms of dispersion are scale-dependent [Dykaar and Kitanidis, 1996] and the assumption here is that local-scale mixing/dispersion be similar to plume-scale/macro-scale dispersion. This is valid in the case of uniform flow through a homogeneous domain. Homogeneous here means that the spatial scale of any heterogeneity, physical or chemical, is small compared to the scale of the contaminant (electron donor) plume. Note that in practice there might be many situations where this assumption does not apply, as for example discussed by Trefry et al. (2003) but, moreover, the reader should be aware that understanding scale issues is critical to understanding dispersive processes. 

2. Problem statement 

A bimolecular chemical reaction is considered between two solutes that goes to completion, i.e. 

A + B → AB (1) 

Initially, the two dimensional flow domain Ω contains a constant concentration CA. At a point (x 0 , y 0 ), solute B is injected into the flow domain with constant mass flow rate Q ∗ CB , where CB denotes the concentration of reactant B. The flow field in Ω is constant and uniform, such that q = (qx, 0), where qx denotes the specific discharge in the positive x−direction. Figure 2(a) is a schematic representation of the problem definition. Figure 2(b) is the idealised contour distribution (of the reactants) for this problem. For the bimolecular reaction considered here, the rate of production of AB at any point in the flow domain is equal to the rate of loss of each reactant, implying 

rAB = −rA = −rB. (2) 

The reaction (1) can be envisaged at the reaction fringe. In Figure 3 the profiles through an idealised cross-section in both the xand y-directions for this problem are considered. Consistent with the work of Gramling et al. (2002), product AB is only produced where both reactant A 


 A 

 A 

 A 

 A 

 B 

 A 

 A 

 A 

 A A 

 A 

 oo 

 A 

 x 

 C 

 C 

 C 

 C 

 C 

 Q.C 

 C 

 C 

 C 

 C C 

 y 

 (x ,y ) 

 C 

 q 

 x 

 y 

 x 

 0,0 

Figure 2: Domain Ω: above, (a) Problem definition, and below, (b) idealised reactant (contour) distributions. 

_F 2 F_ (^) _m F 1 F 1 Fm F_ (^2) _y C AB CAB C BT C B C AT C A_ 0 0.2 0.4 0.6 0.8 1 C/Co length (m) _x C B CB_^ _T C A CA_^ _T F m_ 0 0.2 0.4 0.6 0.8 1 C/Co length (m) Figure 3: Idealised profiles of reactants and product across the reactive fringe for a cross section in, left, (a) y-direction and, right, (b) x-direction: CAT^ and CB T^ denote the total aqueous concentration of A and B respectively, CA, CB and CAB denote the concentrations of pure A, B and AB; points Fm, F 1 and F 2 , denote the centre, inner and outer boundaries of the plume fringe respectively. 


and B are simultaneously present; thus equation (2) demonstrates that either reactant A or B is the limiting reactant depending on the location in the fringe at which the reaction is taking place. Note also that point Fm is the point at the centre of the plume fringe, where the concentrations of pure A and B are identically zero. In Figure 3(a) F 1 and F 2 represent the outer and inner boundaries of the fringe, i.e. where CB = 1 and CA = 1 respectively. In Figure 3(b) F 1 coincides with the origin and F 2 ¿ 1000 (in the positive x halfplane). 

3. Model equations, boundary and initial conditions 

 The mass-balance equations for reactants A and B are given by 

n ∂CA ∂t 

 + qx 

## ∂CA 

 ∂x 

 − αLqx 

## ∂^2 CA 

 ∂x^2 

 − αT qx 

## ∂^2 CA 

 ∂y^2 

 + rAB = 0, (3) 

n ∂CB ∂t 

 + qx 

## ∂CB 

 ∂x 

 − αLqx 

## ∂^2 CB 

 ∂x^2 

 − αT qx 

## ∂^2 CB 

 ∂y^2 

 + rAB = 0, (4) 

and for product AB 

n ∂C AB ∂t 

 + qx 

## ∂CAB 

 ∂x 

 − αLqx 

## ∂^2 CAB 

 ∂x^2 

 − αT qx 

## ∂^2 CAB 

 ∂y^2 

 − rAB = 0. (5) 

Here, αL and αT denote the longitudinal and transversal dispersion lengths respectively. Note that this particular set of mass balance equations only holds under the assumption that αL and αT are constant and equal for all species present in a uniform flow field. Adding the mass balance equations (4) and (5) yields 

n ∂CB T ∂t 

 + qx 

## ∂CB T 

 ∂x 

 − αLqx 

## ∂^2 CB T 

 ∂x^2 

 − αT qx 

## ∂^2 CB T 

 ∂y^2 

## = 0, (6) 

where CB T^ = CB T^ (x, y, t) = CB (x, y, t) + CAB (x, y, t) denotes the combined concentrations of B and AB, i.e. the total molar concentration of reactant B in domain Ω. Introducing the dimensionless parameters 

x∗^ = 

 x αL 

 , y∗^ = 

 y αL 

 , and q∗^ = 

 qx qo 

## , (7) 

and substituting these into (6) gives 

n ∂C B T ∂t 

## + 

 qoq∗ αL 

## ∂CB T 

 ∂x∗^ 

## − 

 qoq∗ αL 

## ∂^2 CB T 

 ∂x∗^2 

## − 

 qoq∗αT αL^2 

## ∂^2 CB T 

 ∂y∗^2 

## = 0. (8) 

Multiplying (8) by αL/qo, introducing the dimensionless parameter t∗^ = tqo/nαL and the new variable β = αT /αL, and dropping the ∗^ notation for convenience yields 

 ∂CB T ∂t 

 + q ∂C B T ∂x 

 − q ∂ 

(^2) CB T ∂x^2 − βq ∂ (^2) CB T ∂y^2 

## = 0, (9) 


i.e., the mass balance equation for CB T^ in dimensionless notation. The uniform flow field infers qo = qx, implying q∗^ = 1. Introducing the moving coordinate s(x, t) = x − t such that CB T^ (x, y, t) = CB T^ (s(x, t), y, t) gives 

 ∂CB T ∂t 

## = 

## ∂^2 CB T 

 ∂s^2 

 + β ∂ 

(^2) CB T ∂y^2 

## , (10) 

which will be the starting point for further analysis. The initial condition is given by 

CB T^ (s, y, 0) = 0 for all (s, y) ∈ R, (11) 

implying 

C(s, y, 0) = C 0 (s, y) = CA for all (s, y) ∈ R. (12) 

At point (x 0 , y 0 ) reactant B is continuously injected, such that 

M = M (t) = 

∫ (^) t 0 QCB dt, (13) where M denotes the injected amount of reactant CB and Q is the injection flow rate, thus QCB is the mass transfer rate in mols−^1. 

4. Solution procedure 

First consider instantaneous injection of a constant amount M in point (x 0 , y 0 ). In this case the fundamental solution of (10) is given by [Carslaw and Jaeger, 1986] 

CB T^ (s, y, t) = 

## M 

 4 π 

## √ 

 β 

## 1 

 t e 

− (s−x 40 t− t)2− (y− 4 βty0)2 (^). (14) Next consider continuous injection in (x 0 , y 0 ), such that dM = QCB dt. (15) The instantaneous result of the injection of an infinitesimally small amount dM on concentration follows directly from (14) and (15), yielding dCB T^ (s, y, t) = dM 4 π 

## √ 

 β 

## 1 

 t e 

− (s−x 40 t− t)2− (y− 4 βty0)2 (^). (16) For continuous injection in time interval (0, t) one obtains CB T^ (s, y, t) = 

## CB Q 

 4 π 

∫ (^) t 0 

## 1 

 (t − τ ) 

 e−^ 

 (s−x 0 −(t−τ ))2 4(t−τ ) −^ (y−y0)2 

4 β(t−τ ) (^) dθ. (17) Next, set ξ = t − τ. Under the assumption that the injection point (x 0 , y 0 ) coincides with the origin (0, 0) of our coordinate system, the integral (17) can be recast into CB T^ (s, y, t) = − 

## CB Q 

 4 π 

 e 2 s^ ∫^ t 0 

## 1 

 ξ e 

− A(s,y ξ )−Bξ (^) dξ, (18) 


where A(s, y) and B are respectively given by 

A(s, y) = 

 βs^2 + y^2 4 β 

 and B = 1 4 

## . (19) 

Written using dimensionless notation, (18) becomes 

 CB T CB 

## = − 

## F 

## 2 

## √ 

 β e 

 s 2 ∫^ t 0 

## 1 

 ξ e 

− A(s,y ξ )−Bξ (^) dξ, (20) where one easily obtains F = (^2) πqnQoαL. In the limit t → ∞, (20) reduces to the stationary concentration distribution CB T CB 

## = 

## F 

## 2 

## √ 

 β e 

 s 2 K 0 (2 

## √ 

## AB), (21) 

where K 0 denotes the modified Bessel function of zeroth order and second kind. In terms of the original dimensionless variables [Carslaw and Jaeger, 1986] 

CB T^ (x∗, y∗, ∞) = 

## F 

## √ 

 β e 

 x∗ 

(^2) K 0   1 2 √√ √√ ( x∗^2 + y∗^2 β )  (^). (22) The solution procedure implies that an infinite concentration of reactant B (CB ) is concentrated in point (x 0 , y 0 ) at time t = 0. Physically this is unrealistic because in reality there is always a finite value for CB , however mathematically the assumption allows the derivation of an explicit solution (22) to the problem using the fundamental solution. Close to the origin therefore, the solution (22) of CB T^ is not representative of a practical situation; as (x, y) −→ (0, 0), CB T^ −→ ∞. However since these non-physical effects occur only in close proximity to the origin, values of CB T^ at all other positions in the domain will not significantly reflect this phenomenon, thus these effects should be ignored. If it is necessary to determine the concentration profiles of reactants and products analytically, say along the line y = 0, i.e. along a cross section of the plume in this problem, care must be taken with respect to the phenomenon described above. In general, solute concentrations are scaled by C 0 , i.e concentration equal to one. Therefore let CA C 0 

## = 

## CB 

## C 0 

## = 1. (23) 

It follows from symmetry (Figure 3(b)) that 

 CAT C 0 

## = 1 − 

## CB T 

## C 0 

 for Fm > x > ∞ and 

## CB T 

## C 0 

## = 1 − 

## CAT 

## C 0 

 for 0 < x < Fm, and (24) 

## CA 

## C 0 

## = 2 

## CAT 

## C 0 

 − 1 for Fm > x > ∞ and 

## CB 

## C 0 

## = 2 

## CB T 

## C 0 

 − 1 for 0 < x < Fm. (25) 

As already described CB /C 0 = ∞ at (0, 0), therefore the solution is manipulated to disregard this non-physical effect in close proximity to the origin. In such a way one can remove, without 


 significant effect on the results, the profiles of CB /CO > 1. This is demonstrated in the following example and Figure 4: 

 Example. Selecting the values 

 n = 0. 2 π, Q = 10, q 0 = 1, αL = 10, αT = 1, (26) 

 for the parameters in equation (22), yields 

 CB T^ (x, y, ∞) = 

## √ 

## 10 

## 10 

 e 20 x K 0 

( (^1) 20 √ x^2 + 10y^2 ) 

. (27) 

 For this set of parameters, i.e. the distance from the origin to the point F 1 where CB T^ (x, 0 , ∞) = 1 is given by 

 F 1 ≈ 1. 14 m. (28) 

 Therefore, in this profile, interest is limited to solutions of CB T^ for values of x ≥ F 1 ≈ 1. 14 m. The value of CB T^ and therefore CB for x < F 1 ≈ 1. 14 m is taken to be 1. Likewise the point Fm, where reactants B and A are zero, can be determined by solving equation (25), i.e. obtaining the solution in x for CB T^ (x, 0 , ∞) = 0.5 (25). It follows that the solution is 

 Fm ≈ 9. 11 m. (29) 

 The profiles of reactants A and B and product AB can be visualised in Figure 4. 

 x 

 C B 

 CB^ T 

 C A 

 CA^ T 

_F 1 F_ (^) _m_ 0 0.2 0.4 0.6 0.8 1 C/Co 20 40 60 80 100 Length (m) _y x 0.2 0.5_ –8^ _F_^1 _Fm_ –6 –4 –2 2 4 6 8 20 40 60 80 Figure 4: Left, (a) profiles of reactants A and B and product AB along x−axis and, right, (b) distribution of reactant B (C/Co contours 1.0, 0.5 and 0.2) in domain Ω. In order to validate these results, a numerical comparison was undertaken using PHT3D [Prommer et al., 2003], a verified reactive transport model. PHT3D combines the transport simulator MT3DMS [Zheng and Wang, 1999] with the geochemical model PHREEQC-2 [Parkhurst 


and Appello, 1999] to simulate reactive transport in saturated porous media. A (half-)model grid 19.5m wide by 117.7m long, comprising 1220 grid cells, was used in conjunction with the afore selected hydrological parameters. The HMOC scheme was used to solve the advection-diffusion equations and the model was simulated for 180 days, at timesteps of 1 day whereby steady state flow conditions were reached. The numerical model is only realistic if the injection rate of CB is chosen such that it is negligible with respect to the flow field. In this way, Q = qxA and qx cancels from (22), and the flow field remains homogeneous. Similarly as done in the example above, the input files for PHT3D were also manipulated such that CB for x < F 1 was fixed at CB /Co = 1, where F 1 = 1.14 taken from the analytical result. Figure 5 shows block-centered results obtained from the numerical simulation. The fit is good, with only small discrepancies between the analytical and numerically generated profiles occurring close to the origin, as to be expected, i.e. Fmnum^ ≈ 8. 10 m in the numerically generated profile as compared to Fmexact^ ≈ 9. 11 m. Using a finer model grid may eliminate part of this error, although some discrepancy will always remain. 

Figure 5: Numerical generated profiles for reactants A and B and product AB along the x-axis. 

5. Plume length 

Plume length L is arbitrarily chosen as the length of the plume measured along the x-axis from the origin to a certain concentration contour. The notation βn^ is used to represent the ratio of αT /αL, where the superscript n represents the value of αL. Figure 6 represents the concentration distribution of the plume, resulting from the solution of equation (22), where β^1 = αT /αL = 1; αL = 1, and the sum of the other hydrological parameters, as written in equation (22), is equal to 1. The outermost contour C/Co is equal to 0.1. In this article the C/Co = 0.1 contour is chosen to define the end of a plume, which leads to the implicit expression 

## CB T^ (L∗, 0 , ∞) = 

## F 

## √ 

 β e 

 L∗ 

(^2) K 0 ( (^) L∗ 2 ) = 0. 1. (30) 


 y 

 x 

 * 

 * 

 –3 

 –2 

 –1 

 0 

 1 

 2 

 3 

 2 4 6 8 10 

Figure 6: C/Co distribution from equation (22); β^1 = αT /αL = 1 and the sum of the other parameters as written in equation (22) equal to 1. 

Note that this expression implicitly defines the relation between plume length L and the two dispersion lengths, i.e. L = L(αL, αT ). In general the argument of the Bessel function in (30) will be large and K 0 (s) can be approximated for 2 ≤ s < +∞ by the series expansion (Abramowitz and Stegun, 1964) 

s 

 1 

(^2) es^ K 0 (s) = 1. 25331414 − 0. 07832358 ( 2 s ) + 0. 02189568 ( 2 s ) 2 − 0. 01062446 ( 2 s ) 3 

## +0. 00587872 

( (^2) s ) 4 − 0. 00251540 ( (^2) s ) 5 + 0. 00053208 ( (^2) s ) 6 + ε, where |ε| < 1 .9 10−^7. As a first approximation only the first term on the right-hand side of the series expansion is considered, i.e. s (^12) es^ K 0 (s) ≈ 1. 25331414 ≈ √ π 2 

## . (31) 

Substitution of this approximation in (30) yields 

## L∗^ = 

## L 

 αL 

## ≈ 2 

( (^) F 0. 1 ) (^2) π 2 

## · 

## 1 

 β 

 = 100πF 2 · 

## 1 

 β 

## = 100 

 πn^2 Q^2 4 π^2 q^2 o αL 

## · 

## 1 

 αT 

## . (32) 

Simplifying (32) gives 

## L ≈ 

 100 n^2 Q^2 4 πq^2 o 

## · 

## 1 

 αT 

## . (33) 

Note that in this approximation, plume length L is solely a function of αT , i.e. independent of the longitudinal dispersion length αL. Figure 7 shows plume length and concentration distributions, as obtained from the exact solution (30), for different values of β^1 = αT /αL. Furthermore it is important to note excellent agreement between the zeroth order approximation (33) and the exact solution (30) when β^1 = 1; the two lines overlying each other in Figure 7, the difference between them being in the order of 1cm. As a next, more accurate approximation, the second 


 y 

 x 

 β=0.01 

 β=0.1 

 β=1 

 –15 

 –10 

 –5 

 0 

 5 

 10 

 15 

 Width 

 –50 50 100 150 200 250 300 Length 

Figure 7: 0. 1 C/Co contourplots of the exact solution for β^1 = 1, 0 .1 and 0.01. Note the zeroth order approximation for β^1 = 1 fits the contour for the exact solution, thus two distinct lines are not visible here. 

term at the right-hand side of the series expansion for K 0 is included, i.e. 

s 

(^12) es^ K 0 (s) ≈ 1. 25331414 − 0. 07832358 ( 2 s ) ≈ √ π 2 

## − 

## √ 

 2 π 32 

 ( 2 s 

 ) 

. (34) 

Substitution of this approximation in (30) gives 

 F √ β 

 √ 2 L∗ 

 (√ π 2 

## − 

## √ 

 2 π 32 

 ( 4 L∗ 

 )) ≈ 0. 1 , (35) 

or 

 0. 005 β F 2 αL 

## L − 

 π 2 

## + 

 π^2 α^2 L L^2 

## ≈ 0. (36) 

The solution of (36), i.e. a third-order algebraic equation, implicitly defines L = L(αL, αT ). Figure 8 represents both the zeroth and first order approximations, together with the exact (Bessel) solution. For values of 0. 1 > β^1 > 1 the zeroth order approximation (33) satisfactorily predicts plume lengths. For β^1 < 0 .1, the difference between the zeroth order approximation and the exact solution become significant and as a better estimate of plume length the first order approximation (36) should be used, although for β^1 < 0 .5 this too becomes increasingly inaccurate. It is also relevant to note that the appoximate expressions for plume length L (33),(36) remain unaffected by the non-physical phenomena discussed earlier, the extent of the plume being typically far away from (x 0 , y 0 ). 

6. Transient plume length development 

At values of β^1 close to 1, the length of a stationary plume is almost independent of αL. The assumption therefore is that αL is only important for the transient development of the plume. In order to verify this assumption, the transient plume is analysed; the starting point for the 


 First order soln. 

 Zeroth order soln. 

1/β=α (^) _L_ /α _T Exact (Bessel) soln._ 0 50 100 150 200 250 300 L (m) (^20 40 60 80 100) Figure 8: Effect of increasing ratio of β^1 on plume length. analysis is the expression that relates L(t), i.e. the length of the plume measured from the injection point at x = 0 along the x−axis to the 0. 1 C/Co concentration contour. This is given by CB T^ (L∗(t), 0 , t) = 

## F 

 2 ∗ √β e 

 L∗(t) 2 

∫ (^) t 0 

## 1 

 ζ e 

 − pL∗ ζ( t)2−Bsdζ = 0. 1 (37) 

where p = 1/4. This problem can be solved numerically as follows. Equation (37) is rewritten as 

∫ (^) t 0 

## 1 

 ζ e 

 − pL 2(t)2 α^2 Lζ −Bζ dζ = 1 5 

## √ 

 β 

 F e 

 L(t) 2 αL 

## . (38) 

The hydrological parameters are taken to be the same as those used in the Example in Section 4, i.e. n = 0. 2 π, Q = 10, qx = 1, αT = 1. As a first step, the right hand side (RHS) of equation (38) is solved, specifying the appropriate plume length. The integral on the left hand side (LHS) can be split into N segments and approximated using the trapezium rule, solved iteratively for small length steps (∆L) and time steps (∆t) until it is equal to the RHS. In this way the time t taken to reach a certain plume length L can then be related (see Figure 9), and consecutive solutions produce the transient solution. The problem (37) was calculated for β^1 = 1, 0.1 and 0 .01. Figure 10 represents the transient development of the plume. For 1 > β^1 > 0 .1 plume length develops rapidly to an asymptotic value; for values of β^1 close to unity the initial growth in plume length is almost linear. For smaller values of β^1 , i.e. β^1 < 0 .1, plume development is considerably slower. It appears that in these cases αL plays a much more important role and acts as a kind of ’smoothing effect’, delaying the development of the plume. Note that the asymptotic values, as one might expect, are identical to the results for plume lengths obtained in Section 5. 

7. A note on βn 

Since β is defined as αT /αL, a β value of 1 implies that αT = αL and neither the exact value of αL or αT is known. The superscript n was introduced to clarify this ratio, but little has been 


Figure 9: Solution procedure to approximate the integral in equation (38). 

Figure 10: Transient development of plume; results for β^1 = 1, 0 .1 and 0.01. 


said over its relevance. Figure 11 shows the variation of plume length at the stationary condition against values of the transversal dispersivity αT and clearly demonstrates that plume lengths are not the same for all βn^ values. 

Figure 11: Variation of plume length with value of αT. 

8. Conclusions 

Concentration distributions of reactants and products involved in the simple bimolecular reaction (1) anywhere in a two dimensional domain can be modelled using the solution (22) of the modified Bessel function. However it is important to state that in the derivation method of equation (22) non-physical effects are introduced. Far away from the origin, these effects are negligible, and this has been verified with the use of a reliable numerical model. Defining the length of a plume as the distance from the origin to an arbitrary concentration contour (C/Co = 0.1 in this study) enables the solution of the modified Bessel function in terms of plume length L. Denoting β^1 = αT /αL = 1 (where the superscript 1 denotes αL = 1), in the limit where 0 > β^1 > 0 .1, plume length L can be expressed as a zeroth order approximation (33) consisting of a few hydrological parameters including αT and independent of αL. In most practical (experimental) cases, the ratio αT /αL is often assumed to be ≈ 0 .1, thus the use of such an approximation to equation (30) should serve accurately to quantify the length of a plume in situations where fast instantaneous reactions are occurring, e.g. simple cases of aerobic degradation. A more accurate approximation for L when β^1 < 0 .1 can be obtained from a first order approximation (36), which depends both on αT and αL. Although an expression is presented for the stationary case which demonstrates that the length and distribution of a plume is independent of αL, numerical simulations show that the longitudinal dispersion plays an important role in transient plume development, especially for small values of β^1. For values of β^1 close to unity, advection dominates significantly over the processes of dispersion and plumes grow rapidly in length, quickly reaching the asymptotic value. When αT is small in comparison to αL, plumes develop much more gradually and plume 


development becomes a real advective-diffusive process. However, the most important conclusion remains thus: In practical situations where there is one electron acceptor dominating the degradation process, the stationary length of a plume can be quantified solely as a function of the transversal dispersion coefficient, αT. 

Acknowledgements 

This research is funded by the Dutch research organization TRIAS, an initiative of NWOALW, SKB and Delft Cluster. The article was made possible by work carried out in conjunction with Prof. Peter Grathwohl and Asa Olsson of the Geosciences laboratory at the University of Tubingen, Germany. The authors would like to acknowledge the community of CORONA for their support in producing this article. CORONA is a research project supported by the European Commission under the Fifth Framework Programme, Key Action 1 ’Sustainable Management and Quality of Water’, within the thematic programme for Energy, Environment and Sustainable Development. This article does not represent the opinion of the Community and the authors are solely responsible for the use of any data herein. 

## REFERENCES 

1. Abromowitz and Stegun (eds.), 1964. Handbook of Mathematical Functions. With fomulas,     graphs and mathematical tables. Dover Publications, Inc., New York. 

2. Bear, J., 1972. Dynamics of Fluids in Porous Media. American Elsevier, New York. 

3. Borden, R.C., Bedient, P.B., 1986. Transport of dissolved hydrocarbons influenced by oxygen-     limited biodegradation: Theoretical development. Water Resour. Res. 13, 1973-1982. 

4. In Carslaw and Jaeger (eds.), 1986. Conduction of Heat in Solids (Second Edition). Claredon     Press, Oxford. 

5. Cirpka, O.A., Frind, E.O., Helmig, R., 1999. Numerical simulation of biodegradation con-     trolled by transverse mixin g. J. Contam. Hydrol. 40, 159-182. 

6. Domenico, P.A. An analytical model for multidimensional transport of a decaying contami-     nant species. J. Hydrol. 91, 49-58. 

7. Dykaar, B.B., Kitanidis, P.K., 1996. Macrotransport of a biologically reacting solute through     porous media. Water Resour. Res. 32(2), 307-320. 

8. Gramling, C.M., Harvey, C.F., Meigs, L.C., 2002. Reactive Transport in Porous Media: A     Comparison of Model Prediction with Laboratory Visualization. Environ. Sci. Technol. 36,     2508-2514. 

9. Grathwohl, P., Klenk, I.D., Ederhardt, C., Maier, U., 2000. Steady state plumes: mechanisms     of transverse mixing in aquifers. Contaminant Site Remediation: From Source Zones to     Ecosystems. Proc. 2000, CRSC, Melbourne, Vic., 4-8 Dec., Centre for Groundwater Studies,     CSIRO, Perth, Western Australia, 459-466. 

10. Grathwohl, P., Klenk, I.D., Eberhardt, C., Maier, U., 2001. Steady State Plumes: Mech-     anisms of Transverse Mixing in Aquifers. In Seiler and Wohnlich (eds): New Approaches     Charcterizing Groundwater Flow, proceedings IAH congress, 89 - 94. 

11. Klenk, I.D., Grathwohl, P., 2002. Transverse vertical dispersion in groundwater and the     capillary fringe. J. Contam. Hydrol. 58, 111-128. 


12. Knutson, C., Werth, C., Valocchi, A., 2003. The influence of pore-scale transverse mixing     upon biodegradation reactions and biomass growth. Geophysical Research Abstracts, Volume     5, EAE03-A-04690. 

13. Parkhurst, D.L., Appelo, C.A.J., 1999. User’s guide to PHREEQC (Version 2)-A computer     program for speciation, batch-reaction , one-dimensional transport, and inverse geochemical     calculations. U.S. Geological Survey Water-Resources Investigations Report 99-4259, 312 p. 

14. Prommer, H., Barry, D.A., Zheng, C., 2003. MODFLOW/MT3DMS-based reactive multi-     component transport modelling. J. Ground Water 41(2), 247-257. 

15. Rahman, M.A., Jose, S.C., Cirpka, O.A., 2003. Large-scale sandbox experiments on disper-     sion and mixing. Geophysical Research Abstracts, Volume 5, EAE03-A-05935. 

16. Trefry, M. G., Ruan, F. P., McLaughlin, D., 2003. Numerical simulations of preasymptotic     transport in heterogeneous porous media: Departures from the Gaussian limit. Water Resour.     Res. 39(3),. 

17. Zheng, C., Wang, P.P., 1999. MT3DMS: A modular three-dimensional multispecies model     for simulation of advection, dispersion and chemical reactions of contaminants in ground-     water systems; Documentation and User’s Guide. Contract Report SERDP-99-1, U.S. Army     Engineer Research and Development Center, Vicksburg, MS. 


