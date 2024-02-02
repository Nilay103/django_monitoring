from rest_framework.renderers import JSONRenderer


class CustomRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        # Customize the response format here if needed
        # For example, add a 'status' field to the response
        response_data = {
            'status': 'success',
            'data': data,
        }
        return super().render(response_data, accepted_media_type, renderer_context)
    