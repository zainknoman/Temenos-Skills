# PV.CUSTOMER.DETAIL — Table Schema

> Source: `INSERTS/I_F.PV.CUSTOMER.DETAIL` in `PV_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PVCD.MANAGEMENT.ID` | `PvCustomerDetail_ManagementId` |  |  |  |
| 2 | `PVCD.PROFILE.ID` | `PvCustomerDetail_ProfileId` |  |  |  |
| 3 | `PVCD.LAST.CLASS.DATE` | `PvCustomerDetail_LastClassDate` |  |  |  |
| 4 | `PVCD.AUTO.CLASS` | `PvCustomerDetail_AutoClass` |  |  |  |
| 5 | `PVCD.MANUAL.CLASS` | `PvCustomerDetail_ManualClass` |  |  |  |
| 6 | `PVCD.REASON` | `PvCustomerDetail_Reason` |  |  |  |
| 7 | `PVCD.PR.CLASS.DTE` | `PvCustomerDetail_PrClassDte` |  |  |  |
| 8 | `PVCD.PR.AUTO.CLASS` | `PvCustomerDetail_PrAutoClass` |  |  |  |
| 9 | `PVCD.PR.MAN.CLASS` | `PvCustomerDetail_PrManClass` |  |  |  |
| 10 | `PVCD.PR.REASON` | `PvCustomerDetail_PrReason` |  |  |  |
| 11 | `PVCD.SEQ.NO` | `PvCustomerDetail_SeqNo` | TField |  | Latest Sequence Number that is used to create PV.CUSTOMER.DETAIL.HIST |
| 12 | `PVCD.SEQUENCE.DATE` | `PvCustomerDetail_SequenceDate` | TField |  | The date after which the details are moved from Prev fields to PV.CUSTOMER.DETAIL.HIST |
| 13 | `PVCD.PROB.OF.DEFT` | `PvCustomerDetail_ProbOfDeft` |  |  |  |
| 14 | `PVCD.LOSS.GIVEN.DEFT` | `PvCustomerDetail_LossGivenDeft` | TField |  | Facilitate the option to the bank to configure the Loss given Default (LGD) at the customer level in IFRS 9 impairment Model. Validation Rules: Input enabled only when I9 installed. Accepts number or percentage depending on the values defined on LGD.VAL.FMT field of IFRS Parameter. |
| 15 | `PVCD.CUSTOMER.CONTRACT` | `PvCustomerDetail_CustomerContract` |  |  |  |
| 16 | `PVCD.ASSET.AUTO.CLASS` | `PvCustomerDetail_AssetAutoClass` |  |  |  |
| 17 | `PVCD.JOINT.FLAG` | `PvCustomerDetail_JointFlag` |  |  |  |
| 18 | `PVCD.CUSTOMER.ID` | `PvCustomerDetail_CustomerId` |  |  |  |
| 19 | `PVCD.CONTAGION.DATE` | `PvCustomerDetail_ContagionDate` | TField |  | This field holds the date when the Obligor Contagion processing happened and the Contagion status was updated Validation Rules: NoInput Field |
| 20 | `PVCD.CONTAGION.CLASS` | `PvCustomerDetail_ContagionClass` | TField |  | This field is used to capture the Contagion class after Obligor Contagion processing Validation Rules: NoInput Field |
| 21 | `PVCD.LOCAL.REF` | `PvCustomerDetail_LocalRef` |  |  |  |
| 22 | `PVCD.OVERRIDE` | `PvCustomerDetail_Override` |  |  |  |
| 23 | `PVCD.RECORD.STATUS` | `PvCustomerDetail_RecordStatus` | String |  |  |
| 24 | `PVCD.CURR.NO` | `PvCustomerDetail_CurrNo` | String |  |  |
| 25 | `PVCD.INPUTTER` | `PvCustomerDetail_Inputter` |  |  |  |
| 26 | `PVCD.DATE.TIME` | `PvCustomerDetail_DateTime` |  |  |  |
| 27 | `PVCD.AUTHORISER` | `PvCustomerDetail_Authoriser` | String |  |  |
| 28 | `PVCD.CO.CODE` | `PvCustomerDetail_CoCode` | String |  |  |
| 29 | `PVCD.DEPT.CODE` | `PvCustomerDetail_DeptCode` | String |  |  |
| 30 | `PVCD.AUDITOR.CODE` | `PvCustomerDetail_AuditorCode` | String |  |  |
| 31 | `PVCD.AUDIT.DATE.TIME` | `PvCustomerDetail_AuditDateTime` | String |  |  |
| 32 | `PVCD.CONTAGION.STATUS` | `PvCustomerDetail_ContagionStatus` | TField |  | This field is used to capture the Contagion Status (DEFAULT/PERFORMING) after Obligor Contagion processing Validation Rules: NoInput Field |
