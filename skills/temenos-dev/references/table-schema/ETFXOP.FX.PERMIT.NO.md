# ETFXOP.FX.PERMIT.NO — Table Schema

> Source: `INSERTS/I_F.ETFXOP.FX.PERMIT.NO` in `ETFXOP_ForexPermit.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ETFXOP.FXPR.FX.PERMIT.NO` | `EtfxopFxPermitNo_FxPermitNo` | TField |  | No input field - Will be updated by the system based on routine logic and selection |
| 2 | `ETFXOP.FXPR.TXN.TYPE` | `EtfxopFxPermitNo_TxnType` | TField |  | Dropdown field with the following values, 01 � Import Goods 02 � Export Goods 03 � Imp Services 05 � Small Items Export |
| 3 | `ETFXOP.FXPR.CUST.ID` | `EtfxopFxPermitNo_CustId` | TField |  | T24 Customer ID to be provided. |
| 4 | `ETFXOP.FXPR.FXPN.ISSUE.DATE` | `EtfxopFxPermitNo_FxpnIssueDate` | TField |  | NoInput Field. Date on which the FX permit number is issued to be displayed. Defaulted to TODAY. |
| 5 | `ETFXOP.FXPR.FXPN.EXPIRY.DATE` | `EtfxopFxPermitNo_FxpnExpiryDate` | TField |  | Date on which the FX permit is expiring. Auto populated based on the days defined in Parameter table. |
| 6 | `ETFXOP.FXPR.FCY.CCY` | `EtfxopFxPermitNo_FcyCcy` | TField |  | To accept a valid currency code. Vetted to Currency table. |
| 7 | `ETFXOP.FXPR.FCY.AMOUNT` | `EtfxopFxPermitNo_FcyAmount` | TField |  | If Foreign Currency is selected then Foreign currency amount to be entered. |
| 8 | `ETFXOP.FXPR.BEN.NAME` | `EtfxopFxPermitNo_BenName` | TField |  | To store the Exporter Name |
| 9 | `ETFXOP.FXPR.TYPE.OF.PAYMENT` | `EtfxopFxPermitNo_TypeOfPayment` | TField |  | Drop drown � Values of LC, CAD � Cash against doc, ADV Payment, Consignment, Small Items |
| 10 | `ETFXOP.FXPR.COMM.INV.NO` | `EtfxopFxPermitNo_CommInvNo` | TField | Yes | To be mandatory if TYPE.OF.PAYMENT EQ �CAD� |
| 11 | `ETFXOP.FXPR.DEST.COUNTRY` | `EtfxopFxPermitNo_DestCountry` |  |  |  |
| 12 | `ETFXOP.FXPR.CANCEL.REASON` | `EtfxopFxPermitNo_CancelReason` | TField |  | To capture the cancellation reason when cancelling Forex permit number. |
| 13 | `ETFXOP.FXPR.STATUS` | `EtfxopFxPermitNo_Status` | TField |  | Will display the status of Forex Permit Number |
| 14 | `ETFXOP.FXPR.RESERVED.1` | `EtfxopFxPermitNo_Reserved1` | TField |  |  |
| 15 | `ETFXOP.FXPR.RESERVED.2` | `EtfxopFxPermitNo_Reserved2` | TField |  |  |
| 16 | `ETFXOP.FXPR.RESERVED.3` | `EtfxopFxPermitNo_Reserved3` | TField |  |  |
| 17 | `ETFXOP.FXPR.RESERVED.4` | `EtfxopFxPermitNo_Reserved4` | TField |  |  |
| 18 | `ETFXOP.FXPR.RESERVED.5` | `EtfxopFxPermitNo_Reserved5` | TField |  |  |
| 19 | `ETFXOP.FXPR.RESERVED.6` | `EtfxopFxPermitNo_Reserved6` | TField |  |  |
| 20 | `ETFXOP.FXPR.RESERVED.7` | `EtfxopFxPermitNo_Reserved7` | TField |  |  |
| 21 | `ETFXOP.FXPR.RESERVED.8` | `EtfxopFxPermitNo_Reserved8` | TField |  |  |
| 22 | `ETFXOP.FXPR.RESERVED.9` | `EtfxopFxPermitNo_Reserved9` | TField |  |  |
| 23 | `ETFXOP.FXPR.RESERVED.10` | `EtfxopFxPermitNo_Reserved10` | TField |  |  |
| 24 | `ETFXOP.FXPR.LOCAL.REF` | `EtfxopFxPermitNo_LocalRef` |  |  |  |
| 25 | `ETFXOP.FXPR.OVERRIDE` | `EtfxopFxPermitNo_Override` |  |  |  |
| 26 | `ETFXOP.FXPR.RECORD.STATUS` | `EtfxopFxPermitNo_RecordStatus` | String |  |  |
| 27 | `ETFXOP.FXPR.CURR.NO` | `EtfxopFxPermitNo_CurrNo` | String |  |  |
| 28 | `ETFXOP.FXPR.INPUTTER` | `EtfxopFxPermitNo_Inputter` |  |  |  |
| 29 | `ETFXOP.FXPR.DATE.TIME` | `EtfxopFxPermitNo_DateTime` |  |  |  |
| 30 | `ETFXOP.FXPR.AUTHORISER` | `EtfxopFxPermitNo_Authoriser` | String |  |  |
| 31 | `ETFXOP.FXPR.CO.CODE` | `EtfxopFxPermitNo_CoCode` | String |  |  |
| 32 | `ETFXOP.FXPR.DEPT.CODE` | `EtfxopFxPermitNo_DeptCode` | String |  |  |
| 33 | `ETFXOP.FXPR.AUDITOR.CODE` | `EtfxopFxPermitNo_AuditorCode` | String |  |  |
| 34 | `ETFXOP.FXPR.AUDIT.DATE.TIME` | `EtfxopFxPermitNo_AuditDateTime` | String |  |  |
