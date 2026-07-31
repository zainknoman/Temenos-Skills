# AUOBPZ.PARAMETER — Table Schema

> Source: `INSERTS/I_F.AUOBPZ.PARAMETER` in `AUOBPZ_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AUOBPZ.ORGANISATION.TYPE` | `AuobpzParameter_OrganisationType` |  |  |  |
| 2 | `AUOBPZ.SECTOR.START` | `AuobpzParameter_SectorStart` |  |  |  |
| 3 | `AUOBPZ.SECTOR.END` | `AuobpzParameter_SectorEnd` |  |  |  |
| 4 | `AUOBPZ.PERSON.SECTOR.END` | `AuobpzParameter_PersonSectorEnd` |  |  |  |
| 5 | `AUOBPZ.DEFAULT.TRANSACTIONS.PERIOD` | `AuobpzParameter_DefaultTransactionsPeriod` | TField |  | The default period for which the transactions will be returned in the Transactions API related response if there is no time period specified in the Request |
| 6 | `AUOBPZ.TRANSACTIONS.MAX.PERIOD` | `AuobpzParameter_TransactionsMaxPeriod` | TField |  | The time period against which the period specified in the request is checked. If the period specified in the request is older than the parameterized period, then the system will not pass the transactions in the response. |
| 7 | `AUOBPZ.OVERLAY.SERVICE` | `AuobpzParameter_OverlayService` | TField |  | The overlay service provided by the bank. |
| 8 | `AUOBPZ.DISPLAY.LENDING.RATE` | `AuobpzParameter_DisplayLendingRate` | TField |  | Flag value to indicate to display the LENDING info. Check the field to view the values related LENDING Details |
| 9 | `AUOBPZ.OVERRIDE` | `AuobpzParameter_Override` |  |  |  |
| 10 | `AUOBPZ.LOCAL.REF` | `AuobpzParameter_LocalRef` |  |  |  |
| 11 | `AUOBPZ.RECORD.STATUS` | `AuobpzParameter_RecordStatus` | String |  |  |
| 12 | `AUOBPZ.CURR.NO` | `AuobpzParameter_CurrNo` | String |  |  |
| 13 | `AUOBPZ.INPUTTER` | `AuobpzParameter_Inputter` |  |  |  |
| 14 | `AUOBPZ.DATE.TIME` | `AuobpzParameter_DateTime` |  |  |  |
| 15 | `AUOBPZ.AUTHORISER` | `AuobpzParameter_Authoriser` | String |  |  |
| 16 | `AUOBPZ.CO.CODE` | `AuobpzParameter_CoCode` | String |  |  |
| 17 | `AUOBPZ.DEPT.CODE` | `AuobpzParameter_DeptCode` | String |  |  |
| 18 | `AUOBPZ.AUDITOR.CODE` | `AuobpzParameter_AuditorCode` | String |  |  |
| 19 | `AUOBPZ.APCA.NUMBER.OUTGOING` | `AuobpzParameter_ApcaNumberOutgoing` | TField |  | 6 Digit APCA number for the initiating institution. Value from the BAAS.CS2.PARAMETER (AU0010001-OUTGOING) > DEFLT.FI.USER. |
| 20 | `AUOBPZ.APCA.NUMBER.INCOMING` | `AuobpzParameter_ApcaNumberIncoming` | TField |  | 6 Digit APCA number for the initiating institution. |
| 21 | `AUOBPZ.PERSON.SECTOR.START` | `AuobpzParameter_PersonSectorStart` |  |  |  |
| 22 | `AUOBPZ.OCCUPATION.CODE.VERSION` | `AuobpzParameter_OccupationCodeVersion` | TField | Yes | The applicable ANZSCO release version of the occupation code provided. Mandatory if an occupationCode is supplied. e.g. ANZSCO_1220.0_2013_V1.2 |
| 23 | `AUOBPZ.INDUSTRY.CODE.VERSION` | `AuobpzParameter_IndustryCodeVersion` | TField |  | The applicable ANZSIC release version of the industry code provided. Should only be supplied if industryCode is also supplied. e.g. ANZSIC_1292.0_2006_V2.0 |
| 24 | `AUOBPZ.CUSTOMER.ROLE` | `AuobpzParameter_CustomerRole` |  |  |  |
| 25 | `AUOBPZ.NOMINATION` | `AuobpzParameter_Nomination` |  |  |  |
| 26 | `AUOBPZ.REPRESENT.OWNER` | `AuobpzParameter_RepresentOwner` |  |  |  |
| 27 | `AUOBPZ.ACCOUNT.TYPE` | `AuobpzParameter_AccountType` |  |  |  |
| 28 | `AUOBPZ.RELATION.ID` | `AuobpzParameter_RelationId` |  |  |  |
| 29 | `AUOBPZ.CUSTOMER.TYPE` | `AuobpzParameter_CustomerType` |  |  |  |
| 30 | `AUOBPZ.PRIMARY.CUSTOMER.ROLE` | `AuobpzParameter_PrimaryCustomerRole` |  |  |  |
| 31 | `AUOBPZ.AUDIT.DATE.TIME` | `AuobpzParameter_AuditDateTime` | String |  |  |
