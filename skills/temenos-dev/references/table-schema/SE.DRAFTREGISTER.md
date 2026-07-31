# SE.DRAFTREGISTER — Table Schema

> Source: `INSERTS/I_F.SE.DRAFTREGISTER` in `SE_ModelBank.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DRR.DESCRIPTION` | `SeDraftregister_Description` |  |  |  |
| 2 | `DRR.CUSTOMER` | `SeDraftregister_Customer` | TField |  |  |
| 3 | `DRR.CATEGORY` | `SeDraftregister_Category` | TField |  |  |
| 4 | `DRR.DRAFT.TYPE` | `SeDraftregister_DraftType` | TField |  |  |
| 5 | `DRR.DRAFT.CHARGE` | `SeDraftregister_DraftCharge` | TField |  |  |
| 6 | `DRR.DRAFT.REVIEW.FREQUENCY` | `SeDraftregister_DraftReviewFrequency` | TField |  |  |
| 7 | `DRR.ACCOUNT` | `SeDraftregister_Account` | TField |  |  |
| 8 | `DRR.CURRENCY` | `SeDraftregister_Currency` | TField |  |  |
| 9 | `DRR.AVAIL.DRAFT.AMT` | `SeDraftregister_AvailDraftAmt` | TField |  |  |
| 10 | `DRR.START.DATE` | `SeDraftregister_StartDate` | TField |  |  |
| 11 | `DRR.END.DATE` | `SeDraftregister_EndDate` | TField |  |  |
| 12 | `DRR.MAX.DRAFTS` | `SeDraftregister_MaxDrafts` | TField |  |  |
| 13 | `DRR.DRAFT.ISSUE.CUSTOMERS` | `SeDraftregister_DraftIssueCustomers` |  |  |  |
| 14 | `DRR.INTEREST.BASIS` | `SeDraftregister_InterestBasis` | TField |  |  |
| 15 | `DRR.EXCHANGE.RATE` | `SeDraftregister_ExchangeRate` | TField |  |  |
| 16 | `DRR.NOTES` | `SeDraftregister_Notes` |  |  |  |
| 17 | `DRR.DRAFT.DATE` | `SeDraftregister_DraftDate` |  |  |  |
| 18 | `DRR.DRAFT.NUMBER` | `SeDraftregister_DraftNumber` |  |  |  |
| 19 | `DRR.DRAFT.ISSUE.TO` | `SeDraftregister_DraftIssueTo` |  |  |  |
| 20 | `DRR.DRAFT.AMOUNT` | `SeDraftregister_DraftAmount` |  |  |  |
| 21 | `DRR.OTHER.OFFICER` | `SeDraftregister_OtherOfficer` |  |  |  |
| 22 | `DRR.LOCAL.REF` | `SeDraftregister_LocalRef` |  |  |  |
| 23 | `DRR.STMT.NOS` | `SeDraftregister_StmtNos` |  |  |  |
| 24 | `DRR.OVERRIDE` | `SeDraftregister_Override` |  |  |  |
| 25 | `DRR.RECORD.STATUS` | `SeDraftregister_RecordStatus` | String |  |  |
| 26 | `DRR.CURR.NO` | `SeDraftregister_CurrNo` | String |  |  |
| 27 | `DRR.INPUTTER` | `SeDraftregister_Inputter` |  |  |  |
| 28 | `DRR.DATE.TIME` | `SeDraftregister_DateTime` |  |  |  |
| 29 | `DRR.AUTHORISER` | `SeDraftregister_Authoriser` | String |  |  |
| 30 | `DRR.CO.CODE` | `SeDraftregister_CoCode` | String |  |  |
| 31 | `DRR.DEPT.CODE` | `SeDraftregister_DeptCode` | String |  |  |
| 32 | `DRR.AUDITOR.CODE` | `SeDraftregister_AuditorCode` | String |  |  |
| 33 | `DRR.AUDIT.DATE.TIME` | `SeDraftregister_AuditDateTime` | String |  |  |
