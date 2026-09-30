import logging

from opentelemetry import trace
from opentelemetry._logs import set_logger_provider

from opentelemetry.sdk._logs import(
    LoggerProvider,
    LoggingHandler
)

from opentelemetry.exporter.otlp.proto.grpc._log_exporter import (
    OTLPLogExporter,
)

from opentelemetry.sdk._logs.export import(
    BatchLogRecordProcessor,
)

from opentelemetry.sdk.resources import Resource

def setup_logging():

    resource = Resource.create({
        "service.name": "product-inventory",
        "service.version": "1.0.0",
        "service.enivornment": "development",
    })

    logger_provider = LoggerProvider(
        resource=resource
    )

    exporter = OTLPLogExporter(
        endpoint="otel-collector:4317",
        insecure=True
    )

    logger_provider.add_log_record_processor(
        BatchLogRecordProcessor(exporter=exporter)
    )

    set_logger_provider(logger_provider=logger_provider)

    handler = LoggingHandler(
        level=logging.INFO,
        logger_provider=logger_provider
    )

    logging.basicConfig(
        level=logging.INFO,
        handlers=[handler],
    )