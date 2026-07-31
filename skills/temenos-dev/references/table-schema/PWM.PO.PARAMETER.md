# PWM.PO.PARAMETER — Table Schema

> Source: `INSERTS/I_F.PWM.PO.PARAMETER` in `SC_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `WM.POPARAM.ACCT.TRANS.PO` | `PwmPoParameter_AcctTransPo` | TField |  | This field is to decide whether to generate a payment order or follow the traditional way of settlement foraccount transfers. A value Yes signifies PO will be generated for Account transfers and a value No signifies the existing logic forsettlement. Validations Allowed Values - YES or NO |
| 2 | `WM.POPARAM.PO.PRODUCT` | `PwmPoParameter_PoProduct` | TField |  | This field will hold a valid PAYMENT.ORDER.PRODUCT that will be supported by Securities, Derrivatives and Structure Product modules. |
| 3 | `WM.POPARAM.PO.APPLICATION` | `PwmPoParameter_PoApplication` |  |  |  |
| 4 | `WM.POPARAM.PO.SUSP.CATEG` | `PwmPoParameter_PoSuspCateg` |  |  |  |
| 5 | `WM.POPARAM.PO.SUSP.TXN.CODE` | `PwmPoParameter_PoSuspTxnCode` |  |  |  |
| 6 | `WM.POPARAM.ORDER.INITIATION.TYPE` | `PwmPoParameter_OrderInitiationType` |  |  |  |
| 7 | `WM.POPARAM.PAYMENT.CATEGORY` | `PwmPoParameter_PaymentCategory` |  |  |  |
| 8 | `WM.POPARAM.PAYMENT.METHOD` | `PwmPoParameter_PaymentMethod` |  |  |  |
| 9 | `WM.POPARAM.PAYMENT.PURPOSE` | `PwmPoParameter_PaymentPurpose` |  |  |  |
| 10 | `WM.POPARAM.PO.VERSION` | `PwmPoParameter_PoVersion` |  |  |  |
| 11 | `WM.POPARAM.MV.RESERVED01` | `PwmPoParameter_MvReserved01` |  |  |  |
| 12 | `WM.POPARAM.MV.RESERVED02` | `PwmPoParameter_MvReserved02` |  |  |  |
| 13 | `WM.POPARAM.MV.RESERVED03` | `PwmPoParameter_MvReserved03` |  |  |  |
| 14 | `WM.POPARAM.MV.RESERVED04` | `PwmPoParameter_MvReserved04` |  |  |  |
| 15 | `WM.POPARAM.MV.RESERVED05` | `PwmPoParameter_MvReserved05` |  |  |  |
| 16 | `WM.POPARAM.RESERVED01` | `PwmPoParameter_Reserved01` | TField |  |  |
| 17 | `WM.POPARAM.RESERVED02` | `PwmPoParameter_Reserved02` | TField |  |  |
| 18 | `WM.POPARAM.RESERVED03` | `PwmPoParameter_Reserved03` | TField |  |  |
| 19 | `WM.POPARAM.RESERVED04` | `PwmPoParameter_Reserved04` | TField |  |  |
| 20 | `WM.POPARAM.RESERVED05` | `PwmPoParameter_Reserved05` | TField |  |  |
| 21 | `WM.POPARAM.LOCAL.REF` | `PwmPoParameter_LocalRef` |  |  |  |
| 22 | `WM.POPARAM.OVERRIDE` | `PwmPoParameter_Override` |  |  |  |
| 23 | `WM.POPARAM.RECORD.STATUS` | `PwmPoParameter_RecordStatus` | String |  |  |
| 24 | `WM.POPARAM.CURR.NO` | `PwmPoParameter_CurrNo` | String |  |  |
| 25 | `WM.POPARAM.INPUTTER` | `PwmPoParameter_Inputter` |  |  |  |
| 26 | `WM.POPARAM.DATE.TIME` | `PwmPoParameter_DateTime` |  |  |  |
| 27 | `WM.POPARAM.AUTHORISER` | `PwmPoParameter_Authoriser` | String |  |  |
| 28 | `WM.POPARAM.CO.CODE` | `PwmPoParameter_CoCode` | String |  |  |
| 29 | `WM.POPARAM.DEPT.CODE` | `PwmPoParameter_DeptCode` | String |  |  |
| 30 | `WM.POPARAM.AUDITOR.CODE` | `PwmPoParameter_AuditorCode` | String |  |  |
| 31 | `WM.POPARAM.AUDIT.DATE.TIME` | `PwmPoParameter_AuditDateTime` | String |  |  |
