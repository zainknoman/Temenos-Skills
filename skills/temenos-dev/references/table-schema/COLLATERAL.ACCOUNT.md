# COLLATERAL.ACCOUNT — Table Schema

> Source: `INSERTS/I_F.COLLATERAL.ACCOUNT` in `CO_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `COLL.ACC.NOM.CURRENCY` | `CollateralAccount_NomCurrency` | TField | No | Currency used for the purpose of evaluating and viewing the values of underlying Collaterals in Enquiries and reports. Validation Rules: Valid T24 Currency.Optional field |
| 2 | `COLL.ACC.SHORT.NAME` | `CollateralAccount_ShortName` |  |  |  |
| 3 | `COLL.ACC.COLL.PROVIDER` | `CollateralAccount_CollProvider` | TField | Yes | Customer who provides the collateral. Validation Rules: Valid Customer record.Mandatory field. |
| 4 | `COLL.ACC.ACCOUNT.OFFICER` | `CollateralAccount_AccountOfficer` | TField | No | Credit Officer who is responsible for administering and maintaining the Collaterals of the Provider. Validation Rules: Must be a valid record in DEPT.ACCT.OFFICER file.Optional field. |
| 5 | `COLL.ACC.COLLATERAL.ITEM` | `CollateralAccount_CollateralItem` |  |  |  |
| 6 | `COLL.ACC.COLL.ACC.RANKING` | `CollateralAccount_CollAccRanking` | TField | No | Ranking of the Collateral Account to enable to user to easily identify the order in which the Collateral accounts can be linked to the Collateral pool. Validation Rules: Upto 3 alphanumeric characters are allowed. Optional field. |
| 7 | `COLL.ACC.START.DATE` | `CollateralAccount_StartDate` | TField | No | Date from which the Collateral Account is effective. Default to Today date when it is not inputted. Validation Rules: Standard T24 Date format. Optional field. BackDate/ForwardDate will be accepted. |
| 8 | `COLL.ACC.END.DATE` | `CollateralAccount_EndDate` | TField | No | Represents the Expiry date of the Collateral Account. The Status of the Collateral Account becomes 'LIQ' when this date is reached. Validation Rules: Standard T24 Date format. Optional field. Cannot be less than Start Date. An override will be indicated when the Expiry date of the linked Collateral Items is beyond this End date. |
| 9 | `COLL.ACC.REVIEW.DATE.FQU` | `CollateralAccount_ReviewDateFqu` | TField | No | Date and frequency at which the collateral account should be reviewed. A combined date and frequency field which is automatically cycled by the system as part of the end-of-day. Validation Rules: 17 type frequency format. Optional input Review Date cannot be less than Start Date. |
| 10 | `COLL.ACC.STATUS` | `CollateralAccount_Status` | TField |  | The status of the Collateral Account. The status of the collateral Account is indicated in this field as follows: FWD - forward status; Start date is forward. CUR - current status; End date is forward and Start Date is earlier or equal to today. LIQ - liquidated status; End Date is past the today date. This field is automatically maintained by the system by an end-of-day process and is updated in accordance with any changes to the dates online. Validation Rules: 'FWD', 'CUR', 'LIQ'. Internal field. This is a NOINPUT field. |
| 11 | `COLL.ACC.COLL.POOL.REF` | `CollateralAccount_CollPoolRef` | TField |  | COLLATERAL.POOL Id. Refers the Collateral Pool to which the Collateral Account is linked. Validation Rules: Must be a Valid COLLATERAL.POOL id. NOINPUT field. Updated when a Collateral Account is linked to Collateral Pool. |
| 12 | `COLL.ACC.ACCOUNT.LEVEL.HAIRCUT` | `CollateralAccount_AccountLevelHaircut` | TField |  |  |
| 13 | `COLL.ACC.RESERVED09` | `CollateralAccount_Reserved09` | TField |  |  |
| 14 | `COLL.ACC.RESERVED08` | `CollateralAccount_Reserved08` | TField |  |  |
| 15 | `COLL.ACC.RESERVED07` | `CollateralAccount_Reserved07` | TField |  |  |
| 16 | `COLL.ACC.RESERVED06` | `CollateralAccount_Reserved06` | TField |  |  |
| 17 | `COLL.ACC.RESERVED05` | `CollateralAccount_Reserved05` | TField |  |  |
| 18 | `COLL.ACC.RESERVED04` | `CollateralAccount_Reserved04` | TField |  |  |
| 19 | `COLL.ACC.RESERVED03` | `CollateralAccount_Reserved03` | TField |  |  |
| 20 | `COLL.ACC.RESERVED02` | `CollateralAccount_Reserved02` | TField |  |  |
| 21 | `COLL.ACC.RESERVED01` | `CollateralAccount_Reserved01` | TField |  |  |
| 22 | `COLL.ACC.LOCAL.REF` | `CollateralAccount_LocalRef` |  |  |  |
| 23 | `COLL.ACC.OVERRIDE` | `CollateralAccount_Override` |  |  |  |
| 24 | `COLL.ACC.RECORD.STATUS` | `CollateralAccount_RecordStatus` | String |  |  |
| 25 | `COLL.ACC.CURR.NO` | `CollateralAccount_CurrNo` | String |  |  |
| 26 | `COLL.ACC.INPUTTER` | `CollateralAccount_Inputter` |  |  |  |
| 27 | `COLL.ACC.DATE.TIME` | `CollateralAccount_DateTime` |  |  |  |
| 28 | `COLL.ACC.AUTHORISER` | `CollateralAccount_Authoriser` | String |  |  |
| 29 | `COLL.ACC.CO.CODE` | `CollateralAccount_CoCode` | String |  |  |
| 30 | `COLL.ACC.DEPT.CODE` | `CollateralAccount_DeptCode` | String |  |  |
| 31 | `COLL.ACC.AUDITOR.CODE` | `CollateralAccount_AuditorCode` | String |  |  |
| 32 | `COLL.ACC.AUDIT.DATE.TIME` | `CollateralAccount_AuditDateTime` | String |  |  |
