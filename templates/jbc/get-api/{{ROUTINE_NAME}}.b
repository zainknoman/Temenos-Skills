*-----------------------------------------------------------------------------
* Program    : {{ROUTINE_NAME}}
* Type       : GET
* Description: {{DESCRIPTION}}
* Application: {{APP}}
*
* Modification History:
* Date       | Author          | Description
* -----------|-----------------|--------------------------------------------
* {{TODAY}} | {{AUTHOR}} | Initial version
*-----------------------------------------------------------------------------
$PACKAGE {{PACKAGE}}
SUBROUTINE {{ROUTINE_NAME}}(recordId, fieldValue)
    $USING {{APP_COMPONENT}}

    fieldValue = ''
    readErr = ''
    record = {{APP_COMPONENT}}.{{APP_RECORD}}.Read(recordId, readErr)
    IF readErr EQ '' THEN
        fieldValue = record<{{FIELD}}>
    END
RETURN
END
