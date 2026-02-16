from rest_framework import viewsets
from rest_framework import status
from rest_framework import response as Response
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

    # Request and Response both custom
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
              "Date_created" : result["date_created"]
            },
            status = status.HTTP_201_CREATED
        )
    
    def update(self, request, *args, **kwargs):
      partial = kwargs.pop('partial', False)
      instance = self.get_object()
      incoming_data = {
          "id" : request.data.get("todo_id"),
          "name" : request.data.get("todo"),
          "done" : request.data.get("done")
      }
      serializer = self.get_serializer(instance, data = incoming_data, partial = partial)
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

    # Only response is custom
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
    
    def get_queryset(self):
        queryset = super().get_queryset()
        user_id = self.request.query_params.get("user_id")
        if user_id:
            queryset = queryset.filter(user = user_id)
        return queryset
    
    
    

        




