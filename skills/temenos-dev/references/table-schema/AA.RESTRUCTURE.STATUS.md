# AA.RESTRUCTURE.STATUS — Table Schema

> Source: `INSERTS/I_F.AA.RESTRUCTURE.STATUS` in `AA_RestructureRules.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.RS.RESTRUCTURE.STATUS` | `AaRestructureStatus_RestructureStatus` |  |  |  |
| 2 | `AA.RS.DESCRIPTION` | `AaRestructureStatus_Description` |  |  |  |
| 3 | `AA.RS.BOOK.MEMO.LOAN` | `AaRestructureStatus_BookMemoLoan` |  |  |  |
| 4 | `AA.RS.PREVIOUS.STATUS` | `AaRestructureStatus_PreviousStatus` |  |  |  |
| 5 | `AA.RS.RESERVED1` | `AaRestructureStatus_Reserved1` |  |  |  |
| 6 | `AA.RS.RESERVED2` | `AaRestructureStatus_Reserved2` |  |  |  |
| 7 | `AA.RS.MEMO.PRODUCT.TYPE` | `AaRestructureStatus_MemoProductType` | TField |  | This field indicates if Memo/Technical loan product can be created using same product or different product. Allowed values are SAME.PRODUCT and DIFFERENT.PRODUCT. Currently the option &apos;DIFFERENT.PRODUCT&apos; will be defaulted and cannot be modified. The option SAME.PRODUCT is for future usage. |
| 8 | `AA.RS.ALLOCATE.AS.PER.ML` | `AaRestructureStatus_AllocateAsPerMl` | TField |  | Indicates if payment made on Memo(Technical) loan should consider Original Loan or Technical Loan properties for repaying Original Loan. If set to Yes Technical loan properties will be considered, If set to No Original loan properties will be considered. Validation Rules: 1. Allowed only if BookMemoLoan is set to yes |
| 9 | `AA.RS.AUTO.TERMINATE.ML` | `AaRestructureStatus_AutoTerminateMl` | TField | Yes | Indicates if the Memo(Technical)loan should be automatically terminated when original loan is closed. Validation Rules: 1. Non Mandatory field 2. Value is defaulted to yes |
| 10 | `AA.RS.LOCAL.REF` | `AaRestructureStatus_LocalRef` |  |  |  |
| 11 | `AA.RS.OVERRIDE` | `AaRestructureStatus_Override` |  |  |  |
| 12 | `AA.RS.RECORD.STATUS` | `AaRestructureStatus_RecordStatus` | String |  |  |
| 13 | `AA.RS.CURR.NO` | `AaRestructureStatus_CurrNo` | String |  |  |
| 14 | `AA.RS.INPUTTER` | `AaRestructureStatus_Inputter` |  |  |  |
| 15 | `AA.RS.DATE.TIME` | `AaRestructureStatus_DateTime` |  |  |  |
| 16 | `AA.RS.AUTHORISER` | `AaRestructureStatus_Authoriser` | String |  |  |
| 17 | `AA.RS.CO.CODE` | `AaRestructureStatus_CoCode` | String |  |  |
| 18 | `AA.RS.DEPT.CODE` | `AaRestructureStatus_DeptCode` | String |  |  |
| 19 | `AA.RS.AUDITOR.CODE` | `AaRestructureStatus_AuditorCode` | String |  |  |
| 20 | `AA.RS.AUDIT.DATE.TIME` | `AaRestructureStatus_AuditDateTime` | String |  |  |
