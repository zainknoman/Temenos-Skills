# ARACCT.FX.BLACKLIST — Table Schema

> Source: `INSERTS/I_F.ARACCT.FX.BLACKLIST` in `ARACCT_FXBlacklistLimitValidation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ARACCT.FXB.PROVIDER.CODE` | `AracctFxBlacklist_ProviderCode` | TField |  | Internal reference code given by the provider. |
| 2 | `ARACCT.FXB.CUSTOMER.NUMBER` | `AracctFxBlacklist_CustomerNumber` | TField |  | Customer number of the Legal Id received from the input file. In case the legal Id does not have a customer in T24, this field will be blank. |
| 3 | `ARACCT.FXB.STATUS` | `AracctFxBlacklist_Status` | TField |  | Status of the register, A-New/modified and B- removal. |
| 4 | `ARACCT.FXB.CUSTOMER.NAME` | `AracctFxBlacklist_CustomerName` |  |  |  |
| 5 | `ARACCT.FXB.LEGAL.ID.TYPE` | `AracctFxBlacklist_LegalIdType` | TField |  | Legal Identification type,01,02,03.. etc |
| 6 | `ARACCT.FXB.LEGAL.ID.NAME` | `AracctFxBlacklist_LegalIdName` | TField |  | Description of the Legal Id type for (DNE/LE/LC/CUIT/CUIL/CDI) |
| 7 | `ARACCT.FXB.COMMUNICATION.TYPE` | `AracctFxBlacklist_CommunicationType` | TField |  | Type of communication from the Central bank. This field is stored for information purpose in T24. |
| 8 | `ARACCT.FXB.COMMUNICATION.NUMBER` | `AracctFxBlacklist_CommunicationNumber` | TField |  | Communication number from the Central bank. This is a numeric field. |
| 9 | `ARACCT.FXB.ISSUANCE.DATE` | `AracctFxBlacklist_IssuanceDate` | TField |  | Communication date from the Central bank. |
| 10 | `ARACCT.FXB.REFERENCE` | `AracctFxBlacklist_Reference` |  |  |  |
| 11 | `ARACCT.FXB.BLACKLISTED.FROM` | `AracctFxBlacklist_BlacklistedFrom` | TField |  | Date from which the customer is blacklisted. |
| 12 | `ARACCT.FXB.BLACKLISTED.TO` | `AracctFxBlacklist_BlacklistedTo` | TField |  | Date till which the customer is blacklisted. |
| 13 | `ARACCT.FXB.COMMENTS` | `AracctFxBlacklist_Comments` |  |  |  |
| 14 | `ARACCT.FXB.MANUAL.INPUT` | `AracctFxBlacklist_ManualInput` | TField |  | To identify if the record has been input manually by user or uploaded from file. This is a YES or No field.If the value is YES then the record is registered manually by user. If it is NO then the record is uploaded from an input file. |
| 15 | `ARACCT.FXB.BLACKLISTED.CUSTOMER` | `AracctFxBlacklist_BlacklistedCustomer` | TField |  | This field hold values YES/NO.1. If YES - then FX blacklist customer validation will happen for the customer when teller or payment order transaction is performed2. If NO - Then no FX blacklist customer validation will happen.When the records are created from Bulk file upload the value is automatically set as YES when the STATUS is A, and NO when the STATUS is B.When created manually the field will appear with the value YES, if the end user decides to make it as NO he can uncheck the field. |
| 16 | `ARACCT.FXB.FILE.NAME` | `AracctFxBlacklist_FileName` | TField |  | The name of the last file in which this record has been created/Amended will be available. |
| 17 | `ARACCT.FXB.PROCESSED.DATE` | `AracctFxBlacklist_ProcessedDate` | TField |  |  |
| 18 | `ARACCT.FXB.RESERVED.10` | `AracctFxBlacklist_Reserved10` | TField |  | Reserved for Future use. |
| 19 | `ARACCT.FXB.RESERVED.9` | `AracctFxBlacklist_Reserved9` | TField |  | Reserved for Future use. |
| 20 | `ARACCT.FXB.RESERVED.8` | `AracctFxBlacklist_Reserved8` | TField |  | Reserved for Future use. |
| 21 | `ARACCT.FXB.RESERVED.7` | `AracctFxBlacklist_Reserved7` | TField |  | Reserved for Future use. |
| 22 | `ARACCT.FXB.RESERVED.6` | `AracctFxBlacklist_Reserved6` | TField |  | Reserved for Future use. |
| 23 | `ARACCT.FXB.RESERVED.5` | `AracctFxBlacklist_Reserved5` | TField |  | Reserved for Future use. |
| 24 | `ARACCT.FXB.RESERVED.4` | `AracctFxBlacklist_Reserved4` | TField |  | Reserved for Future use. |
| 25 | `ARACCT.FXB.RESERVED.3` | `AracctFxBlacklist_Reserved3` | TField |  | Reserved for Future use. |
| 26 | `ARACCT.FXB.RESERVED.2` | `AracctFxBlacklist_Reserved2` | TField |  | Reserved for Future use. |
| 27 | `ARACCT.FXB.RESERVED.1` | `AracctFxBlacklist_Reserved1` | TField |  | Reserved for Future use. |
| 28 | `ARACCT.FXB.RECORD.STATUS` | `AracctFxBlacklist_RecordStatus` | String |  |  |
| 29 | `ARACCT.FXB.CURR.NO` | `AracctFxBlacklist_CurrNo` | String |  |  |
| 30 | `ARACCT.FXB.INPUTTER` | `AracctFxBlacklist_Inputter` |  |  |  |
| 31 | `ARACCT.FXB.DATE.TIME` | `AracctFxBlacklist_DateTime` |  |  |  |
| 32 | `ARACCT.FXB.AUTHORISER` | `AracctFxBlacklist_Authoriser` | String |  |  |
| 33 | `ARACCT.FXB.CO.CODE` | `AracctFxBlacklist_CoCode` | String |  |  |
| 34 | `ARACCT.FXB.DEPT.CODE` | `AracctFxBlacklist_DeptCode` | String |  |  |
| 35 | `ARACCT.FXB.AUDITOR.CODE` | `AracctFxBlacklist_AuditorCode` | String |  |  |
| 36 | `ARACCT.FXB.AUDIT.DATE.TIME` | `AracctFxBlacklist_AuditDateTime` | String |  |  |
