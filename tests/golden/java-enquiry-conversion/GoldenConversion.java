package com.temenos.t24.custom.golden;
// Implements: Enquiry from EB_EnquiryHook.jar
// T24 Application: CUSTOMER
// Hook type: Enquiry.setValue (CONVERSION)

import java.util.List;

import com.temenos.api.TStructure;
import com.temenos.t24.api.complex.eb.enquiryhook.EnquiryContext;
import com.temenos.t24.api.complex.eb.enquiryhook.FilterCriteria;
import com.temenos.t24.api.hook.system.Enquiry;

public class GoldenConversion extends Enquiry {

    @Override
    public String setValue(String value, String currentId, TStructure currentRecord,
            List<FilterCriteria> filterCriteria, EnquiryContext enquiryContext) {

        if (value == null || value.isEmpty()) {
            return "NOT SET";
        }
        return value;
    }
}
