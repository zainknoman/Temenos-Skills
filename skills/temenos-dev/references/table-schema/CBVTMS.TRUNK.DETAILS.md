# CBVTMS.TRUNK.DETAILS — Table Schema

> Source: `INSERTS/I_F.CBVTMS.TRUNK.DETAILS` in `CBVTMS_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `VTMS.BANK.NAME` | `CbvtmsTrunkDetails_BankName` | TField |  | The bank name which has deposited the currency |
| 2 | `VTMS.REQUEST.ID` | `CbvtmsTrunkDetails_RequestId` | TField |  | The request ID rasied by the commercial bank |
| 3 | `VTMS.DATE.DEPOSITED` | `CbvtmsTrunkDetails_DateDeposited` | TField |  | The date on which the deposit of currency was made |
| 4 | `VTMS.TOTAL.VALUE` | `CbvtmsTrunkDetails_TotalValue` | TField |  | The total value deposited |
| 5 | `VTMS.DENOMINATION` | `CbvtmsTrunkDetails_Denomination` |  |  |  |
| 6 | `VTMS.PROCESSED` | `CbvtmsTrunkDetails_Processed` | TField |  | Indicates if the denomination in the truck is send to currency processing or not |
| 7 | `VTMS.LOCAL.REF` | `CbvtmsTrunkDetails_LocalRef` |  |  |  |
| 8 | `VTMS.RESERVED.1` | `CbvtmsTrunkDetails_Reserved1` | TField |  | Reserved field for future use |
| 9 | `VTMS.RESERVED.2` | `CbvtmsTrunkDetails_Reserved2` | TField |  | Reserved field for future use |
| 10 | `VTMS.RESERVED.3` | `CbvtmsTrunkDetails_Reserved3` | TField |  | Reserved field for future use |
| 11 | `VTMS.RESERVED.4` | `CbvtmsTrunkDetails_Reserved4` | TField |  | Reserved field for future use |
| 12 | `VTMS.RESERVED.5` | `CbvtmsTrunkDetails_Reserved5` | TField |  | Reserved field for future use |
| 13 | `VTMS.OVERRIDE` | `CbvtmsTrunkDetails_Override` |  |  |  |
| 14 | `VTMS.RECORD.STATUS` | `CbvtmsTrunkDetails_RecordStatus` | String |  |  |
| 15 | `VTMS.CURR.NO` | `CbvtmsTrunkDetails_CurrNo` | String |  |  |
| 16 | `VTMS.INPUTTER` | `CbvtmsTrunkDetails_Inputter` |  |  |  |
| 17 | `VTMS.DATE.TIME` | `CbvtmsTrunkDetails_DateTime` |  |  |  |
| 18 | `VTMS.AUTHORISER` | `CbvtmsTrunkDetails_Authoriser` | String |  |  |
| 19 | `VTMS.CO.CODE` | `CbvtmsTrunkDetails_CoCode` | String |  |  |
| 20 | `VTMS.DEPT.CODE` | `CbvtmsTrunkDetails_DeptCode` | String |  |  |
| 21 | `VTMS.AUDITOR.CODE` | `CbvtmsTrunkDetails_AuditorCode` | String |  |  |
| 22 | `VTMS.AUDIT.DATE.TIME` | `CbvtmsTrunkDetails_AuditDateTime` | String |  |  |
