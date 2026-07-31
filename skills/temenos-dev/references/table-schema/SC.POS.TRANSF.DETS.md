# SC.POS.TRANSF.DETS — Table Schema

> Source: `INSERTS/I_F.SC.POS.TRANSF.DETS` in `SC_SctOffMarketTrades.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.PTD.POSITION.TRANSFER.ID` | `ScPosTransfDets_PositionTransferId` | TField |  | Holds the Position Transfer id generated from the Bulk Transfer |
| 2 | `SC.PTD.PORTFOLIO.ID` | `ScPosTransfDets_PortfolioId` | TField |  | Holds the portfolio which is part of this bulk transfer |
| 3 | `SC.PTD.SECURITY.NO` | `ScPosTransfDets_SecurityNo` | TField |  | Holds the security code, defaulted from the Position Transfer |
| 4 | `SC.PTD.SECURITY.CCY` | `ScPosTransfDets_SecurityCcy` | TField |  | Holds the security currency |
| 5 | `SC.PTD.PF.OUT.REF.CCY` | `ScPosTransfDets_PfOutRefCcy` | TField |  | This is the Reference Currency of the Portfolio from where positions are being transferred. |
| 6 | `SC.PTD.PF.REF.IN.CCY` | `ScPosTransfDets_PfRefInCcy` | TField |  | This is the Reference Currency of the Portfolio to which the positions are being transferred to |
| 7 | `SC.PTD.DEPOSITORY` | `ScPosTransfDets_Depository` | TField |  | This is the depository from where positions are being transferred. |
| 8 | `SC.PTD.NOMINEE` | `ScPosTransfDets_Nominee` | TField |  | This is the Nominee code from where positions are being transferred. |
| 9 | `SC.PTD.MATURITY.DATE` | `ScPosTransfDets_MaturityDate` | TField |  | This is the Maturity date from where positions are being transferred. |
| 10 | `SC.PTD.INTEREST.RATE` | `ScPosTransfDets_InterestRate` | TField |  | This is the interest rate from where positions are being transferred. |
| 11 | `SC.PTD.SUB.ACCOUNT` | `ScPosTransfDets_SubAccount` | TField |  | Specifies the sub account which is going to be transferred |
| 12 | `SC.PTD.NO.NOMINAL` | `ScPosTransfDets_NoNominal` | TField |  | Quantity corresponding to this portfolio. Defaults from SC.BULK.TRANSFER if quantity is specified for thisportfolio. If quantity is not specified, the total holdings for this portfolio for this security on this custodiansecurity account would be defaulted |
| 13 | `SC.PTD.PRICE` | `ScPosTransfDets_Price` | TField |  | Holds the price at which the security is being held by the transferring party. |
| 14 | `SC.PTD.SHORT.POSITION` | `ScPosTransfDets_ShortPosition` | TField |  | Updated as 'Yes' if the transfer would result in a short position. |
| 15 | `SC.PTD.FROM.CUST.LEI.NCI` | `ScPosTransfDets_FromCustLeiNci` | TField |  | This field holds the LEI/NCI code of the customer from which positions are transferred. Mapped from the Bulk Transfer record |
