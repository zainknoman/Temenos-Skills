# CAPL.TX.FT4SDRSP.SLIPS — Table Schema

> Source: `INSERTS/I_F.CAPL.TX.FT4SDRSP.SLIPS` in `CADEPO_CRAReporting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `T4SDRSP.ID.1` | `CaplTxFt4sdrspSlips_Id1` | TField |  |  |
| 2 | `T4SDRSP.SLIP.YEAR` | `CaplTxFt4sdrspSlips_SlipYear` | TField |  |  |
| 3 | `T4SDRSP.SLIP.NUMBER` | `CaplTxFt4sdrspSlips_SlipNumber` | TField |  |  |
| 4 | `T4SDRSP.SLIP.SEQ.NO` | `CaplTxFt4sdrspSlips_SlipSeqNo` | TField |  |  |
| 5 | `T4SDRSP.CUSTOMER.1` | `CaplTxFt4sdrspSlips_Customer1` | TField |  |  |
| 6 | `T4SDRSP.CUSTOMER.2` | `CaplTxFt4sdrspSlips_Customer2` | TField |  |  |
| 7 | `T4SDRSP.COMPANY` | `CaplTxFt4sdrspSlips_Company` | TField |  |  |
| 8 | `T4SDRSP.SLIP.PROCESS` | `CaplTxFt4sdrspSlips_SlipProcess` | TField |  |  |
| 9 | `T4SDRSP.SLIP.AMENDED` | `CaplTxFt4sdrspSlips_SlipAmended` | TField |  |  |
| 10 | `T4SDRSP.AMEND.SEQ.NO` | `CaplTxFt4sdrspSlips_AmendSeqNo` | TField |  |  |
| 11 | `T4SDRSP.SLIP.DATE` | `CaplTxFt4sdrspSlips_SlipDate` | TField |  |  |
| 12 | `T4SDRSP.SLIP.USER` | `CaplTxFt4sdrspSlips_SlipUser` | TField |  |  |
| 13 | `T4SDRSP.BOX.20` | `CaplTxFt4sdrspSlips_Box20` | TField |  |  |
| 14 | `T4SDRSP.BOX.22` | `CaplTxFt4sdrspSlips_Box22` | TField |  |  |
| 15 | `T4SDRSP.BOX.25` | `CaplTxFt4sdrspSlips_Box25` | TField |  |  |
| 16 | `T4SDRSP.BOX.18` | `CaplTxFt4sdrspSlips_Box18` | TField |  |  |
| 17 | `T4SDRSP.BOX.27` | `CaplTxFt4sdrspSlips_Box27` | TField |  |  |
| 18 | `T4SDRSP.BOX.30` | `CaplTxFt4sdrspSlips_Box30` | TField |  |  |
| 19 | `T4SDRSP.BOX.35` | `CaplTxFt4sdrspSlips_Box35` | TField |  |  |
| 20 | `T4SDRSP.YEAR` | `CaplTxFt4sdrspSlips_Year` | TField |  |  |
| 21 | `T4SDRSP.BOX.24` | `CaplTxFt4sdrspSlips_Box24` | TField |  |  |
| 22 | `T4SDRSP.BOX.12` | `CaplTxFt4sdrspSlips_Box12` | TField |  |  |
| 23 | `T4SDRSP.BOX.36` | `CaplTxFt4sdrspSlips_Box36` | TField |  |  |
| 24 | `T4SDRSP.BOX.14` | `CaplTxFt4sdrspSlips_Box14` | TField |  |  |
| 25 | `T4SDRSP.BOX.60` | `CaplTxFt4sdrspSlips_Box60` | TField |  |  |
| 26 | `T4SDRSP.BOX.61` | `CaplTxFt4sdrspSlips_Box61` | TField |  |  |
| 27 | `T4SDRSP.BEN.NAME.1` | `CaplTxFt4sdrspSlips_BenName1` | TField |  |  |
| 28 | `T4SDRSP.BEN.ADR.1` | `CaplTxFt4sdrspSlips_BenAdr1` | TField |  |  |
| 29 | `T4SDRSP.BEN.ADR.2` | `CaplTxFt4sdrspSlips_BenAdr2` | TField |  |  |
| 30 | `T4SDRSP.BEN.ADR.3` | `CaplTxFt4sdrspSlips_BenAdr3` | TField |  |  |
| 31 | `T4SDRSP.BEN.ADR.4` | `CaplTxFt4sdrspSlips_BenAdr4` | TField |  |  |
| 32 | `T4SDRSP.BEN.ADR.5` | `CaplTxFt4sdrspSlips_BenAdr5` | TField |  |  |
| 33 | `T4SDRSP.BEN.ADR.6` | `CaplTxFt4sdrspSlips_BenAdr6` | TField |  |  |
| 34 | `T4SDRSP.BEN.ADR.7` | `CaplTxFt4sdrspSlips_BenAdr7` | TField |  |  |
| 35 | `T4SDRSP.BEN.ADR.8` | `CaplTxFt4sdrspSlips_BenAdr8` | TField |  |  |
| 36 | `T4SDRSP.BEN.ADR.9` | `CaplTxFt4sdrspSlips_BenAdr9` | TField |  |  |
| 37 | `T4SDRSP.BOX.34` | `CaplTxFt4sdrspSlips_Box34` | TField |  |  |
| 38 | `T4SDRSP.BOX.28` | `CaplTxFt4sdrspSlips_Box28` | TField |  |  |
| 39 | `T4SDRSP.EXCL.CUST.FLAG` | `CaplTxFt4sdrspSlips_ExclCustFlag` | TField |  |  |
| 40 | `T4SDRSP.BAD.ADDRESS` | `CaplTxFt4sdrspSlips_BadAddress` | TField |  |  |
| 41 | `T4SDRSP.RESERVED.9` | `CaplTxFt4sdrspSlips_Reserved9` | TField |  |  |
| 42 | `T4SDRSP.RESERVED.8` | `CaplTxFt4sdrspSlips_Reserved8` | TField |  |  |
| 43 | `T4SDRSP.RESERVED.7` | `CaplTxFt4sdrspSlips_Reserved7` | TField |  |  |
| 44 | `T4SDRSP.RESERVED.6` | `CaplTxFt4sdrspSlips_Reserved6` | TField |  |  |
| 45 | `T4SDRSP.RESERVED.5` | `CaplTxFt4sdrspSlips_Reserved5` | TField |  |  |
| 46 | `T4SDRSP.RESERVED.4` | `CaplTxFt4sdrspSlips_Reserved4` | TField |  |  |
| 47 | `T4SDRSP.RESERVED.3` | `CaplTxFt4sdrspSlips_Reserved3` | TField |  |  |
| 48 | `T4SDRSP.RESERVED.2` | `CaplTxFt4sdrspSlips_Reserved2` | TField |  |  |
| 49 | `T4SDRSP.RESERVED.1` | `CaplTxFt4sdrspSlips_Reserved1` | TField |  |  |
| 50 | `T4SDRSP.OVERRIDE` | `CaplTxFt4sdrspSlips_Override` |  |  |  |
| 51 | `T4SDRSP.RECORD.STATUS` | `CaplTxFt4sdrspSlips_RecordStatus` | String |  |  |
| 52 | `T4SDRSP.CURR.NO` | `CaplTxFt4sdrspSlips_CurrNo` | String |  |  |
| 53 | `T4SDRSP.INPUTTER` | `CaplTxFt4sdrspSlips_Inputter` |  |  |  |
| 54 | `T4SDRSP.DATE.TIME` | `CaplTxFt4sdrspSlips_DateTime` |  |  |  |
| 55 | `T4SDRSP.AUTHORISER` | `CaplTxFt4sdrspSlips_Authoriser` | String |  |  |
| 56 | `T4SDRSP.CO.CODE` | `CaplTxFt4sdrspSlips_CoCode` | String |  |  |
| 57 | `T4SDRSP.DEPT.CODE` | `CaplTxFt4sdrspSlips_DeptCode` | String |  |  |
| 58 | `T4SDRSP.AUDITOR.CODE` | `CaplTxFt4sdrspSlips_AuditorCode` | String |  |  |
| 59 | `T4SDRSP.AUDIT.DATE.TIME` | `CaplTxFt4sdrspSlips_AuditDateTime` | String |  |  |
