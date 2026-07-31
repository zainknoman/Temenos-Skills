# CAPL.H.TX.XML.PARMS — Table Schema

> Source: `INSERTS/I_F.CAPL.H.TX.XML.PARMS` in `CADEPO_CRAReporting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAPL.TXP.GIT.HEADER` | `CaplHTxXmlParms_GitHeader` | TField |  | This field is used to define the header for the xml file generated.Valid record from DFE.MAPPING.E.g. NR4.HEADER |
| 2 | `CAPL.TXP.GIT.GROUP` | `CaplHTxXmlParms_GitGroup` | TField |  | This field is used to define the dfe group for the tax slip.Valid record from DFE.MAPPING.E.g NR4.SLIPS |
| 3 | `CAPL.TXP.GIT.DETAIL` | `CaplHTxXmlParms_GitDetail` | TField |  | This field is used to define the tax slip detail for the xml generated.Valid record from DFE.MAPPING.E.g. NR4.SLIPS |
| 4 | `CAPL.TXP.GIT.FOOTER` | `CaplHTxXmlParms_GitFooter` | TField |  | This field is used to define the footer for the xml file generated.Valid record from DFE.MAPPING.E.g. NR4.SUMMARY |
| 5 | `CAPL.TXP.OUT.DIR` | `CaplHTxXmlParms_OutDir` | TField |  | This field is used to define the directory to which the xml file to be generated.Valid directory to be defined here.E.g. .\bnk.interface\TAXATION.BP |
| 6 | `CAPL.TXP.OUT.FILE` | `CaplHTxXmlParms_OutFile` | TField |  | Filed is used to define the out file name for the xml which is to be generated in the out directory.Valid file name to be defined.E.g. NR4BNK-A.xml |
| 7 | `CAPL.TXP.SEL.CRITERIA` | `CaplHTxXmlParms_SelCriteria` |  |  |  |
| 8 | `CAPL.TXP.HEADER.TAGS` | `CaplHTxXmlParms_HeaderTags` |  |  |  |
| 9 | `CAPL.TXP.INTER.HEADER.TAGS` | `CaplHTxXmlParms_InterHeaderTags` |  |  |  |
| 10 | `CAPL.TXP.INTER.FOOTER.TAGS` | `CaplHTxXmlParms_InterFooterTags` |  |  |  |
| 11 | `CAPL.TXP.FOOTER.TAGS` | `CaplHTxXmlParms_FooterTags` |  |  |  |
| 12 | `CAPL.TXP.L3.SWITCH` | `CaplHTxXmlParms_L3Switch` | TField |  |  |
| 13 | `CAPL.TXP.RESERVED.4` | `CaplHTxXmlParms_Reserved4` | TField |  |  |
| 14 | `CAPL.TXP.RESERVED.3` | `CaplHTxXmlParms_Reserved3` | TField |  |  |
| 15 | `CAPL.TXP.RESERVED.2` | `CaplHTxXmlParms_Reserved2` | TField |  |  |
| 16 | `CAPL.TXP.RESERVED.1` | `CaplHTxXmlParms_Reserved1` | TField |  |  |
| 17 | `CAPL.TXP.RECORD.STATUS` | `CaplHTxXmlParms_RecordStatus` | String |  |  |
| 18 | `CAPL.TXP.CURR.NO` | `CaplHTxXmlParms_CurrNo` | String |  |  |
| 19 | `CAPL.TXP.INPUTTER` | `CaplHTxXmlParms_Inputter` |  |  |  |
| 20 | `CAPL.TXP.DATE.TIME` | `CaplHTxXmlParms_DateTime` |  |  |  |
| 21 | `CAPL.TXP.AUTHORISER` | `CaplHTxXmlParms_Authoriser` | String |  |  |
| 22 | `CAPL.TXP.CO.CODE` | `CaplHTxXmlParms_CoCode` | String |  |  |
| 23 | `CAPL.TXP.DEPT.CODE` | `CaplHTxXmlParms_DeptCode` | String |  |  |
| 24 | `CAPL.TXP.AUDITOR.CODE` | `CaplHTxXmlParms_AuditorCode` | String |  |  |
| 25 | `CAPL.TXP.AUDIT.DATE.TIME` | `CaplHTxXmlParms_AuditDateTime` | String |  |  |
