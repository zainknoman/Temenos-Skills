# CAPL.H.PAP.DD.PARAM — Table Schema

> Source: `INSERTS/I_F.CAPL.H.PAP.DD.PARAM` in `CAEFPA_EFTPap.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAPL.DD.PARAM.ID` | `CaplHPapDdParam_DdParamId` | TField |  | This parameter links the DD.PARAMETER ID where in the details about layout structure and the number of days before the value date, which the files (records) are extracted. |
| 2 | `CAPL.EFT1.PATH` | `CaplHPapDdParam_Eft1Path` | TField | Yes | Purpose of the field to store the valid Directory name where the ZEFT1 extract files have to be placed.This is a conditional mandatory field.Eg - ./PAP.BP |
| 3 | `CAPL.EFT1.FILENAME` | `CaplHPapDdParam_Eft1Filename` | TField |  | This field is to define the file name to be used for generating the ZEFT1 file.Field is used to store the file name to process the ZEFT1 extract by lead company's.eg. ZEFT1.DAT |
| 4 | `CAPL.EFT1.ORIG.ID` | `CaplHPapDdParam_Eft1OrigId` | TField |  | Purpose of the field to hold the originator ID used for EFT1 file processing.Validations: Value this field to be matched with the incoming file value in originator position.If value not matched, file will not be processed and to be reject |
| 5 | `CAPL.EFT2.PATH` | `CaplHPapDdParam_Eft2Path` | TField | Yes | Purpose of the field to store the valid Directory name where the ZEFT2 extract files have to be placed.This is a conditional mandatory field.Eg - ./PAP.BP |
| 6 | `CAPL.EFT2.FILENAME` | `CaplHPapDdParam_Eft2Filename` | TField |  | This field is to define the file name to be used for generating the ZEFT1 file.Field is used to store the file name to process the ZEFT2 extract by lead company's.eg. ZEFT2.DAT |
| 7 | `CAPL.EFT2.ORIG.ID` | `CaplHPapDdParam_Eft2OrigId` | TField |  | Purpose of the field to hold the originator ID used for EFT2 file processing.Validations: Value this field to be matched with the incoming file value in originator position.If value not matched, file will not be processed and to be reject |
| 8 | `CAPL.EFT3.PATH` | `CaplHPapDdParam_Eft3Path` | TField | Yes | Purpose of the field to store the valid Directory name where the ZEFT3 extract files have to be placed.This is a conditional mandatory field.Eg - ./PAP.BP |
| 9 | `CAPL.EFT3.FILENAME` | `CaplHPapDdParam_Eft3Filename` | TField |  | This field is to define the file name to be used for generating the ZEFT3 file.Field is used to store the file name to process the ZEFT2 extract by lead company's.eg. ZEFT3.DAT |
| 10 | `CAPL.EFT3.ORIG.ID` | `CaplHPapDdParam_Eft3OrigId` | TField |  | Purpose of the field to hold the originator ID used for EFT3 file processing.Validations: Value this field to be matched with the incoming file value in originator position.If value not matched, file will not be processed and to be reject |
| 11 | `CAPL.CALENDER` | `CaplHPapDdParam_Calender` | TField |  | The CALENDAR which will be referred while checking for holidays. |
| 12 | `CAPL.PAP.CALENDER` | `CaplHPapDdParam_PapCalender` | TField |  | This calendar will be referred to, when the process of extraction is actually initiated. This calendar will be checked if the day on which the process is run is a working day or not. |
| 13 | `CAPL.ALLOWED.DD.EVENTS` | `CaplHPapDdParam_AllowedDdEvents` |  |  |  |
| 14 | `CAPL.PAYMENT.TYPE` | `CaplHPapDdParam_PaymentType` |  |  |  |
| 15 | `CAPL.DAYS.FOR.PAYMENT` | `CaplHPapDdParam_DaysForPayment` | TField |  | Field to store the number of days which is validated agains the frequeny date in CAPL.H.PAP.DD.PARAMValidation - if today's date is less than the frequency date in CAPL.H.PAP.DD.DDI + number of days in DAYS.FOR.PAYMENT, user will be thrown with the error.Allowed 2 digits numeric., 1-99 |
| 16 | `CAPL.INSTITUTE.NAME` | `CaplHPapDdParam_InstituteName` | TField |  | Field is used to store the institute name to be reported in ZEFT file.Eg. TEMENOS |
| 17 | `CAPL.SHORT.INT.NAME` | `CaplHPapDdParam_ShortIntName` | TField |  | Field is used to store the short name of the institute which is used to report in ZEFT file.Validation: 4 ANeg. TEM |
| 18 | `CAPL.ORIG.SHORT.NAME` | `CaplHPapDdParam_OrigShortName` | TField |  | Field is used to store the Originator short name which is to be reported in ZEFT file.Eg. TEMENOS |
| 19 | `CAPL.ORIG.LONG.NAME` | `CaplHPapDdParam_OrigLongName` | TField |  | Field is used to store the Originator Full name which is to be reported in ZEFT file.Eg. TEMENOS |
| 20 | `CAPL.PAP.MAX.SEQ.NO` | `CaplHPapDdParam_PapMaxSeqNo` | TField |  | Field used to store the sequence number of the ZEFT files. Once the File is processed, value gets incremented and updated.Validation - if the incoming file sequence NE to the value in this field, field gets incremented with 1 based on the sequence updated in CAPL.H.PAP.FILE.NUMBEREg 9999 |
| 21 | `CAPL.LOCAL.REF` | `CaplHPapDdParam_LocalRef` |  |  |  |
| 22 | `CAPL.OVERRIDE` | `CaplHPapDdParam_Override` |  |  |  |
| 23 | `CAPL.PRODUCT.TYPE` | `CaplHPapDdParam_ProductType` | TField |  | Field is used to store the payment order product which is to be considered for sending the payment related information in the ZEFT file.Validations - records from PAYMENT.ORDER.PRODUCT table.Eg. EFT |
| 24 | `CAPL.RECORD.STATUS` | `CaplHPapDdParam_RecordStatus` | String |  |  |
| 25 | `CAPL.CURR.NO` | `CaplHPapDdParam_CurrNo` | String |  |  |
| 26 | `CAPL.INPUTTER` | `CaplHPapDdParam_Inputter` |  |  |  |
| 27 | `CAPL.DATE.TIME` | `CaplHPapDdParam_DateTime` |  |  |  |
| 28 | `CAPL.AUTHORISER` | `CaplHPapDdParam_Authoriser` | String |  |  |
| 29 | `CAPL.CO.CODE` | `CaplHPapDdParam_CoCode` | String |  |  |
| 30 | `CAPL.DEPT.CODE` | `CaplHPapDdParam_DeptCode` | String |  |  |
| 31 | `CAPL.AUDITOR.CODE` | `CaplHPapDdParam_AuditorCode` | String |  |  |
| 32 | `CAPL.AUDIT.DATE.TIME` | `CaplHPapDdParam_AuditDateTime` | String |  |  |
