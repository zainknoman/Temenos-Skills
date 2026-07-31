# INLEND.IEC.STATUS — Table Schema

> Source: `INSERTS/I_F.INLEND.IEC.STATUS` in `INDPMS_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `INLEND.IEC.OWN.CUSTOMER` | `InlendIecStatus_OwnCustomer` | TField |  | Own Customer. |
| 2 | `INLEND.IEC.CUSTOMER.ID` | `InlendIecStatus_CustomerId` | TField |  | CUSTOMER ID to Which IE Code is Mapped to. |
| 3 | `INLEND.IEC.EXPORTER.CATEGORY` | `InlendIecStatus_ExporterCategory` | TField |  | A Valid Record From INLEND.EXPORTER.CATEGORY. |
| 4 | `INLEND.IEC.EXPIRY.STATUS.HOLDER` | `InlendIecStatus_ExpiryStatusHolder` | TField |  | Date Until Which Exporter is Categorised as Status Holder. |
| 5 | `INLEND.IEC.IEC.STATUS` | `InlendIecStatus_IecStatus` | TField |  | A Valid Record in INLEND.IEC.STATUS.Allowed Values are CANCELLED,SUSPENDED,ACTIVE and SURRENDERED. |
| 6 | `INLEND.IEC.CAUTION.LIST.STATUS` | `InlendIecStatus_CautionListStatus` |  |  |  |
| 7 | `INLEND.IEC.CAUTION.LIST.STATUS.DATE` | `InlendIecStatus_CautionListStatusDate` |  |  |  |
| 8 | `INLEND.IEC.MODE.OF.DATA` | `InlendIecStatus_ModeOfData` | TField |  | Mode of Data.Allowed Values are UPLOAD/MANUAL |
| 9 | `INLEND.IEC.IE.NAME` | `InlendIecStatus_IeName` |  |  |  |
| 10 | `INLEND.IEC.IE.ADDRESS` | `InlendIecStatus_IeAddress` |  |  |  |
| 11 | `INLEND.IEC.TOTAL.BILLS` | `InlendIecStatus_TotalBills` | TField |  | Number of Bills Outstanding for IE. |
| 12 | `INLEND.IEC.NUMBER.BILLS.OPEN` | `InlendIecStatus_NumberBillsOpen` | TField |  | Number of Bills Open. |
| 13 | `INLEND.IEC.TOTAL.BILL.AMOUNT` | `InlendIecStatus_TotalBillAmount` | TField |  | Total Amount Against Total Number of Bills. |
| 14 | `INLEND.IEC.TOTAL.OPEN.BILL.AMOUNT` | `InlendIecStatus_TotalOpenBillAmount` | TField |  | Total Amount Against Total Number of Open Bills. |
| 15 | `INLEND.IEC.TOTAL.REALIZED.AMT.OPEN.BILL` | `InlendIecStatus_TotalRealizedAmtOpenBill` | TField |  | Total Realized Amount Against Open Bills. |
| 16 | `INLEND.IEC.TOTAL.PNDNG.AMT.OPEN.BILL` | `InlendIecStatus_TotalPndngAmtOpenBill` | TField |  | Total Un-Realized Amount Against Open Bills. |
| 17 | `INLEND.IEC.OPEN.TOTAL.BILL.AMOUNT.PRCNT` | `InlendIecStatus_OpenTotalBillAmountPrcnt` | TField |  | Total Pending Open Bill Amount/Total Bill Amount As a Percentage. |
| 18 | `INLEND.IEC.RESERVED.5` | `InlendIecStatus_Reserved5` | TField |  | Reserved for Future Use. |
| 19 | `INLEND.IEC.RESERVED.4` | `InlendIecStatus_Reserved4` | TField |  | Reserved for Future Use. |
| 20 | `INLEND.IEC.RESERVED.3` | `InlendIecStatus_Reserved3` | TField |  | Reserved for Future Use. |
| 21 | `INLEND.IEC.RESERVED.2` | `InlendIecStatus_Reserved2` | TField |  | Reserved for Future Use. |
| 22 | `INLEND.IEC.RESERVED.1` | `InlendIecStatus_Reserved1` | TField |  | Reserved for Future Use. |
| 23 | `INLEND.IEC.LOCAL.REF` | `InlendIecStatus_LocalRef` |  |  |  |
| 24 | `INLEND.IEC.OVERRIDE` | `InlendIecStatus_Override` |  |  |  |
| 25 | `INLEND.IEC.RECORD.STATUS` | `InlendIecStatus_RecordStatus` | String |  |  |
| 26 | `INLEND.IEC.CURR.NO` | `InlendIecStatus_CurrNo` | String |  |  |
| 27 | `INLEND.IEC.INPUTTER` | `InlendIecStatus_Inputter` |  |  |  |
| 28 | `INLEND.IEC.DATE.TIME` | `InlendIecStatus_DateTime` |  |  |  |
| 29 | `INLEND.IEC.AUTHORISER` | `InlendIecStatus_Authoriser` | String |  |  |
| 30 | `INLEND.IEC.CO.CODE` | `InlendIecStatus_CoCode` | String |  |  |
| 31 | `INLEND.IEC.DEPT.CODE` | `InlendIecStatus_DeptCode` | String |  |  |
| 32 | `INLEND.IEC.AUDITOR.CODE` | `InlendIecStatus_AuditorCode` | String |  |  |
| 33 | `INLEND.IEC.AUDIT.DATE.TIME` | `InlendIecStatus_AuditDateTime` | String |  |  |
