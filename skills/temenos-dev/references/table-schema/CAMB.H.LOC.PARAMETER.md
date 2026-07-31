# CAMB.H.LOC.PARAMETER — Table Schema

> Source: `INSERTS/I_F.CAMB.H.LOC.PARAMETER` in `CALOCR_LineOfCredit.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LOCP.LIMIT.REFERENCE` | `CambHLocParameter_LimitReference` |  |  |  |
| 2 | `LOCP.ACC.UPD.ACTIVITY` | `CambHLocParameter_AccUpdActivity` | TField |  | This field is used to define a valid AA.ACTIVITY for ACCOUNTS product line, using which the PAST.DUE.STATUS of LOC account will be updated.A valid AA.ACTIVITY Id that will be used to update the Account condition in the Demand Arrangement for LOC Past Due Status. |
| 3 | `LOCP.ACC.CLOSE.ACTIVITY` | `CambHLocParameter_AccCloseActivity` |  |  |  |
| 4 | `LOCP.ACC.BAL.PROPERTY` | `CambHLocParameter_AccBalProperty` | TField |  | This field is used to define the Balance type to be considered for fetching the LOC account balance.A valid AA.PROPERTY Id that is used to indicate Demand/LOC Account Property. |
| 5 | `LOCP.AC.DR.INT.PROPERTY` | `CambHLocParameter_AcDrIntProperty` | TField |  | This field is used to defined the DEBIT INTEREST PROPERTY name for calculating Due balances of LOC account.A valid AA.PROPERTY Id that is used to indicate Demand Account's Debit Interest Property. |
| 6 | `LOCP.PAST.DUE.STATUS` | `CambHLocParameter_PastDueStatus` |  |  |  |
| 7 | `LOCP.NUMBER.OF.DAYS` | `CambHLocParameter_NumberOfDays` |  |  |  |
| 8 | `LOCP.OFS.SOURCE.ID` | `CambHLocParameter_OfsSourceId` | TField |  | Field to define the OFS Source id, which will be used by System to update the LOC status using OFS.Validation: Valid OFS.SOURCE record |
| 9 | `LOCP.ACC.ACT.VERSION` | `CambHLocParameter_AccActVersion` | TField |  | Field to define the AAA Version, which will be used by System to update the LOC status using OFS.Validation: Valid Version record |
| 10 | `LOCP.LOC.DELINQUENT.STATUS` | `CambHLocParameter_LocDelinquentStatus` |  |  |  |
| 11 | `LOCP.LOC.DELIQUENT.DAYS` | `CambHLocParameter_LocDeliquentDays` |  |  |  |
| 12 | `LOCP.OD.DELIQUENT.DAYS` | `CambHLocParameter_OdDeliquentDays` | TField |  | This field is used to define the no of days after overdrawing the Account, which is to be flagged as delinquent if the account is overdrawn and no deposit is made. |
| 13 | `LOCP.OD.DEFAULT.PAY.PERIOD` | `CambHLocParameter_OdDefaultPayPeriod` | TField |  |  |
| 14 | `LOCP.REPAY.TOLER.PERCENT` | `CambHLocParameter_RepayTolerPercent` | TField |  |  |
| 15 | `LOCP.REPAY.TOLER.CCY` | `CambHLocParameter_RepayTolerCcy` |  |  |  |
| 16 | `LOCP.REPAY.TOLER.AMT` | `CambHLocParameter_RepayTolerAmt` |  |  |  |
| 17 | `LOCP.ARC.LOC.BAL.CNT` | `CambHLocParameter_ArcLocBalCnt` | TField |  |  |
| 18 | `LOCP.REST.ACTIVITIES` | `CambHLocParameter_RestActivities` |  |  |  |
| 19 | `LOCP.WR.OFF.TXN.CODE` | `CambHLocParameter_WrOffTxnCode` |  |  |  |
| 20 | `LOCP.MAX.VAL.RETAIN` | `CambHLocParameter_MaxValRetain` | TField |  | The purpose of this field is used to define the max number of transaction to be displayed in CAMB.L.LOC.BAL.DETAILS, remaining will be stored to CAMB.L.LOC.BAL.DETAILS.HIST table.Allowed values are 2 numeric character.Ex. 15, 5, 10 etc. |
| 21 | `LOCP.AUTO.CLOSE.ACTVITY` | `CambHLocParameter_AutoCloseActvity` | TField |  | The purpose of this field is to define the activity to be considered to trigger LOCClosure Process.Valid record from AA.ACTIVITY table.Ex. AR.LOC.CLOSURENote: If the Performing activity matches with the activity defined in this field, System triggers the Automatic LOC Closure Activities. Automatic LOC Closure Activities are defined inAUTO.LOC.PARAMETER table. |
| 22 | `LOCP.MIN.PAY.AMT` | `CambHLocParameter_MinPayAmt` | TField |  |  |
| 23 | `LOCP.ACCT.TITLE` | `CambHLocParameter_AcctTitle` | TField |  | Field to define valid field name from ACCOUNT application.The field name defined here is used for showing Account title in enquiry display |
| 24 | `LOCP.RECORD.STATUS` | `CambHLocParameter_RecordStatus` | String |  |  |
| 25 | `LOCP.CURR.NO` | `CambHLocParameter_CurrNo` | String |  |  |
| 26 | `LOCP.INPUTTER` | `CambHLocParameter_Inputter` |  |  |  |
| 27 | `LOCP.DATE.TIME` | `CambHLocParameter_DateTime` |  |  |  |
| 28 | `LOCP.AUTHORISER` | `CambHLocParameter_Authoriser` | String |  |  |
| 29 | `LOCP.CO.CODE` | `CambHLocParameter_CoCode` | String |  |  |
| 30 | `LOCP.DEPT.CODE` | `CambHLocParameter_DeptCode` | String |  |  |
| 31 | `LOCP.AUDITOR.CODE` | `CambHLocParameter_AuditorCode` | String |  |  |
| 32 | `LOCP.AUDIT.DATE.TIME` | `CambHLocParameter_AuditDateTime` | String |  |  |
