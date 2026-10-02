*-----------------------------------------------------------------------------
* Program    : V.GOLDEN.VVR
* Type       : VVR
* Description: Golden case
* Application: CUSTOMER
*
* Modification History:
* Date       | Author          | Description
* -----------|-----------------|--------------------------------------------
* 2026-10-02 | golden-case | Initial version
*-----------------------------------------------------------------------------
$PACKAGE GOLDEN.Legacy
    SUBROUTINE V.GOLDEN.VVR
    $INSERT I_COMMON
    $INSERT I_EQUATE
    $INSERT I_F.CUSTOMER

    IF AF NE EB.CUS.MNEMONIC THEN RETURN
    IF COMI EQ '' THEN
        ETEXT = 'MNEMONIC IS MANDATORY'
        CALL STORE.END.ERROR
    END
    RETURN
END
