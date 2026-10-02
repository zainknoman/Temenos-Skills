*-----------------------------------------------------------------------------
* Program    : {{ROUTINE_NAME}}
* Type       : OFS
* Description: {{DESCRIPTION}}
* Application: {{APP}}
*
* Modification History:
* Date       | Author          | Description
* -----------|-----------------|--------------------------------------------
* {{TODAY}} | {{AUTHOR}} | Initial version
*-----------------------------------------------------------------------------
$PACKAGE {{PACKAGE}}
    SUBROUTINE {{ROUTINE_NAME}}(Y.RECORD.ID, Y.NEW.VALUE)
    $INSERT I_COMMON
    $INSERT I_EQUATE

    OFS.SOURCE.ID = '{{OFS_SOURCE}}'
    OFS.REC = '{{APP}},{{VERSION_NAME}}/I/PROCESS,//':ID.COMPANY:',':Y.RECORD.ID:',{{FIELD_NAME}}:1:1=':Y.NEW.VALUE
    OFS.MSG.ID = ''
    OPTIONS = ''
    CALL OFS.POST.MESSAGE(OFS.REC, OFS.MSG.ID, OFS.SOURCE.ID, OPTIONS)
    RETURN
END
