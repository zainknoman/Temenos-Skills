# AA.SIMULATION.RUNNER — Table Schema

> Source: `INSERTS/I_F.AA.SIMULATION.RUNNER` in `AA_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.SIM.DESCRIPTION` | `AaSimulationRunner_Description` |  |  |  |
| 2 | `AA.SIM.ARRANGEMENT.REF` | `AaSimulationRunner_ArrangementRef` | TField |  | This field represents the arrangement reference which can be an existing arrangement or a simulated arrangement. If this field is input with an existing arrangement reference then it represents that existing arrangement is simulated. If this field is input with a simulated arrangement reference then it represents that arrangement is virtual |
| 3 | `AA.SIM.SIM.CURRENCY` | `AaSimulationRunner_SimCurrency` | TField |  | Defaults the base currency for this arrangement. NOINPUT field |
| 4 | `AA.SIM.SIM.RUN.DATE` | `AaSimulationRunner_SimRunDate` | TField |  | Date on which this simulation is run. Usually defaults to TODAY |
| 5 | `AA.SIM.SIM.END.DATE` | `AaSimulationRunner_SimEndDate` | TField |  | This field denotes date upto which Simulation needs to run. It left as NULL would run upto the Matuity date of the arrangement. |
| 6 | `AA.SIM.SIM.S.DATE` | `AaSimulationRunner_SimSDate` |  |  |  |
| 7 | `AA.SIM.S.ACTIVITY` | `AaSimulationRunner_SActivity` |  |  |  |
| 8 | `AA.SIM.S.RUN.STAGE` | `AaSimulationRunner_SRunStage` |  |  |  |
| 9 | `AA.SIM.S.AMOUNT` | `AaSimulationRunner_SAmount` |  |  |  |
| 10 | `AA.SIM.RUN.S.ACT` | `AaSimulationRunner_RunSAct` |  |  |  |
| 11 | `AA.SIM.RESERVED.16` | `AaSimulationRunner_Reserved16` |  |  |  |
| 12 | `AA.SIM.RESERVED.15` | `AaSimulationRunner_Reserved15` |  |  |  |
| 13 | `AA.SIM.RESERVED.14` | `AaSimulationRunner_Reserved14` |  |  |  |
| 14 | `AA.SIM.RESERVED.13` | `AaSimulationRunner_Reserved13` |  |  |  |
| 15 | `AA.SIM.SIM.U.DATE` | `AaSimulationRunner_SimUDate` |  |  |  |
| 16 | `AA.SIM.U.ACTIVITY` | `AaSimulationRunner_UActivity` |  |  |  |
| 17 | `AA.SIM.U.RUN.STAGE` | `AaSimulationRunner_URunStage` |  |  |  |
| 18 | `AA.SIM.U.AMOUNT` | `AaSimulationRunner_UAmount` |  |  |  |
| 19 | `AA.SIM.RUN.U.ACT` | `AaSimulationRunner_RunUAct` |  |  |  |
| 20 | `AA.SIM.RESERVED.12` | `AaSimulationRunner_Reserved12` |  |  |  |
| 21 | `AA.SIM.RESERVED.11` | `AaSimulationRunner_Reserved11` |  |  |  |
| 22 | `AA.SIM.SIM.T.DATE` | `AaSimulationRunner_SimTDate` |  |  |  |
| 23 | `AA.SIM.T.ACTIVITY` | `AaSimulationRunner_TActivity` |  |  |  |
| 24 | `AA.SIM.T.RUN.STAGE` | `AaSimulationRunner_TRunStage` |  |  |  |
| 25 | `AA.SIM.T.AMOUNT` | `AaSimulationRunner_TAmount` |  |  |  |
| 26 | `AA.SIM.T.OVR.AMOUNT` | `AaSimulationRunner_TOvrAmount` |  |  |  |
| 27 | `AA.SIM.RUN.T.ACT` | `AaSimulationRunner_RunTAct` |  |  |  |
| 28 | `AA.SIM.RESERVED.10` | `AaSimulationRunner_Reserved10` |  |  |  |
| 29 | `AA.SIM.RESERVED.09` | `AaSimulationRunner_Reserved09` |  |  |  |
| 30 | `AA.SIM.EXECUTE.SIMULATION` | `AaSimulationRunner_ExecuteSimulation` | TField |  | This field allows the user to decide whehther the simulation can be executed to live arrangement. YES can be set if simulation status is simulation is successfull |
| 31 | `AA.SIM.SIM.CAPTURE.REF` | `AaSimulationRunner_SimCaptureRef` |  |  |  |
| 32 | `AA.SIM.STATUS` | `AaSimulationRunner_Status` | TField |  | This denotes the status of the simulation runner. COMPLETED - SUCCESSFULLY -&gt; This denotes that runner has been executed successfully COMPLETED - ERROR -&gt; This denotes that runner is completed but has got errors while executing Processing -&gt; This denotes that runner is getting executed |
| 33 | `AA.SIM.ERR.SOURCE` | `AaSimulationRunner_ErrSource` |  |  |  |
| 34 | `AA.SIM.ERR.MESSAGE` | `AaSimulationRunner_ErrMessage` |  |  |  |
| 35 | `AA.SIM.INFO.SOURCE` | `AaSimulationRunner_InfoSource` |  |  |  |
| 36 | `AA.SIM.INFO.MESSAGE` | `AaSimulationRunner_InfoMessage` |  |  |  |
| 37 | `AA.SIM.LOCAL.REF` | `AaSimulationRunner_LocalRef` |  |  |  |
| 38 | `AA.SIM.QUOTATION.REFERENCE` | `AaSimulationRunner_QuotationReference` | TField |  |  |
| 39 | `AA.SIM.INITIATING.REFERENCE` | `AaSimulationRunner_InitiatingReference` | TField |  | This field is used to identify the initiating reference of the Simulation. The value given for the CONTEXT.TYPE INITIATING.REFERENCE in the Simulation Capture will be mapped into this field. This is to suppress archival of such simulation records which are triggered from External systems. |
| 40 | `AA.SIM.OVERRIDE` | `AaSimulationRunner_Override` |  |  |  |
| 41 | `AA.SIM.RECORD.STATUS` | `AaSimulationRunner_RecordStatus` | String |  |  |
| 42 | `AA.SIM.CURR.NO` | `AaSimulationRunner_CurrNo` | String |  |  |
| 43 | `AA.SIM.INPUTTER` | `AaSimulationRunner_Inputter` |  |  |  |
| 44 | `AA.SIM.DATE.TIME` | `AaSimulationRunner_DateTime` |  |  |  |
| 45 | `AA.SIM.AUTHORISER` | `AaSimulationRunner_Authoriser` | String |  |  |
| 46 | `AA.SIM.CO.CODE` | `AaSimulationRunner_CoCode` | String |  |  |
| 47 | `AA.SIM.DEPT.CODE` | `AaSimulationRunner_DeptCode` | String |  |  |
| 48 | `AA.SIM.AUDITOR.CODE` | `AaSimulationRunner_AuditorCode` | String |  |  |
| 49 | `AA.SIM.AUDIT.DATE.TIME` | `AaSimulationRunner_AuditDateTime` | String |  |  |
| 50 | `AA.SIM.ERR.ARRANGEMENT` | `AaSimulationRunner_ErrArrangement` |  |  |  |
| 51 | `AA.SIM.SYNCHRONOUS` | `AaSimulationRunner_Synchronous` | TField | Yes | This field denotes whether the Simulation is synchronous or not.This field is applicable only for Iris API calls Non mandatory field. |
