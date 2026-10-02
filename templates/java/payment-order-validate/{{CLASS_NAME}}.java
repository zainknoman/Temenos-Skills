package {{JAVA_PACKAGE}};
// Implements: PaymentOrderLifecycle from PI_PaymentOrderLifecycleHook.jar
// T24 Application: {{APP}}
// Hook type: PaymentOrderLifecycle.validatePaymentOrderRecord

import com.temenos.api.TValidationResponse;
import com.temenos.t24.api.complex.pi.paymentorderlifecyclehook.PaymentOrderValidationContext;
import com.temenos.t24.api.hook.payments.PaymentOrderLifecycle;
import com.temenos.t24.api.records.paymentorder.PaymentOrderRecord;

public class {{CLASS_NAME}} extends PaymentOrderLifecycle {

    @Override
    public TValidationResponse validatePaymentOrderRecord(String paymentOrderId, PaymentOrderRecord paymentOrderRecord,
            PaymentOrderValidationContext paymentOrderValidationContext) {

        String value = paymentOrderRecord.get{{FIELD}}().getValue();
        if (value == null || value.isEmpty()) {
            paymentOrderRecord.get{{FIELD}}().setError("{{ERROR_TEXT}}");
        }
        return paymentOrderRecord.getValidationResponse();
    }
}
