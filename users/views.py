from rest_framework.views import APIView
from api.serializers import UserSerializer
from rest_framework.response import Response

class CurrentUser(APIView):
    def get(self,request):
        context = {
            'username':self.request.user.username ,
             "email":self.request.user.email,
                   }
        return Response(context)