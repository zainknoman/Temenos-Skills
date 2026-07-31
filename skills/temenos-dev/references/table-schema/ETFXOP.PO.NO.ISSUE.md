# ETFXOP.PO.NO.ISSUE — Table Schema

> Source: `INSERTS/I_F.ETFXOP.PO.NO.ISSUE` in `ETFXOP_ForexPermit.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ETFXOP.PONO.PO.NUMBER` | `EtfxopPoNoIssue_PoNumber` | TField |  | No Input Field.Will be updated by the system based on routine logic. |
| 2 | `ETFXOP.PONO.CUST.ID` | `EtfxopPoNoIssue_CustId` | TField |  | Input field.T24 Customer ID to be provided. |
| 3 | `ETFXOP.PONO.IMPORTER.NAME` | `EtfxopPoNoIssue_ImporterName` | TField |  | Input Field. Importer Name to be captured |
| 4 | `ETFXOP.PONO.SUPPLIER.NAME` | `EtfxopPoNoIssue_SupplierName` | TField |  | Input Field. Exporter Name to be captured |
| 5 | `ETFXOP.PONO.DESC.OF.GOODS` | `EtfxopPoNoIssue_DescOfGoods` | TField |  | Input Field. Description of Goods. |
| 6 | `ETFXOP.PONO.GOODS.QTY` | `EtfxopPoNoIssue_GoodsQty` | TField |  | Input Field. Quantity of goods to be captured. |
| 7 | `ETFXOP.PONO.FCY.CCY` | `EtfxopPoNoIssue_FcyCcy` | TField |  | Input Field. To accept a valid currency code. Vetted to Currency table. |
| 8 | `ETFXOP.PONO.FCY.AMOUNT` | `EtfxopPoNoIssue_FcyAmount` | TField |  | Input Field. If Foreign Currency is selected then Foreign currency amount to be entered. |
| 9 | `ETFXOP.PONO.PO.ISSUE.DATE` | `EtfxopPoNoIssue_PoIssueDate` | TField |  | Date on which the PO number is issued to be displayed. Defaulted to TODAY. |
| 10 | `ETFXOP.PONO.PROFORMA.INV.NO` | `EtfxopPoNoIssue_ProformaInvNo` | TField |  | Input Field. Proforma Invoice to be updated. |
| 11 | `ETFXOP.PONO.PO.EXPIRY.DATE` | `EtfxopPoNoIssue_PoExpiryDate` | TField |  | Date on which the PO is expiring. Auto populated based on the days defined in Parameter table. |
| 12 | `ETFXOP.PONO.COMMITTEE.APPRVL.DATE` | `EtfxopPoNoIssue_CommitteeApprvlDate` | TField |  | Input Field. Date on which the Fund Manager approves the PO |
| 13 | `ETFXOP.PONO.CANCEL.REASON` | `EtfxopPoNoIssue_CancelReason` | TField |  | To capture the reason of cancellation when Purchase order is cancelled. |
| 14 | `ETFXOP.PONO.STATUS` | `EtfxopPoNoIssue_Status` | TField |  | No Input Field.Will display the status of PO number. |
| 15 | `ETFXOP.PONO.RESERVED.1` | `EtfxopPoNoIssue_Reserved1` | TField |  |  |
| 16 | `ETFXOP.PONO.RESERVED.2` | `EtfxopPoNoIssue_Reserved2` | TField |  |  |
| 17 | `ETFXOP.PONO.RESERVED.3` | `EtfxopPoNoIssue_Reserved3` | TField |  |  |
| 18 | `ETFXOP.PONO.RESERVED.4` | `EtfxopPoNoIssue_Reserved4` | TField |  |  |
| 19 | `ETFXOP.PONO.RESERVED.5` | `EtfxopPoNoIssue_Reserved5` | TField |  |  |
| 20 | `ETFXOP.PONO.RESERVED.6` | `EtfxopPoNoIssue_Reserved6` | TField |  |  |
| 21 | `ETFXOP.PONO.RESERVED.7` | `EtfxopPoNoIssue_Reserved7` | TField |  |  |
| 22 | `ETFXOP.PONO.RESERVED.8` | `EtfxopPoNoIssue_Reserved8` | TField |  |  |
| 23 | `ETFXOP.PONO.RESERVED.9` | `EtfxopPoNoIssue_Reserved9` | TField |  |  |
| 24 | `ETFXOP.PONO.RESERVED.10` | `EtfxopPoNoIssue_Reserved10` | TField |  |  |
| 25 | `ETFXOP.PONO.LOCAL.REF` | `EtfxopPoNoIssue_LocalRef` |  |  |  |
| 26 | `ETFXOP.PONO.OVERRIDE` | `EtfxopPoNoIssue_Override` |  |  |  |
| 27 | `ETFXOP.PONO.RECORD.STATUS` | `EtfxopPoNoIssue_RecordStatus` | String |  |  |
| 28 | `ETFXOP.PONO.CURR.NO` | `EtfxopPoNoIssue_CurrNo` | String |  |  |
| 29 | `ETFXOP.PONO.INPUTTER` | `EtfxopPoNoIssue_Inputter` |  |  |  |
| 30 | `ETFXOP.PONO.DATE.TIME` | `EtfxopPoNoIssue_DateTime` |  |  |  |
| 31 | `ETFXOP.PONO.AUTHORISER` | `EtfxopPoNoIssue_Authoriser` | String |  |  |
| 32 | `ETFXOP.PONO.CO.CODE` | `EtfxopPoNoIssue_CoCode` | String |  |  |
| 33 | `ETFXOP.PONO.DEPT.CODE` | `EtfxopPoNoIssue_DeptCode` | String |  |  |
| 34 | `ETFXOP.PONO.AUDITOR.CODE` | `EtfxopPoNoIssue_AuditorCode` | String |  |  |
| 35 | `ETFXOP.PONO.AUDIT.DATE.TIME` | `EtfxopPoNoIssue_AuditDateTime` | String |  |  |
