# HUTXNF.LEVY.CARD.TRANSACTION — Table Schema

> Source: `INSERTS/I_F.HUTXNF.LEVY.CARD.TRANSACTION` in `HUTXNF_TransactionLevy.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `HU.CT.TRANSACTION.AMOUNT` | `HutxnfLevyCardTransaction_TransactionAmount` |  |  |  |
| 2 | `HU.CT.CURRENCY` | `HutxnfLevyCardTransaction_Currency` |  |  |  |
| 3 | `HU.CT.CARD.NUMBER` | `HutxnfLevyCardTransaction_CardNumber` |  |  |  |
| 4 | `HU.CT.LEVY.ELIGIBLE` | `HutxnfLevyCardTransaction_LevyEligible` |  |  |  |
| 5 | `HU.CT.RESERVED.10` | `HutxnfLevyCardTransaction_Reserved10` | TField |  |  |
| 6 | `HU.CT.RESERVED.9` | `HutxnfLevyCardTransaction_Reserved9` | TField |  |  |
| 7 | `HU.CT.RESERVED.8` | `HutxnfLevyCardTransaction_Reserved8` | TField |  |  |
| 8 | `HU.CT.RESERVED.7` | `HutxnfLevyCardTransaction_Reserved7` | TField |  |  |
| 9 | `HU.CT.RESERVED.6` | `HutxnfLevyCardTransaction_Reserved6` | TField |  |  |
| 10 | `HU.CT.RESERVED.5` | `HutxnfLevyCardTransaction_Reserved5` | TField |  |  |
| 11 | `HU.CT.RESERVED.4` | `HutxnfLevyCardTransaction_Reserved4` | TField |  |  |
| 12 | `HU.CT.RESERVED.3` | `HutxnfLevyCardTransaction_Reserved3` | TField |  |  |
| 13 | `HU.CT.RESERVED.2` | `HutxnfLevyCardTransaction_Reserved2` | TField |  |  |
| 14 | `HU.CT.RESERVED.1` | `HutxnfLevyCardTransaction_Reserved1` | TField |  |  |
| 15 | `HU.CT.LOCAL.REF` | `HutxnfLevyCardTransaction_LocalRef` |  |  |  |
| 16 | `HU.CT.OVERRIDE` | `HutxnfLevyCardTransaction_Override` |  |  |  |
| 17 | `HU.CT.RECORD.STATUS` | `HutxnfLevyCardTransaction_RecordStatus` | String |  |  |
| 18 | `HU.CT.CURR.NO` | `HutxnfLevyCardTransaction_CurrNo` | String |  |  |
| 19 | `HU.CT.INPUTTER` | `HutxnfLevyCardTransaction_Inputter` |  |  |  |
| 20 | `HU.CT.DATE.TIME` | `HutxnfLevyCardTransaction_DateTime` |  |  |  |
| 21 | `HU.CT.AUTHORISER` | `HutxnfLevyCardTransaction_Authoriser` | String |  |  |
| 22 | `HU.CT.CO.CODE` | `HutxnfLevyCardTransaction_CoCode` | String |  |  |
| 23 | `HU.CT.DEPT.CODE` | `HutxnfLevyCardTransaction_DeptCode` | String |  |  |
| 24 | `HU.CT.AUDITOR.CODE` | `HutxnfLevyCardTransaction_AuditorCode` | String |  |  |
| 25 | `HU.CT.AUDIT.DATE.TIME` | `HutxnfLevyCardTransaction_AuditDateTime` | String |  |  |
