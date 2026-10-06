*-----------------------------------------------------------------------------
* Program    : {{ROUTINE_NAME}}
* Type       : BATCH record routine
* Description: {{DESCRIPTION}}
* Application: {{APP}}
*
* Modification History:
* Date       | Author          | Description
* -----------|-----------------|--------------------------------------------
* {{TODAY}} | {{AUTHOR}} | Initial version
*-----------------------------------------------------------------------------
$PACKAGE {{PACKAGE}}
SUBROUTINE {{ROUTINE_NAME}}(recordId)
    $INSERT I_{{ROUTINE_NAME}}.COMMON
    $USING EB.DataAccess
    $USING {{APP_COMPONENT}}

    record = ''
    readErr = ''
    EB.DataAccess.FRead(fnApp, recordId, record, fApp, readErr)
    IF readErr NE '' THEN RETURN
    IF record<{{FIELD}}> NE '{{SELECT_VALUE}}' THEN RETURN

*   Record-level processing goes here.
    CRT '{{ROUTINE_NAME}}: ':recordId
RETURN
END
