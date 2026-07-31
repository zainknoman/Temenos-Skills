# PV.CUSTOMER.DETAIL.HIST — Table Schema

> Source: `INSERTS/I_F.PV.CUSTOMER.DETAIL.HIST` in `PV_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PVCDH.MANAGEMENT.ID` | `PvCustomerDetailHist_ManagementId` |  |  |  |
| 2 | `PVCDH.PROFILE.ID` | `PvCustomerDetailHist_ProfileId` |  |  |  |
| 3 | `PVCDH.LAST.CLASS.DATE` | `PvCustomerDetailHist_LastClassDate` |  |  |  |
| 4 | `PVCDH.AUTO.CLASS` | `PvCustomerDetailHist_AutoClass` |  |  |  |
| 5 | `PVCDH.MANUAL.CLASS` | `PvCustomerDetailHist_ManualClass` |  |  |  |
| 6 | `PVCDH.REASON` | `PvCustomerDetailHist_Reason` |  |  |  |
| 7 | `PVCDH.PR.CLASS.DTE` | `PvCustomerDetailHist_PrClassDte` |  |  |  |
| 8 | `PVCDH.PR.AUTO.CLASS` | `PvCustomerDetailHist_PrAutoClass` |  |  |  |
| 9 | `PVCDH.PR.MAN.CLASS` | `PvCustomerDetailHist_PrManClass` |  |  |  |
| 10 | `PVCDH.PR.REASON` | `PvCustomerDetailHist_PrReason` |  |  |  |
| 11 | `PVCDH.SEQ.NO` | `PvCustomerDetailHist_SeqNo` | TField |  | Latest Sequence Number that is used to create PV.CUSTOMER.DETAIL.HIST |
| 12 | `PVCDH.SEQUENCE.DATE` | `PvCustomerDetailHist_SequenceDate` | TField |  | The date after which the details are moved from Prev fields to PV.CUSTOMER.DETAIL.HIST |
| 13 | `PVCDH.PROB.OF.DEFT` | `PvCustomerDetailHist_ProbOfDeft` |  |  |  |
| 14 | `PVCDH.LOSS.GIVEN.DEFT` | `PvCustomerDetailHist_LossGivenDeft` | TField |  | Facilitate the option to the bank to configure the Loss given Default (LGD) at the customer level in IFRS 9 impairment Model. Validation Rules: Input enabled only when I9 installed. Accepts number or percentage depending on the values defined on LGD.VAL.FMT field of IFRS Parameter. |
| 15 | `PVCDH.CUSTOMER.CONTRACT` | `PvCustomerDetailHist_CustomerContract` |  |  |  |
| 16 | `PVCDH.ASSET.AUTO.CLASS` | `PvCustomerDetailHist_AssetAutoClass` |  |  |  |
| 17 | `PVCDH.JOINT.FLAG` | `PvCustomerDetailHist_JointFlag` |  |  |  |
| 18 | `PVCDH.CUSTOMER.ID` | `PvCustomerDetailHist_CustomerId` |  |  |  |
| 19 | `PVCDH.CONTAGION.DATE` | `PvCustomerDetailHist_ContagionDate` | TField |  | This field holds the date when the Obligor Contagion processing happened and the Contagion status was updated Validation Rules: NoInput Field |
| 20 | `PVCDH.CONTAGION.CLASS` | `PvCustomerDetailHist_ContagionClass` | TField |  | This field is used to capture the Contagion class after Obligor Contagion processing Validation Rules: NoInput Field |
| 21 | `PVCDH.LOCAL.REF` | `PvCustomerDetailHist_LocalRef` |  |  |  |
| 22 | `PVCDH.OVERRIDE` | `PvCustomerDetailHist_Override` |  |  |  |
| 23 | `PVCDH.CONTAGION.STATUS` | `PvCustomerDetailHist_ContagionStatus` | TField |  | This field is used to capture the Contagion Status (DEFAULT/PERFORMING) after Obligor Contagion processing Validation Rules: NoInput Field |
