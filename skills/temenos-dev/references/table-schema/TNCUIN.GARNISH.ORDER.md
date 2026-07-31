# TNCUIN.GARNISH.ORDER — Table Schema

> Source: `INSERTS/I_F.TNCUIN.GARNISH.ORDER` in `TNCUIN_Garnishment.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TNCUIN.GARNISH.ORDER.ORDER.DATE` | `TncuinGarnishOrder_OrderDate` | TField |  | This field stores the date on when the Garnishment order is raised/created by the Bailiff. Format- DD/MM/YYYY |
| 2 | `TNCUIN.GARNISH.ORDER.NOTIFICATION.DATE` | `TncuinGarnishOrder_NotificationDate` | TField |  | This field stores the date on when the Garnishment order is received by the bank. This date should not be lesser than the DATE.ORDER. format is DD/MM/YYYY |
| 3 | `TNCUIN.GARNISH.ORDER.BAILIFF.NAME` | `TncuinGarnishOrder_BailiffName` |  |  |  |
| 4 | `TNCUIN.GARNISH.ORDER.LEGAL.DOC.NAME` | `TncuinGarnishOrder_LegalDocName` | TField |  | This field stores the type of the Legal Document which is updated in the Garnishment order |
| 5 | `TNCUIN.GARNISH.ORDER.LEGAL.ID` | `TncuinGarnishOrder_LegalId` | TField |  | This field stores the Legal ID of the customer which is updated in the garnishment order received |
| 6 | `TNCUIN.GARNISH.ORDER.GARNISH.CCY` | `TncuinGarnishOrder_GarnishCcy` | TField |  | This field stores the Currency in which the customer owes the fund to the creditor. Vetted with CURRENCY application |
| 7 | `TNCUIN.GARNISH.ORDER.GARNISH.AMT` | `TncuinGarnishOrder_GarnishAmt` | TField |  | This field stores the amount which the customer owes to the creditor |
| 8 | `TNCUIN.GARNISH.ORDER.GARNISH.STATUS` | `TncuinGarnishOrder_GarnishStatus` | TField |  | This field stores the status of the Garnishment order.Below are the values:(1) Garnishment Created(2) Case in progress(3) Judgement of Release(4) Payment Order Judgement(5) Judgement in suspension |
| 9 | `TNCUIN.GARNISH.ORDER.JUDGEMENT` | `TncuinGarnishOrder_Judgement` | TField |  | This field stores the Judgement received from the court for the Garnishment order |
| 10 | `TNCUIN.GARNISH.ORDER.LOCAL.REF` | `TncuinGarnishOrder_LocalRef` |  |  |  |
| 11 | `TNCUIN.GARNISH.ORDER.GLOBAL.CCY` | `TncuinGarnishOrder_GlobalCcy` |  |  |  |
| 12 | `TNCUIN.GARNISH.ORDER.GLOBAL.AMT` | `TncuinGarnishOrder_GlobalAmt` |  |  |  |
| 13 | `TNCUIN.GARNISH.ORDER.REPORT.TYPE` | `TncuinGarnishOrder_ReportType` | TField |  | This field stores the type of the Report received bythe bank. Below are the possible values to beconfigurable in EB.LOOKUP:(1) Garnishment(2) Opposition Administrative(3) Requisition |
| 14 | `TNCUIN.GARNISH.ORDER.NOTIFICATION.TYPE` | `TncuinGarnishOrder_NotificationType` | TField |  | This field stores the type of the Notification received.The values are configurable in EB.LOOKUP andpossible values are:If the REPORT.TYPE is Garnishment the followingvalues are applicable (better to restrict the dropdownrather than having a validation) :(1) Garnishment(2) Protective Garnishment(3) Salary Garnishment If the REPORT.TYPE is Opposition Administrativethe following values are applicable:(4) Opposition(5) Rent Opposition(6) Social Funds Opposition If the REPORT.TYPE is Requisition the followingvalues are applicable:(7) Information Request(8) Posting Restriction(9) Release Posting Restriction(10)Transfer to Authority |
| 15 | `TNCUIN.GARNISH.ORDER.EXCLUDE.ACCOUNT` | `TncuinGarnishOrder_ExcludeAccount` |  |  |  |
| 16 | `TNCUIN.GARNISH.ORDER.OVERRIDE` | `TncuinGarnishOrder_Override` |  |  |  |
| 17 | `TNCUIN.GARNISH.ORDER.RECORD.STATUS` | `TncuinGarnishOrder_RecordStatus` | String |  |  |
| 18 | `TNCUIN.GARNISH.ORDER.CURR.NO` | `TncuinGarnishOrder_CurrNo` | String |  |  |
| 19 | `TNCUIN.GARNISH.ORDER.INPUTTER` | `TncuinGarnishOrder_Inputter` |  |  |  |
| 20 | `TNCUIN.GARNISH.ORDER.DATE.TIME` | `TncuinGarnishOrder_DateTime` |  |  |  |
| 21 | `TNCUIN.GARNISH.ORDER.AUTHORISER` | `TncuinGarnishOrder_Authoriser` | String |  |  |
| 22 | `TNCUIN.GARNISH.ORDER.CO.CODE` | `TncuinGarnishOrder_CoCode` | String |  |  |
| 23 | `TNCUIN.GARNISH.ORDER.DEPT.CODE` | `TncuinGarnishOrder_DeptCode` | String |  |  |
| 24 | `TNCUIN.GARNISH.ORDER.AUDITOR.CODE` | `TncuinGarnishOrder_AuditorCode` | String |  |  |
| 25 | `TNCUIN.GARNISH.ORDER.AUDIT.DATE.TIME` | `TncuinGarnishOrder_AuditDateTime` | String |  |  |
| 26 | `TNCUIN.GARNISH.ORDER.JUDGE.SUMMON.LEVEL` | `TncuinGarnishOrder_JudgeSummonLevel` |  |  |  |
| 27 | `TNCUIN.GARNISH.ORDER.JUDGE.SUMMON.COURT` | `TncuinGarnishOrder_JudgeSummonCourt` |  |  |  |
| 28 | `TNCUIN.GARNISH.ORDER.JUDGE.SUMMON.DETAILS` | `TncuinGarnishOrder_JudgeSummonDetails` |  |  |  |
| 29 | `TNCUIN.GARNISH.ORDER.JUDGE.SUMMON.DATE` | `TncuinGarnishOrder_JudgeSummonDate` |  |  |  |
| 30 | `TNCUIN.GARNISH.ORDER.JUDGE.SUMMON.REF` | `TncuinGarnishOrder_JudgeSummonRef` |  |  |  |
| 31 | `TNCUIN.GARNISH.ORDER.JUDGE.HEAR.DATE` | `TncuinGarnishOrder_JudgeHearDate` |  |  |  |
| 32 | `TNCUIN.GARNISH.ORDER.JUDGE.SUMMON.BAILIFF` | `TncuinGarnishOrder_JudgeSummonBailiff` |  |  |  |
| 33 | `TNCUIN.GARNISH.ORDER.JUDGE.SUMMON.TRIAL.NUMBER` | `TncuinGarnishOrder_JudgeSummonTrialNumber` |  |  |  |
| 34 | `TNCUIN.GARNISH.ORDER.EXTERNAL.ORDER.NUMBER` | `TncuinGarnishOrder_ExternalOrderNumber` | TField |  | This is the Requisition Order Number, assigned bythe legal authority, as written on the received order.Input is allowed in this field only if theREPORT.TYPE is Requisition or else it will be a no input field. |
| 35 | `TNCUIN.GARNISH.ORDER.INTERNAL.ORDER.NUMBER` | `TncuinGarnishOrder_InternalOrderNumber` | TField |  | This is the internal Requisition order number, asdecided by the bank. Input is allowed in this field onlyif the REPORT.TYPE is Requisition or else it will bea no input field |
| 36 | `TNCUIN.GARNISH.ORDER.REQUESTER` | `TncuinGarnishOrder_Requester` | TField |  | This field is to capture the Requester details. Input isallowed in this field only if the REPORT.TYPE isRequisition or else it will be a no-input field. |
| 37 | `TNCUIN.GARNISH.ORDER.ASSET.TYPE` | `TncuinGarnishOrder_AssetType` |  |  |  |
| 38 | `TNCUIN.GARNISH.ORDER.ASSET.DESCRIPTION` | `TncuinGarnishOrder_AssetDescription` |  |  |  |
| 39 | `TNCUIN.GARNISH.ORDER.ASSET.AMOUNT` | `TncuinGarnishOrder_AssetAmount` |  |  |  |
| 40 | `TNCUIN.GARNISH.ORDER.CREDITOR.NAME` | `TncuinGarnishOrder_CreditorName` |  |  |  |
| 41 | `TNCUIN.GARNISH.ORDER.SIMPLE.RELEASE.NUMBER` | `TncuinGarnishOrder_SimpleReleaseNumber` |  |  |  |
| 42 | `TNCUIN.GARNISH.ORDER.SIMPLE.RELEASE.DATE` | `TncuinGarnishOrder_SimpleReleaseDate` |  |  |  |
| 43 | `TNCUIN.GARNISH.ORDER.RELEASE.BAILIFF.NAME` | `TncuinGarnishOrder_ReleaseBailiffName` |  |  |  |
| 44 | `TNCUIN.GARNISH.ORDER.CUSTOMER.NUMBER` | `TncuinGarnishOrder_CustomerNumber` | TField |  |  |
| 45 | `TNCUIN.GARNISH.ORDER.FIRST.NAME` | `TncuinGarnishOrder_FirstName` |  |  |  |
| 46 | `TNCUIN.GARNISH.ORDER.LAST.NAME` | `TncuinGarnishOrder_LastName` |  |  |  |
| 47 | `TNCUIN.GARNISH.ORDER.FATHER.LAST.NAME` | `TncuinGarnishOrder_FatherLastName` |  |  |  |
