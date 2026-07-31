# CZ.CDP.ERASE.OPTION — Table Schema

> Source: `INSERTS/I_F.CZ.CDP.ERASE.OPTION` in `CZ_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CZ.CDE.DATA.TYPE` | `CzCdpEraseOption_DataType` | TField | Yes | Field to denote the data type for which the erase option of default needs to be applied on. Allowed values are DATE,NUMBER,ALPHA Mandatory only if erase action is set to DEFAULT |
| 2 | `CZ.CDE.ERASE.ACTION` | `CzCdpEraseOption_EraseAction` | TField | Yes | This field denotes erasure action applied to the data field identifield as personal data(PD). Allowed values are DEFAULT,NULLIFY,NO.ACTION,OBFUSCATE DEFAULT: will set the value in the PD field to a defualt value. NULLIFY: will clear the content of the PD field if not mandatory; or apply default value if PD field is mandatory NO.ACTION: value in the PD field is not cleared/erased. OBFUSCATE: value in the PD will be masked to hide the original contents. A logic will be applied to mask. |
| 3 | `CZ.CDE.ERASE.DATA.VALUE` | `CzCdpEraseOption_EraseDataValue` | TField | Yes | Field to denote what DATE value needs to be defaulted if the erase option is applied. Mandatory if DATA.TYPE is DATE and the ERASE.ACTION is DEFAULT. Allows only date format |
| 4 | `CZ.CDE.ERASE.CHAR.VALUE` | `CzCdpEraseOption_EraseCharValue` | TField | Yes | Field to denote what character needs to be defaulted if the erase option is applied. Allows only one character to be defined. For example if the ERASE.CHAR.VALUE is set as X and MIN.MAX.CHAR as MAX, then the personal data field will be defaulted with XXXXXXXXXX (if the maximum number of characters allowed in the field is 10 Mandatory if DATA.TYPE is ALPHA or NUMBER and the ERASE.ACTION is DEFAULT. The system expects only a numeric value if DATA.TYPE is NUMBER whereas if it is ALPHA both number or alphabet can be given. |
| 5 | `CZ.CDE.MIN.MAX.CHAR` | `CzCdpEraseOption_MinMaxChar` | TField | Yes | Allowed values are MIN,MAX,NONE Becomes mandatory field if ERASE.CHAR.VALUE is mentioned |
| 6 | `CZ.CDE.ACTION.RTN` | `CzCdpEraseOption_ActionRtn` | TField |  | Only allowed and Required If ERASE.ACTION is OBFUSCATE Specify either: i) A jBC subroutine name, or ii)For java implementations: An EB.API record id with a source type of METHOD which implements an interface defined in the EB.API record CZ.CDP.ERASE.OPTION.ACTION.RTN.HOOK. This field supports the GeneralDataProtectionRegulation.getObfuscatedFieldValue() method. The GeneralDataProtectionRegulation class is in the com.temenos.t24.api.hook.party package which is in CZ_FrameworkHook.jar shipped with T24. |
| 7 | `CZ.CDE.RESERVED.20` | `CzCdpEraseOption_Reserved20` | TField |  |  |
| 8 | `CZ.CDE.RESERVED.19` | `CzCdpEraseOption_Reserved19` | TField |  |  |
| 9 | `CZ.CDE.RESERVED.18` | `CzCdpEraseOption_Reserved18` | TField |  |  |
| 10 | `CZ.CDE.RESERVED.17` | `CzCdpEraseOption_Reserved17` | TField |  |  |
| 11 | `CZ.CDE.RESERVED.16` | `CzCdpEraseOption_Reserved16` | TField |  |  |
| 12 | `CZ.CDE.RESERVED.15` | `CzCdpEraseOption_Reserved15` | TField |  |  |
| 13 | `CZ.CDE.RESERVED.14` | `CzCdpEraseOption_Reserved14` | TField |  |  |
| 14 | `CZ.CDE.RESERVED.13` | `CzCdpEraseOption_Reserved13` | TField |  |  |
| 15 | `CZ.CDE.RESERVED.12` | `CzCdpEraseOption_Reserved12` | TField |  |  |
| 16 | `CZ.CDE.RESERVED.11` | `CzCdpEraseOption_Reserved11` | TField |  |  |
| 17 | `CZ.CDE.RESERVED.10` | `CzCdpEraseOption_Reserved10` | TField |  |  |
| 18 | `CZ.CDE.RESERVED.09` | `CzCdpEraseOption_Reserved09` | TField |  |  |
| 19 | `CZ.CDE.RESERVED.08` | `CzCdpEraseOption_Reserved08` | TField |  |  |
| 20 | `CZ.CDE.RESERVED.07` | `CzCdpEraseOption_Reserved07` | TField |  |  |
| 21 | `CZ.CDE.RESERVED.06` | `CzCdpEraseOption_Reserved06` | TField |  |  |
| 22 | `CZ.CDE.RESERVED.05` | `CzCdpEraseOption_Reserved05` | TField |  |  |
| 23 | `CZ.CDE.RESERVED.04` | `CzCdpEraseOption_Reserved04` | TField |  |  |
| 24 | `CZ.CDE.RESERVED.03` | `CzCdpEraseOption_Reserved03` | TField |  |  |
| 25 | `CZ.CDE.RESERVED.02` | `CzCdpEraseOption_Reserved02` | TField |  |  |
| 26 | `CZ.CDE.RESERVED.01` | `CzCdpEraseOption_Reserved01` | TField |  |  |
| 27 | `CZ.CDE.LOCAL.REF` | `CzCdpEraseOption_LocalRef` |  |  |  |
| 28 | `CZ.CDE.RECORD.STATUS` | `CzCdpEraseOption_RecordStatus` | String |  |  |
| 29 | `CZ.CDE.CURR.NO` | `CzCdpEraseOption_CurrNo` | String |  |  |
| 30 | `CZ.CDE.INPUTTER` | `CzCdpEraseOption_Inputter` |  |  |  |
| 31 | `CZ.CDE.DATE.TIME` | `CzCdpEraseOption_DateTime` |  |  |  |
| 32 | `CZ.CDE.AUTHORISER` | `CzCdpEraseOption_Authoriser` | String |  |  |
| 33 | `CZ.CDE.CO.CODE` | `CzCdpEraseOption_CoCode` | String |  |  |
| 34 | `CZ.CDE.DEPT.CODE` | `CzCdpEraseOption_DeptCode` | String |  |  |
| 35 | `CZ.CDE.AUDITOR.CODE` | `CzCdpEraseOption_AuditorCode` | String |  |  |
| 36 | `CZ.CDE.AUDIT.DATE.TIME` | `CzCdpEraseOption_AuditDateTime` | String |  |  |
