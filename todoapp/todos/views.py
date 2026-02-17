from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .models import Todo

from .serializers import TodoApiSerializer

class TodoAPIViewSet(viewsets.ModelViewSet):
    """
        success response for create/update/get
        {
          "name": "",
          "done": true/false,
          "date_created": ""
        }

        success response for list
        [
          {
            "name": "",
            "done": true/false,
            "date_created": ""
          }
        ]
    """
    queryset = Todo.objects.all()
    serializer_class = TodoApiSerializer

    # localhost:8000/api/todos/todos/ - POST
    def create(self, request, *args, **kwargs):
        incoming_data = {
            "name" : request.data.get("todo"),
            "user" : request.data.get("user_id"),
        }

        serializer = self.get_serializer(data = incoming_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        result = serializer.data
        return Response(
            {
              "name" : result["name"],
              "done" : result["done"],
              "date_created" : result["date_created"]
            },
            status = status.HTTP_201_CREATED
        )
    
    # localhost:8000/api/todos/todos/1/ - PUT
    def update(self, request, *args, **kwargs):
        # partial = kwargs.pop('partial', True)
        instance = self.get_object()
        incoming_data = {
            "id" : request.data.get("todo_id"),
            "name" : request.data.get("todo"),
            "done" : request.data.get("done")
        }
        # In get serializer I need to send user field so set partial to false as not extracting user anywhere
        serializer = self.get_serializer(instance, data = incoming_data, partial = True)
        serializer.is_valid(raise_exception = True)
        serializer.save()

        result = serializer.data
        return Response(
            {
                "todo_id" : result["id"],
                "todo" : result["name"],
                "done" : result["done"]
            },
            status = status.HTTP_200_OK
        )

    # localhost:8000/api/todos/todos/12/- GET
    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        return Response(
            {
                "todo_id": response.data["id"],
                "todo" : response.data["name"],
                "done" : response.data["done"]
            },
            status = response.status_code
        )
    
    # localhost:8000/api/todos/todos/?user_id=6 - GET
    def get_queryset(self):
        queryset = super().get_queryset()
        user_id = self.request.query_params.get("user_id")
        if user_id:
            queryset = queryset.filter(user = user_id)
        return queryset
    
    
    

        




