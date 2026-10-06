*-----------------------------------------------------------------------------
* Program    : B.GOLDEN.SERVICE
* Type       : BATCH record routine
* Description: Golden case
* Application: CUSTOMER
*
* Modification History:
* Date       | Author          | Description
* -----------|-----------------|--------------------------------------------
* 2026-10-02 | golden-case | Initial version
*-----------------------------------------------------------------------------
$PACKAGE GOLDEN.Legacy
    SUBROUTINE B.GOLDEN.SERVICE(Y.ID)
    $INSERT I_COMMON
    $INSERT I_EQUATE
    $INSERT I_F.CUSTOMER
    $INSERT I_B.GOLDEN.SERVICE.COMMON

    R.APP = ''
    Y.READ.ERR = ''
    CALL F.READ(FN.APP, Y.ID, R.APP, F.APP, Y.READ.ERR)
    IF Y.READ.ERR NE '' THEN RETURN
    IF R.APP<EB.CUS.SECTOR> NE '1001' THEN RETURN

    GOSUB PROCESS.RECORD
    RETURN

PROCESS.RECORD:
*   Record-level processing goes here.
    CRT 'B.GOLDEN.SERVICE: ':Y.ID
    RETURN
END
