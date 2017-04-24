import urllib
from bs4 import BeautifulSoup as bs

from rest_framework import views
from rest_framework.response import Response


class KeyAPIView(views.APIView):
    def get(self, request, *args, **kwargs):
        ret = {}
        ret['type'] = 'buttons'
        ret['buttons'] = ['소마']
        print(ret)
        return Response(ret)


class CheckAPIView(views.APIView):
    def post(self, request, *args, **kwargs):
        ret = {
            'message':{
                'text': '??'
            }
        }
        if '소마' == request.data['content']:
            data = urllib.request.urlopen("http://www.swmaestro.kr/web/web/recruitment/applicationGuide.do")
            s_data = bs(data)
            if '2016' in s_data.findAll('p')[3].text:
                text = '변화없음(2016년 버전)\n'
                text += s_data.findAll('p')[3].text
                ret['message']['text'] = text
                return Response(ret)
            else:
                ret['message']['text'] = '변화있음 홈페이지에서 확인바랍니다.'
                return Response(ret)
        return Response(ret)
