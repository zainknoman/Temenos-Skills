package {{JAVA_PACKAGE}};
// Implements: Enquiry from EB_EnquiryHook.jar
// T24 Application: {{APP}}
// Hook type: Enquiry.setFilterCriteria (BUILD.ROUTINE)

import java.util.List;

import com.temenos.t24.api.complex.eb.enquiryhook.EnquiryContext;
import com.temenos.t24.api.complex.eb.enquiryhook.FilterCriteria;
import com.temenos.t24.api.hook.system.Enquiry;

public class {{CLASS_NAME}} extends Enquiry {

    @Override
    public List<FilterCriteria> setFilterCriteria(List<FilterCriteria> filterCriteria, EnquiryContext enquiryContext) {
        FilterCriteria criteria = new FilterCriteria();
        criteria.setFieldname("{{FIELD_NAME}}");
        criteria.setOperand("EQ");
        criteria.setValue("{{FILTER_VALUE}}");
        filterCriteria.add(criteria);
        return filterCriteria;
    }
}
