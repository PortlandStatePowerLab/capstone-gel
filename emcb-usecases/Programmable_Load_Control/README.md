# emcb-usecases

Test and validate the benefit of Energy-Management-Circuit-Breakers with Actual DERs.

## Objectives:
In this project, we study the benefits of EMCBs in demand response and peak load mitigation.

## DERs:

Distributed Energy Resources used in this study include the following:

* A. O. Smith Electrical Water Heater.
* A. O. Smith Hybrid Water Heater.
* NHR 9430 Load Simulator (Simulating EVs)

## Simulation:

The simulation part of this project uses GridLAB-D. GridLAB-D is an open source ssoftware developed by PNNL.

## Use-cases:

* Programmable Load Control.
* Load Research.
* EV Managed Charging.
* Cold Load Pickup Mitigation.
* Islanding Support

## Data Files Naming Convention:

### For files from Virtual Peaker website:

* \<which_water_heater\>-\<vp\>\<day\>
    
    * For example, if the data for the Electric Water heater, the name would look like: EWH_VP1.csv

### For files from Power Analyzer:

* \<EWH\>-\<HPWH\>-\<HPWH_mode\>

    * For example, if a heat pump water heater is in a Hybrid mode: ewh_hpwh_Hybrid

    * Heat_Pump_Water_Heater is in Resistive Mode: ewh_hpwh_Electric
 
## Folder Structure:

There are five usecases. The first usecase is Programmable Load Control. Each usecase' data and figures will be stored in a different folder. the Programmable usecase folder is arranged as follows:

   * docs folder is where the references and citations are located.
   * Data/final_logs folder is where the final version of the data located. There are other files that contain data but not used in the report.
   * figures/overleaf_figures folder is where the figures that are used in the report located.
   * scripts folder is where the scripts to modify the log files and plot the data located.
   * GLD_model folder is where the GridLAB-D model that represents the behavior of the EMCB is located.

The rest of the files and folders are kept in this repository as they might be useful for future studies.
