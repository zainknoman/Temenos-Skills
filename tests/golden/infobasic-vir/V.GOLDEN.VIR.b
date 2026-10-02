*-----------------------------------------------------------------------------
* Program    : V.GOLDEN.VIR
* Type       : VIR
* Description: Golden case
* Application: CUSTOMER
*
* Modification History:
* Date       | Author          | Description
* -----------|-----------------|--------------------------------------------
* 2026-10-02 | golden-case | Initial version
*-----------------------------------------------------------------------------
$PACKAGE GOLDEN.Legacy
    SUBROUTINE V.GOLDEN.VIR
    $INSERT I_COMMON
    $INSERT I_EQUATE
    $INSERT I_F.CUSTOMER

    Y.VALUE = R.NEW(EB.CUS.SECTOR)
    IF Y.VALUE EQ '' THEN
        AF = EB.CUS.SECTOR
        ETEXT = 'SECTOR IS MANDATORY'
        CALL STORE.END.ERROR
    END
    RETURN
END
