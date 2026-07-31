# CAPL.TX.FT4SDRIF.SLIPS — Table Schema

> Source: `INSERTS/I_F.CAPL.TX.FT4SDRIF.SLIPS` in `CADEPO_CRAReporting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `T4SDRIF.ID.1` | `CaplTxFt4sdrifSlips_Id1` | TField |  |  |
| 2 | `T4SDRIF.SLIP.YEAR` | `CaplTxFt4sdrifSlips_SlipYear` | TField |  |  |
| 3 | `T4SDRIF.SLIP.NUMBER` | `CaplTxFt4sdrifSlips_SlipNumber` | TField |  |  |
| 4 | `T4SDRIF.SLIP.SEQ.NO` | `CaplTxFt4sdrifSlips_SlipSeqNo` | TField |  |  |
| 5 | `T4SDRIF.CUSTOMER.1` | `CaplTxFt4sdrifSlips_Customer1` | TField |  |  |
| 6 | `T4SDRIF.CUSTOMER.2` | `CaplTxFt4sdrifSlips_Customer2` | TField |  |  |
| 7 | `T4SDRIF.COMPANY` | `CaplTxFt4sdrifSlips_Company` | TField |  |  |
| 8 | `T4SDRIF.SLIP.PROCESS` | `CaplTxFt4sdrifSlips_SlipProcess` | TField |  |  |
| 9 | `T4SDRIF.SLIP.AMENDED` | `CaplTxFt4sdrifSlips_SlipAmended` | TField |  |  |
| 10 | `T4SDRIF.AMEND.SEQ.NO` | `CaplTxFt4sdrifSlips_AmendSeqNo` | TField |  |  |
| 11 | `T4SDRIF.SLIP.DATE` | `CaplTxFt4sdrifSlips_SlipDate` | TField |  |  |
| 12 | `T4SDRIF.SLIP.USER` | `CaplTxFt4sdrifSlips_SlipUser` | TField |  |  |
| 13 | `T4SDRIF.BOX.16` | `CaplTxFt4sdrifSlips_Box16` | TField |  |  |
| 14 | `T4SDRIF.BOX.18` | `CaplTxFt4sdrifSlips_Box18` | TField |  |  |
| 15 | `T4SDRIF.BOX.24` | `CaplTxFt4sdrifSlips_Box24` | TField |  |  |
| 16 | `T4SDRIF.BOX.28` | `CaplTxFt4sdrifSlips_Box28` | TField |  |  |
| 17 | `T4SDRIF.BOX.35` | `CaplTxFt4sdrifSlips_Box35` | TField |  |  |
| 18 | `T4SDRIF.BOX.22` | `CaplTxFt4sdrifSlips_Box22` | TField |  |  |
| 19 | `T4SDRIF.BOX.30` | `CaplTxFt4sdrifSlips_Box30` | TField |  |  |
| 20 | `T4SDRIF.YEAR` | `CaplTxFt4sdrifSlips_Year` | TField |  |  |
| 21 | `T4SDRIF.BOX.26` | `CaplTxFt4sdrifSlips_Box26` | TField |  |  |
| 22 | `T4SDRIF.BOX.12` | `CaplTxFt4sdrifSlips_Box12` | TField |  |  |
| 23 | `T4SDRIF.BOX.32` | `CaplTxFt4sdrifSlips_Box32` | TField |  |  |
| 24 | `T4SDRIF.BOX.14` | `CaplTxFt4sdrifSlips_Box14` | TField |  |  |
| 25 | `T4SDRIF.BOX.60` | `CaplTxFt4sdrifSlips_Box60` | TField |  |  |
| 26 | `T4SDRIF.BOX.61` | `CaplTxFt4sdrifSlips_Box61` | TField |  |  |
| 27 | `T4SDRIF.BEN.NAME.1` | `CaplTxFt4sdrifSlips_BenName1` | TField |  |  |
| 28 | `T4SDRIF.BEN.ADR.1` | `CaplTxFt4sdrifSlips_BenAdr1` | TField |  |  |
| 29 | `T4SDRIF.BEN.ADR.2` | `CaplTxFt4sdrifSlips_BenAdr2` | TField |  |  |
| 30 | `T4SDRIF.BEN.ADR.3` | `CaplTxFt4sdrifSlips_BenAdr3` | TField |  |  |
| 31 | `T4SDRIF.BEN.ADR.4` | `CaplTxFt4sdrifSlips_BenAdr4` | TField |  |  |
| 32 | `T4SDRIF.BEN.ADR.5` | `CaplTxFt4sdrifSlips_BenAdr5` | TField |  |  |
| 33 | `T4SDRIF.BEN.ADR.6` | `CaplTxFt4sdrifSlips_BenAdr6` | TField |  |  |
| 34 | `T4SDRIF.BEN.ADR.7` | `CaplTxFt4sdrifSlips_BenAdr7` | TField |  |  |
| 35 | `T4SDRIF.BEN.ADR.8` | `CaplTxFt4sdrifSlips_BenAdr8` | TField |  |  |
| 36 | `T4SDRIF.BEN.ADR.9` | `CaplTxFt4sdrifSlips_BenAdr9` | TField |  |  |
| 37 | `T4SDRIF.PRINT.STATUS` | `CaplTxFt4sdrifSlips_PrintStatus` | TField |  |  |
| 38 | `T4SDRIF.EXCL.CUST.FLAG` | `CaplTxFt4sdrifSlips_ExclCustFlag` | TField |  |  |
| 39 | `T4SDRIF.BAD.ADDRESS` | `CaplTxFt4sdrifSlips_BadAddress` | TField |  |  |
| 40 | `T4SDRIF.RESERVED.9` | `CaplTxFt4sdrifSlips_Reserved9` | TField |  |  |
| 41 | `T4SDRIF.RESERVED.8` | `CaplTxFt4sdrifSlips_Reserved8` | TField |  |  |
| 42 | `T4SDRIF.RESERVED.7` | `CaplTxFt4sdrifSlips_Reserved7` | TField |  |  |
| 43 | `T4SDRIF.RESERVED.6` | `CaplTxFt4sdrifSlips_Reserved6` | TField |  |  |
| 44 | `T4SDRIF.RESERVED.5` | `CaplTxFt4sdrifSlips_Reserved5` | TField |  |  |
| 45 | `T4SDRIF.RESERVED.4` | `CaplTxFt4sdrifSlips_Reserved4` | TField |  |  |
| 46 | `T4SDRIF.RESERVED.3` | `CaplTxFt4sdrifSlips_Reserved3` | TField |  |  |
| 47 | `T4SDRIF.RESERVED.2` | `CaplTxFt4sdrifSlips_Reserved2` | TField |  |  |
| 48 | `T4SDRIF.RESERVED.1` | `CaplTxFt4sdrifSlips_Reserved1` | TField |  |  |
| 49 | `T4SDRIF.OVERRIDE` | `CaplTxFt4sdrifSlips_Override` |  |  |  |
| 50 | `T4SDRIF.RECORD.STATUS` | `CaplTxFt4sdrifSlips_RecordStatus` | String |  |  |
| 51 | `T4SDRIF.CURR.NO` | `CaplTxFt4sdrifSlips_CurrNo` | String |  |  |
| 52 | `T4SDRIF.INPUTTER` | `CaplTxFt4sdrifSlips_Inputter` |  |  |  |
| 53 | `T4SDRIF.DATE.TIME` | `CaplTxFt4sdrifSlips_DateTime` |  |  |  |
| 54 | `T4SDRIF.AUTHORISER` | `CaplTxFt4sdrifSlips_Authoriser` | String |  |  |
| 55 | `T4SDRIF.CO.CODE` | `CaplTxFt4sdrifSlips_CoCode` | String |  |  |
| 56 | `T4SDRIF.DEPT.CODE` | `CaplTxFt4sdrifSlips_DeptCode` | String |  |  |
| 57 | `T4SDRIF.AUDITOR.CODE` | `CaplTxFt4sdrifSlips_AuditorCode` | String |  |  |
| 58 | `T4SDRIF.AUDIT.DATE.TIME` | `CaplTxFt4sdrifSlips_AuditDateTime` | String |  |  |
