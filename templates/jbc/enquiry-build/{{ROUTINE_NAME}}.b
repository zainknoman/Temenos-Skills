*-----------------------------------------------------------------------------
* Program    : {{ROUTINE_NAME}}
* Type       : ENQUIRY BUILD.ROUTINE
* Description: {{DESCRIPTION}}
* Application: {{APP}}
*
* Modification History:
* Date       | Author          | Description
* -----------|-----------------|--------------------------------------------
* {{TODAY}} | {{AUTHOR}} | Initial version
*-----------------------------------------------------------------------------
$PACKAGE {{PACKAGE}}
SUBROUTINE {{ROUTINE_NAME}}(enqData)

    enqData<2,-1> = '{{FIELD_NAME}}'
    enqData<3,-1> = 'EQ'
    enqData<4,-1> = '{{FILTER_VALUE}}'
RETURN
END
