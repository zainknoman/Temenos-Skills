*-----------------------------------------------------------------------------
* Program    : V.GOLDEN.VAR
* Type       : VAR
* Description: Golden case
* Application: FUNDS.TRANSFER
*
* Modification History:
* Date       | Author          | Description
* -----------|-----------------|--------------------------------------------
* 2026-10-02 | golden-case | Initial version
*-----------------------------------------------------------------------------
$PACKAGE GOLDEN.Legacy
    SUBROUTINE V.GOLDEN.VAR
    $INSERT I_COMMON
    $INSERT I_EQUATE
    $INSERT I_F.FUNDS.TRANSFER
    $INSERT I_F.ACCOUNT

    FN.LINK = 'F.ACCOUNT'
    F.LINK = ''
    CALL OPF(FN.LINK, F.LINK)

    Y.LINK.ID = R.NEW(FT.DEBIT.ACCT.NO)
    R.LINK = ''
    Y.READ.ERR = ''
    CALL F.READ(FN.LINK, Y.LINK.ID, R.LINK, F.LINK, Y.READ.ERR)
    IF Y.READ.ERR NE '' OR R.LINK<AC.CATEGORY> EQ '' THEN
        ETEXT = 'DEBIT ACCOUNT HAS NO CATEGORY'
        CALL STORE.END.ERROR
    END
    RETURN
END
