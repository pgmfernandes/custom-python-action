import jsonpickle


class ConfigPipeline:

    @staticmethod
    def parse_from_json(json_content):
        obj = jsonpickle.decode(json_content)
        return obj
