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
    SUBROUTINE {{ROUTINE_NAME}}(ENQ.DATA)
    $INSERT I_COMMON
    $INSERT I_EQUATE
    $INSERT I_ENQUIRY.COMMON

    ENQ.DATA<2,-1> = '{{FIELD_NAME}}'
    ENQ.DATA<3,-1> = 'EQ'
    ENQ.DATA<4,-1> = '{{FILTER_VALUE}}'
    RETURN
END
