# ETFXOP.PARAMETER — Table Schema

> Source: `INSERTS/I_F.ETFXOP.PARAMETER` in `ETFXOP_ForexPermit.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ETFXOP.PRMT.FXPN.IM.LC.VALID.DAYS` | `EtfxopParameter_FxpnImLcValidDays` | TField |  | Defines the validity for Import of Goods and services (LC). Accepts Values in Calendar days. |
| 2 | `ETFXOP.PRMT.FXPN.IM.COLL.VALID.DAYS` | `EtfxopParameter_FxpnImCollValidDays` | TField |  | Defines the validity for Import of Goods and services (Collections). Accepts Values in Calendar days. |
| 3 | `ETFXOP.PRMT.FXPN.IM.ADV.VALID.DAYS` | `EtfxopParameter_FxpnImAdvValidDays` | TField |  | Defines the validity for Import of Goods and services for Advance payment. Accepts Values in Calendar days. |
| 4 | `ETFXOP.PRMT.FXPN.EX.VALID.DAYS` | `EtfxopParameter_FxpnExValidDays` | TField |  | Defines the validity for Export of Goods and services. Accepts Values in Calendar days. |
| 5 | `ETFXOP.PRMT.PO.VALID.DAYS` | `EtfxopParameter_PoValidDays` | TField |  | Defines the validity period for Purchase Order. Accepts Values in Calendar days. |
| 6 | `ETFXOP.PRMT.BANK.CODE` | `EtfxopParameter_BankCode` | TField |  | Bank Code is a 3 digit code which forms the part of the Forex Permit Number and Purchase Order Number. Bank is expected to define this constant value as the first 3 digits of the Forex Permit Number and Purchase Order Number. |
| 7 | `ETFXOP.PRMT.RESERVED.1` | `EtfxopParameter_Reserved1` | TField |  |  |
| 8 | `ETFXOP.PRMT.RESERVED.2` | `EtfxopParameter_Reserved2` | TField |  |  |
| 9 | `ETFXOP.PRMT.RESERVED.3` | `EtfxopParameter_Reserved3` | TField |  |  |
| 10 | `ETFXOP.PRMT.RESERVED.4` | `EtfxopParameter_Reserved4` | TField |  |  |
| 11 | `ETFXOP.PRMT.RESERVED.5` | `EtfxopParameter_Reserved5` | TField |  |  |
| 12 | `ETFXOP.PRMT.RESERVED.6` | `EtfxopParameter_Reserved6` | TField |  |  |
| 13 | `ETFXOP.PRMT.RESERVED.7` | `EtfxopParameter_Reserved7` | TField |  |  |
| 14 | `ETFXOP.PRMT.RESERVED.8` | `EtfxopParameter_Reserved8` | TField |  |  |
| 15 | `ETFXOP.PRMT.RESERVED.9` | `EtfxopParameter_Reserved9` | TField |  |  |
| 16 | `ETFXOP.PRMT.RESERVED.10` | `EtfxopParameter_Reserved10` | TField |  |  |
| 17 | `ETFXOP.PRMT.LOCAL.REF` | `EtfxopParameter_LocalRef` |  |  |  |
| 18 | `ETFXOP.PRMT.OVERRIDE` | `EtfxopParameter_Override` |  |  |  |
| 19 | `ETFXOP.PRMT.RECORD.STATUS` | `EtfxopParameter_RecordStatus` | String |  |  |
| 20 | `ETFXOP.PRMT.CURR.NO` | `EtfxopParameter_CurrNo` | String |  |  |
| 21 | `ETFXOP.PRMT.INPUTTER` | `EtfxopParameter_Inputter` |  |  |  |
| 22 | `ETFXOP.PRMT.DATE.TIME` | `EtfxopParameter_DateTime` |  |  |  |
| 23 | `ETFXOP.PRMT.AUTHORISER` | `EtfxopParameter_Authoriser` | String |  |  |
| 24 | `ETFXOP.PRMT.CO.CODE` | `EtfxopParameter_CoCode` | String |  |  |
| 25 | `ETFXOP.PRMT.DEPT.CODE` | `EtfxopParameter_DeptCode` | String |  |  |
| 26 | `ETFXOP.PRMT.AUDITOR.CODE` | `EtfxopParameter_AuditorCode` | String |  |  |
| 27 | `ETFXOP.PRMT.AUDIT.DATE.TIME` | `EtfxopParameter_AuditDateTime` | String |  |  |
