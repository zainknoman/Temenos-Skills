# COMPANY.CREATE — Table Schema

> Source: `INSERTS/I_F.COMPANY.CREATE` in `ST_CompanyCreation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.CRC.COMPANY.NAME` | `CompanyCreate_CompanyName` |  |  |  |
| 2 | `EB.CRC.NAME.ADDRESS` | `CompanyCreate_NameAddress` |  |  |  |
| 3 | `EB.CRC.MNEMONIC` | `CompanyCreate_Mnemonic` | TField |  | This is the mnemonic for the new company. It must not be an already existing company mnemonic value. |
| 4 | `EB.CRC.FINANCIAL.COM` | `CompanyCreate_FinancialCom` | TField |  | This field will indicate whether a Lead Company or a Branch Company is to be created. If company code in this field is equal to the company code of the key of this record then a new Lead company and all its associated files will be created. If the company code in this field is the same as that of an existing Lead Company then a Branch is being created. If a Branch is being created the branch company and its Lead company must belong to the same company group and the company in this field must be a lead company. You cannot link a branch to another branch. |
| 5 | `EB.CRC.FINANCIAL.MNE` | `CompanyCreate_FinancialMne` | TField |  | If a Lead company is being created then the value in this field must be equal to the MNEMONIC of this record. If a branch is being created then the menmonic must be equal to the mnemonic of the company defined in the FINANCIAL.COM field. |
| 6 | `EB.CRC.SUB.DIVISION.CODE` | `CompanyCreate_SubDivisionCode` | TField |  | Identifies the sub division code of the company being created, if the company being created is a type N or a type A company, then it must be the last 4 digits of the new company, i.e. record key, and it must be blank if the company being created is a type C or Type R. |
| 7 | `EB.CRC.CREATION.DATE` | `CompanyCreate_CreationDate` | TField |  | This field is reserved for future use, and will have no effect. |
| 8 | `EB.CRC.DEFAULT.COMPANY` | `CompanyCreate_DefaultCompany` | TField |  | Indicates an existing company record that can be used to populate the new company record. It will still be possible to amend the copied data fields if this is allowed. THe purpose of this field is to cut down on the amount of input required for the new company record, for example the application fields etc. |
| 9 | `EB.CRC.CONSOLIDATION.MARK` | `CompanyCreate_ConsolidationMark` | TField |  | The CONSOLIDATION.MARK value in the company being created. Option are N,C,R and A |
| 10 | `EB.CRC.RESERVED.7` | `CompanyCreate_Reserved7` |  |  |  |
| 11 | `EB.CRC.RESERVED.6` | `CompanyCreate_Reserved6` | TField |  |  |
| 12 | `EB.CRC.RESERVED.5` | `CompanyCreate_Reserved5` | TField |  |  |
| 13 | `EB.CRC.RESERVED.4` | `CompanyCreate_Reserved4` | TField |  |  |
| 14 | `EB.CRC.RESERVED.3` | `CompanyCreate_Reserved3` | TField |  |  |
| 15 | `EB.CRC.RESERVED.2` | `CompanyCreate_Reserved2` | TField |  |  |
| 16 | `EB.CRC.RESERVED.1` | `CompanyCreate_Reserved1` | TField |  |  |
| 17 | `EB.CRC.RECORD.STATUS` | `CompanyCreate_RecordStatus` | String |  |  |
| 18 | `EB.CRC.CURR.NO` | `CompanyCreate_CurrNo` | String |  |  |
| 19 | `EB.CRC.INPUTTER` | `CompanyCreate_Inputter` |  |  |  |
| 20 | `EB.CRC.DATE.TIME` | `CompanyCreate_DateTime` |  |  |  |
| 21 | `EB.CRC.AUTHORISER` | `CompanyCreate_Authoriser` | String |  |  |
| 22 | `EB.CRC.CO.CODE` | `CompanyCreate_CoCode` | String |  |  |
| 23 | `EB.CRC.DEPT.CODE` | `CompanyCreate_DeptCode` | String |  |  |
| 24 | `EB.CRC.AUDITOR.CODE` | `CompanyCreate_AuditorCode` | String |  |  |
| 25 | `EB.CRC.AUDIT.DATE.TIME` | `CompanyCreate_AuditDateTime` | String |  |  |
