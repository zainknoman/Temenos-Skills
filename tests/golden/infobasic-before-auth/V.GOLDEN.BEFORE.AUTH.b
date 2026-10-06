*-----------------------------------------------------------------------------
* Program    : V.GOLDEN.BEFORE.AUTH
* Type       : BEFORE.AUTH.RTN
* Description: Golden case
* Application: CUSTOMER
*
* Modification History:
* Date       | Author          | Description
* -----------|-----------------|--------------------------------------------
* 2026-10-02 | golden-case | Initial version
*-----------------------------------------------------------------------------
$PACKAGE GOLDEN.Legacy
    SUBROUTINE V.GOLDEN.BEFORE.AUTH
    $INSERT I_COMMON
    $INSERT I_EQUATE
    $INSERT I_F.CUSTOMER

    R.NEW(EB.CUS.MNEMONIC) = 'SAMPLE'
    RETURN
END
