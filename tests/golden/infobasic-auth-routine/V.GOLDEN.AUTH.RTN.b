*-----------------------------------------------------------------------------
* Program    : V.GOLDEN.AUTH.RTN
* Type       : AUTH.ROUTINE
* Description: Golden case
* Application: CUSTOMER
*
* Modification History:
* Date       | Author          | Description
* -----------|-----------------|--------------------------------------------
* 2026-10-02 | golden-case | Initial version
*-----------------------------------------------------------------------------
$PACKAGE GOLDEN.Legacy
    SUBROUTINE V.GOLDEN.AUTH.RTN
    $INSERT I_COMMON
    $INSERT I_EQUATE
    $INSERT I_F.CUSTOMER

    FN.LOG = 'F.SAMPLE.AUDIT.LOG'
    F.LOG = ''
    CALL OPF(FN.LOG, F.LOG)

    R.LOG = ''
    R.LOG<1> = R.NEW(EB.CUS.SECTOR)
    R.LOG<2> = TODAY
    R.LOG<3> = OPERATOR
    CALL F.WRITE(FN.LOG, ID.NEW, R.LOG)
    RETURN
END
