# DEPT.ACCT.OFFICER — Table Schema

> Source: `INSERTS/I_F.DEPT.ACCT.OFFICER` in `ST_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.DAO.AREA` | `DeptAcctOfficer_Area` | A (alphanumeric) | Yes | Free format description of the Area of responsibility for the Account Officer. When the code being created refers to a Department (Foreign Exchange, Funds Transfer Unit, Money Market, etc.), the name of the Department should be entered in this field. If the code being created refers to an Account Officer, the name of the area where the Account Officer is working (e.g. Private Banking Group, Financial Institutions, etc.) should be entered in this field. Validation Rules: 3-35 type A (alphanumeric) characters. (Mandatory input) |
| 2 | `EB.DAO.NAME` | `DeptAcctOfficer_Name` | A (alphanumeric) | Yes | Indicates the name of the Department Head or the name of the Account Officer, working in the area specified. The actual name of the Account Officer or Department Head should be entered in this field. When an Application refers to a Department or Account Officer, the content of this field will be shown as the enrichment of the code being input/ displayed. Validation Rules: 3-35 type A (alphanumeric) (Mandatory input) |
| 3 | `EB.DAO.DELIVERY.POINT` | `DeptAcctOfficer_DeliveryPoint` | A (alphanumeric) | Yes | Indicates the internal office location for delivery of reports. The purpose of this field is to indicate a Delivery Point for the delivery of reports, etc. to the corresponding Department/Account Officer. Information like the name of the Building or the Floor number where this area is located are typical examples of information applicable to this field. Validation Rules: 1-16 type A (alphanumeric) characters. (Mandatory input) |
| 4 | `EB.DAO.RESTR.TO.COMPS` | `DeptAcctOfficer_RestrToComps` |  |  |  |
| 5 | `EB.DAO.PROHIBIT.COMPS` | `DeptAcctOfficer_ProhibitComps` |  |  |  |
| 6 | `EB.DAO.TELEPHONE.NO` | `DeptAcctOfficer_TelephoneNo` | TField |  | Free format field for the entry of an account officers telephone number. Validation Rules: Up to 15 alphanumeric characters. |
| 7 | `EB.DAO.FAX.NO` | `DeptAcctOfficer_FaxNo` | TField |  | Free format field for the entry of an account officers fax number. Validation Rules: Up to 15 alphanumeric characters. |
| 8 | `EB.DAO.TELEX.NO` | `DeptAcctOfficer_TelexNo` | TField |  | Free format field for the entry of an account officers telex number. Validation Rules: Up to 8 alphanumeric characters. |
| 9 | `EB.DAO.DEPT.LEVEL` | `DeptAcctOfficer_DeptLevel` | TField | Conditional | This fields indicates the level of this department within the departmental hierarchy. Validation Rules: Must be a valid entry of the DEPT.LEVEL file. Mandatory if DEPT.PARENT is input, otherwise optional. |
| 10 | `EB.DAO.DEPT.PARENT` | `DeptAcctOfficer_DeptParent` | TField | No | This fields refers to another DEPT.ACCT.OFFICER record that is the 'parent' of this one in the departmental hierarchy. For example, if this record represents a dealer desk then the DEPT.PARENT may point to the record representing 'Treasury'. Validation Rules: Must be a valid entry on the DEPT.ACCT.OFFICER file. The DEPT.ACCT.OFFICER specified here must be of a higher level than the current record. Optional input. |
| 11 | `EB.DAO.ALT.DEPT.LEVEL` | `DeptAcctOfficer_AltDeptLevel` | TField | Conditional | This fields indicates the level of this department within the alternative departmental hierarchy. Validation Rules: Must be a valid entry on the ALT.DEPT.LEVEL file. Mandatory if ALT.DEPT.PARENT is input, otherwise optional. |
| 12 | `EB.DAO.ALT.DEPT.PARENT` | `DeptAcctOfficer_AltDeptParent` | TField | No | This fields refers to another DEPT.ACCT.OFFICER record that is the 'parent' of this one in the alternative departmental hierarchy. For example, if this record represents a dealer desk then the ALT.DEPT.PARENT may point to the record representing 'Treasury'. Validation Rules: Must be a valid entry on the DEPT.ACCT.OFFICER file. The DEPT.ACCT.OFFICER specified here must be of a higher level than the current record. Optional Input. |
| 13 | `EB.DAO.LOCAL.REF` | `DeptAcctOfficer_LocalRef` |  |  |  |
| 14 | `EB.DAO.MNEMONIC` | `DeptAcctOfficer_Mnemonic` | TField |  | MNEMONIC Specifies an alternative method of referencing the Department Account Officer. The Mnemonic code rather than the Account ID may be used at any time to reference the Department Account Officer details. It can be used in situations the bank would like to identify account officers using alphanumeric fields. Validation Rules: 3 - 10 type MNE (uppercase alpha or numeric or '.') characters. The Mnemonic code must be unique. |
| 15 | `EB.DAO.DEPARTMENT` | `DeptAcctOfficer_Department` | TField |  | DEPARTMENT This field can be used when the account officer is part of an account key if the DAO ID is greater than 4 digits. Validation Rules: Up to 4 numeric characters are allowed. It must exist as a record in DEPT.ACCT.OFFICER file. |
| 16 | `EB.DAO.ACCEPT.MESSAGE` | `DeptAcctOfficer_AcceptMessage` | TField |  | This field specifies whether this account officer will accept secure messages. Functionaly, this field is linked with the table EB.SECURE.MESSAGE which establish secure messaging between bank user and customer. Validation Rules: : Must be allowed to input YES or Blank If the input is YES then account officer will accept messages triggered from the customers. Otherwise it will not accept messages. |
| 17 | `EB.DAO.EVENT` | `DeptAcctOfficer_Event` |  |  |  |
| 18 | `EB.DAO.FIELD` | `DeptAcctOfficer_Field` |  |  |  |
| 19 | `EB.DAO.OPERAND` | `DeptAcctOfficer_Operand` |  |  |  |
| 20 | `EB.DAO.VALUE` | `DeptAcctOfficer_Value` |  |  |  |
| 21 | `EB.DAO.MV.ALERT.RES6` | `DeptAcctOfficer_MvAlertRes6` |  |  |  |
| 22 | `EB.DAO.MV.ALERT.RES5` | `DeptAcctOfficer_MvAlertRes5` |  |  |  |
| 23 | `EB.DAO.MV.ALERT.RES4` | `DeptAcctOfficer_MvAlertRes4` |  |  |  |
| 24 | `EB.DAO.MV.ALERT.RES3` | `DeptAcctOfficer_MvAlertRes3` |  |  |  |
| 25 | `EB.DAO.MV.ALERT.RES2` | `DeptAcctOfficer_MvAlertRes2` |  |  |  |
| 26 | `EB.DAO.MV.ALERT.RES1` | `DeptAcctOfficer_MvAlertRes1` |  |  |  |
| 27 | `EB.DAO.REQUEST.ID` | `DeptAcctOfficer_RequestId` |  |  |  |
| 28 | `EB.DAO.CUSTOMER.ID` | `DeptAcctOfficer_CustomerId` | TField |  | This field holds the ID of the CUSTOMER table created for the account officer, details from this customer record is used for delivering alerts. |
| 29 | `EB.DAO.OVERRIDE` | `DeptAcctOfficer_Override` |  |  |  |
| 30 | `EB.DAO.RECORD.STATUS` | `DeptAcctOfficer_RecordStatus` | String |  |  |
| 31 | `EB.DAO.CURR.NO` | `DeptAcctOfficer_CurrNo` | String |  |  |
| 32 | `EB.DAO.INPUTTER` | `DeptAcctOfficer_Inputter` |  |  |  |
| 33 | `EB.DAO.DATE.TIME` | `DeptAcctOfficer_DateTime` |  |  |  |
| 34 | `EB.DAO.AUTHORISER` | `DeptAcctOfficer_Authoriser` | String |  |  |
| 35 | `EB.DAO.CO.CODE` | `DeptAcctOfficer_CoCode` | String |  |  |
| 36 | `EB.DAO.DEPT.CODE` | `DeptAcctOfficer_DeptCode` | String |  |  |
| 37 | `EB.DAO.AUDITOR.CODE` | `DeptAcctOfficer_AuditorCode` | String |  |  |
| 38 | `EB.DAO.AUDIT.DATE.TIME` | `DeptAcctOfficer_AuditDateTime` | String |  |  |
