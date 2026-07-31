# LBRPTS.COLLECTION.SUMMON — Table Schema

> Source: `INSERTS/I_F.LBRPTS.COLLECTION.SUMMON` in `LBRPTS_HonoraryCalculation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CO.SU.CUS.NAME` | `LbrptsCollectionSummons_CusName` | TField |  |  |
| 2 | `CO.SU.SUMMON.ADDRESS` | `LbrptsCollectionSummons_SummonAddress` | TField |  |  |
| 3 | `CO.SU.ACCT.OFFICER` | `LbrptsCollectionSummons_AcctOfficer` | TField |  |  |
| 4 | `CO.SU.CUST.GUARANTOR` | `LbrptsCollectionSummons_CustGuarantor` | TField |  |  |
| 5 | `CO.SU.MAIN.CUST.ID` | `LbrptsCollectionSummons_MainCustId` | TField |  |  |
| 6 | `CO.SU.SUMMON.SENT.DATE` | `LbrptsCollectionSummons_SummonSentDate` |  |  |  |
| 7 | `CO.SU.SUMMON.RECEIVED` | `LbrptsCollectionSummons_SummonReceived` |  |  |  |
| 8 | `CO.SU.REASON.SUMMON.NR` | `LbrptsCollectionSummons_ReasonSummonNr` |  |  |  |
| 9 | `CO.SU.SUMMON.RCV.DATE` | `LbrptsCollectionSummons_SummonRcvDate` |  |  |  |
| 10 | `CO.SU.NEXT.SUMMON.DATE` | `LbrptsCollectionSummons_NextSummonDate` | TField |  |  |
| 11 | `CO.SU.RESERVED.10` | `LbrptsCollectionSummons_Reserved10` | TField |  |  |
| 12 | `CO.SU.RESERVED.9` | `LbrptsCollectionSummons_Reserved9` | TField |  |  |
| 13 | `CO.SU.RESERVED.8` | `LbrptsCollectionSummons_Reserved8` | TField |  |  |
| 14 | `CO.SU.RESERVED.7` | `LbrptsCollectionSummons_Reserved7` | TField |  |  |
| 15 | `CO.SU.RESERVED.6` | `LbrptsCollectionSummons_Reserved6` | TField |  |  |
| 16 | `CO.SU.RESERVED.5` | `LbrptsCollectionSummons_Reserved5` | TField |  |  |
| 17 | `CO.SU.RESERVED.4` | `LbrptsCollectionSummons_Reserved4` | TField |  |  |
| 18 | `CO.SU.RESERVED.3` | `LbrptsCollectionSummons_Reserved3` | TField |  |  |
| 19 | `CO.SU.RESERVED.2` | `LbrptsCollectionSummons_Reserved2` | TField |  |  |
| 20 | `CO.SU.RESERVED.1` | `LbrptsCollectionSummons_Reserved1` | TField |  |  |
| 21 | `CO.SU.LOCAL.REF` | `LbrptsCollectionSummons_LocalRef` |  |  |  |
| 22 | `CO.SU.OVERRIDE` | `LbrptsCollectionSummons_Override` |  |  |  |
| 23 | `CO.SU.RECORD.STATUS` | `LbrptsCollectionSummons_RecordStatus` | String |  |  |
| 24 | `CO.SU.CURR.NO` | `LbrptsCollectionSummons_CurrNo` | String |  |  |
| 25 | `CO.SU.INPUTTER` | `LbrptsCollectionSummons_Inputter` |  |  |  |
| 26 | `CO.SU.DATE.TIME` | `LbrptsCollectionSummons_DateTime` |  |  |  |
| 27 | `CO.SU.AUTHORISER` | `LbrptsCollectionSummons_Authoriser` | String |  |  |
| 28 | `CO.SU.CO.CODE` | `LbrptsCollectionSummons_CoCode` | String |  |  |
| 29 | `CO.SU.DEPT.CODE` | `LbrptsCollectionSummons_DeptCode` | String |  |  |
| 30 | `CO.SU.AUDITOR.CODE` | `LbrptsCollectionSummons_AuditorCode` | String |  |  |
| 31 | `CO.SU.AUDIT.DATE.TIME` | `LbrptsCollectionSummons_AuditDateTime` | String |  |  |
