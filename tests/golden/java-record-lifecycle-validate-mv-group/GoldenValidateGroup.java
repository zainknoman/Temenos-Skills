package com.temenos.t24.custom.golden;
// Implements: RecordLifecycle from EB_TemplateHook.jar
// T24 Application: CUSTOMER
// Hook type: RecordLifecycle

import com.temenos.api.TStructure;
import com.temenos.api.TValidationResponse;
import com.temenos.t24.api.complex.eb.templatehook.TransactionContext;
import com.temenos.t24.api.hook.system.RecordLifecycle;
import com.temenos.t24.api.records.customer.CustomerRecord;
import com.temenos.t24.api.records.customer.RelationCodeClass;

public class GoldenValidateGroup extends RecordLifecycle {

    @Override
    public TValidationResponse validateRecord(String application, String currentRecordId,
            TStructure currentRecord, TStructure unauthorisedRecord,
            TStructure liveRecord, TransactionContext transactionContext) {

        CustomerRecord rec = new CustomerRecord(currentRecord);
        String value = (rec.getRelationCode().isEmpty() ? "" : rec.getRelationCode(0).getRelCustomer().getValue());
        if (value == null || value.isEmpty()) {
            if (rec.getRelationCode().isEmpty()) {
                rec.setRelationCode(new RelationCodeClass(), 0);
            }
            rec.getRelationCode(0).getRelCustomer().setError("RELATED CUSTOMER IS MANDATORY");
        }
        currentRecord.set(rec.toStructure());
        return rec.getValidationResponse();
    }
}
