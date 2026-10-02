package com.temenos.t24.custom.golden;
// Implements: RecordLifecycle from EB_TemplateHook.jar
// T24 Application: FUNDS.TRANSFER
// Hook type: RecordLifecycle.isOverrideAutoApprove

import com.temenos.api.TBoolean;
import com.temenos.api.TStructure;
import com.temenos.t24.api.complex.eb.templatehook.ErrorText;
import com.temenos.t24.api.complex.eb.templatehook.TransactionContext;
import com.temenos.t24.api.hook.system.RecordLifecycle;

public class GoldenOverride extends RecordLifecycle {

    @Override
    public TBoolean isOverrideAutoApprove(String application, String currentRecordId, TStructure currentRecord,
            TransactionContext transactionContext, ErrorText errorText) {

        return new TBoolean("SAMPLE.OVERRIDE".equals(errorText.getId()));
    }
}
