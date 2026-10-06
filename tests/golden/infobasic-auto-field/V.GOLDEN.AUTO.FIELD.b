*-----------------------------------------------------------------------------
* Program    : V.GOLDEN.AUTO.FIELD
* Type       : AUTO.NEW.CONTENT
* Description: Golden case
* Application: FUNDS.TRANSFER
*
* Modification History:
* Date       | Author          | Description
* -----------|-----------------|--------------------------------------------
* 2026-10-02 | golden-case | Initial version
*-----------------------------------------------------------------------------
$PACKAGE GOLDEN.Legacy
    SUBROUTINE V.GOLDEN.AUTO.FIELD
    $INSERT I_COMMON
    $INSERT I_EQUATE
    $INSERT I_F.FUNDS.TRANSFER
    $INSERT I_F.ACCOUNT

    Y.LINK.ID = R.NEW(FT.DEBIT.ACCT.NO)
    IF Y.LINK.ID EQ '' THEN RETURN

    FN.LINK = 'F.ACCOUNT'
    F.LINK = ''
    CALL OPF(FN.LINK, F.LINK)
    R.LINK = ''
    Y.READ.ERR = ''
    CALL F.READ(FN.LINK, Y.LINK.ID, R.LINK, F.LINK, Y.READ.ERR)
    IF Y.READ.ERR EQ '' THEN
        R.NEW(FT.DEBIT.CURRENCY) = R.LINK<AC.CURRENCY>
    END
    RETURN
END
