from opentelemetry.sdk.resources import Resource
from opentelemetry import trace

from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter

from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.sqlalchemy import SQLAlchemyInstrumentor

def setup_telemetry(app, engine):
    resource = Resource.create({
        "service.name": "product-inventory",
        "service.version": "1.0.0",
        "service.environment": "development"
    })

    trace_provider = TracerProvider(
        resource=resource
    )

    oltp_exporter = OTLPSpanExporter(
        endpoint="otel-collector:4317",
        insecure=True
    )

    trace_provider.add_span_processor(
        BatchSpanProcessor(oltp_exporter)
    )

    trace.set_tracer_provider(tracer_provider=trace_provider)

    FastAPIInstrumentor.instrument_app(app)

    SQLAlchemyInstrumentor().instrument(
        engine=engine
    )