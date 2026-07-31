# ETFXOP.FXPN.PO.DETAILS — Table Schema

> Source: `INSERTS/I_F.ETFXOP.FXPN.PO.DETAILS` in `ETFXOP_ForexPermit.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ETFXOP.FXPNO.CUST.ID` | `EtfxopFxpnPoDetails_CustId` | TField |  | Customer ID the customer to whom the Forex permit number or Purchase order number belongs to. |
| 2 | `ETFXOP.FXPNO.FXPN.PO.RECORD.ID` | `EtfxopFxpnPoDetails_FxpnPoRecordId` | TField |  | Contains the Record ID of Forex permit or Purchase Order number table |
| 3 | `ETFXOP.FXPNO.REF.NUMBER` | `EtfxopFxpnPoDetails_RefNumber` |  |  |  |
| 4 | `ETFXOP.FXPNO.FXPN.OS.AMOUNT` | `EtfxopFxpnPoDetails_FxpnOsAmount` | TField |  | This is the Outstanding value of FX permit if the FX permit is used. |
| 5 | `ETFXOP.FXPNO.PO.OS.AMOUNT` | `EtfxopFxpnPoDetails_PoOsAmount` | TField |  | To store the outstanding value of PO. |
| 6 | `ETFXOP.FXPNO.UNAUTH.AMOUNT` | `EtfxopFxpnPoDetails_UnauthAmount` | TField |  | Unauthorised amount is stored in the live table after committing the record and cleared upon authorization. |
| 7 | `ETFXOP.FXPNO.COLL.REF` | `EtfxopFxpnPoDetails_CollRef` |  |  |  |
| 8 | `ETFXOP.FXPNO.COLL.AMT` | `EtfxopFxpnPoDetails_CollAmt` |  |  |  |
| 9 | `ETFXOP.FXPNO.FXPN.PERMIT.NO` | `EtfxopFxpnPoDetails_FxpnPermitNo` |  |  |  |
| 10 | `ETFXOP.FXPNO.STATUS` | `EtfxopFxpnPoDetails_Status` | TField |  | Active,Inactive,Cancelled |
| 11 | `ETFXOP.FXPNO.RESERVED.1` | `EtfxopFxpnPoDetails_Reserved1` | TField |  |  |
| 12 | `ETFXOP.FXPNO.RESERVED.2` | `EtfxopFxpnPoDetails_Reserved2` | TField |  |  |
| 13 | `ETFXOP.FXPNO.RESERVED.3` | `EtfxopFxpnPoDetails_Reserved3` | TField |  |  |
| 14 | `ETFXOP.FXPNO.RESERVED.4` | `EtfxopFxpnPoDetails_Reserved4` | TField |  |  |
| 15 | `ETFXOP.FXPNO.RESERVED.5` | `EtfxopFxpnPoDetails_Reserved5` | TField |  |  |
| 16 | `ETFXOP.FXPNO.RESERVED.6` | `EtfxopFxpnPoDetails_Reserved6` | TField |  |  |
| 17 | `ETFXOP.FXPNO.RESERVED.7` | `EtfxopFxpnPoDetails_Reserved7` | TField |  |  |
| 18 | `ETFXOP.FXPNO.RESERVED.8` | `EtfxopFxpnPoDetails_Reserved8` | TField |  |  |
| 19 | `ETFXOP.FXPNO.RESERVED.9` | `EtfxopFxpnPoDetails_Reserved9` | TField |  |  |
| 20 | `ETFXOP.FXPNO.RESERVED.10` | `EtfxopFxpnPoDetails_Reserved10` | TField |  |  |
