import structlog


def configure_structlog(is_debug: bool):
    shared_processors = [
        # Processors that have nothing to do with output,
        # e.g., add timestamps or log level names.
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.TimeStamper("iso", utc=False),
        structlog.processors.UnicodeDecoder(),
    ]

    if is_debug:
        # Pretty printing when we run in a terminal session.
        # Automatically prints pretty tracebacks when "rich" is installed
        processors = shared_processors + [
            structlog.processors.ExceptionPrettyPrinter(),
            structlog.dev.ConsoleRenderer(),
        ]
    else:
        # Print JSON when we run, e.g., in a Docker container.
        # Also print structured tracebacks.
        processors = shared_processors + [
            structlog.processors.dict_tracebacks,
            structlog.processors.JSONRenderer(),
        ]

    structlog.configure(processors)


def get_logger(name: str, is_debug: bool):
    configure_structlog(is_debug)
    return structlog.get_logger(name)
