# SC.POST.EVENT.ADJUST — Table Schema

> Source: `INSERTS/I_F.SC.POST.EVENT.ADJUST` in `SC_ScoSecurityPositionUpdate.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.EVADJ.SECURITY.NO` | `ScPostEventAdjust_SecurityNo` | TField |  | Event Security of an Event . Defaulted with SECURITY.NO from DIARY |
| 2 | `SC.EVADJ.OLD.MKT.PRC` | `ScPostEventAdjust_OldMktPrc` | TField |  | Market Price of Event Security can be mentioned here. Defaulted with OLD.MKT.PRC from DIARY |
| 3 | `SC.EVADJ.NARRATIVE` | `ScPostEventAdjust_Narrative` |  |  |  |
| 4 | `SC.EVADJ.EVENT.TYPE` | `ScPostEventAdjust_EventType` | TField |  | Event Type of Event can be mentioned here. Defaulted with EVENT.TYPE from DIARY Validation Rules : NOINPUT Field |
| 5 | `SC.EVADJ.EX.DATE` | `ScPostEventAdjust_ExDate` | TField |  | Ex Date of Event can be mentioned here. Defaulted with EX.DATE from DIARY Validation Rules : NOINPUT Field |
| 6 | `SC.EVADJ.PAY.DATE` | `ScPostEventAdjust_PayDate` | TField |  | Pay Date of Event can be mentioned here. Defaulted with PAY.DATE from DIARY Validation Rules : NOINPUT Field |
| 7 | `SC.EVADJ.VALUE.DATE` | `ScPostEventAdjust_ValueDate` | TField |  | Value Date of Event can be mentioned here. Defaulted with VALUE.DATE from DIARY Validation Rules : NOINPUT Field |
| 8 | `SC.EVADJ.OPTION.DESC` | `ScPostEventAdjust_OptionDesc` |  |  |  |
| 9 | `SC.EVADJ.NEW.SEC.NO` | `ScPostEventAdjust_NewSecNo` |  |  |  |
| 10 | `SC.EVADJ.NEW.MKT.PRC` | `ScPostEventAdjust_NewMktPrc` |  |  |  |
| 11 | `SC.EVADJ.BOOK.COST` | `ScPostEventAdjust_BookCost` |  |  |  |
| 12 | `SC.EVADJ.ADD.ON.SEC` | `ScPostEventAdjust_AddOnSec` |  |  |  |
| 13 | `SC.EVADJ.NEW.SEC.CAP.RET` | `ScPostEventAdjust_NewSecCapRet` |  |  |  |
| 14 | `SC.EVADJ.NEW.SEC.INCOME` | `ScPostEventAdjust_NewSecIncome` |  |  |  |
| 15 | `SC.EVADJ.BOOK.COST.PERC` | `ScPostEventAdjust_BookCostPerc` |  |  |  |
| 16 | `SC.EVADJ.BUYBCK.PRICE` | `ScPostEventAdjust_BuybckPrice` | TField |  | This field will hold the final buyback price |
| 17 | `SC.EVADJ.BUYBCK.INC` | `ScPostEventAdjust_BuybckInc` | TField |  | Field to store income component in a Buy Back event. This field will be used to compute the proceeds that needs to be treated as income. |
| 18 | `SC.EVADJ.BUYBCK.TAX` | `ScPostEventAdjust_BuybckTax` | TField |  | Field to store the tax value of the buyback security. |
| 19 | `SC.EVADJ.CAPITAL.PROCEEDS` | `ScPostEventAdjust_CapitalProceeds` | TField |  | Capital Proceeds per unit for Off Market Buy Back is stored here |
| 20 | `SC.EVADJ.CG.TAX.ACQ.DATE` | `ScPostEventAdjust_CgTaxAcqDate` | TField |  | Field to store Acquisition Date of Lots created for Capital Gains |
| 21 | `SC.EVADJ.CG.TAX.DISP.DATE` | `ScPostEventAdjust_CgTaxDispDate` | TField |  | Field to store Disposal Date of Lots created for Capital Gains |
| 22 | `SC.EVADJ.CG.TAX.EFF.DATE` | `ScPostEventAdjust_CgTaxEffDate` | TField |  | Field to store Effective Date of Lots created for Capital Gains |
| 23 | `SC.EVADJ.CG.GROUP` | `ScPostEventAdjust_CgGroup` |  |  |  |
| 24 | `SC.EVADJ.CG.ROLLOVER` | `ScPostEventAdjust_CgRollover` |  |  |  |
| 25 | `SC.EVADJ.CG.ROLL.PRE.CGT` | `ScPostEventAdjust_CgRollPreCgt` |  |  |  |
| 26 | `SC.EVADJ.CG.ROLL.PRE.CGT.DATE` | `ScPostEventAdjust_CgRollPreCgtDate` |  |  |  |
| 27 | `SC.EVADJ.CG.NOT.CAP.RETURN` | `ScPostEventAdjust_CgNotCapReturn` |  |  |  |
| 28 | `SC.EVADJ.CG.DIVIDEND` | `ScPostEventAdjust_CgDividend` |  |  |  |
| 29 | `SC.EVADJ.CG.CA.RULES` | `ScPostEventAdjust_CgCaRules` | TField |  | Field can be used to link to a record from CG.CA.RULES to define methods to update CG.TXN.BASE . |
| 30 | `SC.EVADJ.CG.ANTI.OVERLAP` | `ScPostEventAdjust_CgAntiOverlap` | TField |  | Field to determine calculation of Capital Gains for units sold between ex date and effective date in a Capital return event If set to Yes - Capital Gains are calculated based on Capital Return Amount. If Blank - Capital Gains are calculated based on Cash paid out during Capital Return. |
| 31 | `SC.EVADJ.STATUS` | `ScPostEventAdjust_Status` | TField |  | Informatory field to identify the type of update to this record. Allowed Options : INITIAL , FINAL |
| 32 | `SC.EVADJ.SERVICE.STATUS` | `ScPostEventAdjust_ServiceStatus` | TField |  | Field is to identify processing of this record by service : CG.COST.ADJUSTMENT . Update to this field is as below: ACTIVATED - Record is ready to be picked by service : CG.COST.ADJUSTMENT PROCESSING - Record is picked by service : CG.COST.ADJUSTMENT and is being processed. PROCESSED - Record is processed by service : CG.COST.ADJUSTMENT Validation Rules : Validation Rules : NOINPUT Field Field |
| 33 | `SC.EVADJ.CG.TIME.CR` | `ScPostEventAdjust_CgTimeCr` | TField |  | CG.TRD.TIME.CR mapped from Diary. |
| 34 | `SC.EVADJ.CG.TIME.DR` | `ScPostEventAdjust_CgTimeDr` | TField |  | CG.TRD.TIME.DR mapped from Diary. |
| 35 | `SC.EVADJ.RESERVED.13` | `ScPostEventAdjust_Reserved13` | TField |  |  |
| 36 | `SC.EVADJ.RESERVED.12` | `ScPostEventAdjust_Reserved12` | TField |  |  |
| 37 | `SC.EVADJ.RESERVED.11` | `ScPostEventAdjust_Reserved11` | TField |  |  |
| 38 | `SC.EVADJ.RESERVED.10` | `ScPostEventAdjust_Reserved10` | TField |  |  |
| 39 | `SC.EVADJ.RESERVED.09` | `ScPostEventAdjust_Reserved09` | TField |  |  |
| 40 | `SC.EVADJ.RESERVED.08` | `ScPostEventAdjust_Reserved08` | TField |  |  |
| 41 | `SC.EVADJ.RESERVED.07` | `ScPostEventAdjust_Reserved07` | TField |  |  |
| 42 | `SC.EVADJ.RESERVED.06` | `ScPostEventAdjust_Reserved06` | TField |  |  |
| 43 | `SC.EVADJ.RESERVED.05` | `ScPostEventAdjust_Reserved05` | TField |  |  |
| 44 | `SC.EVADJ.RESERVED.04` | `ScPostEventAdjust_Reserved04` | TField |  |  |
| 45 | `SC.EVADJ.RESERVED.03` | `ScPostEventAdjust_Reserved03` | TField |  |  |
| 46 | `SC.EVADJ.RESERVED.02` | `ScPostEventAdjust_Reserved02` | TField |  |  |
| 47 | `SC.EVADJ.RESERVED.01` | `ScPostEventAdjust_Reserved01` | TField |  |  |
| 48 | `SC.EVADJ.LOCAL.REF` | `ScPostEventAdjust_LocalRef` |  |  |  |
| 49 | `SC.EVADJ.OVERRIDE` | `ScPostEventAdjust_Override` |  |  |  |
| 50 | `SC.EVADJ.RECORD.STATUS` | `ScPostEventAdjust_RecordStatus` | String |  |  |
| 51 | `SC.EVADJ.CURR.NO` | `ScPostEventAdjust_CurrNo` | String |  |  |
| 52 | `SC.EVADJ.INPUTTER` | `ScPostEventAdjust_Inputter` |  |  |  |
| 53 | `SC.EVADJ.DATE.TIME` | `ScPostEventAdjust_DateTime` |  |  |  |
| 54 | `SC.EVADJ.AUTHORISER` | `ScPostEventAdjust_Authoriser` | String |  |  |
| 55 | `SC.EVADJ.CO.CODE` | `ScPostEventAdjust_CoCode` | String |  |  |
| 56 | `SC.EVADJ.DEPT.CODE` | `ScPostEventAdjust_DeptCode` | String |  |  |
| 57 | `SC.EVADJ.AUDITOR.CODE` | `ScPostEventAdjust_AuditorCode` | String |  |  |
| 58 | `SC.EVADJ.AUDIT.DATE.TIME` | `ScPostEventAdjust_AuditDateTime` | String |  |  |
| 59 | `SC.EVADJ.RATE` | `ScPostEventAdjust_Rate` |  |  |  |
