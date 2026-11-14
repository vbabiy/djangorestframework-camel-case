from django.conf import settings


def pytest_configure():
    settings.configure(
        REST_FRAMEWORK={
            "DEFAULT_RENDERER_CLASSES": (
                "djangorestframework_camel_case.render.CamelCaseJSONRenderer",
                "djangorestframework_camel_case.render.CamelCaseBrowsableAPIRenderer",
            )
        },
        JSON_CAMEL_CASE={
            "RENDERER_CLASS": "tests.render.SimpleCustomRenderer",
            "PARSER_CLASS": "tests.parser.SimpleCustomParser",
        },
    )
