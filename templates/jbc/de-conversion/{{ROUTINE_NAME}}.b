*-----------------------------------------------------------------------------
* Program    : {{ROUTINE_NAME}}
* Type       : DE CONVERSION
* Description: {{DESCRIPTION}}
* Application: {{APP}}
*
* Modification History:
* Date       | Author          | Description
* -----------|-----------------|--------------------------------------------
* {{TODAY}} | {{AUTHOR}} | Initial version
*-----------------------------------------------------------------------------
$PACKAGE {{PACKAGE}}
SUBROUTINE {{ROUTINE_NAME}}(inValue, headerRec, mvNo, outValue, errorMsg)
    $USING {{APP_COMPONENT}}

    outValue = ''
    errorMsg = ''
    IF inValue EQ '' THEN RETURN
    readErr = ''
    record = {{APP_COMPONENT}}.{{APP_RECORD}}.Read(inValue, readErr)
    IF readErr EQ '' THEN
        outValue = record<{{FIELD}}>
    END
RETURN
END
