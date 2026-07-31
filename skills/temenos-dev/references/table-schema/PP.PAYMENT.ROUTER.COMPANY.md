# PP.PAYMENT.ROUTER.COMPANY — Table Schema

> Source: `INSERTS/I_F.PP.PAYMENT.ROUTER.COMPANY` in `PP_PaymentRouterService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.PRC.CompanyID` | `PpPaymentRouterCompany_Companyid` | TField |  | Indicates the company ID for which the record is created. It is NOINPUT field. On click of validate button, Company ID gets autopopulated from PP Company. Examples: BNK,GB1 Validation Rules: 3 alphanumeric characters. |
| 2 | `PP.PRC.RESERVED.5` | `PpPaymentRouterCompany_Reserved5` | TField |  | Standard T24 String. No Input Field |
| 3 | `PP.PRC.RESERVED.4` | `PpPaymentRouterCompany_Reserved4` | TField |  | Standard T24 String. No Input Field |
| 4 | `PP.PRC.RESERVED.3` | `PpPaymentRouterCompany_Reserved3` | TField |  | Standard T24 String. No Input Field |
| 5 | `PP.PRC.RESERVED.2` | `PpPaymentRouterCompany_Reserved2` | TField |  | Standard T24 String. No Input Field |
| 6 | `PP.PRC.RESERVED.1` | `PpPaymentRouterCompany_Reserved1` | TField |  | Standard T24 String. No Input Field |
| 7 | `PP.PRC.LOCAL.REF` | `PpPaymentRouterCompany_LocalRef` |  |  |  |
| 8 | `PP.PRC.OVERRIDE` | `PpPaymentRouterCompany_Override` |  |  |  |
| 9 | `PP.PRC.RECORD.STATUS` | `PpPaymentRouterCompany_RecordStatus` | String |  |  |
| 10 | `PP.PRC.CURR.NO` | `PpPaymentRouterCompany_CurrNo` | String |  |  |
| 11 | `PP.PRC.INPUTTER` | `PpPaymentRouterCompany_Inputter` |  |  |  |
| 12 | `PP.PRC.DATE.TIME` | `PpPaymentRouterCompany_DateTime` |  |  |  |
| 13 | `PP.PRC.AUTHORISER` | `PpPaymentRouterCompany_Authoriser` | String |  |  |
| 14 | `PP.PRC.CO.CODE` | `PpPaymentRouterCompany_CoCode` | String |  |  |
| 15 | `PP.PRC.DEPT.CODE` | `PpPaymentRouterCompany_DeptCode` | String |  |  |
| 16 | `PP.PRC.AUDITOR.CODE` | `PpPaymentRouterCompany_AuditorCode` | String |  |  |
| 17 | `PP.PRC.AUDIT.DATE.TIME` | `PpPaymentRouterCompany_AuditDateTime` | String |  |  |
