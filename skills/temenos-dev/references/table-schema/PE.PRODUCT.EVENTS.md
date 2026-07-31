# PE.PRODUCT.EVENTS — Table Schema

> Source: `INSERTS/I_F.PE.PRODUCT.EVENTS` in `SC_ScPeFunds.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.PE.PROD.ISSUER` | `PeProductEvents_Issuer` | TField | Yes | Identifies the issuer of the Fund Validation Rules: Input should be a valid id from CUSTOMER table Mandatory field Nochange field |
| 2 | `SC.PE.PROD.ISSUER.ACC` | `PeProductEvents_IssuerAcc` | TField |  | Identifies the account of fund issuer. All issuer entries would be posted to this account Nostro Account of the Security Currency will be defaulted to this field if left blank Validation error will be triggered if nostro account is not found and if left blank Validation Rules: Input should be a valid id from ACCOUNT table Nochange field |
| 3 | `SC.PE.PROD.CAPITAL.CALL.REF` | `PeProductEvents_CapitalCallRef` |  |  |  |
| 4 | `SC.PE.PROD.CAPITAL.CALL.DATE` | `PeProductEvents_CapitalCallDate` | TField | Yes | This field holds the date on which Capital Call for the PE fund is issued System throws validation error "Input missing,check values for Capital Call" if CAPITAL.CALL.DATE field is inputted and if CAPITAL.CALL.REF, PAYMENT.DATE, CAPITAL.CALL.PERCENTAGE are missing System also checks if CAPITAL.CALL.REF, PAYMENT.DATE, CAPITAL.CALL.PERCENTAGE are inputted, and if CAPITAL.CALL.DATE is missing Validation Rules: Standard T24 Date field Mandatory field for Capital call event |
| 5 | `SC.PE.PROD.PAYMENT.DATE` | `PeProductEvents_PaymentDate` | TField | Yes | This field holds the date on which the customer has to make payment for the PE fund System throws validation error "Input missing,check values for Capital Call" if PAYMENT.DATE field is inputted and if any of CAPITAL.CALL.REF, CAPITAL.CALL.DATE,CAPITAL.CALL.PERCENTAGE are missing System also checks if CAPITAL.CALL.REF, CAPITAL.CALL.PERCENTAGE , CAPITAL.CALL.DATE are inputted, and if CAPITAL.CALL.PERCENTAGE is missing Validation Rules: Standard T24 Rate field Mandatory field for Capital call event |
| 6 | `SC.PE.PROD.CAPITAL.CALL.PERCENTAGE` | `PeProductEvents_CapitalCallPercentage` | TField | Yes | Capital Calls are issued in tranches. This field holds the percentage of the commitment that is being drawn down.This percentage is applied on the commitment of each customer to determine the amount due from each of them System throws validation error "Input missing,check values for Capital Call" if CAPITAL.CALL.PERCENTAGE field is inputted and if any of CAPITAL.CALL.REF, PAYMENT.DATE, CAPITAL.CALL.PERCENTAGE are missing System also checks if CAPITAL.CALL.REFERENCE, PAYMENT.DATE, CAPITAL.CALL.PERCENTAGE are inputted, and if CAPITAL.CALL.DATE is missing Validation Rules: Standard T24 Date field Mandatory field for Capital call event |
| 7 | `SC.PE.PROD.ACTUAL.PE.PRICE` | `PeProductEvents_ActualPePrice` | TField |  | This field identifies the price to be used when UNITS.ISSUED is set to YES. i.e. Units are issued at this NAV Defaulted to 1 if left blank This price will be passed to PRICE field of SECURITY.TRANSFER during Capital call and to PRICE field of SEC.TRADE for Capital Return event when UNITS.ISSUED is YES Validation Rules: Standard T24 Price field |
| 8 | `SC.PE.PROD.UNITS.ISSUED` | `PeProductEvents_UnitsIssued` | TField |  | This field indicates that the PE fund has received the contribution from the subscribers and then allots/issues units to the fund subscribers This field should be set to NO for a fresh capital call, and can be amended from NO to YES when the allotment of Units happens subsequently Validation Rules: Values accepted are YES , NO |
| 9 | `SC.PE.PROD.UNITS.ISSUE.DATE` | `PeProductEvents_UnitsIssueDate` | TField | Yes | This field indicates that the date on which the units are alloted to the subscribers of PE fund Validation Rules: Standard T24 Date field Mandatory when UNITS.ISSUED is set to YES |
| 10 | `SC.PE.PROD.RETURN.OF.CAPITAL.PERC` | `PeProductEvents_ReturnOfCapitalPerc` | TField | Yes | This field holds the percentage of capital amount being returned Validation Rules: Standard T24 Rate field Mandatory for Capital Return event Validation error "Input missing, check values for Capital Return" will be thrown when RETURN.OF.CAPITAL.PERC is inputted and if any one of PERCENTAGE.BASIS, RETURN.DATE are missing System also checks if PERCENTAGE.BASIS, RETURN.DATE are inputted, and if value of this field is missing |
| 11 | `SC.PE.PROD.PERCENTAGE.BASIS` | `PeProductEvents_PercentageBasis` | TField | Yes | This field identifies on which amount, the return of capital call amount is to be calculated Validation Rules: Options allowed are INITIAL COMMITMENT , LAST CONTRIBUTION Mandatory for Capital Return event If the value of this field is INITIAL.COMMITMENT, then the return amount will be calcualted as below Return Amount = RETURN.OF.CAPITAL.PERC * Commitment Amount / 100 if the value is LAST CONTRIBUTION, then the return amount will be calcualted as below Return Amount = RETURN.OF.CAPITAL.PERC * Amount of latest capital call/ 100 Validation error "Input missing, check values for Capital Return" will be thrown when PERCENTAGE.BASIS is inputted and if any one of RETURN.OF.CAPITAL.PERC, RETURN.DATE are missing System also checks if RETURN.OF.CAPITAL.PERC, RETURN.DATE are inputted, and if value of this field is missing |
| 12 | `SC.PE.PROD.INTEREST.PERC.ROC` | `PeProductEvents_InterestPercRoc` | TField | Yes | This field identifies interest rate to be used for calcualtion of interst amount that the customer is to receive after capital Return event Validation Rules: Standard T24 Rate field Mandatory for Capital Return event Validation error "Input missing, check values for Capital Return" will be thrown when INTEREST.PERC.ROC is inputted and if any one of RETURN.OF.CAPITAL.PERC, PERCENTAGE.BASIS, RETURN.DATE are missing System also checks if RETURN.OF.CAPITAL.PERC, PERCENTAGE.BASIS, RETURN.DATE are inputted, and if value of this field is missing |
| 13 | `SC.PE.PROD.RETURN.DATE` | `PeProductEvents_ReturnDate` | TField | Yes | This field identifies the date on which the capital return is being done Validation Rules: Standard T24 Date field Mandatory for Capital Return event Validation error "Input missing, check values for Capital Return" will be thrown when RETURN.DATE is inputted and if any one of RETURN.OF.CAPITAL.PERC, PERCENTAGE.BASIS are missing System also checks if RETURN.OF.CAPITAL.PERC, PERCENTAGE.BASIS are inputted, and if value of this field is missing |
| 14 | `SC.PE.PROD.COMMIT.REDN.PERC` | `PeProductEvents_CommitRednPerc` | TField | Yes | This field identifies the percentage of commitment amount to be reduced form Initial commitment amount Validation Rules: Standard T24 Rate field Mandatory for Commitment Reduction event Validation error "Input Missing for event" will be thrown when COMMIT.REDN.PERC is inputted without COMMIT.REDN.DATE |
| 15 | `SC.PE.PROD.COMMIT.REDN.DATE` | `PeProductEvents_CommitRednDate` | TField | Yes | This field identifies the date on which commitment reduction event happens Validation Rules: Standard T24 Date field Mandatory for Commitment Reduction event Validation error "Input Missing for event" will be thrown when COMMIT.REDN.DATE is inputted without COMMIT.REDN.RATE |
| 16 | `SC.PE.PROD.MATURITY.PRICE` | `PeProductEvents_MaturityPrice` | TField | Yes | This field identifies the final price or NAV at which the PE fund is redeemed Validation Rules: Standard T24 Price field Mandatory for Maturity event Validation error "Cant Initiate Event, capital call not done" will be thrown when maturity event is triggered before Capital Call event Validation error "Input Missing for event" will be triggered when MATURITY.PRICE is given without MATURITY.DATE |
| 17 | `SC.PE.PROD.MATURITY.DATE` | `PeProductEvents_MaturityDate` | TField | Yes | This field identifies the date on which Maturity of PE Fund happens Validation Rules: Standard T24 Date field Mandatory for Maturity event Validation error "Input Missing for event" will be thrown when MATURITY.DATE is inputted without MATURITY.PRICE |
| 18 | `SC.PE.PROD.MGMT.FEE.FREQ` | `PeProductEvents_MgmtFeeFreq` | TField | No | This field holds the frequency of Management Fees PE.MANAGEMENT.FEES records for customers who subscribed for PE fund will be automatically created by system on this frequency date Validation Rules: Standard T24 Freqency field Optional field |
| 19 | `SC.PE.PROD.MGMT.FEE.CODE` | `PeProductEvents_MgmtFeeCode` | TField | No | The management fee(FT.COMMISSION.TYPE) is defined in this field. The fee would be calculated based on this field on frequency as specified in the field MGMT.FEE.FREQ and PE.MANAGEMENT.FEES records would be created for the user review Validation Rules: Input should be a valid FT.COMMISSION.TYPE id Optional field The debit Account number of FT record created for Management fees will be mapped from either PL category or an iternal Account of FT.COMMISSION.TYPE record of this value The management fees amount will be calcualted by record of this value from FT.COMMISSION.TYPE |
| 20 | `SC.PE.PROD.MGMT.FEE.OFFSET` | `PeProductEvents_MgmtFeeOffset` | TField | No | This field holds the offset between the fee calculation date and fee value date, and is specified interms of Working days Validation Rules: Input should be a Numeric value of length 3 Optional field VALUE.DATE of the accounting entries generated for PE Management fees will be calculated by this field |
| 21 | `SC.PE.PROD.UNDRAWN.SECURITY` | `PeProductEvents_UndrawnSecurity` | TField |  | This field holds the id of PE fund with PE.TYPE as DRAWDOWN. Value will be defaulted from DRAWDOWN PE fund which is related to id of the record which is INITIAL COMMITMENT PE fund Validation Rules: Value should be id of SECURITY.MASTER record whose PE.TYPE is DRAWDOWN Validation error "Missing Undrawn Security SetUp" will be triggered when the PE.FUND of this field value is not a DRAWDOWN |
| 22 | `SC.PE.PROD.CAPITAL.SECURITY` | `PeProductEvents_CapitalSecurity` | TField |  | This field holds the id of PE fund with PE.TYPE as CAPITAL CALL. Value will be defaulted from CAPITAL CALL PE fund which is related to id of the record which is INITIAL COMMITMENT PE fund Validation Rules: Value should be id of SECURITY.MASTER record whose PE.TYPE is CAPITAL CALL Validation error "Missing Undrawn Security SetUp" will be triggered when the PE.FUND of this field value is not a CAPITAL CALL |
| 23 | `SC.PE.PROD.ACTUAL.PE.SECURITY` | `PeProductEvents_ActualPeSecurity` | TField |  | This field holds the id of PE fund with PE.TYPE as ACTUAL PE SECURITY. Value will be defaulted from ACTUAL PE SECURITY fund which is related to id of the record which is INITIAL COMMITMENT PE fund Validation Rules: Value should be id of SECURITY.MASTER record whose PE.TYPE is ACTUAL PE SECURITY Validation error "Missing Undrawn Security SetUp" will be triggered when the PE.FUND of this field value is not a ACTUAL PE SECURITY |
| 24 | `SC.PE.PROD.NEXT.FREQ.DATE` | `PeProductEvents_NextFreqDate` | TField |  | This field holds the nextS frequency date on which the Management fees will be calculated and records will be created Value will be automatically calculated by system and used for Management fees Validation Rules: Noinput, System updated field Standard T24 Date field |
| 25 | `SC.PE.PROD.SAVE.CAP.CALL.REF` | `PeProductEvents_SaveCapCallRef` |  |  |  |
| 26 | `SC.PE.PROD.SAVE.CAP.CALL.DATE` | `PeProductEvents_SaveCapCallDate` |  |  |  |
| 27 | `SC.PE.PROD.SAVE.PAYMENT.DATE` | `PeProductEvents_SavePaymentDate` |  |  |  |
| 28 | `SC.PE.PROD.SAVE.CAP.CALL.PERC` | `PeProductEvents_SaveCapCallPerc` |  |  |  |
| 29 | `SC.PE.PROD.SAVE.UNITS.ISSUED` | `PeProductEvents_SaveUnitsIssued` |  |  |  |
| 30 | `SC.PE.PROD.SAVE.UNITS.ISSUE.DATE` | `PeProductEvents_SaveUnitsIssueDate` |  |  |  |
| 31 | `SC.PE.PROD.SAVE.RETURN.OF.CAP.PERC` | `PeProductEvents_SaveReturnOfCapPerc` |  |  |  |
| 32 | `SC.PE.PROD.SAVE.PERCENTAGE.BASIS` | `PeProductEvents_SavePercentageBasis` |  |  |  |
| 33 | `SC.PE.PROD.SAVE.INT.PERC.ROC` | `PeProductEvents_SaveIntPercRoc` |  |  |  |
| 34 | `SC.PE.PROD.SAVE.RETURN.DATE` | `PeProductEvents_SaveReturnDate` |  |  |  |
| 35 | `SC.PE.PROD.SAVE.COMMIT.REDN.PERC` | `PeProductEvents_SaveCommitRednPerc` |  |  |  |
| 36 | `SC.PE.PROD.SAVE.COMMIT.REDN.DATE` | `PeProductEvents_SaveCommitRednDate` |  |  |  |
| 37 | `SC.PE.PROD.SAVE.MATURITY.PRICE` | `PeProductEvents_SaveMaturityPrice` |  |  |  |
| 38 | `SC.PE.PROD.SAVE.MATURITY.DATE` | `PeProductEvents_SaveMaturityDate` |  |  |  |
| 39 | `SC.PE.PROD.RESERVED1` | `PeProductEvents_Reserved1` |  |  |  |
| 40 | `SC.PE.PROD.RESERVED2` | `PeProductEvents_Reserved2` |  |  |  |
| 41 | `SC.PE.PROD.RESERVED3` | `PeProductEvents_Reserved3` |  |  |  |
| 42 | `SC.PE.PROD.RESERVED4` | `PeProductEvents_Reserved4` |  |  |  |
| 43 | `SC.PE.PROD.RESERVED5` | `PeProductEvents_Reserved5` |  |  |  |
| 44 | `SC.PE.PROD.RESERVED6` | `PeProductEvents_Reserved6` |  |  |  |
| 45 | `SC.PE.PROD.RESERVED7` | `PeProductEvents_Reserved7` |  |  |  |
| 46 | `SC.PE.PROD.RESERVED8` | `PeProductEvents_Reserved8` |  |  |  |
| 47 | `SC.PE.PROD.RESERVED9` | `PeProductEvents_Reserved9` |  |  |  |
| 48 | `SC.PE.PROD.RESERVED10` | `PeProductEvents_Reserved10` |  |  |  |
| 49 | `SC.PE.PROD.RESERVED11` | `PeProductEvents_Reserved11` |  |  |  |
| 50 | `SC.PE.PROD.RESERVED12` | `PeProductEvents_Reserved12` |  |  |  |
| 51 | `SC.PE.PROD.RESERVED13` | `PeProductEvents_Reserved13` |  |  |  |
| 52 | `SC.PE.PROD.RESERVED14` | `PeProductEvents_Reserved14` |  |  |  |
| 53 | `SC.PE.PROD.RESERVED15` | `PeProductEvents_Reserved15` |  |  |  |
| 54 | `SC.PE.PROD.RESERVED16` | `PeProductEvents_Reserved16` |  |  |  |
| 55 | `SC.PE.PROD.RESERVED17` | `PeProductEvents_Reserved17` |  |  |  |
| 56 | `SC.PE.PROD.RESERVED18` | `PeProductEvents_Reserved18` |  |  |  |
| 57 | `SC.PE.PROD.RESERVED19` | `PeProductEvents_Reserved19` |  |  |  |
| 58 | `SC.PE.PROD.RESERVED20` | `PeProductEvents_Reserved20` |  |  |  |
| 59 | `SC.PE.PROD.RESERVED21` | `PeProductEvents_Reserved21` |  |  |  |
| 60 | `SC.PE.PROD.RESERVED22` | `PeProductEvents_Reserved22` |  |  |  |
| 61 | `SC.PE.PROD.RESERVED23` | `PeProductEvents_Reserved23` |  |  |  |
| 62 | `SC.PE.PROD.RESERVED24` | `PeProductEvents_Reserved24` |  |  |  |
| 63 | `SC.PE.PROD.RESERVED25` | `PeProductEvents_Reserved25` |  |  |  |
| 64 | `SC.PE.PROD.RESERVED26` | `PeProductEvents_Reserved26` |  |  |  |
| 65 | `SC.PE.PROD.RESERVED27` | `PeProductEvents_Reserved27` | TField |  |  |
| 66 | `SC.PE.PROD.RESERVED28` | `PeProductEvents_Reserved28` | TField |  |  |
| 67 | `SC.PE.PROD.LOCAL.REF` | `PeProductEvents_LocalRef` |  |  |  |
| 68 | `SC.PE.PROD.STMT.NOS` | `PeProductEvents_StmtNos` |  |  |  |
| 69 | `SC.PE.PROD.OVERRIDE` | `PeProductEvents_Override` |  |  |  |
| 70 | `SC.PE.PROD.RECORD.STATUS` | `PeProductEvents_RecordStatus` | String |  |  |
| 71 | `SC.PE.PROD.CURR.NO` | `PeProductEvents_CurrNo` | String |  |  |
| 72 | `SC.PE.PROD.INPUTTER` | `PeProductEvents_Inputter` |  |  |  |
| 73 | `SC.PE.PROD.DATE.TIME` | `PeProductEvents_DateTime` |  |  |  |
| 74 | `SC.PE.PROD.AUTHORISER` | `PeProductEvents_Authoriser` | String |  |  |
| 75 | `SC.PE.PROD.CO.CODE` | `PeProductEvents_CoCode` | String |  |  |
| 76 | `SC.PE.PROD.DEPT.CODE` | `PeProductEvents_DeptCode` | String |  |  |
| 77 | `SC.PE.PROD.AUDITOR.CODE` | `PeProductEvents_AuditorCode` | String |  |  |
| 78 | `SC.PE.PROD.AUDIT.DATE.TIME` | `PeProductEvents_AuditDateTime` | String |  |  |
