# CHEQUE.RETURN — Table Schema

> Source: `INSERTS/I_F.CHEQUE.RETURN` in `CQ_ChqSubmit.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CHRE.TRANSACTION.REF` | `ChequeReturn_TransactionRef` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 2 | `CHRE.CHEQUE.NUMBER` | `ChequeReturn_ChequeNumber` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 3 | `CHRE.CHEQUE.TYPE` | `ChequeReturn_ChequeType` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 4 | `CHRE.ACCOUNT.NO` | `ChequeReturn_AccountNo` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 5 | `CHRE.CURRENCY` | `ChequeReturn_Currency` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 6 | `CHRE.RETURN.REJECT.CODE` | `ChequeReturn_ReturnRejectCode` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 7 | `CHRE.RETURN.REJECT.REASON` | `ChequeReturn_ReturnRejectReason` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 8 | `CHRE.RETURN.DATE` | `ChequeReturn_ReturnDate` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 9 | `CHRE.COMMENT` | `ChequeReturn_Comment` |  |  |  |
| 10 | `CHRE.RETURN.SOURCE` | `ChequeReturn_ReturnSource` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 11 | `CHRE.DRAWER.ACCOUNT` | `ChequeReturn_DrawerAccount` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 12 | `CHRE.RETURN.COUNT` | `ChequeReturn_ReturnCount` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 13 | `CHRE.INCR.RETURN.CNT` | `ChequeReturn_IncrReturnCnt` | TField | No | Optional. The field provides the user with option of whether return count needs to be incremented or not, in Cheque Register Supplement, for a cheque return request. Valid values are No/Blank. Default is Blank. The flag should be set to NO if the Cheque Return Request is to rectify Reject reason code, populated earlier due to operational errors. If not set, then the request is considered as a normal return request and return count is updated in Cheque Register Supplement. |
| 14 | `CHRE.RESERVED.4` | `ChequeReturn_Reserved4` | TField |  |  |
| 15 | `CHRE.RESERVED.3` | `ChequeReturn_Reserved3` | TField |  |  |
| 16 | `CHRE.RESERVED.2` | `ChequeReturn_Reserved2` | TField |  |  |
| 17 | `CHRE.RESERVED.1` | `ChequeReturn_Reserved1` | TField |  |  |
| 18 | `CHRE.LOCAL.REF` | `ChequeReturn_LocalRef` |  |  |  |
| 19 | `CHRE.OVERRIDE` | `ChequeReturn_Override` |  |  |  |
| 20 | `CHRE.RECORD.STATUS` | `ChequeReturn_RecordStatus` | String |  |  |
| 21 | `CHRE.CURR.NO` | `ChequeReturn_CurrNo` | String |  |  |
| 22 | `CHRE.INPUTTER` | `ChequeReturn_Inputter` |  |  |  |
| 23 | `CHRE.DATE.TIME` | `ChequeReturn_DateTime` |  |  |  |
| 24 | `CHRE.AUTHORISER` | `ChequeReturn_Authoriser` | String |  |  |
| 25 | `CHRE.CO.CODE` | `ChequeReturn_CoCode` | String |  |  |
| 26 | `CHRE.DEPT.CODE` | `ChequeReturn_DeptCode` | String |  |  |
| 27 | `CHRE.AUDITOR.CODE` | `ChequeReturn_AuditorCode` | String |  |  |
| 28 | `CHRE.AUDIT.DATE.TIME` | `ChequeReturn_AuditDateTime` | String |  |  |
