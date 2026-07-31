# CZ.CDP.PRODUCT — Table Schema

> Source: `INSERTS/I_F.CZ.CDP.PRODUCT` in `CZ_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CDP.PRD.SYS.DESC` | `CzCdpProduct_SysDesc` | TField | Yes | A short description on the System that is included in the CDP Architecture. Validation Rule: Alphanumeric characters of length upto 100. Mandatory field |
| 2 | `CDP.PRD.SYS.STATUS` | `CzCdpProduct_SysStatus` | TField | Yes | Current status of the system in the CDP Architecture. Options allowed - ACTIVE,INACTIVE If a system is newly added and is active, the status would be ACTIVE If a system is removed the status will have to be updated as INACTIVE Validation Rule: Mandatory field |
| 3 | `CDP.PRD.CUST.STATUS.CHECK` | `CzCdpProduct_CustStatusCheck` | TField |  |  |
| 4 | `CDP.PRD.EXT.PARTY.ID.SYS` | `CzCdpProduct_ExtPartyIdSys` | TField |  | This field hold the External system from which the PartyId is to be fetched. Validation Rule : Allowed Values are PARTYMS(PartyID) and DBX(Digital Profile ID) |
| 5 | `CDP.PRD.RESERVED.18` | `CzCdpProduct_Reserved18` | TField |  |  |
| 6 | `CDP.PRD.RESERVED.17` | `CzCdpProduct_Reserved17` | TField |  |  |
| 7 | `CDP.PRD.RESERVED.16` | `CzCdpProduct_Reserved16` | TField |  |  |
| 8 | `CDP.PRD.RESERVED.15` | `CzCdpProduct_Reserved15` | TField |  |  |
| 9 | `CDP.PRD.RESERVED.14` | `CzCdpProduct_Reserved14` | TField |  |  |
| 10 | `CDP.PRD.RESERVED.13` | `CzCdpProduct_Reserved13` | TField |  |  |
| 11 | `CDP.PRD.RESERVED.12` | `CzCdpProduct_Reserved12` | TField |  |  |
| 12 | `CDP.PRD.RESERVED.11` | `CzCdpProduct_Reserved11` | TField |  |  |
| 13 | `CDP.PRD.RESERVED.10` | `CzCdpProduct_Reserved10` | TField |  |  |
| 14 | `CDP.PRD.RESERVED.09` | `CzCdpProduct_Reserved09` | TField |  |  |
| 15 | `CDP.PRD.RESERVED.08` | `CzCdpProduct_Reserved08` | TField |  |  |
| 16 | `CDP.PRD.RESERVED.07` | `CzCdpProduct_Reserved07` | TField |  |  |
| 17 | `CDP.PRD.RESERVED.06` | `CzCdpProduct_Reserved06` | TField |  |  |
| 18 | `CDP.PRD.RESERVED.05` | `CzCdpProduct_Reserved05` | TField |  |  |
| 19 | `CDP.PRD.RESERVED.04` | `CzCdpProduct_Reserved04` | TField |  |  |
| 20 | `CDP.PRD.RESERVED.03` | `CzCdpProduct_Reserved03` | TField |  |  |
| 21 | `CDP.PRD.RESERVED.02` | `CzCdpProduct_Reserved02` | TField |  |  |
| 22 | `CDP.PRD.RESERVED.01` | `CzCdpProduct_Reserved01` | TField |  |  |
| 23 | `CDP.PRD.LOCAL.REF` | `CzCdpProduct_LocalRef` |  |  |  |
| 24 | `CDP.PRD.OVERRIDE` | `CzCdpProduct_Override` |  |  |  |
| 25 | `CDP.PRD.RECORD.STATUS` | `CzCdpProduct_RecordStatus` | String |  |  |
| 26 | `CDP.PRD.CURR.NO` | `CzCdpProduct_CurrNo` | String |  |  |
| 27 | `CDP.PRD.INPUTTER` | `CzCdpProduct_Inputter` |  |  |  |
| 28 | `CDP.PRD.DATE.TIME` | `CzCdpProduct_DateTime` |  |  |  |
| 29 | `CDP.PRD.AUTHORISER` | `CzCdpProduct_Authoriser` | String |  |  |
| 30 | `CDP.PRD.CO.CODE` | `CzCdpProduct_CoCode` | String |  |  |
| 31 | `CDP.PRD.DEPT.CODE` | `CzCdpProduct_DeptCode` | String |  |  |
| 32 | `CDP.PRD.AUDITOR.CODE` | `CzCdpProduct_AuditorCode` | String |  |  |
| 33 | `CDP.PRD.AUDIT.DATE.TIME` | `CzCdpProduct_AuditDateTime` | String |  |  |
