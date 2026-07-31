# CAREGS.CDIC.ACCT.DETAILS — Table Schema

> Source: `INSERTS/I_F.CAREGS.CDIC.ACCT.DETAILS` in `CADEPO_CDIC.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CDIC.AC.DET.OWNER.ID` | `CaregsCdicAcctDetails_OwnerId` | TField |  | Purpose of the field to store the Owner of the ID account.FI with CIF ProcessOwner ID will be updated based on the field CUSTOMER / OWNER.FI with CU processOwner ID will be updated based on the field REL.CUSTOMER having role as FIRST.Valid record of CUSTOMER |
| 2 | `CDIC.AC.DET.JOINT.ACCOUNT.FLAG` | `CaregsCdicAcctDetails_JointAccountFlag` | TField |  | Purpose of the field to indicate whether the account is joint account or not.Allowed inputs YES / NOValidation:If all JOINT.OWNER.ROLE = CAREGS.CDIC.PARAMETER > NB.PT.REL.CODE, then flag as No.Validation : EB.LOOKUP > JOINT.INSCATEG. If the account insurance category matches with the eblookup, only then joint account flag gets updated as YES. |
| 3 | `CDIC.AC.DET.JOINT.OWNER.ID` | `CaregsCdicAcctDetails_JointOwnerId` |  |  |  |
| 4 | `CDIC.AC.DET.JOINT.OWNER.ROLE` | `CaregsCdicAcctDetails_JointOwnerRole` |  |  |  |
| 5 | `CDIC.AC.DET.JOINT.PAYEE.FLAG` | `CaregsCdicAcctDetails_JointPayeeFlag` |  |  |  |
| 6 | `CDIC.AC.DET.RESERVED.8` | `CaregsCdicAcctDetails_Reserved8` |  |  |  |
| 7 | `CDIC.AC.DET.RESERVED.7` | `CaregsCdicAcctDetails_Reserved7` |  |  |  |
| 8 | `CDIC.AC.DET.RESERVED.6` | `CaregsCdicAcctDetails_Reserved6` |  |  |  |
| 9 | `CDIC.AC.DET.INSURANCE.CATEGORY` | `CaregsCdicAcctDetails_InsuranceCategory` | TField |  | Purpose of the field to store the Insurance category to which the account belongs to.Field is updated based on the logic derived from the table - CAREGS.CDIC.INSURANCE.CATEGExample - BASIC |
| 10 | `CDIC.AC.DET.INSUR.CATEG.CODE` | `CaregsCdicAcctDetails_InsurCategCode` | TField |  |  |
| 11 | `CDIC.AC.DET.TRUST.TYPE.CODE` | `CaregsCdicAcctDetails_TrustTypeCode` | TField |  | Purpose of the field to store the Trust Account code to which the account belongs to.Field is updated based on the logic derived from the table - CAREGS.CDIC.TRUST.CODESExample - 1Allowed 2 digits numeric, upto 99. |
| 12 | `CDIC.AC.DET.CLEARING.ACCT.CODE` | `CaregsCdicAcctDetails_ClearingAcctCode` | TField |  |  |
| 13 | `CDIC.AC.DET.CLEARING.ACCT.TYPE` | `CaregsCdicAcctDetails_ClearingAcctType` | TField |  |  |
| 14 | `CDIC.AC.DET.PRODUCT.CODE` | `CaregsCdicAcctDetails_ProductCode` | TField |  | Purpose of the field to store the Product code to which the account belongs to.Field is updated based on the table CAREGS.CDIC.PRODUCT.CODESExample - 1 |
| 15 | `CDIC.AC.DET.PRODUCT.GROUP.CODE` | `CaregsCdicAcctDetails_ProductGroupCode` | TField |  | Purpose of the field to store the Product Group code to which the account belongs to.Field is updated based on the table CAREGS.CDIC.PRODUCT.CODESExample - 1 |
| 16 | `CDIC.AC.DET.ACCOUNT.TYPE.CODE` | `CaregsCdicAcctDetails_AccountTypeCode` | TField |  | To store the account type of the account |
| 17 | `CDIC.AC.DET.COMPANY.CODE` | `CaregsCdicAcctDetails_CompanyCode` | TField |  | Company code of the account. Valid id from the COMPANY table |
| 18 | `CDIC.AC.DET.SUBSYSTEM.ID` | `CaregsCdicAcctDetails_SubsystemId` | TField |  | Subsystem id from CAREGS.CDIC.PARAMETER&gt;SYSTEM record |
| 19 | `CDIC.AC.DET.PRODUCT.LINE` | `CaregsCdicAcctDetails_ProductLine` | TField |  |  |
| 20 | `CDIC.AC.DET.BALANCE` | `CaregsCdicAcctDetails_Balance` | TField |  |  |
| 21 | `CDIC.AC.DET.ACCESS.BALANCE` | `CaregsCdicAcctDetails_AccessBalance` | TField |  |  |
| 22 | `CDIC.AC.DET.INT.LAST.PAY.DATE` | `CaregsCdicAcctDetails_IntLastPayDate` | TField |  |  |
| 23 | `CDIC.AC.DET.INT.ACCR.AMOUNT` | `CaregsCdicAcctDetails_IntAccrAmount` | TField |  |  |
| 24 | `CDIC.AC.DET.PAYEE.FLAG` | `CaregsCdicAcctDetails_PayeeFlag` | TField |  |  |
| 25 | `CDIC.AC.DET.OWNER.ROLE` | `CaregsCdicAcctDetails_OwnerRole` | TField |  |  |
| 26 | `CDIC.AC.DET.ESCROW.ACCOUNT` | `CaregsCdicAcctDetails_EscrowAccount` | TField |  |  |
| 27 | `CDIC.AC.DET.BENEFICIARY` | `CaregsCdicAcctDetails_Beneficiary` |  |  |  |
| 28 | `CDIC.AC.DET.LAST.PAY.DATE` | `CaregsCdicAcctDetails_LastPayDate` |  |  |  |
| 29 | `CDIC.AC.DET.NEXT.PAY.DATE` | `CaregsCdicAcctDetails_NextPayDate` |  |  |  |
| 30 | `CDIC.AC.DET.FEDERAL.CHECK` | `CaregsCdicAcctDetails_FederalCheck` | TField |  | Purpose of the field to indicate whether the ID account to be reported in table 130 or table 160 in cdic extract.Applicable values - YES / NO |
| 31 | `CDIC.AC.DET.CURRENCY` | `CaregsCdicAcctDetails_Currency` | TField |  | Purpose of the field to indicate account currency |
| 32 | `CDIC.AC.DET.FED.INS.CATEG.CODE` | `CaregsCdicAcctDetails_FedInsCategCode` | TField |  | Purpose of the field to store fed insurance category code defined in CAREGS.CDIC.INSURANCE.CATEGORY for the correspondinginsurance category |
| 33 | `CDIC.AC.DET.RESERVED.2` | `CaregsCdicAcctDetails_Reserved2` | TField |  |  |
| 34 | `CDIC.AC.DET.RESERVED.1` | `CaregsCdicAcctDetails_Reserved1` | TField |  |  |
| 35 | `CDIC.AC.DET.RECORD.STATUS` | `CaregsCdicAcctDetails_RecordStatus` | String |  |  |
| 36 | `CDIC.AC.DET.CURR.NO` | `CaregsCdicAcctDetails_CurrNo` | String |  |  |
| 37 | `CDIC.AC.DET.INPUTTER` | `CaregsCdicAcctDetails_Inputter` |  |  |  |
| 38 | `CDIC.AC.DET.DATE.TIME` | `CaregsCdicAcctDetails_DateTime` |  |  |  |
| 39 | `CDIC.AC.DET.AUTHORISER` | `CaregsCdicAcctDetails_Authoriser` | String |  |  |
| 40 | `CDIC.AC.DET.CO.CODE` | `CaregsCdicAcctDetails_CoCode` | String |  |  |
| 41 | `CDIC.AC.DET.DEPT.CODE` | `CaregsCdicAcctDetails_DeptCode` | String |  |  |
| 42 | `CDIC.AC.DET.AUDITOR.CODE` | `CaregsCdicAcctDetails_AuditorCode` | String |  |  |
| 43 | `CDIC.AC.DET.AUDIT.DATE.TIME` | `CaregsCdicAcctDetails_AuditDateTime` | String |  |  |
