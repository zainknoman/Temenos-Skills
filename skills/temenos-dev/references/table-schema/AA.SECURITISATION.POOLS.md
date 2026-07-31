# AA.SECURITISATION.POOLS — Table Schema

> Source: `INSERTS/I_F.AA.SECURITISATION.POOLS` in `AA_Participant.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.SEC.POOL.DESCRIPTION` | `AaSecuritisationPools_Description` |  |  |  |
| 2 | `AA.SEC.POOL.START.DATE` | `AaSecuritisationPools_StartDate` | TField | Yes | Pool Start date. Input Mandatory and if left blank, then it will be defaulted with Today�s date. Securitization of the arrangements under the pool can only be made on or after this date. Only arrangements older than this date can be added into the Pool. |
| 3 | `AA.SEC.POOL.EXPIRY.DATE` | `AaSecuritisationPools_ExpiryDate` | TField | No | Pool Expiry date. Input Optional and if Specified then, it can�t be less than start date. Adding new arrangements to the pool will not be allowed after this date. |
| 4 | `AA.SEC.POOL.RESERVED.20` | `AaSecuritisationPools_Reserved20` |  |  |  |
| 5 | `AA.SEC.POOL.RESERVED.19` | `AaSecuritisationPools_Reserved19` |  |  |  |
| 6 | `AA.SEC.POOL.RESERVED.18` | `AaSecuritisationPools_Reserved18` | TField |  |  |
| 7 | `AA.SEC.POOL.RESERVED.17` | `AaSecuritisationPools_Reserved17` | TField |  |  |
| 8 | `AA.SEC.POOL.RESERVED.16` | `AaSecuritisationPools_Reserved16` | TField |  |  |
| 9 | `AA.SEC.POOL.RESERVED.15` | `AaSecuritisationPools_Reserved15` | TField |  |  |
| 10 | `AA.SEC.POOL.RESERVED.14` | `AaSecuritisationPools_Reserved14` | TField |  |  |
| 11 | `AA.SEC.POOL.RESERVED.13` | `AaSecuritisationPools_Reserved13` | TField |  |  |
| 12 | `AA.SEC.POOL.RESERVED.12` | `AaSecuritisationPools_Reserved12` | TField |  |  |
| 13 | `AA.SEC.POOL.RESERVED.11` | `AaSecuritisationPools_Reserved11` | TField |  |  |
| 14 | `AA.SEC.POOL.INVESTOR.ID` | `AaSecuritisationPools_InvestorId` |  |  |  |
| 15 | `AA.SEC.POOL.SHARE.PERCENTAGE` | `AaSecuritisationPools_SharePercentage` |  |  |  |
| 16 | `AA.SEC.POOL.DEF.BENEFICIARY` | `AaSecuritisationPools_DefBeneficiary` |  |  |  |
| 17 | `AA.SEC.POOL.DEF.PO.PRODUCT` | `AaSecuritisationPools_DefPoProduct` |  |  |  |
| 18 | `AA.SEC.POOL.RESERVED.10` | `AaSecuritisationPools_Reserved10` |  |  |  |
| 19 | `AA.SEC.POOL.RESERVED.9` | `AaSecuritisationPools_Reserved9` |  |  |  |
| 20 | `AA.SEC.POOL.RESERVED.8` | `AaSecuritisationPools_Reserved8` |  |  |  |
| 21 | `AA.SEC.POOL.RESERVED.7` | `AaSecuritisationPools_Reserved7` |  |  |  |
| 22 | `AA.SEC.POOL.RESERVED.6` | `AaSecuritisationPools_Reserved6` |  |  |  |
| 23 | `AA.SEC.POOL.RESERVED.5` | `AaSecuritisationPools_Reserved5` |  |  |  |
| 24 | `AA.SEC.POOL.RESERVED.4` | `AaSecuritisationPools_Reserved4` |  |  |  |
| 25 | `AA.SEC.POOL.RESERVED.3` | `AaSecuritisationPools_Reserved3` |  |  |  |
| 26 | `AA.SEC.POOL.RESERVED.2` | `AaSecuritisationPools_Reserved2` |  |  |  |
| 27 | `AA.SEC.POOL.RESERVED.1` | `AaSecuritisationPools_Reserved1` |  |  |  |
| 28 | `AA.SEC.POOL.LOCAL.REF` | `AaSecuritisationPools_LocalRef` |  |  |  |
| 29 | `AA.SEC.POOL.OVERRIDE` | `AaSecuritisationPools_Override` |  |  |  |
| 30 | `AA.SEC.POOL.RECORD.STATUS` | `AaSecuritisationPools_RecordStatus` | String |  |  |
| 31 | `AA.SEC.POOL.CURR.NO` | `AaSecuritisationPools_CurrNo` | String |  |  |
| 32 | `AA.SEC.POOL.INPUTTER` | `AaSecuritisationPools_Inputter` |  |  |  |
| 33 | `AA.SEC.POOL.DATE.TIME` | `AaSecuritisationPools_DateTime` |  |  |  |
| 34 | `AA.SEC.POOL.AUTHORISER` | `AaSecuritisationPools_Authoriser` | String |  |  |
| 35 | `AA.SEC.POOL.CO.CODE` | `AaSecuritisationPools_CoCode` | String |  |  |
| 36 | `AA.SEC.POOL.DEPT.CODE` | `AaSecuritisationPools_DeptCode` | String |  |  |
| 37 | `AA.SEC.POOL.AUDITOR.CODE` | `AaSecuritisationPools_AuditorCode` | String |  |  |
| 38 | `AA.SEC.POOL.AUDIT.DATE.TIME` | `AaSecuritisationPools_AuditDateTime` | String |  |  |
