# CAPL.H.DH.CHQ.ORDER.PARAM — Table Schema

> Source: `INSERTS/I_F.CAPL.H.DH.CHQ.ORDER.PARAM` in `CACQOR_ChequeOrdering.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAPL.H.DCOP.MICR.INSTUTION.NO` | `CaplHDhChqOrderParam_MicrInstutionNo` | TField |  |  |
| 2 | `CAPL.H.DCOP.MICR.TRANSIT.CURRENCY` | `CaplHDhChqOrderParam_MicrTransitCurrency` |  |  |  |
| 3 | `CAPL.H.DCOP.MICR.TRANSIT.NUMBER` | `CaplHDhChqOrderParam_MicrTransitNumber` |  |  |  |
| 4 | `CAPL.H.DCOP.CHK.DIGIT.OVERRIDE` | `CaplHDhChqOrderParam_ChkDigitOverride` | TField |  | Field to define the Cheque digit override flag. Used for mapping the value in Cheque ordering exract. |
| 5 | `CAPL.H.DCOP.ORD.BR.CODE` | `CaplHDhChqOrderParam_OrdBrCode` | TField |  | Field denotes the transit number of the branch placing the cheque order.Allowed values are alphanumeric character with 5 character.E.g. 2222 |
| 6 | `CAPL.H.DCOP.ORD.SUB.BR.CODE` | `CaplHDhChqOrderParam_OrdSubBrCode` | TField |  | The purpose of the field is used to denote the sub branch code of the branch placing the cheque order.Allowed values are alphanumeric character with 2 character.Eg. 33 |
| 7 | `CAPL.H.DCOP.DOM.INST.NUMBER` | `CaplHDhChqOrderParam_DomInstNumber` | TField |  | The purpose of the field is to defien the institution number of the domicile address to appear on the cheque.Allowed values are alphanumeric character with 3 character. |
| 8 | `CAPL.H.DCOP.DOM.TRANSIT.NUMBER` | `CaplHDhChqOrderParam_DomTransitNumber` | TField |  | This field is used to define the transit number of the domicile address to appear on the cheque.Allowed values are alphanumeric character with 5 character. |
| 9 | `CAPL.H.DCOP.DOM.SUB.BR.NUMBER` | `CaplHDhChqOrderParam_DomSubBrNumber` | TField |  | This field is used to defien the sub branch number of the domicile address to appear on the cheque.Allowed values are alphanumeric character with 2 character. |
| 10 | `CAPL.H.DCOP.SUPPLIER.ID` | `CaplHDhChqOrderParam_SupplierId` | TField |  | The field is used to define the supplier ID of the cheque order.Allowed values are alphanumeric character with 10 character. |
| 11 | `CAPL.H.DCOP.SUPPLIER.NAME` | `CaplHDhChqOrderParam_SupplierName` | TField |  | Field to capture the suppliser.Allowed values are alphanumeric character with 35 character.E.g Western Cheque management. |
| 12 | `CAPL.H.DCOP.MERGE.FILE` | `CaplHDhChqOrderParam_MergeFile` | TField |  | This field is used to merge the file of all the branches and send in a single file or to create a separate file for each branch.Valid inputs are Y/N'Y' - Merge all the branches.'N' - Create separate file for each branch. |
| 13 | `CAPL.H.DCOP.CHQ.ORDER.FILE.NAME` | `CaplHDhChqOrderParam_ChqOrderFileName` | TField |  | Field used to define the naming convention of the cheque order file.Format is NNNNNNNX.NNNN - Numeric Value (Note: last 4 digits are sequence number which will be incremented for every extract).X - Alpha character.Allowed values are alphanumeric character with 35 character.Eg. 0000103D.809 |
| 14 | `CAPL.H.DCOP.ARCH.PERIOD` | `CaplHDhChqOrderParam_ArchPeriod` | TField |  | The purpose of this field is used to denote the Archival period in monthsAllowed value 2 alphanumeric character |
| 15 | `CAPL.H.DCOP.CHQ.ORD.FT.TXN.TYPE` | `CaplHDhChqOrderParam_ChqOrdFtTxnType` | TField |  | Field is used to define the valid FT.TXN.TYPE.CONDITION record which is used to post the Cheque Order charges.Valid record from FT.TXN.TYPE.CONDITION tableE.g AC , ACBP |
| 16 | `CAPL.H.DCOP.FT.VERSION` | `CaplHDhChqOrderParam_FtVersion` | TField |  | This field is used to define the FT version for posting FT for charge.Valid record from VERSION.E.g. FUNDS.TRANSFER,CAMB.DH.INTERFACE |
| 17 | `CAPL.H.DCOP.APP.VERSION` | `CaplHDhChqOrderParam_AppVersion` | TField |  | This field is used to define the FT version for posting FT for charge.Valid record from VERSION.E.g. FUNDS.TRANSFER,CAMB.DH.INTERFACE |
| 18 | `CAPL.H.DCOP.OFS.SOURCE` | `CaplHDhChqOrderParam_OfsSource` | TField |  | Field is used to define the OFS.SOURCE record used to post FT for charges.Valid record from OFS.SOURCE.E.g. DH.INTER |
| 19 | `CAPL.H.DCOP.OFS.USER.NAME` | `CaplHDhChqOrderParam_OfsUserName` | TField |  | The field holds the User name to be used for posting FT for charges.Valid record from USER application.E.g. INPUTT |
| 20 | `CAPL.H.DCOP.OFS.PASSWORD` | `CaplHDhChqOrderParam_OfsPassword` | TField |  | Filed used to define the OFS password required for posting FT for charges.Valid password to be defined. |
| 21 | `CAPL.H.DCOP.LOCAL.REF` | `CaplHDhChqOrderParam_LocalRef` |  |  |  |
| 22 | `CAPL.H.DCOP.PERSONAL.CUS` | `CaplHDhChqOrderParam_PersonalCus` |  |  |  |
| 23 | `CAPL.H.DCOP.BUSINESS.USD` | `CaplHDhChqOrderParam_BusinessUsd` |  |  |  |
| 24 | `CAPL.H.DCOP.BUSINESS.CAD` | `CaplHDhChqOrderParam_BusinessCad` |  |  |  |
| 25 | `CAPL.H.DCOP.PERS.USD` | `CaplHDhChqOrderParam_PersUsd` |  |  |  |
| 26 | `CAPL.H.DCOP.PERS.CAD` | `CaplHDhChqOrderParam_PersCad` |  |  |  |
| 27 | `CAPL.H.DCOP.ADD.MANDT.CHECK` | `CaplHDhChqOrderParam_AddMandtCheck` |  |  |  |
| 28 | `CAPL.H.DCOP.UPDATE.CLEAR.ADD` | `CaplHDhChqOrderParam_UpdateClearAdd` |  |  |  |
| 29 | `CAPL.H.DCOP.MANDT.SHIP.ADDRESS` | `CaplHDhChqOrderParam_MandtShipAddress` |  |  |  |
| 30 | `CAPL.H.DCOP.NON.INT.SHIP.ADD` | `CaplHDhChqOrderParam_NonIntShipAdd` |  |  |  |
| 31 | `CAPL.H.DCOP.INT.POSTAL.CODE` | `CaplHDhChqOrderParam_IntPostalCode` | TField |  | Purpose of the field to indicate the postal code to be updated in SHIP.TO.OTHER.POSTAL.CODE in cheque ordering, when customer address country not matches with NON.INT.SHIP.ADDE.g. Z0Z0Z0 |
| 32 | `CAPL.H.DCOP.SHIP.TO.OTHER` | `CaplHDhChqOrderParam_ShipToOther` | TField |  | Purpose of the field to define the field name where the actual international postal code of the customer to be updated.Validation - Valid field of CAPL.H.DH. CHQ.ORDER |
| 33 | `CAPL.H.DCOP.SRC.FI.CODE` | `CaplHDhChqOrderParam_SrcFiCode` | TField |  | Source FI code.This value will be provided by D + H |
| 34 | `CAPL.H.DCOP.SRC.TRANSIT.CODE` | `CaplHDhChqOrderParam_SrcTransitCode` | TField |  | Sourct transit code. This value will be provided by D + H |
| 35 | `CAPL.H.DCOP.CUSTOMER.COM.CHECK` | `CaplHDhChqOrderParam_CustomerComCheck` | TField |  | This field is used to define whether primary owner or membership needs to be reported in the cheque order.Allowed values are:PRIMARY.OWNER / NONE - This will report the primary owner of the membership in the cheque order.CONTAINER - This will report the membership record in the cheque order.Note: This setup is applicable only for client following container process. |
| 36 | `CAPL.H.DCOP.RESERVED.10` | `CaplHDhChqOrderParam_Reserved10` | TField |  |  |
| 37 | `CAPL.H.DCOP.RESERVED.9` | `CaplHDhChqOrderParam_Reserved9` | TField |  |  |
| 38 | `CAPL.H.DCOP.RESERVED.8` | `CaplHDhChqOrderParam_Reserved8` | TField |  |  |
| 39 | `CAPL.H.DCOP.RESERVED.7` | `CaplHDhChqOrderParam_Reserved7` | TField |  |  |
| 40 | `CAPL.H.DCOP.RESERVED.6` | `CaplHDhChqOrderParam_Reserved6` | TField |  |  |
| 41 | `CAPL.H.DCOP.RESERVED.5` | `CaplHDhChqOrderParam_Reserved5` | TField |  |  |
| 42 | `CAPL.H.DCOP.RESERVED.4` | `CaplHDhChqOrderParam_Reserved4` | TField |  |  |
| 43 | `CAPL.H.DCOP.RESERVED.3` | `CaplHDhChqOrderParam_Reserved3` | TField |  |  |
| 44 | `CAPL.H.DCOP.RESERVED.2` | `CaplHDhChqOrderParam_Reserved2` | TField |  |  |
| 45 | `CAPL.H.DCOP.RESERVED.1` | `CaplHDhChqOrderParam_Reserved1` | TField |  |  |
| 46 | `CAPL.H.DCOP.OVERRIDE` | `CaplHDhChqOrderParam_Override` |  |  |  |
| 47 | `CAPL.H.DCOP.RECORD.STATUS` | `CaplHDhChqOrderParam_RecordStatus` | String |  |  |
| 48 | `CAPL.H.DCOP.CURR.NO` | `CaplHDhChqOrderParam_CurrNo` | String |  |  |
| 49 | `CAPL.H.DCOP.INPUTTER` | `CaplHDhChqOrderParam_Inputter` |  |  |  |
| 50 | `CAPL.H.DCOP.DATE.TIME` | `CaplHDhChqOrderParam_DateTime` |  |  |  |
| 51 | `CAPL.H.DCOP.AUTHORISER` | `CaplHDhChqOrderParam_Authoriser` | String |  |  |
| 52 | `CAPL.H.DCOP.CO.CODE` | `CaplHDhChqOrderParam_CoCode` | String |  |  |
| 53 | `CAPL.H.DCOP.DEPT.CODE` | `CaplHDhChqOrderParam_DeptCode` | String |  |  |
| 54 | `CAPL.H.DCOP.AUDITOR.CODE` | `CaplHDhChqOrderParam_AuditorCode` | String |  |  |
| 55 | `CAPL.H.DCOP.AUDIT.DATE.TIME` | `CaplHDhChqOrderParam_AuditDateTime` | String |  |  |
