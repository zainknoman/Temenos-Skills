# ST.PROXY.PARAMETER — Table Schema

> Source: `INSERTS/I_F.ST.PROXY.PARAMETER` in `ST_AliasManagement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ST.PRP.FINAL.STATUS` | `StProxyParameter_FinalStatus` |  |  |  |
| 2 | `ST.PRP.INITIAL.STATUS` | `StProxyParameter_InitialStatus` | TField | Yes | Initial status which will be populated when a new record is created. Mandatory Input. |
| 3 | `ST.PRP.MANUAL.DECISION.STATUS` | `StProxyParameter_ManualDecisionStatus` | TField | Yes | Status to be used in proxy record when the indicator field does not point to a next status field, indicating that the proxy record required manual intervention. Mandatory Input. |
| 4 | `ST.PRP.EXPOSED.PROXY.STATUS` | `StProxyParameter_ExposedProxyStatus` |  |  |  |
| 5 | `ST.PRP.ACTIVE.STATUS` | `StProxyParameter_ActiveStatus` | TField |  | Proxies with this status must be re-confirmed periodically, if the Confirmation Frequency is defined. If the proxy directories reaches this status then the date on which the directory reaches this status must be updated in the ACTIVATION.DATE field. |
| 6 | `ST.PRP.CONFIRMATION.BASE.DATE` | `StProxyParameter_ConfirmationBaseDate` | TField | Yes | Indicates the starting point to calculate Next Confirm Deadline in that record. Mandatory if Confirmation frequency is defined. |
| 7 | `ST.PRP.CONFIRMATION.FREQUENCY` | `StProxyParameter_ConfirmationFrequency` | TField |  | Frequency when the proxy must be reconfirmed of its ownership. Amendment will not be effected for the existing proxy directories and will be applicable for the proxy directories created henceforth. |
| 8 | `ST.PRP.CONFIRMATION.PERIOD` | `StProxyParameter_ConfirmationPeriod` | TField |  | Period when the customer needs to re-confirm the proxy, in advance of the next confirmation deadline. |
| 9 | `ST.PRP.DDA.TYPE` | `StProxyParameter_DdaType` | TField | No | Optional field to indicate that the account used as proxy could be either a valid T24 account or an external account Valid value - EXTERNAL EXTERNAL - The account fields in ST.PROXY.DIRECTORY will accept an external reference and there will not be any validation against core table NULL - The account fields in ST.PROXY.DIRECTORY will accept a valid account or an alternate reference The value of this field can be changed from External to blank, e.g. when the bank has migrated all their accounts in the Temenos Core Banking In this case system would raise validation error during of the amendment of proxy links created for an external account since with the option being blank, system expects the account to be valid in T24 |
| 10 | `ST.PRP.RESERVED09` | `StProxyParameter_Reserved09` | TField |  |  |
| 11 | `ST.PRP.RESERVED08` | `StProxyParameter_Reserved08` | TField |  |  |
| 12 | `ST.PRP.RESERVED07` | `StProxyParameter_Reserved07` | TField |  |  |
| 13 | `ST.PRP.RESERVED06` | `StProxyParameter_Reserved06` | TField |  |  |
| 14 | `ST.PRP.RESERVED05` | `StProxyParameter_Reserved05` | TField |  |  |
| 15 | `ST.PRP.RESERVED04` | `StProxyParameter_Reserved04` | TField |  |  |
| 16 | `ST.PRP.RESERVED03` | `StProxyParameter_Reserved03` | TField |  |  |
| 17 | `ST.PRP.RESERVED02` | `StProxyParameter_Reserved02` | TField |  |  |
| 18 | `ST.PRP.RESERVED01` | `StProxyParameter_Reserved01` | TField |  |  |
| 19 | `ST.PRP.LOCAL.REF` | `StProxyParameter_LocalRef` |  |  |  |
| 20 | `ST.PRP.OVERRIDE` | `StProxyParameter_Override` |  |  |  |
| 21 | `ST.PRP.RECORD.STATUS` | `StProxyParameter_RecordStatus` | String |  |  |
| 22 | `ST.PRP.CURR.NO` | `StProxyParameter_CurrNo` | String |  |  |
| 23 | `ST.PRP.INPUTTER` | `StProxyParameter_Inputter` |  |  |  |
| 24 | `ST.PRP.DATE.TIME` | `StProxyParameter_DateTime` |  |  |  |
| 25 | `ST.PRP.AUTHORISER` | `StProxyParameter_Authoriser` | String |  |  |
| 26 | `ST.PRP.CO.CODE` | `StProxyParameter_CoCode` | String |  |  |
| 27 | `ST.PRP.DEPT.CODE` | `StProxyParameter_DeptCode` | String |  |  |
| 28 | `ST.PRP.AUDITOR.CODE` | `StProxyParameter_AuditorCode` | String |  |  |
| 29 | `ST.PRP.AUDIT.DATE.TIME` | `StProxyParameter_AuditDateTime` | String |  |  |
