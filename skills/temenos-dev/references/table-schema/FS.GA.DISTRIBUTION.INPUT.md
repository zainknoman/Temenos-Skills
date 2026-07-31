# FS.GA.DISTRIBUTION.INPUT — Table Schema

> Source: `INSERTS/I_F.FS.GA.DISTRIBUTION.INPUT` in `FS_StaticData.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.DISTRIBUTION.INPUT.FUND.ID` | `FsGaDistributionInput_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 2 | `FS.GA.DISTRIBUTION.INPUT.SHARE.CLASS.CODE` | `FsGaDistributionInput_ShareClassCode` | TField |  | Share class Multifonds DB Column is TPARTS. |
| 3 | `FS.GA.DISTRIBUTION.INPUT.DATE.OF.NAV` | `FsGaDistributionInput_DateOfNav` | TField |  | Date of the NAV Multifonds DB Column is DATE_NAV. |
| 4 | `FS.GA.DISTRIBUTION.INPUT.DISTRIBUTION.DATE` | `FsGaDistributionInput_DistributionDate` | TField |  | Distribution Date Multifonds DB Column is DATE_DISTRIBUTION. |
| 5 | `FS.GA.DISTRIBUTION.INPUT.BS.GROUPING` | `FsGaDistributionInput_BsGrouping` | TField |  | Balance sheet grouping like Assets, Liabilities etc Multifonds DB Column is CTIF. |
| 6 | `FS.GA.DISTRIBUTION.INPUT.EQUALIZATION.CHART` | `FsGaDistributionInput_EqualizationChart` | TField |  | Enter equalization chart number. Multifonds DB Column is NRUBR_REGUL. |
| 7 | `FS.GA.DISTRIBUTION.INPUT.PRODUCT.AMOUNT` | `FsGaDistributionInput_ProductAmount` | TField |  | Product Amount Multifonds DB Column is MNT_PROD. |
| 8 | `FS.GA.DISTRIBUTION.INPUT.CHARGES.AMOUNT` | `FsGaDistributionInput_ChargesAmount` | TField |  | Refers to the Charges amount can enter manually to be taken into consideration on the report SDEGA19. Multifonds DB Column is MNT_FRAIS. |
| 9 | `FS.GA.DISTRIBUTION.INPUT.INPUTORDER` | `FsGaDistributionInput_Inputorder` | TField |  | This field has to be populated manually by users Multifonds DB Column is INPUTORDER. |
| 10 | `FS.GA.DISTRIBUTION.INPUT.NET.MNT` | `FsGaDistributionInput_NetMnt` | TField |  | Net Mnt Multifonds DB Column is MNT_NET. |
| 11 | `FS.GA.DISTRIBUTION.INPUT.RAN.EX1.AMOUNT` | `FsGaDistributionInput_RanEx1Amount` | TField |  | RAN EX1 Amount Multifonds DB Column is MNT_RAN_EX1. |
| 12 | `FS.GA.DISTRIBUTION.INPUT.DISTRIBUTION.AMOUNT` | `FsGaDistributionInput_DistributionAmount` | TField |  | Refers to the distribution amount Multifonds DB Column is MNT_DISTRIB. |
| 13 | `FS.GA.DISTRIBUTION.INPUT.UNIT.AMOUNT.CP` | `FsGaDistributionInput_UnitAmountCp` | TField |  | Unit Amount CP Multifonds DB Column is MNT_CP_UNIT. |
| 14 | `FS.GA.DISTRIBUTION.INPUT.DISTRIBUTION.AMOUNT.REV` | `FsGaDistributionInput_DistributionAmountRev` | TField |  | Distribution Amount REV Multifonds DB Column is MNT_REV_DISTRIB. |
| 15 | `FS.GA.DISTRIBUTION.INPUT.DIVIDEND.DISTRIBUTION.AMOUNT` | `FsGaDistributionInput_DividendDistributionAmount` | TField |  | Users can enter manually an Unit Dividend amount Multifonds DB Column is MNT_UNIT_DISTRIB. |
| 16 | `FS.GA.DISTRIBUTION.INPUT.UNIT.AMOUNT.DECIMAL` | `FsGaDistributionInput_UnitAmountDecimal` | TField |  | Unit Amount Decimal Multifonds DB Column is MNT_UNIT_DEC. |
| 17 | `FS.GA.DISTRIBUTION.INPUT.AFCI.AMOUNT` | `FsGaDistributionInput_AfciAmount` | TField |  | AFCI Amount Multifonds DB Column is MNT_AFCI. |
| 18 | `FS.GA.DISTRIBUTION.INPUT.AFCI.REPORT` | `FsGaDistributionInput_AfciReport` | TField |  | This field automatically populated with the sum of the account balances linked to an equalization chart category and for which the check box 'A.F/C.I' is flagged. Multifonds DB Column is MNT_AFCI_REPORT. |
| 19 | `FS.GA.DISTRIBUTION.INPUT.AFCI.TOTAL.AMOUNT` | `FsGaDistributionInput_AfciTotalAmount` | TField |  | AFCI Total Amount Multifonds DB Column is MNT_AFCI_TOTAL. |
| 20 | `FS.GA.DISTRIBUTION.INPUT.AFCI.UNIT` | `FsGaDistributionInput_AfciUnit` | TField |  | AFCI Unit Multifonds DB Column is AFCI_UNIT. |
| 21 | `FS.GA.DISTRIBUTION.INPUT.AFCI.RGRP` | `FsGaDistributionInput_AfciRgrp` | TField |  | Users can enter manually an Unit Dividend amount. Multifonds DB Column is AFCI_RGRP. |
| 22 | `FS.GA.DISTRIBUTION.INPUT.AFCI.RETENU` | `FsGaDistributionInput_AfciRetenu` | TField |  | Users can enter manually an 'Avoir Fiscal Credit Imports return. Multifonds DB Column is MNT_AFCI_CAT. |
| 23 | `FS.GA.DISTRIBUTION.INPUT.REPORT.EX.AMOUNT` | `FsGaDistributionInput_ReportExAmount` | TField |  | Report EX Amount Multifonds DB Column is MNT_REPORTEX. |
| 24 | `FS.GA.DISTRIBUTION.INPUT.AFCI.MAX` | `FsGaDistributionInput_AfciMax` | TField |  | Users can enter manually a maximum 'Avoir Fiscal Credit Imports Multifonds DB Column is AFCI_MAX. |
| 25 | `FS.GA.DISTRIBUTION.INPUT.RESERVED10` | `FsGaDistributionInput_Reserved10` | TField |  |  |
| 26 | `FS.GA.DISTRIBUTION.INPUT.RESERVED9` | `FsGaDistributionInput_Reserved9` | TField |  |  |
| 27 | `FS.GA.DISTRIBUTION.INPUT.RESERVED8` | `FsGaDistributionInput_Reserved8` | TField |  |  |
| 28 | `FS.GA.DISTRIBUTION.INPUT.RESERVED7` | `FsGaDistributionInput_Reserved7` | TField |  |  |
| 29 | `FS.GA.DISTRIBUTION.INPUT.RESERVED6` | `FsGaDistributionInput_Reserved6` | TField |  |  |
| 30 | `FS.GA.DISTRIBUTION.INPUT.RESERVED5` | `FsGaDistributionInput_Reserved5` | TField |  |  |
| 31 | `FS.GA.DISTRIBUTION.INPUT.RESERVED4` | `FsGaDistributionInput_Reserved4` | TField |  |  |
| 32 | `FS.GA.DISTRIBUTION.INPUT.RESERVED3` | `FsGaDistributionInput_Reserved3` | TField |  |  |
| 33 | `FS.GA.DISTRIBUTION.INPUT.RESERVED2` | `FsGaDistributionInput_Reserved2` | TField |  |  |
| 34 | `FS.GA.DISTRIBUTION.INPUT.RESERVED1` | `FsGaDistributionInput_Reserved1` | TField |  |  |
| 35 | `FS.GA.DISTRIBUTION.INPUT.RECORD.STATUS` | `FsGaDistributionInput_RecordStatus` | String |  |  |
| 36 | `FS.GA.DISTRIBUTION.INPUT.CURR.NO` | `FsGaDistributionInput_CurrNo` | String |  |  |
| 37 | `FS.GA.DISTRIBUTION.INPUT.INPUTTER` | `FsGaDistributionInput_Inputter` |  |  |  |
| 38 | `FS.GA.DISTRIBUTION.INPUT.DATE.TIME` | `FsGaDistributionInput_DateTime` |  |  |  |
| 39 | `FS.GA.DISTRIBUTION.INPUT.AUTHORISER` | `FsGaDistributionInput_Authoriser` | String |  |  |
| 40 | `FS.GA.DISTRIBUTION.INPUT.CO.CODE` | `FsGaDistributionInput_CoCode` | String |  |  |
| 41 | `FS.GA.DISTRIBUTION.INPUT.DEPT.CODE` | `FsGaDistributionInput_DeptCode` | String |  |  |
| 42 | `FS.GA.DISTRIBUTION.INPUT.AUDITOR.CODE` | `FsGaDistributionInput_AuditorCode` | String |  |  |
| 43 | `FS.GA.DISTRIBUTION.INPUT.AUDIT.DATE.TIME` | `FsGaDistributionInput_AuditDateTime` | String |  |  |
