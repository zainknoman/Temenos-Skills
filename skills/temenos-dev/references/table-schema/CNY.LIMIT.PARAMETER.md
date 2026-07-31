# CNY.LIMIT.PARAMETER — Table Schema

> Source: `INSERTS/I_F.CNY.LIMIT.PARAMETER` in `OTREMI_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CNY.LIMIT.PARAM.DESCRIPTION` | `CnyLimitParameter_Description` | TField |  | Description of the parameter table |
| 2 | `CNY.LIMIT.PARAM.REMITTANCE.TYPE` | `CnyLimitParameter_RemittanceType` |  |  |  |
| 3 | `CNY.LIMIT.PARAM.SECTOR.FROM` | `CnyLimitParameter_SectorFrom` |  |  |  |
| 4 | `CNY.LIMIT.PARAM.SECTOR.TO` | `CnyLimitParameter_SectorTo` |  |  |  |
| 5 | `CNY.LIMIT.PARAM.LEGAL.DOC.NAME` | `CnyLimitParameter_LegalDocName` |  |  |  |
| 6 | `CNY.LIMIT.PARAM.RESERVED.1` | `CnyLimitParameter_Reserved1` |  |  |  |
| 7 | `CNY.LIMIT.PARAM.RESERVED.2` | `CnyLimitParameter_Reserved2` |  |  |  |
| 8 | `CNY.LIMIT.PARAM.RESERVED.3` | `CnyLimitParameter_Reserved3` |  |  |  |
| 9 | `CNY.LIMIT.PARAM.REMITTANCE.LIMIT` | `CnyLimitParameter_RemittanceLimit` | TField |  | Allowed CNY remittance limit |
| 10 | `CNY.LIMIT.PARAM.SR.CITIZEN.LIMIT` | `CnyLimitParameter_SrCitizenLimit` | TField |  | Allowed per transaction limit for senior citizens |
| 11 | `CNY.LIMIT.PARAM.DETECT.SCAM.DAYS` | `CnyLimitParameter_DetectScamDays` | TField |  | Specifies the number of days to be verified for detecting fradulent transactions |
| 12 | `CNY.LIMIT.PARAM.DETECT.TXN.COUNT` | `CnyLimitParameter_DetectTxnCount` | TField |  | Specifies the number of transaction allowed for a customer and the same will be check for detecting fraudulent transactions |
| 13 | `CNY.LIMIT.PARAM.BEN.CHECK.RTN` | `CnyLimitParameter_BenCheckRtn` | TField |  | Routine to get the account name to compare with beneficiary name |
| 14 | `CNY.LIMIT.PARAM.PO.REMITTANCE.TYPE` | `CnyLimitParameter_PoRemittanceType` |  |  |  |
| 15 | `CNY.LIMIT.PARAM.PO.SECTOR.FROM` | `CnyLimitParameter_PoSectorFrom` |  |  |  |
| 16 | `CNY.LIMIT.PARAM.PO.SECTOR.TO` | `CnyLimitParameter_PoSectorTo` |  |  |  |
| 17 | `CNY.LIMIT.PARAM.PO.LEGAL.DOC.NAME` | `CnyLimitParameter_PoLegalDocName` |  |  |  |
| 18 | `CNY.LIMIT.PARAM.RESERVED.8` | `CnyLimitParameter_Reserved8` | TField |  | Reserved for future use |
| 19 | `CNY.LIMIT.PARAM.RESERVED.9` | `CnyLimitParameter_Reserved9` | TField |  | Reserved for future use |
| 20 | `CNY.LIMIT.PARAM.RESERVED.10` | `CnyLimitParameter_Reserved10` | TField |  | Reserved for future use |
| 21 | `CNY.LIMIT.PARAM.RESERVED.11` | `CnyLimitParameter_Reserved11` | TField |  | Reserved for future use |
| 22 | `CNY.LIMIT.PARAM.RESERVED.12` | `CnyLimitParameter_Reserved12` | TField |  | Reserved for future use |
| 23 | `CNY.LIMIT.PARAM.RESERVED.13` | `CnyLimitParameter_Reserved13` | TField |  | Reserved for future use |
| 24 | `CNY.LIMIT.PARAM.LOCAL.REF` | `CnyLimitParameter_LocalRef` |  |  |  |
| 25 | `CNY.LIMIT.PARAM.OVERRIDE` | `CnyLimitParameter_Override` |  |  |  |
| 26 | `CNY.LIMIT.PARAM.RECORD.STATUS` | `CnyLimitParameter_RecordStatus` | String |  |  |
| 27 | `CNY.LIMIT.PARAM.CURR.NO` | `CnyLimitParameter_CurrNo` | String |  |  |
| 28 | `CNY.LIMIT.PARAM.INPUTTER` | `CnyLimitParameter_Inputter` |  |  |  |
| 29 | `CNY.LIMIT.PARAM.DATE.TIME` | `CnyLimitParameter_DateTime` |  |  |  |
| 30 | `CNY.LIMIT.PARAM.AUTHORISER` | `CnyLimitParameter_Authoriser` | String |  |  |
| 31 | `CNY.LIMIT.PARAM.CO.CODE` | `CnyLimitParameter_CoCode` | String |  |  |
| 32 | `CNY.LIMIT.PARAM.DEPT.CODE` | `CnyLimitParameter_DeptCode` | String |  |  |
| 33 | `CNY.LIMIT.PARAM.AUDITOR.CODE` | `CnyLimitParameter_AuditorCode` | String |  |  |
| 34 | `CNY.LIMIT.PARAM.AUDIT.DATE.TIME` | `CnyLimitParameter_AuditDateTime` | String |  |  |
