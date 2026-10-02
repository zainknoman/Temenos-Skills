package com.temenos.t24.custom.golden;
// Implements: PaymentOrderLifecycle from PI_PaymentOrderLifecycleHook.jar
// T24 Application: PAYMENT.ORDER
// Hook type: PaymentOrderLifecycle.validatePaymentOrderRecord

import com.temenos.api.TValidationResponse;
import com.temenos.t24.api.complex.pi.paymentorderlifecyclehook.PaymentOrderValidationContext;
import com.temenos.t24.api.hook.payments.PaymentOrderLifecycle;
import com.temenos.t24.api.records.paymentorder.PaymentOrderRecord;

public class GoldenPaymentOrderCheck extends PaymentOrderLifecycle {

    @Override
    public TValidationResponse validatePaymentOrderRecord(String paymentOrderId, PaymentOrderRecord paymentOrderRecord,
            PaymentOrderValidationContext paymentOrderValidationContext) {

        String value = paymentOrderRecord.getDebitAccount().getValue();
        if (value == null || value.isEmpty()) {
            paymentOrderRecord.getDebitAccount().setError("DEBIT ACCOUNT IS MANDATORY");
        }
        return paymentOrderRecord.getValidationResponse();
    }
}
