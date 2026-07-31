# UKDDMP.DDO.DIRECTORY — Table Schema

> Source: `INSERTS/I_F.UKDDMP.DDO.DIRECTORY` in `UKDDMP_Import.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `UKDDMP.DDO.DIR.RECORD.TYPE` | `UkddmpDdoDirectory_RecordType` | TField |  | Record type � will be O |
| 2 | `UKDDMP.DDO.DIR.LAST.AMENDED.DATE` | `UkddmpDdoDirectory_LastAmendedDate` | TField |  | DDMMYY (this is the date when latest the directory was amended) |
| 3 | `UKDDMP.DDO.DIR.SERVICE.USER.NO` | `UkddmpDdoDirectory_ServiceUserNo` | TField |  | Value of SUN (Service User number) |
| 4 | `UKDDMP.DDO.DIR.SERVICE.USER.NAME` | `UkddmpDdoDirectory_ServiceUserName` | TField |  | Service User name |
| 5 | `UKDDMP.DDO.DIR.SU.ADDRESSEE.NAME` | `UkddmpDdoDirectory_SuAddresseeName` | TField |  | Contact address of the Scheme administrator |
| 6 | `UKDDMP.DDO.DIR.SU.POSTAL.NAME` | `UkddmpDdoDirectory_SuPostalName` | TField |  | Postal name of the scheme administrator |
| 7 | `UKDDMP.DDO.DIR.SU.ADDRESSLINE1` | `UkddmpDdoDirectory_SuAddressline1` | TField |  | Address |
| 8 | `UKDDMP.DDO.DIR.SU.ADDRESSLINE2` | `UkddmpDdoDirectory_SuAddressline2` | TField |  | Address |
| 9 | `UKDDMP.DDO.DIR.SU.ADDRESSLINE3` | `UkddmpDdoDirectory_SuAddressline3` | TField |  | Address |
| 10 | `UKDDMP.DDO.DIR.SU.ADDRESSLINE4` | `UkddmpDdoDirectory_SuAddressline4` | TField |  | Address |
| 11 | `UKDDMP.DDO.DIR.SU.POST.CODE` | `UkddmpDdoDirectory_SuPostCode` | TField |  | Post Code |
| 12 | `UKDDMP.DDO.DIR.TELEPHONE` | `UkddmpDdoDirectory_Telephone` | TField |  | Telephone no |
| 13 | `UKDDMP.DDO.DIR.FAX.NUMBER` | `UkddmpDdoDirectory_FaxNumber` | TField |  | Fax number |
| 14 | `UKDDMP.DDO.DIR.ORIG.ADDRESSLINE1` | `UkddmpDdoDirectory_OrigAddressline1` | TField |  | User name |
| 15 | `UKDDMP.DDO.DIR.ORIG.ADDRESSLINE2` | `UkddmpDdoDirectory_OrigAddressline2` | TField |  | Postal name |
| 16 | `UKDDMP.DDO.DIR.ORIG.ADDRESSLINE3` | `UkddmpDdoDirectory_OrigAddressline3` | TField |  | Address of service user |
| 17 | `UKDDMP.DDO.DIR.ORIG.ADDRESSLINE4` | `UkddmpDdoDirectory_OrigAddressline4` | TField |  | Address of service user |
| 18 | `UKDDMP.DDO.DIR.ORIG.ADDRESSLINE5` | `UkddmpDdoDirectory_OrigAddressline5` | TField |  | Address of service user |
| 19 | `UKDDMP.DDO.DIR.ORIG.ADDRESSLINE6` | `UkddmpDdoDirectory_OrigAddressline6` | TField |  | Address of service user |
| 20 | `UKDDMP.DDO.DIR.SPONSOR.BANK.CODE` | `UkddmpDdoDirectory_SponsorBankCode` | TField |  | The bank code of the service user�s sponsor |
| 21 | `UKDDMP.DDO.DIR.ORIGINATOR.STATUS` | `UkddmpDdoDirectory_OriginatorStatus` | TField |  | Originator Status |
| 22 | `UKDDMP.DDO.DIR.AUDDIS.STATUS` | `UkddmpDdoDirectory_AuddisStatus` | TField |  | AUDDIS status of the user � can be either L, M, T or N |
| 23 | `UKDDMP.DDO.DIR.PRIOR.NOT.PERIOD` | `UkddmpDdoDirectory_PriorNotPeriod` | TField |  | Prior notification period. Will be numeric, zero (0) filled to the left where required. |
| 24 | `UKDDMP.DDO.DIR.DORMANCY.PERIOD` | `UkddmpDdoDirectory_DormancyPeriod` | TField |  | Dormancy period for the mandate. Will be numeric, zero (0) filled to the left where required. 999 means the DD is indefinite |
| 25 | `UKDDMP.DDO.DIR.MARKET.SEGMENT` | `UkddmpDdoDirectory_MarketSegment` | TField |  | Market segment |
| 26 | `UKDDMP.DDO.DIR.AMAL.SEGMENT` | `UkddmpDdoDirectory_AmalSegment` | TField |  | Amalgamation Segment |
| 27 | `UKDDMP.DDO.DIR.RESERVED` | `UkddmpDdoDirectory_Reserved` | TField |  | Reserved |
| 28 | `UKDDMP.DDO.DIR.PADDER.REC` | `UkddmpDdoDirectory_PadderRec` | TField |  | Padder record |
| 29 | `UKDDMP.DDO.DIR.ACC.RECORD.TYPE` | `UkddmpDdoDirectory_AccRecordType` |  |  |  |
| 30 | `UKDDMP.DDO.DIR.ACC.LAST.AMENDED.DATE` | `UkddmpDdoDirectory_AccLastAmendedDate` |  |  |  |
| 31 | `UKDDMP.DDO.DIR.ACC.SUN` | `UkddmpDdoDirectory_AccSun` |  |  |  |
| 32 | `UKDDMP.DDO.DIR.ACC.SORT.CODE` | `UkddmpDdoDirectory_AccSortCode` |  |  |  |
| 33 | `UKDDMP.DDO.DIR.ACCOUNT.TYPE` | `UkddmpDdoDirectory_AccountType` |  |  |  |
| 34 | `UKDDMP.DDO.DIR.ACCOUNT.NAME` | `UkddmpDdoDirectory_AccountName` |  |  |  |
| 35 | `UKDDMP.DDO.DIR.ACC.PADDER.REC` | `UkddmpDdoDirectory_AccPadderRec` |  |  |  |
| 36 | `UKDDMP.DDO.DIR.LOCAL.REF` | `UkddmpDdoDirectory_LocalRef` |  |  |  |
| 37 | `UKDDMP.DDO.DIR.RESERVED.1` | `UkddmpDdoDirectory_Reserved1` | TField |  |  |
| 38 | `UKDDMP.DDO.DIR.RESERVED.2` | `UkddmpDdoDirectory_Reserved2` | TField |  |  |
| 39 | `UKDDMP.DDO.DIR.RESERVED.3` | `UkddmpDdoDirectory_Reserved3` | TField |  |  |
| 40 | `UKDDMP.DDO.DIR.RESERVED.4` | `UkddmpDdoDirectory_Reserved4` | TField |  |  |
| 41 | `UKDDMP.DDO.DIR.RESERVED.5` | `UkddmpDdoDirectory_Reserved5` | TField |  |  |
| 42 | `UKDDMP.DDO.DIR.RECORD.STATUS` | `UkddmpDdoDirectory_RecordStatus` | String |  |  |
| 43 | `UKDDMP.DDO.DIR.CURR.NO` | `UkddmpDdoDirectory_CurrNo` | String |  |  |
| 44 | `UKDDMP.DDO.DIR.INPUTTER` | `UkddmpDdoDirectory_Inputter` |  |  |  |
| 45 | `UKDDMP.DDO.DIR.DATE.TIME` | `UkddmpDdoDirectory_DateTime` |  |  |  |
| 46 | `UKDDMP.DDO.DIR.AUTHORISER` | `UkddmpDdoDirectory_Authoriser` | String |  |  |
| 47 | `UKDDMP.DDO.DIR.CO.CODE` | `UkddmpDdoDirectory_CoCode` | String |  |  |
| 48 | `UKDDMP.DDO.DIR.DEPT.CODE` | `UkddmpDdoDirectory_DeptCode` | String |  |  |
| 49 | `UKDDMP.DDO.DIR.AUDITOR.CODE` | `UkddmpDdoDirectory_AuditorCode` | String |  |  |
| 50 | `UKDDMP.DDO.DIR.AUDIT.DATE.TIME` | `UkddmpDdoDirectory_AuditDateTime` | String |  |  |
