# SC.PERSONAL.ASSET.TYPE — Table Schema

> Source: `INSERTS/I_F.SC.PERSONAL.ASSET.TYPE` in `SC_SctOtherAssets.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.PAT.DESCRIPTION` | `ScPersonalAssetType_Description` | TField |  | This field will hold the description of the Asset type |
| 2 | `SC.PAT.ASSET.TYPE` | `ScPersonalAssetType_AssetType` | TField |  | This field will hold the ASSET.TYPE to which this SUB.ASSET.TYPE belongs. This will also be the default Asset allocation Noinput field |
| 3 | `SC.PAT.EXPENSE.TAX.TREATMENT` | `ScPersonalAssetType_ExpenseTaxTreatment` | TField |  | This field will hold whether the Expense tax treatment to be performed for this Personal Asset type. The value given here will be defaultedto the respective transaction record for this Personal Asset type. Any one of the following three values can only be input to this field:(DEDUCTIBLE, NOT.DEDUCTIBLE, NOT.APPLICABLE) |
| 4 | `SC.PAT.INCOME.TAX.TREATMENT` | `ScPersonalAssetType_IncomeTaxTreatment` | TField |  | This field will hold whether the Income tax treatment to be performed for this Personal Asset type. The value given here will be defaultedto the respective transaction record for this Personal Asset type. Any one of the following three values can only be input to this field:(ASSESABLE, NON.ASSESABLE, NOT.APPLICABLE) |
| 5 | `SC.PAT.DISPOSAL.TAX.TREATMENT` | `ScPersonalAssetType_DisposalTaxTreatment` | TField |  | This field will hold the type of Disposal tax treatment to be performed for this Personal Asset type. The value given here will be defaultedto the respective transaction record for this Personal Asset type. The disposal tax treatments can be(REVENUE, CG.EXEMPT, SPECIAL, STANDARD.CG) Cannot set "CG.EXEMPT" when liability is set |
| 6 | `SC.PAT.LIABILITY` | `ScPersonalAssetType_Liability` | TField |  | If set to YES, it means that this asset type is a Liability. Eg: Loans. |
| 7 | `SC.PAT.MULTIPLE.LOTS` | `ScPersonalAssetType_MultipleLots` | TField |  | Checking this field will allow multiple credit or debit type of transaction. |
| 8 | `SC.PAT.CG.EXEMPT.VALUE` | `ScPersonalAssetType_CgExemptValue` | TField |  | Standard amount field. This field can be set only if Multiple Lots is not YES. The value here will be assumed to be in Local currency. |
| 9 | `SC.PAT.NO.LOSS.OFFSET` | `ScPersonalAssetType_NoLossOffset` | TField |  |  |
| 10 | `SC.PAT.RESERVED.11` | `ScPersonalAssetType_Reserved11` | TField |  |  |
| 11 | `SC.PAT.RESERVED.10` | `ScPersonalAssetType_Reserved10` | TField |  |  |
| 12 | `SC.PAT.RESERVED.09` | `ScPersonalAssetType_Reserved09` | TField |  |  |
| 13 | `SC.PAT.RESERVED.08` | `ScPersonalAssetType_Reserved08` | TField |  |  |
| 14 | `SC.PAT.RESERVED.07` | `ScPersonalAssetType_Reserved07` | TField |  |  |
| 15 | `SC.PAT.RESERVED.06` | `ScPersonalAssetType_Reserved06` | TField |  |  |
| 16 | `SC.PAT.RESERVED.05` | `ScPersonalAssetType_Reserved05` | TField |  |  |
| 17 | `SC.PAT.RESERVED.04` | `ScPersonalAssetType_Reserved04` | TField |  |  |
| 18 | `SC.PAT.RESERVED.03` | `ScPersonalAssetType_Reserved03` | TField |  |  |
| 19 | `SC.PAT.RESERVED.02` | `ScPersonalAssetType_Reserved02` | TField |  |  |
| 20 | `SC.PAT.RESERVED.01` | `ScPersonalAssetType_Reserved01` | TField |  |  |
| 21 | `SC.PAT.LOCAL.REF` | `ScPersonalAssetType_LocalRef` |  |  |  |
| 22 | `SC.PAT.OVERRIDE` | `ScPersonalAssetType_Override` |  |  |  |
| 23 | `SC.PAT.RECORD.STATUS` | `ScPersonalAssetType_RecordStatus` | String |  |  |
| 24 | `SC.PAT.CURR.NO` | `ScPersonalAssetType_CurrNo` | String |  |  |
| 25 | `SC.PAT.INPUTTER` | `ScPersonalAssetType_Inputter` |  |  |  |
| 26 | `SC.PAT.DATE.TIME` | `ScPersonalAssetType_DateTime` |  |  |  |
| 27 | `SC.PAT.AUTHORISER` | `ScPersonalAssetType_Authoriser` | String |  |  |
| 28 | `SC.PAT.CO.CODE` | `ScPersonalAssetType_CoCode` | String |  |  |
| 29 | `SC.PAT.DEPT.CODE` | `ScPersonalAssetType_DeptCode` | String |  |  |
| 30 | `SC.PAT.AUDITOR.CODE` | `ScPersonalAssetType_AuditorCode` | String |  |  |
| 31 | `SC.PAT.AUDIT.DATE.TIME` | `ScPersonalAssetType_AuditDateTime` | String |  |  |
