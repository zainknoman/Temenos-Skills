*-----------------------------------------------------------------------------
* Program    : GOLDEN.OFS.UPDATE
* Type       : OFS
* Description: Golden case
* Application: CUSTOMER
*
* Modification History:
* Date       | Author          | Description
* -----------|-----------------|--------------------------------------------
* 2026-10-02 | golden-case | Initial version
*-----------------------------------------------------------------------------
$PACKAGE GOLDEN.Legacy
    SUBROUTINE GOLDEN.OFS.UPDATE(Y.RECORD.ID, Y.NEW.VALUE)
    $INSERT I_COMMON
    $INSERT I_EQUATE

    OFS.SOURCE.ID = 'TEST.OFS'
    OFS.REC = 'CUSTOMER,GOLDEN.OFS/I/PROCESS,//':ID.COMPANY:',':Y.RECORD.ID:',SECTOR:1:1=':Y.NEW.VALUE
    OFS.MSG.ID = ''
    OPTIONS = ''
    CALL OFS.POST.MESSAGE(OFS.REC, OFS.MSG.ID, OFS.SOURCE.ID, OPTIONS)
    RETURN
END
