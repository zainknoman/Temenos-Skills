# AN.ANACREDIT.PARAMETER — Table Schema

> Source: `INSERTS/I_F.AN.ANACREDIT.PARAMETER` in `AN_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AN.CR.PAR.NAT.ID.REP.COMP` | `AnAnacreditParameter_NatIdRepComp` | TField | Yes | This is the National ID the Reporting Company uses to identify itself to its NCB Validation Rules: Input is mandatory. |
| 2 | `AN.CR.PAR.COUNTRY.JURISDICTION` | `AnAnacreditParameter_CountryJurisdiction` | TField | Yes | This field defines the country of the Reporting Agent Validation Rules: Must be a valid record from COUNTRY table and the input is mandatory |
| 3 | `AN.CR.PAR.UNIT.TYPE` | `AnAnacreditParameter_UnitType` | TField | Yes | The field indicates the unit type of the Reporting Agent. Possible values are HEAD.OFFICE and FOREIGN.BRANCH. Validation Rules: Mandatory field and if the Reporting Agent is a Foreign Branch, the HEAD.OFFICE.ID field is mandatory. |
| 4 | `AN.CR.PAR.HEAD.OFFICE.ID` | `AnAnacreditParameter_HeadOfficeId` | TField | Yes | The Head Office is the legal entity of which the foreign branch or the domestic part is a legally dependent part. This field enables Foreign branches of an institution to reference the Head Office of the Bank. Validation Rules: Mandatory if UNIT.TYPE is FOREIGN.BRANCH. |
| 5 | `AN.CR.PAR.RMS` | `AnAnacreditParameter_Rms` | TField | Yes | Yes or No field that indicates if the Reporting Agent is located in a Reporting Member State Validation Rules: Mandatory field. |
| 6 | `AN.CR.PAR.OBSERVING.AGENT` | `AnAnacreditParameter_ObservingAgent` |  |  |  |
| 7 | `AN.CR.PAR.NAT.ID.OBS.AGENT` | `AnAnacreditParameter_NatIdObsAgent` |  |  |  |
| 8 | `AN.CR.PAR.PRODUCT` | `AnAnacreditParameter_Product` |  |  |  |
| 9 | `AN.CR.PAR.DATA.SET` | `AnAnacreditParameter_DataSet` |  |  |  |
| 10 | `AN.CR.PAR.DATA.TO.BE.REPTD` | `AnAnacreditParameter_DataToBeReptd` |  |  |  |
| 11 | `AN.CR.PAR.REP.FREQ` | `AnAnacreditParameter_RepFreq` |  |  |  |
| 12 | `AN.CR.PAR.REP.CURRENCY` | `AnAnacreditParameter_RepCurrency` |  |  |  |
| 13 | `AN.CR.PAR.REP.THRESHOLD` | `AnAnacreditParameter_RepThreshold` |  |  |  |
| 14 | `AN.CR.PAR.ENTITY.CUS.FIELD` | `AnAnacreditParameter_EntityCusField` |  |  |  |
| 15 | `AN.CR.PAR.ENTITY.CUS.OPERAND` | `AnAnacreditParameter_EntityCusOperand` |  |  |  |
| 16 | `AN.CR.PAR.ENTITY.CUS.VALUE` | `AnAnacreditParameter_EntityCusValue` |  |  |  |
| 17 | `AN.CR.PAR.OUT.ROUTINE` | `AnAnacreditParameter_OutRoutine` | TField |  | An exit point API for the banks to add local information to the extract. Validation Rules: Must be a valid EB.API record. |
| 18 | `AN.CR.PAR.RESERVED.60` | `AnAnacreditParameter_Reserved60` | TField |  |  |
| 19 | `AN.CR.PAR.RESERVED.59` | `AnAnacreditParameter_Reserved59` | TField |  |  |
| 20 | `AN.CR.PAR.RESERVED.58` | `AnAnacreditParameter_Reserved58` | TField |  |  |
| 21 | `AN.CR.PAR.RESERVED.57` | `AnAnacreditParameter_Reserved57` | TField |  |  |
| 22 | `AN.CR.PAR.RESERVED.56` | `AnAnacreditParameter_Reserved56` | TField |  |  |
| 23 | `AN.CR.PAR.RESERVED.55` | `AnAnacreditParameter_Reserved55` | TField |  |  |
| 24 | `AN.CR.PAR.RESERVED.54` | `AnAnacreditParameter_Reserved54` | TField |  |  |
| 25 | `AN.CR.PAR.RESERVED.53` | `AnAnacreditParameter_Reserved53` | TField |  |  |
| 26 | `AN.CR.PAR.RESERVED.52` | `AnAnacreditParameter_Reserved52` | TField |  |  |
| 27 | `AN.CR.PAR.RESERVED.51` | `AnAnacreditParameter_Reserved51` | TField |  |  |
| 28 | `AN.CR.PAR.RESERVED.50` | `AnAnacreditParameter_Reserved50` | TField |  |  |
| 29 | `AN.CR.PAR.RESERVED.49` | `AnAnacreditParameter_Reserved49` | TField |  |  |
| 30 | `AN.CR.PAR.RESERVED.48` | `AnAnacreditParameter_Reserved48` | TField |  |  |
| 31 | `AN.CR.PAR.RESERVED.47` | `AnAnacreditParameter_Reserved47` | TField |  |  |
| 32 | `AN.CR.PAR.RESERVED.46` | `AnAnacreditParameter_Reserved46` | TField |  |  |
| 33 | `AN.CR.PAR.RESERVED.45` | `AnAnacreditParameter_Reserved45` | TField |  |  |
| 34 | `AN.CR.PAR.RESERVED.44` | `AnAnacreditParameter_Reserved44` | TField |  |  |
| 35 | `AN.CR.PAR.RESERVED.43` | `AnAnacreditParameter_Reserved43` | TField |  |  |
| 36 | `AN.CR.PAR.RESERVED.42` | `AnAnacreditParameter_Reserved42` | TField |  |  |
| 37 | `AN.CR.PAR.RESERVED.41` | `AnAnacreditParameter_Reserved41` | TField |  |  |
| 38 | `AN.CR.PAR.RESERVED.40` | `AnAnacreditParameter_Reserved40` | TField |  |  |
| 39 | `AN.CR.PAR.RESERVED.39` | `AnAnacreditParameter_Reserved39` | TField |  |  |
| 40 | `AN.CR.PAR.RESERVED.38` | `AnAnacreditParameter_Reserved38` | TField |  |  |
| 41 | `AN.CR.PAR.RESERVED.37` | `AnAnacreditParameter_Reserved37` | TField |  |  |
| 42 | `AN.CR.PAR.RESERVED.36` | `AnAnacreditParameter_Reserved36` | TField |  |  |
| 43 | `AN.CR.PAR.RESERVED.35` | `AnAnacreditParameter_Reserved35` | TField |  |  |
| 44 | `AN.CR.PAR.RESERVED.34` | `AnAnacreditParameter_Reserved34` | TField |  |  |
| 45 | `AN.CR.PAR.RESERVED.33` | `AnAnacreditParameter_Reserved33` | TField |  |  |
| 46 | `AN.CR.PAR.RESERVED.32` | `AnAnacreditParameter_Reserved32` | TField |  |  |
| 47 | `AN.CR.PAR.RESERVED.31` | `AnAnacreditParameter_Reserved31` | TField |  |  |
| 48 | `AN.CR.PAR.RESERVED.30` | `AnAnacreditParameter_Reserved30` | TField |  |  |
| 49 | `AN.CR.PAR.RESERVED.29` | `AnAnacreditParameter_Reserved29` | TField |  |  |
| 50 | `AN.CR.PAR.RESERVED.28` | `AnAnacreditParameter_Reserved28` | TField |  |  |
| 51 | `AN.CR.PAR.RESERVED.27` | `AnAnacreditParameter_Reserved27` | TField |  |  |
| 52 | `AN.CR.PAR.RESERVED.26` | `AnAnacreditParameter_Reserved26` | TField |  |  |
| 53 | `AN.CR.PAR.RESERVED.25` | `AnAnacreditParameter_Reserved25` | TField |  |  |
| 54 | `AN.CR.PAR.RESERVED.24` | `AnAnacreditParameter_Reserved24` | TField |  |  |
| 55 | `AN.CR.PAR.RESERVED.23` | `AnAnacreditParameter_Reserved23` | TField |  |  |
| 56 | `AN.CR.PAR.RESERVED.22` | `AnAnacreditParameter_Reserved22` | TField |  |  |
| 57 | `AN.CR.PAR.RESERVED.21` | `AnAnacreditParameter_Reserved21` | TField |  |  |
| 58 | `AN.CR.PAR.RESERVED.20` | `AnAnacreditParameter_Reserved20` | TField |  |  |
| 59 | `AN.CR.PAR.RESERVED.19` | `AnAnacreditParameter_Reserved19` | TField |  |  |
| 60 | `AN.CR.PAR.RESERVED.18` | `AnAnacreditParameter_Reserved18` | TField |  |  |
| 61 | `AN.CR.PAR.RESERVED.17` | `AnAnacreditParameter_Reserved17` | TField |  |  |
| 62 | `AN.CR.PAR.RESERVED.16` | `AnAnacreditParameter_Reserved16` | TField |  |  |
| 63 | `AN.CR.PAR.RESERVED.15` | `AnAnacreditParameter_Reserved15` | TField |  |  |
| 64 | `AN.CR.PAR.RESERVED.14` | `AnAnacreditParameter_Reserved14` | TField |  |  |
| 65 | `AN.CR.PAR.RESERVED.13` | `AnAnacreditParameter_Reserved13` | TField |  |  |
| 66 | `AN.CR.PAR.RESERVED.12` | `AnAnacreditParameter_Reserved12` | TField |  |  |
| 67 | `AN.CR.PAR.RESERVED.11` | `AnAnacreditParameter_Reserved11` | TField |  |  |
| 68 | `AN.CR.PAR.RESERVED.10` | `AnAnacreditParameter_Reserved10` | TField |  |  |
| 69 | `AN.CR.PAR.RESERVED.09` | `AnAnacreditParameter_Reserved09` | TField |  |  |
| 70 | `AN.CR.PAR.RESERVED.08` | `AnAnacreditParameter_Reserved08` | TField |  |  |
| 71 | `AN.CR.PAR.RESERVED.07` | `AnAnacreditParameter_Reserved07` | TField |  |  |
| 72 | `AN.CR.PAR.RESERVED.06` | `AnAnacreditParameter_Reserved06` | TField |  |  |
| 73 | `AN.CR.PAR.RESERVED.05` | `AnAnacreditParameter_Reserved05` | TField |  |  |
| 74 | `AN.CR.PAR.RESERVED.04` | `AnAnacreditParameter_Reserved04` | TField |  |  |
| 75 | `AN.CR.PAR.RESERVED.03` | `AnAnacreditParameter_Reserved03` | TField |  |  |
| 76 | `AN.CR.PAR.RESERVED.02` | `AnAnacreditParameter_Reserved02` | TField |  |  |
| 77 | `AN.CR.PAR.RESERVED.01` | `AnAnacreditParameter_Reserved01` | TField |  |  |
| 78 | `AN.CR.PAR.LOCAL.REF` | `AnAnacreditParameter_LocalRef` |  |  |  |
| 79 | `AN.CR.PAR.OVERRIDE` | `AnAnacreditParameter_Override` |  |  |  |
| 80 | `AN.CR.PAR.RECORD.STATUS` | `AnAnacreditParameter_RecordStatus` | String |  |  |
| 81 | `AN.CR.PAR.CURR.NO` | `AnAnacreditParameter_CurrNo` | String |  |  |
| 82 | `AN.CR.PAR.INPUTTER` | `AnAnacreditParameter_Inputter` |  |  |  |
| 83 | `AN.CR.PAR.DATE.TIME` | `AnAnacreditParameter_DateTime` |  |  |  |
| 84 | `AN.CR.PAR.AUTHORISER` | `AnAnacreditParameter_Authoriser` | String |  |  |
| 85 | `AN.CR.PAR.CO.CODE` | `AnAnacreditParameter_CoCode` | String |  |  |
| 86 | `AN.CR.PAR.DEPT.CODE` | `AnAnacreditParameter_DeptCode` | String |  |  |
| 87 | `AN.CR.PAR.AUDITOR.CODE` | `AnAnacreditParameter_AuditorCode` | String |  |  |
| 88 | `AN.CR.PAR.AUDIT.DATE.TIME` | `AnAnacreditParameter_AuditDateTime` | String |  |  |
