# HUTXNF.FREE.TXN.PARAM — Table Schema

> Source: `INSERTS/I_F.HUTXNF.FREE.TXN.PARAM` in `HUTXNF_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `HUTPAR.STAT.FREE.ATM.COUNT` | `HutxnfFreeTxnParam_StatFreeAtmCount` | TField |  | The number of statutory free discount provided if declaration is made. |
| 2 | `HUTPAR.STAT.FREE.ATM.AMT` | `HutxnfFreeTxnParam_StatFreeAtmAmt` | TField |  | The amount till which statutory free discount is applicable if declaration is made. |
| 3 | `HUTPAR.COURT.OF.GUARDIANS.PRODUCT` | `HutxnfFreeTxnParam_CourtOfGuardiansProduct` | TField |  | List of products for which statutory discount is provided. |
| 4 | `HUTPAR.ATM.FREE.PACKAGE` | `HutxnfFreeTxnParam_AtmFreePackage` |  |  |  |
| 5 | `HUTPAR.ATM.FREE.PRODUCT` | `HutxnfFreeTxnParam_AtmFreeProduct` |  |  |  |
| 6 | `HUTPAR.PACKAGE.TYPE` | `HutxnfFreeTxnParam_PackageType` |  |  |  |
| 7 | `HUTPAR.OWN.ATM.FREE.COUNT` | `HutxnfFreeTxnParam_OwnAtmFreeCount` |  |  |  |
| 8 | `HUTPAR.OTHER.ATM.FREE.COUNT` | `HutxnfFreeTxnParam_OtherAtmFreeCount` |  |  |  |
| 9 | `HUTPAR.RESERVED.12` | `HutxnfFreeTxnParam_Reserved12` |  |  |  |
| 10 | `HUTPAR.RESERVED.11` | `HutxnfFreeTxnParam_Reserved11` |  |  |  |
| 11 | `HUTPAR.OWN.ATM.ACTIVITY.ID` | `HutxnfFreeTxnParam_OwnAtmActivityId` | TField |  | Activity assigned for Own ATM withdrawal transactions (Vetted into list of activity) |
| 12 | `HUTPAR.OTHER.ATM.ACTIVITY.ID` | `HutxnfFreeTxnParam_OtherAtmActivityId` | TField |  | Activity assigned for Other ATM withdrawal transactions (Vetted into list of activity) |
| 13 | `HUTPAR.COG.TT.ACTIVITY.ID` | `HutxnfFreeTxnParam_CogTtActivityId` | TField |  | Activity assigned for teller transactions (Vetted into list of activity) |
| 14 | `HUTPAR.DECLARATION.REVIEW.DAY` | `HutxnfFreeTxnParam_DeclarationReviewDay` | TField |  | The field specifies the day before which the declaration is valid for free transactions |
| 15 | `HUTPAR.MIGRATION.ACTIVITY.ID` | `HutxnfFreeTxnParam_MigrationActivityId` | TField |  | Activity assigned for migration which has to be considered by the routine. (Vetted into list of activity) |
| 16 | `HUTPAR.CUS.RES.CHECK.ROUTINE` | `HutxnfFreeTxnParam_CusResCheckRoutine` | A (alphanumeric) |  | An EB.API record id with a source type of METHOD which implements an interface defined in the EB.API record HUTXNF.FREE.TXN.PARAM.CUS.RES.HOOK. This field supports the TransactionFee.isHungaryResident() method. The TransactionFee class is in the com.temenos.t24.api.hook.countrymodelbank.hungary package which is in HUTXNF_TransactionFeeHook.jar shipped with T24. This routine is invoked during HUTXNF.ELIGIBILITY.CHECK service. Validation Rules: Up to 35 type A (alphanumeric) characters. The subroutine entered should exist in EB.API record. |
| 17 | `HUTPAR.CHARGE.CHECK.STAGE` | `HutxnfFreeTxnParam_ChargeCheckStage` | TField |  | The field specifies if free of charge is based on "Settlement" or "Reservation". |
| 18 | `HUTPAR.RESERVE.LOCK.TYPE` | `HutxnfFreeTxnParam_ReserveLockType` | TField |  | The field specifies the lock type that will be used to create AC.LOCKED.EVENTS for an ATM reservation. |
| 19 | `HUTPAR.OWN.ATM.CODE` | `HutxnfFreeTxnParam_OwnAtmCode` |  |  |  |
| 20 | `HUTPAR.OTHER.ATM.CODE` | `HutxnfFreeTxnParam_OtherAtmCode` |  |  |  |
| 21 | `HUTPAR.RESERVED.4` | `HutxnfFreeTxnParam_Reserved4` |  |  |  |
| 22 | `HUTPAR.RESERVED.3` | `HutxnfFreeTxnParam_Reserved3` |  |  |  |
| 23 | `HUTPAR.RESERVED.2` | `HutxnfFreeTxnParam_Reserved2` |  |  |  |
| 24 | `HUTPAR.RESERVED.1` | `HutxnfFreeTxnParam_Reserved1` | TField |  | Reserved for future use. |
| 25 | `HUTPAR.LOCAL.REF` | `HutxnfFreeTxnParam_LocalRef` |  |  |  |
| 26 | `HUTPAR.OVERRIDE` | `HutxnfFreeTxnParam_Override` |  |  |  |
| 27 | `HUTPAR.RECORD.STATUS` | `HutxnfFreeTxnParam_RecordStatus` | String |  |  |
| 28 | `HUTPAR.CURR.NO` | `HutxnfFreeTxnParam_CurrNo` | String |  |  |
| 29 | `HUTPAR.INPUTTER` | `HutxnfFreeTxnParam_Inputter` |  |  |  |
| 30 | `HUTPAR.DATE.TIME` | `HutxnfFreeTxnParam_DateTime` |  |  |  |
| 31 | `HUTPAR.AUTHORISER` | `HutxnfFreeTxnParam_Authoriser` | String |  |  |
| 32 | `HUTPAR.CO.CODE` | `HutxnfFreeTxnParam_CoCode` | String |  |  |
| 33 | `HUTPAR.DEPT.CODE` | `HutxnfFreeTxnParam_DeptCode` | String |  |  |
| 34 | `HUTPAR.AUDITOR.CODE` | `HutxnfFreeTxnParam_AuditorCode` | String |  |  |
| 35 | `HUTPAR.AUDIT.DATE.TIME` | `HutxnfFreeTxnParam_AuditDateTime` | String |  |  |
