# ENQUIRY.SELECT — Table Schema

> Source: `INSERTS/I_F.ENQUIRY.SELECT` in `EB_Reports.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ESAV.SELECTION.TYPE` | `EnquirySelect_SelectionType` |  |  |  |
| 2 | `ESAV.SELECTION.FIELD` | `EnquirySelect_SelectionField` |  |  |  |
| 3 | `ESAV.OPERAND` | `EnquirySelect_Operand` |  |  |  |
| 4 | `ESAV.LIST` | `EnquirySelect_List` |  |  |  |
| 5 | `ESAV.ENQUIRY` | `EnquirySelect_Enquiry` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 6 | `ESAV.PRE.SET.SELECTION` | `EnquirySelect_PreSetSelection` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 7 | `ESAV.BACKGROUND` | `EnquirySelect_Background` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 8 | `ESAV.NOTIFY` | `EnquirySelect_Notify` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 9 | `ESAV.SORT.FIELD` | `EnquirySelect_SortField` |  |  |  |
| 10 | `ESAV.FIXED.SELECTION` | `EnquirySelect_FixedSelection` |  |  |  |
| 11 | `ESAV.FIXED.SORT` | `EnquirySelect_FixedSort` |  |  |  |
| 12 | `ESAV.PRINT` | `EnquirySelect_Print` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 13 | `ESAV.NO.SORT.OPTION` | `EnquirySelect_NoSortOption` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 14 | `ESAV.RECORD.STATUS` | `EnquirySelect_RecordStatus` | String |  |  |
| 15 | `ESAV.CURR.NO` | `EnquirySelect_CurrNo` | String |  |  |
| 16 | `ESAV.INPUTTER` | `EnquirySelect_Inputter` |  |  |  |
| 17 | `ESAV.DATE.TIME` | `EnquirySelect_DateTime` |  |  |  |
| 18 | `ESAV.AUTHORISER` | `EnquirySelect_Authoriser` | String |  |  |
| 19 | `ESAV.CO.CODE` | `EnquirySelect_CoCode` | String |  |  |
| 20 | `ESAV.DEPT.CODE` | `EnquirySelect_DeptCode` | String |  |  |
| 21 | `ESAV.AUDITOR.CODE` | `EnquirySelect_AuditorCode` | String |  |  |
| 22 | `ESAV.AUDIT.DATE.TIME` | `EnquirySelect_AuditDateTime` | String |  |  |
