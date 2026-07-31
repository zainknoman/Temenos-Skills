# AUOBPZ.ACCT.DATASHARE — Table Schema

> Source: `INSERTS/I_F.AUOBPZ.ACCT.DATASHARE` in `AUOBPZ_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AUOBPZ.DATASHARE.ALT.ACCT.ID` | `AuobpzAcctDatashare_AltAcctId` | TField |  | Contains the unique account identifier Valid entry from ALTERNATE.ACCOUNT |
| 2 | `AUOBPZ.DATASHARE.CUSTOMER.NUMBER` | `AuobpzAcctDatashare_CustomerNumber` | TField |  | Contains the customer id for whom the disclosure option of the account is updated or nomination for in the account is provided. |
| 3 | `AUOBPZ.DATASHARE.DATA.SHARING.STATUS` | `AuobpzAcctDatashare_DataSharingStatus` | TField |  | Contains the overall data sharing status of the account. |
| 4 | `AUOBPZ.DATASHARE.DATA.SHARING.CHANGE.DATE` | `AuobpzAcctDatashare_DataSharingChangeDate` | TField |  | Contains the date on which the overall data sharing status of the account got updated. |
| 5 | `AUOBPZ.DATASHARE.DATA.SHARING.UPDATED.BY` | `AuobpzAcctDatashare_DataSharingUpdatedBy` | TField |  | Contains the customer identifier who last updated disclosure option of the account or nomination of secondary users in the account. |
| 6 | `AUOBPZ.DATASHARE.DATA.SHARING.SOURCE` | `AuobpzAcctDatashare_DataSharingSource` | TField |  | Indicates the source details by which the overall data sharing status of account gets updated. Possible values- DOMS (Disclosure Option Management System) Nominations |
| 7 | `AUOBPZ.DATASHARE.RESERVED.2` | `AuobpzAcctDatashare_Reserved2` | TField |  |  |
| 8 | `AUOBPZ.DATASHARE.RESERVED.1` | `AuobpzAcctDatashare_Reserved1` | TField |  |  |
| 9 | `AUOBPZ.DATASHARE.LOCAL.REF` | `AuobpzAcctDatashare_LocalRef` |  |  |  |
| 10 | `AUOBPZ.DATASHARE.OVERRIDE` | `AuobpzAcctDatashare_Override` |  |  |  |
| 11 | `AUOBPZ.DATASHARE.RECORD.STATUS` | `AuobpzAcctDatashare_RecordStatus` | String |  |  |
| 12 | `AUOBPZ.DATASHARE.CURR.NO` | `AuobpzAcctDatashare_CurrNo` | String |  |  |
| 13 | `AUOBPZ.DATASHARE.INPUTTER` | `AuobpzAcctDatashare_Inputter` |  |  |  |
| 14 | `AUOBPZ.DATASHARE.DATE.TIME` | `AuobpzAcctDatashare_DateTime` |  |  |  |
| 15 | `AUOBPZ.DATASHARE.AUTHORISER` | `AuobpzAcctDatashare_Authoriser` | String |  |  |
| 16 | `AUOBPZ.DATASHARE.CO.CODE` | `AuobpzAcctDatashare_CoCode` | String |  |  |
| 17 | `AUOBPZ.DATASHARE.DEPT.CODE` | `AuobpzAcctDatashare_DeptCode` | String |  |  |
| 18 | `AUOBPZ.DATASHARE.AUDITOR.CODE` | `AuobpzAcctDatashare_AuditorCode` | String |  |  |
| 19 | `AUOBPZ.DATASHARE.AUDIT.DATE.TIME` | `AuobpzAcctDatashare_AuditDateTime` | String |  |  |
