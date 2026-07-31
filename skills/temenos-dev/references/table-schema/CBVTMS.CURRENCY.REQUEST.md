# CBVTMS.CURRENCY.REQUEST — Table Schema

> Source: `INSERTS/I_F.CBVTMS.CURRENCY.REQUEST` in `CBVTMS_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `VTMS.REQUEST.TYPE` | `CbvtmsCurrencyRequest_RequestType` | TField |  | The type of request has to be captured like Ordering Currency, withdrawal and deposit. |
| 2 | `VTMS.REQUESTED.SOURCE` | `CbvtmsCurrencyRequest_RequestedSource` | TField |  | This should be if the request is raised by manual,swift or external screen. |
| 3 | `VTMS.REQUEST.STATUS` | `CbvtmsCurrencyRequest_RequestStatus` | TField |  | The current status of the request like New, send to printer, cancelled and processed. |
| 4 | `VTMS.ENTITY.TYPE` | `CbvtmsCurrencyRequest_EntityType` | TField |  |  |
| 5 | `VTMS.REQUESTED.BY.TO` | `CbvtmsCurrencyRequest_RequestedByTo` | TField |  | The details of the request raised by the commercial bank. |
| 6 | `VTMS.REQUEST.DATE` | `CbvtmsCurrencyRequest_RequestDate` | TField |  | The date on which the request is raised. |
| 7 | `VTMS.REQUEST.TIME` | `CbvtmsCurrencyRequest_RequestTime` | TField |  | This will capture the request time. |
| 8 | `VTMS.AMEND.DATE` | `CbvtmsCurrencyRequest_AmendDate` | TField |  | Date on which the amendment of the request is done. |
| 9 | `VTMS.AMEND.TIME` | `CbvtmsCurrencyRequest_AmendTime` | TField |  | Time on which the amendment was made. |
| 10 | `VTMS.SCHEDULE.DATE` | `CbvtmsCurrencyRequest_ScheduleDate` | TField |  | The date on which the denomination is requested for deposit or withdrawal. |
| 11 | `VTMS.AUTHORISER.ID` | `CbvtmsCurrencyRequest_AuthoriserId` |  |  |  |
| 12 | `VTMS.CURRENCY` | `CbvtmsCurrencyRequest_Currency` | TField |  | The currency in which the request raised for ordering or withdrawal or deposit. |
| 13 | `VTMS.TOTAL.VALUE` | `CbvtmsCurrencyRequest_TotalValue` | TField |  | The total value for which the request is raised. |
| 14 | `VTMS.CARTON.DETAILS` | `CbvtmsCurrencyRequest_CartonDetails` |  |  |  |
| 15 | `VTMS.NO.OF.CARTON` | `CbvtmsCurrencyRequest_NoOfCarton` |  |  |  |
| 16 | `VTMS.DENOMINATION` | `CbvtmsCurrencyRequest_Denomination` |  |  |  |
| 17 | `VTMS.LOCAL.REF` | `CbvtmsCurrencyRequest_LocalRef` |  |  |  |
| 18 | `VTMS.RESERVED.5` | `CbvtmsCurrencyRequest_Reserved5` | TField |  | Reserved field for future use |
| 19 | `VTMS.RESERVED.4` | `CbvtmsCurrencyRequest_Reserved4` | TField |  | Reserved field for future use |
| 20 | `VTMS.RESERVED.3` | `CbvtmsCurrencyRequest_Reserved3` | TField |  | Reserved field for future use |
| 21 | `VTMS.RESERVED.2` | `CbvtmsCurrencyRequest_Reserved2` | TField |  | Reserved field for future use |
| 22 | `VTMS.RESERVED.1` | `CbvtmsCurrencyRequest_Reserved1` | TField |  | Reserved field for future use |
| 23 | `VTMS.OVERRIDE` | `CbvtmsCurrencyRequest_Override` |  |  |  |
| 24 | `VTMS.RECORD.STATUS` | `CbvtmsCurrencyRequest_RecordStatus` | String |  |  |
| 25 | `VTMS.CURR.NO` | `CbvtmsCurrencyRequest_CurrNo` | String |  |  |
| 26 | `VTMS.INPUTTER` | `CbvtmsCurrencyRequest_Inputter` |  |  |  |
| 27 | `VTMS.DATE.TIME` | `CbvtmsCurrencyRequest_DateTime` |  |  |  |
| 28 | `VTMS.AUTHORISER` | `CbvtmsCurrencyRequest_Authoriser` | String |  |  |
| 29 | `VTMS.CO.CODE` | `CbvtmsCurrencyRequest_CoCode` | String |  |  |
| 30 | `VTMS.DEPT.CODE` | `CbvtmsCurrencyRequest_DeptCode` | String |  |  |
| 31 | `VTMS.AUDITOR.CODE` | `CbvtmsCurrencyRequest_AuditorCode` | String |  |  |
| 32 | `VTMS.AUDIT.DATE.TIME` | `CbvtmsCurrencyRequest_AuditDateTime` | String |  |  |
