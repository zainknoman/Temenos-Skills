*-----------------------------------------------------------------------------
* Program    : {{ROUTINE_NAME}}
* Type       : ENQUIRY CONVERSION
* Description: {{DESCRIPTION}}
* Application: {{APP}}
*
* Modification History:
* Date       | Author          | Description
* -----------|-----------------|--------------------------------------------
* {{TODAY}} | {{AUTHOR}} | Initial version
*-----------------------------------------------------------------------------
$PACKAGE {{PACKAGE}}
SUBROUTINE {{ROUTINE_NAME}}
    $USING EB.Reports
    $USING {{APP_COMPONENT}}

    recordId = EB.Reports.getOData()
    IF recordId EQ '' THEN RETURN
    readErr = ''
    record = {{APP_COMPONENT}}.{{APP_RECORD}}.Read(recordId, readErr)
    IF readErr EQ '' THEN
        EB.Reports.setOData(record<{{FIELD}}>)
    END ELSE
        EB.Reports.setOData('')
    END
RETURN
END
