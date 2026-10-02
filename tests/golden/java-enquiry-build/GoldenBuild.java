package com.temenos.t24.custom.golden;
// Implements: Enquiry from EB_EnquiryHook.jar
// T24 Application: CUSTOMER
// Hook type: Enquiry.setFilterCriteria (BUILD.ROUTINE)

import java.util.List;

import com.temenos.t24.api.complex.eb.enquiryhook.EnquiryContext;
import com.temenos.t24.api.complex.eb.enquiryhook.FilterCriteria;
import com.temenos.t24.api.hook.system.Enquiry;

public class GoldenBuild extends Enquiry {

    @Override
    public List<FilterCriteria> setFilterCriteria(List<FilterCriteria> filterCriteria, EnquiryContext enquiryContext) {
        FilterCriteria criteria = new FilterCriteria();
        criteria.setFieldname("SECTOR");
        criteria.setOperand("EQ");
        criteria.setValue("1001");
        filterCriteria.add(criteria);
        return filterCriteria;
    }
}
