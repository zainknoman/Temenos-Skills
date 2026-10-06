*-----------------------------------------------------------------------------
* Program    : GOLDEN.AA.GET.STATUS
* Type       : AA GETTER
* Description: Golden case
* Application: AA.ARRANGEMENT
*
* Modification History:
* Date       | Author          | Description
* -----------|-----------------|--------------------------------------------
* 2026-10-02 | golden-case | Initial version
*-----------------------------------------------------------------------------
$PACKAGE GOLDEN.Legacy
    SUBROUTINE GOLDEN.AA.GET.STATUS(ARRANGEMENT.ID, RET.VALUE, RET.ERR)
    $INSERT I_COMMON
    $INSERT I_EQUATE
    $INSERT I_F.AA.ARRANGEMENT

    RET.VALUE = ''
    RET.ERR = ''
    FN.ARR = 'F.AA.ARRANGEMENT'
    F.ARR = ''
    CALL OPF(FN.ARR, F.ARR)
    R.ARR = ''
    CALL F.READ(FN.ARR, ARRANGEMENT.ID, R.ARR, F.ARR, RET.ERR)
    IF RET.ERR NE '' THEN RETURN
    RET.VALUE = R.ARR<AA.ARR.ARR.STATUS>
    RETURN
END
