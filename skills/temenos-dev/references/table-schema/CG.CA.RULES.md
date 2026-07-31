# CG.CA.RULES — Table Schema

> Source: `INSERTS/I_F.CG.CA.RULES` in `SC_SctCapitalGains.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CA.RUL.DESCRIPTION` | `CgCaRules_Description` |  |  |  |
| 2 | `CA.RUL.EVENT.DATE` | `CgCaRules_EventDate` | TField |  | Value defined here is used to update trade date and time for the lot , if LOT.DATE is opted as EVENT.DATE . Allowed options are PAY.DATE , VALUE.DATE , EX.DATE , RECORD.DATE. |
| 3 | `CA.RUL.INCOME.EVENT` | `CgCaRules_IncomeEvent` | TField |  | Flag indication if corporate action event is to be treated as an income event.If set , Entitlement amount fromcorporate action is updated in CG.TXN.BASE as income. |
| 4 | `CA.RUL.UPD.COST` | `CgCaRules_UpdCost` | TField |  | Flag indication if corporate action event impacts cost of the event security.If set ,cost changed isreduced/increased to original lots proportionately. |
| 5 | `CA.RUL.UPD.LOT.ES` | `CgCaRules_UpdLotEs` | TField |  | Flag indication to update credit movements for corporate action event if Security for the movement is same asunderlying or event security. |
| 6 | `CA.RUL.ES.LOT.DATE` | `CgCaRules_EsLotDate` | TField |  | Option to choose trade date time for new nominal that is updated to CG.TXN.BASE Allowed options : ORIG.DATE - Nominal for this transaction movement is updated to original lots with trade date time as originalacquisition date. EVENT.DATE - Nominal for this transaction is identified as a separate lot , with trade date time as defined inEVENT.DATE |
| 7 | `CA.RUL.ES.LOT.COST` | `CgCaRules_EsLotCost` | TField |  | Option to choose cost for new nominal that is updated to CG.TXN.BASE Allowed options : DIVIDEND - Dividend value from the entitlement is updated as cost for the movement. ZERO - Cost for new nominals is considered as zero. GROSS.COST - Cost calculated in SECURITY.TRANS is updated for new nominals. PRORATA - A New Lot is created with new nominal and Cost will be demerged between New Lot and existing Lot. |
| 8 | `CA.RUL.UPD.LOT.NS` | `CgCaRules_UpdLotNs` | TField |  | Flag indication to update credit movements for corporate action event if Security for the movement is differentfrom underlying or event security. |
| 9 | `CA.RUL.NS.LOT.DATE` | `CgCaRules_NsLotDate` | TField |  | Option to choose trade date time for new nominal that is updated to CG.TXN.BASE Allowed options : ORIG.DATE - Nominal for this transaction movement is updated to original lots with trade date time as originalacquisition date. EVENT.DATE - Nominal for this transaction is identified as a separate lot , with trade date time as defined inEVENT.DATE |
| 10 | `CA.RUL.NS.LOT.COST` | `CgCaRules_NsLotCost` | TField |  | Option to choose cost for new nominal that is updated to CG.TXN.BASE Allowed options : DIVIDEND - Dividend value from the entitlement is updated as cost for the movement. ZERO - Cost for new nominals is considered as zero. GROSS.COST - Cost calculated in SECURITY.TRANS is updated for new nominals. DEMERGE.COST - Cost from event security is demerged to new nominals for each lot in event security. MKT.PRC - Cost for new nominal is updated as market value of new nominals . |
| 11 | `CA.RUL.CALC.CG` | `CgCaRules_CalcCg` | TField |  | Indicates if Capital Gains should be calculated or not for a debit movement. |
| 12 | `CA.RUL.CG.ROLLOVER` | `CgCaRules_CgRollover` |  |  |  |
| 13 | `CA.RUL.UPD.NET.NOM` | `CgCaRules_UpdNetNom` | TField |  | Indicates if sum of debit and credit quantity is updated to original lots. |
| 14 | `CA.RUL.REDUCE.CASH` | `CgCaRules_ReduceCash` | TField |  | Flag to denote if Cash received from Entitlement should be reduced proportionately in original lots beforeapplying Cost methods. |
| 15 | `CA.RUL.INSTRUMENT.TYPE` | `CgCaRules_InstrumentType` |  |  |  |
| 16 | `CA.RUL.CA.TAX.ACQ.DATE` | `CgCaRules_CaTaxAcqDate` |  |  |  |
| 17 | `CA.RUL.CA.TAX.DISP.DATE` | `CgCaRules_CaTaxDispDate` |  |  |  |
| 18 | `CA.RUL.RESERVED.25` | `CgCaRules_Reserved25` | TField |  |  |
| 19 | `CA.RUL.RESERVED.24` | `CgCaRules_Reserved24` | TField |  |  |
| 20 | `CA.RUL.RESERVED.23` | `CgCaRules_Reserved23` | TField |  |  |
| 21 | `CA.RUL.RESERVED.22` | `CgCaRules_Reserved22` | TField |  |  |
| 22 | `CA.RUL.RESERVED.21` | `CgCaRules_Reserved21` | TField |  |  |
| 23 | `CA.RUL.RESERVED.20` | `CgCaRules_Reserved20` | TField |  |  |
| 24 | `CA.RUL.RESERVED.19` | `CgCaRules_Reserved19` | TField |  |  |
| 25 | `CA.RUL.RESERVED.18` | `CgCaRules_Reserved18` | TField |  |  |
| 26 | `CA.RUL.RESERVED.17` | `CgCaRules_Reserved17` | TField |  |  |
| 27 | `CA.RUL.RESERVED.16` | `CgCaRules_Reserved16` | TField |  |  |
| 28 | `CA.RUL.RESERVED.15` | `CgCaRules_Reserved15` | TField |  |  |
| 29 | `CA.RUL.RESERVED.14` | `CgCaRules_Reserved14` | TField |  |  |
| 30 | `CA.RUL.RESERVED.13` | `CgCaRules_Reserved13` | TField |  |  |
| 31 | `CA.RUL.RESERVED.12` | `CgCaRules_Reserved12` | TField |  |  |
| 32 | `CA.RUL.RESERVED.11` | `CgCaRules_Reserved11` | TField |  |  |
| 33 | `CA.RUL.RESERVED.10` | `CgCaRules_Reserved10` | TField |  |  |
| 34 | `CA.RUL.RESERVED.09` | `CgCaRules_Reserved09` | TField |  |  |
| 35 | `CA.RUL.RESERVED.08` | `CgCaRules_Reserved08` | TField |  |  |
| 36 | `CA.RUL.RESERVED.07` | `CgCaRules_Reserved07` | TField |  |  |
| 37 | `CA.RUL.RESERVED.06` | `CgCaRules_Reserved06` | TField |  |  |
| 38 | `CA.RUL.RESERVED.05` | `CgCaRules_Reserved05` | TField |  |  |
| 39 | `CA.RUL.RESERVED.04` | `CgCaRules_Reserved04` | TField |  |  |
| 40 | `CA.RUL.RESERVED.03` | `CgCaRules_Reserved03` | TField |  |  |
| 41 | `CA.RUL.RESERVED.02` | `CgCaRules_Reserved02` | TField |  |  |
| 42 | `CA.RUL.RESERVED.01` | `CgCaRules_Reserved01` | TField |  |  |
| 43 | `CA.RUL.LOCAL.REF` | `CgCaRules_LocalRef` |  |  |  |
| 44 | `CA.RUL.OVERRIDE` | `CgCaRules_Override` |  |  |  |
| 45 | `CA.RUL.RECORD.STATUS` | `CgCaRules_RecordStatus` | String |  |  |
| 46 | `CA.RUL.CURR.NO` | `CgCaRules_CurrNo` | String |  |  |
| 47 | `CA.RUL.INPUTTER` | `CgCaRules_Inputter` |  |  |  |
| 48 | `CA.RUL.DATE.TIME` | `CgCaRules_DateTime` |  |  |  |
| 49 | `CA.RUL.AUTHORISER` | `CgCaRules_Authoriser` | String |  |  |
| 50 | `CA.RUL.CO.CODE` | `CgCaRules_CoCode` | String |  |  |
| 51 | `CA.RUL.DEPT.CODE` | `CgCaRules_DeptCode` | String |  |  |
| 52 | `CA.RUL.AUDITOR.CODE` | `CgCaRules_AuditorCode` | String |  |  |
| 53 | `CA.RUL.AUDIT.DATE.TIME` | `CgCaRules_AuditDateTime` | String |  |  |
| 54 | `CA.RUL.CG.GROUP` | `CgCaRules_CgGroup` |  |  |  |
| 55 | `CA.RUL.CG.ROLL.PRE.CGT` | `CgCaRules_CgRollPreCgt` |  |  |  |
| 56 | `CA.RUL.CG.ROLL.PRE.CGT.DATE` | `CgCaRules_CgRollPreCgtDate` |  |  |  |
| 57 | `CA.RUL.CG.NOT.CAP.RETURN` | `CgCaRules_CgNotCapReturn` |  |  |  |
| 58 | `CA.RUL.CG.DIVIDEND` | `CgCaRules_CgDividend` |  |  |  |
