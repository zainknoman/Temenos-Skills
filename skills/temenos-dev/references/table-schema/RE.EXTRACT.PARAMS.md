# RE.EXTRACT.PARAMS — Table Schema

> Source: `INSERTS/I_F.RE.EXTRACT.PARAMS` in `RE_ReportExtraction.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `RE.EXP.REP.LINE.NARR` | `ReExtractParams_RepLineNarr` |  |  |  |
| 2 | `RE.EXP.ASSET.KEY.POS` | `ReExtractParams_AssetKeyPos` |  |  |  |
| 3 | `RE.EXP.PROFIT.KEY.POS` | `ReExtractParams_ProfitKeyPos` |  |  |  |
| 4 | `RE.EXP.CONSOL.KEY.IN.REC` | `ReExtractParams_ConsolKeyInRec` | A (alphanumeric) | Yes | This field indicates whether the consolidation key is to be stored in the output disk file or not. A value of YES in this field results in the consolidation key being output to the disk file created by RE.RETURN.EXTRACT. Validation Rules: Up to 3 type A (alphanumeric) characters. Allowed values are YES or NO. (Mandatory input.) |
| 5 | `RE.EXP.MAT.DATE.RANGE` | `ReExtractParams_MatDateRange` |  |  |  |
| 6 | `RE.EXP.AMOUNT.TYPE` | `ReExtractParams_AmountType` | A (alphanumeric) | Yes | Indicates whether the closing balance or the day's movements are to be stored in the output file. The amount to be output in the disk file is mentioned here. If this field has a value of CLOSING then the closing balance of each consolidation key is stored. In case the value is MOVEMENT, net of the day's movements is stored in the output file. Validation Rules: Up to 8 type A (alphanumeric) characters. Allowed values are CLOSING or MOVEMENT. (Mandatory input.) |
| 7 | `RE.EXP.CONTRACT.DETAILS` | `ReExtractParams_ContractDetails` | TField |  | Specifies whether records created should contain details from Consolidated files in the CRB base, or should contain individual contract balances and details relevant to the CRB line definition. A value of NO will result in records containing the balance details from the CONSOLIDATE.ASST.LIAB / PRFT.LOSS files only. In this case the extract records will be keyed by sequence number only. A value of YES will result in individual contract balances for the relevant asset type of contracts being output. Additional information output when YES is used is: ID : Sequence * Contract Id * Asset Type CUSTOMER id Deal Balance in deal currency Deal Balance in local currency Interest / Exchange Rate Value Date Maturity Date Initial Term in Days Reamaining Term in days These fields are appended to the end of the exisiting record. |
| 8 | `RE.EXP.INC.CONSOL.DETAIL` | `ReExtractParams_IncConsolDetail` | TField | No | Specifies whether the balance fields LOCAL.BALANCE and FOREIGN.BALANCE should be populated for transaction level records. Transaction level records are created when the CONTRACT.DETAILS field is set to YES. If this is set two types of extract record will be produced: Consolidated records identified by a numeric only key These records contain the Consolidated Balance for the asset type from the CONSOLIDATE.ASST.LIAB file. The fields LOCAL.BALANCE and FOREIGN.BALANCE contain the consolidated balance. For profit and loss records the total from the CONSOLIDATE.PRFT.LOSS file is held in the fields LOCAL.BALANCE and FOREIGN.BALANCE. Transaction or P&amp;L consolidated records identified by a key containing the deal number and application separated by a '*' For a deal the DEAL.BALANCE and DEAL.LCY.BALANCE will be populated. If this field is set to YES the LOCAL.BALANCE and FOREIGN.BALANCE will also be populated. For a P&amp;L level consolidated record fields DEAL.BALANCE and DEAL.LCY.BALANCE will be populated, if this field is set to YES the LOCAL.BALANCE and FOREIGN.BALANCE will also be populated. Validation Rules: Optional field Possible values YES, NO or null. |
| 9 | `RE.EXP.INCL.PERIOD.END` | `ReExtractParams_InclPeriodEnd` | TField |  | Validation Rules: |
| 10 | `RE.EXP.PL.DETAILS` | `ReExtractParams_PlDetails` | TField |  | Help Text for this field is unavailable.Please refer to the T24 User Guides for further information. |
| 11 | `RE.EXP.KEY.FORMAT` | `ReExtractParams_KeyFormat` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 12 | `RE.EXP.CRB.REPORT` | `ReExtractParams_CrbReport` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 13 | `RE.EXP.OPTIONS` | `ReExtractParams_Options` |  |  |  |
| 14 | `RE.EXP.CRB.FILE.LEVEL` | `ReExtractParams_CrbFileLevel` | TField |  | This field determines at which level the CRB flat files are generated. It has 2 options FIN and FRP and the default option is FRP. A value of "FRP" will generate the CRB flat files at Branch(Book) level while running either with online service or as part COB. A value of "FIN" will generate the CRB flat files at lead company level including the branch(Book) details while running either with the online service or as part of COB And Defaults to "FRP" when this field is left blank |
| 15 | `RE.EXP.CSV.FILE.FORMAT` | `ReExtractParams_CsvFileFormat` | TField |  | This field enables to generate CRB report information as sequential file (CSV) and this is used only in case of DW.EXPORT application configured at the company level for Insight product. A value of "Y" will generate the CRB report as sequential file instead of generating in normal flat files Allowed input as "Y" only when CRB.FILE.LEVEL has the value of "FIN" Defaults to null |
| 16 | `RE.EXP.LOCAL.REF` | `ReExtractParams_LocalRef` |  |  |  |
| 17 | `RE.EXP.CONTRT.ZERO.SUPP` | `ReExtractParams_ContrtZeroSupp` | TField |  | Indicates whether the CRF flat file (RE.CRF.REPORT.NAME) needs to be updated for the accounts/ contracts when the balances are zero A value of YES will not write the CRF extract file with the account/contract records with zero balances A value of NO will update the CRF flat file even if the contracts' balances are zero Defaults to YES |
| 18 | `RE.EXP.RESERVED.2` | `ReExtractParams_Reserved2` | TField |  |  |
| 19 | `RE.EXP.OVERRIDE` | `ReExtractParams_Override` |  |  |  |
| 20 | `RE.EXP.RECORD.STATUS` | `ReExtractParams_RecordStatus` | String |  |  |
| 21 | `RE.EXP.CURR.NO` | `ReExtractParams_CurrNo` | String |  |  |
| 22 | `RE.EXP.INPUTTER` | `ReExtractParams_Inputter` |  |  |  |
| 23 | `RE.EXP.DATE.TIME` | `ReExtractParams_DateTime` |  |  |  |
| 24 | `RE.EXP.AUTHORISER` | `ReExtractParams_Authoriser` | String |  |  |
| 25 | `RE.EXP.CO.CODE` | `ReExtractParams_CoCode` | String |  |  |
| 26 | `RE.EXP.DEPT.CODE` | `ReExtractParams_DeptCode` | String |  |  |
| 27 | `RE.EXP.AUDITOR.CODE` | `ReExtractParams_AuditorCode` | String |  |  |
| 28 | `RE.EXP.AUDIT.DATE.TIME` | `ReExtractParams_AuditDateTime` | String |  |  |
