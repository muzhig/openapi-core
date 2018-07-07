"""OpenAPI core properties generators module"""
from six import iteritems


class PropertiesGenerator(object):

    def __init__(self, dereferencer):
        self.dereferencer = dereferencer

    def generate(self, properties, in_request_body=False):
        for property_name, schema_spec in iteritems(properties):
            schema = self._create_schema(schema_spec, in_request_body)
            yield property_name, schema

    def _create_schema(self, schema_spec, in_request_body=False):
        from openapi_core.schema.schemas.factories import SchemaFactory
        return SchemaFactory(self.dereferencer).create(schema_spec, in_request_body=in_request_body)
