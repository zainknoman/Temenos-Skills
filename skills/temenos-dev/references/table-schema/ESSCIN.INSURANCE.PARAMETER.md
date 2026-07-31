# ESSCIN.INSURANCE.PARAMETER — Table Schema

> Source: `INSERTS/I_F.ESSCIN.INSURANCE.PARAMETER` in `ESSPIN_SocialInsurance.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ES.PM.PAYMENT.ORDER.PRODUCT` | `EsscinInsuranceParameter_PaymentOrderProduct` | TField |  | It holds the Payment Order Product |
| 2 | `ES.PM.ENTITY.NUMBER` | `EsscinInsuranceParameter_EntityNumber` | TField |  | It Holds the Bank Entity Number |
| 3 | `ES.PM.ACCOUNT.CATEGORY` | `EsscinInsuranceParameter_AccountCategory` | TField |  | It holds the TGSS Category |
| 4 | `ES.PM.TGSS.ACCOUNT` | `EsscinInsuranceParameter_TgssAccount` | TField |  | It holds TGSS Vostro Account |
| 5 | `ES.PM.CECA.ACCOUNT` | `EsscinInsuranceParameter_CecaAccount` | TField |  | It holds CECA Vostro Acoount |
| 6 | `ES.PM.LOCAL.REF` | `EsscinInsuranceParameter_LocalRef` |  |  |  |
| 7 | `ES.PM.OUTFILE.FROM.DATE` | `EsscinInsuranceParameter_OutfileFromDate` | TField |  |  |
| 8 | `ES.PM.OUTFILE.TO.DATE` | `EsscinInsuranceParameter_OutfileToDate` | TField |  |  |
| 9 | `ES.PM.RESERVED.3` | `EsscinInsuranceParameter_Reserved3` | TField |  |  |
| 10 | `ES.PM.RESERVED.4` | `EsscinInsuranceParameter_Reserved4` | TField |  |  |
| 11 | `ES.PM.RESERVED.5` | `EsscinInsuranceParameter_Reserved5` | TField |  |  |
| 12 | `ES.PM.RESERVED.6` | `EsscinInsuranceParameter_Reserved6` | TField |  |  |
| 13 | `ES.PM.RESERVED.7` | `EsscinInsuranceParameter_Reserved7` | TField |  |  |
| 14 | `ES.PM.RESERVED.8` | `EsscinInsuranceParameter_Reserved8` | TField |  |  |
| 15 | `ES.PM.RESERVED.9` | `EsscinInsuranceParameter_Reserved9` | TField |  |  |
| 16 | `ES.PM.RESERVED.10` | `EsscinInsuranceParameter_Reserved10` | TField |  |  |
| 17 | `ES.PM.RESERVED.11` | `EsscinInsuranceParameter_Reserved11` | TField |  |  |
| 18 | `ES.PM.RESERVED.12` | `EsscinInsuranceParameter_Reserved12` | TField |  |  |
| 19 | `ES.PM.RESERVED.13` | `EsscinInsuranceParameter_Reserved13` | TField |  |  |
| 20 | `ES.PM.RESERVED.14` | `EsscinInsuranceParameter_Reserved14` | TField |  |  |
| 21 | `ES.PM.RESERVED.15` | `EsscinInsuranceParameter_Reserved15` | TField |  |  |
| 22 | `ES.PM.OVERRIDE` | `EsscinInsuranceParameter_Override` |  |  |  |
| 23 | `ES.PM.RECORD.STATUS` | `EsscinInsuranceParameter_RecordStatus` | String |  |  |
| 24 | `ES.PM.CURR.NO` | `EsscinInsuranceParameter_CurrNo` | String |  |  |
| 25 | `ES.PM.INPUTTER` | `EsscinInsuranceParameter_Inputter` |  |  |  |
| 26 | `ES.PM.DATE.TIME` | `EsscinInsuranceParameter_DateTime` |  |  |  |
| 27 | `ES.PM.AUTHORISER` | `EsscinInsuranceParameter_Authoriser` | String |  |  |
| 28 | `ES.PM.CO.CODE` | `EsscinInsuranceParameter_CoCode` | String |  |  |
| 29 | `ES.PM.DEPT.CODE` | `EsscinInsuranceParameter_DeptCode` | String |  |  |
| 30 | `ES.PM.AUDITOR.CODE` | `EsscinInsuranceParameter_AuditorCode` | String |  |  |
| 31 | `ES.PM.AUDIT.DATE.TIME` | `EsscinInsuranceParameter_AuditDateTime` | String |  |  |
