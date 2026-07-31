# SC.CUSTODY.PARAM — Table Schema

> Source: `INSERTS/I_F.SC.CUSTODY.PARAM` in `SC_STP.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.CTDY.PARAM.INTERNAL.BROKER` | `ScCustodyParam_InternalBroker` | TField |  | For transactions created from incoming MT540 to MT543 messages, the BROKER.NO field in SEC.TRADE andSECURITY.TRANSFER will be defaulted from this field. Validation Rules: Should be defined as BROKER in CUSTOMER.SECURITY |
| 2 | `SC.CTDY.PARAM.TRD.CR.TXN` | `ScCustodyParam_TrdCrTxn` | TField |  | Credit transaction code for SEC.TRADE created based on incoming instruction (MT541 , MT543), will be updated fromthis field. Validation Rules: Should be a valid Credit Securities Transaction code |
| 3 | `SC.CTDY.PARAM.TRD.DR.TXN` | `ScCustodyParam_TrdDrTxn` | TField |  | Debit transaction code for SEC.TRADE created based on incoming instruction (MT541 , MT543), will be updated fromthis field. Validation Rules: Should be a valid Debit Securities Transaction code |
| 4 | `SC.CTDY.PARAM.EXT.TRF.CR.TXN` | `ScCustodyParam_ExtTrfCrTxn` | TField |  | Credit transaction code for SECURITY.TRANSFER created based on incoming instruction (MT540 , MT542), will beupdated from this field. Validation Rules: Should be a valid Credit Securities Transaction code |
| 5 | `SC.CTDY.PARAM.EXT.TRF.DR.TXN` | `ScCustodyParam_ExtTrfDrTxn` | TField |  | Debit transaction code for SECURITY.TRANSFER created based on incoming instruction (MT540 , MT542), will beupdated from this field. Validation Rules: Should be a valid Debit Securities Transaction code |
| 6 | `SC.CTDY.PARAM.INT.TRF.CR.TXN` | `ScCustodyParam_IntTrfCrTxn` | TField |  | Credit transaction code for internal SECURITY.TRANSFER created based on incoming instruction (MT542),will be updated from this field. Validation Rules: Should be a valid Credit Securities Transaction code |
| 7 | `SC.CTDY.PARAM.INT.TRF.DR.TXN` | `ScCustodyParam_IntTrfDrTxn` | TField |  | Debit transaction code for internal SECURITY.TRANSFER created based on incoming instruction (MT542), willbe updated from this field. Validation Rules: Should be a valid Debit Securities Transaction code |
| 8 | `SC.CTDY.PARAM.ALLOWED.SEC.TYPE` | `ScCustodyParam_AllowedSecType` |  |  |  |
| 9 | `SC.CTDY.PARAM.OFS.VERSION` | `ScCustodyParam_OfsVersion` |  |  |  |
| 10 | `SC.CTDY.PARAM.OFS.SOURCE` | `ScCustodyParam_OfsSource` |  |  |  |
| 11 | `SC.CTDY.PARAM.MKT.FEE.CALC` | `ScCustodyParam_MktFeeCalc` | TField |  | Field to specify whether market fees are to be calculated based on rules or picked up from incoming MT Messages. If set to YES , System rules will be applied for Fee amount calculation. If set to NO , Fees in message will be mapped to transaction and System rules will not be applied. Validation Rules: Allowed Values : YES or NO |
| 12 | `SC.CTDY.PARAM.DEF.MKT.FEE.TYPE` | `ScCustodyParam_DefMktFeeType` |  |  |  |
| 13 | `SC.CTDY.PARAM.DEF.MKT.FEE.QUAL` | `ScCustodyParam_DefMktFeeQual` |  |  |  |
| 14 | `SC.CTDY.PARAM.RESERVED.27` | `ScCustodyParam_Reserved27` | TField |  |  |
| 15 | `SC.CTDY.PARAM.RESERVED.26` | `ScCustodyParam_Reserved26` | TField |  |  |
| 16 | `SC.CTDY.PARAM.RESERVED.25` | `ScCustodyParam_Reserved25` | TField |  |  |
| 17 | `SC.CTDY.PARAM.RESERVED.24` | `ScCustodyParam_Reserved24` | TField |  |  |
| 18 | `SC.CTDY.PARAM.RESERVED.23` | `ScCustodyParam_Reserved23` | TField |  |  |
| 19 | `SC.CTDY.PARAM.RESERVED.22` | `ScCustodyParam_Reserved22` | TField |  |  |
| 20 | `SC.CTDY.PARAM.RESERVED.21` | `ScCustodyParam_Reserved21` | TField |  |  |
| 21 | `SC.CTDY.PARAM.RESERVED.20` | `ScCustodyParam_Reserved20` | TField |  |  |
| 22 | `SC.CTDY.PARAM.RESERVED.19` | `ScCustodyParam_Reserved19` | TField |  |  |
| 23 | `SC.CTDY.PARAM.RESERVED.18` | `ScCustodyParam_Reserved18` | TField |  |  |
| 24 | `SC.CTDY.PARAM.RESERVED.17` | `ScCustodyParam_Reserved17` | TField |  |  |
| 25 | `SC.CTDY.PARAM.RESERVED.16` | `ScCustodyParam_Reserved16` | TField |  |  |
| 26 | `SC.CTDY.PARAM.RESERVED.15` | `ScCustodyParam_Reserved15` | TField |  |  |
| 27 | `SC.CTDY.PARAM.RESERVED.14` | `ScCustodyParam_Reserved14` | TField |  |  |
| 28 | `SC.CTDY.PARAM.RESERVED.13` | `ScCustodyParam_Reserved13` | TField |  |  |
| 29 | `SC.CTDY.PARAM.RESERVED.12` | `ScCustodyParam_Reserved12` | TField |  |  |
| 30 | `SC.CTDY.PARAM.RESERVED.11` | `ScCustodyParam_Reserved11` | TField |  |  |
| 31 | `SC.CTDY.PARAM.RESERVED.10` | `ScCustodyParam_Reserved10` | TField |  |  |
| 32 | `SC.CTDY.PARAM.RESERVED.9` | `ScCustodyParam_Reserved9` | TField |  |  |
| 33 | `SC.CTDY.PARAM.RESERVED.8` | `ScCustodyParam_Reserved8` | TField |  |  |
| 34 | `SC.CTDY.PARAM.RESERVED.7` | `ScCustodyParam_Reserved7` | TField |  |  |
| 35 | `SC.CTDY.PARAM.RESERVED.6` | `ScCustodyParam_Reserved6` | TField |  |  |
| 36 | `SC.CTDY.PARAM.RESERVED.5` | `ScCustodyParam_Reserved5` | TField |  |  |
| 37 | `SC.CTDY.PARAM.RESERVED.4` | `ScCustodyParam_Reserved4` | TField |  |  |
| 38 | `SC.CTDY.PARAM.RESERVED.3` | `ScCustodyParam_Reserved3` | TField |  |  |
| 39 | `SC.CTDY.PARAM.RESERVED.2` | `ScCustodyParam_Reserved2` | TField |  |  |
| 40 | `SC.CTDY.PARAM.RESERVED.1` | `ScCustodyParam_Reserved1` | TField |  |  |
| 41 | `SC.CTDY.PARAM.LOCAL.REF` | `ScCustodyParam_LocalRef` |  |  |  |
| 42 | `SC.CTDY.PARAM.OVERRIDE` | `ScCustodyParam_Override` |  |  |  |
| 43 | `SC.CTDY.PARAM.RECORD.STATUS` | `ScCustodyParam_RecordStatus` | String |  |  |
| 44 | `SC.CTDY.PARAM.CURR.NO` | `ScCustodyParam_CurrNo` | String |  |  |
| 45 | `SC.CTDY.PARAM.INPUTTER` | `ScCustodyParam_Inputter` |  |  |  |
| 46 | `SC.CTDY.PARAM.DATE.TIME` | `ScCustodyParam_DateTime` |  |  |  |
| 47 | `SC.CTDY.PARAM.AUTHORISER` | `ScCustodyParam_Authoriser` | String |  |  |
| 48 | `SC.CTDY.PARAM.CO.CODE` | `ScCustodyParam_CoCode` | String |  |  |
| 49 | `SC.CTDY.PARAM.DEPT.CODE` | `ScCustodyParam_DeptCode` | String |  |  |
| 50 | `SC.CTDY.PARAM.AUDITOR.CODE` | `ScCustodyParam_AuditorCode` | String |  |  |
| 51 | `SC.CTDY.PARAM.AUDIT.DATE.TIME` | `ScCustodyParam_AuditDateTime` | String |  |  |
