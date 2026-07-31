# FICOLL.SECONDARY.PLEDGE.DETAILS — Table Schema

> Source: `INSERTS/I_F.FICOLL.SECONDARY.PLEDGE.DETAILS` in `FICOLL_Collateral.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FICOLL.PLEDGE.TYPE` | `FicollSecondaryPledgeDetails_Type` | TField |  | This field is of radio button type which has 2 values namely, 1) Secondary Pledge 2) Bearer Bond. Validation Rules: 1) When Secondary pledge is chosen a validation is required to check that the @id of this table is equal to the collateral id of the Bearer bond. 2) When Bearer Bond is chosen a validation is required to check that the @id of this table is equal to the underlying Asset id. When this field is chosen, the following fields are no-input field,Deed id, Deed amount, Deed from amount, Deed to amount. |
| 2 | `FICOLL.PLEDGE.ISSUE.DATE` | `FicollSecondaryPledgeDetails_IssueDate` |  |  |  |
| 3 | `FICOLL.PLEDGE.BENEFICIARY.NONCUST` | `FicollSecondaryPledgeDetails_BeneficiaryNoncust` |  |  |  |
| 4 | `FICOLL.PLEDGE.REGISTER.NUMBER` | `FicollSecondaryPledgeDetails_RegisterNumber` |  |  |  |
| 5 | `FICOLL.PLEDGE.ACTUAL.PLEDGE.AMOUNT` | `FicollSecondaryPledgeDetails_ActualPledgeAmount` |  |  |  |
| 6 | `FICOLL.PLEDGE.FROM.AMOUNT` | `FicollSecondaryPledgeDetails_FromAmount` |  |  |  |
| 7 | `FICOLL.PLEDGE.TO.AMOUNT` | `FicollSecondaryPledgeDetails_ToAmount` |  |  |  |
| 8 | `FICOLL.PLEDGE.UPDATE.THIRD.PARTY.VALUE` | `FicollSecondaryPledgeDetails_UpdateThirdPartyValue` |  |  |  |
| 9 | `FICOLL.PLEDGE.DEED.ID` | `FicollSecondaryPledgeDetails_DeedId` |  |  |  |
| 10 | `FICOLL.PLEDGE.DEED.AMOUNT` | `FicollSecondaryPledgeDetails_DeedAmount` |  |  |  |
| 11 | `FICOLL.PLEDGE.DEED.FROM.AMOUNT` | `FicollSecondaryPledgeDetails_DeedFromAmount` |  |  |  |
| 12 | `FICOLL.PLEDGE.DEED.TO.AMOUNT` | `FicollSecondaryPledgeDetails_DeedToAmount` |  |  |  |
| 13 | `FICOLL.PLEDGE.LOCAL.REF` | `FicollSecondaryPledgeDetails_LocalRef` |  |  |  |
| 14 | `FICOLL.PLEDGE.OVERRIDE` | `FicollSecondaryPledgeDetails_Override` |  |  |  |
| 15 | `FICOLL.PLEDGE.RECORD.STATUS` | `FicollSecondaryPledgeDetails_RecordStatus` | String |  |  |
| 16 | `FICOLL.PLEDGE.CURR.NO` | `FicollSecondaryPledgeDetails_CurrNo` | String |  |  |
| 17 | `FICOLL.PLEDGE.INPUTTER` | `FicollSecondaryPledgeDetails_Inputter` |  |  |  |
| 18 | `FICOLL.PLEDGE.DATE.TIME` | `FicollSecondaryPledgeDetails_DateTime` |  |  |  |
| 19 | `FICOLL.PLEDGE.AUTHORISER` | `FicollSecondaryPledgeDetails_Authoriser` | String |  |  |
| 20 | `FICOLL.PLEDGE.CO.CODE` | `FicollSecondaryPledgeDetails_CoCode` | String |  |  |
| 21 | `FICOLL.PLEDGE.DEPT.CODE` | `FicollSecondaryPledgeDetails_DeptCode` | String |  |  |
| 22 | `FICOLL.PLEDGE.AUDITOR.CODE` | `FicollSecondaryPledgeDetails_AuditorCode` | String |  |  |
| 23 | `FICOLL.PLEDGE.AUDIT.DATE.TIME` | `FicollSecondaryPledgeDetails_AuditDateTime` | String |  |  |
