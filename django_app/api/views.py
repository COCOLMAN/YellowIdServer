from rest_framework import views
from rest_framework.response import Response


class KeyAPIView(views.APIView):
    def get(self, request, *args, **kwargs):
        ret = {}
        ret['type'] = 'buttons'
        ret['buttons'] = ['소마']
        print(ret)
        return Response(ret)
