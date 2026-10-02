package {{JAVA_PACKAGE}};
// Implements: Enquiry from EB_EnquiryHook.jar
// T24 Application: {{APP}}
// Hook type: Enquiry.setValue (CONVERSION)

import java.util.List;

import com.temenos.api.TStructure;
import com.temenos.t24.api.complex.eb.enquiryhook.EnquiryContext;
import com.temenos.t24.api.complex.eb.enquiryhook.FilterCriteria;
import com.temenos.t24.api.hook.system.Enquiry;

public class {{CLASS_NAME}} extends Enquiry {

    @Override
    public String setValue(String value, String currentId, TStructure currentRecord,
            List<FilterCriteria> filterCriteria, EnquiryContext enquiryContext) {

        if (value == null || value.isEmpty()) {
            return "{{EMPTY_TEXT}}";
        }
        return value;
    }
}
