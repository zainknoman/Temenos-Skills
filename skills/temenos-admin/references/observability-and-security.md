# Observability & Security Reference

Source: `TAFJ_HOME/TemnMonitor`, `TAFJ_HOME/TemnXACML`, verified 2026-07-31.

## TemnMonitor — bundled observability stack

`TAFJ_HOME/TemnMonitor/` ships a full, ready-to-launch monitoring stack (real
directories present, not a stub):

| Component | Directory |
|---|---|
| Elasticsearch | `elasticsearch/` |
| Grafana | `grafana/` |
| Helm charts | `helm/` |
| InfluxDB | `influxdb/` |
| Jaeger (distributed tracing) | `jaeger/` |
| Logstash | `logstash/` |
| OpenTelemetry | `opentelemetry/` |
| Prometheus | `prometheus/` |
| Pushgateway | `pushgateway/` |
| Splunk | `splunk/` |
| Source | `src/` |

Launch via `docker-compose-monitoring.yml` (root of `TemnMonitor/`), or the
provided `launch-monitoring.bat` / `launch-monitoring.sh`. Config lives in
`.env`. See `TemnMonitor/README.txt` and `README-vagrant.txt` for the
authoritative setup steps — don't guess at compose service names, read the
actual `docker-compose-monitoring.yml`.

This confirms T24/TAFJ has first-class support for a modern OTel-based
observability pipeline (traces via Jaeger/OpenTelemetry, metrics via
Prometheus/Grafana/InfluxDB, logs via ELK/Splunk) — relevant when a developer
asks how to instrument or monitor a T24 estate rather than just customise it.

## TemnXACML — entitlements / authorisation

`TAFJ_HOME/TemnXACML/` provides XACML-based authorisation:

- `authz-decision-adapter-3.0.5.zip` (+ `authz/` extracted dir) — the
  authorisation decision adapter.
- `authz-t24-external-3.0.5.zip` — external T24 authorisation integration.
- `SMS2XACML_Generator.zip` (+ extracted dir) — generates XACML policies from
  T24 SMS (Security Management System) definitions, i.e. converts T24's
  native entitlements model into XACML policy form.
- `transact-authz/` — Transact-specific authorisation module.

This is the mechanism to reach for when a request involves converting T24
SMS-defined entitlements into an external policy-decision-point model, or
integrating T24 authorisation with an external XACML PDP. Don't confuse this
with `bnk/Extensions/EB_AuthorizationService` or
`EB_AuthenticationService` (see `temenos-integration` skill) — those are
service-extension modules; TemnXACML is the policy-translation layer.

## Related security PDFs

In `docs/TAFJ-DevSecOps/` (not duplicated here — see `temenos-devsecops`
skill): `TAFJ-Secure-Authentication-Using-Keycloak.pdf`,
`TAFJ-Kerberos_setup.pdf`, `TAFJ-MultiTenant.pdf`.
